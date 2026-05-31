#!/usr/bin/env python
"""Build page-level transcript HTML and a client-side search index.

The page scans remain the primary publication surface. This script extracts a
literal secondary text layer from the canonical DOCX and aligns it to the
already-rendered page manifest.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import zipfile
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def paragraph_text(paragraph: ET.Element) -> str:
    parts: list[str] = []
    for node in paragraph.iter():
        name = local_name(node.tag)
        if name == "t":
            parts.append(node.text or "")
        elif name == "tab":
            parts.append("\t")
        elif name == "br" and node.attrib.get(W + "type") != "page":
            parts.append("\n")
    return "".join(parts).strip()


def table_text(table: ET.Element) -> str:
    rows: list[str] = []
    for row in table.findall(".//" + W + "tr"):
        cells: list[str] = []
        for cell in row.findall(W + "tc"):
            paragraphs = [paragraph_text(p) for p in cell.findall(".//" + W + "p")]
            cell_text = " ".join(p for p in paragraphs if p).strip()
            cells.append(cell_text)
        if any(cells):
            rows.append("\t".join(cells).rstrip())
    return "\n".join(rows).strip()


def block_text(block: ET.Element) -> str:
    if local_name(block.tag) == "tbl":
        return table_text(block)
    return paragraph_text(block)


def has_last_rendered_page_break(block: ET.Element) -> bool:
    return any(True for _ in block.iter(W + "lastRenderedPageBreak"))


def has_page_break(block: ET.Element) -> bool:
    return any(br.attrib.get(W + "type") == "page" for br in block.iter(W + "br"))


def has_section_break(block: ET.Element) -> bool:
    return any(True for _ in block.iter(W + "sectPr"))


def extract_docx_pages(docx_path: Path) -> list[str]:
    with zipfile.ZipFile(docx_path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))

    body = root.find(W + "body")
    if body is None:
        raise RuntimeError("DOCX document body could not be found.")

    pages: list[str] = []
    current: list[str] = []

    for block in list(body):
        text = block_text(block)

        # Word stores some rendered page break markers inside the first block of
        # the next page. When that happens, split before adding the block text.
        if has_last_rendered_page_break(block) and current:
            pages.append("\n\n".join(current).strip())
            current = []

        if text:
            current.append(text)

        # Manual page breaks and section breaks usually close the current page.
        if (has_page_break(block) or has_section_break(block)) and current:
            pages.append("\n\n".join(current).strip())
            current = []

    if current:
        pages.append("\n\n".join(current).strip())

    return pages


def excerpt(text: str, limit: int = 280) -> str:
    value = collapse(text)
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def page_filename(index: int) -> str:
    return f"page-{index:03d}.html"


def render_transcript_index(manifest: list[dict[str, object]], search_index: list[dict[str, object]]) -> str:
    pages = "\n".join(
        f"""        <li>
          <a href="{html.escape(str(item['full_text_path']))}">
            <strong>{html.escape(str(item['page_label']))}</strong>
            <span>{html.escape(str(item['title']))}</span>
          </a>
        </li>"""
        for item in search_index
    )
    return f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Transcript</title>
  <link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
  <header class="site-header compact">
    <p class="kicker"><a href="index.html">Ana sayfa</a></p>
    <h1>Transcript</h1>
    <p class="lead">
      Bu katman, sayfa görsellerini değiştirmeyen sayfa bazlı metin erişimidir.
      Arama sonuçları ilgili transcript sayfasına ve oradan sayfa görüntüsüne bağlanır.
    </p>
  </header>

  <main class="page" data-search-root>
    <section class="panel">
      <h2>Arama</h2>
      <label class="search-field">
        <span>Transcript içinde ara</span>
        <input type="search" data-search-input placeholder="Örn. bakım, operasyon, Makale Ödevi 2">
      </label>
      <p class="search-count" data-search-count>{len(manifest)} sayfa aranabilir.</p>
      <div class="search-results" data-search-results></div>
    </section>

    <section class="panel">
      <h2>Sayfa Listesi</h2>
      <ol class="transcript-list">
{pages}
      </ol>
    </section>

    <section class="panel">
      <h2>Kalite Notu</h2>
      <p>
        Transcript DOCX metin katmanından sayfa kırılım sinyalleri korunarak çıkarılmıştır.
        Görsel sayfa taramaları birincil doğruluk kaynağıdır.
      </p>
    </section>
  </main>

  <script src="assets/js/viewer.js"></script>
</body>
</html>
"""


