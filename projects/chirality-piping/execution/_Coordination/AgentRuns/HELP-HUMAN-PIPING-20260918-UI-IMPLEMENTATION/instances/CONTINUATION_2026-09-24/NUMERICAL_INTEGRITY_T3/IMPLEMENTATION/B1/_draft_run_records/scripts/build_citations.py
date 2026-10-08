#!/usr/bin/env python3
"""I108 (B1 SK): build PR-B1's citations.json from check_citations.py's --suggest output.

Usage (VENV python, from anywhere):
  build_citations.py <suggest.json> <list.txt> <out citations.json> <package dir> <T6S citations.json>

- <suggest.json> is check_citations.py --suggest over 3d73db745e..d07006c2f0 with an empty index.
- <list.txt> is the same run's --list output, used for each token's cited_at sites.
- The one TODO entry (the generator class) is resolved here by hand, with its reason.
- The documents table is #1082's 23 names, read unchanged from T6S's index (equal to F2A_D1's).
Standard library only; reads only its arguments; writes only <out>.
"""
import hashlib, json, os, sys

sug_path, list_path, out_path, pkg, t6s_path = sys.argv[1:6]
P = "projects/chirality-piping/"
NUM = "75cd6be76bd6407fc24e0f1da834c2135407b69e"

sites = {}
for line in open(list_path, encoding="utf-8"):
    if not line.startswith("  ") or "\t" not in line:
        continue
    parts = line.strip("\n").lstrip().split("\t")
    if len(parts) < 3 or parts[1] == "document":
        continue
    where, cls, tok = parts[0], parts[1], parts[2]
    f, _, ln = where.rpartition(":")
    sites.setdefault((cls, tok), []).append(f"{f[len(P):] if f.startswith(P) else f}:{ln}")

HAND = {
    ("generator", "R/I86/b1_w_probe_01/_run_records/gen_inputs.py"): {
        "num_paths": ["I86/b1_w_probe_01/_run_records/gen_inputs.py"],
        "note": "I86's SW input generator (RR \"I86's SW probe accepted; …\"); b1_sq_inputs.rs pins its outputs by the "
                "input hashes I86 recorded. The same token is also a record_path citation",
    },
}

copies = {}
for name, num_path in (("QUAL_B1.md", "I104/b1_sq_01/QUAL_B1.md"),
                       ("RSS_TIME.md", "I104/b1_sq_01/RSS_TIME.md"),
                       ("registration.diff", "I104/b1_sq_01/registration.diff")):
    data = open(os.path.join(pkg, "copies", name), "rb").read()
    copies[f"copies/{name}"] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "num_path": num_path}

cits = []
for e in json.load(open(sug_path, encoding="utf-8")):
    key = (e["class"], e["token"])
    e.pop("first_seen", None)
    if "TODO" in e:
        e.pop("TODO")
        e.update(HAND[key])
    if key == ("record_path", "R/I104/b1_sq_01/QUAL_B1.md"):
        e["copy"] = "copies/QUAL_B1.md"
        e["sha256"] = copies["copies/QUAL_B1.md"]["sha256"]
    e["cited_at"] = sites.get(key, [])
    cits.append(e)

missing = [k for k in HAND if k not in {(c["class"], c["token"]) for c in cits}]
if missing:
    sys.exit(f"hand entries not suggested: {missing}")

idx = {
    "schema": "u9-citation-index-v1",
    "about": ("Resolves every record and RR citation that PR-B1 adds to maintained source: the 33 files of "
              "3d73db745e..d07006c2f0, equal to NUM 75cd6be76b outside the execution records. Records stay on the "
              "integration branch, pinned at num_commit (NUM's head when written, pushed; it carries RR \"I108's package "
              "returned; …\"). Verify with main's IMPLEMENTATION/F2A_D1/check_citations.py (#1082's tool, unchanged), "
              "--index this file. The documents table is #1082's 23 names, unchanged, as S-I1, U8 and T6S carry it. "
              "cited_at paths are relative to projects/chirality-piping/ at source_basis; num_path is relative to "
              "records_root at num_commit; heading_line is a line of rr_path at num_commit. No named_references are kept: "
              "the package cites its other sources in CHANGE_RECORD.md."),
    "num_branch": "codex/piping-numerical-integrity-20260926",
    "num_commit": NUM,
    "github": "https://github.com/sgttomas/chirality",
    "records_root": "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30",
    "rr_path": "projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/ROOT_RULINGS_V1.md",
    "source_basis": "d07006c2f001be5565646d6f1cf046e6dc96006c",
    "source_base": "3d73db745edd3378e0bb254a1b263215ef0861e9",
    "copies": copies,
    "citations": cits,
    "documents": json.load(open(t6s_path, encoding="utf-8"))["documents"],
    "code_anchors": [],
    "named_references": [],
}
with open(out_path, "w", encoding="utf-8") as w:
    json.dump(idx, w, indent=1, ensure_ascii=False)
    w.write("\n")
print(f"{len(cits)} citations, {len(copies)} copies -> {out_path}")
