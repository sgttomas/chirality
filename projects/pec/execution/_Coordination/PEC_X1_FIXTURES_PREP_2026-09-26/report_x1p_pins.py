#!/usr/bin/env python3
"""Table every pinned (commit, path, blob) reference: resolves, ancestor of <observation>,
blob equal at the pinned commit, and the path's blob at <observation> (drift is informational).
Usage: report_x1p_pins.py <repo> <observation commit> <pinned MANIFEST.json>"""
import json, subprocess, sys
repo, obs, man = sys.argv[1:4]
def g(*a): return subprocess.run(["git", "-C", repo, *a], capture_output=True)
m = json.load(open(man)); bad = 0
print("| Pin | Commit | Path | Blob | Resolves | Ancestor of observation | Blob at pinned commit | Same path at observation |")
print("|---|---|---|---|---|---|---|---|")
for e in m["templates"] + m["pins"]:
    ok_c = g("cat-file", "-e", e["commit"] + "^{commit}").returncode == 0
    anc = g("merge-base", "--is-ancestor", e["commit"], obs).returncode == 0
    r = g("rev-parse", "--verify", "--quiet", f"{e['commit']}:{e['path']}")
    eq = r.returncode == 0 and r.stdout.decode().strip() == e["blob"]
    o = g("rev-parse", "--verify", "--quiet", f"{obs}:{e['path']}")
    drift = "absent" if o.returncode else ("unchanged" if o.stdout.decode().strip() == e["blob"] else "changed " + o.stdout.decode().strip()[:9])
    bad += not (ok_c and anc and eq)
    print(f"| {e['id']} | `{e['commit'][:9]}` | `{e['path']}` | `{e['blob'][:9]}` | {'yes' if ok_c else 'NO'} | {'yes' if anc else 'NO'} | {'equal' if eq else 'DIFFERS'} | {drift} |")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(m['templates'])+len(m['pins'])-bad}/{len(m['templates'])+len(m['pins'])}")
sys.exit(1 if bad else 0)
