from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path('/home/ubuntu/web-dev')
OUT=ROOT/'bulk-page-summaries.txt'
chunks=[]
for p in sorted(ROOT.rglob('index.html')):
    if p.parent.name == 'ask':
        continue
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    main=soup.find('main')
    chunks.append(f'### {p.relative_to(ROOT)}\nTITLE: {soup.title.get_text(" ",strip=True) if soup.title else ""}\nH1: {[h.get_text(" ",strip=True) for h in soup.find_all("h1")]}\nH2: {[h.get_text(" ",strip=True) for h in soup.find_all("h2")]}\nTEXT: {(main.get_text(" ",strip=True) if main else soup.get_text(" ",strip=True))[:5000]}\n')
OUT.write_text('\n'.join(chunks)+'\n',encoding='utf-8')
print(f'wrote={OUT}')
