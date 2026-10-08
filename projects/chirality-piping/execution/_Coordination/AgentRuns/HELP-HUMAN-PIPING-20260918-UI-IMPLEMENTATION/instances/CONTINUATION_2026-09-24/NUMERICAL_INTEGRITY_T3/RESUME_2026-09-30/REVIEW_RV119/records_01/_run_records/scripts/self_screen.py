#!/usr/bin/env python3
"""RV119: screen RV119's own records folder before return. Terms (assembled or read at run time): the strict pattern
of B1_COMMON; the machine's network name, local host name and computer name; the laptop-model form; the earlier
form (read from RR at H) and its domain; the dot-local suffix; the junit hostname attribute; split host forms;
the owner's e-mail; absolute temp, home and system roots. Prints counts and file:line for any hit, with the
matched text masked. Usage: self_screen.py <records folder> <repo> <H>"""
import os, re, sys, subprocess
D, repo, H = sys.argv[1:4]
def sh(*a):
    r = subprocess.run(list(a), capture_output=True); return r.stdout.decode().strip() if r.returncode == 0 else ""
T3_ = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
rr = sh("git", "-C", repo, "show", f"{H}:{T3_}ROOT_RULINGS_V1.md")
earlier = re.search(r"beside `([^`]+)`", next(l for l in rr.splitlines() if l.startswith("**Screen widened (E-16"))).group(1)
S = "/"; J = r"[\W_]{0,6}"; MB = bytes.fromhex("6d6163626f6f6b").decode()
email = sh("git", "-C", repo, "log", "-1", "--format=%ae", H)
pats = {
 "strict": "~" + S + "|" + S + "Users" + S + "|" + S + "private" + S + r"|\." + "claude" + S + "worktrees|swbpipe" + "-control-layer",
 "network/local/computer name": "(?i)" + "|".join(re.escape(x) for x in (sh("hostname"), sh("scutil", "--get", "LocalHostName"), sh("scutil", "--get", "ComputerName")) if x),
 "laptop-model form": "(?i)" + MB,
 "laptop-model form (split)": "(?i)" + J.join(MB[:3]) + J + MB[3:],
 "earlier form or domain": "(?i)" + re.escape(earlier) + "|" + J.join(re.escape(x) for x in earlier.split(".")[1:]),
 "dot-local": r"\." + "lo" + r"cal\b",
 "junit hostname attribute": "host" + r"name\s*=\s*\"",
 "owner e-mail": re.escape(email) if email else r"(?!x)x",
 "absolute roots": "(?<![\\w.<-])" + S + "(?:tmp|var" + S + "folders|home|Volumes|Library|Applications)" + S,
}
cre = {k: re.compile(v) for k, v in pats.items()}
n = {k: 0 for k in pats}; files = 0
for root, dirs, fs in os.walk(D):
    for f in fs:
        p = os.path.join(root, f); files += 1
        if os.path.islink(p): print("LINK", os.path.relpath(p, D)); continue
        t = open(p, "rb").read().decode("utf-8", "replace")
        for i, l in enumerate(t.splitlines(), 1):
            for k, c in cre.items():
                for m in c.finditer(l):
                    n[k] += 1
                    print(f"HIT\t{k}\t{os.path.relpath(p, D)}:{i}\t{l[max(0,m.start()-30):m.start()]}<masked>{l[m.end():m.end()+30]}")
dirs_build = [r for r, ds, fs in os.walk(D) if os.path.basename(r) == "build"]
print(f"files {files}; folders named build: {len(dirs_build)}; " + "; ".join(f"{k}={v}" for k, v in n.items()))
