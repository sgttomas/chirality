#!/usr/bin/env python3
"""Run the required isolated negative cases for a manifested packet candidate."""

from __future__ import annotations

import argparse
import filecmp
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable


Mutation = Callable[[Path], None]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_json(command: list[str]) -> tuple[int, dict[str, object]]:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise AssertionError(
            f"command did not return JSON: {command!r}: {error}: {result.stdout!r}"
        ) from error
    return result.returncode, payload


def append(path: Path, data: bytes) -> None:
    path.write_bytes(path.read_bytes() + data)


def record_text(token_lines: list[str], manifest_sha: str) -> str:
    tokens = "\n".join(token_lines)
    return (
        "# NEGATIVE VALIDATION FIXTURE — NOT AN OWNER ACT\n\n"
        "| Decision | `ACCEPT` |\n"
        f"| Bound manifest SHA-256 | `{manifest_sha}` |\n\n"
        f"{tokens}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_dir", type=Path)
    args = parser.parse_args()

    blueprint = Path(__file__).resolve().parent
    candidate_validator = blueprint / "validate_candidate_packet.py"
    acceptance_validator = blueprint / "validate_owner_acceptance.py"
    candidate = args.candidate_dir.resolve()
    manifest_sha = sha256(candidate / "CANDIDATE_SET_MANIFEST.sha256")
    exact_token = (
        f"ACCEPT DEL-02-06 INPUT PACKET {manifest_sha} — Ryan Tufts 2026-08-03"
    )
    results: list[dict[str, str]] = []

    def negative_candidate(name: str, mutation: Mutation, expected_issue: str) -> None:
        fixture = temp_root / name
        shutil.copytree(candidate, fixture)
        mutation(fixture)
        code, payload = run_json(
            [sys.executable, str(candidate_validator), str(fixture)]
        )
        issues = "\n".join(str(item) for item in payload.get("issues", []))
        if code == 0 or payload.get("valid") is not False or expected_issue not in issues:
            raise AssertionError(
                f"{name}: expected rejection containing {expected_issue!r}; "
                f"code={code}, payload={payload}"
            )
        results.append({"case": name, "result": "REJECTED", "issue": expected_issue})

    with tempfile.TemporaryDirectory(prefix="del0206-packet-negative-") as temp:
        temp_root = Path(temp)

        negative_candidate(
            "01_missing_file",
            lambda d: (d / "OWNER_GATE.md").unlink(),
            "exact membership mismatch",
        )
        negative_candidate(
            "02_extra_file",
            lambda d: (d / "EXTRA.md").write_text("extra\n", encoding="utf-8"),
            "exact membership mismatch",
        )
        negative_candidate(
            "03_renamed_file",
            lambda d: (d / "OWNER_GATE.md").rename(d / "OWNER_GATE_RENAMED.md"),
            "exact membership mismatch",
        )
        negative_candidate(
            "04_content_byte_changed",
            lambda d: append(d / "OWNER_SELECTION.md", b"changed\n"),
            "digest mismatch for OWNER_SELECTION.md",
        )

        def malformed_manifest(directory: Path) -> None:
            path = directory / "CANDIDATE_SET_MANIFEST.sha256"
            lines = path.read_text(encoding="utf-8").splitlines()
            lines[0] = lines[0].replace("  ", " ", 1).upper()
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        negative_candidate(
            "05_uppercase_one_space_manifest",
            malformed_manifest,
            "invalid line",
        )

        def self_manifest(directory: Path) -> None:
            path = directory / "CANDIDATE_SET_MANIFEST.sha256"
            append(path, f"{sha256(path)}  CANDIDATE_SET_MANIFEST.sha256\n".encode())

        negative_candidate(
            "06_manifest_self_entry",
            self_manifest,
            "unexpected filename CANDIDATE_SET_MANIFEST.sha256",
        )
        negative_candidate(
            "07_unresolved_placeholder",
            lambda d: append(d / "OWNER_SELECTION.md", b"{{S2_PRD_SHA256}}\n"),
            "unresolved template placeholder",
        )

        def add_crlf(directory: Path) -> None:
            path = directory / "OWNER_GATE.md"
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n", 1))

        negative_candidate("08a_crlf", add_crlf, "CR byte present")
        negative_candidate(
            "08b_trailing_whitespace",
            lambda d: append(d / "OWNER_GATE.md", b"trailing-space \n"),
            "trailing whitespace",
        )
        negative_candidate(
            "08c_surplus_eof_blank",
            lambda d: append(d / "OWNER_GATE.md", b"\n"),
            "require exactly one terminal newline",
        )

        def replace_with_symlink(directory: Path) -> None:
            path = directory / "OWNER_GATE.md"
            path.unlink()
            path.symlink_to(candidate / "OWNER_GATE.md")

        negative_candidate(
            "08d_symlink",
            replace_with_symlink,
            "missing regular non-symlink file",
        )
        negative_candidate(
            "08e_machine_absolute_path",
            lambda d: append(d / "OWNER_GATE.md", b"/Users/example/secret\n"),
            "machine-absolute path detected",
        )

        def delete_open_row(directory: Path) -> None:
            path = directory / "OPEN_ITEMS.csv"
            lines = path.read_text(encoding="utf-8").splitlines()
            path.write_text("\n".join([lines[0], *lines[2:]]) + "\n", encoding="utf-8")

        negative_candidate(
            "09_open_item_deleted",
            delete_open_row,
            "expected 16 rows, found 15",
        )

        def remove_fresh(directory: Path) -> None:
            path = directory / "OWNER_SELECTION.md"
            text = path.read_text(encoding="utf-8").replace("FRESH", "CURRENT")
            path.write_text(text, encoding="utf-8")

        negative_candidate(
            "10_fresh_marker_removed",
            remove_fresh,
            "missing required text: FRESH",
        )
        negative_candidate(
            "11_embedded_owner_token",
            lambda d: append(d / "OWNER_GATE.md", (exact_token + "\n").encode()),
            "embedded owner acceptance token is forbidden",
        )

        def negative_acceptance(
            name: str, token_lines: list[str], bound_sha: str, expected_issue: str
        ) -> None:
            record = temp_root / f"{name}.md"
            record.write_text(record_text(token_lines, bound_sha), encoding="utf-8")
            code, payload = run_json(
                [
                    sys.executable,
                    str(acceptance_validator),
                    str(candidate),
                    str(record),
                ]
            )
            issues = "\n".join(str(item) for item in payload.get("issues", []))
            if code == 0 or payload.get("valid") is not False or expected_issue not in issues:
                raise AssertionError(
                    f"{name}: expected rejection containing {expected_issue!r}; "
                    f"code={code}, payload={payload}"
                )
            results.append(
                {"case": name, "result": "REJECTED", "issue": expected_issue}
            )

        wrong_sha = "0" * 64
        wrong_token = (
            f"ACCEPT DEL-02-06 INPUT PACKET {wrong_sha} — Ryan Tufts 2026-08-03"
        )
        negative_acceptance(
            "12_wrong_manifest_token",
            [wrong_token],
            wrong_sha,
            "acceptance token does not bind",
        )
        negative_acceptance(
            "13a_zero_tokens",
            [],
            manifest_sha,
            "expected exactly one acceptance token, found 0",
        )
        negative_acceptance(
            "13b_two_tokens",
            [exact_token, exact_token],
            manifest_sha,
            "expected exactly one acceptance token, found 2",
        )

        accepted_then_edited = temp_root / "14_accepted_then_edited"
        shutil.copytree(candidate, accepted_then_edited)
        fixture_record = temp_root / "14_fixture_acceptance.md"
        fixture_record.write_text(
            record_text([exact_token], manifest_sha), encoding="utf-8"
        )
        acceptance_code, acceptance_payload = run_json(
            [
                sys.executable,
                str(acceptance_validator),
                str(accepted_then_edited),
                str(fixture_record),
            ]
        )
        if acceptance_code != 0 or acceptance_payload.get("valid") is not True:
            raise AssertionError("14_accepted_then_edited: fixture acceptance precheck failed")
        append(accepted_then_edited / "OWNER_SELECTION.md", b"post-acceptance edit\n")
        candidate_code, candidate_payload = run_json(
            [sys.executable, str(candidate_validator), str(accepted_then_edited)]
        )
        if candidate_code == 0 or candidate_payload.get("valid") is not False:
            raise AssertionError("14_accepted_then_edited: edited candidate was not rejected")
        results.append(
            {
                "case": "14_accepted_then_edited",
                "result": "REJECTED",
                "issue": "candidate manifest/content mismatch after fixture acceptance",
            }
        )

        live_copy = temp_root / "15_nonidentical_live_copy"
        shutil.copytree(candidate, live_copy)
        append(live_copy / "OWNER_GATE.md", b"copy drift\n")
        if filecmp.cmp(
            candidate / "OWNER_GATE.md", live_copy / "OWNER_GATE.md", shallow=False
        ):
            raise AssertionError("15_nonidentical_live_copy: drift was not detected")
        results.append(
            {
                "case": "15_nonidentical_live_copy",
                "result": "REJECTED",
                "issue": "byte comparison mismatch",
            }
        )

    print(
        json.dumps(
            {
                "schema": "chirality.del0206-input-packet-negative-validation/v1",
                "valid": True,
                "candidate_manifest_sha256": manifest_sha,
                "cases_passed": len(results),
                "results": results,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
