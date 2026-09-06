"""Read existing local design/reference bytes; never launch a browser or fetch resources."""
from pathlib import Path
import base64
import hashlib
import json
import re
import struct
import subprocess
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser

repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
work = repo / 'projects/chirality-app-dev'
basis = work / 'plans/shell-redesign_2026-09-04'
out = Path(__file__).resolve().parent
historical = work / 'execution/_Coordination/AgentRuns/APP_SHELL_CONVERGENCE_2026-09-06/pkg02-workflows-readonly/browser-01'
sha = lambda b: hashlib.sha256(b).hexdigest()

def identity(p):
    b = p.read_bytes()
    return {'path': p.relative_to(repo).as_posix(), 'sha256': sha(b), 'bytes': len(b)}

readme = (basis / 'README.md').read_text()
html_path = basis / 'mock/chirality-shell-mocks.html'
html = html_path.read_text()
assets = []
for expected, relative in re.findall(r'^([0-9a-f]{64})  ((?:assets|mock)/\S+)$', readme, re.M):
    p = basis / relative
    item = identity(p)
    item.update({'readme_sha256': expected, 'matches_readme': item['sha256'] == expected})
    if p.suffix == '.png':
        item['png_dimensions'] = list(struct.unpack('>II', p.read_bytes()[16:24]))
    assets.append(item)

class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = {}
        self.references = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line, column = self.getpos()
        if tag == 'script':
            self.scripts.append({'line': line, 'src': a.get('src'), 'inline': 'src' not in a})
        for key in ['src', 'href']:
            if key not in a:
                continue
            value = a[key]
            if value.startswith('data:image/'):
                header, payload = value.split(',', 1)
                b = base64.b64decode(payload)
                digest = sha(b)
                record = self.images.setdefault(digest, {'sha256': digest, 'mime': header.split(';')[0][5:], 'bytes': len(b), 'dimensions': list(struct.unpack('>II', b[16:24])), 'occurrences': []})
                record['occurrences'].append({'line': line, 'column': column, 'tag': tag, 'width_attribute': a.get('width'), 'height_attribute': a.get('height'), 'style': a.get('style'), 'class': a.get('class')})
            else:
                kind = 'external' if re.match(r'https?://', value) else 'fragment' if value.startswith('#') else 'relative'
                item = {'line': line, 'tag': tag, 'attribute': key, 'value': value, 'kind': kind}
                if kind == 'relative':
                    item['exists_relative_to_mock'] = (html_path.parent / value).exists()
                self.references.append(item)

inventory = Inventory()
inventory.feed(html)
roles = {
    '63c138f15647bce8ca236207a377adeb6d2ce5f15356b3895bce1d2949ef761b': 'Logo panel size samples at displayed 256/128 and large desktop icon samples',
    '8f95af2791d49d3434873e70d58c9cbc65d0283050f3821ba53cc3dc01adec6b': 'Logo panel mark samples displayed at64',
    'e5a3526260fa67475d198afdbcbe75455615a27f5c6823ec18ef7ea20da46a41': 'Logo panel samples displayed at44/32/22/16 and historical header-at22 reference',
    '28e8c67571cb183e74f1b115dc9f5d56695eaabfc69dd4beaa2000dc54309b11': 'Logo panel corporate lockup on light ground, displayed height96',
    '1f789877c188ebd39d3ef9d9ed294ffd323e5c691a4362aafdec1cb02e746562': 'Logo panel corporate lockup on dark ground, displayed height96',
    '19112f1fa9415e452132374377570f7d3c48abe044ffa7f5ca2db9a116308da4': 'Logo panel Dock icon samples on light/dark desktops',
}
for digest, item in inventory.images.items():
    item['role'] = roles.get(digest, 'UNMAPPED')
    item['byte_identical_packaged_assets'] = [a['path'] for a in assets if '/assets/' in a['path'] and a['sha256'] == digest]

