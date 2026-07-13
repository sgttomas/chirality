#!/usr/bin/env python3
"""Normalize generated machine paths and rebind child manifests deterministically."""

from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import tempfile
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


repo = Path(
    subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
)
manager = Path(__file__).resolve().parent
repo_literal = str(repo)
tmp_literal = tempfile.gettempdir()
immutable_names = {
    "Datasheet.md",
    "Specification.md",
    "Guidance.md",
    "Procedure.md",
    "Dependencies.csv",
    "_STATUS.md",
    "_CONTEXT.md",
    "_REFERENCES.md",
    "_DEPENDENCIES.md",
    "_SEMANTIC.md",
    "_SEMANTIC_LENSING.md",
}

normalization_rows: list[list[str]] = []
preserved_rows: list[list[str]] = []
changed: set[Path] = set()

for path in sorted(p for p in manager.rglob("*") if p.is_file()):
    if path.name in {"MANIFEST.tsv", "PATH_NORMALIZATION.tsv", "MANIFEST_REBIND.tsv", "PRESERVED_SOURCE_LITERAL_INVENTORY.tsv"}:
        continue
    try:
        original = path.read_text()
    except UnicodeDecodeError:
        continue
    repo_count = original.count(repo_literal)
    tmp_count = original.count(tmp_literal)
    if not repo_count and not tmp_count:
        continue
    rel = path.relative_to(repo).as_posix()
    if path.name in immutable_names:
        preserved_rows.append([rel, str(repo_count), str(tmp_count), "IMMUTABLE_COPIED_SOURCE_OR_CONTROL"])
        continue
    normalized = original.replace(repo_literal, "{REPO_ROOT}")
    normalized = normalized.replace(tmp_literal, "{TMPDIR}")
    restored = normalized.replace("{REPO_ROOT}", repo_literal)
    restored = restored.replace("{TMPDIR}", tmp_literal)
    reverse_ok = restored == original
    if not reverse_ok:
        raise SystemExit(f"reverse proof failed: {rel}")
    before_sha = hashlib.sha256(original.encode()).hexdigest()
    before_bytes = len(original.encode())
    path.write_text(normalized)
    after_sha = digest(path)
    after_bytes = path.stat().st_size
    normalization_rows.append(
        [rel, before_sha, str(before_bytes), after_sha, str(after_bytes), str(repo_count), str(tmp_count), "true"]
    )
    changed.add(path.resolve())

rebind_rows: list[list[str]] = []
for manifest in sorted(manager.glob("children/*/MANIFEST.tsv")):
    child = manifest.parent
    before_sha = digest(manifest)
    before_bytes = manifest.stat().st_size
    with manifest.open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = reader.fieldnames
        if not fields:
            raise SystemExit(f"manifest has no header: {manifest}")
        rows = list(reader)
    path_key = next((x for x in fields if x.lower() == "path"), None)
    sha_key = next((x for x in fields if x.lower() == "sha256"), None)
    bytes_key = next((x for x in fields if x.lower() == "bytes"), None)
    if not path_key or not sha_key or not bytes_key:
        raise SystemExit(f"unsupported manifest schema: {manifest}")
    rebound = 0
    for row in rows:
        raw = row[path_key]
        candidate = Path(raw)
        if not candidate.is_absolute():
            repo_candidate = (repo / candidate).resolve()
            child_candidate = (child / candidate).resolve()
            candidate = repo_candidate if repo_candidate.is_file() else child_candidate
        else:
            candidate = candidate.resolve()
        if candidate in changed:
            row[sha_key] = digest(candidate)
            row[bytes_key] = str(candidate.stat().st_size)
            rebound += 1
    if rebound:
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        manifest.write_text(output.getvalue())
    rebind_rows.append(
        [
            child.name,
            before_sha,
            str(before_bytes),
            digest(manifest),
            str(manifest.stat().st_size),
            str(len(rows)),
            str(rebound),
            "true" if all(row[path_key] != "MANIFEST.tsv" and not row[path_key].endswith("/MANIFEST.tsv") for row in rows) else "false",
        ]
    )

with (manager / "PATH_NORMALIZATION.tsv").open("w", newline="") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    writer.writerow(["path", "before_sha256", "before_bytes", "after_sha256", "after_bytes", "repo_root_replacements", "tmpdir_replacements", "exact_reverse_proof"])
    writer.writerows(normalization_rows)

with (manager / "PRESERVED_SOURCE_LITERAL_INVENTORY.tsv").open("w", newline="") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    writer.writerow(["path", "repo_root_occurrences", "tmpdir_occurrences", "disposition"])
    writer.writerows(preserved_rows)

with (manager / "MANIFEST_REBIND.tsv").open("w", newline="") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    writer.writerow(["child_instance", "before_sha256", "before_bytes", "after_sha256", "after_bytes", "data_rows", "rebound_rows", "self_excluding"])
    writer.writerows(rebind_rows)

print(
    f"normalized_files={len(normalization_rows)} "
    f"preserved_files={len(preserved_rows)} "
    f"manifest_count={len(rebind_rows)}"
)
