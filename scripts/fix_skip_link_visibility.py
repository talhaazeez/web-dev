from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
STYLE = '''<style id="skip-link-visibility-fix">.skip-link{position:fixed!important;left:12px!important;top:12px!important;z-index:10000!important;display:inline-flex!important;align-items:center!important;visibility:visible!important;opacity:1!important;background:#17121d!important;color:#fff!important;padding:10px 14px!important;border:2px solid #fff!important;border-radius:8px!important;text-decoration:none!important;font-weight:800!important;line-height:1.2!important;box-shadow:0 6px 18px rgba(23,18,29,.24)!important}.skip-link:hover,.skip-link:focus-visible{background:#7114b8!important;color:#fff!important;outline:3px solid #df3f83!important;outline-offset:3px}@media(max-width:700px){.skip-link{top:78px!important;left:12px!important}}</style>'''

for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    if 'id="skip-link-visibility-fix"' not in text:
        text = text.replace('</head>', STYLE + '\n</head>', 1)
        path.write_text(text, encoding='utf-8')
        print(f'updated={path.relative_to(ROOT)}')
    else:
        print(f'already-present={path.relative_to(ROOT)}')
