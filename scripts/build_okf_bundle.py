from pathlib import Path
from datetime import date, timedelta

ROOT = Path('/home/ubuntu/web-dev')
BUNDLE = ROOT / 'okf'
TODAY = date(2026, 8, 15)
STALE_AFTER = TODAY + timedelta(days=180)
OKF_SPEC = 'https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf'
OKF_INTRO = 'https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing'

pages = [
    {
        'slug': 'homepage', 'title': 'Sibe CAD management website', 'type': 'concept',
        'description': 'Public overview of Sibe cloud CAD management for SolidWorks teams, including trial, product positioning, and evaluation routes.',
        'resource': 'https://sibe-cad.vercel.app/', 'tags': ['sibe', 'cloud-cad', 'solidworks', 'pdm', 'trial'],
        'body': '''# Sibe CAD management website\n\nSibe is presented as a cloud CAD and PDM workspace for SolidWorks teams. The public homepage describes version control, CAD file management, revision approvals, BOM/product data, browser-based collaboration, and a 14-day free trial.\n\n## Related concepts\n\n- [Cloud CAD management](cloud-cad-management.md)\n- [Ask Sibe endpoint](ask-sibe.md)\n- [Contact Sibe](contact.md)\n- [Editorial methodology](editorial-methodology.md)\n\n## Verification\n\nConfirm current plan limits, supported file formats, and commercial terms on the official Sibe product and pricing routes.'''
    },
    {
        'slug': 'cloud-cad-management', 'title': 'Cloud CAD management for SolidWorks teams', 'type': 'concept',
        'description': 'Cloud CAD workflow covering SolidWorks version control, references, revisions, BOM context, and browser collaboration.',
        'resource': 'https://sibe-cad.vercel.app/cloud-cad-management/', 'tags': ['cloud-cad', 'solidworks', 'version-control', 'collaboration'],
        'body': '''# Cloud CAD management for SolidWorks teams\n\nCloud CAD management is described as a shared online workspace for SolidWorks files, references, versions, revisions, product data, and browser-based collaboration. The workflow is evaluated with a representative assembly before a broader rollout.\n\n## Related concepts\n\n- [CAD file management](cad-file-management.md)\n- [Revision approval workflow](revision-approval-workflow.md)\n- [BOM management](bom-management.md)\n- [Remote collaboration](remote-collaboration.md)\n- [PDM migration](pdm-migration.md)\n\n## Sources\n\nThe [official Sibe cloud CAD page](https://sibe-cad.vercel.app/cloud-cad-management/) and linked official Sibe sources provide the product context. The [Sibe editorial methodology](editorial-methodology.md) explains how public claims are reviewed.'''
    },
    {
        'slug': 'cad-file-management', 'title': 'CAD file management for SolidWorks', 'type': 'concept',
        'description': 'SolidWorks file, reference, metadata, version, check-in/check-out, and review workflow concept.',
        'resource': 'https://sibe-cad.vercel.app/features/cad-file-management/', 'tags': ['cad-files', 'solidworks', 'references', 'metadata'],
        'body': '''# CAD file management for SolidWorks\n\nThe CAD file management workflow focuses on keeping parts, assemblies, drawings, references, metadata, and versions connected to the SolidWorks workflow. Teams can evaluate how files are found, trusted, reviewed, and shared before standardizing a wider process.\n\n## Related concepts\n\n- [Cloud CAD management](cloud-cad-management.md)\n- [Revision approval workflow](revision-approval-workflow.md)\n- [Remote collaboration](remote-collaboration.md)'''
    },
    {
        'slug': 'revision-approval-workflow', 'title': 'SolidWorks revision approval workflow', 'type': 'concept',
        'description': 'Revision states, reviewer context, release decisions, and version-aware approval workflow for SolidWorks designs.',
        'resource': 'https://sibe-cad.vercel.app/features/solidworks-revision-approval-workflow/', 'tags': ['solidworks', 'revisions', 'approvals', 'release'],
        'body': '''# SolidWorks revision approval workflow\n\nThe revision workflow describes moving a design from In Progress to Pending Approval to Released while retaining version history, release notes, reviewer comments, markups, and decision context tied to the exact design version.\n\n## Related concepts\n\n- [CAD file management](cad-file-management.md)\n- [Cloud CAD management](cloud-cad-management.md)\n- [BOM management](bom-management.md)'''
    },
    {
        'slug': 'bom-management', 'title': 'SolidWorks BOM and product data management', 'type': 'concept',
        'description': 'Assembly-aware BOM, custom properties, nested subassemblies, version-aware product data, and manufacturing export context.',
        'resource': 'https://sibe-cad.vercel.app/features/solidworks-bom-management/', 'tags': ['solidworks', 'bom', 'product-data', 'assemblies'],
        'body': '''# SolidWorks BOM and product data management\n\nThe BOM workflow uses SolidWorks assembly structure and part metadata as a starting point for an indented bill of materials and downstream product data. Nested subassemblies, custom properties, versions, manufacturing exports, purchasing, and production planning are connected to the design context.\n\n## Related concepts\n\n- [Cloud CAD management](cloud-cad-management.md)\n- [CAD file management](cad-file-management.md)\n- [Revision approval workflow](revision-approval-workflow.md)'''
    },
    {
        'slug': 'remote-collaboration', 'title': 'Remote engineering collaboration for SolidWorks teams', 'type': 'concept',
        'description': 'Distributed engineering workflow with controlled design views, permissions, comments, markups, and review history.',
        'resource': 'https://sibe-cad.vercel.app/features/remote-team-collaboration-for-solidworks-teams/', 'tags': ['remote-work', 'solidworks', 'collaboration', 'browser-review'],
        'body': '''# Remote engineering collaboration for SolidWorks teams\n\nDistributed teams can work around the same controlled design version while engineers continue in SolidWorks and project managers, customers, suppliers, quality teams, and reviewers use browser-based views. The public workflow emphasizes controlled access, comments, markups, and review history.\n\n## Related concepts\n\n- [Cloud CAD management](cloud-cad-management.md)\n- [CAD file management](cad-file-management.md)\n- [PDM migration](pdm-migration.md)'''
    },
    {
        'slug': 'pdm-migration', 'title': 'SolidWorks PDM migration to the cloud', 'type': 'concept',
        'description': 'Phased cloud PDM migration evaluation using a representative assembly, references, permissions, reviews, and release workflow.',
        'resource': 'https://sibe-cad.vercel.app/cloud-pdm/solidworks-pdm-migration/', 'tags': ['pdm', 'migration', 'solidworks', 'cloud'],
        'body': '''# SolidWorks PDM migration to the cloud\n\nThe migration approach recommends a phased evaluation instead of beginning with a large infrastructure change. A representative assembly can validate references, subassemblies, version control, approvals, remote reviews, permissions, and day-to-day usability before a wider migration decision.\n\n## Related concepts\n\n- [Cloud CAD management](cloud-cad-management.md)\n- [Remote collaboration](remote-collaboration.md)\n- [Revision approval workflow](revision-approval-workflow.md)'''
    },
    {
        'slug': 'contact', 'title': 'Contact Sibe', 'type': 'concept',
        'description': 'Official Sibe demo route, evaluation path, and public company mailing address.',
        'resource': 'https://sibe-cad.vercel.app/contact/', 'tags': ['contact', 'demo', 'trial', 'sibe'],
        'body': '''# Contact Sibe\n\nThe official Sibe demo route is the primary path for product questions, a walkthrough, and trial guidance. The page also records the Sibe, Inc. mailing address so readers can distinguish the customer-facing route from legal-entity information.\n\n## Related concepts\n\n- [Sibe CAD management website](homepage.md)\n- [Editorial methodology](editorial-methodology.md)\n- [Ask Sibe endpoint](ask-sibe.md)\n\nUse the official [Sibe demo page](https://www.sibe.io/demo) for current contact and product details.'''
    },
    {
        'slug': 'editorial-methodology', 'title': 'Sibe editorial methodology', 'type': 'concept',
        'description': 'Editorial source, review, freshness, accessibility, structured-data, and deployment-verification process.',
        'resource': 'https://sibe-cad.vercel.app/editorial-methodology/', 'tags': ['editorial', 'sources', 'verification', 'freshness'],
        'body': f'''# Sibe editorial methodology\n\nSibe product education pages are written as original explanations and checked against official Sibe product, About, security, demo, pricing, and feature pages. The editorial team makes a final pass for clarity, context, and natural phrasing so the guidance is useful to people who work with CAD data. Pages carry publication and review dates, source links, accessibility landmarks, structured data, and post-deployment route checks.\n\n## External OKF reference\n\nGoogle Cloud describes the [Open Knowledge Format]({OKF_INTRO}) as a vendor-neutral, Markdown-based format for portable knowledge that people and software tools can read. This Sibe bundle follows the repository’s plain-Markdown and YAML-frontmatter approach; it is published as a Sibe knowledge bundle and does not claim certification by Google.\n\n## Related concepts\n\n- [Sibe CAD management website](homepage.md)\n- [Contact Sibe](contact.md)\n- [Google Cloud OKF reference](../references/google-cloud-okf.md)'''
    },
    {
        'slug': 'ask-sibe', 'title': 'Ask Sibe informational endpoint', 'type': 'concept',
        'description': 'Read-only natural-language information endpoint for public Sibe CAD resources with declarative WebMCP support.',
        'resource': 'https://sibe-cad.vercel.app/ask/', 'tags': ['ask', 'webmcp', 'information', 'sibe'],
        'body': '''# Ask Sibe informational endpoint\n\nAsk Sibe provides read-only informational answers about public Sibe CAD content, including cloud CAD management, SolidWorks version control, BOM workflows, browser collaboration, trial details, pricing links, security links, and contact options. It does not access private workspaces, create accounts, process payments, change subscriptions, or perform destructive actions.\n\n## Related concepts\n\n- [Sibe CAD management website](homepage.md)\n- [Contact Sibe](contact.md)\n- [Editorial methodology](editorial-methodology.md)'''
    },
]

