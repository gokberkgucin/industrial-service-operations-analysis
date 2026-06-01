import re
import sys
from pathlib import Path


root = Path(sys.argv[1]).resolve()
html_files = list(root.rglob("*.html"))
pattern = re.compile(r'''(?:href|src|data)\s*=\s*["']([^"'#?]+)''', re.I)

bad = []
checked = 0

for html_file in html_files:
    text = html_file.read_text(encoding="utf-8", errors="ignore")
    for raw in pattern.findall(text):
        if raw.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "data:")):
            continue
        target = (html_file.parent / raw).resolve()
        checked += 1
        if not target.exists():
            bad.append((str(html_file.relative_to(root)), raw))

print(f"HTML dosyası: {len(html_files)}")
print(f"Kontrol edilen yerel link: {checked}")
if bad:
    print("KIRIK LİNKLER:")
    for src, raw in bad:
        print(f"{src} -> {raw}")
    sys.exit(1)
else:
    print("Tüm yerel linkler mevcut.")
