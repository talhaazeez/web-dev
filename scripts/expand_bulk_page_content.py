from pathlib import Path
from html import escape

ROOT = Path('/home/ubuntu/web-dev')

CSS = '''<style id="bulk-summary-css">
.bulk-summary{padding:64px 0;background:linear-gradient(135deg,#fff 0%,#fbf7fd 100%);border-top:1px solid #eadff0;border-bottom:1px solid #eadff0}.bulk-summary .container{width:min(calc(100% - 36px),1120px);margin:0 auto}.bulk-summary .bulk-kicker{display:block;margin-bottom:8px;color:#8a52a8;font-size:11px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.bulk-summary h2{margin:0 0 12px;color:#241a2b;font-size:clamp(28px,4vw,44px);line-height:1.1;letter-spacing:-.035em}.bulk-summary .bulk-lead{max-width:820px;color:#6d6575;font-size:17px;line-height:1.65}.bulk-summary .bulk-lead strong{color:#432651}.bulk-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:28px}.bulk-card{padding:22px;border:1px solid #e6d9eb;border-radius:16px;background:#fff;box-shadow:0 10px 28px rgba(42,19,57,.05)}.bulk-card .bulk-label{display:block;color:#a26abb;font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}.bulk-card h3{margin:8px 0;color:#241a2b;font-size:20px;line-height:1.2}.bulk-card p{margin:0;color:#6d6575;line-height:1.6}.bulk-card cite{display:block;margin-top:12px;font-size:12px;font-style:normal;font-weight:800}.bulk-card cite a{color:#7114b8}.bulk-details{display:grid;grid-template-columns:180px 1fr;gap:12px 22px;margin:30px 0 0;padding:20px;border:1px solid #e6d9eb;border-radius:16px;background:#fff}.bulk-details dt{color:#7114b8;font-weight:900}.bulk-details dd{margin:0;color:#6d6575}.bulk-steps{display:grid;gap:10px;margin:28px 0 0;padding:0;list-style:none;counter-reset:bulk-step}.bulk-steps li{counter-increment:bulk-step;position:relative;padding:14px 16px 14px 48px;border:1px solid #e6d9eb;border-radius:12px;background:#fff;color:#6d6575}.bulk-steps li:before{content:counter(bulk-step);position:absolute;left:14px;top:13px;width:24px;height:24px;border-radius:8px;background:#17121d;color:#fff;text-align:center;font-weight:900}.bulk-steps strong{color:#241a2b}.bulk-note{margin-top:20px;color:#6d6575;font-size:13px}.bulk-note a{color:#7114b8;font-weight:800}@media(max-width:760px){.bulk-grid{grid-template-columns:1fr}.bulk-details{grid-template-columns:1fr;gap:5px}.bulk-details dd{margin-bottom:8px}}
</style>'''

