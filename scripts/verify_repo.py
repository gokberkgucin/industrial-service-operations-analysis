from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_PATH = REPO_ROOT / "metadata" / "qa-report.md"

MANDATORY_FILES = [
    Path("README.md"),
    Path("docs/internship-part-1.md"),
    Path("docs/internship-part-2.md"),
    Path("docs/references.md"),
    Path("docs/publication-note.md"),
    Path("LICENSE.md"),
]

FRONTMATTER_REQUIRED = [
    Path("docs/internship-part-1.md"),
    Path("docs/internship-part-2.md"),
    Path("docs/references.md"),
    Path("docs/publication-note.md"),
]

IGNORED_DIRS = {".git", "_work", "__pycache__", ".venv", "venv", "node_modules"}
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "tel:")


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        parts = set(path.relative_to(REPO_ROOT).parts)
        if parts & IGNORED_DIRS:
            continue
        files.append(path)
    return sorted(files)


def has_frontmatter(text: str) -> bool:
    if not text.startswith("---\n"):
        return False
    lines = text.splitlines()
    if len(lines) < 3:
        return False
    return any(line.strip() == "---" for line in lines[1:])


def is_external(target: str) -> bool:
    lower = target.lower()
    return lower.startswith(REMOTE_SCHEMES)


def normalize_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target:
        return None
    if target.startswith("#") or is_external(target):
        return None
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    target = unquote(target).strip()
    if not target:
        return None
    return target


def resolve_link(source_file: Path, target: str) -> Path:
    candidate = (source_file.parent / target).resolve()
    return candidate


def extract_markdown_links(text: str) -> list[tuple[bool, str]]:
    # Captures ordinary inline Markdown links and images. It intentionally
    # avoids reference-style links because this repo currently does not use them.
    links: list[tuple[bool, str]] = []
    pattern = re.compile(r"(!?)\[[^\]]*]\(([^)\n]+)\)")
    for match in pattern.finditer(text):
        is_image = bool(match.group(1))
        target = match.group(2)
        links.append((is_image, target))
    return links


def check_required_files(results: list[CheckResult], errors: list[str]) -> None:
    missing = [path for path in MANDATORY_FILES if not (REPO_ROOT / path).is_file()]
    if missing:
        for path in missing:
            errors.append(f"Zorunlu dosya eksik: `{path.as_posix()}`")
        results.append(CheckResult("Zorunlu dosyalar", "FAIL", f"{len(missing)} dosya eksik."))
    else:
        results.append(CheckResult("Zorunlu dosyalar", "PASS", f"{len(MANDATORY_FILES)} dosya bulundu."))


def check_frontmatter(results: list[CheckResult], errors: list[str]) -> None:
    missing: list[str] = []
    for path in FRONTMATTER_REQUIRED:
        full = REPO_ROOT / path
        if full.exists() and not has_frontmatter(read_text(full)):
            missing.append(path.as_posix())

    if missing:
        for item in missing:
            errors.append(f"Frontmatter eksik veya kapanmamış: `{item}`")
        results.append(CheckResult("Frontmatter", "FAIL", f"{len(missing)} dosyada frontmatter problemi var."))
    else:
        results.append(CheckResult("Frontmatter", "PASS", f"{len(FRONTMATTER_REQUIRED)} zorunlu docs dosyası frontmatter içeriyor."))


def check_links(results: list[CheckResult], errors: list[str]) -> None:
    broken_images: list[str] = []
    broken_links: list[str] = []
    checked_images = 0
    checked_links = 0

    for md in markdown_files():
        text = read_text(md)
        for is_image, raw_target in extract_markdown_links(text):
            target = normalize_target(raw_target)
            if target is None:
                continue
            resolved = resolve_link(md, target)
            if is_image:
                checked_images += 1
                if not resolved.is_file():
                    broken_images.append(f"{rel(md)} -> {raw_target}")
            else:
                checked_links += 1
                if not resolved.exists():
                    broken_links.append(f"{rel(md)} -> {raw_target}")

    if broken_images:
        for item in broken_images:
            errors.append(f"Kırık görsel linki: `{item}`")
        results.append(CheckResult("Görsel linkleri", "FAIL", f"{len(broken_images)} kırık görsel linki bulundu."))
    else:
        results.append(CheckResult("Görsel linkleri", "PASS", f"{checked_images} görsel linki doğrulandı."))

    if broken_links:
        for item in broken_links:
            errors.append(f"Kırık relative link: `{item}`")
        results.append(CheckResult("Relative linkler", "FAIL", f"{len(broken_links)} kırık relative link bulundu."))
    else:
        results.append(CheckResult("Relative linkler", "PASS", f"{checked_links} relative link doğrulandı."))


def check_empty_todos(results: list[CheckResult], errors: list[str]) -> None:
    hits: list[str] = []
    todo_pattern = re.compile(r"\bTODO\b\s*[:\-–—]?\s*(.*)$", re.IGNORECASE)

    for md in markdown_files():
        for line_no, line in enumerate(read_text(md).splitlines(), start=1):
            match = todo_pattern.search(line)
            if not match:
                continue
            remainder = match.group(1).strip()
            # A TODO with almost no explanatory text is treated as unfinished.
            alnum_count = sum(ch.isalnum() for ch in remainder)
            if alnum_count < 8:
                hits.append(f"{rel(md)}:{line_no}: {line.strip()}")

    if hits:
        for item in hits:
            errors.append(f"Boş veya belirsiz TODO bloğu: `{item}`")
        results.append(CheckResult("TODO kontrolü", "FAIL", f"{len(hits)} boş/belirsiz TODO bulundu."))
    else:
        results.append(CheckResult("TODO kontrolü", "PASS", "Boş veya belirsiz TODO bloğu bulunmadı."))


