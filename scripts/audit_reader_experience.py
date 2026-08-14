from pathlib import Path
import re
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
for path in sorted(ROOT.rglob('index.html')):
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    for node in soup(['script', 'style', 'noscript']):
        node.decompose()
    text = ' '.join(soup.get_text(' ', strip=True).split())
    words = re.findall(r"\b[\w’'-]+\b", text)
    headings = [h.get_text(' ', strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])]
    links = [a.get_text(' ', strip=True) for a in soup.find_all('a')]
    print(f'{path.relative_to(ROOT)} words={len(words)} headings={len(headings)} links={len(links)} h1={headings[:1]}')
    print('  headings:', ' | '.join(headings[:8]))
    print('  guide_links:', ', '.join(x for x in links if any(k in x.lower() for k in ['learn', 'read', 'compare', 'start', 'demo', 'contact', 'verify', 'next', 'source'])))
