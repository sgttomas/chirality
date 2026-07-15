#!/usr/bin/env python3
"""Reproduce Stage-2 conversion and rollback closure on the checked-out source state."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "instances/RECON-CLOSURE/evidence"
SCOPE_TOOLS = ROOT / "tools/scope_of_work"
sys.path.insert(0, str(SCOPE_TOOLS))
from common import resolve_production_format  # noqa: E402

LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
EXPECTED_DIGEST = "b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31"
FROZEN_BASIS_COMMIT = "c5f5bbd6e636916a76c34a04295f6ddd2a3d0983"
CONTROL_FILES = ("_STATUS.md", "_CONTEXT.md", "_DEPENDENCIES.md", "_REFERENCES.md", "Dependencies.csv")

GROUPS = {
    "P4_PILOTS": RUN / "snapshots/P4_PILOTS/preintegration-r1",
    "W_A1": RUN / "snapshots/W_A1/integration/postmerge",
    "W_A2": RUN / "snapshots/W_A2/integration/postmerge",
    "W_A3": RUN / "snapshots/W_A3/integration/postmerge",
    "W_P1_PKG03": RUN / "snapshots/W_P1/PKG03-preintegration-accepted",
    "W_P1_PKG04": RUN / "snapshots/W_P1/PKG04-preintegration-r1",
    "I0_ISSUED": RUN / "snapshots/I0/preintegration-r1",
    "PACKAGE_BATCH_ADOPTION": ROOT / "execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01/snapshots/reconciliation",
    "W_P2": RUN / "snapshots/W_P2/preintegration",
    "W_P3": RUN / "snapshots/W_P3/preintegration",
    "W_P4": RUN / "snapshots/W_P4/preintegration",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def action(row: dict[str, str]) -> str:
    raw = row.get("action") or row.get("operation") or ""
    return {"A": "ADD", "D": "DELETE", "RESTORE": "ADD"}.get(raw, raw)


def transition(row: dict[str, str]) -> tuple[str, str, str, str]:
    act = action(row)
    before = row.get("before_sha256", "")
    after = row.get("after_sha256", "")
    content = row.get("sha256", "")
    if not before and not after:
        before, after = ("ABSENT", content) if act == "ADD" else (content, "ABSENT")
    return row["path"], act, before, after


def git(*args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, check=True)
    return proc.stdout.strip()


def audit_census() -> tuple[list[dict[str, object]], dict[str, object], list[str]]:
    basis = rows(RUN / "basis/CENSUS_MANIFEST.tsv")
    errors: list[str] = []
    output: list[dict[str, object]] = []
    formats: Counter[str] = Counter()
    lifecycles: Counter[str] = Counter()
    conversion_formats: Counter[str] = Counter()
    current_paths: list[str] = []
    metadata_hits = 0
    status_drift = 0

    for old in basis:
        rel = old["path"]
        directory = ROOT / rel
        current_paths.append(rel)
        resolution = resolve_production_format(directory)
        formats[resolution.state] += 1
        excluded = old["project"] == "PIP" and old["package"] == "PKG-00"
        if not excluded:
            conversion_formats[resolution.state] += 1
        status = directory / "_STATUS.md"
        status_hash = sha(status) if status.is_file() else "MISSING"
        if status_hash != old["status_sha256"]:
            status_drift += 1
            errors.append(f"status drift: {rel}")
        text = status.read_text(encoding="utf-8") if status.is_file() else ""
        match = re.search(r"\*\*Current State:\*\*\s*([^\n]+)", text)
        lifecycle = match.group(1).strip() if match else "UNKNOWN"
        lifecycles[lifecycle] += 1
        sow = directory / "ScopeOfWork.md"
        found: list[str] = []
        if sow.is_file():
            sow_text = sow.read_text(encoding="utf-8")
            found = [
                token for token in (
                    "migration-authority:", "candidate-compound-id:",
                    "sow-source-begin", "sow-source-end", "issued-preparation-",
                    "evidence-candidate", "migration candidate"
                ) if token in sow_text
            ]
            metadata_hits += len(found)
            if found:
                errors.append(f"candidate metadata in production: {rel}: {','.join(found)}")
        if not resolution.valid:
            errors.append(f"invalid format {resolution.state}: {rel}: {'; '.join(resolution.issues)}")
        output.append({
            "project": old["project"], "package": old["package"],
            "deliverable_id": old["deliverable_id"], "path": rel,
            "excluded_upstream_context": excluded, "format": resolution.state,
            "format_valid": resolution.valid, "lifecycle": lifecycle,
            "status_sha256": status_hash, "status_matches_frozen_basis": status_hash == old["status_sha256"],
            "sow_sha256": sha(sow) if sow.is_file() else "ABSENT",
            "legacy_files_present": sum((directory / name).is_file() for name in LEGACY),
            "candidate_residue": ",".join(found),
        })

    digest = hashlib.sha256(("\n".join(sorted(current_paths)) + "\n").encode()).hexdigest()
    if len(basis) != 154: errors.append(f"census count {len(basis)} != 154")
    if digest != EXPECTED_DIGEST: errors.append(f"membership digest {digest} != {EXPECTED_DIGEST}")
    if conversion_formats != Counter({"SOW_V1": 146}): errors.append(f"conversion formats {dict(conversion_formats)}")
    if formats != Counter({"SOW_V1": 146, "LEGACY_FOUR_DOC": 8}): errors.append(f"tracked formats {dict(formats)}")
    if lifecycles != Counter({"IN_PROGRESS": 153, "ISSUED": 1}): errors.append(f"lifecycle counts {dict(lifecycles)}")
    issued = [r for r in output if r["lifecycle"] == "ISSUED"]
    if len(issued) != 1 or issued[0]["project"] != "PIP" or issued[0]["deliverable_id"] != "DEL-01-01":
        errors.append(f"issued identity mismatch: {[(r['project'], r['deliverable_id']) for r in issued]}")
    summary = {
        "tracked_members": len(basis), "membership_digest": digest,
        "formats": dict(formats), "conversion_population": 146,
        "conversion_formats": dict(conversion_formats), "excluded_members": 8,
        "lifecycles": dict(lifecycles), "status_drift": status_drift,
        "candidate_metadata_hits": metadata_hits,
    }
    return output, summary, errors


def audit_manifests() -> tuple[list[dict[str, object]], dict[str, object], list[str]]:
    details: list[dict[str, object]] = []
    errors: list[str] = []
    member_owners: dict[str, str] = {}
    all_paths: set[str] = set()
    total_rows = 0
    simulated = 0
    for name, base in GROUPS.items():
        forward_file = base / "REPLACEMENT_MANIFEST.tsv"
        rollback_file = base / "ROLLBACK_MANIFEST.tsv"
        if not forward_file.is_file() or not rollback_file.is_file():
            errors.append(f"missing manifest pair: {name}")
            continue
        forward = [transition(r) for r in rows(forward_file)]
        rollback = [transition(r) for r in rows(rollback_file)]
        total_rows += len(forward)
        if len(forward) != len(rollback): errors.append(f"row count mismatch: {name}")
        f_by_path = {r[0]: r for r in forward}
        r_by_path = {r[0]: r for r in rollback}
        if len(f_by_path) != len(forward): errors.append(f"duplicate forward path: {name}")
        if len(r_by_path) != len(rollback): errors.append(f"duplicate rollback path: {name}")
        if set(f_by_path) != set(r_by_path): errors.append(f"forward/rollback path mismatch: {name}")
        group_members: set[str] = set()
        live_ok = inverse_ok = True
        for path, act, before, after in forward:
            if path in all_paths: errors.append(f"cross-group duplicate path: {path}")
            all_paths.add(path)
            member = str(Path(path).parent)
            group_members.add(member)
            owner = member_owners.setdefault(member, name)
            if owner != name: errors.append(f"member owned by {owner} and {name}: {member}")
            live = ROOT / path
            observed = sha(live) if live.is_file() else "ABSENT"
            if observed != after:
                live_ok = False
                errors.append(f"live target mismatch: {name}: {path}: {observed} != {after}")
            reverse = r_by_path.get(path)
            if reverse is None or reverse[1] != ("DELETE" if act == "ADD" else "ADD") or reverse[2] != after or reverse[3] != before:
                inverse_ok = False
                errors.append(f"non-inverse rollback: {name}: {path}")
        if len(forward) != 5 * len(group_members): errors.append(f"non-atomic five-row population: {name}")
        # Deterministic state-machine simulation: apply then inverse for each member.
        for member in group_members:
            frows = [r for r in forward if str(Path(r[0]).parent) == member]
            state = {p: before for p, _, before, _ in frows}
            for p, _, before, after in frows:
                if state[p] != before: errors.append(f"apply precondition mismatch: {name}: {p}")
                state[p] = after
            for p, _, before, after in (r_by_path[r[0]] for r in frows):
                if state[p] != before: errors.append(f"rollback precondition mismatch: {name}: {p}")
                state[p] = after
            if any(state[p] != before for p, _, before, _ in frows):
                errors.append(f"simulation failed: {name}: {member}")
            else:
                simulated += 1
        details.append({
            "group": name, "forward_manifest": str(forward_file.relative_to(ROOT)),
            "rollback_manifest": str(rollback_file.relative_to(ROOT)),
            "members": len(group_members), "forward_rows": len(forward),
            "rollback_rows": len(rollback), "current_hashes_exact": live_ok,
            "exact_inverse": inverse_ok, "simulations": len(group_members),
        })
    if len(member_owners) != 146: errors.append(f"manifest member coverage {len(member_owners)} != 146")
    if total_rows != 730: errors.append(f"forward row coverage {total_rows} != 730")
    if simulated != 146: errors.append(f"simulation coverage {simulated} != 146")
    summary = {"groups": len(details), "members": len(member_owners), "forward_rows": total_rows,
               "unique_paths": len(all_paths), "simulations": simulated}
    return details, summary, errors


def audit_callers() -> tuple[list[dict[str, object]], dict[str, object], list[str]]:
    manifest = rows(RUN / "basis/CALLER_MANIFEST.tsv")
    details: list[dict[str, object]] = []
    errors: list[str] = []
    dispositions = Counter()
    for row in manifest:
        surface = row["surface"]
        dispositions[row["disposition"]] += 1
        if surface.startswith("@aggregate:"):
            continue
        path = ROOT / surface
        exists = path.is_file()
        if not exists: errors.append(f"classified caller missing: {surface}")
        text = path.read_text(encoding="utf-8", errors="replace") if exists else ""
        details.append({"surface": surface, "disposition": row["disposition"], "exists": exists,
                        "current_sha256": sha(path) if exists else "MISSING",
                        "mentions_scope_of_work": "ScopeOfWork" in text or "scope-of-work" in text,
                        "mentions_legacy": any(t in text for t in ("four-documents", "Datasheet.md", "LEGACY_FOUR_DOC"))})
    retained = [d for d in details if d["disposition"] == "RETAIN_LEGACY"]
    if len(retained) != 5 or not all(d["exists"] for d in retained):
        errors.append(f"retained legacy caller population invalid: {len(retained)}")
    activated = [d for d in details if d["disposition"] == "ACTIVATE"]
    if not all(d["exists"] for d in activated): errors.append("one or more activated callers missing")
    summary = {"manifest_rows": len(manifest), "exact_surfaces": len(details),
               "aggregate_rows": len(manifest) - len(details), "dispositions": dict(dispositions),
               "retained_legacy": len(retained), "activated": len(activated)}
    return details, summary, errors


def audit_controls(census: list[dict[str, object]]) -> tuple[list[dict[str, object]], dict[str, object], list[str]]:
    details: list[dict[str, object]] = []
    errors: list[str] = []
    for member in census:
        for filename in CONTROL_FILES:
            rel = f"{member['path']}/{filename}"
            current = ROOT / rel
            proc = subprocess.run(["git", "show", f"{FROZEN_BASIS_COMMIT}:{rel}"], cwd=ROOT, capture_output=True)
            before = hashlib.sha256(proc.stdout).hexdigest() if proc.returncode == 0 else "ABSENT"
            after = sha(current) if current.is_file() else "ABSENT"
            matches = before == after
            if not matches: errors.append(f"control drift: {rel}: {before} != {after}")
            details.append({"path": rel, "basis_sha256": before, "current_sha256": after, "matches": matches})
    summary = {"rows": len(details), "matching": sum(bool(r["matches"]) for r in details),
               "drift": sum(not bool(r["matches"]) for r in details), "basis_commit": FROZEN_BASIS_COMMIT}
    return details, summary, errors


def write_tsv(path: Path, records: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not records:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader(); writer.writerows(records)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    census, census_summary, census_errors = audit_census()
    manifests, manifest_summary, manifest_errors = audit_manifests()
    callers, caller_summary, caller_errors = audit_callers()
    controls, control_summary, control_errors = audit_controls(census)
    errors = census_errors + manifest_errors + caller_errors + control_errors
    report = {
        "schema": "chirality-sow-closure-reconciliation/v1",
        "source_head": git("rev-parse", "HEAD"),
        "source_tree": git("rev-parse", "HEAD^{tree}"),
        "census": census_summary, "manifests": manifest_summary, "callers": caller_summary,
        "controls": control_summary,
        "retirement_implemented": False, "h2_approved": False, "rollback_executed": False,
        "verdict": "PASS" if not errors else "BLOCKED", "errors": errors,
    }
    write_tsv(OUT / "CENSUS.tsv", census)
    write_tsv(OUT / "CANDIDATE_RESIDUE.tsv", [r for r in census if r["candidate_residue"]])
    write_tsv(OUT / "MANIFEST_AUDIT.tsv", manifests)
    write_tsv(OUT / "CALLER_AUDIT.tsv", callers)
    write_tsv(OUT / "CONTROL_PRESERVATION.tsv", controls)
    (OUT / "RECONCILIATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
