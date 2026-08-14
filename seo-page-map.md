# SEO page architecture

## Homepage: `/`

Primary intent: cloud CAD management for SolidWorks and cloud PDM for SolidWorks.

Expansion sections: cloud PDM versus shared drives, use cases by engineering role, and a concise topic hub linking to the supporting pages.

## Supporting keyword pages

| URL | Search intent | Primary keyword | Supporting themes |
|---|---|---|---|
| `/cloud-cad-management/` | Product/category | cloud CAD management for SolidWorks | cloud PDM, SolidWorks add-in, no servers, no VPN, remote access |
| `/features/cad-file-management/` | Feature | CAD file management with SolidWorks | file references, metadata, search, version history, check-in/check-out |
| `/features/solidworks-revision-approval-workflow/` | Workflow | SolidWorks revision approval workflow | In Progress, Pending Approval, Released, release notes, audit trail |
| `/features/solidworks-bom-management/` | Feature | SolidWorks BOM management | indented BOMs, assembly structure, custom properties, manufacturing exports |
| `/features/remote-team-collaboration-for-solidworks-teams/` | Use case | remote engineering collaboration | browser-based design review, suppliers, customers, secure sharing |
| `/cloud-pdm/solidworks-pdm-migration/` | Problem/solution | SolidWorks PDM migration | phased evaluation, file references, cloud adoption, migration planning |

## Linking rules

The homepage will link to every supporting page from relevant sections. Each supporting page will link back to the homepage, the free trial, pricing, demo, and two related topic pages. Anchor text will describe the destination naturally, for example “cloud CAD management for SolidWorks,” “SolidWorks revision approval workflow,” and “BOM management for manufacturing.”

## Structured-data rules

The homepage will use WebPage, SoftwareApplication, Organization, and FAQPage JSON-LD. Each supporting page will use WebPage, SoftwareApplication, BreadcrumbList, and FAQPage JSON-LD. The canonical URL, Open Graph URL, and JSON-LD WebPage URL will match each page’s production URL.

All copy will be original and based on the reviewed Sibe sitemap and page themes. It will not reproduce source page text or testimonials verbatim.
