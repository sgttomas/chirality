"""D-PEC-91 R16 execution evidence (P1_STORE_GUARD_04 author evidence).

Usage: PYTHONDONTWRITEBYTECODE=1 python3 r16_block_probe.py <path-to-postimage-v2-tree>

R16's read-only-checkout block in test_ver_002 runs only when
os.access(checkout, os.W_OK) is false after chmod 0o555. This probe copies the
v2 tree to a temporary directory outside the checkout, inserts one
instrumentation line as the first statement inside that `if` block (it writes a
marker file named by the R16_MARKER environment variable), runs only
test_ver_002 there, and reports whether the marker was written, i.e. whether
the block's assertions actually executed on this host. The source tree is
only read; the instrumented copy is removed on exit.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

TEST = "tests/storage/test_store_lifecycle.py"
ANCHOR = "            if not os.access(self.checkout, os.W_OK):\n"
MARKER_LINE = '                Path(os.environ["R16_MARKER"]).write_text("ran", encoding="utf-8")\n'


def main() -> int:
    if len(sys.argv) != 2:
        sys.exit("usage: r16_block_probe.py <path-to-postimage-v2-tree>")
    source = Path(sys.argv[1]).resolve()
    print(f"r16_block_probe: source v2 tree {source}")
    print(f"interpreter {sys.executable} {sys.version.split()[0]}; uid {os.getuid()}")
    with tempfile.TemporaryDirectory(prefix="r16_block_") as scratch:
        parent = Path(scratch)
        v2 = parent / "v2"
        shutil.copytree(source, v2, ignore=shutil.ignore_patterns("__pycache__", ".pec-v2"))
        target = v2 / TEST
        text = target.read_text(encoding="utf-8")
        if text.count(ANCHOR) != 1:
            print(f"APPLY-ERROR: anchor occurs {text.count(ANCHOR)} times")
            return 2
        target.write_text(text.replace(ANCHOR, ANCHOR + MARKER_LINE), encoding="utf-8")
        marker = parent / "r16.marker"
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", R16_MARKER=str(marker))
        completed = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(v2 / "tests" / "storage"), "-p", "test_*.py",
             "-k", "test_ver_002", "-v"],
            cwd=parent,
            env=env,
            capture_output=True,
            text=True,
        )
        output = (completed.stdout + completed.stderr).strip().splitlines()
        print(f"instrumented test_ver_002 run: exit={completed.returncode}; last line: {output[-1] if output else ''}")
        for line in output:
            if line.startswith("Ran ") or line.endswith(" ... ok") or "FAIL" in line or "ERROR" in line:
                print(f"  {line}")
        executed = marker.is_file() and marker.read_text(encoding="utf-8") == "ran"
        print(f"R16 read-only block executed (marker written): {executed}")
    return 0 if completed.returncode == 0 and executed else 1


if __name__ == "__main__":
    sys.exit(main())
