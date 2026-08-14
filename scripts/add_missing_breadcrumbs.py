from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
PAGES = {
    'contact': {
        'label': 'Contact',
        'url': 'https://sibe-cad.vercel.app/contact/',
        'path': '/contact/',
    },
    'editorial-methodology': {
        'label': 'Editorial Methodology',
        'url': 'https://sibe-cad.vercel.app/editorial-methodology/',
        'path': '/editorial-methodology/',
    },
    'ask': {
        'label': 'Ask Sibe',
        'url': 'https://sibe-cad.vercel.app/ask/',
        'path': '/ask/',
    },
}

BREADCRUMB_STYLE = (
    '<style id="breadcrumb-nav-fix">'
    '.breadcrumb{width:min(calc(100% - 36px),1120px);margin:0 auto;padding:18px 0 6px;display:flex;align-items:center;gap:10px;color:#6d6575;font-size:13px;line-height:1.4}'
    '.breadcrumb a{color:#7114b8;font-weight:800;text-decoration:none}'
    '.breadcrumb a:hover,.breadcrumb a:focus-visible{text-decoration:underline}'
    '.breadcrumb span[aria-hidden="true"]{color:#b5a8ba}'
    '</style>'
)


def breadcrumb_graph(page):
    return {
        '@type': 'BreadcrumbList',
        '@id': f"https://sibe-cad.vercel.app{page['path']}#breadcrumb",
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Sibe', 'item': 'https://sibe-cad.vercel.app/'},
            {'@type': 'ListItem', 'position': 2, 'name': page['label'], 'item': page['url']},
        ],
    }


def update_jsonld(path, page):
    data = json.loads(path.read_text(encoding='utf-8'))
    graph = data.setdefault('@graph', [])
    breadcrumb_id = f"https://sibe-cad.vercel.app{page['path']}#breadcrumb"
    graph[:] = [item for item in graph if item.get('@id') != breadcrumb_id]
    for item in graph:
        if item.get('@type') == 'WebPage':
            item['breadcrumb'] = {'@id': breadcrumb_id}
    graph.append(breadcrumb_graph(page))
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


for slug, page in PAGES.items():
    html_path = ROOT / slug / 'index.html'
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    main = soup.find('main')
    if main and not main.find('nav', class_='breadcrumb'):
        nav = soup.new_tag('nav', attrs={'aria-label': 'Breadcrumb', 'class': 'breadcrumb'})
        home = soup.new_tag('a', href='/')
        home.string = 'Home'
        separator = soup.new_tag('span', attrs={'aria-hidden': 'true'})
        separator.string = '›'
        current = soup.new_tag('span')
        current.string = page['label']
        nav.extend([home, ' ', separator, ' ', current])
        main.insert(0, nav)
    if slug == 'ask' and not soup.find('style', id='breadcrumb-nav-fix'):
        soup.head.append(BeautifulSoup(BREADCRUMB_STYLE, 'html.parser'))
    for script in soup.find_all('script', type='application/ld+json'):
        try:
            data = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        if '@graph' not in data:
            continue
        breadcrumb_id = f"https://sibe-cad.vercel.app{page['path']}#breadcrumb"
        data['@graph'] = [item for item in data['@graph'] if item.get('@id') != breadcrumb_id]
        for item in data['@graph']:
            if item.get('@type') == 'WebPage':
                item['breadcrumb'] = {'@id': breadcrumb_id}
        data['@graph'].append(breadcrumb_graph(page))
        script.string = json.dumps(data, indent=2, ensure_ascii=False)
        break
    html_path.write_text(str(soup), encoding='utf-8')
    update_jsonld(ROOT / slug / 'index.jsonld', page)

print('missing-breadcrumbs-added')
