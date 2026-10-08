"""RV123 (round 2; S = WT/scratch/rv123_rvp2/r2): copy text evidence into the records with placeholder paths only (WT, S, NUM, P), and
screen for absolute home or private paths and this machine's names (never printed)."""
import re, subprocess, sys, pathlib
U = '/' + 'Us' + 'ers/'
PV = '/' + 'pri' + 'vate/'
HOME = U + 'ry' + 'an'
WT = HOME + '/dev/chirality-t3'
REPL = [(WT + '/scratch/rv123_rvp2/r2', 'S'), (WT + '/scratch/rv123_rvp2', 'WT/scratch/rv123_rvp2'), (WT + '/numerics', 'NUM'), (WT, 'WT'),
        (HOME + '/.rustup', '<rustup>'), (HOME + '/.local', '<local>'), (HOME + '/.cargo', '<cargo>'),
        (HOME + '/.claude', '<claude>'), (HOME, '<home>')]
def names():
    out = set()
    for cmd in (['hostname'], ['scutil', '--get', 'LocalHostName'], ['scutil', '--get', 'ComputerName']):
        try:
            v = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        except Exception:
            continue
        for part in re.split(r'[^A-Za-z0-9]+', v):
            if len(part) >= 4 and part.lower() not in {'local', 'home', 'redacted-label', 'mini', 'pro', 'air'}:
                out.add(part.lower())
    return out
NAMES = names()
def clean(text):
    for a, b in REPL:
        text = text.replace(a, b)
    text = re.sub(re.escape(PV) + r'(tmp|var)/\S*', '<tmp>', text)
    return text
def screen(text):
    hits = []
    for pat in (U, PV, '~' + '/'):
        if pat in text: hits.append(pat)
    low = text.lower()
    for n in NAMES:
        if n in low: hits.append('<host-name>')
    return hits
if __name__ == '__main__':
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    t = clean(src.read_text(errors='replace'))
    h = screen(t)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(t)
    print(f'{dst.name} hits={len(h)}' + ('' if not h else ' ' + ','.join(sorted(set(h)))))
