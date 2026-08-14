from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT = Path('/home/ubuntu/web-dev')
EXPECTED = {
    'contact': ('Contact', 'https://sibe-cad.vercel.app/contact/'),
    'editorial-methodology': ('Editorial Methodology', 'https://sibe-cad.vercel.app/editorial-methodology/'),
    'ask': ('Ask Sibe', 'https://sibe-cad.vercel.app/ask/'),
}

for slug, (label, url) in EXPECTED.items():
    html_path = ROOT / slug / 'index.html'
    endpoint_path = ROOT / slug / 'index.jsonld'
    soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
    nav = soup.find('nav', class_='breadcrumb')
    assert nav and nav.get('aria-label') == 'Breadcrumb'
    links = nav.find_all('a')
    assert len(links) == 1 and links[0].get('href') == '/'
    visible = [part.strip() for part in nav.get_text(' ', strip=True).split('›')]
    assert visible == ['Home', label], (slug, visible)

    scripts = soup.find_all('script', type='application/ld+json')
    html_graph = None
    for script in scripts:
        try:
            data = json.loads(script.string or script.get_text())
        except json.JSONDecodeError:
            continue
        if '@graph' in data:
            html_graph = data['@graph']
            break
    endpoint_graph = json.loads(endpoint_path.read_text(encoding='utf-8'))['@graph']
    for graph, source in ((html_graph, html_path), (endpoint_graph, endpoint_path)):
        breadcrumb = next(item for item in graph if item.get('@type') == 'BreadcrumbList')
        items = breadcrumb['itemListElement']
        assert [item['position'] for item in items] == [1, 2], source
        assert items[0]['name'] == 'Home' and items[0]['item'] == 'https://sibe-cad.vercel.app/'
        assert items[1]['name'] == label and items[1]['item'] == url
        webpage = next(item for item in graph if item.get('@type') == 'WebPage')
        assert webpage['breadcrumb']['@id'] == breadcrumb['@id']
    print(f'breadcrumb-ok={slug}')

print('breadcrumb-regression=passed pages=3')
