from pathlib import Path
import json
import requests
from bs4 import BeautifulSoup

BASE = 'https://sibe-cad.vercel.app'
EXPECTED = {
    '/': ['Home'],
    '/cloud-cad-management/': ['Home', 'Cloud CAD Management'],
    '/features/cad-file-management/': ['Home', 'Cloud CAD Management', 'CAD File Management'],
    '/features/solidworks-revision-approval-workflow/': ['Home', 'Cloud CAD Management', 'Revision Approval Workflow'],
    '/features/solidworks-bom-management/': ['Home', 'Cloud CAD Management', 'SolidWorks BOM Management'],
    '/features/remote-team-collaboration-for-solidworks-teams/': ['Home', 'Cloud CAD Management', 'Remote Team Collaboration'],
    '/cloud-pdm/solidworks-pdm-migration/': ['Home', 'Cloud CAD Management', 'SolidWorks PDM Migration'],
    '/contact/': ['Home', 'Contact'],
    '/editorial-methodology/': ['Home', 'Editorial Methodology'],
    '/ask/': ['Home', 'Ask Sibe'],
}

for path, expected in EXPECTED.items():
    response = requests.get(BASE + path, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    nav = soup.find('nav', class_='breadcrumb')
    visible = [part.strip() for part in nav.get_text(' ', strip=True).split('›')] if nav else []
    schemas = []
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        schemas.extend(data.get('@graph', []))
    crumb = next((item for item in schemas if item.get('@type') == 'BreadcrumbList'), None)
    structured = [item.get('name') for item in crumb.get('itemListElement', [])] if crumb else []
    print(f'{path} visible={visible} schema={structured} expected={expected}')
    if path == '/':
        assert not nav, 'homepage should not have redundant breadcrumb'
        assert not crumb, 'homepage should not have redundant breadcrumb schema'
    else:
        assert visible == expected, (path, visible, expected)
        assert structured == expected, (path, structured, expected)
print('live-breadcrumb-audit=passed')
