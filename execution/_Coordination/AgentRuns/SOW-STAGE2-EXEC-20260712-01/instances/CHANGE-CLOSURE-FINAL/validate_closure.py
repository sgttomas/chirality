#!/usr/bin/env python3
"""Validate the exact control-plane-only conversion-closure integration."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
BASIS = "79de30d83b91a2ab468a3f17536a5233c2f85fe7"
EXPECTED = {
    "final_reconciliation": "7975141369025a50087c6f8d94b51d59740d0adabb49576518c9c4d7926add27",
    "final_evaluation": "3a17c5b5637216b74018206a931a4a01fb6c90769094ac77d4a3c57da47b133f",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", BASIS, "HEAD"], cwd=ROOT, text=True
    ).splitlines()
    assert changed
    assert all(path.startswith("execution/_Coordination/") for path in changed), changed

    prohibited = ["projects/", "skills/", "tools/", "agents/", "docs/"]
    assert not any(path.startswith(tuple(prohibited)) for path in changed), changed

    for name, expected in EXPECTED.items():
        manifest = RUN / "snapshots/CONVERSION_CLOSURE" / name / "MANIFEST.tsv"
        assert sha256(manifest) == expected

    for instance in ("RECON-CLOSURE-FINAL", "EVALUATION-CLOSURE-FINAL"):
        status = json.loads((RUN / "instances" / instance / "STATUS.json").read_text())
        assert status["status"] == "PASS"
        assert status["basis"] == BASIS

    graph = json.loads((RUN / "WORK_GRAPH.json").read_text())
    nodes = {node["id"]: node for node in graph["nodes"]}
    assert nodes["CONVERSION-CLOSURE"]["status"] == "PASS_ACCEPTED"
    assert nodes["CONVERSION-CLOSURE"]["basis"] == BASIS
    assert nodes["CONVERSION-CLOSURE-CHANGE"]["status"] == "RELEASED"
    h2 = next(item for item in graph["gates"] if item["id"] == "H2")
    assert h2["state"] == "UNAPPROVED"
    assert nodes["LEGACY_RETIREMENT"]["status"] == "PARKED_HUMAN_GATE"

    acceptance = (RUN / "snapshots/CONVERSION_CLOSURE/HELP_HUMAN_ACCEPTANCE.md").read_text()
    assert "PASS_ACCEPTED" in acceptance
    assert "CONVERSION_CLOSED — LEGACY_RETIREMENT_RULING_REQUIRED" in acceptance
    assert "H2 remains an explicit human ruling" in acceptance

    print(json.dumps({
        "basis": BASIS,
        "changed_paths": len(changed),
        "control_plane_only": True,
        "h2": "UNAPPROVED",
        "legacy_retirement": "PARKED_HUMAN_GATE",
        "manifest_sha256": EXPECTED,
        "verdict": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
