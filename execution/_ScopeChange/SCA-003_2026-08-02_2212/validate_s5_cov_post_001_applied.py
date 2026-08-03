#!/usr/bin/env python3
"""Validate exact S5 application of the COV-POST-001 correction."""

from __future__ import annotations

import difflib
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02"
LIVE = ROOT / "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
CANDIDATE = SNAPSHOT / "COV_POST_001_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
PREAPPLY = SNAPSHOT / "Basis_Reconciliation_Candidate/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md"
ACCEPTED_DIFF = SNAPSHOT / "COV_POST_001_Exact_Amendment.diff"

PATHS = {
    "launch_brief": RUN / "instances/S5-SCOPE-CORRECTION-APPLY/LAUNCH_BRIEF.md",
    "owner_ruling": RUN / "OWNER_RULING_2026-08-03_COV_POST_001_ACCEPT_APPLY.md",
    "live": LIVE,
    "candidate": CANDIDATE,
    "preapply": PREAPPLY,
    "accepted_diff": ACCEPTED_DIFF,
    "s4_validation": SNAPSHOT / "COV_POST_001_Validation.json",
    "s4_return": RUN / "instances/S4-SCOPE-CORRECTION/RETURN.md",
    "prd": ROOT / "docs/PRD_ROOT.md",
    "latest": ROOT / "execution/_ScopeChange/_LATEST.md",
    "scope_ledger": ROOT / "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv",
    "deliverable_register": ROOT / "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv",
}
EXPECTED = {
    "launch_brief": "4fa9b7ef81509dda32313787cd80778e8ca64910ee6f6b0e8982f05615928a7e",
    "owner_ruling": "8a9c005aa219d6e19f58e164721368ad72418019960182379edf52d5327a9851",
    "live": "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    "candidate": "23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d",
    "preapply": "69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c",
    "accepted_diff": "205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e",
    "s4_validation": "feccaf181660b6bf06f4a92066108ff3678553e1bbca5d28c794bfda81b174af",
    "s4_return": "8ba4c4f194ec2276021af8a49e087ff7bc009386e8802580409946ca0a4ca947",
    "prd": "d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4",
    "latest": "b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1",
    "scope_ledger": "3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2",
    "deliverable_register": "a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395",
}
OWNER_EVIDENCE = "12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129"
APPLIED_EVIDENCE = "f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8"
DECISION_PATH = "execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ids(value: str) -> set[str]:
    return set(re.findall(r"\b(?:PKG-[0-9]{2}|DEL-[0-9]{2}-[0-9]{2}|SOW-[0-9]{3}|OBJ-[0-9]{3})\b", value))


actual = {name: sha256(path) for name, path in PATHS.items()}
checks: list[dict[str, str]] = []


def check(name: str, passed: bool, evidence: str) -> None:
    checks.append({"name": name, "result": "PASS" if passed else "FAIL", "evidence": evidence})


for name in PATHS:
    check(f"sha256:{name}", actual[name] == EXPECTED[name], f"expected={EXPECTED[name]}; actual={actual[name]}")

live_bytes = LIVE.read_bytes()
candidate_bytes = CANDIDATE.read_bytes()
pre = PREAPPLY.read_text(encoding="utf-8")
live = LIVE.read_text(encoding="utf-8")
check("application:byte_parity", live_bytes == candidate_bytes, "live equals accepted candidate")

reproduced_diff = "".join(
    difflib.unified_diff(
        pre.splitlines(keepends=True),
        live.splitlines(keepends=True),
        fromfile="a/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
        tofile="b/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
        n=0,
        lineterm="\n",
    )
)
check("application:accepted_diff_reproduced", reproduced_diff.encode() == ACCEPTED_DIFF.read_bytes(), sha256(ACCEPTED_DIFF))
check("application:three_hunks", reproduced_diff.count("\n@@ ") + reproduced_diff.startswith("@@ ") == 3, "three unified-diff hunks")

changed_text = "\n".join(line[1:] for line in reproduced_diff.splitlines() if line.startswith("+") and not line.startswith("+++"))
check(
    "future_truth:wording",
    not re.search(r"\b(?:pending|confirmed)\b", changed_text, re.IGNORECASE)
    and OWNER_EVIDENCE in changed_text
    and APPLIED_EVIDENCE in changed_text
    and DECISION_PATH in changed_text,
    "changed passages contain completed-act evidence and Decision_Log pointer without pending/confirmed",
)
check("semantic_inventory:identifiers", ids(pre) == ids(live) and len(ids(live)) == 89, "89 identifiers preserved")
pre_dec023 = next(line for line in pre.splitlines() if "| DEC-023 |" in line)
live_dec023 = next(line for line in live.splitlines() if "| DEC-023 |" in line)
check("history:dec023", pre_dec023 == live_dec023, "DEC-023 byte-preserved")
check("shape:decision_rows", pre.count("| DEC-") == live.count("| DEC-"), "decision-row count unchanged")

failures = [entry for entry in checks if entry["result"] != "PASS"]
report = {
    "schema_version": "1.0",
    "run_id": "ROOT_FOUR_LANES_2026-08-02",
    "node": "S5",
    "finding": "COV-POST-001",
    "status": "PASS" if not failures else "FAIL",
    "checks_total": len(checks),
    "checks_passed": len(checks) - len(failures),
    "checks_failed": len(failures),
    "hashes": actual,
    "checks": checks,
}
(SNAPSHOT / "S5_Applied_Validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

applied = {
    "schema_version": "1.0",
    "run_id": "ROOT_FOUR_LANES_2026-08-02",
    "node": "S5",
    "finding": "COV-POST-001",
    "application_state": "APPLIED_PENDING_HUMAN_CONFIRMATION",
    "authority_sha256": actual["owner_ruling"],
    "path": "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md",
    "before_sha256": actual["preapply"],
    "approved_candidate_sha256": actual["candidate"],
    "applied_sha256": actual["live"],
    "exact_candidate_match": live_bytes == candidate_bytes,
    "preserved": {
        "docs/PRD_ROOT.md": actual["prd"],
        "execution/_ScopeChange/_LATEST.md": actual["latest"],
        "execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv": actual["scope_ledger"],
        "execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv": actual["deliverable_register"],
    },
}
(SNAPSHOT / "S5_Applied_File_Hashes.json").write_text(json.dumps(applied, indent=2) + "\n", encoding="utf-8")

print(json.dumps({"status": report["status"], "checks": len(checks), "failures": len(failures)}))
raise SystemExit(1 if failures else 0)
