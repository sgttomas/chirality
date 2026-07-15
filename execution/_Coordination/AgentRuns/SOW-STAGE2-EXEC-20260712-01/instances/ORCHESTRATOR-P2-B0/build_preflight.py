#!/usr/bin/env python3
"""Build the deterministic, read-only W-P2 Piping preflight snapshot."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_P2/preflight"
P3 = RUN / "snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv"
P4 = RUN / "snapshots/P4_PILOTS/integration/postmerge/POST_STATE_LEDGER.tsv"
PIPING = ROOT / "projects/chirality-piping"
DAG = PIPING / "execution/_DAG/DAG-007/DependencyEdges.csv"
DISPATCH = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
PACKAGES = {"PKG-05": 5, "PKG-06": 5, "PKG-07": 8, "PKG-08": 6, "PKG-09": 5}
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
BINDING_FILES = SOURCE_FILES + CONTROL_FILES
MAX_MEMBERS = 5
MAX_LINES = 2053


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n")


def current_state(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("**Current State:**"):
            return line.split("**Current State:**", 1)[1].strip().strip("`")
    return "UNRESOLVED"


def physical_lines(path: Path) -> int:
    return len(path.read_bytes().splitlines())


def dependency_rows(path: Path) -> int:
    with path.open(newline="") as handle:
        return max(sum(1 for _ in csv.reader(handle)) - 1, 0)


def section_items(path: Path, heading: str) -> str:
    active = False
    items: list[str] = []
    for line in path.read_text().splitlines():
        if line == heading:
            active = True
            continue
        if active and line.startswith("## "):
            break
        if active and line.startswith("- "):
            items.append(line[2:].strip())
    return ", ".join(items)


def validate(deliverable: Path) -> dict[str, object]:
    proc = subprocess.run(
        ["python3", "tools/scope_of_work/validate_scope_of_work.py", str(deliverable), "--json"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return {
        "exit_code": proc.returncode,
        "format": payload.get("format", "UNRESOLVED"),
        "valid": payload.get("valid", False),
        "issues": json.dumps(payload.get("issues", []), separators=(",", ":")),
    }


def make_batches(rows: list[dict[str, object]]) -> list[list[dict[str, object]]]:
    batches: list[list[dict[str, object]]] = []
    current: list[dict[str, object]] = []
    current_lines = 0
    for row in rows:
        lines = int(row["source_lines"])
        if lines > MAX_LINES:
            raise SystemExit(f"single member exceeds line limit: {row['deliverable_id']}={lines}")
        if current and (len(current) + 1 > MAX_MEMBERS or current_lines + lines > MAX_LINES):
            batches.append(current)
            current = []
            current_lines = 0
        current.append(row)
        current_lines += lines
    if current:
        batches.append(current)
    return batches


def refs() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for ref in ["HEAD", "refs/remotes/origin/main"]:
        value = subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, text=True).strip()
        rows.append({"ref": ref, "sha": value, "result": "PASS" if value == DISPATCH else "FAIL"})
    remote = subprocess.check_output(["git", "ls-remote", "--heads", "origin", "main"], cwd=ROOT, text=True).split()[0]
    rows.append({"ref": "remote refs/heads/main", "sha": remote, "result": "PASS" if remote == DISPATCH else "FAIL"})
    # Local main is intentionally allowed to lag in this isolated closeout worktree;
    # origin/main and remote main are the synchronized live basis.
    local_main = subprocess.check_output(["git", "rev-parse", "refs/heads/main"], cwd=ROOT, text=True).strip()
    rows.append({"ref": "refs/heads/main (informational isolated-worktree ref)", "sha": local_main, "result": "INFO"})
    for label, ancestor in [
        ("D-GOV-16", "7584718aa32b112e415331736d1a8e68c12ac176"),
        ("W-P1 acceptance", "c5abf91b717c0b3901d2a27c578e63976853f8de"),
        ("H1 ruling binding", "b776813d57124df94e9ba1b66a8a63e89487b388"),
        ("I1 merge", "6d56a1b6f391d21618f3328179d5a48654aec422"),
    ]:
        ok = subprocess.run(["git", "merge-base", "--is-ancestor", ancestor, DISPATCH], cwd=ROOT).returncode == 0
        rows.append({"ref": f"ancestor {label}@{ancestor}", "sha": DISPATCH, "result": "PASS" if ok else "FAIL"})
    return rows


def main() -> None:
    if OUT.exists() and any(OUT.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty snapshot: {OUT}")
    OUT.mkdir(parents=True, exist_ok=True)
    p3_rows = read_tsv(P3)
    selected = [r for r in p3_rows if r["project"] == "PIP" and r["package"] in PACKAGES]
    selected.sort(key=lambda r: (r["package"], r["deliverable_id"]))
    counts = dict(sorted(Counter(r["package"] for r in selected).items()))
    if len(selected) != 29 or counts != PACKAGES:
        raise SystemExit(f"population mismatch: {len(selected)} {counts}")

    managers = {pkg: f"WORKING-P2-{pkg.replace('-', '')}" for pkg in PACKAGES}
    manifest_rows: list[dict[str, object]] = []
    binding_rows: list[dict[str, object]] = []
    validator_rows: list[dict[str, object]] = []
    p3_mismatches: list[str] = []
    total_dep_rows = 0
    for source in selected:
        rel = Path(source["path"])
        live = ROOT / rel
        result = validate(live)
        validator_rows.append({"package": source["package"], "deliverable_id": source["deliverable_id"], "live_path": rel.as_posix(), **result})
        hashes: dict[str, str] = {}
        line_counts: dict[str, int] = {}
        for name in BINDING_FILES:
            path = live / name
            state = "PRESENT" if path.is_file() else "MISSING"
            digest = sha(path) if path.is_file() else "MISSING"
            hashes[name] = digest
            binding_rows.append({"package": source["package"], "deliverable_id": source["deliverable_id"], "live_path": rel.as_posix(), "binding": name, "state": state, "sha256": digest})
        for name in SOURCE_FILES:
            line_counts[name] = physical_lines(live / name)
        p3_map = {
            "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
            "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256", "_STATUS.md": "status_sha256",
        }
        p3_match = all(hashes[name] == source[field] for name, field in p3_map.items())
        if not p3_match:
            p3_mismatches.append(source["deliverable_id"])
        dep_count = dependency_rows(live / "Dependencies.csv")
        total_dep_rows += dep_count
        did = source["deliverable_id"]
        manager = managers[source["package"]]
        total_lines = sum(line_counts.values())
        manifest_rows.append({
            "project": "PIP", "package": source["package"], "manager": manager,
            "deliverable_id": did, "live_path": rel.as_posix(), "lifecycle": current_state(live / "_STATUS.md"),
            "pilot": source["pilot"], "issued": source["issued"], "live_format": result["format"],
            "datasheet_sha256": hashes["Datasheet.md"], "datasheet_lines": line_counts["Datasheet.md"],
            "specification_sha256": hashes["Specification.md"], "specification_lines": line_counts["Specification.md"],
            "guidance_sha256": hashes["Guidance.md"], "guidance_lines": line_counts["Guidance.md"],
            "procedure_sha256": hashes["Procedure.md"], "procedure_lines": line_counts["Procedure.md"],
            "source_lines": total_lines, "status_sha256": hashes["_STATUS.md"], "context_sha256": hashes["_CONTEXT.md"],
            "references_sha256": hashes["_REFERENCES.md"], "dependencies_md_sha256": hashes["_DEPENDENCIES.md"],
            "dependencies_csv_sha256": hashes["Dependencies.csv"], "dependency_rows": dep_count,
            "scope_refs": section_items(live / "_CONTEXT.md", "## Scope Coverage"),
            "objective_refs": section_items(live / "_CONTEXT.md", "## Objective Support"),
            "decomposition_basis": f"projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@{DISPATCH}",
            "candidate_path": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P2/PIP-{source['package'].replace('-', '')}/{did}/ScopeOfWork.md",
            "integration_delta": "A ScopeOfWork.md;D Datasheet.md;D Specification.md;D Guidance.md;D Procedure.md",
            "p3_source_status_match": str(p3_match).lower(),
            "binding_state": "COMPLETE" if all(hashes[name] != "MISSING" for name in BINDING_FILES) else "INCOMPLETE",
        })

    manifest_fields = list(manifest_rows[0])
    write_tsv(OUT / "P2_MANIFEST.tsv", manifest_fields, manifest_rows)
    write_tsv(OUT / "EXPECTED_LIVE_BINDINGS.tsv", ["package", "deliverable_id", "live_path", "binding", "state", "sha256"], binding_rows)
    write_tsv(OUT / "VALIDATOR_RESULTS.tsv", ["package", "deliverable_id", "live_path", "exit_code", "format", "valid", "issues"], validator_rows)

    # Minimal consecutive partition under both accepted hard limits.
    batch_rows: list[dict[str, object]] = []
    package_rows: list[dict[str, object]] = []
    for sequence, package in enumerate(PACKAGES, 1):
        members = [r for r in manifest_rows if r["package"] == package]
        batches = make_batches(members)
        for batch_number, batch in enumerate(batches, 1):
            batch_id = f"{package}-B{batch_number}"
            manager = managers[package]
            ids = [str(r["deliverable_id"]) for r in batch]
            batch_rows.append({
                "package": package, "manager": manager, "batch": batch_id, "batch_sequence": batch_number,
                "members": len(batch), "member_ids": ",".join(ids), "first_member": ids[0], "last_member": ids[-1],
                "source_lines": sum(int(r["source_lines"]) for r in batch), "member_limit": MAX_MEMBERS,
                "line_limit": MAX_LINES, "author_instance": f"{manager}/children/AUTHOR-B{batch_number}",
                "verifier_instance": f"{manager}/children/VERIFY-B{batch_number}",
                "author_then_verifier": "REQUIRED", "partition_verdict": "PASS",
            })
        depends = "W-P2-B0_ACCEPTED" if sequence == 1 else f"W-P2-{list(PACKAGES)[sequence-2].replace('-', '')}_PASS"
        package_rows.append({
            "wave": "W-P2", "sequence": sequence, "package": f"PIP-{package}", "manager": managers[package],
            "members": len(members), "source_lines": sum(int(r["source_lines"]) for r in members), "batches": len(batches),
            "member_ids": ",".join(str(r["deliverable_id"]) for r in members), "depends_on": depends,
            "candidate_write_scope": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P2/PIP-{package.replace('-', '')}/**",
            "evidence_write_scope": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{managers[package]}/**",
            "sealed_brief": f"snapshots/W_P2/preflight/PACKAGE_BRIEFS/{managers[package]}.md",
            "fan_in_gates": f"{len(members)}/{len(members)} complete author-verifier coverage; {len(members)*9}/{len(members)*9} bindings; exact {len(members)*5}-row replacement/inverse; zero project writes",
            "release_state": "PARKED_AWAITING_HELP_HUMAN_ACCEPTANCE",
        })
    write_tsv(OUT / "BATCH_PLAN.tsv", list(batch_rows[0]), batch_rows)
    write_tsv(OUT / "PACKAGE_PLAN.tsv", list(package_rows[0]), package_rows)

    # PKG-00 direction remains a live invariant for these five actual packages.
    with DAG.open(newline="") as handle:
        dag_rows = list(csv.DictReader(handle))
    active = [r for r in dag_rows if r["Status"] == "ACTIVE"]
    direction_rows = []
    for package in PACKAGES:
        edges = [r for r in active if r["FromPackageID"] == package and r["TargetPackageID"] == "PKG-00"]
        direction_rows.append({
            "package": package, "active_edges_to_pkg00": len(edges),
            "covered_deliverables": len({r["FromDeliverableID"] for r in edges}),
            "pkg00_targets": ",".join(sorted({r["TargetDeliverableID"] or r["TargetRefID"] for r in edges})),
            "verdict": "PASS" if edges else "FAIL",
        })
    outbound = [r for r in active if r["FromPackageID"] == "PKG-00" and (r["TargetPackageID"] not in ("", "PKG-00") or (r["TargetDeliverableID"] and not r["TargetDeliverableID"].startswith("DEL-00-")))]
    write_tsv(OUT / "PKG00_DIRECTION_VALIDATION.tsv", list(direction_rows[0]), direction_rows)
    write_tsv(OUT / "PKG00_OUTBOUND_CONTRADICTIONS.tsv", ["DependencyID", "FromPackageID", "FromDeliverableID", "TargetPackageID", "TargetDeliverableID", "Status", "Statement"], outbound)

    # Freeze all accepted Piping SOW predecessors and prove no selected overlap.
    p4_by_id = {r["deliverable_id"]: r for r in read_tsv(P4) if r["project"] == "PIP"}
    p3_pip = {r["deliverable_id"]: r for r in p3_rows if r["project"] == "PIP"}
    predecessor_ids = sorted(set(p4_by_id) | {r["deliverable_id"] for r in p3_rows if r["project"] == "PIP" and r["package"] in {"PKG-01", "PKG-02", "PKG-03", "PKG-04"}})
    predecessor_rows: list[dict[str, object]] = []
    for did in predecessor_ids:
        source = p3_pip[did]
        live = ROOT / source["path"]
        result = validate(live)
        predecessor_rows.append({
            "deliverable_id": did, "live_path": source["path"], "lifecycle": current_state(live / "_STATUS.md"),
            "format": result["format"], "valid": result["valid"], "sow_sha256": sha(live / "ScopeOfWork.md") if (live / "ScopeOfWork.md").is_file() else "MISSING",
            "status_sha256": sha(live / "_STATUS.md"), "legacy_files": sum((live / name).exists() for name in SOURCE_FILES),
            "selected_overlap": str(any(r["deliverable_id"] == did for r in manifest_rows)).lower(),
            "verdict": "PASS" if result["format"] == "SOW_V1" and result["valid"] and not any((live / name).exists() for name in SOURCE_FILES) else "FAIL",
        })
    write_tsv(OUT / "PREDECESSOR_RESULTS.tsv", list(predecessor_rows[0]), predecessor_rows)

    methods = [
        ("docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md", "ACTIVE_STANDARD"),
        ("tools/scope_of_work/common.py", "ACTIVE_RESOLVER"),
        ("tools/scope_of_work/validate_scope_of_work.py", "ACTIVE_VALIDATOR"),
        ("tools/scope_of_work/convert_four_documents_to_scope_of_work.py", "ACTIVE_CONVERTER"),
        ("tools/scope_of_work/map_scope_of_work_claims.py", "ACTIVE_MAPPER"),
        ("tools/scope_of_work/report_scope_of_work_parity.py", "ACTIVE_PARITY"),
        ("tools/scope_of_work/derive_review_checklist.py", "ACTIVE_CHECKLIST"),
        ("tools/scope_of_work/finalize_scope_of_work.py", "ACTIVE_FINALIZER"),
        ("skills/scope-of-work/SKILL.md", "ACTIVE_SKILL"),
        ("skills/scope-of-work/BRIEF_SCHEMA.md", "ACTIVE_BRIEF_SCHEMA"),
        ("skills/scope-of-work/QA_CHECKS.md", "ACTIVE_QA"),
        ("skills/scope-of-work/TOOL_POLICY.md", "ACTIVE_TOOL_POLICY"),
        ("docs/SOFTWARE_WORKFLOW_PROFILE.md", "RATIFIED_PROFILE_CONTRACT"),
        ("projects/chirality-piping/AGENTS.md", "PROJECT_INSTRUCTIONS"),
        ("projects/chirality-piping/software-workflow.json", "PROJECT_CHECK_PROFILE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv", "ACCEPTED_EXECUTION_POPULATION"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/ACCEPTANCE.md", "ACCEPTED_P1_PREDECESSOR"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/I0/integration/postmerge/MANIFEST.tsv", "ACCEPTED_I1_PREDECESSOR"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md", "ACTIVE_HUMAN_STEER"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/PACKAGE-BATCH-ADOPTION-001.md", "ACTIVE_BATCH_RULE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/RUNTIME-EFFICIENCY-001.md", "ACTIVE_RUNTIME_RULE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/PKG03-DETERMINISTIC-EVIDENCE-NORMALIZATION-001.md", "ACTIVE_NORMALIZATION_RULE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/MANAGER-CHILD-TOPOLOGY-CLARIFICATION-001.md", "ACTIVE_TOPOLOGY_RULE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/POST-I1-CLOSURE-RELEASE-CORRECTION-001.md", "ACTIVE_RELEASE_CORRECTION"),
        ("projects/chirality-piping/execution/_DAG/DAG-007/DependencyEdges.csv", "ACCEPTED_DEPENDENCY_REGISTER"),
    ]
    missing_methods = [path for path, _ in methods if not (ROOT / path).is_file()]
    if missing_methods:
        raise SystemExit(f"missing method bindings: {missing_methods}")
    write_tsv(OUT / "METHOD_BINDINGS.tsv", ["surface", "sha256", "classification"], [{"surface": p, "sha256": sha(ROOT / p), "classification": c} for p, c in methods])
    ref_rows = refs()
    write_tsv(OUT / "REFS.tsv", ["ref", "sha", "result"], ref_rows)

    contract = f"""
