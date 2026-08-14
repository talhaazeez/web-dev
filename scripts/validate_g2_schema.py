from pathlib import Path
import json
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
G2_URL = 'https://www.g2.com/products/sibe/reviews'
REVIEW_ID = 'https://sibe-cad.vercel.app/#g2-review-jessica-c'
html_path = ROOT / 'index.html'
soup = BeautifulSoup(html_path.read_text(encoding='utf-8'), 'html.parser')
assert soup.find(id='g2-review-context')
assert soup.find('a', href=G2_URL)
# Open Graph uses property= for social metadata, but no actual RDFa vocabulary/type/resource attributes are present.
for attr in ('vocab', 'typeof', 'resource', 'prefix', 'about'):
    assert not soup.find(attrs={attr: True}), attr

def graph_from(text):
    data = json.loads(text)
    return data['@graph']

inline_graph = None
for script in soup.find_all('script', type='application/ld+json'):
    try:
        graph = graph_from(script.string or script.get_text())
    except (json.JSONDecodeError, KeyError):
        continue
    if any(node.get('@id') == 'https://sibe-cad.vercel.app/#software' for node in graph):
        inline_graph = graph
        break
assert inline_graph is not None
standalone_graph = graph_from((ROOT / 'index.jsonld').read_text(encoding='utf-8'))
for graph in (inline_graph, standalone_graph):
    software = next(node for node in graph if node.get('@id') == 'https://sibe-cad.vercel.app/#software')
    assert G2_URL in software['sameAs']
    rating = software['aggregateRating']
    assert rating['@type'] == 'AggregateRating'
    assert rating['ratingValue'] == 4.9
    assert rating['bestRating'] == 5
    assert rating['ratingCount'] == 35
    assert rating['reviewCount'] == 35
    assert rating['url'] == G2_URL
    assert software['review']['@id'] == REVIEW_ID
    review = next(node for node in graph if node.get('@id') == REVIEW_ID)
    assert review['url'] == G2_URL
    assert review['reviewRating']['ratingValue'] == 5
    assert review['author']['name'] == 'Jessica C.'
    assert review['publisher']['name'] == 'G2'
    for faq in (node for node in graph if node.get('@type') == 'FAQPage'):
        for question in faq.get('mainEntity', []):
            assert 'suggestedAnswer' not in question
            assert 'upvoteCount' not in question
print('g2-schema-regression=passed')
