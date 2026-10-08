#!/usr/bin/env python3
"""RV119: extra host-data shapes over the PR's added text (whole files, .gz decompressed) and the '+' lines of
modified files: private IPv4 addresses, MAC addresses, URL-encoded home roots, Windows-style home roots,
user-data or keychain paths. Hits are printed with the matched token's shape only.
Usage: extra_host_scan.py <repo> <M> <H>"""
import re, subprocess, sys, gzip, collections
repo, M, H = sys.argv[1:4]
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
U = "Us" + "ers"
pats = {
 "private IPv4": re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b"),
 "MAC address": re.compile(r"\b[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}\b"),
 "URL-encoded home root": re.compile(r"%2F" + U + r"%2F|" + U + r"%2F", re.I),
 "Windows home root": re.compile(r"[A-Za-z]:\\\\" + U + r"\\\\"),
 "keychain or app-support": re.compile(r"Keychains|Application Support|Library/Preferences"),
}
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
cnt = collections.Counter()
for row in git("diff","--no-renames","--name-status",M,H).decode().splitlines():
    st,p = row.split("\t",1)
    if st == "A":
        raw = git("show", f"{H}:{p}")
        if p.endswith(".gz"): raw = gzip.decompress(raw)
        lines = list(enumerate(raw.decode("utf-8","replace").splitlines(),1))
    else:
        lines=[]; ln=0
        for l in git("diff","-U0",M,H,"--",p).decode("utf-8","replace").splitlines():
            m = re.match(r"@@ -\S+ \+(\d+)", l)
            if m: ln=int(m.group(1)); continue
            if l.startswith("+") and not l.startswith("+++"): lines.append((ln,l[1:])); ln+=1
    for i,l in lines:
        for k,c in pats.items():
            for m in c.finditer(l):
                cnt[k]+=1
                tok = m.group(0)
                shape = re.sub(r"[0-9]", "9", tok) if k != "keychain or app-support" else tok
                print(f"{k}\t{p.replace(T3,'T3/')}\t{i}\t{shape[:40]}\t{l.strip()[:120] if k=='MAC address' else ''}")
print("TOTALS\t" + "\t".join(f"{k}={cnt[k]}" for k in pats))
