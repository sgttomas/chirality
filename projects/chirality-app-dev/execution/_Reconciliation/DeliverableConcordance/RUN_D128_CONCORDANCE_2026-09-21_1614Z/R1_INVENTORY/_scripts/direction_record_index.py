#!/usr/bin/env python3
"""DIRECTION_RECORD_INDEX.csv.

Sources: plans/chirality_app_v3_*; plans/steers/chirality_app_v3_*; App
execution/_ScopeChange/SCA-APP-00[89]*/**/*.md at depth <= 2 below the SCA folder; and, recursively,
files named HANDOFF* / OWNER* / *RULING* inside App AgentRuns folders APP_V3_*, APPDEV_V3_NODE_*,
CHIRALITY_V3_*. Kind = first matching filename rule in KIND_RULES (lower-cased basename), else OTHER.
Date = first YYYY-MM-DD or YYYYMMDD in the basename, else in the nearest ancestor directory name.
Title = first `# ` heading (.md), <title> (.html), else empty. SHA256 of file bytes.
"""
import argparse, glob, hashlib, os, re
import r1_common as C

KIND_RULES = [
    ("RULING_RECORD", r"ruling_record"), ("RULING_CANDIDATE", r"ruling_candidate"), ("RULING", r"ruling"),
    ("OWNER", r"^owner"), ("HANDOFF", r"handoff"), ("STEER", r"steer"), ("DIRECTION", r"direction"),
    ("REVIEW", r"review"), ("PLAN", r"plan"), ("NOTICE", r"notice"), ("BRIEF", r"brief"),
    ("AUDIT", r"audit"), ("CONCORDANCE", r"concordance"), ("DAG", r"^dag"), ("CARRIER_MAP", r"carrier_map"),
    ("IMPACT_ASSESSMENT", r"impact_assessment"), ("DECISION_LOG", r"decision_log"),
    ("RUN_SUMMARY", r"run_summary"), ("CLOSURE", r"closure"), ("POINTER", r"pointer|_latest"),
    ("AMENDMENT", r"amendment"), ("REVISION", r"revision"), ("TRANSACTION", r"transaction"),
    ("CANDIDATE", r"candidate"), ("RECONSTRUCTION", r"reconstruction"), ("RECORD", r"record"),
    ("INIT_TASK", r"init_task"), ("INPUTS", r"inputs"),
]


def kind(name):
    n = name.lower()
    for k, pat in KIND_RULES:
        if re.search(pat, n):
            return k
    return "OTHER"


def date_of(root, p):
    def find(s):
        m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", s) or re.search(r"(20\d{2})(\d{2})(\d{2})", s)
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else ""
    d = find(os.path.basename(p))
    q = os.path.dirname(p)
    while not d and len(q) > len(root):
        d = find(os.path.basename(q))
        q = os.path.dirname(q)
    return d


def title_of(p):
    t = C.read_text(p)
    if p.endswith(".md"):
        m = re.search(r"^#\s+(.*)$", t, re.M)
    elif p.endswith(".html"):
        m = re.search(r"<title>(.*?)</title>", t, re.S | re.I)
    else:
        m = None
    return " ".join(m.group(1).split()) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = a.frozen_root.rstrip("/")
    app = os.path.join(root, C.APP_REL)
    paths = set(p for p in glob.glob(os.path.join(root, "plans/chirality_app_v3_*")) if os.path.isfile(p))
    paths |= set(p for p in glob.glob(os.path.join(root, "plans/steers/chirality_app_v3_*")) if os.path.isfile(p))
    for sca in glob.glob(os.path.join(app, "execution/_ScopeChange/SCA-APP-00[89]*")):
        paths |= set(glob.glob(os.path.join(sca, "*.md"))) | set(glob.glob(os.path.join(sca, "*/*.md")))
    for pat in ("APP_V3_*", "APPDEV_V3_NODE_*", "CHIRALITY_V3_*"):
        for run in glob.glob(os.path.join(app, "execution/_Coordination/AgentRuns", pat)):
            for dp, dns, fns in os.walk(run):
                for fn in fns:
                    if fn.startswith(("HANDOFF", "OWNER")) or "RULING" in fn:
                        paths.add(os.path.join(dp, fn))
    rows = []
    for p in sorted(paths, key=lambda x: C.rel(root, x)):
        with open(p, "rb") as fh:
            sha = hashlib.sha256(fh.read()).hexdigest()
        rows.append([C.rel(root, p), kind(os.path.basename(p)), date_of(root, p), title_of(p), sha])
    C.write_csv(a.out, ["Path", "Kind", "Date", "Title", "SHA256"], rows)
    kinds = {}
    for r in rows:
        kinds[r[1]] = kinds.get(r[1], 0) + 1
    print(len(rows), "records", dict(sorted(kinds.items())))


if __name__ == "__main__":
    main()
