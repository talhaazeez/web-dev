# Full Glippy remediation matrix

The attached CSV contains 66 findings for the cloud CAD management page. The CSV appears to reflect an earlier page snapshot, so findings are mapped against the current repository before deployment.

## Implement across all webpages

| CSV finding | Current action |
|---|---|
| Schema completeness | Retain and extend JSON-LD with WebPage, Organization, Person, SoftwareApplication, Offer, BreadcrumbList, FAQPage, sameAs, dates, author, publisher, featureList, and speakable properties. |
| SameAs missing | Use the official Sibe LinkedIn organization profile and About page in the Organization and Person entities. |
| Publication dates missing | Keep visible Published/Reviewed dates and machine-readable datePublished/dateModified on every page. |
| Heading IDs, direct answers, snippet paragraphs, sequential content, and missing summary | Add IDs to all substantive headings, direct-answer paragraphs, TL;DR/quick-answer sections, tables, and ordered workflow lists. |
| Thin content and low self-contained sections | Expand the audited page with definitions, comparison content, workflow steps, editorial context, FAQs, proof-backed trust statements, and clear problem-to-solution framing. |
| Low proof points/social proof/authority | Add only verified official proof signals: 14-day free trial, setup-under-20-minutes claim, official customer/testimonial links, Sibe About page, Data Security page, named SolidWorks expert, and official LinkedIn entity. |
| Weak factual verifiability | Add a visible Sources and methodology section with links to official Sibe product, About, security, demo, pricing, and feature pages. |
| No copyright year | Add a current copyright year to every footer. |
| Images without lazy loading | Add loading="lazy" to below-fold non-logo images when present; keep above-fold branding eager. |
| Machine-readable discovery | Retain sitemap, robots, the OKF bundle, manifest, Vercel Link headers, and IndexNow key/submission script. |
| No privacy/terms/contact/editorial signals | Link the verified app privacy and terms routes, local Contact page, and local Editorial Methodology page on every page. |

## Not applicable or not safe to fabricate

| CSV finding | Decision |
|---|---|
| Article/BlogPosting schema | The audited URL is a product landing page, not an article. Adding Article schema would misrepresent the page type. Product pages use WebPage and SoftwareApplication schema instead. |
| No hreflang | No alternate language pages exist, so hreflang would be incorrect. |
| AI-specific meta tags, RSL/license.xml | These are emerging conventions; no licensing policy or AI usage policy was supplied. Do not publish unsupported legal or licensing claims. |
| RSS/Atom feed | The current site has no recurring article feed. A feed containing only static product pages would be misleading. |
| WebMCP/UCP/MCP/A2A/NLWeb/schemamap/Web Bot Auth | The site exposes no transactional agent tools, MCP server, commerce protocol, dynamic query endpoint, or signed-agent API. Placeholder discovery files would be unsupported. |
| Video/audio/charts | The audited page is a static product explainer. These are optional multimodal enhancements, not defects. |
| High-authority .gov/.edu links | Product claims are best supported by official Sibe sources. Adding unrelated authority links would reduce relevance and could imply unsupported endorsements. |
| Data statistics and measurable outcomes | Only official product claims and named testimonials may be used; no independent performance dataset was supplied. Avoid fabricated statistics. |

## Validation targets

All nine production pages should return HTTP 200 and contain current dates, author/entity references, internal links, Contact/Privacy/Terms links, skip links, canonical metadata, and JSON-LD. The audited cloud CAD page should additionally include a summary, answer-ready sections, definitions, comparison table, ordered steps, editorial context, official proof links, and source attribution.
