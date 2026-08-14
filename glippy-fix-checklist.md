# Glippy report fix checklist

Source: attached Glippy report for https://sibe-cad.vercel.app/cloud-cad-management/, generated 2026-08-15.

## High-impact fixes to implement

| Report finding | Evidence in report | Fix decision |
|---|---|---|
| Schema is incomplete | One WebPage block; missing FAQPage; SoftwareApplication missing offers; WebPage missing description/date fields | Add consistent WebPage, Organization, SoftwareApplication, Offer, BreadcrumbList, and FAQPage JSON-LD to the relevant pages. Add datePublished/dateModified, author/publisher, featureList, operatingSystem, and a free-trial Offer where supported by existing site copy. |
| Thin content warning | Report measured 99 words on the audited page, while the current repository contains expanded copy | Add answer-sized definitions, a visible summary, workflow steps, and FAQ content to the audited page; verify the deployed page after changes. |
| No skip link | Report says no skip-to-content link | Add a keyboard-accessible skip link and a matching main-content id to every page. |
| Weak internal discovery | Report counted seven internal links and found no breadcrumbs or in-page anchors | Add breadcrumbs, a compact contents block, section ids, and contextual links to all supporting pages. |
| Meta description too long | Report measured 168 characters | Keep the audited page description within approximately 150–160 characters and normalize descriptions across supporting pages. |
| No Twitter Card metadata | Report found no/few Twitter Card tags | Add summary_large_image Twitter metadata and social image references using the existing favicon/logo asset where no dedicated social image exists. |
| Weak entity signals | Report found no author, date, About/Contact, privacy/terms, credentials, editorial policy, or contact information | Add visible “Reviewed and updated” metadata, an author/reviewer line, an About and trust links block, contact/demo link, and a concise editorial/methodology note. Do not invent personal credentials or legal claims. |
| Weak citation readiness | Report found no definition lists, tables, heading ids, direct-answer patterns, snippet-ready paragraphs, steps, or summary | Add a TL;DR summary, definition list, a comparison table, numbered workflow steps, direct-answer paragraphs, and ids on important headings. |
| No Content-Signal directive | Report flagged no Content-Signal directive | Add a conservative robots.txt declaration: search=yes, ai-input=yes, ai-train=no. This is an emerging convention, not a guaranteed crawler control. |
| No llms.txt | Report found no llms.txt or llms-full.txt | Add curated machine-readable summaries and links at /llms.txt and /llms-full.txt. Treat this as an optional emerging convention, not a search-engine guarantee. |
| IndexNow not detected | Report explicitly recommended IndexNow | Add an IndexNow key file, a deterministic submission script, and a GitHub Actions workflow triggered after pushes. Submit the current sitemap URLs to the IndexNow endpoint. Google does not support IndexNow, so retain the XML sitemap for Google. |

## Findings not automatically implemented

The report’s WebMCP, UCP, MCP server card, A2A agent card, NLWeb, schemamap, HTTP message-signature directory, RSS/feed, RSL licensing, and hreflang suggestions are not implemented because the current site has no agent transaction tools, multilingual variants, content feed, licensing policy, or authenticated service endpoint. Adding placeholder discovery files would create unsupported claims or broken interfaces.

## Validation targets

- All seven HTML pages retain one H1, a skip link, a main id, icon tags, canonical URL, Open Graph tags, Twitter Card tags, and JSON-LD.
- The audited page has a concise meta description, visible summary, breadcrumbs, a contents block, numbered steps, definition list, comparison table, FAQs, contact/trust links, and a reviewed date.
- robots.txt references the sitemap and Content-Signal line.
- llms.txt, llms-full.txt, the IndexNow key file, and the workflow exist.
- All sitemap URLs, static assets, and discovery files return HTTP 200 after deployment.
