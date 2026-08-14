from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
for html_path in sorted(ROOT.rglob('index.html')):
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    script = soup.find('script', attrs={'type': 'application/ld+json'})
    if not script or not script.string:
        raise RuntimeError(f'JSON-LD script missing: {html_path}')
    data = json.loads(script.string)
    output = html_path.parent / 'index.jsonld'
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'synced={output.relative_to(ROOT)}')

root = ROOT / 'index.jsonld'
mirror = ROOT / 'machine-readable' / 'index.jsonld'
mirror.write_text(root.read_text(encoding='utf-8'), encoding='utf-8')
print(f'synced={mirror.relative_to(ROOT)}')