DATA = {
    'index.html': {
        'id': 'homepage-key-takeaways',
        'title': 'Key takeaways for evaluating Sibe',
        'lead': 'Sibe is a cloud-first workspace for SolidWorks version control, CAD file management, revision approvals, BOM/product data, and browser-based collaboration. The fastest way to judge fit is to test one representative assembly rather than evaluating a clean demo folder.',
        'cards': [
            ('Proof point', '14-day evaluation', 'The published product positioning describes a 14-day free trial with no credit card required. Confirm current terms on the official pricing page.', 'https://www.sibe.io/pricing', 'Official pricing and trial details'),
            ('Workflow outcome', 'One controlled definition', 'Check-in/check-out, version history, approvals, BOM structure, and browser review can be evaluated around the same SolidWorks project.', '/cloud-cad-management/', 'Cloud CAD management overview'),
            ('Trust signal', 'Evidence-led review', 'Sibe publishes product, security, company, demo, pricing, and methodology resources so teams can verify plan-specific or security-sensitive claims.', '/editorial-methodology/', 'Editorial methodology'),
        ],
        'details': [('Best starting point', 'Use an assembly with references, repeated parts, custom properties, drawings, and a real review dependency.'), ('What to measure', 'Record how quickly the team finds the current revision, checks BOM structure, invites a reviewer, and traces the release decision.'), ('What remains to verify', 'Confirm current plan limits, supported file formats, export behavior, and permissions through the official Sibe route.')],
        'steps': ['Start with one representative SolidWorks assembly.', 'Connect the add-in and verify references, version history, metadata, and review status.', 'Invite a non-CAD reviewer and compare the handoff with the team’s current folder or spreadsheet process.'],
        'note': 'This summary is an original explanation of the public Sibe product positioning; it is not a customer performance claim or fabricated case study.'
    },
    'features/cad-file-management/index.html': {
        'id': 'cad-file-management-answer-summary',
        'title': 'What CAD file management changes for a SolidWorks team',
        'lead': 'Sibe CAD file management treats a SolidWorks project as a connected product definition: parts, drawings, subassemblies, references, metadata, and versions move together. That helps teams replace filename guessing with a workflow they can inspect and review.',
        'cards': [
            ('Problem', 'Disconnected references', 'Shared folders make it easy to open a part without understanding which assembly, drawing, or revision it belongs to.'),
            ('Solution', 'Reference-aware control', 'The native add-in and cloud workspace keep check-in/check-out, version history, metadata, and related files closer to the engineering context.'),
            ('Proof point', '14-day evaluation', 'Use a representative assembly during the published free-trial evaluation and verify the reference and review workflow on real project data.', 'https://www.sibe.io/pricing', 'Official pricing and trial details'),
        ],
        'details': [('Reference-aware', 'Parts, drawings, and subassemblies are evaluated as related CAD data rather than isolated filenames.'), ('Searchable context', 'Part numbers, descriptions, materials, project identifiers, and other available properties become easier to find outside the CAD window.'), ('Review outcome', 'A non-CAD reviewer can inspect selected information in a browser without requiring a SolidWorks seat, subject to workspace permissions.')],
        'steps': ['Choose an assembly with the references that usually create the most confusion.', 'Check it in, inspect the structure and metadata, and make one real design change.', 'Invite a reviewer and confirm that the version under review is the one the team intended to share.'],
        'note': 'Confirm current supported file types, search behavior, and permissions on the official Sibe demo route.'
    },
    'features/solidworks-bom-management/index.html': {
        'id': 'bom-management-answer-summary',
        'title': 'What SolidWorks BOM management should make easier',
        'lead': 'Sibe positions the managed SolidWorks assembly as the starting point for product data. The intended outcome is less duplicate entry between engineering, purchasing, manufacturing, and project teams because structure, metadata, quantity, and revision context stay connected.',
        'cards': [
            ('Problem', 'Spreadsheet drift', 'A manually maintained BOM can lag behind the assembly after a part, quantity, property, or revision changes.'),
            ('Solution', 'Assembly-led product data', 'Use nested assembly structure and SolidWorks custom properties as the starting point for an indented BOM workflow.'),
            ('Proof point', 'Downstream review', 'Evaluate whether purchasing and manufacturing can find the product structure they need without requesting a new spreadsheet export for every change.', '/features/solidworks-bom-management/', 'BOM management page'),
        ],
        'details': [('Structure', 'Nested subassemblies and component relationships show how the product is put together.'), ('Metadata', 'Part numbers, descriptions, materials, project identifiers, and other available properties can support downstream context.'), ('Control', 'Review BOM information alongside the relevant version or revision instead of an untracked snapshot.')],
        'steps': ['Check in an assembly with repeated parts and at least one subassembly.', 'Inspect structure, quantity, custom properties, and version context in the cloud workspace.', 'Ask a downstream stakeholder to use the resulting product data and record any missing fields or export requirements.'],
        'note': 'The page describes a workflow model; confirm exact export formats and plan capabilities for the specific manufacturing process.'
    },
    'features/solidworks-revision-approval-workflow/index.html': {
        'id': 'revision-approval-answer-summary',
        'title': 'What a visible revision approval workflow changes',
        'lead': 'Sibe describes a practical path from In Progress to Pending Approval to Released. The value is not another filename convention; it is a visible decision trail connecting the exact design version, release notes, reviewer feedback, and approved downstream definition.',
        'cards': [
            ('Problem', 'Release ambiguity', 'When approval status lives in email or filenames, manufacturing and suppliers may not know which design decision is final.'),
            ('Solution', 'Three visible states', 'In Progress, Pending Approval, and Released give the team a shared vocabulary for the design state.'),
            ('Proof point', 'Browser review', 'A controlled review can bring managers, quality teams, suppliers, and customers into the decision without requiring every reviewer to install SolidWorks.', '/features/remote-team-collaboration-for-solidworks-teams/', 'Remote collaboration page'),
        ],
        'details': [('In Progress', 'Engineers iterate in SolidWorks while check-in/check-out and version history record the changing design.'), ('Pending Approval', 'Release notes, comments, and markups give reviewers context for the decision.'), ('Released', 'The approved revision becomes the controlled definition for manufacturing, suppliers, and downstream work.')],
        'steps': ['Move a real design change into review with release context.', 'Invite a non-CAD reviewer to inspect the selected version and record feedback.', 'Release the decision and verify that the approved state is visible to the next team.'],
        'note': 'Confirm current workflow permissions, locking behavior, and approval configuration through the official Sibe demo route.'
    },
    'features/remote-team-collaboration-for-solidworks-teams/index.html': {
        'id': 'remote-collaboration-answer-summary',
        'title': 'What remote SolidWorks collaboration should preserve',
        'lead': 'Remote collaboration works when the team shares the same controlled design context, not when engineers repeatedly export screenshots and STEP files. Sibe connects SolidWorks version control with browser-based views for the people who need to review or act on the product definition.',
        'cards': [
            ('Problem', 'Review by attachment', 'Email chains and screenshots can separate feedback from the design version that prompted it.'),
            ('Solution', 'Role-appropriate access', 'Engineers continue in SolidWorks while project managers, customers, suppliers, quality teams, and reviewers use selected browser views.'),
            ('Proof point', 'No VPN project', 'The product is positioned around cloud access for distributed work without requiring a customer-managed PDM server and separate VPN project.', '/features/remote-team-collaboration-for-solidworks-teams/', 'Remote collaboration page'),
        ],
        'details': [('Engineering', 'Keep version history, references, revisions, and check-in/check-out connected to the native workflow.'), ('Reviewers', 'Inspect a selected 2D or 3D design without needing a SolidWorks license, subject to permissions.'), ('Decisions', 'Keep comments, markups, status, and release history associated with the design version under review.')],
        'steps': ['Choose a real project with a distributed reviewer or supplier dependency.', 'Share the selected version with only the role or partner that needs it.', 'Compare browser review, feedback capture, and release traceability with the current email workflow.'],
        'note': 'Access controls and external-sharing behavior should be confirmed for the current Sibe workspace and plan.'
    },
    'cloud-pdm/solidworks-pdm-migration/index.html': {
        'id': 'pdm-migration-answer-summary',
        'title': 'How to evaluate a SolidWorks PDM migration safely',
        'lead': 'A cloud PDM migration does not need to begin with a full historical data move. A safer evaluation starts with one representative project and tests references, version control, approvals, browser reviews, permissions, and downstream usability before a broader decision.',
        'cards': [
            ('Risk', 'Big-bang migration', 'Moving every file before validating the everyday workflow can make it difficult to isolate adoption, reference, and permission problems.'),
            ('Approach', 'Subset-based evaluation', 'Use a representative assembly and the people who need to engineer, review, approve, or consume its product data.'),
            ('Proof point', 'Phased trial', 'The published Sibe workflow supports a 14-day evaluation with no credit card required; confirm current terms before planning the test.', 'https://www.sibe.io/pricing', 'Official pricing and trial details'),
        ],
        'details': [('Validate references', 'Parts, drawings, and subassemblies should remain understandable in the controlled workspace.'), ('Validate collaboration', 'A manager, supplier, or customer should be able to review a controlled browser view with the intended permissions.'), ('Validate adoption', 'The engineering team should be able to use the workflow without creating a separate infrastructure project before the benefit is visible.')],
        'steps': ['Choose a project that contains the real friction the team wants to reduce.', 'Run check-in, version, review, and permission tests with a small group.', 'Document what worked, what needs configuration, and what should be confirmed before wider migration.'],
        'note': 'The migration page is an evaluation framework, not a promise that every legacy configuration or file type migrates automatically.'
    },
    'contact/index.html': {
        'id': 'contact-answer-summary',
        'title': 'Choose the right way to contact Sibe',
        'lead': 'The official Sibe demo route is the primary path for product questions, a walkthrough, and trial guidance. The page also records the Sibe, Inc. mailing address so readers can distinguish the customer-facing route from the legal entity information.',
        'cards': [
            ('Product questions', 'Request a demo', 'Use the official demo route so the request reaches the Customer Success team and the appropriate product experts.', 'https://www.sibe.io/demo', 'Official demo route'),
            ('Evaluation', 'Start the free trial', 'Teams that want to test the workflow directly can use the official trial route and begin with one representative assembly.', 'https://app.sibe.io/', 'Official trial route'),
            ('Entity record', 'Mailing address', 'Sibe, Inc. is listed at 8 The Green #23150, Dover, DE 19901, United States on the contact page.', '/contact/', 'Contact page'),
        ],
        'details': [('Best route for a walkthrough', 'Official demo page.'), ('Best route for a hands-on evaluation', 'Official Sibe trial page.'), ('Best route for entity verification', 'The mailing address and linked About, security, pricing, and methodology resources on this site.')],
        'steps': ['Describe the SolidWorks workflow or product-data issue you want to discuss.', 'Use the official demo route for a walkthrough or the official trial route for direct evaluation.', 'Confirm current plan, onboarding, response, and security details with the Sibe team.'],
        'note': 'This page does not claim a support email or phone number that is not published in the verified source material.'
    },
    'editorial-methodology/index.html': {
        'id': 'editorial-methodology-answer-summary',
        'title': 'How to interpret the Sibe product pages',
        'lead': 'The Sibe editorial pages are original product explanations built from first-party Sibe sources. They are designed to answer a specific SolidWorks or cloud CAD question while separating verified public claims from details that readers should confirm on the official product route.',
        'cards': [
            ('Sources', 'First-party evidence', 'Product, About, security, demo, pricing, and feature pages are used as the primary references for product descriptions.'),
            ('Editorial method', 'Original explanations', 'The pages summarize workflow concepts in original language rather than presenting third-party copy as Sibe editorial content.'),
            ('Freshness', 'Reviewed dates', 'Pages carry published and reviewed dates, with changes checked after deployment and current links maintained.', '/editorial-methodology/', 'Editorial methodology'),
        ],
        'details': [('Verified claim', 'A statement checked against a linked official Sibe page or an explicitly labeled public source.'), ('Plan-specific detail', 'A capability, export, permission, or commercial detail that should be confirmed on the current official route.'), ('Editorial update', 'A review of content, links, structured data, accessibility landmarks, and deployment status.')],
        'steps': ['Identify the specific SolidWorks or cloud CAD question a page is intended to answer.', 'Follow the cited official source links for product, security, pricing, and plan-specific details.', 'Use the published and reviewed dates to judge whether a claim needs reconfirmation before acting.'],
        'note': 'The methodology page intentionally avoids fabricated testimonials, unsupported statistics, and claims that cannot be checked against public sources.'
    },
}

