from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
head_links = '''<link rel="nlweb" href="/ask/" title="Sibe natural-language information endpoint"/>
<link rel="mcp-server-card" href="/.well-known/mcp/server-card.json" title="Sibe MCP server card"/>
<link rel="agent-card" href="/.well-known/agent-card.json" title="Sibe A2A agent card"/>
<link rel="agent-skills" href="/.well-known/agent-skills/index.json" title="Sibe Agent Skills index"/>
<link rel="ucp" href="/.well-known/ucp" title="Sibe UCP capability profile"/>'''

for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    if 'webmcp-agent.js' not in text:
        text = text.replace('</head>', head_links + '\n<script src="/webmcp-agent.js" defer></script>\n</head>', 1)
    if '>Ask Sibe</a>' not in text and path != ROOT / 'ask' / 'index.html':
        text = text.replace('</nav>', '<a href="/ask/">Ask Sibe</a></nav>', 1)
    path.write_text(text, encoding='utf-8')
    print(f'updated={path.relative_to(ROOT)}')
