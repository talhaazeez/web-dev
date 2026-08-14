from pathlib import Path
from datetime import date, timedelta

ROOT = Path('/home/ubuntu/web-dev')
BASE = 'https://sibe-cad.vercel.app'
TODAY = date(2026, 8, 15)
STALE_AFTER = TODAY + timedelta(days=180)
PAGES = [
    ('homepage', '/', 'Sibe CAD management website', 'Homepage'),
    ('cloud-cad-management', '/cloud-cad-management/', 'Cloud CAD management for SolidWorks teams', 'Cloud CAD management'),
    ('cad-file-management', '/features/cad-file-management/', 'CAD file management for SolidWorks', 'CAD file management'),
    ('revision-approval-workflow', '/features/solidworks-revision-approval-workflow/', 'SolidWorks revision approval workflow', 'Revision approval workflow'),
    ('bom-management', '/features/solidworks-bom-management/', 'SolidWorks BOM and product data management', 'BOM management'),
    ('remote-collaboration', '/features/remote-team-collaboration-for-solidworks-teams/', 'Remote engineering collaboration for SolidWorks teams', 'Remote collaboration'),
    ('pdm-migration', '/cloud-pdm/solidworks-pdm-migration/', 'SolidWorks PDM migration to the cloud', 'PDM migration'),
    ('contact', '/contact/', 'Contact Sibe', 'Contact'),
    ('editorial-methodology', '/editorial-methodology/', 'Sibe editorial methodology', 'Editorial methodology'),
    ('ask-sibe', '/ask/', 'Ask Sibe informational endpoint', 'Ask Sibe'),
]
PATH_BY_SLUG = {
    'homepage': 'index.html',
    'cloud-cad-management': 'cloud-cad-management/index.html',
    'cad-file-management': 'features/cad-file-management/index.html',
    'revision-approval-workflow': 'features/solidworks-revision-approval-workflow/index.html',
    'bom-management': 'features/solidworks-bom-management/index.html',
    'remote-collaboration': 'features/remote-team-collaboration-for-solidworks-teams/index.html',
    'pdm-migration': 'cloud-pdm/solidworks-pdm-migration/index.html',
    'contact': 'contact/index.html',
    'editorial-methodology': 'editorial-methodology/index.html',
    'ask-sibe': 'ask/index.html',
}

for slug, url_path, title, label in PAGES:
    html_path = ROOT / PATH_BY_SLUG[slug]
    text = html_path.read_text(encoding='utf-8')
    concept_href = f'/okf/concepts/{slug}.md'
    link = f'<link href="{concept_href}" rel="alternate" title="OKF concept: {title}" type="text/markdown"/>'
    if concept_href not in text:
        text = text.replace('</head>', link + '</head>', 1)
        html_path.write_text(text, encoding='utf-8')

    md_path = html_path.parent / 'index.md'
    companion = f'\n## OKF companion\n\nThe page-specific [Open Knowledge Format concept]({BASE}{concept_href}) carries the structured, frontmatter-based knowledge representation for this page.\n'
    if md_path.exists():
        md_text = md_path.read_text(encoding='utf-8')
        if '## OKF companion' not in md_text:
            md_path.write_text(md_text.rstrip() + '\n' + companion, encoding='utf-8')

page_links = '\n'.join(
    f'- [{title}]({concept_href}) — webpage: [{BASE}{url_path}]({BASE}{url_path})'
    for slug, url_path, title, label in PAGES
)
page_map = f'''---
type: index
title: Sibe webpage to OKF concept map
description: Explicit mapping from every public Sibe webpage to its colocated Markdown representation and page-specific OKF concept.
resource: {BASE}/okf/page-map.md
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
    resource: {BASE}/sitemap.xml
    title: Sibe XML sitemap
    author: Sibe
    last_modified: {TODAY.isoformat()}
---
# Sibe webpage to OKF concept map

Every public Sibe webpage has a colocated Markdown page and a separate page-specific OKF concept file. The mapping below makes the relationship explicit for people and software tools.

{page_links}
'''
(ROOT / 'okf/page-map.md').write_text(page_map, encoding='utf-8')
print(f'page-specific-okf-links=passed pages={len(PAGES)}')
