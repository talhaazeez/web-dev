from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
STYLE = '''<style id="branding-alignment-fix">.brand{display:inline-flex;align-items:center;gap:9px;line-height:1;text-decoration:none}.brand-logo{display:block;width:34px;height:34px;flex:0 0 34px;object-fit:contain}.brand-wordmark{display:inline-flex;align-items:center;line-height:1;white-space:nowrap}.footer-row{display:flex;align-items:center;gap:20px;flex-wrap:wrap}.footer-brand{display:inline-flex;align-items:center;gap:9px;min-height:28px;line-height:1;text-decoration:none}.footer-brand img{display:block;width:28px;height:28px;flex:0 0 28px;object-fit:contain}.footer-brand>span{display:inline-flex;align-items:center;line-height:1;white-space:nowrap}@media(max-width:700px){.footer-brand{min-height:30px}}</style>'''

for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    if 'id="branding-alignment-fix"' not in text:
        text = text.replace('</head>', STYLE + '\n</head>', 1)
    path.write_text(text, encoding='utf-8')
    print(f'branding-alignment-fixed={path.relative_to(ROOT)}')