def find_executable(names: list[str]) -> str | None:
    for name in names:
        found = shutil.which(name)
        if found:
            return found
    return None


def run_optional_command(command: list[str]) -> tuple[int, str]:
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=False,
    )
    return completed.returncode, completed.stdout.strip()


def optional_markdown_lint(results: list[CheckResult], errors: list[str], warnings: list[str], strict: bool) -> None:
    exe = find_executable(["markdownlint-cli2", "markdownlint-cli2.cmd", "markdownlint", "markdownlint.cmd"])
    if not exe:
        msg = "markdownlint CLI bulunamadı; opsiyonel lint atlandı."
        if strict:
            errors.append(msg)
            results.append(CheckResult("Opsiyonel markdown lint", "FAIL", msg))
        else:
            warnings.append(msg)
            results.append(CheckResult("Opsiyonel markdown lint", "SKIP", msg))
        return

    command = [exe, "**/*.md", "!_work/**", "!node_modules/**"]
    code, output = run_optional_command(command)
    if code != 0:
        errors.append("markdownlint başarısız oldu.")
        results.append(CheckResult("Opsiyonel markdown lint", "FAIL", output or "Komut hata kodu döndürdü."))
    else:
        results.append(CheckResult("Opsiyonel markdown lint", "PASS", output or "markdownlint temiz."))


def optional_link_check(results: list[CheckResult], errors: list[str], warnings: list[str], strict: bool) -> None:
    exe = find_executable(["markdown-link-check", "markdown-link-check.cmd"])
    if not exe:
        msg = "markdown-link-check CLI bulunamadı; opsiyonel harici link kontrolü atlandı."
        if strict:
            errors.append(msg)
            results.append(CheckResult("Opsiyonel link check", "FAIL", msg))
        else:
            warnings.append(msg)
            results.append(CheckResult("Opsiyonel link check", "SKIP", msg))
        return

    failures: list[str] = []
    checked = 0
    for md in markdown_files():
        code, output = run_optional_command([exe, rel(md)])
        checked += 1
        if code != 0:
            failures.append(f"{rel(md)}\n{output}")

    if failures:
        errors.append("markdown-link-check başarısız oldu.")
        results.append(CheckResult("Opsiyonel link check", "FAIL", "\n\n".join(failures)))
    else:
        results.append(CheckResult("Opsiyonel link check", "PASS", f"{checked} Markdown dosyası kontrol edildi."))


def write_report(results: list[CheckResult], errors: list[str], warnings: list[str], args: argparse.Namespace) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    status = "FAIL" if errors else "PASS"
    lines: list[str] = [
        "# QA Report",
        "",
        f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Durum: **{status}**",
        "",
        "## Çalıştırma Komutları",
        "",
        "```powershell",
        "python .\\scripts\\verify_repo.py",
        "python .\\scripts\\verify_repo.py --markdown-lint",
        "python .\\scripts\\verify_repo.py --link-check",
        "python .\\scripts\\verify_repo.py --markdown-lint --link-check --strict-optional",
        "```",
        "",
        "## Kontrol Özeti",
        "",
        "| Kontrol | Durum | Detay |",
        "|---|---|---|",
    ]

    for result in results:
        detail = result.detail.replace("\n", "<br>")
        lines.append(f"| {result.name} | {result.status} | {detail} |")

    lines.extend(["", "## Zorunlu Dosyalar", ""])
    for path in MANDATORY_FILES:
        marker = "var" if (REPO_ROOT / path).exists() else "eksik"
        lines.append(f"- `{path.as_posix()}`: {marker}")

    lines.extend(["", "## Taranan Markdown Dosyaları", ""])
    for path in markdown_files():
        lines.append(f"- `{rel(path)}`")

    lines.extend(["", "## Uyarılar", ""])
    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- Uyarı yok.")

    lines.extend(["", "## Hatalar", ""])
    if errors:
        for error in errors:
            lines.append(f"- {error}")
    else:
        lines.append("- Kritik hata yok.")

    lines.extend([
        "",
        "## Opsiyonel Kontroller",
        "",
        f"- Markdown lint istendi mi: `{args.markdown_lint}`",
        f"- Link check istendi mi: `{args.link_check}`",
        f"- Opsiyonel araç yoksa fail modu: `{args.strict_optional}`",
    ])

    REPORT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify publishable Markdown repository quality.")
    parser.add_argument("--markdown-lint", action="store_true", help="Run markdownlint if a local CLI is available.")
    parser.add_argument("--link-check", action="store_true", help="Run markdown-link-check if a local CLI is available.")
    parser.add_argument("--strict-optional", action="store_true", help="Fail if optional Node-based tools are unavailable.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results: list[CheckResult] = []
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(results, errors)
    check_frontmatter(results, errors)
    check_links(results, errors)
    check_empty_todos(results, errors)

    if args.markdown_lint:
        optional_markdown_lint(results, errors, warnings, args.strict_optional)
    if args.link_check:
        optional_link_check(results, errors, warnings, args.strict_optional)

    write_report(results, errors, warnings, args)

    print(f"QA report written to {REPORT_PATH}")
    if errors:
        print(f"QA failed with {len(errors)} error(s).")
        for error in errors:
            print(f"- {error}")
        return 1

    print("QA passed.")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for warning in warnings:
            print(f"- {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
