from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT = Path('/home/ubuntu/web-dev')
html_pages = sorted(ROOT.rglob('index.html'))
assert len(html_pages) == 10, html_pages

for page in html_pages:
    text = page.read_text(encoding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    assert soup.find('link', rel='nlweb'), page
    assert soup.find('link', rel='mcp-server-card'), page
    assert soup.find('link', rel='agent-card'), page
    assert soup.find('link', rel='agent-skills'), page
    assert soup.find('link', rel='ucp'), page
    assert 'webmcp-agent.js' in text, page

ask = BeautifulSoup((ROOT / 'ask' / 'index.html').read_text(encoding='utf-8'), 'html.parser')
form = ask.find('form', attrs={'toolname': 'askSibe'})
assert form and form.get('tooldescription') and form.get('toolautosubmit') is not None
field = form.find(attrs={'name': 'q'})
assert field and field.get('toolparamdescription')
assert 'document.modelContext.registerTool' in (ROOT / 'ask' / 'index.html').read_text()
assert 'document.modelContext.registerTool' in (ROOT / 'webmcp-agent.js').read_text()

for path in [ROOT / '.well-known' / 'ucp', ROOT / '.well-known' / 'mcp' / 'server-card.json', ROOT / '.well-known' / 'agent-card.json', ROOT / '.well-known' / 'agent-skills' / 'index.json', ROOT / 'ask' / 'index.jsonld']:
    data = json.loads(path.read_text())
    assert isinstance(data, dict), path

sitemap = (ROOT / 'sitemap.xml').read_text()
assert '<loc>https://sibe-cad.vercel.app/ask/</loc>' in sitemap
schemamap = (ROOT / 'schemamap.xml').read_text()
assert 'https://sibe-cad.vercel.app/ask/index.jsonld' in schemamap
llms = (ROOT / 'llms.txt').read_text()
for token in ['/ask/', '/.well-known/ucp', '/.well-known/mcp/server-card.json', '/.well-known/agent-card.json', '/.well-known/agent-skills/index.json']:
    assert token in llms, token
print(f'agent-discovery-regression=passed pages={len(html_pages)}')
