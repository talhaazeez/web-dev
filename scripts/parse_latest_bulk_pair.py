from pathlib import Path
import csv
import json
import re

MD = Path('/home/ubuntu/upload/glippy-bulk-tabs-full-2026-08-14T22-43-10.md')
CSV = Path('/home/ubuntu/upload/glippy-bulk-tabs-report-2026-08-14T22-43-42.csv')
OUT = Path('/home/ubuntu/web-dev/glippy-latest-pair-analysis.json')

rows = CSV.read_text(encoding='utf-8-sig').splitlines()
header_i = next(i for i, line in enumerate(rows) if line.startswith('URL,Overall Score,'))
detail_start = next((i for i, line in enumerate(rows) if line.startswith('# Per-URL Check Details')), len(rows))
reader = csv.DictReader(rows[header_i:detail_start])
score_rows = [row for row in reader if row.get('URL') and row.get('Overall Score')]

details = []
if detail_start is not None:
    detail_reader = csv.DictReader(rows[detail_start + 2:])
    for row in detail_reader:
        if not row.get('URL') or not row.get('Category'):
            continue
        details.append(row)

by_url = {}
for row in score_rows:
    url = row['URL']
    by_url[url] = {
        'url': url,
        'overall_score': int(row['Overall Score']),
        'grade': row['Grade'],
        'categories': {k: int(v) for k, v in row.items() if k not in {'URL', 'Overall Score', 'Grade'} and v},
        'warnings': [],
        'failures': [],
        'infos': [],
    }
for row in details:
    item = {'category': row['Category'], 'check': row['Check'], 'recommendation': row['Recommendation']}
    status = row['Status']
    if row['URL'] not in by_url:
        continue
    by_url[row['URL']][{'warn':'warnings','fail':'failures','info':'infos'}.get(status, 'infos')].append(item)

analysis = {
    'report_markdown': str(MD),
    'report_csv': str(CSV),
    'page_count': len(by_url),
    'pages': list(by_url.values()),
    'low_categories': sorted({
        category
        for page in by_url.values()
        for category, score in page['categories'].items()
        if score < 70
    }),
}
OUT.write_text(json.dumps(analysis, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({
    'page_count': analysis['page_count'],
    'scores': {p['url']: p['overall_score'] for p in analysis['pages']},
    'low_categories': analysis['low_categories'],
    'warning_counts': {p['url']: len(p['warnings']) for p in analysis['pages']},
    'failure_counts': {p['url']: len(p['failures']) for p in analysis['pages']},
}, indent=2, ensure_ascii=False))
