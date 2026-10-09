#!/usr/bin/env python3
"""I110 round 6: write the U3 package's citations.json (PR_N's form). Usage: make_citations.py <num_commit> <source_basis> <out>"""
import json, sys
num, basis, out = sys.argv[1:4]
pr_n = json.load(open("NUM/projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/IMPLEMENTATION/PR_N/citations.json"))
d = {
 "schema": "u9-citation-index-v1",
 "about": ("Resolves every record and RR citation that the U3 PR adds to maintained source: the 133 maintained files of "
           "7eae707bb7..source_basis (the product head; the package commit adds only this package). The scan finds no record, review, run, RR or "
           "design-document citation and no code-line citation. It finds one token of the generator class, which is not a citation: a "
           "maintained file path that the demo recipe's generation record lists in its source inventory (below). Verify with main's "
           "IMPLEMENTATION/F2A_D1/check_citations.py (#1082's tool, unchanged), --index this file. The documents table is #1082's 23 names, "
           "unchanged, as PR-N carries it. cited_at paths are relative to projects/chirality-piping/ at source_basis; num_path is relative to "
           "records_root at num_commit. No copies and no named_references: the package cites its other sources in CHANGE_RECORD.md."),
 "num_branch": pr_n["num_branch"],
 "num_commit": num,
 "github": pr_n["github"],
 "records_root": pr_n["records_root"],
 "rr_path": pr_n["rr_path"],
 "source_basis": basis,
 "source_base": "7eae707bb77722a69b61678c149aa816976bc162",
 "copies": {},
 "citations": [
  {
   "class": "generator",
   "token": "core/units/_run_records/TASK_RUN_2026-06-12_0136.md",
   "num_paths": [],
   "note": ("Not a record citation. The demo recipe's generation record (demo_fixture_generation.json, source_input_files and "
            "source_input_files_after) lists every file of the generator's local dependency closure with its sha256; this is one of them, "
            "a maintained file under projects/chirality-piping/core/units at main 7eae707bb7 and at source_basis. Nothing to resolve at NUM."),
   "cited_at": [
    "fixtures/product_preview/demo_fixture_generation.json:358",
    "fixtures/product_preview/demo_fixture_generation.json:762"
   ]
  }
 ],
 "documents": pr_n["documents"],
 "code_anchors": [],
 "named_references": []
}
open(out, "w").write(json.dumps(d, indent=1) + "\n")