step_text = html.split('var STEPS = [', 1)[1].split('\n  ];', 1)[0]
titles = re.findall(r"\{ t: '((?:\\.|[^'])*)'", step_text)
result = json.loads((historical / 'reference-result.json').read_text())
source_inputs = [basis / 'README.md', basis / '05_LOGO_AND_BRAND.md', html_path, historical / 'reference2.mjs', historical / 'REFERENCE_PREPARATION.md', historical / 'reference-result.json']
screenshots = sorted(historical.glob('reference-*-*.png'))
record = {
    'schema': 'shell-reference-local-asset-audit/v1',
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'repo_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(),
    'method': 'Local read, SHA256, HTMLParser, base64 PNG header dimensions, source inspection; no browser, renderer or network access.',
    'python': sys.version,
    'inputs': [identity(p) for p in source_inputs],
    'packaged_assets_and_mock': assets,
    'unique_embedded_images': list(inventory.images.values()),
    'markup_references': inventory.references,
    'script_elements': inventory.scripts,
    'embedded_font_face_count': html.count('@font-face'),
    'walkthrough': {'count': len(titles), 'titles': [{'one_based_step': i + 1, 'title': title.replace("\\'", "'")} for i, title in enumerate(titles)], 'source_lines': {'STEPS': 936, 'renderWalk': 994, 'click_list': 1003, 'previous_next': 1008, 'keyboard': 1010, 'fit': 1018, 'tabs': 1030, 'theme': 1043}},
    'historical_driver': {
        'invocation_as_recorded': 'node <browser-01>/reference.mjs exited1 due evaluator assertion; node <browser-01>/reference2.mjs exited0; prior exact host escalation after sandbox denial (historical only)',
        'recorded_node': result['node'], 'recorded_browser': result['browser'],
        'driver_contract': '1800x1100 viewport; Walkthrough scenes17/18; light/dark; fullPage, shell and rail PNGs; logical1180x720 assertion; HTTPS route abort; finally browser.close',
        'recorded_requests': result['requests'], 'recorded_errors': result['errors'],
        'font_calibration': 'Preparation prose says fallback and driver aborts HTTPS; result requests[] is empty and document.fonts reports both loaded/unloaded Plex faces. Computed family list/status does not prove glyph face. No guaranteed Plex or fully proven exclusive fallback claim.',
        'captures': [{'scene': c['scene'], 'theme': c['theme'], 'logical_dimensions': [c['geometry']['width'], c['geometry']['height']], 'rendered_box': c['geometry']['box'], 'transform': c['geometry']['transform'], 'computed_family_list': c['geometry']['font'], 'recorded_faces': c['geometry']['faces']} for c in result['captures']],
        'existing_screenshot_identities': [identity(p) for p in screenshots],
        'new_execution': False,
    },
    'source_recreation_limit': '05_LOGO_AND_BRAND.md says scratch scripts were not kept; random quilting makes a pixel-exact original re-derivation not expected. Preserve committed masters; audit does not recreate them.',
    'claims': {'eleven_packaged_assets_match_readme': sum('/assets/' in a['path'] for a in assets) == 11 and all(a['matches_readme'] for a in assets), 'mock_matches_readme': all(a['matches_readme'] for a in assets if '/mock/' in a['path']), 'six_unique_pngs': len(inventory.images) == 6, 'no_external_script_elements': all(s['inline'] for s in inventory.scripts), 'no_missing_relative_markup_references': all(a.get('exists_relative_to_mock', True) for a in inventory.references), 'walkthrough_count26': len(titles) == 26},
}
with (out / 'INVENTORY_v1.json').open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
print(json.dumps({'claims': record['claims'], 'images': [{'dimensions': i['dimensions'], 'role': i['role'], 'occurrences': len(i['occurrences'])} for i in inventory.images.values()], 'external_references': [r for r in inventory.references if r['kind'] == 'external'], 'historical_screenshot_count': len(screenshots)}, indent=2))
