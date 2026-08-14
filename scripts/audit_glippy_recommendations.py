from pathlib import Path
from bs4 import BeautifulSoup
import json
import re

ROOT = Path('/home/ubuntu/web-dev')
results = []
for page in sorted(ROOT.rglob('index.html')):
    soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
    headings = soup.find_all(['h1', 'h2', 'h3'])
    missing_ids = [h.get_text(' ', strip=True) for h in headings if not h.get('id')]
    images = soup.find_all('img')
    missing_lazy = [img.get('src', '') for img in images if not img.get('loading')]
    years = sorted(set(re.findall(r'\b(?:19|20)\d{2}\b', soup.get_text(' ', strip=True))))
    citations = soup.find_all(['cite', 'sup'])
    tables = soup.find_all('table')
    external_links = [a.get('href') for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
    sections = []
    for h in soup.find_all('h2'):
        text = h.find_next_sibling()
        sections.append({'heading': h.get_text(' ', strip=True), 'has_next_content': bool(text)})
    results.append({
        'page': str(page.relative_to(ROOT)),
        'headings': len(headings),
        'missing_heading_ids': missing_ids,
        'images': len(images),
        'missing_lazy_images': missing_lazy,
        'years': years,
        'citation_nodes': len(citations),
        'tables': len(tables),
        'external_links': len(external_links),
        'h2_sections': len(sections),
    })

Path('/home/ubuntu/web-dev/glippy-recommendations-site-audit.json').write_text(json.dumps(results, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
for row in results:
    print(json.dumps(row, ensure_ascii=False))
