#!/usr/bin/env python3
import csv
import hashlib
import json
import subprocess
from pathlib import Path

repo = Path(__file__).resolve().parents[4]
run = Path(__file__).resolve().parent
base = repo / "execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
origin = subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=repo, text=True).strip()
assert head == origin == "88e7590d3664d4f1daf91bed2a8899bda0748b92"
subprocess.run(["git", "merge-base", "--is-ancestor", "d7acbbff8d2bdb4913a8e7727f9f8cbc8787d943", head], cwd=repo, check=True)

manifest = base / "decision_support/PACKAGE_MANIFEST.sha256"
assert sha(manifest) == "623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d"
for line in manifest.read_text(encoding="utf-8").splitlines():
    expected, relative = line.split("  ", 1)
    assert sha(base / relative) == expected

with (base / "decision_support/OWNER_SELECTION_MATRIX.csv").open(newline="", encoding="utf-8") as f:
    matrix = list(csv.DictReader(f))
assert len(matrix) == 27
expected_rows = [f"D{i}" for i in range(1, 10)] + [f"TBD-{i:03d}" for i in range(1, 17)] + ["CENSUS", "COMPAT-DELTA"]
assert [row["row_id"] for row in matrix] == expected_rows
for row in matrix:
    options = row["options"].split("|")
    assert len(options) == 2
    option_ids = [item.split(":", 1)[0] for item in options]
    assert row["recommendation"].split(" ", 1)[0] in option_ids

tm121 = json.loads((run / "TM121_SELECTION_FORM.json").read_text(encoding="utf-8"))
recommended = dict(tm121["recommended_selections"])
assert list(recommended) == expected_rows
assert len(recommended) == 27
for row in matrix:
    assert recommended[row["row_id"]] == row["recommendation"].split(" ", 1)[0]
tuple_value = tuple(recommended[key] for key in ["TBD-005", "TBD-011", "TBD-013", "CENSUS"])
assert list(tuple_value) in tm121["allowed_census_tuples"]
assert len(tm121["allowed_census_tuples"]) == 4
assert tm121["validation_order"] == ["27_exact_option_ids", "allowed_census_tuple", "package_sha256", "human_signer_and_date"]

for name, expected_id, expected_options in [
    ("TM121_SELECTION_FORM.json", "TM-ROOT-121", None),
    ("TM105_SELECTION_FORM.json", "TM-ROOT-105", ["TM105-A", "TM105-B", "TM105-C"]),
    ("TM109_SELECTION_FORM.json", "TM-ROOT-109", ["TM109-A", "TM109-B", "TM109-C"]),
]:
    data = json.loads((run / name).read_text(encoding="utf-8"))
    assert data["decision_id"] == expected_id
    assert data["authority_status"] == "NON_AUTHORITATIVE_UNSIGNED_TEMPLATE"
    assert data["owner_fields"] == {"accountable_human_name": None, "date": None}
    if expected_options is not None:
        assert data["allowed_options"] == expected_options
        assert sorted(data["copy_paste_templates"]) == expected_options
    for text in data["copy_paste_templates"].values():
        assert "<ACCOUNTABLE_HUMAN_NAME>" in text and "<YYYY-MM-DD>" in text

with (run / "N3_BASIS_MANIFEST.csv").open(newline="", encoding="utf-8") as f:
    basis = list(csv.DictReader(f))
assert len(basis) == 22
for row in basis:
    if not row["path"].startswith("git:"):
        assert sha(repo / row["path"]) == row["sha256"], row["id"]

packet = (run / "OWNER_DECISION_PACKET.md").read_text(encoding="utf-8")
accept = tm121["copy_paste_templates"]["ACCEPT_RECOMMENDED"]
assert accept in packet
assert packet.count("<ACCOUNTABLE_HUMAN_NAME>") >= 9
assert "Status: `NON-AUTHORITATIVE / UNSIGNED DECISION PREPARATION`" in packet
print("N3_PACKET_VALIDATION_PASS rows=27 options=54 census_tuples=4 forms=3 basis=22 signer_fields=null")

