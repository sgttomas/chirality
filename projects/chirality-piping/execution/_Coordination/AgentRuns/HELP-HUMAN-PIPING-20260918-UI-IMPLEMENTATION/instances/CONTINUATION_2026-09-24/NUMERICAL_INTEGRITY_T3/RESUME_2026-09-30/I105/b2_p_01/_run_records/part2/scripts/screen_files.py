"""I105: the T3 host screen's patterns (WT/tools/t3_host_screen.py, unmodified, its final main() call
left out) over every file under a directory, read whole. Prints hits with the match replaced; exit 1 on any."""
import pathlib, sys
src = pathlib.Path('WT/tools/t3_host_screen.py').read_text()
assert src.rstrip().endswith('main()')
g = {'__file__': 'WT/tools/t3_host_screen.py', '__name__': 'screen'}
exec(compile(src.rstrip()[:-len('main()')], 't3_host_screen.py', 'exec'), g)
hits = files = 0
for f in sorted(pathlib.Path(sys.argv[1]).rglob('*')):
    if f.is_symlink():
        print('SYMLINK', f.name); hits += 1; continue
    if not f.is_file():
        continue
    files += 1
    for ln, text in enumerate(f.read_bytes().splitlines(), 1):
        for label, c in g['cre'].items():
            if c.search(text):
                print(f'HIT {f.relative_to(sys.argv[1])}:{ln} [{label}]'); hits += 1; break
print(f'files {files}, hits {hits}, names screened {len(g["names"])}')
sys.exit(1 if hits else 0)
