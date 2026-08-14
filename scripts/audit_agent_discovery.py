from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT = Path('/home/ubuntu/web-dev')
rows = []
for page in sorted(ROOT.rglob('index.html')):
    soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
    rows.append({
        'page': str(page.relative_to(ROOT)),
        'forms': len(soup.find_all('form')),
        'webmcp_forms': len([f for f in soup.find_all('form') if f.get('toolname') and f.get('tooldescription')]),
        'model_context_usage': 'modelContext' in page.read_text(encoding='utf-8'),
        'agent_links': [a.get('href') for a in soup.find_all('a', href=True) if '/.well-known/' in a['href'] or a.get('rel') == ['nlweb']],
        'jsonld_types': [node.get('@type') for script in soup.find_all('script', attrs={'type': 'application/ld+json'}) for node in (json.loads(script.string).get('@graph', []) if script.string and isinstance(json.loads(script.string), dict) else []) if isinstance(node, dict)],
    })

discovery = {}
for rel in ['.well-known/ucp', '.well-known/mcp/server-card.json', '.well-known/agent-card.json', '.well-known/agent-skills/index.json']:
    p = ROOT / rel
    discovery[rel] = {'exists': p.exists(), 'bytes': p.stat().st_size if p.exists() else 0}

print(json.dumps({'pages': rows, 'discovery_files': discovery}, indent=2, ensure_ascii=False))
Path('/home/ubuntu/web-dev/agent-discovery-audit.json').write_text(json.dumps({'pages': rows, 'discovery_files': discovery}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
