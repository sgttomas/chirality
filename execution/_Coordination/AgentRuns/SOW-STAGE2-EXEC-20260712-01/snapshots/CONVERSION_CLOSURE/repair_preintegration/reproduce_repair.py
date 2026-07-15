#!/usr/bin/env python3
"""Independently reproduce and audit the bounded clean-production repair."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
BASIS = "715f618e93528d626a73d2134781e8c9c27f6c90"
AUTHOR_REPORTS = RUN / "instances/WORKING-CLEAN-REPAIR/reports"
FINALIZER = ROOT / "tools/scope_of_work/finalize_scope_of_work.py"
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
FORBIDDEN = re.compile(
    r"migration candidate|sow-source-begin|sow-source-end|migration-authority:|"
    r"pilot-variance:|issued-preparation-",
    re.IGNORECASE,
)
BEGIN = re.compile(r'^<!-- sow-source-begin (?P<meta>\{.*\}) -->$')
END = "<!-- sow-source-end -->"

sys.path.insert(0, str(ROOT / "tools/scope_of_work"))
from common import resolve_production_format  # noqa: E402


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{BASIS}:{path}"], cwd=ROOT)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source_blocks(text: str) -> list[tuple[dict[str, object], list[str]]]:
    lines = text.splitlines()
    result: list[tuple[dict[str, object], list[str]]] = []
    i = 0
    while i < len(lines):
        match = BEGIN.match(lines[i])
        if not match:
            i += 1
            continue
        end = i + 1
        while end < len(lines) and lines[end] != END:
            end += 1
        if end == len(lines):
            raise ValueError(f"unterminated source block at line {i + 1}")
        result.append((json.loads(match.group("meta")), lines[i + 1 : end]))
        i = end + 1
    return result


def main() -> int:
    errors: list[str] = []
    attempts: list[str] = []
    project_paths = subprocess.check_output(
        ["git", "diff", "--name-only", BASIS, "--", "projects/chirality-app-dev", "projects/chirality-piping"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    project_paths = sorted(project_paths)
    expected_shape = all(path.endswith("/ScopeOfWork.md") for path in project_paths)
    populations = Counter(
        "chirality-app-dev" if path.startswith("projects/chirality-app-dev/") else "chirality-piping"
        for path in project_paths
    )
    if len(project_paths) != 57:
        errors.append(f"project delta has {len(project_paths)} paths, expected 57")
    if not expected_shape:
        errors.append("project delta contains a non-ScopeOfWork.md path")
    if populations != Counter({"chirality-app-dev": 53, "chirality-piping": 4}):
        errors.append(f"project population mismatch: {dict(populations)}")

    rows: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="recon-clean-repair-") as raw_tmp:
        tmp = Path(raw_tmp)
        for index, path in enumerate(project_paths, 1):
            before = git_blob(path)
            current = (ROOT / path).read_bytes()
            candidate = tmp / f"candidate-{index}.md"
            output = tmp / f"output-{index}.md"
            report_path = tmp / f"report-{index}.json"
            candidate.write_bytes(before)
            proc = subprocess.run(
                [sys.executable, str(FINALIZER), "--evidence-candidate", str(candidate), "--output", str(output), "--report", str(report_path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            attempts.append(f"{path}\texit={proc.returncode}\t{proc.stdout.strip()}\t{proc.stderr.strip()}")
            if proc.returncode != 0:
                errors.append(f"finalizer failed: {path}: {proc.stderr.strip()}")
                continue
            reproduced = output.read_bytes()
            report_bytes = report_path.read_bytes()
            report = json.loads(report_bytes)
            original_text = before.decode("utf-8")
            production_text = current.decode("utf-8")
            blocks = source_blocks(original_text)
            author_report = AUTHOR_REPORTS / Path(path).with_suffix("") / "finalization.json"
            if reproduced != current:
                errors.append(f"reproduced bytes differ: {path}")
            if not author_report.is_file():
                errors.append(f"missing author report: {path}")
            elif author_report.read_bytes() != report_bytes:
                errors.append(f"author report differs from reproduction: {path}")
            if report.get("schema") != "chirality-sow-finalization/v1":
                errors.append(f"report schema mismatch: {path}")
            if report.get("evidence_candidate_sha256") != digest(before):
                errors.append(f"report before binding mismatch: {path}")
            if report.get("production_scope_of_work_sha256") != digest(current):
                errors.append(f"report after binding mismatch: {path}")
            if report.get("source_block_count") != len(blocks) or len(report.get("source_blocks", [])) != len(blocks):
                errors.append(f"report source block count mismatch: {path}")
            for block_index, ((metadata, lines), recorded) in enumerate(zip(blocks, report.get("source_blocks", [])), 1):
                preserved_hash = digest("\n".join(lines).encode("utf-8"))
                if recorded != {**metadata, "preserved_text_sha256": preserved_hash}:
                    errors.append(f"source block report mismatch: {path} block {block_index}")
                quoted = "\n".join(">" if line == "" else f"> {line}" for line in lines)
                if quoted not in production_text:
                    errors.append(f"quoted source content absent: {path} block {block_index}")
            if FORBIDDEN.search(production_text):
                errors.append(f"forbidden production residue: {path}")
            rows.append(
                {
                    "path": path,
                    "basis_sha256": digest(before),
                    "production_sha256": digest(current),
                    "report_sha256": digest(report_bytes),
                    "source_blocks": len(blocks),
                    "wording_updates": report.get("production_wording_update_count"),
                }
            )

    census = read_tsv(RUN / "basis/CENSUS_MANIFEST.tsv")
    formats: Counter[str] = Counter()
    converted: Counter[str] = Counter()
    lifecycle: Counter[str] = Counter()
    residue: list[str] = []
    exemptions = 0
    for member in census:
        directory = ROOT / member["path"]
        resolution = resolve_production_format(directory)
        formats[resolution.state] += 1
        excluded = member["project"] == "PIP" and member["package"] == "PKG-00"
        if not excluded:
            converted[resolution.state] += 1
        if not resolution.valid:
            errors.append(f"invalid format: {member['path']}: {resolution.issues}")
        status_text = (directory / "_STATUS.md").read_text(encoding="utf-8")
        match = re.search(r"\*\*Current State:\*\*\s*([^\n]+)", status_text)
        lifecycle[match.group(1).strip() if match else "UNKNOWN"] += 1
        sow = directory / "ScopeOfWork.md"
        if sow.is_file() and FORBIDDEN.search(sow.read_text(encoding="utf-8")):
            residue.append(member["path"])
        if excluded:
            exemptions += 1
            for name in LEGACY:
                relative = (Path(member["path"]) / name).as_posix()
                if (ROOT / relative).read_bytes() != git_blob(relative):
                    errors.append(f"PKG-00 exemption drift: {relative}")

    if formats != Counter({"SOW_V1": 146, "LEGACY_FOUR_DOC": 8}):
        errors.append(f"format census mismatch: {dict(formats)}")
    if converted != Counter({"SOW_V1": 146}):
        errors.append(f"conversion census mismatch: {dict(converted)}")
    if lifecycle != Counter({"IN_PROGRESS": 153, "ISSUED": 1}):
        errors.append(f"lifecycle census mismatch: {dict(lifecycle)}")
    if residue:
        errors.append(f"forbidden residue in {len(residue)} corpus members")
    if exemptions != 8:
        errors.append(f"PKG-00 exemption count {exemptions}, expected 8")

    manifest = INSTANCE / "REPRODUCTION_MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["path"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    (INSTANCE / "FINALIZER_ATTEMPTS.tsv").write_text("path\tresult\tstdout\tstderr\n" + "\n".join(attempts) + "\n", encoding="utf-8")
    result = {
        "schema": "chirality-sow-clean-repair-reconciliation/v1",
        "basis": BASIS,
        "verdict": "PASS" if not errors else "BLOCKED",
        "errors": errors,
        "project_paths": len(project_paths),
        "project_populations": dict(populations),
        "reproduced_outputs": len(rows),
        "source_blocks": sum(int(row["source_blocks"]) for row in rows),
        "wording_updates": sum(int(row["wording_updates"]) for row in rows),
        "formats": dict(formats),
        "converted_formats": dict(converted),
        "lifecycle": dict(lifecycle),
        "pkg00_exemptions": exemptions,
        "forbidden_residue_members": residue,
        "reproduction_manifest_sha256": digest(manifest.read_bytes()),
    }
    (INSTANCE / "REPRODUCTION_RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
