from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
KICKERS = {
    'index.html': 'How to evaluate Sibe',
    'cloud-cad-management/index.html': 'A practical way to evaluate cloud CAD',
    'features/cad-file-management/index.html': 'For a clearer file workflow',
    'features/solidworks-revision-approval-workflow/index.html': 'Before a design is released',
    'features/solidworks-bom-management/index.html': 'What to check in the BOM workflow',
    'features/remote-team-collaboration-for-solidworks-teams/index.html': 'For teams working across locations',
    'cloud-pdm/solidworks-pdm-migration/index.html': 'A safer way to evaluate migration',
    'contact/index.html': 'Choose the right next step',
    'editorial-methodology/index.html': 'How we approach product information',
}

POLISH_STYLE = '''<style id="reader-experience-polish">
:where(main) p{ text-wrap:pretty }
:where(.hero,.head,.section-head) p{ max-width:68ch }
:where(.meta-line,.source-freshness){ letter-spacing:.01em }
:where(nav.breadcrumb){ margin-bottom:8px }
:where(a):focus-visible{ outline:3px solid rgba(223,63,131,.55); outline-offset:3px }
@media(max-width:700px){ :where(h1,h2,h3){ text-wrap:balance } }
</style>'''

updated = []
for path in sorted(ROOT.rglob('index.html')):
    rel = str(path.relative_to(ROOT))
    text = path.read_text(encoding='utf-8')
    original = text
    kicker = KICKERS.get(rel)
    if kicker:
        text = text.replace('<span class="bulk-kicker">Answer-ready summary</span>', f'<span class="bulk-kicker">{kicker}</span>', 1)
    text = text.replace('<strong>Short answer:</strong>', '<strong>In plain English:</strong>')
    text = text.replace('<h2 id="site-sources-title">Sources and verification</h2>', '<h2 id="site-sources-title">Sources we checked</h2>')
    text = text.replace('<strong>Trust and review resources:</strong>', '<strong>Need to verify something?</strong>')
    text = text.replace('This page is an original summary of Sibe’s public product and company information. Product descriptions are checked against official Sibe pages for the homepage, About, demo, security, pricing, and relevant feature documentation.', 'We prepared this page from Sibe’s public product and company information, checking product descriptions against the homepage, About, demo, security, pricing, and relevant feature documentation.')
    text = text.replace('This summary is an original explanation of the public Sibe product positioning; it is not a customer performance claim or fabricated case study.', 'We wrote this as a practical explanation of Sibe’s public product positioning. It is not a customer performance claim or a case study.')
    if 'id="reader-experience-polish"' not in text:
        text = text.replace('</head>', POLISH_STYLE + '</head>', 1)
    if text != original:
        path.write_text(text, encoding='utf-8')
        updated.append(rel)

print(f'reader-experience-polish=passed pages={len(updated)}')
for rel in updated:
    print(f'updated={rel}')
