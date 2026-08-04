#!/usr/bin/env python3
"""Validate R1 ruling capture without applying any ruling effect."""

import hashlib
import json
import re
import subprocess
from pathlib import Path


repo = Path(__file__).resolve().parents[4]
run = Path(__file__).resolve().parent
transcript_path = run / "OWNER_RULING_TRANSCRIPT_2026-08-03.md"
text = transcript_path.read_text(encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().replace("/ ", "/")


assert text.count("<!-- VERBATIM_OWNER_RETURN_BEGIN -->") == 1
assert text.count("<!-- VERBATIM_OWNER_RETURN_END -->") == 1
block = text.split("<!-- VERBATIM_OWNER_RETURN_BEGIN -->", 1)[1].split(
    "<!-- VERBATIM_OWNER_RETURN_END -->", 1
)[0]
assert block.startswith("\n```text\n") and block.endswith("```\n")
verbatim = block[len("\n```text\n") : -len("```\n")]
canon = canonical(verbatim)

assert verbatim.count("DECIDE ROOT-TM112-STOP-CONTRACT-01 OPTION 1") == 1
assert verbatim.count("DECIDE DEL-02-06 OWNER-SELECTION") == 1
assert verbatim.count("RULE TM-ROOT-105 TM105-A") == 1
assert verbatim.count("RULE TM-ROOT-109 TM109-A") == 1
for number in range(1, 6):
    assert re.search(rf"^{number}\. ", verbatim, re.MULTILINE)
assert verbatim.count("Ryan Tufts 2026-08-03") == 4

# TM-ROOT-112 selects Option 1 and simultaneously holds the remaining human
# semantic subgate before implementation.
tm112_required = [
    "DECIDE ROOT-TM112-STOP-CONTRACT-01 OPTION 1",
    "SHUTDOWN CONTRACT SURFACE; runtime-daemon.ts",
    "BOUNDED daemon.test.ts CASES: IDLE, COMPLETED KEEP-ALIVE, INCOMPLETE ORDINARY REQUEST, LIVE SSE, BOUNDED TERMINATION, DISCONNECT/INTERRUPT, SOCKET AND OWNER CLEANUP, RESTART",
    "EXACT GRACE DURATION, STREAM-CANCELLATION OBLIGATIONS, AND FORCED RESIDUAL-CONNECTION BEHAVIOR RETURN TO ME AS HUMAN-SELECTED SEMANTICS BEFORE IMPLEMENTATION",
]
for required in tm112_required:
    assert canonical(required) in canon

# DEL-02-06 exact option/hash/signer/date validation in the mandatory order.
tm121 = json.loads((run / "TM121_SELECTION_FORM.json").read_text(encoding="utf-8"))
expected_del = tm121["copy_paste_templates"]["ACCEPT_RECOMMENDED"].replace(
    "<ACCOUNTABLE_HUMAN_NAME>", "Ryan Tufts"
).replace("<YYYY-MM-DD>", "2026-08-03")
assert canonical(expected_del) in canon
assert tm121["validation_order"] == [
    "27_exact_option_ids",
    "allowed_census_tuple",
    "package_sha256",
    "human_signer_and_date",
]
selections = dict(tm121["recommended_selections"])
assert len(selections) == 27
selected_tuple = [
    selections["TBD-005"],
    selections["TBD-011"],
    selections["TBD-013"],
    selections["CENSUS"],
]
assert selected_tuple in tm121["allowed_census_tuples"]
assert tm121["package_sha256"] == (
    "623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d"
)

base = repo / "execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001"
manifest = base / "decision_support/PACKAGE_MANIFEST.sha256"
assert sha(manifest) == tm121["package_sha256"]
for line in manifest.read_text(encoding="utf-8").splitlines():
    expected, relative = line.split("  ", 1)
    assert sha(base / relative) == expected

# TM105-A and TM109-A retain their preparation-only/local-meaning boundaries.
for form_name, option in [
    ("TM105_SELECTION_FORM.json", "TM105-A"),
    ("TM109_SELECTION_FORM.json", "TM109-A"),
]:
    form = json.loads((run / form_name).read_text(encoding="utf-8"))
    assert form["recommended_option"] == option
    expected = form["copy_paste_templates"][option].replace(
        "<ACCOUNTABLE_HUMAN_NAME>", "Ryan Tufts"
    ).replace("<YYYY-MM-DD>", "2026-08-03")
    assert canonical(expected) in canon

# Additions 1–5 and their exact effect boundaries.
addition_phrases = [
    "POST-RULING COORDINATION",
    "TM-PIP-032 trigger evaluates against the recorded rulings",
    "CLOSURE-NOTES PRECISION",
    "preparation-posture only with no contract bytes ruled",
    "DURABLE CARRIERS",
    "nothing hides in a closed row",
    "TM-ROOT-112 TRANCHE ROUTING",
    "when the tranche's contract semantics return for my acceptance and the accepted repair lands, route a notice to App",
    "PUBLICATION=AUTHORIZED",
    "commit this session's durable products (Receipt 91, HANDOFF_STATE repair, run package, ruling records) on its branch and open the PR through the normal gate. Merge remains mine.",
]
for phrase in addition_phrases:
    assert canonical(phrase) in canon

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
origin = subprocess.check_output(
    ["git", "rev-parse", "origin/main"], cwd=repo, text=True
).strip()
assert head == origin == "88e7590d3664d4f1daf91bed2a8899bda0748b92"

print(
    "RULING_CAPTURE_VALIDATION_PASS "
    f"verbatim_sha256={hashlib.sha256(verbatim.encode('utf-8')).hexdigest()} "
    f"record_sha256={sha(transcript_path)} returns=4 additions=5 "
    "tm112=OPTION_1_SEMANTICS_HELD tm121=27_OPTIONS_ALLOWED_TUPLE "
    "tm105=TM105-A_PREPARATION_ONLY tm109=TM109-A_PREPARATION_ONLY "
    "publication=LATER_COMMIT_PR_ONLY merge=HUMAN"
)
