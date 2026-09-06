from pathlib import Path
import json, hashlib, sys
from PIL import Image, ImageDraw

root = Path('/private/tmp/app-loop-t3-native-ac3dexfs/fixtures')
files = []
def save(name, content):
    p = root / name
    if p.exists():
        raise RuntimeError(f'Preserve prior fixture: {p}')
    p.write_bytes(content)
    files.append(p)

picture = Image.new('RGB', (900, 400), '#e8efed')
draw = ImageDraw.Draw(picture)
draw.rectangle((30, 30, 870, 370), outline='#365b54', width=8)
draw.text((80, 160), 'T3 LOCAL IMAGE FIXTURE', fill='#12342f', font_size=46)
for extension, format_name in [('png', 'PNG'), ('jpg', 'JPEG'), ('gif', 'GIF'), ('webp', 'WEBP')]:
    p = root / ('Picture.' + extension)
    assert not p.exists()
    picture.save(p, format_name)
    files.append(p)

save('Image-only.svg', b'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="400" viewBox="0 0 900 400"><rect width="900" height="400" fill="#e8efed"/><text x="60" y="180" font-size="42">T3 SVG IMAGE FIXTURE</text><script>window.__t3SvgExecuted = true; alert('T3 SVG SCRIPT MUST NOT RUN');</script><image href="http://127.0.0.1:39119/t3-external-probe.png" width="1" height="1"/></svg>''')
save('Oversized image.png', (root / 'Picture.png').read_bytes() + b'\0' * (2 * 1024 * 1024 + 1))
save('Folded.json', b'{"fixture":"T3 folded JSON","nested":{"items":[1,true,null,{"__proto__":"literal key","constructor":"also literal"}]}}\n')
save('Malformed.json', b'{"broken": [1, 2,}\n')
save('Deep.json', ('[' * 200 + '0' + ']' * 200).encode())
save('Headings and links.md', b'''# Headings and links fixture

[Open local note](Readable%20note.md)

## Repeated heading

First real section.

```md
## Not a real heading
```

## Repeated heading

Second real section.

[Invalid scheme](javascript:alert(1))

<script>window.__t3RawMarkdownExecuted = true;</script>
''')
save('Long filename for readable metadata and breadcrumb wrapping with all content accessible.md', b'# Long file name fixture\n\nThe complete name and content must remain readable.\n')
print(json.dumps({'python': sys.version, 'root': str(root), 'added_files': [{'path': str(p), 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(files)]}, indent=2))
