from pathlib import Path

ROOT = Path('/home/ubuntu/web-dev')
path = ROOT / 'ask/index.html'
text = path.read_text(encoding='utf-8')

meta = '''  <meta name="author" content="Sibe Editorial Team"/>
  <meta name="date-published" content="2026-08-15"/>
  <meta name="date-modified" content="2026-08-15"/>
  <meta name="content-license" content="All rights reserved. Contact Sibe for reuse permissions."/>'''
if 'name="date-published"' not in text:
    text = text.replace('  <meta name="description" content="Ask questions about Sibe cloud CAD management, SolidWorks workflows, the free trial, pricing, security, and contact options."/>\n', '  <meta name="description" content="Ask questions about Sibe cloud CAD management, SolidWorks workflows, the free trial, pricing, security, and contact options."/>\n' + meta + '\n', 1)

schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://sibe-cad.vercel.app/ask/#webpage",
      "name": "Ask Sibe | Natural-Language CAD Information Endpoint",
      "url": "https://sibe-cad.vercel.app/ask/",
      "description": "A read-only natural-language information endpoint for public Sibe CAD resources.",
      "inLanguage": "en",
      "datePublished": "2026-08-15",
      "dateModified": "2026-08-15",
      "isPartOf": {"@id": "https://sibe-cad.vercel.app/#website"},
      "about": {"@id": "https://sibe-cad.vercel.app/#software"},
      "author": {"@id": "https://sibe-cad.vercel.app/#editorial-team"},
      "publisher": {"@id": "https://sibe-cad.vercel.app/#organization"},
      "breadcrumb": {"@id": "https://sibe-cad.vercel.app/ask/#breadcrumb"},
      "potentialAction": {"@type": "SearchAction", "target": "https://sibe-cad.vercel.app/ask/?q={question}", "query-input": "required name=question"}
    },
    {
      "@type": "WebApplication",
      "@id": "https://sibe-cad.vercel.app/ask/#application",
      "name": "Ask Sibe",
      "url": "https://sibe-cad.vercel.app/ask/",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web",
      "isAccessibleForFree": true,
      "featureList": ["Read-only natural-language answers", "Declarative WebMCP askSibe form", "Guarded imperative WebMCP registration"],
      "publisher": {"@id": "https://sibe-cad.vercel.app/#organization"}
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://sibe-cad.vercel.app/ask/#breadcrumb",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Sibe", "item": "https://sibe-cad.vercel.app/"},
        {"@type": "ListItem", "position": 2, "name": "Ask Sibe", "item": "https://sibe-cad.vercel.app/ask/"}
      ]
    },
    {
      "@type": "Organization",
      "@id": "https://sibe-cad.vercel.app/#organization",
      "name": "Sibe",
      "url": "https://www.sibe.io/",
      "logo": "https://sibe-cad.vercel.app/assets/sibe-logo.png",
      "sameAs": ["https://www.linkedin.com/company/sibe-io"],
      "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "url": "https://sibe-cad.vercel.app/contact/", "availableLanguage": "English"}
    },
    {
      "@type": "Person",
      "@id": "https://sibe-cad.vercel.app/#editorial-team",
      "name": "Sibe Editorial Team",
      "url": "https://www.sibe.io/about",
      "sameAs": ["https://www.linkedin.com/company/sibe-io"],
      "worksFor": {"@id": "https://sibe-cad.vercel.app/#organization"}
    }
  ]
}
</script>'''
if 'id="ask-inline-schema"' not in text:
    text = text.replace('<style>\n', schema + '\n<style id="ask-inline-schema">\n', 1)

css = '''<style id="ask-geo-fix">.ask-meta{margin:18px 0 0;color:var(--muted);font-size:13px}.ask-meta strong{color:var(--ink)}.answer-context{margin-top:30px;padding:30px;border:1px solid var(--line);border-radius:22px;background:rgba(255,255,255,.82)}.answer-context h2{margin-top:0}.answer-context p{color:var(--muted)}.answer-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:22px}.answer-grid article{padding:18px;border:1px solid var(--line);border-radius:14px;background:#fff}.answer-grid h3{margin:0 0 8px;font-size:18px}.answer-grid p{margin:0;font-size:14px}.answer-grid cite{display:block;margin-top:10px;color:var(--purple);font-size:12px;font-style:normal;font-weight:800}.answer-context ol{padding-left:22px;color:var(--muted)}.answer-context li{margin:8px 0}.answer-boundary{margin-top:22px;padding:16px;border-left:4px solid var(--pink);background:#fff6fa;border-radius:0 12px 12px 0;color:var(--muted)}@media(max-width:700px){.answer-grid{grid-template-columns:1fr}}</style>'''
if 'id="ask-geo-fix"' not in text:
    text = text.replace('</head>', css + '\n</head>', 1)

freshness = '    <p class="ask-meta"><strong>Published:</strong> <time datetime="2026-08-15">15 August 2026</time> · <strong>Reviewed and updated:</strong> <time datetime="2026-08-15">15 August 2026</time> · <strong>Editor:</strong> Sibe Editorial Team</p>\n'
if 'class="ask-meta"' not in text:
    text = text.replace('    <p>This endpoint answers common informational questions using the published Sibe CAD pages. It does not create accounts, submit purchases, change subscriptions, or expose private workspace data.</p>\n', '    <p>This endpoint answers common informational questions using the published Sibe CAD pages. It does not create accounts, submit purchases, change subscriptions, or expose private workspace data.</p>\n' + freshness, 1)

context = '''  <section class="answer-context" aria-labelledby="coverage-title">
    <h2 id="coverage-title">What this endpoint covers</h2>
    <p><strong>Short answer:</strong> Ask Sibe is a read-only information interface for public Sibe CAD resources. According to the official product pages, the covered topics include cloud CAD management for SolidWorks, version control, CAD file management, revision approvals, BOM/product data, browser-based collaboration, trial guidance, pricing links, security links, and contact options.</p>
    <div class="answer-grid">
      <article><h3>Product workflow</h3><p>Sibe is described as a cloud workspace connecting SolidWorks work with versions, references, revisions, product data, approvals, and browser reviews.</p><cite><a href="/cloud-cad-management/">Cloud CAD management</a></cite></article>
      <article><h3>Evaluation signals</h3><p>The public pages describe a 14-day free trial, no credit card required, and a representative-assembly evaluation approach. Confirm current terms on the official pricing page.</p><cite><a href="https://www.sibe.io/pricing">Official pricing</a></cite></article>
      <article><h3>Trust and sources</h3><p>Answers point back to official Sibe product, demo, security, pricing, company, contact, and editorial-methodology resources for confirmation.</p><cite><a href="/editorial-methodology/">Editorial methodology</a></cite></article>
    </div>
    <h3 id="answer-process">How to use an answer</h3>
    <ol><li>Ask one focused question about a published Sibe CAD topic.</li><li>Use the linked source to confirm current plan, format, permission, security, or commercial details.</li><li>For a product decision, request a demo or test a representative SolidWorks assembly rather than relying on a generic answer.</li></ol>
    <p class="answer-boundary"><strong>Capability boundary:</strong> This page does not access private workspaces, create accounts, submit purchases, process payments, change subscriptions, or claim live transactional MCP, UCP, or A2A backend access.</p>
  </section>
'''
if 'id="coverage-title"' not in text:
    text = text.replace('  <section class="card" aria-labelledby="question-title">', context + '  <section class="card" aria-labelledby="question-title">', 1)

old = "if(document.modelContext&&document.modelContext.registerTool){ document.modelContext.registerTool({name:'askSibe',description:'Answer an informational question using the published Sibe CAD website resources.',inputSchema:{type:'object',properties:{question:{type:'string',description:'A question about Sibe cloud CAD management, SolidWorks workflows, the free trial, pricing, security, or contact options.'}},required:['question']},execute:async function(args){showAnswer(args.question);return getAnswer(args.question);}}).catch(function(){}); }"
new = "if(document.modelContext){ var askTool={name:'askSibe',description:'Answer an informational question using the published Sibe CAD website resources.',inputSchema:{type:'object',properties:{question:{type:'string',description:'A question about Sibe cloud CAD management, SolidWorks workflows, the free trial, pricing, security, or contact options.'}},required:['question']},execute:async function(args){showAnswer(args.question);return getAnswer(args.question);}}; if(typeof document.modelContext.registerTool==='function'){ document.modelContext.registerTool(askTool).catch(function(){}); } if(typeof document.modelContext.provideContext==='function'){ try{ document.modelContext.provideContext(askTool); }catch(e){} } }"
if 'provideContext' not in text:
    text = text.replace(old, new, 1)

path.write_text(text, encoding='utf-8')
print('ask-page-latest-glippy-remediated')
