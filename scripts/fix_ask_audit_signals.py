from pathlib import Path
from bs4 import BeautifulSoup
import re

path = Path('/home/ubuntu/web-dev/ask/index.html')
text = path.read_text(encoding='utf-8')
soup = BeautifulSoup(text, 'html.parser')
used = {node.get('id') for node in soup.find_all(id=True)}
for heading in soup.find_all(['h1','h2','h3']):
    if heading.get('id'):
        continue
    slug = re.sub(r'[^a-z0-9]+','-',heading.get_text(' ',strip=True).lower()).strip('-') or 'section'
    candidate = slug
    i = 2
    while candidate in used:
        candidate = f'{slug}-{i}'
        i += 1
    heading['id'] = candidate
    used.add(candidate)
for image in soup.find_all('img'):
    if image.get('loading') is None:
        image['loading'] = 'lazy'
path.write_text(str(soup), encoding='utf-8')
print('ask-audit-signals-fixed')
