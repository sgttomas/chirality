#!/usr/bin/env python3
"""Read-only D-APP-132 derivative/hash/backcheck; run from any directory."""
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "AGENTS.md").is_file() and (p / "projects/chirality-app-dev").is_dir())
APP = ROOT / "projects/chirality-app-dev"

def digest(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()

def original(path, basis):
    return subprocess.check_output(["git", "show", f"{basis}:{path}"], cwd=ROOT)

def validate_rows(rows, expected, originals, original_fields):
    assert Counter(r["ClaimKey"] for r in rows) == Counter(expected), "key multiset mismatch"
    for row in rows:
        source = originals[row["ClaimKey"]]
        assert {k: row[k] for k in original_fields} == source, "original row changed"
        assert row["OriginalRowSHA256"] == digest(json.dumps(source, sort_keys=True, separators=(",", ":"))), "source row hash mismatch"
        assert row["CurrentWork"] and row["CurrentGate"] and row["CurrentOwner"], "missing current continuation"

def main():
    evidence = json.loads((HERE / "DISPOSITION_EVIDENCE.json").read_text())
    basis = evidence["basis"]
    for entry in evidence["authored_files"]:
        assert digest((ROOT / entry["path"]).read_bytes()) == entry["sha256"], entry["path"]
    for entry in evidence["sources"]:
        assert digest(original(entry["path"], basis)) == entry["basis_sha256"], entry["path"]
        if entry["must_remain_unchanged"]:
            assert digest((ROOT / entry["path"]).read_bytes()) == entry["basis_sha256"], entry["path"]
    rows = list(csv.DictReader((HERE / "CURRENT_RESIDUAL_DISPOSITIONS.csv").open(newline="")))
    originals = {}
    fields = None
    for source in sorted({r["OriginalResidualSource"] for r in rows}):
        for row in csv.DictReader((APP / source).open(newline="")):
            fields = list(row)
            originals[row["ClaimKey"]] = row
    expected = evidence["expected_overlay_keys"]
    validate_rows(rows, expected, originals, fields)
    negatives = []
    for name, changed in [("missing key", rows[:-1]), ("duplicate key", rows + [rows[0]]), ("changed original", [dict(rows[0], Gate="invented")]+rows[1:])]:
        try:
            validate_rows(changed, expected, originals, fields)
        except AssertionError:
            negatives.append(name)
        else:
            raise AssertionError(f"negative control did not fail: {name}")
    changes = json.loads((HERE / "P01_CLAIM_CHANGE_MANIFEST.json").read_text())
    old = original("projects/chirality-app-dev/" + changes["source"], basis).decode()
    now = (APP / changes["source"]).read_text()
    restored = now
    for c in changes["changes"]:
        assert digest(c["before"]) == c["before_sha256"] and digest(c["after"]) == c["after_sha256"]
        assert old.count(c["before"]) == 1 and restored.count(c["after"]) == 1
        restored = restored.replace(c["after"], c["before"], 1)
    assert restored == old, "SoW contains changes outside four manifested units"
    for entry in evidence["status_paths"]:
        before = original(entry, basis).decode(); after = (ROOT / entry).read_text()
        for field in ["Current State", "Authorization Basis", "Directive", "Checking Approval SHA"]:
            pattern = rf"^\*\*{field}:\*\*.*$"
            assert re.search(pattern, before, re.M).group() == re.search(pattern, after, re.M).group(), field
        assert before.split("## History\n",1)[1] in after, "old status history changed"
    bundle = "projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/R5_R6_FOLLOWUP_2026-09-22/APP_DECISION_BUNDLE.md"
    assert (ROOT/bundle).read_bytes().startswith(original(bundle,basis)), "historical proposal edited"
    graph_path=evidence["graph_path"]
    old_graph=json.loads(original(graph_path,basis)); new_graph=json.loads((ROOT/graph_path).read_text())
    old_graph.pop("current_continuation");new_graph.pop("current_continuation")
    assert old_graph==new_graph, "original graph nodes changed"
    prefix="projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/"
    assert not subprocess.check_output(["git","diff",basis,"--name-only","--",prefix],cwd=ROOT).strip(), "frozen R1-R6 changed"
    print(json.dumps({"result":"PASS","overlay_keys":len(rows),"owner_released_claims":2,"consequential_reference_units":2,"negative_controls":negatives,"lifecycle_and_original_history":"UNCHANGED","frozen_reconciliation":"UNCHANGED","product_test_claim":"NONE"},indent=2))

if __name__=="__main__":
    main()
