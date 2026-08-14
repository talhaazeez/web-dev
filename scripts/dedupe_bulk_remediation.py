from pathlib import Path
import re

path = Path('/home/ubuntu/web-dev/index.html')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'(<p class="outcome-line">.*?</p>)(?:\s*\1)+', re.S)
text, count = pattern.subn(r'\1', text)
path.write_text(text, encoding='utf-8')
print(f'deduplicated-outcome-lines={count}')
