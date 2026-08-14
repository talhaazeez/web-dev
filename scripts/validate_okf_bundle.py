from pathlib import Path
import re

ROOT = Path('/home/ubuntu/web-dev')
BUNDLE = ROOT / 'okf'
assert BUNDLE.is_dir()
required = [BUNDLE / 'index.md', BUNDLE / 'concepts/index.md', BUNDLE / 'references/index.md', BUNDLE / 'page-map.md', BUNDLE / 'log.md']
for path in required:
    assert path.exists(), path

files = sorted(BUNDLE.rglob('*.md'))
assert len(files) == 16, len(files)
for path in files:
    text = path.read_text(encoding='utf-8')
    legacy_short = 'llms' + '.txt'
    legacy_full = 'llms' + '-full.txt'
    assert legacy_short not in text and legacy_full not in text, path
    if path.name in {'index.md', 'log.md'} and path.parent == BUNDLE:
        continue
    if path.parent.name in {'concepts', 'references'} and path.name == 'index.md':
        continue
    assert text.startswith('---\n'), path
    end = text.find('\n---\n', 4)
    assert end > 0, path
    front = text[4:end]
    for key in ['type:', 'title:', 'description:', 'resource:', 'tags:', 'generated:', 'verified:', 'status:', 'stale_after:', 'sources:']:
        assert re.search(rf'(?m)^{re.escape(key)}', front), (path, key)

# Verify local Markdown links resolve inside the bundle.
for path in files:
    text = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(('http://', 'https://', '#')):
            continue
        target_path = (path.parent / target.split('#', 1)[0]).resolve()
        assert target_path.exists(), (path, target, target_path)

root_text = (BUNDLE / 'index.md').read_text(encoding='utf-8')
assert 'concepts/index.md' in root_text and 'page-map.md' in root_text and 'references/index.md' in root_text
print(f'okf-bundle-validation=passed markdown_files={len(files)}')
