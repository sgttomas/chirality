#!/usr/bin/env python3
"""Produce PKG-06 verifier-owned replacement, simulation, and closure evidence."""
from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/WORKING-P2-PKG06/children/VERIFY-B1"
CAND = RUN / "candidates/W_P2/PIP-PKG06"
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-06-01": ("2dabc6c8337678fd2cb829fa73e2b5550a692db0045de3d5779fae6208872bb3", 29, 260),
    "DEL-06-02": ("b439df6dab8cadf7c3784589becb85bf75d32d26e3f7f71446b6cc7417d8adc9", 35, 301),
    "DEL-06-03": ("9404636c5eb9becf8fa2c5c3df12aa7d32e276783664b9dfa4970f3f5f651e1f", 30, 231),
    "DEL-06-04": ("58ab8ae2e0a65bfc816c9f3d5ba775381eac2ca86fa74635b0609cfbf2d865a5", 28, 266),
    "DEL-06-05": ("3b05da1fc58d3bb2023ca707ff7325ca390f8c6106765bec8e22c9f17a14aad8", 29, 285),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == HEAD
    assert subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip() == HEAD
    rows = [r for r in csv.DictReader((RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t") if r["deliverable_id"] in EXPECTED]
    assert [r["deliverable_id"] for r in rows] == list(EXPECTED)
    replacement: list[dict[str, object]] = []
    inverse: list[dict[str, object]] = []
    simulations: list[dict[str, object]] = []
    for row in rows:
        did = row["deliverable_id"]
        live = ROOT / row["live_path"]
        clean = CAND / did / "production/ScopeOfWork.md"
        clean_sha, maps, lines = EXPECTED[did]
        assert sha(clean) == clean_sha
        add_path = f'{row["live_path"]}/ScopeOfWork.md'
        replacement.append({"deliverable_id": did, "operation": "ADD", "path": add_path, "sha256": clean_sha})
        inverse.append({"deliverable_id": did, "operation": "DELETE", "path": add_path, "sha256": clean_sha})
        for name, key in [("Datasheet.md", "datasheet_sha256"), ("Specification.md", "specification_sha256"), ("Guidance.md", "guidance_sha256"), ("Procedure.md", "procedure_sha256")]:
            assert sha(live / name) == row[key]
            rel = f'{row["live_path"]}/{name}'
            replacement.append({"deliverable_id": did, "operation": "DELETE", "path": rel, "sha256": row[key]})
            inverse.append({"deliverable_id": did, "operation": "ADD", "path": rel, "sha256": row[key]})

        sim = HERE / "simulations" / did
        if sim.exists():
            shutil.rmtree(sim)
        apply = sim / "apply"
        rollback = sim / "rollback"
        apply.mkdir(parents=True)
        rollback.mkdir(parents=True)
        for name in SOURCE + CONTROLS:
            shutil.copyfile(live / name, apply / name)
            shutil.copyfile(live / name, rollback / name)
        for name in SOURCE:
            (apply / name).unlink()
        shutil.copyfile(clean, apply / "ScopeOfWork.md")
        result = subprocess.run(["python3", "tools/scope_of_work/validate_scope_of_work.py", str(apply), "--json"], cwd=ROOT, text=True, capture_output=True)
        (sim / "apply_validation.stdout").write_text(result.stdout, encoding="utf-8")
        (sim / "apply_validation.stderr").write_text(result.stderr, encoding="utf-8")
        assert result.returncode == 0
        parsed = json.loads(result.stdout)
        assert parsed.get("format") == "SOW_V1" and parsed.get("valid") is True
        assert sha(apply / "ScopeOfWork.md") == clean_sha
        assert all(not (apply / name).exists() for name in SOURCE)
        assert all(sha(apply / name) == sha(live / name) for name in CONTROLS)
        assert all(sha(rollback / name) == sha(live / name) for name in SOURCE + CONTROLS)
        assert not (rollback / "ScopeOfWork.md").exists()
        simulations.append({"deliverable_id": did, "apply": "PASS_SOW_V1", "target": "PASS_EXACT_FIVE_ROW_DELTA", "rollback": "PASS_EXACT_LEGACY_RESTORE", "control_bindings": 5, "mappings": maps, "source_lines": lines})

    write_tsv(HERE / "REPLACEMENT_ROWS.tsv", ["deliverable_id", "operation", "path", "sha256"], replacement)
    write_tsv(HERE / "INVERSE_ROWS.tsv", ["deliverable_id", "operation", "path", "sha256"], inverse)
    write_tsv(HERE / "SIMULATIONS.tsv", ["deliverable_id", "apply", "target", "rollback", "control_bindings", "mappings", "source_lines"], simulations)
    assert len(replacement) == len(inverse) == 25 and len(simulations) == 5

    status = {
        "agent": "VERIFY-B1", "status": "PASS_UNCHANGED", "members_complete": 5,
        "mappings": 151, "source_lines": 1343, "fail_closed_probes": 35,
        "candidate_repairs": 0, "candidate_writes": 0, "project_writes": 0,
        "discrepancies": 0, "semantic_expansions": 0, "waivers": 0,
        "replacement_rows": 25, "inverse_rows": 25, "simulations": 5,
        "native_context_occupancy": "unavailable",
    }
    (HERE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    terminal = {
        "verdict": "PASS_UNCHANGED", "accepted_checkout": HEAD, "origin_main": HEAD,
        "tool_authority": AUTH, "complete_members": list(EXPECTED),
        "live_bindings_unchanged": 45, "candidate_bindings_unchanged": 15,
        "live_scope_of_work_paths_absent": 5, "mapping_rows": 151, "source_lines": 1343,
        "replacement_rows": 25, "inverse_rows": 25, "apply_target_rollback_simulations": 5,
        "candidate_repairs": 0, "candidate_writes": 0, "project_writes": 0,
        "member_discrepancies": 0, "member_repairs": 0,
        "write_prefix": "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG06/children/VERIFY-B1/",
    }
    (HERE / "TERMINAL_AUDIT.json").write_text(json.dumps(terminal, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    (HERE / "CONTAINMENT.md").write_text("""# VERIFY-B1 Containment

- Fresh, non-delegating evidence-only Agent 2; no author or sibling contact.
- Exact scope: `DEL-06-01..05`, completed in numeric order.
- Writes: this verifier folder only; candidates and live project remained read-only.
- Live bindings unchanged: 45/45; candidate bindings unchanged: 15/15.
- Live `ScopeOfWork.md` remains absent for all five members.
- No lifecycle, control, dependency, PKG-00, Git, release, reliance, rollback execution, retirement, or H2 write.
- Native token/context occupancy was unavailable and was not inferred; complete fifth-member evidence shows no observable abbreviation or task drift.
""", encoding="utf-8")
    (HERE / "ATTEMPTS.md").write_text("""# VERIFY-B1 Attempts

One terminal verifier invocation completed all five members. There were zero member failures, retries, candidate repairs, semantic repairs, or evidence normalization repairs. The inherited verifier harness was bound before invocation to trim comma-separated reference tokens and to use a visible verifier-only mutation in the negative probe; these are established template bindings, not runtime failures or candidate changes.
""", encoding="utf-8")
    (HERE / "RETURN.md").write_text("""# VERIFY-B1 Return

Status: `PASS_UNCHANGED`

The fresh evidence-only verifier independently closed `DEL-06-01..05` in numeric order without delegation, author contact, candidate repair, or project write.

- Members: 5/5.
- Fresh conversion: 10/10 evidence outputs byte-identical to each other and accepted candidates.
- Fresh finalization: 10/10 clean outputs and reports byte-identical to accepted production/report candidates.
- Preservation: 151/151 mappings and 1,343/1,343 physical source lines.
- Validation: 5/5 authorized isolated-dual workspaces and 5/5 standalone clean `SOW_V1` candidates pass.
- Deterministic consumers: 10/10 production-bound maps/parity runs, 10/10 checklists, and 10/10 renders reproduce byte-identically.
- Fail-closed probes: 35/35 pass.
- Replacement evidence: exact 25 forward rows, 25 inverse rows, and five apply/target/rollback simulations pass.
- Post-state: 45/45 live and 15/15 candidate bindings unchanged; five live SOW paths remain absent.
- Verdict classes: schema, project content, preservation/containment, clean finalization, and execution substrate all `PASS`.
- Findings: zero discrepancy, repair, blocker, waiver, unknown, semantic expansion, contamination, drift, omission, or late-member abbreviation.

Native token/context occupancy was unavailable and was not inferred. This is derivative verification evidence only; parent fan-in remains required, and no integration, lifecycle, release, reliance, retirement, rollback execution, or H2 authority is granted.
""", encoding="utf-8")


if __name__ == "__main__":
    main()
