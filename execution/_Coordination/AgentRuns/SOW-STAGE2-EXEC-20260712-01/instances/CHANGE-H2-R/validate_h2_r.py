#!/usr/bin/env python3
"""Validate the exact control-plane-only H2-R ruling integration."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
BASIS = "92725eace3ef50306bf0c09032bc59492e636c01"
ALLOWED = (
    "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/CHANGE-H2-R/",
    "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/CONVERSION_CLOSURE/H2_RULING.md",
    "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/ORCHESTRATION_PLAN.md",
    "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/WORK_GRAPH.json",
    "execution/_Coordination/CURRENT_WORKPLAN.md",
    "execution/_Coordination/HANDOFF_STATE.md",
    "execution/_Coordination/LOOP_RECEIPTS.md",
)


def main() -> None:
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", BASIS, "HEAD"], cwd=ROOT, text=True
    ).splitlines()
    assert changed
    assert all(any(path == item or path.startswith(item) for item in ALLOWED) for path in changed), changed

    graph = json.loads((RUN / "WORK_GRAPH.json").read_text())
    nodes = {node["id"]: node for node in graph["nodes"]}
    h2 = next(item for item in graph["human_gates"] if item["id"] == "H2")
    assert h2["state"] == "APPROVED_H2_R"
    assert h2["owner_ruling_basis"] == BASIS
    assert nodes["H2-R"]["status"] == "APPROVED"
    assert nodes["H2-R"]["basis"] == BASIS
    assert nodes["LEGACY_RETIREMENT"]["status"] == "RETAINED_NOT_AUTHORIZED"

    ruling = (RUN / "snapshots/CONVERSION_CLOSURE/H2_RULING.md").read_text()
    assert f"Exact basis: `{BASIS}`" in ruling
    assert "H2-R — RETAIN COMPATIBILITY; NO RETIREMENT" in ruling

    pointer = (ROOT / "execution/_Coordination/CURRENT_WORKPLAN.md").read_text()
    assert "CLOSED — H2-R COMPATIBILITY RETAINED" in pointer
    handoff = (ROOT / "execution/_Coordination/HANDOFF_STATE.md").read_text()
    assert "STAGE2_CLOSED — H2-R COMPATIBILITY RETAINED" in handoff
    assert "legacy retirement is not authorized" in handoff

    print(json.dumps({
        "basis": BASIS,
        "changed_paths": len(changed),
        "control_plane_only": True,
        "h2": "APPROVED_H2_R",
        "legacy_retirement": "RETAINED_NOT_AUTHORIZED",
        "verdict": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
