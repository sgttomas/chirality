#!/usr/bin/env python3
"""Render and verify the acyclic D-APP-104 approval identity."""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sys
from pathlib import Path


ROOT_TOKEN = "{{APPROVAL_EFFECT_MANIFEST_SHA256}}"
ARTIFACT_TOKEN = "{{ARTIFACT_HASHES_SHA256}}"
STATUS_TOKEN = "{{RULING_STATUS}}"
ANSWER_TOKEN = "{{OWNER_ANSWER}}"
RULING_STATUS = "RULED — GIT CLOSEOUT PENDING"
EXACT_OWNER_ANSWER = "Yes"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
MANIFEST_RE = re.compile(r"^([0-9a-f]{64})  ([^\n]+)$")
PROPOSAL = Path(__file__).resolve().parents[1]
REPO_ROOT = PROPOSAL.parents[5]
APPROVAL_MANIFEST = PROPOSAL / "APPROVAL_EFFECT_MANIFEST.sha256"
ARTIFACT_MANIFEST = PROPOSAL / "ARTIFACT_HASHES.sha256"
APPLICATION_MANIFEST = PROPOSAL / "APPLICATION_PAYLOAD_HASHES.sha256"
FILESET = PROPOSAL / "PROPOSAL_FILESET.txt"
LIVE_MANIFEST = PROPOSAL / "LIVE_SURFACE_MANIFEST.csv"
QUESTION_TEMPLATE = PROPOSAL / "OWNER_QUESTION_TEMPLATE.md"
QUESTION_OUTPUT = PROPOSAL / "OWNER_QUESTION.md"
RULING_TEMPLATE = PROPOSAL / "RULING_TEMPLATE.md"
RULING_RELATIVE = (
    "postimages/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "D-APP-104_RULING_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md"
)
RULING_OUTPUT = PROPOSAL / RULING_RELATIVE
ARTIFACT_EXCLUSIONS = {
    ARTIFACT_MANIFEST.name,
    QUESTION_OUTPUT.name,
    RULING_RELATIVE,
}
PROPOSAL_REPO_RELATIVE = (
    "projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/"
    "APP-HOLD-1_DEL-09-07_BOOTSTRAP_2026-09-04/"
)
LIVE_RULING_PATH = (
    "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "D-APP-104_RULING_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md"
)
EXPECTED_APPROVAL_LEAVES = {
    "APPLICATION_AND_ROLLBACK.md",
    "APPLICATION_PAYLOAD_HASHES.sha256",
    "INTEGRATION_CONTRACT.md",
    "LIVE_SURFACE_MANIFEST.csv",
    "OWNER_QUESTION_TEMPLATE.md",
    "PROPOSAL_FILESET.txt",
    "RULING_RENDER_TRANSFORM.md",
    "RULING_TEMPLATE.md",
    "postimages/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "D-APP-104_PACKET_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md",
    "postimages/projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "_REGISTER.md",
    "tools/render_approval.py",
}
EXPECTED_NON_PROPOSAL_LIVE_PATHS = {
    "projects/chirality-app-dev/AGENTS.md",
    "projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv",
    "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/"
    "D-APP-104_PACKET_APP_HOLD_DEL_09_07_BOOTSTRAP_2026-09-04.md",
    LIVE_RULING_PATH,
    "projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md",
    "projects/chirality-app-dev/execution/_Scripts/README.md",
    "projects/chirality-app-dev/execution/_Scripts/app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "APP_HOLD_REGISTER_DRIFT.csv",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "MALFORMED_HOLD_REGISTER_AUTHORITY.csv",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "bootstrap_expected.json",
    "projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py",
    "projects/chirality-app-dev/loop/LOOP_RECEIPTS.md",
}
EXPECTED_APPLICATION_PAYLOAD_LIVE_PATHS = {
    "projects/chirality-app-dev/AGENTS.md",
    "projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv",
    "projects/chirality-app-dev/execution/_Scripts/README.md",
    "projects/chirality-app-dev/execution/_Scripts/app_hold.py",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "APP_HOLD_REGISTER_DRIFT.csv",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "MALFORMED_HOLD_REGISTER_AUTHORITY.csv",
    "projects/chirality-app-dev/execution/_Scripts/tests/fixtures/"
    "bootstrap_expected.json",
    "projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py",
}


