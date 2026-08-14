from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
PAGES = [ROOT / 'contact/index.html', ROOT / 'editorial-methodology/index.html']

for path in PAGES:
    text = path.read_text(encoding='utf-8')
    text = text.replace(
        'header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:2}nav{',
        'header{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:2}header nav{',
        1,
    )
    text = text.replace(
        '.navcta{background:var(--ink);color:#fff!important;padding:9px 13px;border-radius:10px;font-weight:800}.skip-link{position:absolute;left:12px;top:-48px;z-index:1000;background:var(--ink);color:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:800}.skip-link:focus{top:12px}',
        '.navcta{background:var(--ink);color:#fff!important;padding:9px 13px;border-radius:10px;font-weight:800}.breadcrumb{width:min(calc(100% - 36px),var(--max));min-height:0;margin:0 auto;padding:18px 0 6px;display:flex;align-items:center;justify-content:flex-start;gap:10px;color:var(--muted);font-size:13px;line-height:1.4}.breadcrumb a{color:var(--p);font-weight:800;text-decoration:none}.breadcrumb span[aria-hidden="true"]{color:#b5a8ba}.skip-link{position:fixed;left:12px;top:12px;z-index:1000;background:var(--ink);color:#fff;padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:800;box-shadow:0 6px 18px rgba(23,18,29,.2)}.skip-link:focus,.skip-link:hover{background:var(--p);color:#fff}',
        1,
    )
    text = text.replace(
        '@media(max-width:700px){.navlinks{display:none}.grid:',
        '@media(max-width:700px){.navlinks{display:none}.skip-link{top:78px}.grid:',
        1,
    )
    path.write_text(text, encoding='utf-8')
    print(f'fixed={path.relative_to(ROOT)}')
