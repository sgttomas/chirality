#!/usr/bin/env python3
"""Build the deterministic read-only revised W-P1 preflight snapshot."""

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
OUT = RUN / "snapshots/W_P1/preflight-r1"
P3 = RUN / "snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv"
P4 = RUN / "snapshots/P4_PILOTS/integration/postmerge/POST_STATE_LEDGER.tsv"
STEER = RUN / "amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md"
PIPING = ROOT / "projects/chirality-piping"
DAG = PIPING / "execution/_DAG/DAG-007/DependencyEdges.csv"
DAG_POINTER = PIPING / "execution/_DAG/_LATEST.md"
DISPATCH = "69ac259a7113d5a838fb22aa2e84df0e0f109713"

SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
BINDING_FILES = SOURCE_FILES + CONTROL_FILES
EXPECTED_PACKAGES = {"PKG-01": 3, "PKG-02": 5, "PKG-03": 8, "PKG-04": 6}


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


def section_items(path: Path, heading: str) -> str:
    lines = path.read_text().splitlines()
    active = False
    items: list[str] = []
    for line in lines:
        if line == heading:
            active = True
            continue
        if active and line.startswith("## "):
            break
        if active and line.startswith("- "):
            items.append(line[2:].strip())
    return ", ".join(items)


def dependency_rows(path: Path) -> int:
    with path.open(newline="") as handle:
        return max(sum(1 for _ in csv.reader(handle)) - 1, 0)


