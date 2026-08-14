from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT = Path('/home/ubuntu/web-dev')
OKF_URL = 'https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing'

html_path = ROOT / 'editorial-methodology/index.html'
soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
for node in soup.select('#site-sources p.external-reference'):
    node.decompose()
for script in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(script.string or script.get_text())
        for item in data.get('@graph', []):
            if item.get('@type') == 'WebPage' and 'citation' in item:
                citations = item['citation']
                if isinstance(citations, dict): citations = [citations]
                item['citation'] = [citation for citation in citations if citation.get('url') != OKF_URL]
                if not item['citation']:
                    item.pop('citation', None)
        script.string = json.dumps(data, indent=2, ensure_ascii=False)
    except Exception:
        continue
html_path.write_text(str(soup), encoding='utf-8')

md_path = ROOT / 'editorial-methodology/index.md'
lines = md_path.read_text(encoding='utf-8').splitlines()
filtered = []
skip = False
for line in lines:
    if line.strip() == '## External format reference':
        skip = True
        continue
    if skip and line.startswith('## '):
        skip = False
    if not skip:
        filtered.append(line)
md_path.write_text('\n'.join(filtered).rstrip() + '\n', encoding='utf-8')

jsonld_path = ROOT / 'editorial-methodology/index.jsonld'
data = json.loads(jsonld_path.read_text(encoding='utf-8'))
for item in data.get('@graph', []):
    if item.get('@type') == 'WebPage' and 'citation' in item:
        citations = item['citation']
        if isinstance(citations, dict): citations = [citations]
        item['citation'] = [citation for citation in citations if citation.get('url') != OKF_URL]
        if not item['citation']:
            item.pop('citation', None)
jsonld_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('methodology-okf-reference-removed')
