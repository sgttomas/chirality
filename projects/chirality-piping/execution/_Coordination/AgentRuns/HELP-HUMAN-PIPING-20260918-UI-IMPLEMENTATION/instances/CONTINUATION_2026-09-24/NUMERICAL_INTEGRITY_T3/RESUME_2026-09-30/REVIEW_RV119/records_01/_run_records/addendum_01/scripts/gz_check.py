#!/usr/bin/env python3
"""RV119 (ADDENDUM_01 copy: an optional last argument gives the rev to read the earlier form from) (from RV117/RV110): every gzipped file PR #1114 adds decompresses, parses by type, and is screened
like text: machine paths, e-mail, token shapes, credential words, host data (the machine's names read at run
time; the laptop-model form; the earlier form, read from RR at H; the dot-local suffix), the junit hostname attribute, and
the strict pattern of B1_COMMON (assembled at run time). Usage: gz_check.py <repo> <M> <H>"""
import gzip, json, re, subprocess, sys, collections
import xml.etree.ElementTree as ET
repo, M, H = sys.argv[1:4]
SRC = sys.argv[4] if len(sys.argv) > 4 else H   # RV119 ADDENDUM_01: the rev whose RR line names the earlier form (the reviewed head; E-18 reworded it at the new head)
def git(*a): return subprocess.run(["git","-C",repo,*a],capture_output=True,check=True).stdout
def sh(*a):
    r = subprocess.run(list(a), capture_output=True); return r.stdout.decode().strip() if r.returncode == 0 else ""
S="/"
net, short, comp = sh("hostname"), sh("scutil","--get","LocalHostName"), sh("scutil","--get","ComputerName")
T3_ = "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
earlier = re.search(r"beside `([^`]+)`", next(l for l in git("show", f"{SRC}:{T3_}ROOT_RULINGS_V1.md").decode().splitlines() if l.startswith("**Screen widened (E-16"))).group(1)
hostalt = "|".join(re.escape(x) for x in (net, short, comp, earlier) if x)
pats = {
 "home/tmp/private paths": re.compile("|".join([S+"Users"+S, S+"private"+S, S+"var"+S+"folders", r"(?<![\w.<{}])"+S+"tmp"+S, S+"Volumes"+S, S+"home"+S+"[a-z]"])),
 "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
 "token-shaped": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36}\b|\bgithub_pat_[A-Za-z0-9_]{50,}|\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}|\bAKIA[0-9A-Z]{16}\b|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[abprs]-[A-Za-z0-9-]{10,}|\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\."),
 "cred words": re.compile(r"(?i)password|secret|token=|authorization:|api[_-]?key"),
 "host names (run time)": re.compile("(?i)" + hostalt),
 "model form": re.compile("(?i)" + bytes.fromhex("6d6163626f6f6b").decode()),
 "dot-local": re.compile(r"\." + "lo" + r"cal\b"),
 "other host data": re.compile("/" + "Applications" + "/" + r"|\bPID\s+(TTY|PPID|USER)|%CPU|session[_-]?id|\btoolu_|\.claude/|\.codex/"),
 "hostname attr": re.compile("host" + r"name\s*="),
 "strict": re.compile("~"+S+"|"+S+"Users"+S+"|"+S+"private"+S+r"|\."+"claude"+S+"worktrees|swbpipe"+"-control-layer"),
 "owner name": re.compile(r"(?i)ryan|tufts"),
}
T3="projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/"
ns=[r.split("\t",1) for r in git("diff","--no-renames","--name-status",M,H).decode().splitlines()]
gz=[p for st,p in ns if st=="A" and p.endswith(".gz")]
print(f"gzipped added files: {len(gz)}")
byfolder=collections.Counter("/".join(p.replace(T3,"T3/").split("/")[:5]) for p in gz)
for k,v in sorted(byfolder.items()): print(f"  {v}\t{k}")
print("file\tgz_bytes\traw_bytes\tlines\tkind\tparses\t" + "\t".join(pats))
tot=[0]*len(pats); tl=0; bad=0; kinds=collections.Counter(); junit_with_attr=0; junit=0
for p in gz:
    b=git("show",f"{H}:{p}")
    try: raw=gzip.decompress(b)
    except Exception as e: print("DECOMPRESS FAIL", p, e); bad+=1; continue
    t=raw.decode("utf-8","replace"); lines=t.splitlines(); inner=p[:-3]; ok=0
    kind = "json" if inner.endswith(".json") else "xml" if inner.endswith(".xml") else "jsonl" if inner.endswith(".jsonl") else "text"
    try:
        if kind=="json": json.loads(t); ok=1
        elif kind=="jsonl": [json.loads(l) for l in lines if l.strip()]; ok=1
        elif kind=="xml":
            root=ET.fromstring(raw); ok=1
            if root.tag in ("testsuites","testsuite"):
                junit+=1
                if any("hostname" in el.attrib for el in root.iter()): junit_with_attr+=1
        else: ok=1
    except Exception: ok=0
    kinds[kind]+=1
    c=[sum(1 for l in lines if r.search(l)) for r in pats.values()]
    tot=[a+x for a,x in zip(tot,c)]; tl+=len(lines)
    print(f"{p.replace(T3,'T3/')}\t{len(b)}\t{len(raw)}\t{len(lines)}\t{kind}\t{'yes' if ok else 'NO'}\t" + "\t".join(map(str,c)))
print(f"kinds: {dict(kinds)}; decompress failures: {bad}; junit documents: {junit}; junit documents with a hostname attribute: {junit_with_attr}")
print(f"TOTAL lines {tl}\t" + "\t".join(f"{k}={v}" for k,v in zip(pats,tot)))
