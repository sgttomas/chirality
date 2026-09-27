#!/usr/bin/env python3
"""Render (or check) the D1 premise-amendment candidates from their premise ledgers.

Each premise/<KEY>.json names one target and an ordered list of hunks:
  {"key": ..., "target": <repo-relative path>, "preimage_sha256": <64 hex>,
   "hunks": [{"id": "P01", "cause": "...", "pre": "<exact old text>",
              "post": "<exact new text>", "why": "..."}, ...]}

The preimage is read with `git show <observation>:<target>` from --gitdir and
must hash to preimage_sha256. Hunks apply in order to the running text; each
"pre" must occur exactly once in the running text at the time it applies (so
no hunk is ambiguous), and "pre" must be non-empty. The result is the
candidate. Because every byte outside the listed hunks is copied from the
preimage, the ledger is a complete account of what the amendment changes.

  --write   write candidates/<target> (default: check only)
  --check   require each existing candidate to equal the rendering (default)

Exit 0 when every ledger renders (and, in check mode, matches); 1 otherwise.
Stdlib only.
"""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--gitdir", required=True)
ap.add_argument("--prep", required=True)
ap.add_argument("--observation", default=None)
ap.add_argument("--write", action="store_true")
ap.add_argument("--only", nargs="*")
a = ap.parse_args()
prep = Path(a.prep)
targets = json.loads((prep / "targets.json").read_text(encoding="utf-8"))
obs = a.observation or targets["observation_commit"]
known = {t["key"]: t for t in targets["targets"]}

fails = 0
for lf in sorted((prep / "premise").glob("*.json")):
    led = json.loads(lf.read_text(encoding="utf-8"))
    key = led["key"]
    if a.only and key not in a.only:
        continue
    t = known.get(key)
    if t is None or t["path"] != led["target"] or t["preimage_sha256"] != led["preimage_sha256"]:
        print(f"FAIL {key} ledger target/preimage disagrees with targets.json"); fails += 1; continue
    r = subprocess.run(["git", "-C", a.gitdir, "show", f"{obs}:{led['target']}"], capture_output=True)
    if r.returncode != 0:
        print(f"FAIL {key} preimage unreadable at {obs}"); fails += 1; continue
    pre_b = r.stdout
    if hashlib.sha256(pre_b).hexdigest() != led["preimage_sha256"]:
        print(f"FAIL {key} preimage hash mismatch at {obs}"); fails += 1; continue
    text = pre_b.decode("utf-8")
    ok = True
    seen = set()
    for h in led["hunks"]:
        hid = h["id"]
        if hid in seen or not h["pre"]:
            print(f"FAIL {key} {hid} duplicate id or empty pre"); ok = False; break
        seen.add(hid)
        n = text.count(h["pre"])
        if n != 1:
            print(f"FAIL {key} {hid} pre occurs {n} times (must be exactly 1)"); ok = False; break
        text = text.replace(h["pre"], h["post"], 1)
    if not ok:
        fails += 1; continue
    out = text.encode("utf-8")
    cp = prep / "candidates" / led["target"]
    digest = hashlib.sha256(out).hexdigest()
    if a.write:
        cp.parent.mkdir(parents=True, exist_ok=True)
        cp.write_bytes(out)
        print(f"WROTE {key} {len(led['hunks'])} hunks sha256 {digest} {cp.relative_to(prep)}")
    else:
        if not cp.is_file() or cp.read_bytes() != out:
            print(f"FAIL {key} candidate differs from ledger rendering"); fails += 1; continue
        print(f"PASS {key} {len(led['hunks'])} hunks; candidate equals ledger rendering; sha256 {digest}")
print(f"RESULT {'PASS' if fails == 0 else 'FAIL'} fails={fails}")
sys.exit(0 if fails == 0 else 1)
