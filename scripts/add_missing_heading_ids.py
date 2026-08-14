from pathlib import Path
from bs4 import BeautifulSoup
import re

ROOT = Path('/home/ubuntu/web-dev')

def slug(text):
    text = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return text or 'section'

for page in sorted(ROOT.rglob('index.html')):
    text = page.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    used = {node.get('id') for node in soup.find_all(id=True)}
    changed = False
    for heading in soup.find_all(['h1','h2','h3']):
        if heading.get('id'):
            continue
        base = slug(heading.get_text(' ', strip=True))
        candidate = base
        i = 2
        while candidate in used:
            candidate = f'{base}-{i}'
            i += 1
        heading['id'] = candidate
        used.add(candidate)
        changed = True
    if changed:
        page.write_text(str(soup), encoding='utf-8')
        print(f'heading-ids-added={page.relative_to(ROOT)}')
