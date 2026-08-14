from pathlib import Path
from bs4 import BeautifulSoup
import json
import re

ROOT = Path('/home/ubuntu/web-dev')
html_pages = sorted(p for p in ROOT.rglob('index.html') if p.parent.name != 'ask')
assert len(html_pages) == 9, html_pages

for page in html_pages:
    text = page.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3'])
    assert headings and all(h.get('id') for h in headings), page
    images = soup.find_all('img')
    assert len(images) >= 2, page
    assert all(img.get('loading') == 'lazy' for img in images[1:]), page
    sources = soup.find('section', class_='site-sources') or soup.find('section', class_='sources')
    assert sources and sources.find_all('cite'), page
    assert 'Reviewed 15 August 2026' in sources.get_text(' ', strip=True), page
    assert '\x01' not in text, page

home = BeautifulSoup((ROOT / 'index.html').read_text(encoding='utf-8'), 'html.parser')
assert home.find('aside', class_='proof-note')
assert home.find('table', class_='comparison')
assert home.find('h3', id='shared-drive-vs-cloud-pdm')
assert home.find('p', class_='outcome-line')
assert home.find('p', class_='current-context')
assert home.find('nav', class_='contents')

for jsonld in [ROOT / 'index.jsonld', ROOT / 'machine-readable' / 'index.jsonld']:
    data = json.loads(jsonld.read_text(encoding='utf-8'))
    types = {node.get('@type') for node in data.get('@graph', []) if isinstance(node, dict)}
    assert 'WebSite' in types, jsonld
    organizations = [node for node in data['@graph'] if node.get('@type') == 'Organization']
    assert organizations and organizations[0].get('contactPoint'), jsonld

print(f'glippy-recommendations-regression=passed pages={len(html_pages)}')