class ApprovalError(RuntimeError):
    """Deterministic candidate verification failure."""


def require_bytecode_containment() -> None:
    """Fail unless Python bytecode writes are disabled or externally rooted."""
    if sys.dont_write_bytecode:
        return
    prefix_value = os.environ.get("PYTHONPYCACHEPREFIX")
    if not prefix_value:
        raise ApprovalError(
            "Python bytecode containment required: set PYTHONDONTWRITEBYTECODE=1 "
            "or an absolute external PYTHONPYCACHEPREFIX"
        )
    prefix = Path(prefix_value)
    if not prefix.is_absolute():
        raise ApprovalError("PYTHONPYCACHEPREFIX must be absolute")
    resolved_prefix = prefix.resolve()
    resolved_repo = REPO_ROOT.resolve()
    if resolved_prefix == resolved_repo or resolved_repo in resolved_prefix.parents:
        raise ApprovalError("PYTHONPYCACHEPREFIX must be outside the worktree")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def approval_root() -> str:
    return sha256_file(APPROVAL_MANIFEST)


def artifact_digest() -> str:
    return sha256_file(ARTIFACT_MANIFEST)


def _safe_relative(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or value in {"", "."}:
        raise ApprovalError(f"unsafe relative path: {value}")
    return path


def parse_hash_manifest(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        match = MANIFEST_RE.fullmatch(line)
        if not match:
            raise ApprovalError(f"malformed hash-manifest line: {path}: {line}")
        digest, relative = match.groups()
        _safe_relative(relative)
        if relative in rows:
            raise ApprovalError(f"duplicate hash-manifest path: {relative}")
        rows[relative] = digest
    if list(rows) != sorted(rows):
        raise ApprovalError(f"hash manifest is not bytewise path-sorted: {path}")
    return rows


def verify_hash_manifest(path: Path, *, allow_self_exclusion: bool) -> dict[str, str]:
    rows = parse_hash_manifest(path)
    for relative, expected in rows.items():
        target = PROPOSAL / relative
        if target.is_symlink() or not target.is_file():
            raise ApprovalError(f"manifest target is absent or not regular: {relative}")
        actual = sha256_file(target)
        if actual != expected:
            raise ApprovalError(
                f"manifest digest mismatch: {relative}: {actual} != {expected}"
            )
    self_relative = path.relative_to(PROPOSAL).as_posix()
    if not allow_self_exclusion and self_relative in rows:
        raise ApprovalError(f"approval manifest cannot list itself: {self_relative}")
    if allow_self_exclusion and self_relative in rows:
        raise ApprovalError(f"artifact manifest must exclude itself: {self_relative}")
    return rows


def verify_application_manifest() -> dict[str, str]:
    rows = parse_hash_manifest(APPLICATION_MANIFEST)
    expected_keys = {
        PROPOSAL_REPO_RELATIVE + "postimages/" + live_path
        for live_path in EXPECTED_APPLICATION_PAYLOAD_LIVE_PATHS
    }
    if set(rows) != expected_keys:
        raise ApprovalError("application payload manifest set differs from exact contract")
    for repo_relative, expected in rows.items():
        proposal_relative = repo_relative[len(PROPOSAL_REPO_RELATIVE) :]
        target = PROPOSAL / proposal_relative
        if target.is_symlink() or not target.is_file():
            raise ApprovalError(f"application payload is absent or not regular: {repo_relative}")
        if sha256_file(target) != expected:
            raise ApprovalError(f"application payload digest mismatch: {repo_relative}")
    return rows


def render_question() -> bytes:
    text = QUESTION_TEMPLATE.read_text(encoding="utf-8")
    if text.count(ROOT_TOKEN) != 1:
        raise ApprovalError("owner-question template root-token count is not one")
    if text.count(ARTIFACT_TOKEN) != 1:
        raise ApprovalError("owner-question template artifact-token count is not one")
    if STATUS_TOKEN in text or ANSWER_TOKEN in text:
        raise ApprovalError("owner-question template contains ruling-only token")
    rendered = text.replace(ROOT_TOKEN, approval_root())
    rendered = rendered.replace(ARTIFACT_TOKEN, artifact_digest())
    return rendered.encode("utf-8")


def render_ruling(owner_answer: str) -> bytes:
    if owner_answer != EXACT_OWNER_ANSWER:
        raise ApprovalError("only the exact owner answer Yes may render the ruling")
    text = RULING_TEMPLATE.read_text(encoding="utf-8")
    if text.count(ROOT_TOKEN) != 2:
        raise ApprovalError("ruling template root-token count is not two")
    if text.count(ARTIFACT_TOKEN) != 2:
        raise ApprovalError("ruling template artifact-token count is not two")
    if text.count(STATUS_TOKEN) != 1 or text.count(ANSWER_TOKEN) != 1:
        raise ApprovalError("ruling template status/answer token count mismatch")
    rendered = text.replace(ROOT_TOKEN, approval_root())
    rendered = rendered.replace(ARTIFACT_TOKEN, artifact_digest())
    rendered = rendered.replace(STATUS_TOKEN, RULING_STATUS)
    rendered = rendered.replace(ANSWER_TOKEN, EXACT_OWNER_ANSWER)
    return rendered.encode("utf-8")


def expected_fileset() -> list[str]:
    lines = FILESET.read_text(encoding="utf-8").splitlines()
    if not lines or lines != sorted(set(lines)):
        raise ApprovalError("proposal file-set is empty, duplicated, or unsorted")
    for line in lines:
        _safe_relative(line)
    return lines


def observed_fileset() -> list[str]:
    observed: list[str] = []
    for path in PROPOSAL.rglob("*"):
        relative = path.relative_to(PROPOSAL)
        if path.is_symlink():
            raise ApprovalError(
                f"proposal file-set contains symlink: {relative}"
            )
        if path.is_dir():
            if path.name in {"__pycache__", ".pytest_cache"}:
                raise ApprovalError(
                    f"proposal file-set contains Python cache directory: {relative}"
                )
            continue
        if not path.is_file():
            raise ApprovalError(
                f"proposal file-set contains nonregular entry: {relative}"
            )
        if path.suffix == ".pyc":
            raise ApprovalError(
                f"proposal file-set contains Python bytecode: {relative}"
            )
        observed.append(relative.as_posix())
    return sorted(observed)


def verify_live_manifest(
    approval_leaves: dict[str, str],
    artifact_leaves: dict[str, str],
    application_leaves: dict[str, str],
) -> None:
    with LIVE_MANIFEST.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, strict=True)
        expected_fields = [
            "path",
            "action",
            "preimage_sha256",
            "postimage_binding",
            "binding_kind",
            "application_note",
        ]
        if reader.fieldnames != expected_fields:
            raise ApprovalError("live-surface manifest header mismatch")
        rows = list(reader)
    paths = [row["path"] for row in rows]
    if len(paths) != len(set(paths)):
        raise ApprovalError("live-surface manifest has duplicate paths")
    if paths != sorted(paths):
        raise ApprovalError("live-surface manifest is not bytewise path-sorted")
    proposal_rows = {
        row["path"][len(PROPOSAL_REPO_RELATIVE) :]: row
        for row in rows
        if row["path"].startswith(PROPOSAL_REPO_RELATIVE)
    }
    if sorted(proposal_rows) != expected_fileset():
        raise ApprovalError("proposal file set and live-surface rows differ")
    non_proposal_paths = {
        path for path in paths if not path.startswith(PROPOSAL_REPO_RELATIVE)
    }
    if non_proposal_paths != EXPECTED_NON_PROPOSAL_LIVE_PATHS:
        raise ApprovalError("non-proposal live-surface set differs from exact contract")

    for row in rows:
        path = row["path"]
        binding = row["postimage_binding"]
        kind = row["binding_kind"]
        proposal_relative = (
            path[len(PROPOSAL_REPO_RELATIVE) :]
            if path.startswith(PROPOSAL_REPO_RELATIVE)
            else None
        )
        if kind in {"SHA256_APPLICATION_PAYLOAD", "SHA256_APPROVAL_ROOT_LEAF"}:
            if not SHA_RE.fullmatch(binding):
                raise ApprovalError(f"invalid SHA256 binding: {path}")
            candidate = PROPOSAL / "postimages" / path
            if candidate.is_symlink() or not candidate.is_file():
                raise ApprovalError(f"missing live postimage candidate: {path}")
            if sha256_file(candidate) != binding:
                raise ApprovalError(f"live postimage digest mismatch: {path}")
            proposal_candidate = "postimages/" + path
            if kind == "SHA256_APPLICATION_PAYLOAD":
                application_key = PROPOSAL_REPO_RELATIVE + proposal_candidate
                if path not in EXPECTED_APPLICATION_PAYLOAD_LIVE_PATHS:
                    raise ApprovalError(f"unexpected application payload path: {path}")
                if application_leaves.get(application_key) != binding:
                    raise ApprovalError(f"application payload binding mismatch: {path}")
            elif approval_leaves.get(proposal_candidate) != binding:
                raise ApprovalError(f"approval-root postimage binding mismatch: {path}")
        elif kind == "APPROVAL_ROOT_LEAF":
            if proposal_relative not in approval_leaves:
                raise ApprovalError(f"approval-root leaf absent: {path}")
            if approval_leaves[proposal_relative] != sha256_file(PROPOSAL / proposal_relative):
                raise ApprovalError(f"approval-root leaf mismatch: {path}")
            if binding != "BOUND_BY_APPROVAL_EFFECT_MANIFEST":
                raise ApprovalError(f"approval-root marker mismatch: {path}")
        elif kind == "APPLICATION_PAYLOAD_LEAF":
            if proposal_relative is None:
                raise ApprovalError(f"application payload leaf is outside proposal: {path}")
            application_key = PROPOSAL_REPO_RELATIVE + proposal_relative
            if application_leaves.get(application_key) != sha256_file(
                PROPOSAL / proposal_relative
            ):
                raise ApprovalError(f"application-payload leaf mismatch: {path}")
            if binding != "BOUND_BY_APPLICATION_PAYLOAD_AND_APPROVAL_ROOT":
                raise ApprovalError(f"application-payload marker mismatch: {path}")
        elif kind == "ARTIFACT_MANIFEST_LEAF":
            if proposal_relative not in artifact_leaves:
                raise ApprovalError(f"artifact leaf absent: {path}")
            if artifact_leaves[proposal_relative] != sha256_file(PROPOSAL / proposal_relative):
                raise ApprovalError(f"artifact leaf mismatch: {path}")
            if binding != "BOUND_BY_ARTIFACT_HASHES":
                raise ApprovalError(f"artifact marker mismatch: {path}")
        elif kind == "OWNER_APPROVAL_ROOT_CARRIER":
            if proposal_relative != APPROVAL_MANIFEST.name:
                raise ApprovalError(f"wrong owner-root carrier: {path}")
            if binding != "SHA256_CITED_IN_RENDERED_OWNER_QUESTION":
                raise ApprovalError(f"owner-root carrier marker mismatch: {path}")
        elif kind == "DETERMINISTIC_QUESTION":
            if proposal_relative != QUESTION_OUTPUT.name:
                raise ApprovalError(f"wrong deterministic question path: {path}")
            if binding != "RENDERED_FROM_BOUND_TEMPLATE_ROOT_AND_ARTIFACT_DIGEST":
                raise ApprovalError(f"question marker mismatch: {path}")
        elif kind == "DETERMINISTIC_RULING":
            if path not in {
                PROPOSAL_REPO_RELATIVE + RULING_RELATIVE,
                LIVE_RULING_PATH,
            }:
                raise ApprovalError(f"wrong deterministic ruling path: {path}")
            if binding != "RENDERED_AFTER_EXACT_OWNER_YES_WITH_ARTIFACT_DIGEST":
                raise ApprovalError(f"ruling marker mismatch: {path}")
        elif kind == "ARTIFACT_MANIFEST_EXCLUSIONS":
            if proposal_relative != ARTIFACT_MANIFEST.name:
                raise ApprovalError(f"wrong artifact self-exclusion path: {path}")
            if binding != "SELF_AND_RENDERED_OUTPUTS_EXCLUDED":
                raise ApprovalError(f"artifact self-exclusion marker mismatch: {path}")
            if proposal_relative in artifact_leaves:
                raise ApprovalError("artifact manifest unexpectedly hashes itself")
        elif kind == "DYNAMIC_RECEIPT":
            if path != "projects/chirality-app-dev/loop/LOOP_RECEIPTS.md":
                raise ApprovalError(f"wrong dynamic receipt path: {path}")
            if binding != "NEXT_AVAILABLE_REMINT":
                raise ApprovalError(f"dynamic receipt marker mismatch: {path}")
        else:
            raise ApprovalError(f"unknown live-surface binding kind: {kind}: {path}")


def verify() -> None:
    require_bytecode_containment()
    approval_leaves = verify_hash_manifest(
        APPROVAL_MANIFEST, allow_self_exclusion=False
    )
    artifact_leaves = verify_hash_manifest(
        ARTIFACT_MANIFEST, allow_self_exclusion=True
    )
    application_leaves = verify_application_manifest()
    if set(approval_leaves) != EXPECTED_APPROVAL_LEAVES:
        raise ApprovalError("approval-effect manifest leaf set differs from exact contract")
    expected_artifact_leaves = set(expected_fileset()) - ARTIFACT_EXCLUSIONS
    if set(artifact_leaves) != expected_artifact_leaves:
        raise ApprovalError(
            "artifact manifest does not match the exact acyclic exclusion contract"
        )
    if expected_fileset() != observed_fileset():
        raise ApprovalError("proposal file set differs from PROPOSAL_FILESET.txt")
    if QUESTION_OUTPUT.read_bytes() != render_question():
        raise ApprovalError("rendered owner question differs from bound template")
    if RULING_OUTPUT.read_bytes() != render_ruling(EXACT_OWNER_ANSWER):
        raise ApprovalError("conditional ruling differs from deterministic render")
    verify_live_manifest(approval_leaves, artifact_leaves, application_leaves)


def write_output(data: bytes, output: str | None) -> None:
    if output:
        Path(output).write_bytes(data)
    else:
        sys.stdout.buffer.write(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    question = subparsers.add_parser("render-question")
    question.add_argument("--output")
    ruling = subparsers.add_parser("render-ruling")
    ruling.add_argument("--owner-answer", required=True)
    ruling.add_argument("--output")
    subparsers.add_parser("verify")
    args = parser.parse_args()
    try:
        require_bytecode_containment()
        if args.command == "render-question":
            write_output(render_question(), args.output)
        elif args.command == "render-ruling":
            write_output(render_ruling(args.owner_answer), args.output)
        else:
            verify()
            print(
                "APPROVAL_VERIFY_PASS "
                f"approval_root={approval_root()} "
                f"artifact_digest={artifact_digest()} "
                f"proposal_files={len(expected_fileset())}"
            )
    except (ApprovalError, OSError, UnicodeError) as error:
        print(f"APPROVAL_VERIFY_ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
