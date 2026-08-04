#!/usr/bin/env python3
"""Validate the published TM-ROOT-112 implementation carrier identity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


RUN_ROOT = Path(__file__).resolve().parent
REPO_ROOT = RUN_ROOT.parents[3]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


identity = json.loads((RUN_ROOT / "CARRIER_IDENTITY.json").read_text(encoding="utf-8"))
assert identity["schemaVersion"] == "chirality.tm112-implementation-carrier/v1"
assert identity["runId"] == "ROOT_TM112_IMPLEMENT_2026-08-03"

brief = identity["implementationBrief"]
assert brief["preNormalizationAuthoringExecutionSha256"] == (
    "b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218"
)
assert brief["whitespaceNormalizedPublishedSha256"] == (
    "617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d"
)
assert sha256(REPO_ROOT / brief["path"]) == brief["whitespaceNormalizedPublishedSha256"]

for relative, expected in identity["finalProducts"].items():
    assert sha256(REPO_ROOT / relative) == expected, relative

evidence = identity["terminalEvidence"]
evidence_paths = {
    "i1bManagerRecoveredNormalizedSha256": (
        "instances/I1B-IMPLEMENTER/MANAGER_RECOVERED_RETURN.md"
    ),
    "i2ManagerRecoveredRefutationNormalizedSha256": (
        "instances/I2-FRESH-REFUTER/MANAGER_RECOVERED_REFUTATION.md"
    ),
    "i3ReturnSha256": "instances/I3-BOUNDED-REMEDIATION/RETURN.md",
    "i4BackcheckNormalizedPublishedSha256": (
        "instances/I4-FRESH-BACKCHECK/BACKCHECK.md"
    ),
    "i4ReturnSha256": "instances/I4-FRESH-BACKCHECK/RETURN.md",
}
for key, relative in evidence_paths.items():
    assert sha256(RUN_ROOT / relative) == evidence[key], relative

manifest_lines = (RUN_ROOT / "FINAL_PRODUCT_HASHES.sha256").read_text(
    encoding="utf-8"
).splitlines()
assert len(manifest_lines) == 3
assert all(line and not line.endswith((" ", "\t")) for line in manifest_lines)

required_publication_records = [
    "ORCHESTRATION_PLAN.md",
    "VALIDATION.md",
    "MANAGER_RETURN.md",
    "HANDOFF_STATE.md",
    "OWNER_IMPLEMENTATION_ACCEPTANCE_PACKET.md",
    "FORMAT_NORMALIZATION.md",
]
for relative in required_publication_records:
    text = (RUN_ROOT / relative).read_text(encoding="utf-8")
    assert brief["preNormalizationAuthoringExecutionSha256"] in text, relative
    assert brief["whitespaceNormalizedPublishedSha256"] in text, relative

print("PASS: TM-ROOT-112 implementation carrier identity and manifests validate")
