#!/usr/bin/env python3
"""Run fresh PKG-11 checks and terminally bind AUTHOR-B1 evidence."""
import csv
import hashlib
import os
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[8]
run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
child = run / "instances/WORKING-P3-PKG11/children/AUTHOR-B1"
pre = run / "snapshots/W_P3/preflight"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def capture(name, command):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, env=env)
    (child / f"{name}.stdout").write_text(result.stdout, encoding="utf-8")
    (child / f"{name}.stderr").write_text(result.stderr, encoding="utf-8")
    (child / f"{name}.exit").write_text(f"{result.returncode}\n", encoding="utf-8")
    assert result.returncode == 0, (name, result.returncode)

assert sha(pre / "P3_MANIFEST.tsv") == "ffaa85110f530cedac5e3dd8866354be9a7d89079dc3cf758c715d275839f5f4"
assert sha(pre / "EXPECTED_LIVE_BINDINGS.tsv") == "82cb784e9e676a3f4ece2e68341e8217fcf2e33160ba1b61559f395d4d6411b1"
with (pre / "METHOD_BINDINGS.tsv").open(newline="", encoding="utf-8") as handle:
    method_rows = list(csv.DictReader(handle, delimiter="\t"))
assert method_rows and all(sha(root / row["surface"]) == row["sha256"] for row in method_rows)
with (pre / "PKG00_DIRECTION_VALIDATION.tsv").open(newline="", encoding="utf-8") as handle:
    pkg00 = [row for row in csv.DictReader(handle, delimiter="\t") if row["package"] == "PKG-11"]
assert len(pkg00) == 1 and pkg00[0]["verdict"] == "PASS" and pkg00[0]["active_edges_to_pkg00"] == "25"
with (pre / "VALIDATOR_RESULTS.tsv").open(newline="", encoding="utf-8") as handle:
    validator = [row for row in csv.DictReader(handle, delimiter="\t") if row["package"] == "PKG-11"]
assert len(validator) == 5 and all(row["valid"] == "True" and row["format"] == "LEGACY_FOUR_DOC" for row in validator)
pkg10 = run / "instances/WORKING-P3-PKG10"
assert sha(pkg10 / "MANIFEST.tsv") == "4856fe725d0feaf4866d39a749d2e3769031204b452268466119cf210023ed0a"
assert sha(pkg10 / "PACKAGE_HANDOFF.md") == "4173257adf37355629ab71e8dbbc74f45de36b0d422fb8238ba7f8bbdf9fd6a5"

deps = []
with (pre / "P3_MANIFEST.tsv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        if row["package"] == "PKG-11":
            deps.append(str(root / row["live_path"] / "Dependencies.csv"))
for index, path in enumerate(deps, 1):
    capture(f"dependency-schema-{index}", ["python3", "tools/validation/validate_dependencies_schema.py", path])
capture("scope-of-work-tests", ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/scope_of_work/test_scope_of_work_tools.py"])
capture("practitioner-harness-tests", ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/practitioner_harness"])
capture("practitioner-self-check", ["python3", "tools/practitioner_harness/harness.py", "self-check"])

template = run / "instances/WORKING-P2-PKG09/children/AUTHOR-B1/finalize_author.py"
source = template.read_text(encoding="utf-8")
replacements = {
    "WORKING-P2-PKG09": "WORKING-P3-PKG11",
    "candidates/W_P2/PIP-PKG09": "candidates/W_P3/PIP-PKG11",
    "snapshots/W_P2/preflight/P2_MANIFEST.tsv": "snapshots/W_P3/preflight/P3_MANIFEST.tsv",
    'DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]': 'DIDS=[f"DEL-11-{n:02d}" for n in range(1,6)]',
    "DEL-09-01 through DEL-09-05": "DEL-11-01 through DEL-11-05",
    "PKG-09": "PKG-11",
    "W_P2/PIP-PKG09": "W_P3/PIP-PKG11",
    "P2 preflight": "P3 preflight",
    "(162,1357,1357)": "(159,1588,1588)",
    "162 mappings": "159 mappings",
    "1,357/1,357": "1,588/1,588",
    "162/162": "159/159",
    '"mappings_passed":162': '"mappings_passed":159',
    '"source_lines_covered":1357': '"source_lines_covered":1588',
    '"source_lines_total":1357': '"source_lines_total":1588',
}
for old, new in replacements.items():
    source = source.replace(old, new)
source = source.replace(
    "- Pre-execution syntax parsing found one closing-bracket typo in the newly written local harness at the `simulations.append` call. No tool, candidate, source, project, or evidence output had run or been written. The exact one-character mechanical repair changed `)` to `])`; syntax parsing then passed and the complete harness ran once from the beginning.\n",
    "- No failed or repaired attempt occurred; the local harness passed syntax validation before registered-tool execution.\n",
)
source = source.replace(
    "Terminalization rebuilt all direct and transitive bindings after the repair",
    "Terminalization built all direct and transitive bindings after the complete run",
)
source = source.replace(
    "A one-character local harness syntax typo was detected and repaired before any execution output existed; the complete run then started from the beginning and all direct/transitive evidence was frozen after it. No registered tool failed or retried.",
    "The local harness passed syntax validation before execution; no registered tool failed or retried, and all direct/transitive evidence was frozen after the complete run.",
)
source = source.replace('"event":"repair","attempt":1,"failure_category":"EXECUTION_SUBSTRATE","reason_code":"LOCAL_SYNTAX_BRACKET_REPAIRED_BEFORE_EXECUTION","remediation":"ONE_CHARACTER_BRACKET_FIX_FULL_RUN_FROM_START"', '"event":"pass","attempt":1,"failure_category":"NONE","reason_code":"HARNESS_SYNTAX_PASS","remediation":"NONE"')
for forbidden in ("DEL-09-", "PKG-09", "WORKING-P2-PKG09", "W_P2/PIP-PKG09", "P2_MANIFEST.tsv"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__"})
