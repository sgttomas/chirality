#!/usr/bin/env python3
"""Reproduce current W-A1 package manifests and the PKG01 R1-to-R2 chain."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[8]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_A1/preintegration/detailed"
SNAPSHOT = OUT.parent
EXPECTED_COUNTS = {"00": 23, "01": 40, "02": 64, "03": 62}
EXPECTED_MANIFESTS = {
    "01": "4924de97675bf8f0ad8bba606d3d5fc171d03445259a5e96eb72c5e002871f62",
}
CHECKOUT = ROOT.as_posix()
TEMP_PREFIX = "/" + "var/folders/"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    bindings: list[dict[str, str | int]] = []
    for package, expected_count in EXPECTED_COUNTS.items():
        base = RUN / f"instances/WORKING-A1-PKG{package}"
        manifest = base / "MANIFEST.tsv"
        if package in EXPECTED_MANIFESTS and sha(manifest) != EXPECTED_MANIFESTS[package]:
            raise RuntimeError(f"PKG{package} manifest identity mismatch")
        with manifest.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        if len(rows) != expected_count:
            raise RuntimeError(f"PKG{package} manifest count {len(rows)} != {expected_count}")
        for ordinal, row in enumerate(rows, 1):
            path = ROOT / row["path"]
            actual = sha(path) if path.is_file() else "MISSING"
            status = "PASS" if actual == row["sha256"] else "FAIL"
            bindings.append({
                "package": f"APP-PKG-{package}", "ordinal": ordinal, "kind": row["kind"],
                "path": row["path"], "expected_sha256": row["sha256"],
                "actual_sha256": actual, "status": status,
            })
            if status != "PASS":
                raise RuntimeError(f"binding mismatch: {row['path']}")
    if len(bindings) != 189:
        raise RuntimeError(f"current aggregate bindings {len(bindings)} != 189")

    fields = list(bindings[0])
    with (OUT / "CURRENT_PACKAGE_BINDINGS.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(bindings)

    pkg01 = RUN / "instances/WORKING-A1-PKG01"
    expected = {
        "PROJECT_CHECKS.json": {
            "pre_bytes": 45934,
            "pre_sha": "756aa875a1279526dc192b4e338f049167a7de1134f18a6478450269931972a3",
            "post_bytes": 45898,
            "post_sha": "94e56cfbc1b67b7c6c9d5da81c8aa032cd867117c9accd816a5ee97df78f035d",
            "results": 5,
        },
        "PROJECT_CHECKS_PREMERGE.json": {
            "pre_bytes": 12902,
            "pre_sha": "9ca4aac07fa13ace3794e1fe1a136a210a751519007991bc026839cd3b8a6638",
            "post_bytes": 12866,
            "post_sha": "ec6372e7a1e1de38b17580a8b8ef39e06218d71019856725c40231a89ca8f606",
            "results": 1,
        },
    }
    chain_rows: list[dict[str, str | int]] = []
    for name, proof in expected.items():
        path = pkg01 / name
        post = path.read_bytes()
        data = json.loads(post)
        if len(post) != proof["post_bytes"] or sha(path) != proof["post_sha"]:
            raise RuntimeError(f"R2 postimage mismatch: {name}")
        if data.get("workspace_root") != "~" or data.get("status") != "PASS":
            raise RuntimeError(f"R2 JSON status/portability mismatch: {name}")
        results = data.get("results", [])
        if len(results) != proof["results"] or any(row.get("status") != "PASS" or row.get("exit_code") != 0 for row in results):
            raise RuntimeError(f"R2 check result mismatch: {name}")
        token = b'"workspace_root": "~"'
        replacement = f'"workspace_root": "{CHECKOUT}"'.encode()
        if post.count(token) != 1:
            raise RuntimeError(f"R2 substitution count mismatch: {name}")
        pre = post.replace(token, replacement, 1)
        pre_sha = hashlib.sha256(pre).hexdigest()
        if len(pre) != proof["pre_bytes"] or pre_sha != proof["pre_sha"]:
            raise RuntimeError(f"R2 reverse proof mismatch: {name}")
        chain_rows.append({
            "artifact": name, "r1_post_r2_pre_bytes": len(pre),
            "r1_post_r2_pre_sha256": pre_sha, "r2_post_bytes": len(post),
            "r2_post_sha256": sha(path), "substitutions": 1,
            "json_parse": "PASS", "all_registered_results": "PASS", "reverse_proof": "PASS",
        })
    with (OUT / "PKG01_R2_CHAIN.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, list(chain_rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(chain_rows)

    # Machine-specific hits are legal only in copied source/control bytes,
    # marker-bound candidate/render bytes, or verifier fixtures copied from them.
    allowed_names = {
        "Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md",
        "Dependencies.csv", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md",
        "_STATUS.md", "ScopeOfWork.md",
    }
    portability_rows: list[dict[str, str | int]] = []
    for path in sorted(pkg01.rglob("*")):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        hits = text.count(CHECKOUT) + text.count(TEMP_PREFIX)
        if not hits:
            continue
        rel = path.relative_to(ROOT).as_posix()
        is_render = path.suffix == ".html" and "ScopeOfWork" in path.name
        is_fixture = "fixtures" in path.parts
        is_copied_or_candidate = path.name in allowed_names and "workspace" in path.parts
        if not (is_render or is_fixture or is_copied_or_candidate):
            raise RuntimeError(f"unclassified generated portability hit: {rel}")
        classification = "PRESERVED_SOURCE_LITERAL"
        portability_rows.append({"path": rel, "hits": hits, "classification": classification})
    with (OUT / "PKG01_PORTABILITY_HITS.tsv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["path", "hits", "classification"]
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(portability_rows)

    (OUT / "CURRENT_PACKAGE_FANIN.json").write_text(json.dumps({
        "schema": "chirality-w-a1-current-package-fanin/v1",
        "status": "PASS", "package_counts": EXPECTED_COUNTS,
        "aggregate_bindings": 189, "bindings_reproduced": 189,
        "historical_pre_r2_bindings": 186,
        "pkg01_r1_to_r2_chain": "PASS", "pkg01_generated_unclassified_prefixes": 0,
        "preserved_literal_files": len(portability_rows),
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest_rows = []
    for path in sorted(SNAPSHOT.rglob("*")):
        if not path.is_file() or path == SNAPSHOT / "MANIFEST.tsv":
            continue
        manifest_rows.append({
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha(path),
            "bytes": path.stat().st_size,
        })
    with (SNAPSHOT / "MANIFEST.tsv").open("w", newline="", encoding="utf-8") as handle:
        fields = ["path", "sha256", "bytes"]
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest_rows)


if __name__ == "__main__":
    main()
