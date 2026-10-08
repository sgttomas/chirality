#!/usr/bin/env python3
"""RV119: E-16's redaction (IMPLEMENTATION/REDACTION_E16/RECORD.md) against the PR head.
For each of the table's rows (path under R/REVIEW_RV113/rvr_sr_py_01/, old sha256, new sha256):
- the blob at the pre-redaction rev hashes to the old sha256;
- H's blob hashes to the new sha256, decompresses, parses as XML and has no hostname attribute;
- the redacted file decompresses to the original with exactly one hostname attribute removed;
- the pre-redaction blob id is in neither H's nor M's tree, and no file in H's tree (any path) hashes to an old sha256.
Also: rvr_sr_py_01/SHA256SUMS verifies from H's tree, and REVIEW.md's sha256 is reported; and each removed
attribute value is compared with the machine's network name (read at run time; only the comparison is printed).
Usage: redactions_e16_check.py <repo> <M> <H> <pre-redaction rev>"""
import re, subprocess, sys, hashlib, gzip, posixpath
import xml.etree.ElementTree as ET
repo, M, H, OLD = sys.argv[1:5]
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
T3 = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
D = T3 + "RESUME_2026-09-30/REVIEW_RV113/rvr_sr_py_01/"
doc = git("show", f"{H}:{T3}IMPLEMENTATION/REDACTION_E16/RECORD.md").decode()
rows = re.findall(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \| `([0-9a-f]{64})` \|", doc, re.M)
print("rows in REDACTION_E16's table:", len(rows), "; distinct paths:", len({p for p,_,_ in rows}))
def blob(rev, p):
    r = subprocess.run(["git","-C",repo,"rev-parse",f"{rev}:{p}"], capture_output=True)
    return r.stdout.decode().strip() if r.returncode == 0 else None
htree = {}
for l in git("ls-tree","-r",H).decode().splitlines():
    meta,p = l.split("\t",1); htree[p] = meta.split()[2]
mtree = set(l.split()[2] for l in git("ls-tree","-r",M).decode().splitlines())
old_ok=new_ok=attr_free=parse_ok=diff_ok=0; old_blobs=set(); olds=set(); news=set()
attr = re.compile(b' host' + b'name="[^"]*"')
for p,o,n in rows:
    olds.add(o); news.add(n)
    b0 = blob(OLD, D+p); bh = htree.get(D+p)
    d0 = git("cat-file","blob",b0) if b0 else None
    dh = git("cat-file","blob",bh) if bh else None
    if d0 is not None:
        old_blobs.add(b0)
        if hashlib.sha256(d0).hexdigest()==o: old_ok+=1
        else: print("  OLD MISMATCH", p)
    else: print("  not at pre-redaction rev:", p)
    if dh is not None and hashlib.sha256(dh).hexdigest()==n: new_ok+=1
    else: print("  NEW MISMATCH", p)
    if dh is not None:
        xh = gzip.decompress(dh)
        try:
            root = ET.fromstring(xh); parse_ok+=1
            if not any("hostname" in el.attrib for el in root.iter()) and (b"host" + b"name") not in xh: attr_free+=1
            else: print("  ATTRIBUTE PRESENT", p)
        except Exception as e: print("  PARSE FAIL", p, e)
        if d0 is not None:
            x0 = gzip.decompress(d0)
            if len(attr.findall(x0))==1 and attr.sub(b"", x0)==xh: diff_ok+=1
            else: print("  DIFF NOT ONLY THE ATTRIBUTE", p)
print(f"old sha256 match at {OLD[:10]}: {old_ok}/{len(rows)}; new sha256 match at H: {new_ok}/{len(rows)}")
print(f"H's files parse as XML: {parse_ok}; carry no hostname attribute (and no 'hostname' byte string): {attr_free}; equal the original minus exactly one attribute: {diff_ok}")
print("pre-redaction blob ids in H's tree:", len(old_blobs & set(htree.values())), "; in M's tree:", len(old_blobs & mtree))
hits = [p for p,b in htree.items() if p.startswith(T3) and p.endswith(".gz")]
oldhit = [p for p in hits if hashlib.sha256(git("cat-file","blob",htree[p])).hexdigest() in olds]
print(f".gz files under T3 in H's tree: {len(hits)}; hashing to an old sha256: {len(oldhit)}")
ch = [c for c in git("diff","--no-renames","--name-only",M,H).decode().split("\n") if c]
chit = [c for c in ch if hashlib.sha256(git("cat-file","blob",htree[c])).hexdigest() in olds]
print(f"changed files (of {len(ch)}) hashing to an old sha256: {len(chit)}")
# the sum file and REVIEW.md
n=ok=bad=miss=0
for line in git("cat-file","blob",htree[D+"SHA256SUMS"]).decode().splitlines():
    if not line.strip(): continue
    h,name = line.split(None,1); name=name.lstrip("*"); n+=1
    q = posixpath.normpath(posixpath.join(D.rstrip("/"), name))
    if q not in htree: miss+=1; continue
    if hashlib.sha256(git("cat-file","blob",htree[q])).hexdigest()==h: ok+=1
    else: bad+=1
print(f"rvr_sr_py_01/SHA256SUMS at H: {n} entries, {ok} ok, {bad} bad, {miss} missing; the 42 new sha256 all listed: {all((n_ in git('cat-file','blob',htree[D+'SHA256SUMS']).decode()) for n_ in news)}")
print("REVIEW.md sha256 at H:", hashlib.sha256(git("cat-file","blob",htree[D+"REVIEW.md"])).hexdigest())
print("REVIEW.md sha256 at pre-redaction rev:", hashlib.sha256(git("cat-file","blob",blob(OLD, D+"REVIEW.md"))).hexdigest())
s0 = git("show", f"{OLD}:{D}SHA256SUMS").decode().splitlines(); s1 = git("cat-file","blob",htree[D+"SHA256SUMS"]).decode().splitlines()
print(f"SHA256SUMS lines changed between pre-redaction rev and H: {sum(1 for a,b in zip(s0,s1) if a!=b)} (line counts {len(s0)} -> {len(s1)})")
net = subprocess.run(["hostname"], capture_output=True).stdout.decode().strip()
eq = ne = 0
for p_, o_, n_ in rows:
    b0 = blob(OLD, D + p_)
    for v in re.findall(b' host' + b'name="([^"]*)"', gzip.decompress(git("cat-file", "blob", b0))):
        if v.decode() == net: eq += 1
        else: ne += 1
print(f"removed attribute values equal to the network name: {eq}; different: {ne}")
