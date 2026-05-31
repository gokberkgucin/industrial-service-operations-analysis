#!/usr/bin/env python
"""Verify the GitHub Pages publication shell and page-scan assets."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


@dataclass
class Verifier:
    root: Path
    checks: list[CheckResult] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def pass_check(self, name: str, detail: str) -> None:
        self.checks.append(CheckResult(name, "PASS", detail))

    def warn_check(self, name: str, detail: str) -> None:
        self.warnings.append(f"{name}: {detail}")
        self.checks.append(CheckResult(name, "WARN", detail))

    def fail_check(self, name: str, detail: str) -> None:
        self.failures.append(f"{name}: {detail}")
        self.checks.append(CheckResult(name, "FAIL", detail))


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        for attr in ("href", "src"):
            value = data.get(attr)
            if value:
                self.refs.append((tag, attr, value))


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_text_files(root: Path) -> Iterable[Path]:
    for suffix in {".html", ".json", ".css", ".js", ".md", ".txt"}:
        yield from root.glob(f"**/*{suffix}")


def check_manifest(verifier: Verifier) -> tuple[list[dict[str, object]], list[Path]]:
    root = verifier.root
    manifest_path = root / "docs" / "data" / "page_manifest.json"
    pages_dir = root / "docs" / "assets" / "staj" / "pages"

    if not manifest_path.exists():
        verifier.fail_check("manifest exists", "docs/data/page_manifest.json bulunamadı.")
        return [], []
    if not pages_dir.exists():
        verifier.fail_check("pages dir exists", "docs/assets/staj/pages bulunamadı.")
        return [], []

    manifest = load_json(manifest_path)
    if not isinstance(manifest, list):
        verifier.fail_check("manifest format", "Manifest JSON listesi değil.")
        return [], []

    page_files = sorted(pages_dir.glob("page-*.png"))
    manifest_files = [str(item.get("filename", "")) for item in manifest if isinstance(item, dict)]
    expected_files = [f"page-{index:03d}.png" for index in range(1, len(manifest) + 1)]

    if manifest_files != expected_files:
        verifier.fail_check("manifest sequence", f"Manifest dosya sırası beklenen page-001... dizisiyle eşleşmiyor: {manifest_files[:5]} ...")
    else:
        verifier.pass_check("manifest sequence", f"{len(manifest)} manifest kaydı sıralı.")

    asset_files = [p.name for p in page_files]
    if asset_files != expected_files:
        verifier.fail_check("asset sequence", f"Sayfa asset dizisi manifestle eşleşmiyor. Asset: {len(asset_files)}, Manifest: {len(expected_files)}")
    else:
        verifier.pass_check("asset sequence", f"{len(page_files)} PNG sayfa asset'i manifestle eşleşiyor.")

    required = {"page_index", "filename", "page_label", "short_title", "section", "alt_text", "image_path", "transcript_path"}
    missing_fields: list[str] = []
    missing_images: list[str] = []
    for item in manifest:
        if not isinstance(item, dict):
            continue
        missing = required.difference(item.keys())
        if missing:
            missing_fields.append(f"{item.get('filename', '?')}: {', '.join(sorted(missing))}")
        image_path = root / str(item.get("image_path", ""))
        if not image_path.exists():
            missing_images.append(str(item.get("image_path", "")))

    if missing_fields:
        verifier.fail_check("manifest required fields", "; ".join(missing_fields[:10]))
    else:
        verifier.pass_check("manifest required fields", "Tüm manifest kayıtlarında zorunlu alanlar var.")

    if missing_images:
        verifier.fail_check("manifest images", f"Eksik görsel yolları: {missing_images[:10]}")
    else:
        verifier.pass_check("manifest images", "Manifestteki tüm görsel yolları mevcut.")

    return manifest, page_files


def check_html_links(verifier: Verifier) -> None:
    root = verifier.root
    docs = root / "docs"
    html_files = sorted(docs.glob("**/*.html"))
    missing: list[str] = []
    root_absolute: list[str] = []
    local_absolute: list[str] = []
    old_refs: list[str] = []

    for html_file in html_files:
        text = html_file.read_text(encoding="utf-8", errors="replace")
        parser = LinkParser()
        parser.feed(text)
        for tag, attr, ref in parser.refs:
            if ref.startswith(("/", "\\")):
                root_absolute.append(f"{rel(html_file, root)} -> {ref}")
                continue
            if re.match(r"^[A-Za-z]:\\", ref) or ref.startswith("file:"):
                local_absolute.append(f"{rel(html_file, root)} -> {ref}")
                continue
            if ref in {"#"} or ref.startswith(("mailto:", "http://", "https://")):
                continue
            clean = ref.split("#", 1)[0].split("?", 1)[0]
            if clean and not (html_file.parent / clean).exists():
                missing.append(f"{rel(html_file, root)} -> {ref}")

        if "site.css" in text or "site.js" in text:
            old_refs.append(rel(html_file, root))

    if missing:
        verifier.fail_check("relative html links", "; ".join(missing[:20]))
    else:
        verifier.pass_check("relative html links", f"{len(html_files)} HTML dosyasında kırık relative link yok.")

    if root_absolute:
        verifier.fail_check("project-site subpath", f"Root-absolute link bulundu: {root_absolute[:20]}")
    else:
        verifier.pass_check("project-site subpath", "Root-absolute link/src bulunmadı.")

    if local_absolute:
        verifier.fail_check("local absolute paths", f"Yerel absolute path bulundu: {local_absolute[:20]}")
    else:
        verifier.pass_check("local absolute paths", "HTML içinde yerel absolute path yok.")

    if old_refs:
        verifier.fail_check("old css/js refs", f"Eski site.css/site.js referansı var: {old_refs}")
    else:
        verifier.pass_check("old css/js refs", "HTML dosyaları main.css ve viewer.js yapısıyla uyumlu.")


def check_downloads(verifier: Verifier) -> None:
    root = verifier.root
    pdf = root / "docs" / "assets" / "staj" / "originals" / "EK-10_Siemens_Staj_Makale_Analizleri.pdf"
    docx = root / "docs" / "assets" / "staj" / "originals" / "EK-10_Siemens_Staj_Makale_Analizleri.docx"
    missing = [str(p) for p in (pdf, docx) if not p.exists() or p.stat().st_size == 0]
    if missing:
        verifier.fail_check("download artifacts", f"Eksik veya boş indirilebilir dosya: {missing}")
    else:
        verifier.pass_check("download artifacts", f"PDF ({pdf.stat().st_size} bytes) ve DOCX ({docx.stat().st_size} bytes) mevcut.")

    public_pdfs = sorted((root / "docs" / "assets").glob("**/*.pdf"))
    unexpected = [rel(p, root) for p in public_pdfs if p.name != pdf.name]
    if unexpected:
        verifier.fail_check("public pdf boundary", f"Beklenmeyen public PDF bulundu: {unexpected}")
    else:
        verifier.pass_check("public pdf boundary", "Public assets içinde yalnızca staj defteri PDF'i var.")


def check_transcript(verifier: Verifier, manifest: list[dict[str, object]]) -> None:
    root = verifier.root
    transcript_dir = root / "docs" / "transcript"
    search_index_path = root / "docs" / "data" / "search_index.json"
    transcript_pages = sorted(transcript_dir.glob("page-*.html")) if transcript_dir.exists() else []

    if len(transcript_pages) != len(manifest):
        verifier.fail_check("transcript count", f"Transcript sayısı {len(transcript_pages)}, manifest sayısı {len(manifest)}.")
    else:
        verifier.pass_check("transcript count", f"{len(transcript_pages)} transcript sayfası manifestle eşleşiyor.")

    missing_transcripts: list[str] = []
    bad_backlinks: list[str] = []
    for item in manifest:
        path = root / "docs" / str(item.get("transcript_path", ""))
        if not path.exists():
            missing_transcripts.append(str(item.get("transcript_path", "")))
            continue
        expected = f"../staj-defteri.html#page-{int(item['page_index']):03d}"
        text = path.read_text(encoding="utf-8", errors="replace")
        if expected not in text:
            bad_backlinks.append(f"{rel(path, root)} expected {expected}")

    if missing_transcripts:
        verifier.fail_check("manifest transcript paths", f"Eksik transcript path: {missing_transcripts[:10]}")
    else:
        verifier.pass_check("manifest transcript paths", "Manifestteki tüm transcript path'leri mevcut.")

    if bad_backlinks:
        verifier.fail_check("transcript backlinks", "; ".join(bad_backlinks[:10]))
    else:
        verifier.pass_check("transcript backlinks", "Transcript sayfaları ilgili görsel sayfaya geri bağlı.")

    if not search_index_path.exists():
        verifier.fail_check("search index", "docs/data/search_index.json bulunamadı.")
        return
    search_index = load_json(search_index_path)
    if not isinstance(search_index, list) or len(search_index) != len(manifest):
        verifier.fail_check("search index count", f"Search index sayısı manifestle eşleşmiyor.")
        return
    required = {"page_index", "page_label", "title", "text_excerpt", "full_text_path"}
    missing_fields = [str(item.get("page_index", "?")) for item in search_index if not required.issubset(item.keys())]
    if missing_fields:
        verifier.fail_check("search index fields", f"Eksik alanlı search kaydı: {missing_fields[:10]}")
    else:
        verifier.pass_check("search index", f"{len(search_index)} search kaydı gerekli alanlarla mevcut.")


def check_encoding_and_external(verifier: Verifier) -> None:
    root = verifier.root
    docs = root / "docs"
    replacement_files: list[str] = []
    cdn_refs: list[str] = []
    for path in iter_text_files(docs):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "\ufffd" in text:
            replacement_files.append(rel(path, root))
        if re.search(r"cdn|unpkg|jsdelivr|cdnjs", text, re.IGNORECASE):
            cdn_refs.append(rel(path, root))

    if replacement_files:
        verifier.fail_check("utf-8 replacement chars", f"U+FFFD bulunan dosyalar: {replacement_files[:20]}")
    else:
        verifier.pass_check("utf-8 replacement chars", "Docs içeriğinde U+FFFD bulunmadı.")

    if cdn_refs:
        verifier.fail_check("external cdn", f"CDN referansı şüphesi: {cdn_refs}")
    else:
        verifier.pass_check("external cdn", "Dış CDN bağımlılığı bulunmadı.")


def check_git_ignored_sources(verifier: Verifier) -> None:
    targets = [
        "Chase - A history of research in service operations  What s the big idea.pdf",
        "Cross-training policies in field services.pdf",
        "EK-10_Siemens_Staj_Makale_Analizleri.docx",
        "_local_sources/README.local.txt",
    ]
    not_ignored: list[str] = []
    try:
        for target in targets:
            proc = subprocess.run(
                ["git", "check-ignore", "-q", target],
                cwd=verifier.root,
                check=False,
            )
            if proc.returncode != 0:
                not_ignored.append(target)
    except OSError as exc:
        verifier.warn_check("git check-ignore", f"git çalıştırılamadı: {exc}")
        return

    if not not_ignored:
        verifier.pass_check("gitignored private sources", "Kök kaynaklar ve local-only klasörler ignored durumda.")
    else:
        verifier.warn_check("gitignored private sources", f"Ignore görünmeyen private/local kaynaklar: {not_ignored}")


def write_report(verifier: Verifier, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# QA Report",
        "",
        f"Tarih: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Sonuç: {'PASS' if not verifier.failures else 'FAIL'}",
        "",
        "## Kontroller",
        "",
    ]
    for check in verifier.checks:
        lines.append(f"- **{check.status}** `{check.name}`: {check.detail}")
    lines.extend(["", "## Kalan Bilinen Kusurlar", ""])
    if verifier.failures:
        for failure in verifier.failures:
            lines.append(f"- {failure}")
    else:
        lines.append("- Kritik doğrulama hatası yok.")
    if verifier.warnings:
        lines.extend(["", "## Uyarılar", ""])
        for warning in verifier.warnings:
            lines.append(f"- {warning}")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default="planning/qa-report.md")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    verifier = Verifier(root=root)

    manifest, _ = check_manifest(verifier)
    check_html_links(verifier)
    check_downloads(verifier)
    check_transcript(verifier, manifest)
    check_encoding_and_external(verifier)
    check_git_ignored_sources(verifier)

    report = root / args.report
    write_report(verifier, report)
    print(f"QA report written to {rel(report, root)}")
    print(f"Result: {'PASS' if not verifier.failures else 'FAIL'}")
    if verifier.failures:
        for failure in verifier.failures:
            print(f"FAIL: {failure}")
    return 1 if verifier.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
