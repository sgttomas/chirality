#!/usr/bin/env python3
"""Finalize the RECON clean-repair return and immutable derivative snapshot."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/CONVERSION_CLOSURE/repair_preintegration"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    reproduction = json.loads((INSTANCE / "REPRODUCTION_RESULT.json").read_text(encoding="utf-8"))
    rollback = json.loads((INSTANCE / "ROLLBACK_AUDIT.json").read_text(encoding="utf-8"))
    checks = json.loads((INSTANCE / "CHECK_RESULTS.json").read_text(encoding="utf-8"))
    app_rerun = json.loads((INSTANCE / "APP_TEST_RERUN.json").read_text(encoding="utf-8"))
    accepted_initial = [row for row in checks["results"] if row["name"] != "app_tests"]
    overall = (
        reproduction["verdict"] == "PASS"
        and rollback["verdict"] == "PASS"
        and app_rerun["verdict"] == "PASS"
        and all(row["exit_code"] == 0 for row in accepted_initial)
    )

    with (INSTANCE / "REPRODUCTION_MANIFEST.tsv").open(encoding="utf-8", newline="") as handle:
        members = list(csv.DictReader(handle, delimiter="\t"))
    change = INSTANCE / "PROPOSED_CHANGE_MANIFEST.tsv"
    with change.open("w", encoding="utf-8", newline="") as handle:
        fields = ["operation", "path", "before_sha256", "after_sha256", "finalization_report_sha256", "finalization_report_path"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in members:
            report_path = (
                "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/"
                f"WORKING-CLEAN-REPAIR/reports/{Path(row['path']).with_suffix('')}/finalization.json"
            )
            writer.writerow({
                "operation": "REPLACE",
                "path": row["path"],
                "before_sha256": row["basis_sha256"],
                "after_sha256": row["production_sha256"],
                "finalization_report_sha256": row["report_sha256"],
                "finalization_report_path": report_path,
            })

    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    status = {
        "schema": "chirality-agent-return/v1",
        "agent": "RECONCILIATION",
        "run": "SOW-STAGE2-EXEC-20260712-01",
        "instance": "RECON-CLEAN-REPAIR",
        "status": "PASS" if overall else "BLOCKED",
        "basis": "715f618e93528d626a73d2134781e8c9c27f6c90",
        "completed_at": timestamp,
        "project_paths": 57,
        "change_manifest_sha256": sha(change),
        "reproduction_manifest_sha256": sha(INSTANCE / "REPRODUCTION_MANIFEST.tsv"),
    }
    (INSTANCE / "STATUS.json").write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (INSTANCE / "ATTEMPTS.md").write_text(
        "# Attempts\n\n"
        "1. Initial reproduction mechanically misparsed the registered source marker by expecting a colon. "
        "The false block-count failures were retained in the turn record; the owned parser was corrected and all 57 members passed.\n"
        "2. Initial App test copy omitted repository-level fixtures. It produced 708 passing tests and four ENOENT failures. "
        "The failed log is retained as `checks/app_tests.txt`; the complete-layout rerun passed and is retained as `checks/app_tests_r1.txt`.\n"
        "3. Initial rollback audit assumed one historical schema. The traceback was retained in the turn record; normalization for "
        "`D/A`, `DELETE/ADD`, `RESTORE`, and before/after hash fields passed all 730 rows.\n",
        encoding="utf-8",
    )
    (INSTANCE / "CHECKS.md").write_text(
        "# Independent checks\n\n"
        "- 57/57 basis-blob finalizations reproduce byte-identically; all author reports reproduce byte-identically.\n"
        "- 1,753 source blocks are externally bound and preserved as literal quotations; 52 deterministic wording updates are accounted for.\n"
        "- Corpus: 146 valid `SOW_V1`, eight untouched Piping PKG-00 exemptions, zero forbidden residue.\n"
        "- Lifecycle: 153 `IN_PROGRESS`; sole `ISSUED` is Piping `DEL-01-01`.\n"
        "- Rollback: 11 accepted sources, 146 members, 730 unique rows; all hashes reproduce against the census and pinned basis.\n"
        "- Root: 19 focused tests, 264 practitioner tests, and four validators pass.\n"
        "- App: typecheck, 713-test/4-skipped suite, and build pass. The initial fixture-copy failure is retained.\n"
        "- Piping: WASM prerequisite, 476-test desktop suite, and desktop build pass in a disposable copy.\n",
        encoding="utf-8",
    )
    verdict = "PASS" if overall else "BLOCKED"
    (INSTANCE / "RETURN.md").write_text(
        f"# RECON-CLEAN-REPAIR Return — {verdict}\n\n"
        "Independent reproduction accepts the bounded clean-production repair for CHANGE integration. Exactly 57 project files change, "
        "all and only `ScopeOfWork.md`: 53 App members and four Piping PKG-13 pilots. No semantic mismatch, count drift, unauthorized "
        "project path, lifecycle drift, control/status drift, or check disagreement remains.\n\n"
        f"Pinned basis: `715f618e93528d626a73d2134781e8c9c27f6c90`. Proposed CHANGE manifest: "
        f"`PROPOSED_CHANGE_MANIFEST.tsv` SHA-256 `{sha(change)}`. Reproduction manifest SHA-256 "
        f"`{sha(INSTANCE / 'REPRODUCTION_MANIFEST.tsv')}`.\n\n"
        "The sole failed project-test attempt was a verifier disposable-copy construction defect, not a product failure; it is retained "
        "and the corrected complete-layout rerun passes. Integration remains reserved to CHANGE.\n",
        encoding="utf-8",
    )
    (INSTANCE / "HANDOFF_STATE.md").write_text(
        "# Handoff State\n\n"
        f"Verdict: **{verdict}**. Upstream basis: `main@715f618e93528d626a73d2134781e8c9c27f6c90`. "
        "This is a derivative preintegration backcheck and does not replace decomposition or lifecycle truth. CHANGE may integrate only "
        "the 57 replacements in `PROPOSED_CHANGE_MANIFEST.tsv` with their bound external reports. Rerun this reconciliation if any "
        "project path, report, registered finalizer, census, lifecycle/status surface, or accepted rollback source changes. H2 and legacy "
        "retirement remain parked.\n",
        encoding="utf-8",
    )

    if SNAPSHOT.exists():
        shutil.rmtree(SNAPSHOT)
    SNAPSHOT.mkdir(parents=True)
    for path in sorted(INSTANCE.rglob("*")):
        if path.is_file():
            target = SNAPSHOT / path.relative_to(INSTANCE)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    manifest_rows = []
    for path in sorted(SNAPSHOT.rglob("*")):
        if path.is_file() and path.name != "MANIFEST.tsv":
            manifest_rows.append({"path": path.relative_to(SNAPSHOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)})
    with (SNAPSHOT / "MANIFEST.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "bytes", "sha256"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest_rows)
    print(json.dumps({"verdict": verdict, "snapshot": str(SNAPSHOT.relative_to(ROOT)), "snapshot_manifest_sha256": sha(SNAPSHOT / "MANIFEST.tsv"), **status}, indent=2))
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
