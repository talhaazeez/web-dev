from pathlib import Path
import json
import re

REPORT = Path('/home/ubuntu/upload/glippy-bulk-tabs-summary-2026-08-14T22-36-42.md')
OUT = Path('/home/ubuntu/web-dev/glippy-latest-bulk-analysis.json')
lines = REPORT.read_text(encoding='utf-8').splitlines()
pages=[]
current=None
category=None
for line in lines:
    m=re.match(r'^###\s+\d+\.\s+(https?://\S+)',line)
    if m:
        if current: pages.append(current)
        current={'url':m.group(1),'overall_score':None,'grade':None,'categories':[]}
        category=None
        continue
    if current is None: continue
    m=re.match(r'^\*\*Overall Score:\*\*\s*(\d+)\s*\|\s*\*\*Grade:\*\*\s*(\w+)',line)
    if m:
        current['overall_score']=int(m.group(1)); current['grade']=m.group(2); continue
    m=re.match(r'^####\s+(.+?)\s+\((\d+)/100\)',line)
    if m:
        category={'name':m.group(1),'score':int(m.group(2)),'findings':[]}
        current['categories'].append(category)
        continue
    if category is not None and (line.startswith('- ') or line.startswith('  - ')):
        content=line.strip()[2:] if line.strip().startswith('- ') else line.strip()
        if content[:1] in {'✅','⚠️','❌','ℹ️'} or line.startswith('  - '): category['findings'].append(content)
if current: pages.append(current)
for p in pages:
    p['weak_categories']=sorted([c for c in p['categories'] if c['score']<80], key=lambda c:c['score'])
    p['critical_findings']=[f for c in p['categories'] for f in c['findings'] if f.startswith(('❌','⚠️'))]
analysis={'page_count':len(pages),'pages':pages}
OUT.write_text(json.dumps(analysis,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'page_count':len(pages),'scores':{p['url']:p['overall_score'] for p in pages},'critical_findings':{p['url']:p['critical_findings'][:15] for p in pages}},indent=2,ensure_ascii=False))