for rel, item in DATA.items():
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    if 'id="bulk-summary-css"' not in text:
        text = text.replace('</head>', CSS + '\n</head>', 1)
    if f'id="{item["id"]}"' in text:
        path.write_text(text, encoding='utf-8')
        print(f'already-present={rel}')
        continue
    cards=[]
    for card in item['cards']:
        label, title, body, *link = card
        cite = f'<cite><a href="{escape(link[0])}">{escape(link[1])}</a></cite>' if link else ''
        cards.append(f'<article class="bulk-card"><span class="bulk-label">{escape(label)}</span><h3>{escape(title)}</h3><p>{escape(body)}</p>{cite}</article>')
    details=''.join(f'<dt>{escape(k)}</dt><dd>{escape(v)}</dd>' for k,v in item['details'])
    steps=''.join(f'<li><strong>Step {i}.</strong> {escape(step)}</li>' for i,step in enumerate(item['steps'],1))
    block=f'''<section class="bulk-summary" id="{item['id']}"><div class="container"><span class="bulk-kicker">Answer-ready summary</span><h2 id="{item['id']}-title">{escape(item['title'])}</h2><p class="bulk-lead"><strong>Short answer:</strong> {escape(item['lead'])}</p><div class="bulk-grid">{''.join(cards)}</div><dl class="bulk-details">{details}</dl><ol class="bulk-steps">{steps}</ol><p class="bulk-note">{escape(item['note'])} Read the <a href="/ask/">Ask Sibe endpoint</a> for an informational answer or use the official source linked above for current details.</p></div></section>'''
    marker = '<section class="site-sources"'
    if marker not in text:
        marker = '<section class="sources"'
    if marker not in text:
        raise RuntimeError(f'Source section not found: {rel}')
    text = text.replace(marker, block + '\n' + marker, 1)
    path.write_text(text, encoding='utf-8')
    print(f'expanded={rel}')
