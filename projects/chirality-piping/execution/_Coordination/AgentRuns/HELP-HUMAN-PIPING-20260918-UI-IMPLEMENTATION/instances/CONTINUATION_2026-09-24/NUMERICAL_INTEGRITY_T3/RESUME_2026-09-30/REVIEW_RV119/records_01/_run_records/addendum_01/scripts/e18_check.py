#!/usr/bin/env python3
"""RV119 ADDENDUM_01: E-18's two rewordings, between the reviewed head H and the new head H2.
- RR: which lines of H's RR differ in H2 (other than lines appended after H's end); main's RR is still a byte prefix.
- The brief B2C_REVISION_02.md: which lines differ; its sha256 at H and H2.
- Every other file present at H is byte-identical at H2.
Old and new lines are printed with the host-name forms masked (the earlier form is read from H's RR line;
the laptop-model form is hex-encoded here). Usage: e18_check.py <repo> <M> <H> <H2>"""
import subprocess, sys, hashlib, re, difflib
repo, M, H, H2 = sys.argv[1:5]
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
RR = T3 + "ROOT_RULINGS_V1.md"; BR = T3 + "RESUME_2026-09-30/BRIEFS/B2C_REVISION_02.md"
rr_h = git("show", f"{H}:{RR}"); rr_h2 = git("show", f"{H2}:{RR}"); rr_m = git("show", f"{M}:{RR}")
earlier = re.search(r"beside `([^`]+)`", next(l for l in rr_h.decode().splitlines() if l.startswith("**Screen widened (E-16"))).group(1)
NL = bytes([10])
mb = bytes.fromhex("6d6163626f6f6b").decode()
def mask(t):
    t = re.sub(re.escape(earlier), "<earlier-host>", t, flags=re.I)
    t = re.sub("(?i)" + mb, "<model-form>", t)
    return re.sub(r"\." + "lo" + r"cal\b", "[.]local", t)
def linediff(a, b, name):
    la, lb = a.decode().split("\n"), b.decode().split("\n")
    sm = difflib.SequenceMatcher(a=la, b=lb, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal": continue
        print(f"{name}: {tag} H lines {i1+1}-{i2} -> H2 lines {j1+1}-{j2}")
        if tag == "replace" or (tag == "delete"):
            for k in range(i1, i2): print(f"   - H:{k+1}: {mask(la[k])[:300]}")
        if tag == "replace":
            for k in range(j1, j2): print(f"   + H2:{k+1}: {mask(lb[k])[:300]}")
    return la, lb
print(f"RR sha256 H {hashlib.sha256(rr_h).hexdigest()[:16]}…, H2 {hashlib.sha256(rr_h2).hexdigest()[:16]}…; lines H {rr_h.count(NL)}, H2 {rr_h2.count(NL)}")
print("main's RR is an exact byte prefix of H2's:", rr_h2.startswith(rr_m))
la, lb = linediff(rr_h, rr_h2, "RR")
br_h = git("show", f"{H}:{BR}"); br_h2 = git("show", f"{H2}:{BR}")
print(f"brief sha256 H {hashlib.sha256(br_h).hexdigest()}  H2 {hashlib.sha256(br_h2).hexdigest()}")
linediff(br_h, br_h2, "brief")
print("earlier form present (any case) in H2's RR:", bool(re.search(re.escape(earlier), rr_h2.decode(), re.I)), "; in H2's brief:", bool(re.search(re.escape(earlier), br_h2.decode(), re.I)))
# every other file present at H unchanged at H2
ch = [r.split("\t") for r in git("diff", "--no-renames", "--name-status", H, H2).decode().splitlines()]
print("H..H2 non-added changes:", [(s, p.replace(T3, "T3/")) for s, p in ch if s != "A"])
