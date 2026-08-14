from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
BASE = 'https://sibe-cad.vercel.app'
EXPECTED = {
    'cloud-cad-management': ['Home', 'Cloud CAD Management'],
    'features/cad-file-management': ['Home', 'Cloud CAD Management', 'CAD File Management'],
    'features/solidworks-revision-approval-workflow': ['Home', 'Cloud CAD Management', 'Revision Approval Workflow'],
    'features/solidworks-bom-management': ['Home', 'Cloud CAD Management', 'SolidWorks BOM Management'],
    'features/remote-team-collaboration-for-solidworks-teams': ['Home', 'Cloud CAD Management', 'Remote Team Collaboration'],
    'cloud-pdm/solidworks-pdm-migration': ['Home', 'Cloud CAD Management', 'SolidWorks PDM Migration'],
    'contact': ['Home', 'Contact'],
    'editorial-methodology': ['Home', 'Editorial Methodology'],
    'ask': ['Home', 'Ask Sibe'],
}

for slug, expected in EXPECTED.items():
    html_path = ROOT / slug / 'index.html'
    endpoint_path = ROOT / slug / 'index.jsonld'
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    nav = soup.find('nav', class_='breadcrumb')
    visible = [part.strip() for part in nav.get_text(' ', strip=True).split('›')] if nav else []
    assert visible == expected, (slug, visible, expected)
    graphs = []
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        graphs.append(data.get('@graph', []))
    graphs.append(json.loads(endpoint_path.read_text(encoding='utf-8'))['@graph'])
    for graph in graphs:
        crumb = next(item for item in graph if item.get('@type') == 'BreadcrumbList')
        structured = [item['name'] for item in crumb['itemListElement']]
        assert structured == expected, (slug, structured, expected)
        assert [item['position'] for item in crumb['itemListElement']] == list(range(1, len(expected) + 1))
        webpage = next(item for item in graph if item.get('@type') == 'WebPage')
        assert webpage['breadcrumb']['@id'] == crumb['@id']
    print(f'local-hierarchy-ok={slug} levels={len(expected)}')
print('local-breadcrumb-hierarchy=passed pages=9')
