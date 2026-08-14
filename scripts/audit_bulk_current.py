from pathlib import Path
from bs4 import BeautifulSoup
import re

ROOT=Path('/home/ubuntu/web-dev')
for p in sorted(ROOT.rglob('index.html')):
    if p.parent.name=='ask':
        continue
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    main=soup.find('main') or soup
    text=main.get_text(' ',strip=True)
    words=len(re.findall(r"\b[\w’'-]+\b", text))
    print({
        'page':str(p.relative_to(ROOT)),
        'words':words,
        'h2':len(soup.find_all('h2')),
        'bulk_summary':bool(soup.find('section',class_='bulk-summary')),
        'proof_signals':len(soup.find_all(class_=re.compile('proof|bulk-card'))),
        'cite_nodes':len(soup.find_all('cite')),
        'definition_terms':len(soup.find_all('dt')),
        'ordered_steps':len(soup.select('ol li')),
        'tables':len(soup.find_all('table')),
        'direct_answer_patterns':sum(1 for ptag in soup.find_all('p') if re.match(r'^(Short answer|Yes|No|Sibe|The\s)', ptag.get_text(' ',strip=True), re.I)),
    })
