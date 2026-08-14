from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
links = '<link href="/llms.txt" rel="alternate" title="Sibe compatibility summary" type="text/plain"/><link href="/llms-full.txt" rel="alternate" title="Sibe expanded compatibility summary" type="text/plain"/>'
updated = 0
for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    if 'href="/llms.txt"' in text:
        continue
    text = text.replace('</head>', links + '</head>', 1)
    path.write_text(text, encoding='utf-8')
    updated += 1
print(f'llms-discovery-links=passed pages={updated}')
