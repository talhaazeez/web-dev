from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
LINK = '<link rel="alternate" type="text/markdown" href="/okf/index.md" title="Sibe Open Knowledge Format bundle"/>'
for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    if 'title="Sibe Open Knowledge Format bundle"' not in text:
        text = text.replace('</head>', LINK + '\n</head>', 1)
        path.write_text(text, encoding='utf-8')
        print(f'okf-link-added={path.relative_to(ROOT)}')
