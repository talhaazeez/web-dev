from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path('/home/ubuntu/web-dev')
files = sorted(ROOT.rglob('index.html'))
assert len(files) == 10
for path in files:
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    forms = soup.find_all('form')
    assert len(forms) >= 1, path
    ask_forms = [form for form in forms if form.get('toolname') == 'askSibe']
    assert len(ask_forms) == 1, path
    form = ask_forms[0]
    assert form.get('tooldescription')
    assert form.get('action') == '/ask/'
    assert form.get('method', '').lower() == 'get'
    inputs = form.find_all('input')
    assert len(inputs) == 1
    control = inputs[0]
    assert control.get('name') == 'q'
    assert control.get('toolparamdescription')
    input_id = control.get('id')
    assert input_id and len(soup.find_all(id=input_id)) == 1
    label = form.find('label', attrs={'for': input_id})
    assert label and label.get_text(' ', strip=True)
    button = form.find('button', attrs={'type': 'submit'})
    assert button and button.get_text(' ', strip=True)
    print(f'webmcp-form-ok={path.relative_to(ROOT)}')
print('webmcp-declarative-regression=passed pages=10')
