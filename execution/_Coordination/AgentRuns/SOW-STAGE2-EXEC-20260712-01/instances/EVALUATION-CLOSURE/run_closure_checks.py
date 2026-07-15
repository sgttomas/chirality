#!/usr/bin/env python3
"""Independent deterministic checks for the D-GOV-16 conversion closure."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "instances/EVALUATION-CLOSURE"
BASIS = RUN / "basis/CENSUS_MANIFEST.tsv"
VALIDATOR = ROOT / "tools/scope_of_work/validate_scope_of_work.py"
sys.path.insert(0, str(ROOT / "tools/scope_of_work"))
from finalize_scope_of_work import finalize_candidate_text  # noqa: E402

ROLLBACKS = [
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
]

HANDOFFS = [
    RUN / "snapshots/P4_PILOTS/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_A1/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_A2/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_A3/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_P1/HANDOFF_STATE.md",
    RUN / "snapshots/I0/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_P2/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_P3/integration/postmerge/HANDOFF_STATE.md",
    RUN / "snapshots/W_P4/integration/postmerge/HANDOFF_STATE.md",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    rows = list(csv.DictReader(BASIS.open(), delimiter="\t"))
    paths = sorted(row["path"] for row in rows)
    path_digest = hashlib.sha256(("\n".join(paths) + "\n").encode()).hexdigest()
    classifications: list[dict[str, str]] = []
    status_mismatches: list[str] = []
    marker_hits: list[str] = []
    repair_preview: list[dict[str, object]] = []
    lifecycle = Counter()

    for row in rows:
        directory = ROOT / row["path"]
        validator_report = json.loads(subprocess.check_output(
            ["python3", str(VALIDATOR), str(directory), "--json"], text=True
        ))
        excluded = row["project"] == "PIP" and row["package"] == "PKG-00"
        status = directory / "_STATUS.md"
        if sha(status) != row["status_sha256"]:
            status_mismatches.append(row["path"])
        lifecycle[row["lifecycle"]] += 1
        sow = directory / "ScopeOfWork.md"
        if sow.exists():
            text = sow.read_text(encoding="utf-8")
            if "migration-authority:" in text:
                marker_hits.append(rel(sow))
                production, finalization_report = finalize_candidate_text(sow, text)
                repair_preview.append({
                    "path": rel(sow),
                    "current_sha256": sha(sow),
                    "finalized_sha256": hashlib.sha256(production.encode("utf-8")).hexdigest(),
                    "source_blocks_externalized": finalization_report["source_block_count"],
                    "wording_updates": finalization_report["production_wording_update_count"],
                    "migration_authority": finalization_report["migration_control"].get("migration-authority", ""),
                })
        classifications.append({
            "project": row["project"],
            "package": row["package"],
            "deliverable_id": row["deliverable_id"],
            "path": row["path"],
            "excluded_pkg00": str(excluded).lower(),
            "format": validator_report["format"],
            "valid": str(bool(validator_report.get("valid"))).lower(),
            "lifecycle": row["lifecycle"],
            "status_hash_preserved": str(sha(status) == row["status_sha256"]).lower(),
        })

    conversion = [r for r in classifications if r["excluded_pkg00"] == "false"]
    exempt = [r for r in classifications if r["excluded_pkg00"] == "true"]

    rollback_rows: list[dict[str, str]] = []
    rollback_sources: list[dict[str, object]] = []
    for manifest in ROLLBACKS:
        with manifest.open(newline="") as handle:
            manifest_rows = list(csv.DictReader(handle, delimiter="\t"))
        rollback_sources.append({"path": rel(manifest), "rows": len(manifest_rows), "sha256": sha(manifest)})
        for row in manifest_rows:
            p = row["path"]
            rollback_rows.append({"manifest": rel(manifest), "path": p})

    rb_counter = Counter(r["path"] for r in rollback_rows)
    rb_by_dir: dict[str, list[str]] = defaultdict(list)
    for row in rollback_rows:
        rb_by_dir[str(Path(row["path"]).parent)].append(Path(row["path"]).name)
    conversion_dirs = {r["path"] for r in conversion}
    expected_names = {"ScopeOfWork.md", "Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"}
    rollback_bad_sets = {
        d: sorted(names) for d, names in rb_by_dir.items()
        if len(names) != 5 or set(names) != expected_names
    }

    project_status = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "--", "projects/chirality-app-dev", "projects/chirality-piping"],
        cwd=ROOT, text=True
    ).splitlines()
    residue = subprocess.check_output(
        ["find", "projects/chirality-app-dev", "projects/chirality-piping", "-type", "f", "(", "-name", "*.pyc", "-o", "-name", "*.pyo", ")", "-print"],
        cwd=ROOT, text=True
    ).splitlines()

    summary = {
        "schema": "chirality-conversion-closure-evaluation-checks/v1",
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "origin_main": subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip(),
        "census": {
            "total": len(classifications),
            "path_digest": path_digest,
            "expected_path_digest": "b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31",
            "lifecycle": dict(lifecycle),
            "status_hash_mismatches": status_mismatches,
        },
        "conversion_population": {
            "members": len(conversion),
            "formats": dict(Counter(r["format"] for r in conversion)),
            "invalid": sum(r["valid"] != "true" for r in conversion),
        },
        "pkg00_exemption": {
            "members": len(exempt),
            "formats": dict(Counter(r["format"] for r in exempt)),
        },
        "production_cleanliness": {
            "migration_marker_hits": marker_hits,
            "deterministic_repair_preview": {
                "members": len(repair_preview),
                "source_blocks_externalized": sum(int(r["source_blocks_externalized"]) for r in repair_preview),
                "wording_updates": sum(int(r["wording_updates"]) for r in repair_preview),
                "distinct_finalized_hashes": len({r["finalized_sha256"] for r in repair_preview}),
            },
            "project_git_status": project_status,
            "compiled_residue": residue,
        },
        "rollback": {
            "source_manifests": rollback_sources,
            "rows": len(rollback_rows),
            "unique_paths": len(rb_counter),
            "duplicate_paths": sorted(p for p, n in rb_counter.items() if n != 1),
            "deliverable_directories": len(rb_by_dir),
            "directory_set_matches_conversion_population": set(rb_by_dir) == conversion_dirs,
            "bad_five_path_sets": rollback_bad_sets,
        },
        "handoffs": {
            "required": len(HANDOFFS),
            "present": sum(p.is_file() for p in HANDOFFS),
            "bindings": [{"path": rel(p), "sha256": sha(p)} for p in HANDOFFS if p.is_file()],
        },
    }

    with (OUT / "POPULATION.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=classifications[0].keys(), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(classifications)
    with (OUT / "ROLLBACK_SOURCES.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "rows", "sha256"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rollback_sources)
    with (OUT / "REPAIR_PREVIEW.tsv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=repair_preview[0].keys(), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(repair_preview)
    (OUT / "CHECK_RESULTS.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
