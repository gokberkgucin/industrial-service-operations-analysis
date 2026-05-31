#!/usr/bin/env python
"""Build the GitHub Pages page manifest from rendered page images and PDF text."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF
from PIL import Image


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def clean_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


PAGE_METADATA = {
    1: ("Kapak", "kapak/form sayfaları", "Kapak"),
    2: ("Staj Genel Bilgileri", "iş yeri bilgileri", "Staj Genel Bilgileri"),
    3: ("I", "iş yeri bilgileri", "İş Yeri Hakkında Bilgiler I"),
    4: ("II", "iş yeri bilgileri", "İş Yeri Hakkında Bilgiler II"),
    5: ("1", "makale görevi giriş", "Makale görevi giriş"),
    6: ("2", "makale ödevi 1", "Hizmet Operasyonları Hakkında bir Deneme"),
    7: ("3", "makale ödevi 1", "Makale Ödevi 1 - Sonraki Nesiller?"),
    8: ("4", "makale ödevi 1", "Makale Ödevi 1 - İlk çalışmalar ve İnsan-Fonksiyon"),
    9: ("5", "makale ödevi 1", "Makale Ödevi 1 - McDonald's"),
    10: ("6", "makale ödevi 1", "Makale Ödevi 1 - Disney"),
    11: ("7", "makale ödevi 1", "Kişisel Operasyon Yönetimi Deneyimi"),
    12: ("8", "makale ödevi 1", "Süreç: Sonuçlardan Daha Önemli Olabilir"),
    13: ("9", "makale ödevi 1", "İfade Özgürlüğünün Bonusları"),
    14: ("10", "makale ödevi 1", "Rekabet Üstünlüğü"),
    15: ("11", "makale ödevi 1", "Makale Ödevi 1 - devam"),
    16: ("12", "makale ödevi 2", "Makale Ödevi 2 - giriş"),
    17: ("13", "makale ödevi 2", "Genel Bilgiler, Denklemler, Varsayım ve Kabuller"),
    18: ("14", "makale ödevi 2", "Makine Güvenilirliği"),
    19: ("15", "makale ödevi 2", "Ceza Puanı"),
    20: ("16", "makale ödevi 2", "Benzetim Deneyinden Çıkan Bazı Sonuçlar"),
    21: ("17", "makale ödevi 2", "N-FSE İstihdamının Etkisi"),
    22: ("18", "makale ödevi 2", "Makale Ödevi 2 - sonuç yorumları"),
    23: ("19", "makale ödevi 2", "DE: Doğrudan Etki"),
    24: ("20", "makale ödevi 2", "Makale Ödevi 2 - Tablo 2 ve Tablo 3 yorumu"),
    25: ("21", "makale ödevi 2", "Makale Ödevi 2 - arıza ihtimali ve PM bakımı"),
    26: ("21", "makale ödevi 2", "Makale Ödevi 2 - çapraz eğitim politikası eleştirileri"),
    27: ("22", "makale ödevi 2", "Sonuç"),
    28: ("Ek-I", "kaynakça", "Kaynakça"),
}


def page_metadata(page_index: int, text: str) -> tuple[str, str, str]:
    if page_index in PAGE_METADATA:
        return PAGE_METADATA[page_index]
    for line in clean_lines(text):
        line = re.sub(r"\s+", " ", line)
        if len(line) >= 3:
            return f"Sayfa {page_index}", "staj defteri", line[:90]
    return f"Sayfa {page_index}", "staj defteri", f"Sayfa {page_index}"


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf",
        default=str(root / "docs" / "assets" / "staj" / "originals" / "EK-10_Siemens_Staj_Makale_Analizleri.pdf"),
        help="Input PDF path.",
    )
    parser.add_argument(
        "--pages-dir",
        default=str(root / "docs" / "assets" / "staj" / "pages"),
        help="Rendered page image directory.",
    )
    parser.add_argument(
        "--output",
        default=str(root / "docs" / "data" / "page_manifest.json"),
        help="Output page manifest JSON path.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    pages_dir = Path(args.pages_dir).resolve()
    output_path = Path(args.output).resolve()
    log_dir = root / "_work" / "logs"

    if not pdf_path.exists():
        raise FileNotFoundError(f"Input PDF not found: {pdf_path}")
    if not pages_dir.exists():
        raise FileNotFoundError(f"Pages directory not found: {pages_dir}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    manifest = []
    missing_images = []

    for page_number in range(1, doc.page_count + 1):
        filename = f"page-{page_number:03d}.png"
        image_path = pages_dir / filename
        if not image_path.exists():
            missing_images.append(filename)
            width = None
            height = None
        else:
            with Image.open(image_path) as image:
                width, height = image.size

        page = doc.load_page(page_number - 1)
        text = page.get_text("text")
        page_label, section, short_title = page_metadata(page_number, text)
        manifest.append(
            {
                "page_index": page_number,
                "filename": filename,
                "page_label": page_label,
                "short_title": short_title,
                "section": section,
                "alt_text": f"Staj defteri {page_label}: {short_title}",
                "image_path": str(image_path.relative_to(root)).replace("\\", "/"),
                "image_width": width,
                "image_height": height,
            }
        )

    if missing_images:
        raise RuntimeError(f"Missing rendered page images: {', '.join(missing_images)}")

    output_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input_pdf": str(pdf_path),
        "pages_dir": str(pages_dir),
        "output": str(output_path),
        "page_count": len(manifest),
        "sections": sorted({entry["section"] for entry in manifest}),
    }
    (log_dir / "build_manifest.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