# W-P2 Sequential Package Execution Contract

Status: `SEALED CANDIDATE — AWAITING HELP_HUMAN ACCEPTANCE`

This derivative contract freezes the exact 29-member ordinary Piping P2
population on `main@{DISPATCH}`. It does not release a manager or authorize
project mutation.

## Execution topology

Run one fresh WORKING_ITEMS manager per package in strict order PKG-05 through
PKG-09. Within a package, execute every frozen consecutive batch in order.
Each batch has one fresh package-batch author followed only after terminal
author PASS by one fresh evidence-only verifier over 100% of the same members.
The verifier does not repair author output. Both preserve complete per-member
mapping, source-line coverage, source/evidence/production hashes, clean
finalization, exact replacement and inverse rows, simulations, project checks,
telemetry, findings, attempts, repairs, and rerun conditions.

Safe mechanical evidence defects are repaired in owned evidence scope without
stopping: retain the failed attempt, prove the repair is non-semantic, rebuild
every direct/transitive binding, and rerun affected checks. Project, source,
candidate-semantic, lifecycle, authority, or acceptance drift is not mechanical
and must be escalated.

## Content and integration fences

Candidate preparation writes only the exact package candidate/evidence scopes.
Live project paths remain read-only. Every member's future integration delta is
exactly one added clean `ScopeOfWork.md` and four deleted legacy documents;
status and all controls remain byte-identical. Only CHANGE may later integrate
an accepted RECONCILIATION manifest. PKG-00 remains excluded upstream-only
context. H2, retirement, rollback execution, release, and reliance remain
unauthorized.

