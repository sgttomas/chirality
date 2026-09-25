"""Row conservation and quote currency for the 8 touched registers.
usage: rowcons.py <repo> <table.tsv> <preimage-commit>"""
import csv, io, subprocess, sys
from pathlib import Path
repo, table, base = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
regs = [l.split('\t')[0] for l in open(table, encoding='utf-8') if l.split('\t')[0].endswith('/Dependencies.csv')]
def rows(text):
    return {r['DependencyID']: r for r in csv.DictReader(io.StringIO(text))}
tot_added_active = 0
tot_retired = 0
tot_changed = 0
allok = True
for p in regs:
    now = rows((repo / p).read_text(encoding='utf-8'))
    r = subprocess.run(['git', '-C', str(repo), 'show', f'{base}:{p}'], capture_output=True, text=True)
    before = rows(r.stdout) if r.returncode == 0 else {}
    superset = set(before) <= set(now)
    act_before = {k for k, v in before.items() if v['Status'] == 'ACTIVE'}
    act_now = {k for k, v in now.items() if v['Status'] == 'ACTIVE'}
    gained = sorted(act_now - act_before)
    lost = sorted(act_before - act_now)
    changed = sorted(k for k in before if k in now and before[k] != now[k])
    diffcells = {k: sorted(c for c in before[k] if before[k][c] != now[k][c]) for k in changed}
    retired_now = sorted(k for k, v in now.items() if v['Status'] == 'RETIRED')
    tot_added_active += len(gained); tot_retired += len(retired_now); tot_changed += len(changed)
    allok &= superset
    print(f"{p}\n  before={len(before)} after={len(now)} superset={superset} ACTIVE+={gained} ACTIVE-={lost}")
    for k in changed:
        print(f"  changed {k}: {diffcells[k]}")
    # quote currency for new/refreshed rows
    for k, v in now.items():
        if k not in before or (k in diffcells and 'EvidenceQuote' in diffcells[k]):
            ef = v['EvidenceFile']
            cand = [repo / 'projects/pec' / ef]
            text = next((c.read_text(encoding='utf-8') for c in cand if c.exists()), None)
            ok = text is not None and v['EvidenceQuote'] in text
            if v['DependencyClass'] == 'ANCHOR':
                print(f"  quote {k} (ANCHOR, D-PEC-62 locus-descriptor form '{v['EvidenceQuote']}'; not a verbatim-quote row) in {ef}: {'VERBATIM' if ok else 'NOT VERBATIM (expected for this form)'}")
            else:
                print(f"  quote {k} (EXECUTION) in {ef}: {'VERBATIM' if ok else 'NOT VERBATIM'}")
                allok &= ok
print(f"TOTAL ACTIVE gained={tot_added_active} RETIRED rows now={tot_retired} changed existing rows={tot_changed} ALL_OK(superset + EXECUTION quote currency)={allok}")
