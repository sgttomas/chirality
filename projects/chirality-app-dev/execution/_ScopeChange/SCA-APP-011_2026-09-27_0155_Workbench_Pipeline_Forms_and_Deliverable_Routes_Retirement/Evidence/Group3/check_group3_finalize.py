#!/usr/bin/env python3
"""Exercise group3_corrections.py (--check, --apply, --finalize) in a scratch copy.

Run from the repository root, on a tree that holds either the group-2 candidate
(before the correction) or the corrected group-3 candidate. It copies the 16
candidate files into a temporary root, brings the copy to the group-2 candidate
state for DEL-07-04 when needed, and checks:
  - --check fails before the correction and passes after --apply;
  - --apply refuses a second run;
  - build_amendment_preview.py --finalize (group 2) refuses the corrected file;
  - group3_corrections.py --finalize refuses a draft heading, a date mismatch
    and a wrong path, then applies E47 only, and refuses a rerun;
  - the repository tree is unchanged.
Exit 1 on any FAIL.
"""
import csv, hashlib, importlib.util, os, shutil, subprocess, sys, tempfile

SNAP = ("projects/chirality-app-dev/execution/_ScopeChange/"
        "SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement")
G3 = os.path.join(SNAP, "Evidence/Group3/group3_corrections.py")
B2 = os.path.join(SNAP, "Evidence/Group2/build_amendment_preview.py")
CSVP = os.path.join(SNAP, "Evidence/Group2/PREIMAGE_POSTIMAGE.csv")
DECOMP = "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md"
spec = importlib.util.spec_from_file_location("g3", G3)
g3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g3)
rows = list(csv.DictReader(open(CSVP, newline="", encoding="utf-8")))


def h(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def run(script, *a):
    p = subprocess.run([sys.executable, script, *a], capture_output=True, text=True)
    print("$", os.path.basename(script), " ".join(x if len(x) < 60 else "..." + x[-40:] for x in a), "-> rc", p.returncode)
    out = (p.stdout + p.stderr).strip()
    print("   " + out[-400:].replace("\n", "\n   "))
    return p.returncode


before = {r["File"]: h(r["File"]) for r in rows}
root = tempfile.mkdtemp(prefix="sca011-g3-")
for r in rows:
    d = os.path.join(root, r["File"])
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy(r["File"], d)
# Bring the copy to the group-2 candidate state for each corrected file.
for c in g3.CORRECTIONS:
    p = os.path.join(root, c["file"])
    t = open(p, encoding="utf-8").read()
    if c["new"] in t:
        open(p, "w", encoding="utf-8").write(t.replace(c["new"], c["old"], 1))
res = {}
res["group-2 candidate state reproduced"] = all(
    h(os.path.join(root, c["file"])) == c["group2_candidate_sha256"] for c in g3.CORRECTIONS)
res["--check fails before correction"] = run(G3, "--check", "--root", root) == 1
res["--apply"] = run(G3, "--apply", "--root", root) == 0
res["corrected hash"] = all(h(os.path.join(root, c["file"])) == c["corrected_candidate_sha256"] for c in g3.CORRECTIONS)
res["--apply rerun refused"] = run(G3, "--apply", "--root", root) == 1
res["--check passes after correction"] = run(G3, "--check", "--root", root) == 0
dec = ("projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/"
       "SCA-APP-011_GROUP-3_2099-01-02/DECISION.md")
os.makedirs(os.path.dirname(os.path.join(root, dec)))
open(os.path.join(root, dec), "w").write("# SCA-APP-011 checkpoint group 3 — draft\n")
res["finalize refused: heading"] = run(G3, "--finalize", "--date", "2099-01-02", "--group3-decision", dec, "--root", root) == 3
open(os.path.join(root, dec), "w").write("# SCA-APP-011 checkpoint group 3 — accepted (test)\n")
res["finalize refused: date mismatch"] = run(G3, "--finalize", "--date", "2099-01-03", "--group3-decision", dec, "--root", root) == 3
res["finalize refused: wrong path"] = run(G3, "--finalize", "--date", "2099-01-02", "--group3-decision", "x/DECISION.md", "--root", root) == 3
res["group-2 --finalize refuses corrected file"] = run(B2, "--finalize", "--date", "2099-01-02", "--group3-decision", dec, "--root", root) == 1
snap = {r["File"]: h(os.path.join(root, r["File"])) for r in rows}
res["group-3 --finalize"] = run(G3, "--finalize", "--date", "2099-01-02", "--group3-decision", dec, "--root", root) == 0
after = {r["File"]: h(os.path.join(root, r["File"])) for r in rows}
t = open(os.path.join(root, DECOMP), encoding="utf-8").read()
res["E47 applied"] = "| Date | 2099-01-02 |" in t and "amended by SCA-APP-011 |" in t
res["only the decomposition changed"] = [p for p in after if after[p] != snap[p]] == [DECOMP]
res["finalize rerun refused"] = run(G3, "--finalize", "--date", "2099-01-02", "--group3-decision", dec, "--root", root) == 1
res["repository tree unchanged"] = {r["File"]: h(r["File"]) for r in rows} == before
shutil.rmtree(root)
for k, v in res.items():
    print("PASS" if v else "FAIL", k)
sys.exit(0 if all(res.values()) else 1)
