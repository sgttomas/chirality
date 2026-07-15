#!/usr/bin/env python3
"""Fresh PKG10 checks and terminal binding using the accepted PKG09 shape."""
import csv
import hashlib
import os
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[8]
run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
child = run / "instances/WORKING-P3-PKG10/children/AUTHOR-B1"
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
    pkg00 = [row for row in csv.DictReader(handle, delimiter="\t") if row["package"] == "PKG-10"]
assert len(pkg00) == 1 and pkg00[0]["verdict"] == "PASS" and pkg00[0]["active_edges_to_pkg00"] == "28"
with (pre / "VALIDATOR_RESULTS.tsv").open(newline="", encoding="utf-8") as handle:
    validator = [row for row in csv.DictReader(handle, delimiter="\t") if row["package"] == "PKG-10"]
assert len(validator) == 5 and all(row["valid"] == "True" and row["format"] == "LEGACY_FOUR_DOC" for row in validator)

deps = []
with (pre / "P3_MANIFEST.tsv").open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle, delimiter="\t"):
        if row["package"] == "PKG-10":
            deps.append(str(root / row["live_path"] / "Dependencies.csv"))
for index, path in enumerate(deps, 1):
    capture(f"dependency-schema-{index}", ["python3", "tools/validation/validate_dependencies_schema.py", path])
capture("scope-of-work-tests", ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/scope_of_work/test_scope_of_work_tools.py"])
capture("practitioner-harness-tests", ["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/practitioner_harness"])
capture("practitioner-self-check", ["python3", "tools/practitioner_harness/harness.py", "self-check"])

template = run / "instances/WORKING-P2-PKG09/children/AUTHOR-B1/finalize_author.py"
source = template.read_text(encoding="utf-8")
replacements = {
    "WORKING-P2-PKG09": "WORKING-P3-PKG10",
    "candidates/W_P2/PIP-PKG09": "candidates/W_P3/PIP-PKG10",
    "snapshots/W_P2/preflight/P2_MANIFEST.tsv": "snapshots/W_P3/preflight/P3_MANIFEST.tsv",
    'DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]': 'DIDS=[f"DEL-10-{n:02d}" for n in range(1,6)]',
    "DEL-09-01 through DEL-09-05": "DEL-10-01 through DEL-10-05",
    "PKG-09": "PKG-10",
    "W_P2/PIP-PKG09": "W_P3/PIP-PKG10",
    "P2 preflight": "P3 preflight",
    "(162,1357,1357)": "(163,1594,1594)",
    "162 mappings": "163 mappings",
    "1,357/1,357": "1,594/1,594",
    "162/162": "163/163",
    '"mappings_passed":162': '"mappings_passed":163',
    '"source_lines_covered":1357': '"source_lines_covered":1594',
    '"source_lines_total":1357': '"source_lines_total":1594',
}
for old, new in replacements.items():
    source = source.replace(old, new)
source = source.replace(
    "A one-character local harness syntax typo was detected and repaired before any execution output existed;",
    "A helper-only pre-execution seed-substitution regex mismatch was detected and mechanically repaired before any registered tool or candidate output existed;",
)
source = source.replace(
    "Pre-execution syntax parsing found one closing-bracket typo in the newly written local harness at the `simulations.append` call. No tool, candidate, source, project, or evidence output had run or been written. The exact one-character mechanical repair changed `)` to `])`; syntax parsing then passed and the complete harness ran once from the beginning.",
    "Pre-execution attempt 1 stopped at a helper-only seed-substitution assertion because the adapted regex expected the dictionary closing brace on a separate line. No registered tool, candidate, live source, or member evidence output had run. Removing that extra newline assumption was a non-semantic local repair; the complete harness then ran from the beginning.",
)
source = source.replace("LOCAL_SYNTAX_BRACKET_REPAIRED_BEFORE_EXECUTION", "LOCAL_SEED_REGEX_REPAIRED_BEFORE_EXECUTION")
source = source.replace("ONE_CHARACTER_BRACKET_FIX_FULL_RUN_FROM_START", "REGEX_NEWLINE_ASSUMPTION_FIX_FULL_RUN_FROM_START")
for forbidden in ("DEL-09-", "PKG-09", "WORKING-P2-PKG09", "W_P2/PIP-PKG09", "P2_MANIFEST.tsv"):
    assert forbidden not in source, forbidden
compile(source, str(template), "exec")
exec(compile(source, str(template), "exec"), {"__name__": "__main__"})