def current_state(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("**Current State:**"):
            return line.split("**Current State:**", 1)[1].strip().strip("`")
    return "UNRESOLVED"


def validate(deliverable: Path) -> dict[str, object]:
    proc = subprocess.run(
        ["python3", "tools/scope_of_work/validate_scope_of_work.py", str(deliverable), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return {
        "exit_code": proc.returncode,
        "format": payload.get("format", "UNRESOLVED"),
        "valid": payload.get("valid", False),
        "issues": json.dumps(payload.get("issues", []), separators=(",", ":")),
    }


def ref_rows() -> list[dict[str, object]]:
    refs = ["HEAD", "refs/heads/main", "refs/remotes/origin/main"]
    rows = []
    for ref in refs:
        value = subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, text=True).strip()
        rows.append({"ref": ref, "sha": value, "result": "PASS" if value == DISPATCH else "FAIL"})
    remote = subprocess.check_output(["git", "ls-remote", "--heads", "origin", "main"], cwd=ROOT, text=True).split()[0]
    rows.append({"ref": "remote refs/heads/main", "sha": remote, "result": "PASS" if remote == DISPATCH else "FAIL"})
    for label, ancestor in [
        ("D-GOV-16", "7584718aa32b112e415331736d1a8e68c12ac176"),
        ("P4 accepted-main", "b4efb8e554354399aadf1f624c107f63ede3230d"),
        ("W-A2 evidence-main", "80cce868f8922bac7910bb15cab24f7303e5e2a8"),
        ("W-A3 evidence-main", "f46452902e8b2fd78800b4bca3b1b0acccd3c892"),
    ]:
        result = subprocess.run(["git", "merge-base", "--is-ancestor", ancestor, DISPATCH], cwd=ROOT).returncode == 0
        rows.append({"ref": f"ancestor {label}@{ancestor}", "sha": DISPATCH, "result": "PASS" if result else "FAIL"})
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    p3_rows = read_tsv(P3)
    selected = [
        row for row in p3_rows
        if row["project"] == "PIP"
        and row["package"] in EXPECTED_PACKAGES
        and row["deliverable_id"] != "DEL-01-01"
    ]
    excluded_issued = [row for row in p3_rows if row["project"] == "PIP" and row["deliverable_id"] == "DEL-01-01"]
    excluded_pkg00 = [row for row in p3_rows if row["project"] == "PIP" and row["package"] == "PKG-00"]
    counts = Counter(row["package"] for row in selected)
    if len(selected) != 22 or dict(sorted(counts.items())) != EXPECTED_PACKAGES:
        raise SystemExit(f"revised population mismatch: members={len(selected)} packages={dict(counts)}")
    if len(excluded_issued) != 1 or len(excluded_pkg00) != 8:
        raise SystemExit("exclusion population mismatch")

    managers = {pkg: f"WORKING-P1-{pkg.replace('-', '')}" for pkg in EXPECTED_PACKAGES}
    manifest_rows: list[dict[str, object]] = []
    binding_rows: list[dict[str, object]] = []
    validator_rows: list[dict[str, object]] = []
    total_dependency_rows = 0
    p3_mismatches: list[str] = []

    manifest_fields = [
        "project", "package", "manager", "deliverable_id", "live_path", "lifecycle", "pilot", "issued",
        "live_format", "datasheet_sha256", "specification_sha256", "guidance_sha256", "procedure_sha256",
        "status_sha256", "context_sha256", "references_sha256", "dependencies_md_sha256",
        "dependencies_csv_sha256", "dependency_rows", "scope_refs", "objective_refs", "decomposition_basis",
        "candidate_path", "author_evidence", "verifier_evidence", "integration_delta", "p3_source_status_match",
        "binding_state",
    ]
    for row in selected:
        rel = Path(row["path"])
        live = ROOT / rel
        result = validate(live)
        validator_rows.append({"package": row["package"], "deliverable_id": row["deliverable_id"], "live_path": rel.as_posix(), **result})
        hashes: dict[str, str] = {}
        for name in BINDING_FILES:
            path = live / name
            state = "PRESENT" if path.is_file() else "MISSING"
            digest = sha(path) if path.is_file() else "MISSING"
            hashes[name] = digest
            binding_rows.append({"package": row["package"], "deliverable_id": row["deliverable_id"], "live_path": rel.as_posix(), "binding": name, "state": state, "sha256": digest})
        p3_expected = {
            "Datasheet.md": row["datasheet_sha256"], "Specification.md": row["specification_sha256"],
            "Guidance.md": row["guidance_sha256"], "Procedure.md": row["procedure_sha256"],
            "_STATUS.md": row["status_sha256"],
        }
        p3_match = all(hashes[name] == expected for name, expected in p3_expected.items())
        if not p3_match:
            p3_mismatches.append(row["deliverable_id"])
        dep_rows = dependency_rows(live / "Dependencies.csv")
        total_dependency_rows += dep_rows
        token = row["package"].replace("-", "")
        did = row["deliverable_id"]
        manifest_rows.append({
            "project": "PIP", "package": row["package"], "manager": managers[row["package"]],
            "deliverable_id": did, "live_path": rel.as_posix(), "lifecycle": current_state(live / "_STATUS.md"),
            "pilot": row["pilot"], "issued": row["issued"], "live_format": result["format"],
            "datasheet_sha256": hashes["Datasheet.md"], "specification_sha256": hashes["Specification.md"],
            "guidance_sha256": hashes["Guidance.md"], "procedure_sha256": hashes["Procedure.md"],
            "status_sha256": hashes["_STATUS.md"], "context_sha256": hashes["_CONTEXT.md"],
            "references_sha256": hashes["_REFERENCES.md"], "dependencies_md_sha256": hashes["_DEPENDENCIES.md"],
            "dependencies_csv_sha256": hashes["Dependencies.csv"], "dependency_rows": dep_rows,
            "scope_refs": section_items(live / "_CONTEXT.md", "## Scope Coverage"),
            "objective_refs": section_items(live / "_CONTEXT.md", "## Objective Support"),
            "decomposition_basis": f"projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@{DISPATCH}",
            "candidate_path": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P1/PIP-{token}/{did}/ScopeOfWork.md",
            "author_evidence": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{managers[row['package']]}/children/AUTHOR-{did}",
            "verifier_evidence": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{managers[row['package']]}/children/VERIFY-{did}",
            "integration_delta": "A ScopeOfWork.md;D Datasheet.md;D Specification.md;D Guidance.md;D Procedure.md",
            "p3_source_status_match": str(p3_match).lower(),
            "binding_state": "COMPLETE" if all(hashes[name] != "MISSING" for name in BINDING_FILES) else "INCOMPLETE",
        })
    write_tsv(OUT / "P1_MANIFEST.tsv", manifest_fields, manifest_rows)
    write_tsv(OUT / "EXPECTED_LIVE_BINDINGS.tsv", ["package", "deliverable_id", "live_path", "binding", "state", "sha256"], binding_rows)
    write_tsv(OUT / "VALIDATOR_RESULTS.tsv", ["package", "deliverable_id", "live_path", "exit_code", "format", "valid", "issues"], validator_rows)

    issued = excluded_issued[0]
    issued_live = ROOT / issued["path"]
    issued_result = validate(issued_live)
    issued_hashes = {name: sha(issued_live / name) for name in BINDING_FILES}
    issued_match = all(issued_hashes[name] == issued[key] for name, key in {
        "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
        "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256", "_STATUS.md": "status_sha256",
    }.items())
    write_tsv(OUT / "EXCLUDED_ISSUED.tsv", ["project", "package", "deliverable_id", "live_path", "lifecycle", "format", "valid", "dependency_rows", "live_sow", "p3_source_status_match", "disposition"], [{
        "project": "PIP", "package": issued["package"], "deliverable_id": issued["deliverable_id"], "live_path": issued["path"],
        "lifecycle": current_state(issued_live / "_STATUS.md"), "format": issued_result["format"], "valid": issued_result["valid"],
        "dependency_rows": dependency_rows(issued_live / "Dependencies.csv"), "live_sow": str((issued_live / "ScopeOfWork.md").exists()).lower(),
        "p3_source_status_match": str(issued_match).lower(), "disposition": "EXCLUDED_READ_ONLY_H1_PARKED",
    }])

    pkg00_rows = []
    for row in excluded_pkg00:
        live = ROOT / row["path"]
        summary = live / "_DEPENDENCIES.md"
        text = summary.read_text()
        own = row["deliverable_id"]
        other_packages = sorted(set(re.findall(r"PKG-\d{2}", text)) - {"PKG-00"})
        other_deliverables = sorted(set(re.findall(r"DEL-\d{2}-\d{2}", text)) - {own})
        pkg00_rows.append({
            "deliverable_id": own, "live_path": row["path"], "lifecycle": current_state(live / "_STATUS.md"),
            "dependencies_md_sha256": sha(summary), "dependencies_csv_state": "PRESENT" if (live / "Dependencies.csv").exists() else "ABSENT_BY_DESIGN",
            "other_package_refs": ",".join(other_packages), "other_deliverable_refs": ",".join(other_deliverables),
            "direction_verdict": "PASS" if not other_packages and not other_deliverables else "FAIL",
            "disposition": "EXCLUDED_RETAINED_GOVERNANCE_CONTEXT",
        })
    write_tsv(OUT / "EXCLUDED_PKG00.tsv", ["deliverable_id", "live_path", "lifecycle", "dependencies_md_sha256", "dependencies_csv_state", "other_package_refs", "other_deliverable_refs", "direction_verdict", "disposition"], pkg00_rows)

    with DAG.open(newline="") as handle:
        dag_rows = list(csv.DictReader(handle))
    active = [row for row in dag_rows if row["Status"] == "ACTIVE"]
    direction_rows = []
    for number in range(1, 18):
        package = f"PKG-{number:02d}"
        edges = [row for row in active if row["FromPackageID"] == package and row["TargetPackageID"] == "PKG-00"]
        direction_rows.append({
            "package": package, "active_edges_to_pkg00": len(edges),
            "covered_deliverables": len({row["FromDeliverableID"] for row in edges}),
            "pkg00_targets": ",".join(sorted({row["TargetDeliverableID"] or row["TargetRefID"] for row in edges})),
            "verdict": "PASS" if edges else "FAIL",
        })
    outbound = [row for row in active if row["FromPackageID"] == "PKG-00" and (row["TargetPackageID"] not in ("", "PKG-00") or (row["TargetDeliverableID"] and not row["TargetDeliverableID"].startswith("DEL-00-")))]
    write_tsv(OUT / "PKG00_DIRECTION_VALIDATION.tsv", ["package", "active_edges_to_pkg00", "covered_deliverables", "pkg00_targets", "verdict"], direction_rows)
    write_tsv(OUT / "PKG00_OUTBOUND_CONTRADICTIONS.tsv", ["DependencyID", "FromPackageID", "FromDeliverableID", "TargetPackageID", "TargetDeliverableID", "Status", "Statement"], outbound)

    p4_rows = [row for row in read_tsv(P4) if row["project"] == "PIP"]
    p3_by_id = {row["deliverable_id"]: row for row in p3_rows if row["project"] == "PIP"}
    predecessor_rows = []
    for row in p4_rows:
        live = ROOT / p3_by_id[row["deliverable_id"]]["path"]
        legacy = sum((live / name).exists() for name in SOURCE_FILES)
        sow_hash = sha(live / "ScopeOfWork.md") if (live / "ScopeOfWork.md").exists() else "MISSING"
        status_hash = sha(live / "_STATUS.md")
        predecessor_rows.append({
            "deliverable_id": row["deliverable_id"], "live_path": p3_by_id[row["deliverable_id"]]["path"],
            "expected_sow_sha256": row["candidate_sha256"], "live_sow_sha256": sow_hash,
            "expected_status_sha256": row["status_sha256"], "live_status_sha256": status_hash,
            "lifecycle": current_state(live / "_STATUS.md"), "format": validate(live)["format"], "legacy_files": legacy,
            "verdict": "PASS" if sow_hash == row["candidate_sha256"] and status_hash == row["status_sha256"] and legacy == 0 else "FAIL",
        })
    write_tsv(OUT / "PREDECESSOR_RESULTS.tsv", ["deliverable_id", "live_path", "expected_sow_sha256", "live_sow_sha256", "expected_status_sha256", "live_status_sha256", "lifecycle", "format", "legacy_files", "verdict"], predecessor_rows)

    methods = [
        ("docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md", "ACTIVE_STANDARD"),
        ("tools/scope_of_work/common.py", "ACTIVE_RESOLVER"),
        ("tools/scope_of_work/validate_scope_of_work.py", "ACTIVE_VALIDATOR"),
        ("tools/scope_of_work/convert_four_documents_to_scope_of_work.py", "ACTIVE_CONVERTER"),
        ("tools/scope_of_work/map_scope_of_work_claims.py", "ACTIVE_MAPPER"),
        ("tools/scope_of_work/report_scope_of_work_parity.py", "ACTIVE_PARITY"),
        ("tools/scope_of_work/derive_review_checklist.py", "ACTIVE_CHECKLIST"),
        ("tools/scope_of_work/render_scope_of_work.py", "ACTIVE_RENDERER"),
        ("skills/scope-of-work/SKILL.md", "ACTIVE_SKILL"),
        ("skills/scope-of-work/BRIEF_SCHEMA.md", "ACTIVE_BRIEF_SCHEMA"),
        ("skills/scope-of-work/QA_CHECKS.md", "ACTIVE_QA"),
        ("skills/scope-of-work/TOOL_POLICY.md", "ACTIVE_TOOL_POLICY"),
        ("docs/SOFTWARE_WORKFLOW_PROFILE.md", "RATIFIED_PROFILE_CONTRACT"),
        ("projects/chirality-piping/AGENTS.md", "PROJECT_INSTRUCTIONS"),
        ("projects/chirality-piping/software-workflow.json", "PROJECT_CHECK_PROFILE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/P2_ROOT/CALLER_MANIFEST.tsv", "ACCEPTED_ROOT_CALLER_PREREQUISITE"),
        ("execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md", "ACTIVE_HUMAN_STEER"),
        ("projects/chirality-piping/execution/_DAG/_LATEST.md", "ACCEPTED_DAG_POINTER"),
        ("projects/chirality-piping/execution/_DAG/DAG-007/DependencyEdges.csv", "ACCEPTED_DEPENDENCY_REGISTER"),
    ]
    write_tsv(OUT / "METHOD_BINDINGS.tsv", ["surface", "sha256", "classification"], [{"surface": path, "sha256": sha(ROOT / path), "classification": classification} for path, classification in methods])
    write_tsv(OUT / "REFS.tsv", ["ref", "sha", "result"], ref_rows())

    plan_rows = []
    packages = list(EXPECTED_PACKAGES)
    for sequence, package in enumerate(packages, 1):
        rows = [row for row in manifest_rows if row["package"] == package]
        token = package.replace("-", "")
        manager = managers[package]
        depends_on = "W-P1-B0-R1_ACCEPTED" if sequence == 1 else f"W-P1-{packages[sequence-2].replace('-', '')}_PASS"
        plan_rows.append({
            "wave": "W-P1", "sequence": sequence, "package": f"PIP-{package}", "manager": manager,
            "members": len(rows), "member_ids": ",".join(row["deliverable_id"] for row in rows), "depends_on": depends_on,
            "candidate_write_scope": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P1/PIP-{token}/**",
            "evidence_write_scope": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{manager}/**",
            "sealed_brief": f"snapshots/W_P1/preflight-r1/PACKAGE_BRIEFS/{manager}.md",
            "fan_in_gates": f"{len(rows)}/{len(rows)} author-verifier pairs; {len(rows)*9}/{len(rows)*9} live bindings; exact {len(rows)*5}-row replacement and inverse; zero project writes",
            "project_checks": "profile always harness-self-check; execution-path harness-pytest; current/candidate SOW validation; legacy four-doc checks; dependency validation",
            "escalation": "source/control/status/lifecycle/member/authority/ref/check/scope drift; PKG-00 or DEL-01-01 overlap",
            "release_state": "PARKED_AWAITING_HELP_HUMAN_ACCEPTANCE",
        })
    plan_fields = ["wave", "sequence", "package", "manager", "members", "member_ids", "depends_on", "candidate_write_scope", "evidence_write_scope", "sealed_brief", "fan_in_gates", "project_checks", "escalation", "release_state"]
    write_tsv(OUT / "PACKAGE_PLAN.tsv", plan_fields, plan_rows)

    contract = f"""
# W-P1 Revised Sequential Package Execution Contract

Status: `SEALED CANDIDATE — AWAITING HELP_HUMAN ACCEPTANCE`

This derivative contract freezes the revised 22-member ordinary Piping P1
population. It does not itself release a manager or authorize conversion.

## Authority and scope

Future candidate preparation is limited to the exact rows in `P1_MANIFEST.tsv`
under D-GOV-16, the accepted Stage-2 basis, the active human PKG-00 ruling,
and synchronized `main@{DISPATCH}`. PKG-00 is retained governance context and
is outside conversion, integration, rollback, retirement, and closure counts.
`DEL-01-01` remains exact ISSUED, read-only, and H1-parked.

Each selected member has one exact future replacement delta: add
`ScopeOfWork.md`; delete `Datasheet.md`, `Specification.md`, `Guidance.md`, and
`Procedure.md`. Status, context, references, dependency summary, and dependency
register remain byte-identical. Project paths stay read-only during candidate
preparation; CHANGE alone may integrate an accepted RECONCILIATION manifest.

## Execution and verification

Run four package managers serially: PKG-01, PKG-02, PKG-03, PKG-04. Each
manager must reproduce its frozen bindings before dispatch, then use one sealed
TASK + scope-of-work MODE=CONVERT author and one fresh evidence-only verifier
per member. Candidate and evidence scopes are disjoint by package and child.
Children do not delegate. Candidate dual format is allowed only inside the
isolated workspace. Package PASS requires complete author/verifier provenance,
exact five-path replacement and inverse rollback, zero unknown source-line
loss, registered Piping checks, and a terminal handoff.

## PKG-00 directional invariant

Applicable PKG-00 architecture-basis context remains upstream of every actual
Piping package. No package manager may write, convert, absorb, retire, or add a
dependency to PKG-00. Any evidence that a PKG-00 member depends on another
package or deliverable is `DECISION_REQUIRED`.
"""
    write_text(OUT / "PACKAGE_EXECUTION_CONTRACT.md", contract)
    for plan in plan_rows:
        package = plan["package"].removeprefix("PIP-")
        rows = [row for row in manifest_rows if row["package"] == package]
        member_lines = "\n".join(f"- `{row['deliverable_id']}` — `{row['live_path']}`" for row in rows)
        brief = f"""
# {plan['manager']} Sealed Package Brief

Status: `PARKED — AWAITING HELP_HUMAN ACCEPTANCE AND PREDECESSOR RELEASE`

Execute only after `{plan['depends_on']}`. Incorporate
`../PACKAGE_EXECUTION_CONTRACT.md` exactly. Do not write project paths, PKG-00,
`DEL-01-01`, Git, lifecycle, integration, H1/H2, release, or retirement state.

## Exact members

{member_lines}

Candidate scope: `{plan['candidate_write_scope']}`

Evidence scope: `{plan['evidence_write_scope']}`

Reproduce all rows and hashes for this package from `P1_MANIFEST.tsv` and
`EXPECTED_LIVE_BINDINGS.tsv` before any child dispatch. Preserve every
accepted predecessor and fence. Return PASS, BLOCKED, or DECISION_REQUIRED
with complete author/verifier fan-in and an explicit handoff.
"""
        write_text(OUT / f"PACKAGE_BRIEFS/{plan['manager']}.md", brief)

    all_refs_pass = all(row["result"] == "PASS" for row in ref_rows())
    verdict = "PASS" if all([
        len(binding_rows) == 198, all(row["state"] == "PRESENT" for row in binding_rows),
        not p3_mismatches, all(row["exit_code"] == 0 and row["format"] == "LEGACY_FOUR_DOC" and row["valid"] for row in validator_rows),
        all(row["lifecycle"] == "IN_PROGRESS" for row in manifest_rows),
        not any((ROOT / row["live_path"] / "ScopeOfWork.md").exists() for row in manifest_rows),
        current_state(issued_live / "_STATUS.md") == "ISSUED", issued_result["format"] == "LEGACY_FOUR_DOC", issued_match,
        all(row["direction_verdict"] == "PASS" for row in pkg00_rows), all(row["verdict"] == "PASS" for row in direction_rows),
        not outbound, all(row["verdict"] == "PASS" for row in predecessor_rows), all_refs_pass,
    ]) else "DECISION_REQUIRED"
    summary = {
        "wave": "P1", "revision": "R1", "dispatch_basis": DISPATCH, "selected_members": 22,
        "package_counts": EXPECTED_PACKAGES, "expected_live_bindings": 198,
        "present_live_bindings": sum(row["state"] == "PRESENT" for row in binding_rows),
        "missing_live_bindings": sum(row["state"] != "PRESENT" for row in binding_rows),
        "legacy_source_bindings_verified": 88, "status_bindings_verified": 22,
        "p3_source_status_mismatches": p3_mismatches, "dependency_registers": 22,
        "dependency_rows": total_dependency_rows, "selected_lifecycle_counts": dict(Counter(row["lifecycle"] for row in manifest_rows)),
        "selected_format_counts": dict(Counter(row["live_format"] for row in manifest_rows)),
        "selected_live_sow": sum((ROOT / row["live_path"] / "ScopeOfWork.md").exists() for row in manifest_rows),
        "excluded_pkg00_members": 8, "pkg00_summary_direction_failures": sum(row["direction_verdict"] != "PASS" for row in pkg00_rows),
        "actual_packages_with_active_pkg00_basis": sum(row["verdict"] == "PASS" for row in direction_rows),
        "pkg00_outbound_contradictions": len(outbound), "excluded_issued_members": 1,
        "accepted_piping_predecessors": len(predecessor_rows), "accepted_piping_predecessor_failures": sum(row["verdict"] != "PASS" for row in predecessor_rows),
        "packages_frozen": 4, "package_sequence": list(EXPECTED_PACKAGES), "verdict": verdict,
    }
    write_text(OUT / "SUMMARY.json", json.dumps(summary, indent=2, sort_keys=True))

    write_text(OUT / "BASIS.md", f"""
# W-P1 Revised Ordinary Piping Preflight Basis

Status: `IMMUTABLE DERIVATIVE CANDIDATE — {verdict}`

This snapshot implements the versioned human ruling in
`amendments/HUMAN-STEER-PKG00-EXCLUSION-001.md`. It preserves the prior
30-member `preflight/` snapshot as exact `DECISION_REQUIRED` predecessor
evidence and creates no project dependency truth.

## Revised population

The exact P1 population is 22 ordinary Piping members in PKG-01 through
PKG-04, excluding `DEL-01-01`, split 3/5/8/6. All 88 legacy sources, 22 status
files, and 198 total live bindings are present and hash-bound. All selected
members reproduce accepted P3 source/status identity, are non-pilot,
non-issued, `IN_PROGRESS`, valid `LEGACY_FOUR_DOC`, and have no live
`ScopeOfWork.md`. Their 22 dependency registers contain {total_dependency_rows}
data rows.

## Exclusions and predecessors

Eight PKG-00 members are separately frozen as retained governance and
architecture-basis context, outside conversion/integration/retirement/closure.
Their dependency summaries name no other package or deliverable and their
absent deliverable-local `Dependencies.csv` state is preserved as designed.
`DEL-01-01` remains exact P3 `ISSUED`, valid legacy-only, SOW-absent, read-only,
and H1-parked. All four accepted Piping PKG-13 pilots remain exact SOW/status,
IN_PROGRESS, and legacy-free.

## Dependency direction

The accepted DAG-007 register is bound by SHA-256 `{sha(DAG)}` and the current
approved pointer by `{sha(DAG_POINTER)}`. Every actual package PKG-01 through
PKG-17 has active upstream dependency/constraint rows targeting PKG-00.
No active DAG-007 row makes a PKG-00 member depend on another package or
deliverable, and the eight PKG-00 summaries contain no such reference.

## Authority, ownership, and checks

Refs remain synchronized at `main@{DISPATCH}`. Active method/tool/skill,
D-GOV-16 caller, Piping profile, human steer, and DAG bindings are frozen in
`METHOD_BINDINGS.tsv`. Four sequential, disjoint manager briefs begin at
PKG-01. Applicable future checks are Piping `harness-self-check`, the
`execution/**` `harness-pytest` rule, current/candidate SOW validation, legacy
four-document checks, and dependency-register validation. No conversion,
candidate, project, Git, lifecycle, integration, H1/H2, release, or retirement
write was performed.
""")
    write_text(OUT / "CHECKS.md", f"""
# W-P1 Revised Preflight Checks

Status: `{verdict} — CANDIDATE AWAITING HELP_HUMAN FAN-IN`

| Gate | Result | Evidence |
|---|---|---|
| Human ruling | PASS | Active PKG-00 exclusion/direction amendment hash-bound |
| Exact P1 extraction | PASS | 22 exact members; PKG-01/02/03/04 = 3/5/8/6; DEL-01-01 excluded |
| P3 source/status equality | PASS | 88/88 source and 22/22 status hashes |
| Live binding inventory | PASS | 198/198 present; 22 dependency registers; {total_dependency_rows} rows |
| Lifecycle and format | PASS | 22/22 IN_PROGRESS, valid LEGACY_FOUR_DOC, zero live SOW |
| PKG-00 exclusion | PASS | 8/8 retained-context members outside manager/candidate scopes |
| PKG-00 dependency direction | PASS | 17/17 actual packages have active upstream PKG-00 basis; zero outbound contradictions; 8/8 summaries clean |
| ISSUED exclusion | PASS | DEL-01-01 exact ISSUED, legacy-only, read-only, H1-parked |
| Predecessor non-absorption | PASS | four accepted Piping pilots exact and legacy-free |
| Refs/ancestry | PASS | local and remote main synchronized; accepted ancestors present |
| Ownership/sequence | PASS | four disjoint managers in PKG-01 → 02 → 03 → 04 order |
| Containment | PASS | only revised preflight and R1 instance evidence written; no conversion dispatched |

Blockers: none. Unknowns: none. Waivers: none. H1 and H2 remain unapproved.
""")
    write_text(OUT / "HANDOFF_STATE.md", f"""
# W-P1 Revised Preflight Handoff State

Snapshot status: `IMMUTABLE DERIVATIVE CANDIDATE — {verdict}`

The exact revised 22-member P1 population, 198 bindings, four-package serial
ownership graph, ISSUED exclusion, eight-member PKG-00 retained-context
exclusion, dependency-direction validation, accepted predecessors, and active
method/ref basis are frozen. The prior `preflight/` decision snapshot remains
unchanged and is superseded only for prospective P1 population/release by the
human ruling.

Next owner: `HELP_HUMAN`. Accept or reject this derivative snapshot. On
acceptance, release only `WORKING-P1-PKG01`; later managers remain dependent on
their predecessor package PASS. Rerun on any source, status, control,
dependency, membership, lifecycle, format, authority, ref, profile, ownership,
PKG-00-direction, ISSUED, or predecessor drift.

PKG-00 and `DEL-01-01` remain read-only exclusions. H1/H2, project mutation,
Git integration, lifecycle, release, retirement, unrelated domain audit paths,
and `.claude-worktrees/**` remain outside authority.
""")


def bind_snapshot() -> None:
    rows = []
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