def render_page(item: dict[str, object], text: str, prev_path: str | None, next_path: str | None) -> str:
    page_label = html.escape(str(item["page_label"]))
    title = html.escape(str(item["title"]))
    section = html.escape(str(item["section"]))
    scan_path = html.escape("../" + str(item["scan_path"]))
    prev_link = f'<a href="{html.escape(prev_path)}">Önceki transcript</a>' if prev_path else '<span>Önceki yok</span>'
    next_link = f'<a href="{html.escape(next_path)}">Sonraki transcript</a>' if next_path else '<span>Sonraki yok</span>'
    return f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page_label} - {title}</title>
  <link rel="stylesheet" href="../assets/css/main.css">
</head>
<body>
  <header class="site-header compact">
    <p class="kicker"><a href="../transcript.html">Transcript</a></p>
    <h1>{page_label}: {title}</h1>
    <p class="lead">{section}</p>
  </header>

  <main class="page">
    <nav class="panel transcript-nav" aria-label="Transcript gezinme">
      <a href="{scan_path}">Sayfa görüntüsüne git</a>
      {prev_link}
      {next_link}
    </nav>

    <article class="panel transcript-page">
      <h2>Literal Transcript</h2>
      <pre>{html.escape(text)}</pre>
    </article>
  </main>
</body>
</html>
"""


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docx", default=str(root / "EK-10_Siemens_Staj_Makale_Analizleri.docx"))
    parser.add_argument("--manifest", default=str(root / "docs" / "data" / "page_manifest.json"))
    parser.add_argument("--out-dir", default=str(root / "docs" / "transcript"))
    parser.add_argument("--search-index", default=str(root / "docs" / "data" / "search_index.json"))
    args = parser.parse_args()

    docx_path = Path(args.docx).resolve()
    manifest_path = Path(args.manifest).resolve()
    out_dir = Path(args.out_dir).resolve()
    search_index_path = Path(args.search_index).resolve()
    log_dir = root / "_work" / "logs"

    if not docx_path.exists():
        raise FileNotFoundError(f"Source DOCX not found: {docx_path}")
    if not manifest_path.exists():
        raise FileNotFoundError(f"Page manifest not found: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pages = extract_docx_pages(docx_path)
    if len(pages) != len(manifest):
        raise RuntimeError(f"Transcript page count mismatch: docx={len(pages)}, manifest={len(manifest)}")

    out_dir.mkdir(parents=True, exist_ok=True)
    search_index_path.parent.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    search_index: list[dict[str, object]] = []
    for index, (page, text) in enumerate(zip(manifest, pages), start=1):
        filename = page_filename(index)
        full_text_path = f"transcript/{filename}"
        scan_anchor = f"page-{index:03d}"
        item = {
            "page_index": page["page_index"],
            "page_label": page["page_label"],
            "title": page["short_title"],
            "section": page["section"],
            "text_excerpt": excerpt(text),
            "full_text_path": full_text_path,
            "scan_path": f"staj-defteri.html#{scan_anchor}",
            "search_text": collapse(text),
        }
        search_index.append(item)
        page["transcript_path"] = full_text_path
        page["alt_text"] = page.get("alt_text") or f"Staj defteri {page['page_label']}: {page['short_title']}"

    for index, (item, text) in enumerate(zip(search_index, pages), start=1):
        prev_path = page_filename(index - 1) if index > 1 else None
        next_path = page_filename(index + 1) if index < len(search_index) else None
        (out_dir / page_filename(index)).write_text(
            render_page(item, text, prev_path, next_path),
            encoding="utf-8",
        )

    (root / "docs" / "transcript.html").write_text(
        render_transcript_index(manifest, search_index),
        encoding="utf-8",
    )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    search_index_path.write_text(json.dumps(search_index, ensure_ascii=False, indent=2), encoding="utf-8")

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "docx": str(docx_path),
        "manifest": str(manifest_path),
        "transcript_pages": len(pages),
        "search_index": str(search_index_path),
        "output_dir": str(out_dir),
    }
    (log_dir / "build_transcript.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
