#!/usr/bin/env python3
"""Run the reusable Gate-5 coverage builder for chirality-piping WITHOUT editing it.

tools/decomp/build_gate5_coverage.py is data-driven and reusable, but the tail of
its main() unconditionally *updates* two publication/coordination docs by reading
them in place:
  - decomp_root/Chirality_Domain_Decomposition.md  (the published control doc — a
    GATE-6 artifact; it does not exist yet at Gate 5)
  - domain_root/_Coordination/NEXT_INSTANCE_PROMPT.md (a coordination artifact not
    used by this pack)
For chirality-app-dev both existed (control doc created at intake), so the tool
completed. For piping they are legitimately absent at Gate 5, so the read_text()
raises FileNotFoundError after all substantive artifacts are already written.

This wrapper monkeypatches ONLY those two update_* functions to no-op when their
target file is missing (the file content is a Gate-6 / coordination concern, not a
Gate-5 coverage truth), then calls the tool's own main() so every substantive step
runs unchanged: Section_Coverage_Register.csv, Source_Coverage_Summary.csv,
Gate5 telemetry, the review packet, the proposal package, atom slices, and the
in-place updates to the registers that DO exist (Open_Issues, Validation_Checks,
Companion_Inventory, Intake_Telemetry). The shared tool file is untouched.

Usage:  python3 _adapter/gate5_build_coverage.py [--timestamp TS] [--skip-render]
Run with cwd = MONOREPO_ROOT (chirality/). Forwards extra args to the tool.
"""
from __future__ import annotations
import sys
from pathlib import Path

MONO = Path.cwd()
sys.path.insert(0, str(MONO / "tools/decomp"))
import build_gate5_coverage as B  # noqa: E402

_orig_control = B.update_control_doc
_orig_next = B.update_next_prompt


def _skip_if_missing(orig, label):
    def wrapped(path, *a, **k):
        if not Path(path).exists():
            print(f"      [gate5 wrapper] skipping {label}: {path} absent "
                  f"(deferred to Gate 6 / coordination)", flush=True)
            return None
        return orig(path, *a, **k)
    return wrapped


def main():
    B.update_control_doc = _skip_if_missing(_orig_control, "control-doc update")
    B.update_next_prompt = _skip_if_missing(_orig_next, "next-prompt update")
    sys.argv = (["build_gate5_coverage.py",
                 "--domain-root", "domains/chirality-piping", "--repo-root", "."]
                + sys.argv[1:])
    return B.main()


if __name__ == "__main__":
    raise SystemExit(main())
