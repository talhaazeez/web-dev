from pathlib import Path
import re

ROOT = Path('/home/ubuntu/web-dev')
files = sorted(ROOT.rglob('index.html'))
pattern = re.compile(r'(<a\s+href="/features/cad-file-management/">)CAD files(</a>)')
updated = 0
matches = 0
for path in files:
    text = path.read_text(encoding='utf-8')
    count = len(pattern.findall(text))
    if count:
        new_text = pattern.sub(r'\1CAD file management\2', text)
        path.write_text(new_text, encoding='utf-8')
        updated += 1
        matches += count
        print(f'updated={path.relative_to(ROOT)} anchors={count}')
print(f'navigation-label-update=passed files={updated} anchors={matches}')
