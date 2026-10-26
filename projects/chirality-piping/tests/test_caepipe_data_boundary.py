#!/usr/bin/env python3
"""Targeted data-boundary guard for the CAEPIPE correlation pilot (DEL-17-05 Design §8).

CAEPIPE outputs and everything derived from them stay in the private exchange
folder. These checks look at the files Git tracks or would add (tracked plus
untracked, not ignored) and at the pilot command's unconfigured path.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.handoff.caepipe_external import HarnessSkip, resolve_harness_config  # noqa: E402
from core.handoff.caepipe_external.harness import ENV_VAR  # noqa: E402


FORBIDDEN_SEGMENTS = {"caepipe-oracle", "caepipe_out", "oracle_cases"}
# The exchange folder's `_harness/` holds the harness's copy of the guest script and its run lock. The project's
# unrelated `_harness/adapter.yaml` (the agent harness adapter) is not an exchange path, so the segment is
# refused only together with the exchange file names.
FORBIDDEN_HARNESS_FILES = {"Invoke-CaepipeRoundTrip.ps1", "round_trip.lock"}
SECTION_TITLES = (
    "Loads on Anchors in Global Coordinates",
    "Loads on Anchors in Local Coordinates",
    "Element forces in global coordinates",
    "Pipe element forces (local)",
    "Loads on restraints",
    ": Displacements",
    "Min/Max Displacements",
)


def repository_files() -> tuple[Path, list[str]]:
    top = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                         check=False)
    if top.returncode != 0:
        pytest.skip("not inside a Git work tree")
    repo = Path(top.stdout.strip())
    listed = subprocess.run(["git", "-C", str(repo), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                            capture_output=True, check=True)
    return repo, [item for item in listed.stdout.decode("utf-8").split("\0") if item]


def test_no_exchange_style_path_is_tracked():
    _, files = repository_files()
    offending = []
    for name in files:
        parts = name.split("/")
        if FORBIDDEN_SEGMENTS & set(parts):
            offending.append(name)
        elif "_harness" in parts[:-1] and parts[-1] in FORBIDDEN_HARNESS_FILES:
            offending.append(name)
    assert offending == []


def test_caepipe_headed_files_are_declared_invented():
    repo, files = repository_files()
    offending = []
    for name in files:
        path = repo / name
        try:
            with path.open("rb") as handle:
                head = handle.read(16)
        except (IsADirectoryError, FileNotFoundError, PermissionError):
            continue
        if not head.lstrip(b"\xef\xbb\xbf").startswith(b"Caepipe"):
            continue
        provenance = path.with_name(path.stem + ".provenance.json")
        try:
            declared = json.loads(provenance.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            offending.append(name)
            continue
        if declared.get("produced_by_caepipe") is not False or "invented" not in str(declared.get("origin", "")):
            offending.append(name)
    assert offending == []


def test_no_caepipe_section_titles_under_the_public_case_folder():
    repo, files = repository_files()
    prefix = str((ROOT / "validation" / "caepipe_correlation").relative_to(repo)) + "/"
    offending = []
    for name in files:
        if not name.startswith(prefix):
            continue
        text = (repo / name).read_text(encoding="utf-8", errors="replace")
        offending.extend(f"{name}: {title}" for title in SECTION_TITLES if title in text)
    assert offending == []


def test_harness_refuses_an_exchange_folder_inside_a_git_work_tree(tmp_path):
    repo = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", str(repo)], check=True)
    folder = repo / "exchange"
    folder.mkdir()
    (folder / ".gitignore").write_text("*\n", encoding="utf-8")
    result = resolve_harness_config({ENV_VAR: str(folder), "PATH": os.environ.get("PATH", "")})
    assert isinstance(result, HarnessSkip)
    assert "inside a Git work tree" in result.reason


def test_pilot_command_without_configuration_writes_nothing(tmp_path):
    def status() -> str:
        return subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=all"],
                              capture_output=True, text=True, check=True).stdout

    env = {key: value for key, value in os.environ.items() if key != ENV_VAR}
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    before = status()
    completed = subprocess.run([sys.executable, "-m", "tools.caepipe_correlation.run_pilot"], cwd=ROOT, env=env,
                               capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr
    assert "CAEPIPE harness skipped" in completed.stdout and ENV_VAR in completed.stdout
    assert status() == before
