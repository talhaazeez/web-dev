from pathlib import Path
from bs4 import BeautifulSoup
import json

path = Path('/home/ubuntu/web-dev/editorial-methodology/index.html')
url = 'https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing'
name = 'Google Cloud: Introducing the Open Knowledge Format'
soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
for script in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(script.string or script.get_text())
        graph = data.get('@graph', []) if isinstance(data, dict) else []
        webpage = next((item for item in graph if item.get('@type') == 'WebPage'), None)
        if webpage is None:
            continue
        citations = webpage.get('citation', [])
        if isinstance(citations, str): citations = [citations]
        if not any(isinstance(item, dict) and item.get('url') == url for item in citations):
            citations.append({'@type': 'CreativeWork', 'name': name, 'url': url, 'isPartOf': {'@type': 'CreativeWorkSeries', 'name': 'Open Knowledge Format'}})
            webpage['citation'] = citations
            script.string = json.dumps(data, indent=2, ensure_ascii=False)
    except Exception:
        continue
path.write_text(str(soup), encoding='utf-8')
print('okf-inline-schema-synced')
