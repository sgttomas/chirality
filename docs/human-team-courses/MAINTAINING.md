# Maintaining the course series

This file is for maintainers. It is not part of the learner series; do not render or publish it as a course page.

The Markdown files in this directory, `courses/` and `instructors/` are the maintained source. Each HTML file renders its matching source as a self-contained reading edition. External references need a network connection.

## Render the reading editions

The renderer uses the dependencies in `../alignment-manual/requirements.txt`. Run these commands from the repository root:

```sh
python3 -m venv /tmp/chirality-course-renderer
/tmp/chirality-course-renderer/bin/python -m pip install -r docs/alignment-manual/requirements.txt
```

Render the learner and instructor files with the edition basis below. For a new edition, set the basis date and the full commit of the repository used to prepare it.

```sh
/tmp/chirality-course-renderer/bin/python - <<'PY'
from pathlib import Path
import subprocess
root = Path('docs/human-team-courses')
for source in sorted(root.rglob('*.md')):
    if source.name == 'MAINTAINING.md':
        continue
    output = source.with_name('index.html') if source.name == 'README.md' else source.with_suffix('.html')
    subprocess.run([
        '/tmp/chirality-course-renderer/bin/python',
        'docs/alignment-manual/render_manual.py',
        '--source', str(source), '--output', str(output),
        '--basis-date', '2026-10-25',
        '--basis-revision', 'b50a2116352fd7a2bd5ddbeec7b6b6037e86deeb',
        '--edition-label', 'Human-agent team courses', '--metadata-at-end',
    ], check=True)
PY
```

Each source fingerprint identifies the rendered Markdown bytes. Add `--check` to the renderer arguments to check currency without writing.

After a source change, regenerate the affected HTML. Check navigation and content at desktop and narrow widths. Check print layout before distributing a printed copy.

The public website imports a pinned snapshot of the learner and instructor sources. Exclude this file from that snapshot.
