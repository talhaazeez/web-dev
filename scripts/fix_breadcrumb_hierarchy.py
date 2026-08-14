from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
BASE = 'https://sibe-cad.vercel.app'
PAGES = {
    'cloud-cad-management': {
        'label': 'Cloud CAD Management',
        'url': f'{BASE}/cloud-cad-management/',
        'parents': [],
    },
    'features/cad-file-management': {
        'label': 'CAD File Management',
        'url': f'{BASE}/features/cad-file-management/',
        'parents': [('Cloud CAD Management', f'{BASE}/cloud-cad-management/')],
    },
    'features/solidworks-revision-approval-workflow': {
        'label': 'Revision Approval Workflow',
        'url': f'{BASE}/features/solidworks-revision-approval-workflow/',
        'parents': [('Cloud CAD Management', f'{BASE}/cloud-cad-management/')],
    },
    'features/solidworks-bom-management': {
        'label': 'SolidWorks BOM Management',
        'url': f'{BASE}/features/solidworks-bom-management/',
        'parents': [('Cloud CAD Management', f'{BASE}/cloud-cad-management/')],
    },
    'features/remote-team-collaboration-for-solidworks-teams': {
        'label': 'Remote Team Collaboration',
        'url': f'{BASE}/features/remote-team-collaboration-for-solidworks-teams/',
        'parents': [('Cloud CAD Management', f'{BASE}/cloud-cad-management/')],
    },
    'cloud-pdm/solidworks-pdm-migration': {
        'label': 'SolidWorks PDM Migration',
        'url': f'{BASE}/cloud-pdm/solidworks-pdm-migration/',
        'parents': [('Cloud CAD Management', f'{BASE}/cloud-cad-management/')],
    },
    'contact': {
        'label': 'Contact',
        'url': f'{BASE}/contact/',
        'parents': [],
    },
    'editorial-methodology': {
        'label': 'Editorial Methodology',
        'url': f'{BASE}/editorial-methodology/',
        'parents': [],
    },
    'ask': {
        'label': 'Ask Sibe',
        'url': f'{BASE}/ask/',
        'parents': [],
    },
}


def items(page):
    values = [('Home', f'{BASE}/')] + page['parents'] + [(page['label'], page['url'])]
    return [
        {'@type': 'ListItem', 'position': position, 'name': name, 'item': url}
        for position, (name, url) in enumerate(values, 1)
    ]


def breadcrumb(page):
    return {
        '@type': 'BreadcrumbList',
        '@id': f"{page['url']}#breadcrumb",
        'itemListElement': items(page),
    }


def update_graph(graph, page):
    breadcrumb_id = f"{page['url']}#breadcrumb"
    graph[:] = [item for item in graph if item.get('@type') != 'BreadcrumbList' and item.get('@id') != breadcrumb_id]
    for item in graph:
        if item.get('@type') == 'WebPage':
            item['breadcrumb'] = {'@id': breadcrumb_id}
    graph.append(breadcrumb(page))


def update_jsonld(path, page):
    data = json.loads(path.read_text(encoding='utf-8'))
    update_graph(data.setdefault('@graph', []), page)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


for slug, page in PAGES.items():
    html_path = ROOT / slug / 'index.html'
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    nav = soup.find('nav', class_='breadcrumb')
    if nav:
        nav.clear()
        home = soup.new_tag('a', href='/')
        home.string = 'Home'
        nav.append(home)
        for name, url in page['parents'] + [(page['label'], page['url'])]:
            separator = soup.new_tag('span', attrs={'aria-hidden': 'true'})
            separator.string = '›'
            nav.append(' ')
            nav.append(separator)
            nav.append(' ')
            if name == page['label']:
                current = soup.new_tag('span')
                current.string = name
                nav.append(current)
            else:
                parent = soup.new_tag('a', href=url)
                parent.string = name
                nav.append(parent)
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        if '@graph' not in data:
            continue
        update_graph(data['@graph'], page)
        script.string = json.dumps(data, indent=2, ensure_ascii=False)
        break
    html_path.write_text(str(soup), encoding='utf-8')
    update_jsonld(ROOT / slug / 'index.jsonld', page)
    print(f'fixed={slug} levels={len(page["parents"]) + 2}')

print('breadcrumb-hierarchy-fix=passed')