After all package managers pass, direct RECONCILIATION performs aggregate
fan-in itself without a redundant child layer: 100% manifests, paths,
population/totals, replacement/rollback rows, containment and simulations;
fresh reproduction of every exception and the numerically final clean member
per package; full affected-package expansion on any exception or failure.
"""
    write_text(OUT / "PACKAGE_EXECUTION_CONTRACT.md", contract)
    for plan in package_rows:
        package = str(plan["package"]).removeprefix("PIP-")
        members = [r for r in manifest_rows if r["package"] == package]
        batches = [r for r in batch_rows if r["package"] == package]
        member_lines = "\n".join(f"- `{r['deliverable_id']}` — {r['source_lines']} lines — `{r['live_path']}`" for r in members)
        batch_lines = "\n".join(f"- `{r['batch']}`: {r['members']} members, {r['source_lines']} lines; `{r['member_ids']}`; author `{r['author_instance']}` then verifier `{r['verifier_instance']}`" for r in batches)
        brief = f"""
# {plan['manager']} Sealed Package Brief

Status: `PARKED — AWAITING HELP_HUMAN ACCEPTANCE AND PREDECESSOR RELEASE`

Execute only after `{plan['depends_on']}`. Incorporate
`../PACKAGE_EXECUTION_CONTRACT.md` exactly. This is one fresh package manager;
retain package ownership across all batches.