reference = {
    'slug': 'google-cloud-okf', 'title': 'Google Cloud Open Knowledge Format reference', 'type': 'reference',
    'description': 'External reference for the Open Knowledge Format specification and repository conventions.',
    'resource': OKF_INTRO, 'tags': ['okf', 'open-format', 'knowledge-bundle', 'provenance'],
    'body': f'''# Google Cloud Open Knowledge Format reference\n\nThe [Google Cloud OKF introduction]({OKF_INTRO}) presents a portable, vendor-neutral format based on Markdown files with YAML frontmatter. The [GoogleCloudPlatform knowledge-catalog OKF repository]({OKF_SPEC}) provides reference bundles and implementation conventions.\n\nThis Sibe bundle uses concept files, YAML frontmatter, progressive-disclosure indexes, normal Markdown cross-links, provenance fields, and freshness metadata. It is an independent Sibe publication and does not imply Google certification or endorsement.'''
}


def yaml_value(value, indent=''):
    if isinstance(value, list):
        return '[' + ', '.join(value) + ']'
    return str(value)


def render(doc, path):
    source_lines = [
        '  - id: sibe-page',
        f'    resource: {doc["resource"]}',
        f'    title: {doc["title"]}',
        '    author: Sibe',
        f'    last_modified: {TODAY.isoformat()}',
    ]
    if doc['type'] == 'reference':
        source_lines.extend([
            '  - id: google-cloud-okf',
            f'    resource: {OKF_SPEC}',
            '    title: GoogleCloudPlatform knowledge-catalog OKF repository',
            '    author: Google Cloud',
            f'    last_modified: {TODAY.isoformat()}',
        ])
    frontmatter = '\n'.join([
        '---',
        f'type: {doc["type"]}',
        f'title: {doc["title"]}',
        f'description: {doc["description"]}',
        f'resource: {doc["resource"]}',
        f'tags: {yaml_value(doc["tags"])}',
        'generated:',
        '  by: sibe-editorial-team',
        f'  at: {TODAY.isoformat()}T00:00:00Z',
        'verified:',
        '  - by: sibe-editorial-team',
        f'    at: {TODAY.isoformat()}T00:00:00Z',
        'status: stable',
        f'stale_after: {STALE_AFTER.isoformat()}',
        'sources:',
        *source_lines,
        '---',
        '',
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(frontmatter + doc['body'].strip() + '\n', encoding='utf-8')

# Reset and create the bundle directories.
if BUNDLE.exists():
    for item in sorted(BUNDLE.rglob('*'), reverse=True):
        if item.is_file(): item.unlink()
        elif item.is_dir(): item.rmdir()
else:
    BUNDLE.mkdir()

(BUNDLE / 'concepts').mkdir(parents=True, exist_ok=True)
(BUNDLE / 'references').mkdir(parents=True, exist_ok=True)

render({
    'slug': 'bundle', 'title': 'Sibe Open Knowledge Format bundle', 'type': 'bundle',
    'description': 'Portable Sibe CAD knowledge bundle containing public product concepts, trust resources, and provenance.',
    'resource': 'https://sibe-cad.vercel.app/okf/', 'tags': ['sibe', 'okf', 'cloud-cad', 'solidworks', 'public-knowledge'],
    'body': f'''# Sibe Open Knowledge Format bundle\n\nThis directory is a portable Sibe knowledge bundle made from Markdown concept files with YAML frontmatter. It covers public Sibe CAD product, workflow, contact, editorial, and informational endpoint concepts.\n\nThe bundle follows the plain-Markdown, frontmatter, cross-link, provenance, and progressive-disclosure conventions described in the [GoogleCloudPlatform OKF repository]({OKF_SPEC}). It is an independent Sibe bundle and does not claim formal Google certification.\n\n## Subdirectories\n\n- [Concepts](concepts/index.md) — public Sibe product and trust concepts.\n- [Page map](page-map.md) — explicit mapping from every public webpage to its colocated Markdown page and OKF concept.\n- [References](references/index.md) — external format and provenance references.\n\n## Freshness\n\nThe bundle was generated and verified by the Sibe Editorial Team on {TODAY.isoformat()}. Concepts carry `stale_after: {STALE_AFTER.isoformat()}` and should be rechecked against their linked sources after that date.'''
}, BUNDLE / 'index.md')

for doc in pages:
    render(doc, BUNDLE / 'concepts' / f'{doc["slug"]}.md')
render(reference, BUNDLE / 'references' / 'google-cloud-okf.md')

concept_links = '\n'.join([f'- [{doc["title"]}]({doc["slug"]}.md) — {doc["description"]}' for doc in pages])
(BUNDLE / 'concepts/index.md').write_text('''# Sibe concepts\n\nThe concepts below describe public Sibe product workflows, trust resources, and informational surfaces. Each file carries YAML frontmatter with type, resource, provenance, verification, status, and freshness metadata.\n\n''' + concept_links + '\n', encoding='utf-8')
page_links = '\n'.join([f'- [{doc["title"]}](concepts/{doc["slug"]}.md) — webpage: [{doc["resource"]}]({doc["resource"]})' for doc in pages])
(BUNDLE / 'page-map.md').write_text(f'''---
type: index
title: Sibe webpage to OKF concept map
description: Explicit mapping from every public Sibe webpage to its colocated Markdown representation and page-specific OKF concept.
resource: https://sibe-cad.vercel.app/okf/page-map.md
tags: [sibe, okf, pages, mapping]
generated:
  by: sibe-editorial-team
  at: {TODAY.isoformat()}T00:00:00Z
verified:
  - by: sibe-editorial-team
    at: {TODAY.isoformat()}T00:00:00Z
status: stable
stale_after: {STALE_AFTER.isoformat()}
sources:
  - id: sibe-page
    resource: https://sibe-cad.vercel.app/sitemap.xml
    title: Sibe XML sitemap
    author: Sibe
    last_modified: {TODAY.isoformat()}
---
# Sibe webpage to OKF concept map

Every public Sibe webpage has a colocated Markdown page and a separate page-specific OKF concept file. The mapping below makes the relationship explicit for people and software tools.

{page_links}
''', encoding='utf-8')
(BUNDLE / 'references/index.md').write_text(f'''# References\n\n- [Google Cloud Open Knowledge Format reference](google-cloud-okf.md) — Background and repository conventions for portable Markdown knowledge bundles.\n- [GoogleCloudPlatform knowledge-catalog OKF repository]({OKF_SPEC}) — External implementation reference.\n''', encoding='utf-8')
(BUNDLE / 'log.md').write_text(f'''# Bundle log\n\n- {TODAY.isoformat()} — Initial Sibe OKF bundle generated and verified by the Sibe Editorial Team.\n- {TODAY.isoformat()} — Sources use public Sibe pages and the linked Google Cloud OKF reference.\n''', encoding='utf-8')

print(f'okf-bundle-created files={len(list(BUNDLE.rglob("*.md")))}')
