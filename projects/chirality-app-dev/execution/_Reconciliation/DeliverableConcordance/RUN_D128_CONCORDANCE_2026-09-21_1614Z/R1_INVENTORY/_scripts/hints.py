#!/usr/bin/env python3
"""HINTS/<DEL-ID>.csv: mechanical identifier -> location pointers (not evidence).

--out is the HINTS directory. For each CLAIM_INDEX unit the block text is:
CLM / labelled SEC: SoW lines from SourceLine to the next `### ` or `## ` heading;
unlabelled (whole-section) SEC: to the next `## ` heading; REM/REMTXT: the Remaining item
(same parser as REMAINING_INVENTORY). Tokens (deduplicated, sorted):
  backticked spans (len >= 3); CamelCase/lowerCamel identifiers (>= 6 chars, >= 1 internal
  capital); file-like tokens containing `/` or ending in a code/doc extension;
  SOW-nnn, [DEL-xx-yy-]REQ-nnn, K-XXX-n IDs.
Each token is searched fixed-string, case-sensitive, line by line across the IMPLEMENTATION_SURFACES
file set plus all text files under frontend/src/__tests__ and runtime tests (files sorted by repo
path, lines ascending); at most 5 hits per token and 40 per unit (tokens taken in sorted order).
A unit with no hits gets one row with empty Token/HitPath/HitLine so every unit is present.
"""
import argparse, os, re
import r1_common as C

BACKTICK = re.compile(r"`([^`\n]+)`")
CAMEL = re.compile(r"(?<![\w$])(?:[A-Z][a-z0-9]+(?:[A-Z][A-Za-z0-9]*)+|[a-z][a-z0-9]*(?:[A-Z][A-Za-z0-9]*)+)(?![\w$])")
FILELIKE = re.compile(r"[\w@.\-]+(?:/[\w@.\-*]+)+/?|[\w@.\-]+\.(?:tsx?|mjs|cjs|jsx?|json|jsonl|css|md|py|sh|ya?ml|csv|html)\b")
IDS = re.compile(r"\bSOW-\d+\b|\b(?:DEL-\d{2}-\d{2}-)?REQ-\d+\b|\bK-[A-Z]+(?:-[A-Z0-9]+)*-\d+\b|\bK-[A-Z]+-\d+\b")
PER_TOKEN, PER_UNIT = 5, 40


def tokens(text):
    s = set()
    for t in BACKTICK.findall(text):
        t = t.strip()
        if len(t) >= 3:
            s.add(t)
    for t in CAMEL.findall(text):
        if len(t) >= 6:
            s.add(t)
    for t in FILELIKE.findall(text):
        t = t.strip(".")
        if len(t) >= 3 and ("/" in t or "." in t):
            s.add(t)
    for t in IDS.findall(text):
        s.add(t)
    return sorted(s)


def sow_block(lines, start, labelled):
    out = [lines[start - 1]]
    for l in lines[start:]:
        if l.startswith("## ") or (labelled and l.startswith("### ")):
            break
        out.append(l)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--claim-index", default=None)
    a = ap.parse_args()
    root = a.frozen_root
    claims = C.load_claim_index(a.claim_index)
    dirs = C.deliverable_dirs(root)
    rem = {u["ClaimKey"]: u for u in C.remaining_units(root, claims)}
    impl, _ = C.implementation_files(root)
    corpus_paths = sorted(set([p for _, p in impl] + C.test_root_text_files(root)), key=lambda p: C.rel(root, p))
    corpus = [(C.rel(root, p), C.read_text(p).split("\n")) for p in corpus_paths]
    blobs = [(r, "\n".join(ls)) for r, ls in corpus]
    line_cache = {}
    hit_cache = {}

    def hits(tok):
        if tok in hit_cache:
            return hit_cache[tok]
        res = []
        for (r, blob), (_, ls) in zip(blobs, corpus):
            if tok not in blob:
                continue
            for i, l in enumerate(ls, 1):
                if tok in l:
                    res.append((r, i))
                    if len(res) >= PER_TOKEN:
                        break
            if len(res) >= PER_TOKEN:
                break
        hit_cache[tok] = res
        return res

    per_del = {d: [] for d in dirs}
    for c in claims:
        d = dirs[c["DeliverableID"]]
        if c["UnitKind"] in ("REM", "REMTXT"):
            text = rem[c["ClaimKey"]]["ItemText"]
        else:
            if d not in line_cache:
                line_cache[d] = C.read_text(os.path.join(d, "ScopeOfWork.md")).split("\n")
            labelled = c["UnitKind"] == "CLM" or bool(c["Label"])
            text = sow_block(line_cache[d], int(c["SourceLine"]), labelled)
        rows = []
        for tok in tokens(text):
            for r, i in hits(tok):
                if len(rows) >= PER_UNIT:
                    break
                rows.append([c["ClaimKey"], tok, r, i])
            if len(rows) >= PER_UNIT:
                break
        if not rows:
            rows = [[c["ClaimKey"], "", "", ""]]
        per_del[c["DeliverableID"]].extend(rows)
    os.makedirs(a.out, exist_ok=True)
    total = 0
    for del_id, rows in sorted(per_del.items()):
        C.write_csv(os.path.join(a.out, f"{del_id}.csv"), ["ClaimKey", "Token", "HitPath", "HitLine"], rows)
        total += len(rows)
    nohit = sum(1 for rows in per_del.values() for r in rows if not r[1])
    print(len(per_del), "files;", total, "rows;", nohit, "units without hits;", len(hit_cache), "distinct tokens")


if __name__ == "__main__":
    main()
