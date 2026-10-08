#!/usr/bin/env python3
"""RV119: host-name fragments in split, escaped or character-class forms that a literal screen misses.
Same units as publication_scan.py (added files whole, .gz decompressed; '+' lines of modified files).
Patterns are assembled at run time (the earlier form is read from RR at H); output text is sanitized (fragments written <frag>).
Usage: host_variants_scan.py <repo> <M> <H>"""
import re, subprocess, sys, gzip
repo, M, H = sys.argv[1:4]
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
J = r"[\W_]{0,6}"          # joiners: quotes, brackets, backslashes, hyphens, dots, underscores
T3_ = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
# the earlier form, read from RR at H (E-16's "Screen widened" line names it); its domain labels joined by J
earlier = re.search(r"beside `([^`]+)`", next(l for l in git("show", f"{H}:{T3_}ROOT_RULINGS_V1.md").decode().splitlines() if l.startswith("**Screen widened (E-16"))).group(1)
dom = J.join(re.escape(x) for x in earlier.split(".")[1:])
pats = {
 "model form (split)": "(?i)" + J.join(bytes.fromhex("6d6163626f6f6b").decode()[:3]) + J + bytes.fromhex("6d6163626f6f6b").decode()[3:],
 "first name + s (host prefix)": "(?i)ryan" + J + "s" + J + "(mac|m" + J + "b" + J + "p)",
 "earlier domain (split)": "(?i)\\b" + dom + "\\b",
 "mbp short form": "(?i)\\bmbp\\b",
}
cre = {k: re.compile(v) for k,v in pats.items()}
def sanitize(t):
    for c in cre.values(): t = c.sub("<frag>", t)
    t = re.sub("(?i)ry" + "ans", "<first-name-s>", t)
    t = re.sub(r"\." + "lo" + r"cal\b", "[.]local", t)
    t = t.replace("host" + "name=", "host-name=").replace("/" + "Applications" + "/", "/Appli-cations/")
    return t
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
n = {k: 0 for k in pats}
for row in git("diff","--no-renames","--name-status",M,H).decode().splitlines():
    st,p = row.split("\t",1)
    if st == "A":
        raw = git("show", f"{H}:{p}")
        if p.endswith(".gz"): raw = gzip.decompress(raw)
        lines = list(enumerate(raw.decode("utf-8","replace").splitlines(),1))
    else:
        lines = []; ln = 0
        for l in git("diff","-U0",M,H,"--",p).decode("utf-8","replace").splitlines():
            m = re.match(r"@@ -\S+ \+(\d+)", l)
            if m: ln = int(m.group(1)); continue
            if l.startswith("+") and not l.startswith("+++"): lines.append((ln,l[1:])); ln += 1
    for i,l in lines:
        for k,c in cre.items():
            if c.search(l):
                n[k] += 1
                print(f"{k}\t{p.replace(T3,'T3/')}\t{i}\t{sanitize(l.strip())[:200]}")
print("TOTALS\t" + "\t".join(f"{k}={v}" for k,v in n.items()))
