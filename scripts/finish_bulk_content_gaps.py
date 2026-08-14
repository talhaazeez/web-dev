from pathlib import Path

ROOT=Path('/home/ubuntu/web-dev')

cloud=ROOT/'cloud-cad-management/index.html'
text=cloud.read_text(encoding='utf-8')
if 'id="cloud-cad-answer-summary"' not in text:
    css='''<style id="cloud-bulk-summary-css">.cloud-bulk-summary{padding:64px 0;background:#fbf7fd;border-top:1px solid #e6d9eb;border-bottom:1px solid #e6d9eb}.cloud-bulk-summary .container{width:min(calc(100% - 36px),1120px);margin:0 auto}.cloud-bulk-summary .kicker{display:block;margin-bottom:8px;color:#8a52a8;font-size:11px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.cloud-bulk-summary h2{margin:0 0 12px;color:#241a2b;font-size:clamp(28px,4vw,44px);line-height:1.1}.cloud-bulk-summary .lead{max-width:820px;color:#6d6575;font-size:17px}.cloud-bulk-summary .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px}.cloud-bulk-summary article{padding:20px;border:1px solid #e6d9eb;border-radius:16px;background:#fff}.cloud-bulk-summary article strong{display:block;margin-bottom:8px;color:#7114b8}.cloud-bulk-summary article p{margin:0;color:#6d6575}.cloud-bulk-summary dl{display:grid;grid-template-columns:170px 1fr;gap:10px 20px;margin:26px 0;padding:20px;border:1px solid #e6d9eb;border-radius:16px;background:#fff}.cloud-bulk-summary dt{color:#7114b8;font-weight:900}.cloud-bulk-summary dd{margin:0;color:#6d6575}.cloud-bulk-summary ol{margin:24px 0 0;padding-left:24px;color:#6d6575}.cloud-bulk-summary li{padding:6px 0}.cloud-bulk-summary cite{display:block;margin-top:10px;font-size:12px;font-style:normal;font-weight:800}.cloud-bulk-summary cite a{color:#7114b8}@media(max-width:760px){.cloud-bulk-summary .cards{grid-template-columns:1fr}.cloud-bulk-summary dl{grid-template-columns:1fr}.cloud-bulk-summary dd{margin-bottom:8px}}</style>'''
    block='''<section class="cloud-bulk-summary" id="cloud-cad-answer-summary"><div class="container"><span class="kicker">Answer-ready summary</span><h2 id="cloud-cad-answer-summary-title">What cloud CAD management should make easier</h2><p class="lead"><strong>Short answer:</strong> Cloud CAD management gives SolidWorks teams a shared place to control versions, product structure, approvals, and browser reviews without beginning with a customer-managed server project.</p><div class="cards"><article><strong>Proof point</strong><p>The published Sibe positioning describes a 14-day free trial, no credit card required, and quick setup. Confirm current terms on the official pricing page.</p><cite><a href="https://www.sibe.io/pricing">Official pricing and trial details</a></cite></article><article><strong>Outcome to validate</strong><p>Use one real assembly to compare version discovery, reference handling, BOM context, and review status with the team’s current shared-drive workflow.</p><cite><a href="/cloud-cad-management/">Cloud CAD management page</a></cite></article><article><strong>Authority signal</strong><p>Product, security, company, demo, pricing, and methodology pages provide first-party context for the claims represented here.</p><cite><a href="/editorial-methodology/">Editorial methodology</a></cite></article></div><dl><dt>Current version</dt><dd>Check-in/check-out and version history help the team identify the design state being worked on or reviewed.</dd><dt>Product definition</dt><dd>Assembly references, metadata, BOM structure, revisions, and review context stay connected to the CAD workflow.</dd><dt>Evaluation method</dt><dd>Start with a representative project, invite the people who review or consume it, and record what needs confirmation before a wider rollout.</dd></dl><ol><li><strong>Choose:</strong> an assembly with the references and review friction the team actually experiences.</li><li><strong>Connect:</strong> the SolidWorks workflow and test version, metadata, product structure, and browser review.</li><li><strong>Decide:</strong> what the team can standardize now and what should be confirmed with the official Sibe team.</li></ol></div></section>'''
    marker='<section class="sources"'
    text=text.replace('</head>',css+'\n</head>',1)
    text=text.replace(marker,block+'\n'+marker,1)
    cloud.write_text(text,encoding='utf-8')
    print('cloud-summary-added')

comparison_data={
'features/cad-file-management/index.html': [('Current friction','Disconnected parts, drawings, and filenames','Reference-aware product context'),('Version control','Manual naming and folder checks','Check-in/check-out and visible history'),('Review outcome','Screenshots or exports','Controlled browser review')],
'features/solidworks-bom-management/index.html': [('Source','A spreadsheet snapshot','The managed SolidWorks assembly'),('Context','Manual properties and quantities','Assembly structure and custom properties'),('Downstream use','Repeated exports and reconciliation','Structured product data for review and manufacturing')],
'features/solidworks-revision-approval-workflow/index.html': [('Status','Filenames and email decisions','In Progress, Pending Approval, Released'),('Evidence','Separate comments and notes','Release notes, markups, and version history'),('Handoff','Unclear approved revision','Visible controlled definition')],
'features/remote-team-collaboration-for-solidworks-teams/index.html': [('Review','Attachments and screenshots','Selected browser design view'),('Access','Broad file sharing or manual exports','Role-appropriate controlled access'),('Decision','Feedback detached from version','Comments and review history tied to the design')],
'cloud-pdm/solidworks-pdm-migration/index.html': [('Migration start','Move everything before validation','Test one representative project'),('Risk control','Unknown references and permissions','Validate references, access, reviews, and releases'),('Decision','Big-bang rollout assumption','Evidence-led phased rollout decision')],
}
for rel, rows in comparison_data.items():
    path=ROOT/rel
    text=path.read_text(encoding='utf-8')
    if 'class="bulk-comparison"' in text:
        continue
    table='<div class="bulk-comparison"><h3 id="'+rel.split('/')[0]+'-workflow-comparison">Workflow comparison</h3><table class="comparison"><caption>Current workflow friction compared with the Sibe workflow described on this page.</caption><thead><tr><th scope="col">Workflow need</th><th scope="col">Common manual approach</th><th scope="col">Sibe workflow to evaluate</th></tr></thead><tbody>'
    for need, manual, sibe in rows:
        table += f'<tr><th scope="row">{need}</th><td>{manual}</td><td>{sibe}</td></tr>'
    table += '</tbody></table></div>'
    marker='<p class="bulk-note">'
    if marker not in text:
        raise RuntimeError(f'bulk note not found: {rel}')
    text=text.replace(marker,table+marker,1)
    path.write_text(text,encoding='utf-8')
    print(f'comparison-added={rel}')