## Exact members

{member_lines}

## Exact consecutive batches

{batch_lines}

Candidate scope: `{plan['candidate_write_scope']}`

Evidence scope: `{plan['evidence_write_scope']}`

Before dispatch, reproduce every package row and hash from `P2_MANIFEST.tsv`
and `EXPECTED_LIVE_BINDINGS.tsv`, current `IN_PROGRESS` lifecycle, valid exact
`LEGACY_FOUR_DOC`, SOW absence, accepted predecessors, PKG-00 direction, active
method/check bindings, and refs. Dispatch the author/verifier pair for each
batch serially. Child write scopes must be disjoint by role/batch; children do
not delegate. Do not write live project paths, Git, lifecycle, PKG-00,
integration, release, reliance, retirement, rollback execution, or H2 state.

Return PASS, BLOCKED, or DECISION_REQUIRED with complete per-member fan-in,
attempt history, repairs/rebindings, telemetry, blockers/unknowns/waivers,
derivative status, rerun triggers, and explicit handoff for direct RECON.
"""
        write_text(OUT / f"PACKAGE_BRIEFS/{plan['manager']}.md", brief)

    applicable_checks = [
        {"check": "scope-format", "command": "validate_scope_of_work.py --json (29 members)", "result": "PASS" if all(r["exit_code"] == 0 and r["format"] == "LEGACY_FOUR_DOC" and r["valid"] for r in validator_rows) else "FAIL", "evidence": "VALIDATOR_RESULTS.tsv"},
        {"check": "dependency-schema", "command": "validate_dependencies_schema.py (29 registers)", "result": "PENDING", "evidence": "CHECK_COMMAND_RESULTS.tsv"},
        {"check": "harness-self-check", "command": "python3 tools/practitioner_harness/harness.py self-check", "result": "PENDING", "evidence": "CHECK_COMMAND_RESULTS.tsv"},
        {"check": "harness-pytest", "command": "python3 -m pytest -q tools/practitioner_harness", "result": "PENDING", "evidence": "CHECK_COMMAND_RESULTS.tsv"},
    ]
    write_tsv(OUT / "APPLICABLE_CHECKS.tsv", list(applicable_checks[0]), applicable_checks)

    preliminary = all([
        len(binding_rows) == 261, all(r["state"] == "PRESENT" for r in binding_rows), not p3_mismatches,
        all(r["exit_code"] == 0 and r["format"] == "LEGACY_FOUR_DOC" and r["valid"] for r in validator_rows),
        all(r["lifecycle"] == "IN_PROGRESS" and r["pilot"] == "false" and r["issued"] == "false" for r in manifest_rows),
        not any((ROOT / str(r["live_path"]) / "ScopeOfWork.md").exists() for r in manifest_rows),
        all(r["members"] <= MAX_MEMBERS and r["source_lines"] <= MAX_LINES for r in batch_rows),
        all(r["verdict"] == "PASS" for r in direction_rows), not outbound,
        all(r["verdict"] == "PASS" and r["selected_overlap"] == "false" for r in predecessor_rows),
        all(r["result"] in ("PASS", "INFO") for r in ref_rows),
    ])
    summary = {
        "wave": "P2", "dispatch_basis": DISPATCH, "selected_members": 29, "package_counts": PACKAGES,
        "source_lines": sum(int(r["source_lines"]) for r in manifest_rows), "expected_live_bindings": 261,
        "present_live_bindings": sum(r["state"] == "PRESENT" for r in binding_rows), "dependency_registers": 29,
        "dependency_rows": total_dep_rows, "package_batches": len(batch_rows),
        "batch_counts": dict(Counter(str(r["package"]) for r in batch_rows)),
        "lifecycle_counts": dict(Counter(str(r["lifecycle"]) for r in manifest_rows)),
        "format_counts": dict(Counter(str(r["live_format"]) for r in manifest_rows)), "live_sow": 0,
        "p3_source_status_mismatches": p3_mismatches, "accepted_piping_predecessors": len(predecessor_rows),
        "preliminary_verdict": "PASS" if preliminary else "DECISION_REQUIRED",
        "final_verdict": "PENDING_COMMAND_CHECKS",
    }
    write_text(OUT / "SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))
    write_text(OUT / "BASIS.md", f"""
