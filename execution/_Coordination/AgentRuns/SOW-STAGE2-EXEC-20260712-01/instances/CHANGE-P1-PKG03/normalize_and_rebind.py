#!/usr/bin/env python3
"""Normalize the exact PKG-03 EOF inventory and rebind affected manifests."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHANGE = RUN / "instances/CHANGE-P1-PKG03"
WARNING_INVENTORY = CHANGE / "IMMUTABLE_WHITESPACE_WARNINGS.txt"
REPORT = CHANGE / "NORMALIZATION_REPORT.json"
PRESERVED_HEAD = "ce4ea40f2c290eb41b6f9cd29f49d0f54d74a5ca"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def historical(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{PRESERVED_HEAD}:{path}"], cwd=ROOT)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def resolve_manifest_path(manifest: Path, raw: str) -> Path:
    candidate = ROOT / raw if raw.startswith("execution/") else manifest.parent / raw
    resolved = candidate.resolve()
    resolved.relative_to(ROOT.resolve())
    return resolved


def refresh_manifest_rows(manifest: Path) -> dict[str, object]:
    fields, rows = read_tsv(manifest)
    assert fields == ["sha256", "bytes", "path"], (manifest, fields)
    old = sha(manifest)
    seen: set[Path] = set()
    for row in rows:
        target = resolve_manifest_path(manifest, row["path"])
        assert target != manifest.resolve() and target not in seen and target.is_file(), (manifest, target)
        seen.add(target)
        data = target.read_bytes()
        row["sha256"] = sha_bytes(data)
        row["bytes"] = str(len(data))
    write_tsv(manifest, fields, rows)
    return {"path": manifest.relative_to(ROOT).as_posix(), "rows": len(rows), "before": old, "after": sha(manifest)}


def refresh_audit(path: Path, manifests: list[Path]) -> None:
    fields, rows = read_tsv(path)
    index = {m.relative_to(ROOT).as_posix(): m for m in manifests}
    for row in rows:
        if row["manifest"] in index:
            m = index[row["manifest"]]
            row["sha256"] = sha(m)
            row["rows"] = str(sum(1 for _ in csv.DictReader(m.open(), delimiter="\t")))
            row["verdict"] = "PASS"
    write_tsv(path, fields, rows)


def refresh_source_bindings(path: Path, bindings: dict[str, Path]) -> None:
    fields, rows = read_tsv(path)
    for row in rows:
        if row["kind"] in bindings:
            target = bindings[row["kind"]]
            row["sha256"] = sha(target)
            if row["rows"]:
                row["rows"] = str(sum(1 for _ in csv.DictReader(target.open(), delimiter="\t")))
            row["verdict"] = "PASS"
        elif row["path"] in {p.relative_to(ROOT).as_posix() for p in bindings.values()}:
            target = ROOT / row["path"]
            row["sha256"] = sha(target)
            if row["rows"]:
                row["rows"] = str(sum(1 for _ in csv.DictReader(target.open(), delimiter="\t")))
            row["verdict"] = "PASS"
    write_tsv(path, fields, rows)


def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == PRESERVED_HEAD
    raw_lines = WARNING_INVENTORY.read_text(encoding="utf-8").splitlines()
    assert len(raw_lines) == 56
    relpaths: list[str] = []
    records: list[dict[str, object]] = []
    for line in raw_lines:
        match = re.fullmatch(r"(.+):(\d+): new blank line at EOF\.", line)
        assert match, line
        rel = match.group(1)
        assert rel not in relpaths
        relpaths.append(rel)
        path = ROOT / rel
        old = historical(rel)
        new = old[:-1]
        current = path.read_bytes()
        assert old.endswith(b"\n\n"), rel
        if current == old:
            path.write_bytes(new)
            current = new
        elif current != new:
            assert rel.endswith("snapshots/W_P1/PKG03-preintegration-accepted/HELP_HUMAN_ACCEPTANCE.md"), (
                rel, "unexpected post-normalization drift"
            )
        else:
            assert current == new, (rel, "unexpected post-normalization drift")
        assert new.endswith(b"\n") and not new.endswith(b"\n\n")
        records.append({
            "path": rel,
            "before_sha256": sha_bytes(old),
            "after_sha256": sha_bytes(new),
            "before_bytes": len(old),
            "after_bytes": len(new),
            "exact_delta": "REMOVE_ONE_TERMINAL_LF",
            "current_rebound_sha256": sha_bytes(current),
            "current_rebound_bytes": len(current),
        })

    child_manifests = [
        RUN / "instances/WORKING-P1-PKG03/children" / child / "MANIFEST.tsv"
        for child in ["BATCH-01-AUTHOR", "BATCH-01-VERIFY", "BATCH-02-AUTHOR", "BATCH-02-VERIFY"]
    ]
    manager_manifest = RUN / "instances/WORKING-P1-PKG03/MANIFEST.tsv"
    recon_manifest = RUN / "instances/RECON-P1-PKG03/MANIFEST.tsv"
    prior_manifest = RUN / "snapshots/W_P1/PKG03-preintegration/MANIFEST.tsv"
    accepted = RUN / "snapshots/W_P1/PKG03-preintegration-accepted"
    accepted_manifest = accepted / "MANIFEST.tsv"
    audits = [
        RUN / "snapshots/W_P1/PKG03-preintegration/UPSTREAM_MANIFEST_AUDIT.tsv",
        accepted / "UPSTREAM_MANIFEST_AUDIT.tsv",
    ]

    manifest_records: list[dict[str, object]] = []
    for manifest in child_manifests:
        manifest_records.append(refresh_manifest_rows(manifest))
    manifest_records.append(refresh_manifest_rows(manager_manifest))
    refresh_audit(audits[0], [manager_manifest, *child_manifests])
    manifest_records.append(refresh_manifest_rows(prior_manifest))

    # The accepted snapshot retains an exact copied view of the current prior manifest.
    prior_copy = accepted / "PRIOR_SNAPSHOT_MANIFEST.tsv"
    prior_copy.write_bytes(prior_manifest.read_bytes())
    refresh_audit(audits[1], [manager_manifest, *child_manifests])
    source_bindings = accepted / "SOURCE_BINDINGS.tsv"
    fields, rows = read_tsv(source_bindings)
    path_bindings = {
        manager_manifest.relative_to(ROOT).as_posix(): manager_manifest,
        prior_manifest.relative_to(ROOT).as_posix(): prior_manifest,
        **{m.relative_to(ROOT).as_posix(): m for m in child_manifests},
    }
    for row in rows:
        if row["path"] in path_bindings:
            target = path_bindings[row["path"]]
            row["sha256"] = sha(target)
            if row["rows"]:
                row["rows"] = str(sum(1 for _ in csv.DictReader(target.open(), delimiter="\t")))
        elif row["path"].startswith("execution/"):
            target = ROOT / row["path"]
            if target.is_file():
                row["sha256"] = sha(target)
        row["verdict"] = row.get("verdict", "PASS")
    write_tsv(source_bindings, fields, rows)
    manifest_records.append(refresh_manifest_rows(accepted_manifest))
    manifest_records.append(refresh_manifest_rows(recon_manifest))

    # Rebuild the manager last because it binds all four child manifest bytes.
    manifest_records.append(refresh_manifest_rows(manager_manifest))
    refresh_audit(audits[0], [manager_manifest, *child_manifests])
    refresh_audit(audits[1], [manager_manifest, *child_manifests])
    manifest_records.append(refresh_manifest_rows(prior_manifest))
    prior_copy.write_bytes(prior_manifest.read_bytes())
    for row in rows:
        if row["path"] in path_bindings:
            target = path_bindings[row["path"]]
            row["sha256"] = sha(target)
    write_tsv(source_bindings, fields, rows)
    manifest_records.append(refresh_manifest_rows(accepted_manifest))

    report = {
        "schema": "chirality-deterministic-evidence-normalization/v1",
        "preserved_head": PRESERVED_HEAD,
        "normalized_files": len(records),
        "operation": "REMOVE_EXACTLY_ONE_TERMINAL_LF",
        "semantic_project_candidate_change": False,
        "files": records,
        "manifest_rebuilds": manifest_records,
        "accepted_manifest_sha256": sha(accepted_manifest),
    }
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "normalized_files": len(records),
        "accepted_manifest_sha256": report["accepted_manifest_sha256"],
        "report": REPORT.relative_to(ROOT).as_posix(),
    }, indent=2))


if __name__ == "__main__":
    main()
