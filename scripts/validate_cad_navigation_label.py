from pathlib import Path
import re

files = sorted(Path('/home/ubuntu/web-dev').rglob('index.html'))
old = 0
new = 0
for path in files:
    text = path.read_text(encoding='utf-8')
    old += len(re.findall(r'<a\s+href="/features/cad-file-management/">CAD files</a>', text))
    new += len(re.findall(r'<a\s+href="/features/cad-file-management/">CAD file management</a>', text))
    if 'Manage CAD files' in text:
        assert 'Manage CAD files' in text, path
assert old == 0, old
assert new == 17, new
print(f'cad-navigation-label-check=passed pages={len(files)} new_anchor_labels={new} preserved_manage_cta=true')
