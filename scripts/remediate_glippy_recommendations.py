from pathlib import Path
import re
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')

def slugify(text: str) -> str:
    text = re.sub(r'<[^>]+>', ' ', text)
    text = BeautifulSoup(text, 'html.parser').get_text(' ', strip=True).lower()
    text = text.replace('&', ' and ')
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text or 'section'

for path in sorted(ROOT.rglob('index.html')):
    text = path.read_text(encoding='utf-8')
    used = set(re.findall(r'\bid="([^"]+)"', text))
    heading_pattern = re.compile(r'<(h[1-3])(\s[^>]*)?>(.*?)</\1>', re.I | re.S)

    def heading_replacement(match):
        tag, attrs, inner = match.group(1), match.group(2) or '', match.group(3)
        if re.search(r'\bid\s*=', attrs, re.I):
            return match.group(0)
        base = slugify(inner)
        candidate = base
        n = 2
        while candidate in used:
            candidate = f'{base}-{n}'
            n += 1
        used.add(candidate)
        return f'<{tag}{attrs} id="{candidate}">{inner}</{tag}>'

    text = heading_pattern.sub(heading_replacement, text)

    # Keep the header logo eager for branding/LCP and lazy-load the footer logo.
    img_pattern = re.compile(r'<img\b[^>]*>', re.I)
    image_matches = list(img_pattern.finditer(text))
    if len(image_matches) > 1:
        footer_img = image_matches[-1]
        tag = footer_img.group(0)
        if not re.search(r'\bloading\s*=', tag, re.I):
            replacement = tag[:-2] + ' loading="lazy"/>' if tag.endswith('/>') else tag[:-1] + ' loading="lazy">'
            text = text[:footer_img.start()] + replacement + text[footer_img.end():]

    # Add semantic citation nodes to the existing source section without changing URLs.
    source_start = text.find('<section class="site-sources"')
    source_class = 'site-sources'
    if source_start < 0:
        source_start = text.find('<section class="sources"')
        source_class = 'sources'
    if source_start >= 0:
        source_end = text.find('</section>', source_start)
        if source_end >= 0:
            segment_end = source_end + len('</section>')
            segment = text[source_start:segment_end]
            if '<cite>' not in segment:
                segment = re.sub(r'(<a\b[^>]*>.*?</a>)', r'<cite>\1</cite>', segment, flags=re.I | re.S)
            if 'Reviewed 15 August 2026' not in segment:
                marker = '</p>'
                first_p = segment.find(marker)
                if first_p >= 0:
                    insert_at = first_p + len(marker)
                    freshness = '<p class="source-freshness">Reviewed 15 August 2026. Verify plan-specific details and current availability on the official Sibe pages linked below.</p>'
                    segment = segment[:insert_at] + freshness + segment[insert_at:]
            text = text[:source_start] + segment + text[segment_end:]

    if path == ROOT / 'index.html':
        # Add a transparent, current proof-point and evaluation note after the proof strip.
        proof_marker = '</div>\n</div>\n<section>\n<div class="container">\n<div class="section-head">\n<span class="kicker">The problem</span>'
        proof_note = '</div>\n</div>\n<aside class="proof-note" aria-label="Sibe evaluation proof points"><div class="container"><strong>Evaluation proof points:</strong> Sibe publicly describes a 14-day free trial, no-credit-card signup, and quick cloud setup. Use one representative assembly to verify version history, BOM structure, and browser review in your own workflow. <cite><a href="https://www.sibe.io/pricing">Verify current pricing and trial details</a></cite>.</div></aside>\n<section>\n<div class="container">\n<div class="section-head">\n<span class="kicker">The problem</span>'
        if 'class="proof-note"' not in text and proof_marker in text:
            text = text.replace(proof_marker, proof_note, 1)

        # Add explicit outcome language to the major homepage sections.
        outcome_replacements = [
            ('</p>\n</div>\n<div class="problem-grid">', '</p>\n<p class="outcome-line"><strong>Outcome:</strong> A controlled source of truth makes the current, approved design easier to identify before it reaches manufacturing or an external reviewer.</p>\n</div>\n<div class="problem-grid">'),
            ('</p>\n</div>\n<div class="step-grid">', '</p>\n<p class="outcome-line"><strong>Outcome:</strong> A short evaluation on real engineering data shows whether the workflow reduces file chasing without forcing a full enterprise PDM rollout.</p>\n</div>\n<div class="step-grid">'),
            ('</p>\n</div>\n<div class="feature-grid">', '</p>\n<p class="outcome-line"><strong>Outcome:</strong> Version control, structured product data, and browser reviews stay connected to the same SolidWorks workflow.</p>\n</div>\n<div class="feature-grid">'),
        ]
        for old, new in outcome_replacements:
            text = text.replace(old, new, 1)

        # Insert a semantic comparison table before the existing shared-drive CTA note.
        comparison_marker = '<div class="note"><strong>Ready to go deeper?</strong>'
        comparison_html = '<div class="comparison-block"><span class="kicker">Workflow comparison</span><h3 id="shared-drive-vs-cloud-pdm">Shared-drive workflow vs cloud PDM</h3><table class="comparison"><caption>How the workflow changes when a SolidWorks team moves from shared folders to a controlled cloud workspace.</caption><thead><tr><th scope="col">Workflow need</th><th scope="col">Shared folders</th><th scope="col">Cloud PDM workflow</th></tr></thead><tbody><tr><th scope="row">Current design</th><td>Teams search folder names, email, and filenames.</td><td>Version history and check-in/check-out show the working state.</td></tr><tr><th scope="row">Review status</th><td>Approval decisions can remain in messages or spreadsheets.</td><td>Revision status and release history stay with the design.</td></tr><tr><th scope="row">Downstream access</th><td>Engineers export screenshots or duplicate BOM data.</td><td>Authorized stakeholders use browser review and structured product data.</td></tr></tbody></table></div>'
        if 'id="shared-drive-vs-cloud-pdm"' not in text and comparison_marker in text:
            text = text.replace(comparison_marker, comparison_html + comparison_marker, 1)

        # Add a small present-tense context signal for the freshness recommendation.
        freshness_marker = '<p class="meta-line"><strong>Published:</strong>'
        if 'Current site review:' not in text:
            text = text.replace(freshness_marker, '<p class="current-context"><strong>Current site review:</strong> Product and trial details were checked against official Sibe sources on 15 August 2026.</p>\n' + freshness_marker, 1)

        # Add schema completeness signals to the inline homepage graph.
        website_node = '''    {
      "@type": "WebSite",
      "@id": "https://sibe-cad.vercel.app/#website",
      "name": "Sibe CAD Management",
      "url": "https://sibe-cad.vercel.app/",
      "inLanguage": "en",
      "publisher": {
        "@id": "https://sibe-cad.vercel.app/#organization"
      }
    },
'''
        if '"@type": "WebSite"' not in text:
            text = text.replace('  "@graph": [\n', '  "@graph": [\n' + website_node, 1)

        # Extend the existing Organization node with contact-page and legal entity context.
        org_marker = '      "image": "https://sibe-cad.vercel.app/assets/sibe-logo.png"\n    },\n    {\n      "@type": "SoftwareApplication"'
        org_replacement = '      "image": "https://sibe-cad.vercel.app/assets/sibe-logo.png",\n      "contactPoint": {\n        "@type": "ContactPoint",\n        "contactType": "customer support",\n        "url": "https://sibe-cad.vercel.app/contact/",\n        "availableLanguage": "English"\n      }\n    },\n    {\n      "@type": "SoftwareApplication"'
        if org_marker in text and '"contactPoint"' not in text:
            text = text.replace(org_marker, org_replacement, 1)

    path.write_text(text, encoding='utf-8')
    print(f'updated={path.relative_to(ROOT)}')
