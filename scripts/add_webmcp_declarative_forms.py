from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
SKIP = {'ask/index.html'}
FORM_STYLE = '''<style id="reader-webmcp-form-style">
.reader-ask{margin:56px auto 0;padding:34px 36px;border:1px solid #e4d4ec;border-radius:24px;background:radial-gradient(circle at 100% 0,rgba(223,63,131,.1),transparent 30%),linear-gradient(135deg,#fff,#fbf7fd);box-shadow:0 16px 38px rgba(42,19,57,.08)}
.reader-ask-inner{width:min(100%,860px);margin:0 auto}.reader-ask-kicker{display:block;margin-bottom:8px;color:#8a52a8;font-size:11px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.reader-ask h2{margin:0 0 10px;color:#241a2b;font-size:clamp(26px,4vw,42px);line-height:1.1}.reader-ask p{max-width:68ch;color:#6d6575}.reader-ask form{margin-top:20px}.reader-ask label{display:block;margin-bottom:7px;color:#432651;font-size:13px;font-weight:850}.reader-ask-row{display:flex;align-items:stretch;gap:10px}.reader-ask input{flex:1;min-width:0;padding:13px 15px;border:1px solid #d9c6e1;border-radius:12px;background:#fff;color:#241a2b;font:inherit}.reader-ask input:focus{outline:3px solid rgba(113,20,184,.18);border-color:#7114b8}.reader-ask button{padding:13px 18px;border:0;border-radius:12px;background:linear-gradient(100deg,#7114b8,#df3f83);color:#fff;font:inherit;font-weight:900;cursor:pointer}.reader-ask button:hover,.reader-ask button:focus-visible{filter:brightness(1.06)}.reader-ask-note{margin:12px 0 0!important;font-size:12px}.reader-ask-note a{color:#7114b8;font-weight:800}@media(max-width:700px){.reader-ask{margin-top:42px;padding:26px 22px}.reader-ask-row{display:grid}.reader-ask button{width:100%}}
</style>'''

updated = 0
for path in sorted(ROOT.rglob('index.html')):
    rel = str(path.relative_to(ROOT))
    if rel in SKIP:
        continue
    text = path.read_text(encoding='utf-8')
    if 'toolname="askSibe"' in text:
        continue
    slug = path.parent.as_posix().strip('./').replace('/', '-') or 'home'
    input_id = f'reader-question-{slug}'
    form = f'''<section aria-labelledby="reader-ask-title" class="reader-ask"><div class="reader-ask-inner"><span class="reader-ask-kicker">Questions welcome</span><h2 id="reader-ask-title">Want a clearer answer?</h2><p>Ask a focused question about the topic on this page. Sibe’s public information endpoint will point you to the relevant published source.</p><form action="/ask/" method="get" toolautosubmit="" toolname="askSibe" tooldescription="Answer a natural-language informational question using the published Sibe CAD website resources."><label for="{input_id}">Your question</label><div class="reader-ask-row"><input autocomplete="off" id="{input_id}" name="q" placeholder="For example: How does this fit a SolidWorks workflow?" required="" toolparamdescription="A natural-language question about Sibe cloud CAD management, SolidWorks workflows, the free trial, pricing, security, or contact options." type="text"/><button type="submit">Ask Sibe</button></div></form><p class="reader-ask-note">For plan limits and current commercial details, confirm the linked official Sibe source.</p></div></section>'''
    anchor = '<section class="site-sources"'
    if anchor in text:
        text = text.replace(anchor, form + anchor, 1)
    else:
        text = text.replace('</main>', form + '</main>', 1)
    if 'id="reader-webmcp-form-style"' not in text:
        text = text.replace('</head>', FORM_STYLE + '</head>', 1)
    path.write_text(text, encoding='utf-8')
    updated += 1
    print(f'webmcp-form-added={rel}')
print(f'webmcp-declarative-form-update=passed pages={updated}')
