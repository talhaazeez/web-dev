from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
BASE = 'https://sibe-cad.vercel.app'
PAGES = [
    ROOT / 'index.html',
    ROOT / 'cloud-cad-management/index.html',
    ROOT / 'features/cad-file-management/index.html',
    ROOT / 'features/solidworks-revision-approval-workflow/index.html',
    ROOT / 'features/solidworks-bom-management/index.html',
    ROOT / 'features/remote-team-collaboration-for-solidworks-teams/index.html',
    ROOT / 'cloud-pdm/solidworks-pdm-migration/index.html',
]

for page in PAGES:
    soup = BeautifulSoup(page.read_text(), 'html.parser')
    title = soup.title.get_text(strip=True) if soup.title else ''
    description = soup.find('meta', attrs={'name': 'description'})
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    json_blocks = []
    for node in soup.find_all('script', attrs={'type': 'application/ld+json'}):
        json_blocks.append(json.loads(node.string or node.get_text()))
    types = set()
    for block in json_blocks:
        for entity in block.get('@graph', [block]):
            if isinstance(entity, dict) and '@type' in entity:
                types.add(entity['@type'])
    assert len(soup.find_all('h1')) == 1, page
    assert soup.find('a', class_='skip-link'), page
    assert soup.find('main', id='main-content'), page
    assert 35 <= len(title) <= 70, (page, len(title), title)
    assert description and len(description.get('content', '')) <= 160, (page, description.get('content', '') if description else '')
    assert canonical and canonical.get('href', '').startswith(BASE), page
    assert {'WebPage', 'Organization', 'SoftwareApplication', 'FAQPage'} <= types, (page, types)
    assert len(soup.find_all('h2', id=True)) >= 1, page
    assert soup.find('meta', attrs={'name': 'twitter:card'}), page
    assert soup.find('meta', attrs={'property': 'og:image'}), page
    print(f'page-ok={page.relative_to(ROOT)} title={len(title)} description={len(description["content"])} schema={sorted(types)}')

manifest = json.loads((ROOT / 'site.webmanifest').read_text())
assert manifest['short_name'] == 'Sibe'
assert len(manifest['icons']) >= 5
print('manifest-ok')

robots = (ROOT / 'robots.txt').read_text()
assert 'Content-Signal: search=yes, ai-input=yes, ai-train=no' in robots
assert 'Sitemap: https://sibe-cad.vercel.app/sitemap.xml' in robots
print('robots-ok')

sitemap = (ROOT / 'sitemap.xml').read_text()
assert sitemap.count('<loc>') == 7
assert sitemap.count('<lastmod>2026-08-15</lastmod>') == 7
print('sitemap-ok')

key_files = [p for p in ROOT.glob('*.txt') if re.fullmatch(r'[A-Fa-f0-9]{64}\.txt', p.name)]
assert len(key_files) == 1
assert key_files[0].read_text().strip() == key_files[0].stem
print(f'indexnow-key-ok={key_files[0].name}')

assert (ROOT / 'llms.txt').exists() and (ROOT / 'llms-full.txt').exists()
assert (ROOT / 'vercel.json').exists()
assert (ROOT / '.github/workflows/indexnow.yml').exists()
print('discovery-and-workflow-files-ok')
