"""D-PEC-91 (A-53) mutation evidence (P1_STORE_GUARD_04 author evidence).

Usage: PYTHONDONTWRITEBYTECODE=1 python3 mutate_d91.py <path-to-postimage-v2-tree>

Pattern after P1_STORE_GUARD_03/probes/mutate_d89.py. Copies the v2 tree to a
fresh temporary directory (outside any repository checkout) once per
mutation, applies exactly one mutation from the D-PEC-91 per-repair table
(M2 and M3 relative to the A-53 bound 2**53 - 1), runs the storage suite
there with PYTHONDONTWRITEBYTECODE=1, and reports which tests fail. The source
tree given on the command line is only read. Exit status is nonzero if the
baseline fails or any mutation survives (is not caught by every named test).

M1 upper bound removed (the preimage `value >= 0`)
M2 `0 <= value < _MAX_COUNT`
M3 `0 <= value <= _MAX_COUNT + 1`
M4 bound replaced by catching ValueError from str()
M5 str() evaluated before the bound
M6 bound widened to 10**4000
M7 R12 in sqlite_store.py narrowed to `except FileExistsError` (scratch copy only)
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

GUARD = "src/pec_v2/core/content_minimal_guard.py"
ADAPTER = "src/pec_v2/adapters/storage/sqlite_store.py"

P005 = "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution"
POLICY = "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_policy_is_fixed_finite_and_domain_checked"
P002 = "test_store_lifecycle.StoreLifecycleTests.test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation"

COUNT_BRANCH = "        elif field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT:\n"
M4_HELPER = (
    "\n\n"
    "def _m4_render(value: int) -> str | None:\n"
    "    try:\n"
    "        return str(value)\n"
    "    except ValueError:\n"
    "        return None\n"
)

MUTATIONS = (
    ("M1", "upper bound removed (preimage `value >= 0`)", GUARD, [(
        COUNT_BRANCH,
        "        elif field_class is FieldClass.COUNT and type(value) is int and value >= 0:\n",
    )], {P005, POLICY}, None),
    ("M2", "`0 <= value < _MAX_COUNT`", GUARD, [(
        COUNT_BRANCH,
        "        elif field_class is FieldClass.COUNT and type(value) is int and 0 <= value < _MAX_COUNT:\n",
    )], {POLICY}, None),
    ("M3", "`0 <= value <= _MAX_COUNT + 1`", GUARD, [(
        COUNT_BRANCH,
        "        elif field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT + 1:\n",
    )], {POLICY}, None),
    ("M4", "bound replaced by catching ValueError from str()", GUARD, [(
        COUNT_BRANCH,
        "        elif field_class is FieldClass.COUNT and type(value) is int and value >= 0 and _m4_render(value) is not None:\n",
    )], {POLICY}, M4_HELPER),
    ("M5", "str() evaluated before the bound", GUARD, [(
        COUNT_BRANCH,
        "        elif field_class is FieldClass.COUNT and type(value) is int and (early := str(value)) is not None and 0 <= value <= _MAX_COUNT:\n",
    )], {P005, POLICY}, None),
    ("M6", "bound widened to 10**4000", GUARD, [(
        "_MAX_COUNT = 2**53 - 1\n",
        "_MAX_COUNT = 10**4000\n",
    )], {POLICY}, None),
    ("M7", "R12 narrowed to `except FileExistsError`", ADAPTER, [(
        "            self._database_path.parent.mkdir(parents=True, exist_ok=True)\n"
        "        except OSError as error:\n"
        '            raise StoreConfigurationError("metadata store directory could not be created") from error\n',
        "            self._database_path.parent.mkdir(parents=True, exist_ok=True)\n"
        "        except FileExistsError as error:\n"
        '            raise StoreConfigurationError("metadata store directory could not be created") from error\n',
    )], {P002}, None),
)

FAILURE_LINE = re.compile(r"^(FAIL|ERROR): \S+ \(([^)]+)\)", re.MULTILINE)
RAN_LINE = re.compile(r"^Ran (\d+) tests?", re.MULTILINE)


def run_suite(v2: Path) -> tuple[int, int, set[str]]:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(v2 / "tests" / "storage"), "-p", "test_*.py", "-v"],
        cwd=v2.parent,
        env=env,
        capture_output=True,
        text=True,
    )
    output = completed.stdout + completed.stderr
    ran = RAN_LINE.search(output)
    failing = {match.group(2) for match in FAILURE_LINE.finditer(output)}
    return completed.returncode, int(ran.group(1)) if ran else -1, failing


def fresh_copy(source: Path, parent: Path) -> Path:
    target = parent / "v2"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", ".pec-v2"))
    return target


def short(test_id: str) -> str:
    return test_id.rsplit(".", 1)[-1]


def host_enforces_directory_permissions(parent: Path) -> bool:
    probe = parent / "r16-host-probe"
    probe.mkdir()
    probe.chmod(0o555)
    try:
        return not os.access(probe, os.W_OK)
    finally:
        probe.chmod(0o755)
        probe.rmdir()


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: mutate_d91.py <path-to-postimage-v2-tree>")
    source = Path(sys.argv[1]).resolve()
    print(f"mutate_d91: source v2 tree {source}")
    print(f"interpreter {sys.executable} {sys.version.split()[0]}; uid {os.getuid()}")
    status = 0
    with tempfile.TemporaryDirectory(prefix="mutate_d91_") as scratch:
        parent = Path(scratch)
        print(f"host enforces directory permissions (0o555 dir not writable): {host_enforces_directory_permissions(parent)}")
        code, ran, failing = run_suite(fresh_copy(source, parent))
        print(f"BASELINE exit={code} ran={ran} failing={sorted(short(t) for t in failing)}")
        if code != 0 or failing:
            status = 1
        for mutation_id, description, relative, replacements, expected, append in MUTATIONS:
            v2 = fresh_copy(source, parent)
            target = v2 / relative
            text = target.read_text(encoding="utf-8")
            for old, new in replacements:
                occurrences = text.count(old)
                if occurrences != 1:
                    print(f"{mutation_id} APPLY-ERROR: pattern occurs {occurrences} times in {relative}")
                    status = 1
                    break
                text = text.replace(old, new)
            else:
                if append:
                    text += append
                target.write_text(text, encoding="utf-8")
                code, ran, failing = run_suite(v2)
                names = sorted(short(t) for t in failing)
                missing = sorted(short(t) for t in expected - failing)
                verdict = "CAUGHT by all named tests" if not missing and code != 0 else f"NOT CAUGHT by {missing}"
                if missing or code == 0:
                    status = 1
                print(f"{mutation_id} {description}: exit={code} ran={ran} failing={names} -> {verdict}")
    print("RESULT", "PASS" if status == 0 else "FAIL")
    return status


if __name__ == "__main__":
    sys.exit(main())
