#!/usr/bin/env python3
"""Build a SHA-256 manifest from Git objects at the frozen review commit."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


REPO = Path("/Users/ryan/.codex/worktrees/d9d0/chirality")
OUT = REPO / "execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/FROZEN_BASIS_MANIFEST.json"
FREEZE = "da31c19b5656dd74615e308c4215688971d33dc9"
PRODUCT_BASIS = "aeadf5304435e1a4d8b4a26306da9ad4d4519eb6"
REQUEST_PATH = Path("/Users/ryan/.codex/attachments/39f41ce7-f8a2-4b48-9106-597afe60d6fb/pasted-text.txt")
CHARTER_PATH = "plans/chirality_program_architecture_and_tandem_review_2026-07-25.html"
CHARTER_SHA256 = "1756b84400f97d6daa42a6041807fb7ac62b80ac26e3488f7d92697031a9159f"


def run(*args: str, input_bytes: bytes | None = None) -> bytes:
    return subprocess.run(
        args,
        cwd=REPO,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    ).stdout


tree_raw = run("git", "ls-tree", "-r", "-z", "--full-tree", FREEZE)
tree: dict[str, tuple[str, str, str]] = {}
for record in tree_raw.split(b"\0"):
    if not record:
        continue
    meta, path_b = record.split(b"\t", 1)
    mode_b, kind_b, oid_b = meta.split(b" ", 2)
    tree[path_b.decode()] = (mode_b.decode(), kind_b.decode(), oid_b.decode())


EXACT: dict[str, str] = {}


def exact(category: str, *paths: str) -> None:
    for path in paths:
        EXACT[path] = category


exact(
    "charter",
    CHARTER_PATH,
)
exact(
    "root_authority",
    "docs/PRD_ROOT.md",
    "docs/DIRECTIVE.md",
    "docs/CONTRACT.md",
    "docs/SPEC.md",
    "docs/TYPES.md",
    "docs/PLAN.md",
    "execution/_Coordination/PRD_CANDIDATE_2026-07-25_root_product.md",
    "AGENTS.md",
    "skills/README.md",
    "tools/REGISTRY.md",
)
exact(
    "root_method_and_standards",
    "docs/WORKFLOW_COMPONENT_STANDARD.md",
    "docs/DECOMPOSITION_STANDARD.md",
    "docs/SOFTWARE_WORKFLOW_PROFILE.md",
    "docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md",
    "docs/CYCLE_DRIVEN_RESOLUTION.md",
    "tools/validation/validate_decomposition_registers.py",
)
exact(
    "root_current_state",
    "execution/_Coordination/LOOP_INIT.md",
    "execution/_Coordination/CURRENT_WORKPLAN.md",
    "execution/_Coordination/WORKPLAN_2026-07-25_root_initialization.md",
    "execution/_Coordination/LOOP_RECEIPTS.md",
    "execution/_Coordination/HANDOFF_STATE.md",
)
exact(
    "app_authority",
    "projects/chirality-app-dev/chirality.project.json",
    "projects/chirality-app-dev/AGENTS.md",
    "projects/chirality-app-dev/docs/DIRECTIVE.md",
    "projects/chirality-app-dev/docs/CONTRACT.md",
    "projects/chirality-app-dev/docs/SPEC.md",
    "projects/chirality-app-dev/docs/TYPES.md",
    "projects/chirality-app-dev/docs/PLAN.md",
    "projects/chirality-app-dev/docs/PRD.md",
    "projects/chirality-app-dev/docs/MANIFEST.json",
    "projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json",
)
exact(
    "app_current_state",
    "projects/chirality-app-dev/loop/LOOP_INIT.md",
    "projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md",
    "projects/chirality-app-dev/loop/LOOP_RECEIPTS.md",
    "projects/chirality-app-dev/execution/_Coordination/_LATEST.md",
    "projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAEMON_SERVICE_2026-07-25/HANDOFF_STATE.md",
)
exact(
    "app_runtime_seams",
    "projects/chirality-app-dev/frontend/src/lib/runtime-client/daemon-harness-port.ts",
    "projects/chirality-app-dev/frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts",
    "projects/chirality-app-dev/frontend/electron/runtime-host.ts",
    "projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md",
    "projects/chirality-app-dev/docs/harness/reliance_boundary_register.md",
)
exact(
    "pec_authority_and_state",
    "projects/pec/chirality.project.json",
    "projects/pec/AGENTS.md",
    "projects/pec/docs/PRD.md",
    "projects/pec/docs/STATUS.md",
    "projects/pec/execution/_Coordination/_COORDINATION.md",
    "projects/pec/execution/_Coordination/SCA-002_INTAKE_2026-07-25.md",
    "_DomainEngines/profiles/pec.yaml",
    "_DomainEngines/pec/LOOP_INIT.md",
    "_DomainEngines/pec/LOOP_RECEIPTS.md",
)
exact(
    "consulted_context",
    "domains/chirality/_Sources/Source_Manifest.csv",
    "domains/chirality-app-dev/_Sources/Source_Manifest.csv",
    "domains/chirality-piping/_Sources/Source_Manifest.csv",
    "domains/chirality-piping/_Sources/Source_Manifest.index.csv",
    "domains/chirality-piping/_Sources/SOURCE_BOUNDARY.md",
    "domains/piping-design/README.md",
)


APP_DECISIONS = {
    "38",
    "48",
    "49",
    "50",
    "53",
    "54",
    "55",
    "56",
    "57",
    "60",
    "61",
    "64",
    "65",
    "70",
    "71",
    "72",
    "73",
    "74",
}


def categories_for(path: str) -> set[str]:
    categories: set[str] = set()
    if path in EXACT:
        categories.add(EXACT[path])

    if path.startswith("_DomainEngines/_DECISIONS/"):
        categories.add("tier0_decisions")
    if path.startswith("docs/governance_harness/_DECISIONS/"):
        categories.add("root_decisions")
    if path.startswith("execution/_Decomposition/"):
        categories.add("root_decomposition")
    if path.startswith("execution/_harness/"):
        categories.add("root_guard_state")
    if path.startswith("runtime/"):
        categories.add("root_shared_runtime")
    if re.fullmatch(r"agents/AGENT_[^/]+\.md", path):
        categories.add("root_agent_contracts")
    if path.startswith("skills/scope-of-work/") or path.startswith("tools/scope_of_work/"):
        categories.add("shared_sow_method")
    if re.fullmatch(
        r"execution/PKG-0[1-6]_[^/]+/1_Working/DEL-[^/]+/(ScopeOfWork\.md|_STATUS\.md)",
        path,
    ):
        categories.add("root_live_sow")

    if path == "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md":
        categories.add("app_decomposition")
    if path.startswith(
        "projects/chirality-app-dev/execution/_Evaluation/DecompCoverage/COV_SCA_APP_004_POSTCHANGE_2026-07-23_2027/"
    ):
        categories.add("app_decomposition_coverage")
    if path.startswith(
        "projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-003_2026-07-22_Shared_Runtime_Local_Agent_Pilot/"
    ) or path.startswith(
        "projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/"
    ):
        categories.add("app_accepted_amendment_evidence")
    if re.fullmatch(
        r"projects/chirality-app-dev/execution/PKG-(?:00|0[1-9]|10)_[^/]+/1_Working/DEL-[^/]+/(ScopeOfWork\.md|_STATUS\.md|Dependencies\.csv)",
        path,
    ):
        categories.add("app_live_sow")
    app_decision_match = re.search(
        r"projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-(\d+)",
        path,
    )
    if path.endswith("projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md"):
        categories.add("app_decisions")
    if app_decision_match and app_decision_match.group(1) in APP_DECISIONS:
        categories.add("app_decisions")
    if path.startswith("projects/chirality-app-dev/execution/_Coordination/NOTICE_"):
        categories.add("app_root_doctrine_notices")

    if path.startswith("projects/pec/execution/_Decomposition/"):
        categories.add("pec_decomposition")
    if path.startswith(
        "projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/"
    ):
        categories.add("pec_decomposition_coverage")
    if path.startswith(
        "projects/pec/execution/_ScopeChange/SCA-001_2026-07-24_2206/"
    ) or path.startswith(
        "projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/"
    ):
        categories.add("pec_accepted_amendment_evidence")
    if re.fullmatch(
        r"projects/pec/execution/PKG-(?:00|0[1-9]|10)_[^/]+/1_Working/DEL-[^/]+/(ScopeOfWork\.md|_STATUS\.md|Dependencies\.csv)",
        path,
    ):
        categories.add("pec_live_sow_and_dependencies")
    pec_decision_match = re.search(
        r"projects/pec/execution/_Coordination/_DECISIONS/D-PEC-(\d+)",
        path,
    )
    if path.endswith("projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md"):
        categories.add("pec_decisions")
    if pec_decision_match and 57 <= int(pec_decision_match.group(1)) <= 66:
        categories.add("pec_decisions")
    if path.startswith("projects/pec/execution/_Coordination/NOTICE_"):
        categories.add("pec_root_doctrine_notices")

    if path.startswith("domains/chirality/_Coordination/NOTICE_"):
        categories.add("downstream_root_doctrine_notices")

    return categories


missing_exact = sorted(path for path in EXACT if path not in tree)
if missing_exact:
    raise SystemExit(f"Expected frozen paths missing: {missing_exact}")

entries = []
for path in sorted(tree):
    categories = categories_for(path)
    if not categories:
        continue
    mode, kind, oid = tree[path]
    if kind != "blob":
        raise SystemExit(f"Non-blob selected: {path} ({kind})")
    content = run("git", "cat-file", "blob", oid)
    entries.append(
        {
            "path": path,
            "mode": mode,
            "git_blob": oid,
            "sha256": hashlib.sha256(content).hexdigest(),
            "bytes": len(content),
            "categories": sorted(categories),
        }
    )

category_counts = Counter()
for entry in entries:
    category_counts.update(entry["categories"])

charter_entry = next(entry for entry in entries if entry["path"] == CHARTER_PATH)
if charter_entry["sha256"] != CHARTER_SHA256:
    raise SystemExit(
        f"Charter hash mismatch: {charter_entry['sha256']} != {CHARTER_SHA256}"
    )

diff_names = run("git", "diff", "--name-only", PRODUCT_BASIS, FREEZE, "--").decode().splitlines()
if diff_names != [CHARTER_PATH]:
    raise SystemExit(f"Unexpected product-basis-to-freeze diff: {diff_names}")

all_app_invariant_registers = sorted(
    path
    for path in tree
    if path.startswith("projects/chirality-app-dev/")
    and Path(path).name == "contract_invariant_coverage_register.csv"
)

declared_absence_checks = [
    {
        "description": "App required-or-deferred contract invariant coverage register",
        "query": "projects/chirality-app-dev/**/contract_invariant_coverage_register.csv",
        "matches": all_app_invariant_registers,
        "status": "ABSENT" if not all_app_invariant_registers else "PRESENT",
    },
    {
        "description": "Root missing ACTIVE-pinned agent files",
        "paths": [
            "agents/AGENT_CONTEXT_TRANSPOSE.md",
            "agents/AGENT_DECOMP_BASE.md",
            "agents/AGENT_ORCHESTRATOR.md",
            "agents/AGENT_SCHEDULING.md",
            "agents/AGENT_SKILLMAKER.md",
            "agents/AGENT_TOOLMAKER.md",
        ],
        "present": [
            path
            for path in [
                "agents/AGENT_CONTEXT_TRANSPOSE.md",
                "agents/AGENT_DECOMP_BASE.md",
                "agents/AGENT_ORCHESTRATOR.md",
                "agents/AGENT_SCHEDULING.md",
                "agents/AGENT_SKILLMAKER.md",
                "agents/AGENT_TOOLMAKER.md",
            ]
            if path in tree
        ],
        "status": "ALL_ABSENT",
    },
    {
        "description": "Root doctrine notices under Chirality Piping",
        "query": "domains/chirality-piping/**/NOTICE_D-GOV-*",
        "matches": sorted(
            path
            for path in tree
            if path.startswith("domains/chirality-piping/") and "NOTICE_D-GOV-" in path
        ),
        "status": "ABSENT",
    },
    {
        "description": "Root doctrine notices under Piping Design",
        "query": "domains/piping-design/**/NOTICE_D-GOV-*",
        "matches": sorted(
            path
            for path in tree
            if path.startswith("domains/piping-design/") and "NOTICE_D-GOV-" in path
        ),
        "status": "ABSENT",
    },
]

request_bytes = REQUEST_PATH.read_bytes()
manifest = {
    "schema": "chirality.tandem-review.frozen-basis.v1",
    "review_id": "CHIRALITY-PROGRAM-ARCH-TANDEM-2026-07-26-DA31C19",
    "repository": str(REPO),
    "review_freeze": FREEZE,
    "product_basis_commit": PRODUCT_BASIS,
    "basis_rule": "Git blob bytes at review_freeze govern; live filesystem bytes and mutable pointers do not.",
    "product_basis_to_freeze_diff": diff_names,
    "charter": {
        "path": CHARTER_PATH,
        "git_blob": charter_entry["git_blob"],
        "sha256": charter_entry["sha256"],
        "authority_status": "NON_GOVERNING_PROCEDURE_AND_CHALLENGE",
    },
    "initiating_request": {
        "source_path": str(REQUEST_PATH),
        "sha256": hashlib.sha256(request_bytes).hexdigest(),
        "bytes": len(request_bytes),
    },
    "selection_note": (
        "Core review corpus required by the charter and initiating manifest. "
        "A reviewer may follow an evidence reference to another frozen blob only when a selected "
        "governing instrument makes it relevant; any such supplemental evidence must be cited by "
        "review_freeze:path and content hash and must not be a candidate/historical surface treated as authority."
    ),
    "excluded_as_authority": [
        "plans/** other than the charter",
        "candidate and proposal packets unless a governing decision adopts exact bytes",
        "historical workplans, snapshots, AgentRuns, and run evidence unless expressly selected",
        "mutable _LATEST.md and _REGISTER.md pointers as independent authority",
        "domain packs as products under review",
        "PEC frozen v0.4 prototype",
        "App UI/API semantic-parity proposal",
        "resource-governance candidate architecture",
    ],
    "category_counts": dict(sorted(category_counts.items())),
    "entry_count": len(entries),
    "declared_absence_checks": declared_absence_checks,
    "entries": entries,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
encoded = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
OUT.write_bytes(encoded)
print(
    json.dumps(
        {
            "output": str(OUT),
            "sha256": hashlib.sha256(encoded).hexdigest(),
            "entries": len(entries),
            "category_counts": dict(sorted(category_counts.items())),
        },
        indent=2,
        sort_keys=True,
    )
)
