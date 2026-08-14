from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
for path in sorted(ROOT.rglob('index.html')):
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    section = soup.find('section', class_='bulk-summary')
    if not section:
        continue
    kicker = section.find(class_='bulk-kicker')
    title = section.find('h2')
    lead = section.find('p', class_='bulk-lead')
    print(f'--- {path.relative_to(ROOT)} ---')
    print('kicker:', kicker.get_text(' ', strip=True) if kicker else '')
    print('title:', title.get_text(' ', strip=True) if title else '')
    print('lead:', lead.get_text(' ', strip=True) if lead else '')
