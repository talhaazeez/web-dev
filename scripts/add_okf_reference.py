from pathlib import Path
from bs4 import BeautifulSoup
import json

ROOT = Path('/home/ubuntu/web-dev')
OKF_URL = 'https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing'
OKF_TITLE = 'Google Cloud: Introducing the Open Knowledge Format'

# Add a clearly scoped external reference to the editorial methodology source section.
html_path = ROOT / 'editorial-methodology/index.html'
html = html_path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
if OKF_URL not in html:
    sources = soup.find(id='site-sources')
    if sources:
        paragraph = soup.new_tag('p')
        paragraph['class'] = ['external-reference']
        paragraph.append('External format reference: Google Cloud describes the Open Knowledge Format as a vendor-neutral, markdown-based way to represent portable knowledge for people and AI systems. Sibe publishes Markdown, JSON-LD, and discovery resources as practical machine-readable surfaces; this site does not claim formal OKF v0.1 conformance. ')
        cite = soup.new_tag('cite')
        link = soup.new_tag('a', href=OKF_URL, target='_blank', rel='noopener noreferrer')
        link.string = OKF_TITLE
        cite.append(link)
        paragraph.append(cite)
        sources.find('div', class_='container').append(paragraph)

    for script in soup.find_all('script', type='application/ld+json'):
        try:
            graph_data = json.loads(script.string or script.get_text())
            graph = graph_data.get('@graph', []) if isinstance(graph_data, dict) else []
            webpage = next((item for item in graph if item.get('@type') == 'WebPage'), None)
            if webpage is not None and not any(isinstance(x, dict) and x.get('url') == OKF_URL for x in webpage.get('citation', [])):
                citations = webpage.get('citation', [])
                if isinstance(citations, str): citations = [citations]
                citations.append({'@type': 'CreativeWork', 'name': OKF_TITLE, 'url': OKF_URL, 'isPartOf': {'@type': 'CreativeWorkSeries', 'name': 'Open Knowledge Format'}})
                webpage['citation'] = citations
                script.string = json.dumps(graph_data, indent=2, ensure_ascii=False)
        except Exception:
            continue
    html_path.write_text(str(soup), encoding='utf-8')

# Add citation to the editorial WebPage JSON-LD resource.
jsonld_path = ROOT / 'editorial-methodology/index.jsonld'
try:
    data = json.loads(jsonld_path.read_text(encoding='utf-8'))
    graph = data.get('@graph', []) if isinstance(data, dict) else []
    webpage = next((item for item in graph if item.get('@type') == 'WebPage'), None)
    if webpage is not None:
        existing = webpage.get('citation', [])
        if isinstance(existing, str): existing = [existing]
        if not any(isinstance(x, dict) and x.get('url') == OKF_URL for x in existing):
            existing.append({'@type': 'CreativeWork', 'name': OKF_TITLE, 'url': OKF_URL, 'isPartOf': {'@type': 'CreativeWorkSeries', 'name': 'Open Knowledge Format'}})
            webpage['citation'] = existing
            jsonld_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
except Exception:
    pass

# Add the reference to the Markdown representation of the methodology page.
md_path = ROOT / 'editorial-methodology/index.md'
md = md_path.read_text(encoding='utf-8')
if OKF_URL not in md:
    md += f'\n## External format reference\n\nGoogle Cloud describes the [Open Knowledge Format]({OKF_URL}) as a vendor-neutral, markdown-based format for portable knowledge that can be read by people and AI systems. Sibe publishes Markdown, JSON-LD, and discovery resources as practical machine-readable surfaces; this site does not claim formal OKF v0.1 conformance.\n'
    md_path.write_text(md, encoding='utf-8')

# Add machine-readable references for LLM and crawler consumers.
llms_path = ROOT / 'llms.txt'
llms = llms_path.read_text(encoding='utf-8')
section = f'\n## External machine-readable format reference\nGoogle Cloud: Introducing the Open Knowledge Format\n{OKF_URL}\nUse this external reference for background on portable, markdown-based knowledge representations. Sibe publishes practical Markdown, JSON-LD, and discovery resources but does not claim formal OKF v0.1 conformance.\n'
if OKF_URL not in llms:
    llms += section
    llms_path.write_text(llms, encoding='utf-8')

full_path = ROOT / 'llms-full.txt'
full = full_path.read_text(encoding='utf-8')
if OKF_URL not in full:
    marker = '\n## Agent discovery manifests\n'
    if marker in full:
        full = full.replace(marker, section + marker, 1)
    else:
        full += section
    full_path.write_text(full, encoding='utf-8')

print('okf-reference-added')
