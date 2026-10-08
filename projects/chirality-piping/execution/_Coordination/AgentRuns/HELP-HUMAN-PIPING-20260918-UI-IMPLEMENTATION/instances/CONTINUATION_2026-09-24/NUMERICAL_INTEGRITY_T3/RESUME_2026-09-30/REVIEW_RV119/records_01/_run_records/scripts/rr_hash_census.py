#!/usr/bin/env python3
"""RV119: every abbreviated sha256 citation (`<8+ hex>…`) in RR's appended text (lines >= start) and in WG's
T3 section, matched against the sha256 of every file at H under projects/chirality-piping (blobs read with
`git cat-file --batch`), and, for statics, against the files' JCS-free raw bytes only. For each citation the
script prints the line, the hex, and the matching file(s); citations that match no file are listed for a
manual check (canonical-form hashes such as H(DEF-C), or decompressed content).
Path-bound citations ("`path` ... `hex…`" in one sentence) are also checked against that exact path.
Usage: rr_hash_census.py <repo> <H> <RR start line>"""
import re, subprocess, sys, hashlib, collections
repo, H, start = sys.argv[1], sys.argv[2], int(sys.argv[3])
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
P = "projects/chirality-piping/"
T3 = P + "execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
R = T3 + "RESUME_2026-09-30/"
WGP = P + "execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md"
ents = [l.split("\t",1) for l in git("ls-tree","-r",H,"--",P).decode().splitlines()]
paths = {p: m.split()[2] for m,p in ents if m.split()[1] == "blob"}
blob2paths = collections.defaultdict(list)
for p,b in paths.items(): blob2paths[b].append(p)
proc = subprocess.Popen(["git","-C",repo,"cat-file","--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
sha_of = {}
for b in blob2paths:
    proc.stdin.write((b+"\n").encode()); proc.stdin.flush()
    hdr = proc.stdout.readline().split(); size = int(hdr[2]); data = proc.stdout.read(size); proc.stdout.read(1)
    sha_of[b] = hashlib.sha256(data).hexdigest()
proc.stdin.close(); proc.wait()
by_sha = collections.defaultdict(list)
for b,s in sha_of.items():
    for p in blob2paths[b]: by_sha[s].append(p)
shas = sorted(by_sha)
import bisect
def lookup(hx):
    i = bisect.bisect_left(shas, hx); out = []
    while i < len(shas) and shas[i].startswith(hx): out += by_sha[shas[i]]; i += 1
    return out
rr = git("show", f"{H}:{T3}ROOT_RULINGS_V1.md").decode().split("\n")
wg = git("show", f"{H}:{WGP}").decode().split("\n")
s = next(i for i,l in enumerate(wg) if l.startswith("## T3 current route"))
hexre = re.compile(r"`([0-9a-f]{8,64})(?:…|\.\.\.)")
pathhex = re.compile(r"`((?:R/|IMPLEMENTATION/|BRIEFS/|statics/|rvr_|evidence/|_run_records/)[^`]+\.[A-Za-z0-9_]+)`(?:(?!`(?:R/|IMPLEMENTATION/|BRIEFS/)).){0,80}?`([0-9a-f]{8,64})(?:…|\.\.\.)")
def short(p): return p.replace(R,"R/").replace(T3,"T3/").replace(P,"P/")
n=matched=0; unmatched=[]; pb=pbok=0; pbad=[]
for tag, lines, off in (("RR", rr[start-1:], start), ("WG", wg[s:], s+1)):
    for i,l in enumerate(lines):
        for hx in hexre.findall(l):
            n += 1; m = lookup(hx)
            if m: matched += 1; print(f"{tag}:{i+off}\t{hx}\tFILE\t{'; '.join(short(x) for x in m[:3])}{' (+%d)'%(len(m)-3) if len(m)>3 else ''}")
            else: unmatched.append((tag, i+off, hx, l.strip()[:160]))
        for cp, hx in pathhex.findall(l):
            pb += 1
            cands = [x for x in paths if x.endswith("/" + cp.split("R/",1)[-1] if cp.startswith("R/") else "/" + cp)]
            if cp.startswith("R/"): cands = [R + cp[2:]] if (R + cp[2:]) in paths else cands
            good = any(sha_of[paths[c]].startswith(hx) for c in cands)
            pbok += good
            if not good: pbad.append((tag, i+off, cp, hx, len(cands)))
print(f"hex citations {n}; matching a file at H: {matched}; not matching a file: {len(unmatched)}")
for u in unmatched: print("NOFILE\t%s:%d\t%s\t%s" % u)
print(f"path-bound citations {pb}; the named path's sha256 matches: {pbok}")
for b in pbad: print("PATHBOUND-MISMATCH\t%s:%d\t%s\t%s\tcandidates=%d" % b)