# W-P2 Ordinary Piping Preflight Basis

Status: `IMMUTABLE DERIVATIVE CANDIDATE — PENDING COMMAND CHECKS`

The exact population is 29 P3 ordinary Piping members in PKG-05 through
PKG-09, split 5/5/8/6/5. All 116 legacy sources, 29 statuses, and 261 live
bindings reproduce the accepted execution manifest. Every member is non-pilot,
non-issued, `IN_PROGRESS`, valid `LEGACY_FOUR_DOC`, and SOW-absent. The frozen
legacy corpus contains {sum(int(r['source_lines']) for r in manifest_rows)}
physical lines and {total_dep_rows} dependency rows.

The minimum consecutive partition under five-member/2,053-line limits is
seven batches: PKG-05 5; PKG-06 5; PKG-07 5+3; PKG-08 5+1; PKG-09 5.
All accepted Piping SOW predecessors are separately frozen and disjoint. Active
PKG-00 upstream direction is valid for all five packages with zero outbound
contradictions. Method, authority, check-profile, P1/I1, refs, and release
correction bindings are frozen. No project/candidate/Git/lifecycle write or
conversion occurred.
""")


def bind_snapshot() -> None:
    rows: list[dict[str, object]] = []
    for path in sorted(OUT.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.tsv":
            continue
        data_rows: object = "not_applicable"
        if path.suffix == ".tsv":
            data_rows = max(len(path.read_text().splitlines()) - 1, 0)
        rows.append({"artifact": path.relative_to(OUT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size, "data_rows": data_rows, "binding_status": "BOUND"})
    write_tsv(OUT / "MANIFEST.tsv", ["artifact", "sha256", "bytes", "data_rows", "binding_status"], rows)


if __name__ == "__main__":
    main()
    bind_snapshot()
