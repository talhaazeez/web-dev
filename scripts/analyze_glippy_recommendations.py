from collections import Counter, defaultdict
from pathlib import Path
import csv
import json

CSV_PATH = Path('/home/ubuntu/upload/glippy-recommendations-sibe-cad.vercel.app-2026-08-14T22-08-11.csv')
OUT_PATH = Path('/home/ubuntu/web-dev/glippy-recommendations-analysis.json')

lines = CSV_PATH.read_text(encoding='utf-8-sig').splitlines()
metadata = {}
data_start = 0
for i, line in enumerate(lines):
    if line.startswith('#'):
        body = line.lstrip('# ').strip()
        if ': ' in body:
            key, value = body.split(': ', 1)
            metadata[key.strip().lower().replace(' ', '_')] = value.strip()
    elif line.strip():
        data_start = i
        break

reader = csv.DictReader(lines[data_start:])
rows = []
for row in reader:
    rows.append({k.strip(): (v or '').strip() for k, v in row.items()})

by_priority = Counter(row['Priority'] for row in rows)
by_category = defaultdict(list)
for row in rows:
    by_category[row['Category']].append(row)

analysis = {
    'source': str(CSV_PATH),
    'metadata': metadata,
    'row_count': len(rows),
    'priority_counts': dict(by_priority),
    'category_counts': {category: len(items) for category, items in by_category.items()},
    'findings': rows,
    'applicability': {
        'sitewide_html': [
            'Add IDs to all meaningful H2/H3 headings for deep linking.',
            'Add lazy loading to every below-the-fold image.',
            'Strengthen contact/entity signals where accurate information is available.',
            'Add clearer problem-solution and outcome framing.',
            'Add current temporal context and remove ambiguous outdated references.',
            'Improve positioning density with defensible product-specific statements.',
            'Add standalone topic sentences and useful supporting details to major sections.',
            'Improve citation markup and footnote structure using verified official sources.',
            'Add a comparison table where the page already makes workflow comparisons.'
        ],
        'inapplicable_or_not_supported': [
            'Article/BlogPosting schema is not appropriate for this product landing page.',
            'WebMCP article tools are not applicable to a static product landing page without an agent backend.',
            'High-authority .gov/.edu links are not required when relevant authoritative first-party product sources are available.'
        ]
    }
}
OUT_PATH.write_text(json.dumps(analysis, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({
    'metadata': metadata,
    'row_count': len(rows),
    'priority_counts': dict(by_priority),
    'category_counts': dict(analysis['category_counts'])
}, indent=2, ensure_ascii=False))
