#!/usr/bin/env python
"""Render the internship PDF to stable page image assets."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import fitz  # PyMuPDF


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    root = repo_root()
    return argparse.ArgumentParser(description=__doc__).parse_args()


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pdf",
        default=str(root / "docs" / "assets" / "staj" / "originals" / "EK-10_Siemens_Staj_Makale_Analizleri.pdf"),
        help="Input PDF path.",
    )
    parser.add_argument(
        "--out",
        default=str(root / "docs" / "assets" / "staj" / "pages"),
        help="Output directory for rendered page images.",
    )
    parser.add_argument("--dpi", type=int, default=200, help="Rendering DPI.")
    parser.add_argument(
        "--clean-output",
        action="store_true",
        help="Remove existing page-*.png files in the output directory before rendering.",
    )
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    out_dir = Path(args.out).resolve()
    log_dir = root / "_work" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    if not pdf_path.exists():
        raise FileNotFoundError(f"Input PDF not found: {pdf_path}")

    out_dir.mkdir(parents=True, exist_ok=True)
    if args.clean_output:
        for old_page in out_dir.glob("page-*.png"):
            old_page.unlink()

    doc = fitz.open(pdf_path)
    scale = args.dpi / 72.0
    matrix = fitz.Matrix(scale, scale)
    pages = []

    for index in range(doc.page_count):
        page = doc.load_page(index)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        filename = f"page-{index + 1:03d}.png"
        output_path = out_dir / filename
        pix.save(output_path)
        pages.append(
            {
                "page_index": index + 1,
                "filename": filename,
                "path": str(output_path.relative_to(root)).replace("\\", "/"),
                "width": pix.width,
                "height": pix.height,
                "bytes": output_path.stat().st_size,
            }
        )

    result = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input_pdf": str(pdf_path),
        "output_dir": str(out_dir),
        "dpi": args.dpi,
        "page_count": doc.page_count,
        "pages": pages,
    }
    (log_dir / "export_pdf_pages.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
