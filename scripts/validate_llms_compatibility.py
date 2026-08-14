from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
short = ROOT / 'llms.txt'
full = ROOT / 'llms-full.txt'
assert short.exists() and full.exists()
short_text = short.read_text(encoding='utf-8')
full_text = full.read_text(encoding='utf-8')
for text in (short_text, full_text):
    assert 'https://sibe-cad.vercel.app/okf/index.md' in text
    assert 'https://sibe-cad.vercel.app/okf/page-map.md' in text
    assert 'https://sibe-cad.vercel.app/sitemap.xml' in text
    assert 'https://sibe-cad.vercel.app/ask/' in text
assert len(short_text) > 1000
assert len(full_text) > len(short_text)
robots = (ROOT / 'robots.txt').read_text(encoding='utf-8')
assert 'LLMS-TXT: https://sibe-cad.vercel.app/llms.txt' in robots
assert 'LLMS-FULL-TXT: https://sibe-cad.vercel.app/llms-full.txt' in robots
sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
for url in ('https://sibe-cad.vercel.app/llms.txt', 'https://sibe-cad.vercel.app/llms-full.txt', 'https://sibe-cad.vercel.app/okf/page-map.md'):
    assert f'<loc>{url}</loc>' in sitemap
html_files = sorted(ROOT.rglob('index.html'))
assert len(html_files) == 10
for path in html_files:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    assert soup.find('link', rel='alternate', href='/llms.txt')
    assert soup.find('link', rel='alternate', href='/llms-full.txt')
assert 'llms.txt' not in ''.join(p.read_text(encoding='utf-8') for p in (ROOT / 'okf').rglob('*.md'))
assert 'llms-full.txt' not in ''.join(p.read_text(encoding='utf-8') for p in (ROOT / 'okf').rglob('*.md'))
print('llms-compatibility-validation=passed pages=10 files=2')
