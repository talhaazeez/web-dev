from pathlib import Path
import json
import re

REPORT = Path('/home/ubuntu/upload/glippy-bulk-tabs-full-2026-08-14T22-19-20.md')
OUT = Path('/home/ubuntu/web-dev/glippy-bulk-analysis.json')
lines = REPORT.read_text(encoding='utf-8').splitlines()

summary = {}
for line in lines[:45]:
    if line.startswith('**') and ':**' in line:
        key, value = line.split(':**', 1)
        summary[key.strip('*').lower().replace(' ', '_')] = value.strip()

pages = []
current = None
category = None
for line in lines:
    m = re.match(r'^###\s+\d+\.\s+(https?://\S+)', line)
    if m:
        if current:
            pages.append(current)
        current = {'url': m.group(1), 'overall_score': None, 'grade': None, 'categories': []}
        category = None
        continue
    if current is None:
        continue
    m = re.match(r'^\*\*Overall Score:\*\*\s*(\d+)\s*\|\s*\*\*Grade:\*\*\s*(\w+)', line)
    if m:
        current['overall_score'] = int(m.group(1))
        current['grade'] = m.group(2)
        continue
    m = re.match(r'^####\s+(.+?)\s+\((\d+)/100\)', line)
    if m:
        category = {'name': m.group(1), 'score': int(m.group(2)), 'findings': []}
        current['categories'].append(category)
        continue
    if category is not None:
        if line.startswith('- ') and line[2:3] in {'✅', '⚠️', '❌', 'ℹ️'}:
            category['findings'].append(line[2:])
        elif line.startswith('  - '):
            category['findings'].append(line.strip())

if current:
    pages.append(current)

for page in pages:
    page['weak_categories'] = sorted([c for c in page['categories'] if c['score'] < 80], key=lambda x: x['score'])
    page['critical_findings'] = [f for c in page['categories'] for f in c['findings'] if f.startswith(('❌', '⚠️'))]

analysis = {'summary': summary, 'page_count': len(pages), 'pages': pages}
OUT.write_text(json.dumps(analysis, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({
    'summary': summary,
    'page_count': len(pages),
    'scores': {p['url']: p['overall_score'] for p in pages},
    'weak_category_counts': {p['url']: len(p['weak_categories']) for p in pages},
    'critical_findings': {p['url']: p['critical_findings'][:12] for p in pages},
}, indent=2, ensure_ascii=False))
