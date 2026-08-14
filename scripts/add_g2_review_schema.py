from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
G2_URL = 'https://www.g2.com/products/sibe/reviews'
G2_REVIEW_ID = 'https://sibe-cad.vercel.app/#g2-review-jessica-c'

review = {
    '@type': 'Review',
    '@id': G2_REVIEW_ID,
    'name': 'Sibe Simplifies File Management with Clear Cloud Version Control',
    'url': G2_URL,
    'datePublished': '2026-08-14',
    'reviewBody': 'A G2 reviewer described clearer cloud version control, browser access for external partners and non-technical team members, and fewer file-sharing errors, while noting that notification controls could be refined.',
    'reviewRating': {
        '@type': 'Rating',
        'ratingValue': 5,
        'bestRating': 5,
    },
    'author': {
        '@type': 'Person',
        'name': 'Jessica C.',
    },
    'publisher': {
        '@type': 'Organization',
        'name': 'G2',
        'url': 'https://www.g2.com/',
    },
    'itemReviewed': {
        '@id': 'https://sibe-cad.vercel.app/#software',
    },
}

aggregate = {
    '@type': 'AggregateRating',
    'ratingValue': 4.9,
    'bestRating': 5,
    'ratingCount': 35,
    'reviewCount': 35,
    'url': G2_URL,
}

review_section = '''<section class="review-context" id="g2-review-context"><div class="container"><div class="head"><span class="kicker">Independent review context</span><h2 id="what-one-g2-reviewer-highlighted">What one G2 reviewer highlighted.</h2><p>A public G2 review describes clearer cloud version control, easier browser access for external partners and non-technical team members, and less back-and-forth when sharing files. The same review notes that notification controls could be refined. This is one external review, not a universal claim or customer-rating guarantee.</p><p><a href="https://www.g2.com/products/sibe/reviews" rel="noopener noreferrer">Read the review and current G2 rating</a></p></div></div></section>'''
review_style = '''<style id="g2-review-context-css">.review-context{padding:56px 0;background:#fff;border-top:1px solid #e9e1ee;border-bottom:1px solid #e9e1ee}.review-context .head{max-width:820px;margin:0 auto}.review-context .head p{color:#6d6575}.review-context a{color:#7114b8;font-weight:850;text-decoration:underline}.review-context a:focus-visible{outline:3px solid rgba(223,63,131,.55);outline-offset:3px}</style>'''

html_path = ROOT / 'index.html'
html = html_path.read_text(encoding='utf-8')
if 'id="g2-review-context"' not in html:
    html = html.replace('<section class="bulk-summary" id="homepage-key-takeaways">', review_section + '<section class="bulk-summary" id="homepage-key-takeaways">', 1)
if 'id="g2-review-context-css"' not in html:
    html = html.replace('</head>', review_style + '</head>', 1)

soup = BeautifulSoup(html, 'html.parser')
for script in soup.find_all('script', type='application/ld+json'):
    try:
        data = json.loads(script.string or script.get_text())
    except json.JSONDecodeError:
        continue
    graph = data.get('@graph')
    if not graph:
        continue
    software = next((node for node in graph if node.get('@id') == 'https://sibe-cad.vercel.app/#software'), None)
    if software is None:
        continue
    same_as = software.setdefault('sameAs', [])
    if G2_URL not in same_as:
        same_as.append(G2_URL)
    software['aggregateRating'] = aggregate
    software['review'] = {'@id': G2_REVIEW_ID}
    if not any(node.get('@id') == G2_REVIEW_ID for node in graph):
        graph.append(review)
    script.string = json.dumps(data, indent=2, ensure_ascii=False)
    break
html_path.write_text(str(soup), encoding='utf-8')

json_path = ROOT / 'index.jsonld'
data = json.loads(json_path.read_text(encoding='utf-8'))
graph = data['@graph']
software = next(node for node in graph if node.get('@id') == 'https://sibe-cad.vercel.app/#software')
same_as = software.setdefault('sameAs', [])
if G2_URL not in same_as:
    same_as.append(G2_URL)
software['aggregateRating'] = aggregate
software['review'] = {'@id': G2_REVIEW_ID}
if not any(node.get('@id') == G2_REVIEW_ID for node in graph):
    graph.append(review)
json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('g2-review-schema-update=passed')
