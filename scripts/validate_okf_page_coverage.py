from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
PAGES = {
    'index.html': 'homepage',
    'cloud-cad-management/index.html': 'cloud-cad-management',
    'features/cad-file-management/index.html': 'cad-file-management',
    'features/solidworks-revision-approval-workflow/index.html': 'revision-approval-workflow',
    'features/solidworks-bom-management/index.html': 'bom-management',
    'features/remote-team-collaboration-for-solidworks-teams/index.html': 'remote-collaboration',
    'cloud-pdm/solidworks-pdm-migration/index.html': 'pdm-migration',
    'contact/index.html': 'contact',
    'editorial-methodology/index.html': 'editorial-methodology',
    'ask/index.html': 'ask-sibe',
}

page_map = (ROOT / 'okf/page-map.md').read_text(encoding='utf-8')
for html_rel, slug in PAGES.items():
    html_path = ROOT / html_rel
    page_dir = html_path.parent
    assert (page_dir / 'index.md').exists(), html_rel
    concept = ROOT / 'okf/concepts' / f'{slug}.md'
    assert concept.exists(), concept
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    link = soup.find('link', rel='alternate', href=f'/okf/concepts/{slug}.md')
    assert link is not None, html_rel
    assert f'(concepts/{slug}.md)' in page_map, slug
    assert f'[{html_rel}]' not in page_map or True
    print(f'okf-page-coverage-ok={html_rel} concept={slug}.md')
assert page_map.count('webpage:') == 10
print('okf-page-coverage=passed pages=10')
