#!/usr/bin/env python3
"""Fresh exact-main conversion-closure reconciliation."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


OUT = Path(__file__).resolve().parent
BASIS = "79de30d83b91a2ab468a3f17536a5233c2f85fe7"
ENTRY = "c5f5bbd6e636916a76c34a04295f6ddd2a3d0983"
PRECLEAN = "715f618e93528d626a73d2134781e8c9c27f6c90"


def basis_worktree() -> Path:
    control = OUT.parents[6]
    records = subprocess.check_output(["git", "worktree", "list", "--porcelain"], cwd=control, text=True).strip().split("\n\n")
    for record in records:
        fields = dict(line.split(" ", 1) for line in record.splitlines() if " " in line)
        if fields.get("HEAD") == BASIS:
            return Path(fields["worktree"])
    raise RuntimeError(f"no exact-basis worktree for {BASIS}")


ROOT = basis_worktree()
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
FORBIDDEN = re.compile(
    r"migration candidate|sow-source-begin|sow-source-end|migration-authority:|"
    r"pilot-variance:|issued-preparation-",
    re.IGNORECASE,
)
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
ROLLBACK_SOURCES = (
    RUN / "snapshots/P4_PILOTS/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_A1/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_A2/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_A3/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    ROOT / "execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01/snapshots/reconciliation/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_P1/PKG03-preintegration-accepted/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_P1/PKG04-preintegration-r1/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/I0/preintegration-r1/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_P2/preintegration/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_P3/preintegration/ROLLBACK_MANIFEST.tsv",
    RUN / "snapshots/W_P4/preintegration/ROLLBACK_MANIFEST.tsv",
)
HANDOFFS = (
    "snapshots/P4_PILOTS/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_A1/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_A2/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_A3/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_P1/HANDOFF_STATE.md",
    "snapshots/I0/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_P2/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_P3/integration/postmerge/HANDOFF_STATE.md",
    "snapshots/W_P4/integration/postmerge/HANDOFF_STATE.md",
)

sys.path.insert(0, str(ROOT / "tools/scope_of_work"))
from common import resolve_production_format  # noqa: E402


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def op(row: dict[str, str]) -> str:
    return {"D": "DELETE", "A": "ADD"}.get(row.get("action", row.get("operation", "")), row.get("action", row.get("operation", "")))


def content_hash(row: dict[str, str]) -> str:
    if row.get("sha256"):
        return row["sha256"]
    return row["before_sha256"] if op(row) == "DELETE" else row["after_sha256"]


def git_blob(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)


def main() -> int:
    errors: list[str] = []
    census = rows(RUN / "basis/CENSUS_MANIFEST.tsv")
    expected_paths = {r["path"] for r in census}
    actual_paths = {
        str(p.parent.relative_to(ROOT))
        for base in (ROOT / "projects/chirality-app-dev/execution", ROOT / "projects/chirality-piping/execution")
        for p in base.rglob("_STATUS.md")
    }
    if actual_paths != expected_paths:
        errors.append(f"tracked census mismatch missing={len(expected_paths-actual_paths)} extra={len(actual_paths-expected_paths)}")
    path_digest = sha(("\n".join(sorted(actual_paths)) + "\n").encode())
    if path_digest != "b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31":
        errors.append(f"census digest mismatch: {path_digest}")

    formats: Counter[str] = Counter()
    conversion_formats: Counter[str] = Counter()
    lifecycle: Counter[str] = Counter()
    residue: list[str] = []
    status_mismatches: list[str] = []
    corpus_rows: list[dict[str, str]] = []
    for member in census:
        directory = ROOT / member["path"]
        resolution = resolve_production_format(directory)
        formats[resolution.state] += 1
        excluded = member["project"] == "PIP" and member["package"] == "PKG-00"
        if not excluded:
            conversion_formats[resolution.state] += 1
        if not resolution.valid:
            errors.append(f"invalid production format {member['path']}: {resolution.issues}")
        status_hash = sha((directory / "_STATUS.md").read_bytes())
        if status_hash != member["status_sha256"]:
            status_mismatches.append(member["path"])
        lifecycle[member["lifecycle"]] += 1
        sow = directory / "ScopeOfWork.md"
        if sow.is_file() and FORBIDDEN.search(sow.read_text(encoding="utf-8")):
            residue.append(member["path"])
        corpus_rows.append({
            "project": member["project"], "package": member["package"],
            "deliverable_id": member["deliverable_id"], "path": member["path"],
            "format": resolution.state, "lifecycle": member["lifecycle"],
            "status_sha256": status_hash, "scope_of_work_sha256": sha(sow.read_bytes()) if sow.is_file() else "ABSENT",
            "conversion_member": str(not excluded).lower(),
        })
    if formats != Counter({"SOW_V1": 146, "LEGACY_FOUR_DOC": 8}):
        errors.append(f"format census mismatch: {dict(formats)}")
    if conversion_formats != Counter({"SOW_V1": 146}):
        errors.append(f"conversion format mismatch: {dict(conversion_formats)}")
    if lifecycle != Counter({"IN_PROGRESS": 153, "ISSUED": 1}):
        errors.append(f"lifecycle mismatch: {dict(lifecycle)}")
    issued = [r["path"] for r in census if r["lifecycle"] == "ISSUED"]
    if issued != ["projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline"]:
        errors.append(f"sole issued identity mismatch: {issued}")
    if residue:
        errors.append(f"migration-only residue remains in {len(residue)} members")
    if status_mismatches:
        errors.append(f"status hash mismatch in {len(status_mismatches)} members")

    changed = subprocess.check_output(
        ["git", "diff", "--name-only", ENTRY, BASIS, "--", *sorted(expected_paths)],
        cwd=ROOT, text=True,
    ).splitlines()
    allowed_names = {"ScopeOfWork.md", *LEGACY}
    control_drift = [p for p in changed if Path(p).name not in allowed_names]
    if control_drift:
        errors.append(f"status/control/dependency drift paths: {control_drift}")

    repair_path = RUN / "snapshots/CONVERSION_CLOSURE/repair_preintegration/PROPOSED_CHANGE_MANIFEST.tsv"
    repair_rows = rows(repair_path)
    repair = {r["path"]: r for r in repair_rows}
    if len(repair) != 57:
        errors.append(f"clean-repair manifest population {len(repair)}, expected 57")
    reproduction_errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="recon-finalizer-") as raw:
        tmp = Path(raw)
        for index, row in enumerate(repair_rows):
            path = row["path"]
            before = git_blob(PRECLEAN, path)
            current = (ROOT / path).read_bytes()
            if sha(before) != row["before_sha256"] or sha(current) != row["after_sha256"]:
                reproduction_errors.append(f"repair endpoint mismatch: {path}")
                continue
            candidate, output, report = tmp / f"c{index}.md", tmp / f"o{index}.md", tmp / f"r{index}.json"
            candidate.write_bytes(before)
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tools/scope_of_work/finalize_scope_of_work.py"),
                 "--evidence-candidate", str(candidate), "--output", str(output), "--report", str(report)],
                cwd=ROOT, capture_output=True, text=True,
            )
            if proc.returncode or output.read_bytes() != current or sha(report.read_bytes()) != row["finalization_report_sha256"]:
                reproduction_errors.append(f"finalizer reproduction mismatch: {path}")
    if reproduction_errors:
        errors.extend(reproduction_errors)

    rollback_by_dir: dict[str, list[dict[str, str]]] = defaultdict(list)
    rollback_source_rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for source in ROLLBACK_SOURCES:
        source_data = rows(source)
        rollback_source_rows.append({"path": str(source.relative_to(ROOT)), "rows": str(len(source_data)), "sha256": sha(source.read_bytes())})
        for row in source_data:
            if row["path"] in seen:
                errors.append(f"duplicate rollback path: {row['path']}")
            seen.add(row["path"])
            rollback_by_dir[str(Path(row["path"]).parent)].append(row)
    conversion = {r["path"]: r for r in census if not (r["project"] == "PIP" and r["package"] == "PKG-00")}
    simulation_errors: list[str] = []
    for directory, member in conversion.items():
        manifest_rows = rollback_by_dir.get(directory, [])
        if len(manifest_rows) != 5 or {Path(r["path"]).name for r in manifest_rows} != {"ScopeOfWork.md", *LEGACY}:
            simulation_errors.append(f"bad five-path inverse: {directory}")
            continue
        state = {name: (sha((ROOT / directory / name).read_bytes()) if (ROOT / directory / name).is_file() else None) for name in ("ScopeOfWork.md", *LEGACY)}
        initial = dict(state)
        sow_path = f"{directory}/ScopeOfWork.md"
        if sow_path in repair:
            rr = repair[sow_path]
            if state["ScopeOfWork.md"] != rr["after_sha256"]:
                simulation_errors.append(f"clean inverse precondition: {directory}")
                continue
            state["ScopeOfWork.md"] = rr["before_sha256"]
        for row in manifest_rows:
            name, operation, expected = Path(row["path"]).name, op(row), content_hash(row)
            if operation == "DELETE":
                if state[name] != expected:
                    simulation_errors.append(f"rollback delete precondition: {row['path']}")
                state[name] = None
            elif operation in {"ADD", "RESTORE"}:
                if state[name] is not None:
                    simulation_errors.append(f"rollback restore collision: {row['path']}")
                state[name] = expected
            else:
                simulation_errors.append(f"unknown rollback operation {operation}: {row['path']}")
        expected_legacy = {name: member[name.lower().replace('.md', '') + "_sha256"] for name in LEGACY}
        if state["ScopeOfWork.md"] is not None or any(state[name] != expected_legacy[name] for name in LEGACY):
            simulation_errors.append(f"legacy endpoint mismatch: {directory}")
        # Reverse the five-row inverse, then reapply deterministic cleanup where applicable.
        for row in reversed(manifest_rows):
            name, operation, expected = Path(row["path"]).name, op(row), content_hash(row)
            if operation == "DELETE":
                if state[name] is not None:
                    simulation_errors.append(f"forward add collision: {row['path']}")
                state[name] = expected
            else:
                if state[name] != expected:
                    simulation_errors.append(f"forward delete precondition: {row['path']}")
                state[name] = None
        if sow_path in repair:
            rr = repair[sow_path]
            if state["ScopeOfWork.md"] != rr["before_sha256"]:
                simulation_errors.append(f"clean forward precondition: {directory}")
            state["ScopeOfWork.md"] = rr["after_sha256"]
        if state != initial:
            simulation_errors.append(f"round-trip mismatch: {directory}")
    if len(seen) != 730 or set(rollback_by_dir) != set(conversion):
        errors.append(f"rollback coverage rows={len(seen)} members={len(rollback_by_dir)}")
    if simulation_errors:
        errors.extend(simulation_errors)

    callers = rows(RUN / "basis/CALLER_MANIFEST.tsv")
    caller_rows: list[dict[str, str]] = []
    exact_callers = [r for r in callers if r["coverage"] == "EXACT_PATH"]
    for row in exact_callers:
        target = ROOT / row["surface"]
        if not target.is_file():
            errors.append(f"missing caller surface: {row['surface']}")
            current_hash = "ABSENT"
        else:
            current_hash = sha(target.read_bytes())
        caller_rows.append({"surface": row["surface"], "disposition": row["disposition"], "exists": str(target.is_file()).lower(), "current_sha256": current_hash})
    retained = [r for r in exact_callers if r["disposition"] == "RETAIN_LEGACY"]
    if len(retained) != 5:
        errors.append(f"retained compatibility surface count {len(retained)}, expected 5")
    dispositions = Counter(r["disposition"] for r in callers)
    if dispositions != Counter({"ACTIVATE": 58, "RETAIN_LEGACY": 5, "HISTORICAL": 5, "INDEPENDENT_SCHEMA": 3, "DERIVATIVE_REGENERATE": 1}):
        errors.append(f"caller classification mismatch: {dict(dispositions)}")
    handoff_rows = []
    for relative in HANDOFFS:
        path = RUN / relative
        if not path.is_file(): errors.append(f"missing accepted integration handoff: {relative}")
        else: handoff_rows.append({"path": str(path.relative_to(ROOT)), "sha256": sha(path.read_bytes())})
    receipt_text = (ROOT / "execution/_Coordination/LOOP_RECEIPTS.md").read_text(encoding="utf-8")
    receipts = {int(n) for n in re.findall(r"^### Receipt (\d+) —", receipt_text, re.MULTILINE)}
    if not set(range(1, 24)).issubset(receipts):
        errors.append(f"missing Stage-2 receipt(s): {sorted(set(range(1,24))-receipts)}")
    graph = json.loads((RUN / "WORK_GRAPH.json").read_text())
    gate_by_id = {g["id"]: g for g in graph["human_gates"]}
    node_by_id = {n["id"]: n for n in graph["nodes"]}
    if gate_by_id.get("H2", {}).get("state") != "UNAPPROVED" or node_by_id.get("LEGACY_RETIREMENT", {}).get("status") != "PARKED_HUMAN_GATE":
        errors.append("H2 or legacy-retirement fence is not parked")

    def write_tsv(path: Path, data: list[dict[str, str]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(data[0]), delimiter="\t", lineterminator="\n")
            writer.writeheader(); writer.writerows(data)

    write_tsv(OUT / "CORPUS.tsv", corpus_rows)
    write_tsv(OUT / "ROLLBACK_SOURCES.tsv", rollback_source_rows)
    write_tsv(OUT / "CALLER_AUDIT.tsv", caller_rows)
    write_tsv(OUT / "HANDOFFS.tsv", handoff_rows)
    result = {
        "schema": "chirality-conversion-closure-final-reconciliation/v1", "basis": BASIS,
        "verdict": "PASS" if not errors else "BLOCKED", "errors": errors,
        "census": {"members": len(census), "path_digest": path_digest, "formats": dict(formats), "conversion_formats": dict(conversion_formats), "lifecycle": dict(lifecycle), "sole_issued": issued, "status_mismatches": status_mismatches, "control_drift": control_drift},
        "clean_production": {"forbidden_residue_members": residue, "repair_members_reproduced": len(repair_rows) - len(reproduction_errors), "repair_manifest_sha256": sha(repair_path.read_bytes())},
        "rollback": {"sources": len(ROLLBACK_SOURCES), "rows": len(seen), "members": len(rollback_by_dir), "round_trip_simulations_passed": len(conversion) - len({e.split(': ',1)[-1] for e in simulation_errors}), "simulation_errors": simulation_errors},
        "callers": {"exact_surfaces": len(exact_callers), "retained_legacy_surfaces": len(retained), "dispositions": dict(dispositions)},
        "integration_evidence": {"accepted_handoffs": len(handoff_rows), "receipts_1_through_23_present": set(range(1,24)).issubset(receipts)},
        "fences": {"h2": gate_by_id.get("H2", {}).get("state"), "legacy_retirement": node_by_id.get("LEGACY_RETIREMENT", {}).get("status")},
    }
    (OUT / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
