"""D-PEC-89 mutation evidence (P1_STORE_GUARD_03 author evidence).

Usage: python3 mutate_d89.py <path-to-postimage-v2-tree>

Copies the v2 tree to a fresh temporary directory (outside any repository
checkout) once per mutation, applies exactly one reversal from the proposal's
"Mutation evidence" bullet, runs the storage suite there with
PYTHONDONTWRITEBYTECODE=1, and reports which tests fail. The source tree given
on the command line is only read.

M1-M4: `isinstance` restored in `_is_identifier`, `_valid_hex`, the path check,
        and the container check (both container sites, i.e. the preimage form).
M5-M6: each R10 echo restored (record ID, field name), in the A2 form that
        keeps the exact-type rule, so only the echo differs.
M7-M9: R11, R12, R13 removed.
M4a/M4b are supplementary single-site variants of M4 (not in the proposal).
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
FORGED = "test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing"
P002 = "test_store_lifecycle.StoreLifecycleTests.test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation"

CONTAINER_FIRST = (
    "        if type(candidate_fields) is not tuple or not candidate_fields:\n",
    "        if not isinstance(candidate_fields, tuple) or not candidate_fields:\n",
)
CONTAINER_SECOND = (
    "        if type(candidate_fields) is tuple:\n",
    "        if isinstance(candidate_fields, tuple):\n",
)

MUTATIONS = (
    ("M1", "isinstance restored in _is_identifier", GUARD, [(
        "    return type(value) is str and _IDENTIFIER.fullmatch(value) is not None\n",
        "    return isinstance(value, str) and _IDENTIFIER.fullmatch(value) is not None\n",
    )], {POLICY, FORGED}),
    ("M2", "isinstance restored in _valid_hex", GUARD, [(
        "    return type(value) is str and len(value) == length and bool(_LOWER_HEX.fullmatch(value))\n",
        "    return isinstance(value, str) and len(value) == length and bool(_LOWER_HEX.fullmatch(value))\n",
    )], {POLICY, FORGED}),
    ("M3", "isinstance restored in the path check", GUARD, [(
        "    if type(value) is not str or not value:\n",
        "    if not isinstance(value, str) or not value:\n",
    )], {POLICY, FORGED}),
    ("M4", "isinstance restored in the container check (both sites)", GUARD,
     [CONTAINER_FIRST, CONTAINER_SECOND], {POLICY, FORGED}),
    ("M5", "R10 record-ID echo restored", GUARD, [(
        '        record_id = candidate_record_id if _is_identifier(candidate_record_id) else "<unknown>"\n',
        '        record_id = candidate_record_id if type(candidate_record_id) is str else "<unknown>"\n',
    )], {P005, FORGED}),
    ("M6", "R10 field-name echo restored", GUARD, [(
        'failures.append(AdmissionFailure(record_id, fallback, "INVALID_FIELD_NAME",',
        'failures.append(AdmissionFailure(record_id, candidate_name if type(candidate_name) is str else fallback, "INVALID_FIELD_NAME",',
    )], {P005, FORGED}),
    ("M7", "R11 removed (close() unwrapped)", ADAPTER, [(
        "            try:\n"
        "                self._connection.close()\n"
        "            except sqlite3.Error as error:\n"
        '                raise StoreDataError("metadata store could not be closed") from error\n'
        "            self._connection = None\n",
        "            self._connection.close()\n"
        "            self._connection = None\n",
    )], {P002}),
    ("M8", "R12 removed (mkdir unwrapped)", ADAPTER, [(
        "        try:\n"
        "            self._database_path.parent.mkdir(parents=True, exist_ok=True)\n"
        "        except OSError as error:\n"
        '            raise StoreConfigurationError("metadata store directory could not be created") from error\n',
        "        self._database_path.parent.mkdir(parents=True, exist_ok=True)\n",
    )], {P002}),
    ("M9", "R13 removed (unlink OSError unwrapped)", ADAPTER, [(
        "            except FileNotFoundError:\n"
        "                pass\n"
        "            except OSError as error:\n"
        '                raise StoreDataError("metadata store files could not be deleted") from error\n',
        "            except FileNotFoundError:\n"
        "                pass\n",
    )], {P002}),
    ("M4a", "supplementary: container check first site only", GUARD, [CONTAINER_FIRST], None),
    ("M4b", "supplementary: container check loop site only", GUARD, [CONTAINER_SECOND], None),
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


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: mutate_d89.py <path-to-postimage-v2-tree>")
    source = Path(sys.argv[1]).resolve()
    print(f"mutate_d89: source v2 tree {source}")
    print(f"interpreter {sys.executable} {sys.version.split()[0]}")
    status = 0
    with tempfile.TemporaryDirectory(prefix="mutate_d89_") as scratch:
        parent = Path(scratch)
        code, ran, failing = run_suite(fresh_copy(source, parent))
        print(f"BASELINE exit={code} ran={ran} failing={sorted(short(t) for t in failing)}")
        if code != 0 or failing:
            status = 1
        for mutation_id, description, relative, replacements, expected in MUTATIONS:
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
                target.write_text(text, encoding="utf-8")
                code, ran, failing = run_suite(v2)
                names = sorted(short(t) for t in failing)
                if expected is None:
                    verdict = "SUPPLEMENTARY"
                else:
                    missing = sorted(short(t) for t in expected - failing)
                    verdict = "CAUGHT by all named tests" if not missing else f"NOT CAUGHT by {missing}"
                    if missing or code == 0:
                        status = 1
                print(f"{mutation_id} {description}: exit={code} ran={ran} failing={names} -> {verdict}")
    print("RESULT", "PASS" if status == 0 else "FAIL")
    return status


if __name__ == "__main__":
    sys.exit(main())
