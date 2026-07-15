#!/usr/bin/env python3
"""Produce PKG-08-B2 verifier replacement, simulation, and closure evidence."""
from pathlib import Path

repo = Path(__file__).resolve().parents[8]
template = repo / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG06/children/VERIFY-B1/finalize_verifier.py"
source = template.read_text(encoding="utf-8")
remainder = source.split("def sha(path: Path) -> str:", 1)[1]
prefix = '''#!/usr/bin/env python3
from __future__ import annotations
import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/WORKING-P2-PKG08/children/VERIFY-B2"
CAND = RUN / "candidates/W_P2/PIP-PKG08"
HEAD = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROLS = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-08-06": ("22f2934acd6c24463131f24b58eb6b91773b0b5deb9bf15f47d9d365c0e0e4a9", 33, 301),
}
'''
code = prefix + "\ndef sha(path: Path) -> str:" + remainder
code = code.replace('assert len(replacement) == len(inverse) == 25 and len(simulations) == 5', 'assert len(replacement) == len(inverse) == 5 and len(simulations) == 1')
code = code.replace('"agent": "VERIFY-B1"', '"agent": "VERIFY-B2"')
code = code.replace('"members_complete": 5', '"members_complete": 1')
code = code.replace('"mappings": 151, "source_lines": 1343, "fail_closed_probes": 35', '"mappings": 33, "source_lines": 301, "fail_closed_probes": 7')
code = code.replace('"replacement_rows": 25, "inverse_rows": 25, "simulations": 5', '"replacement_rows": 5, "inverse_rows": 5, "simulations": 1')
code = code.replace('"live_bindings_unchanged": 45, "candidate_bindings_unchanged": 15', '"live_bindings_unchanged": 9, "candidate_bindings_unchanged": 3')
code = code.replace('"live_scope_of_work_paths_absent": 5, "mapping_rows": 151, "source_lines": 1343', '"live_scope_of_work_paths_absent": 1, "mapping_rows": 33, "source_lines": 301')
code = code.replace('"replacement_rows": 25, "inverse_rows": 25, "apply_target_rollback_simulations": 5', '"replacement_rows": 5, "inverse_rows": 5, "apply_target_rollback_simulations": 1')
code = code.replace('WORKING-P2-PKG06/children/VERIFY-B1/', 'WORKING-P2-PKG08/children/VERIFY-B2/')
code = code.replace('# VERIFY-B1 Containment', '# VERIFY-B2 Containment')
code = code.replace('`DEL-06-01..05`, completed in numeric order.', '`DEL-08-06`, completed in numeric order.')
code = code.replace('45/45; candidate bindings unchanged: 15/15.', '9/9; candidate bindings unchanged: 3/3.')
code = code.replace('all five members.', 'the member.')
code = code.replace('five live SOW paths remain absent.', 'the live SOW path remains absent.')
code = code.replace('complete fifth-member evidence', 'complete member evidence')
code = code.replace('# VERIFY-B1 Attempts', '# VERIFY-B2 Attempts')
code = code.replace('all five members', 'the member')
code = code.replace('# VERIFY-B1 Return', '# VERIFY-B2 Return')
code = code.replace('`DEL-06-01..05`', '`DEL-08-06`')
code = code.replace('Members: 5/5.', 'Members: 1/1.')
code = code.replace('Fresh conversion: 10/10', 'Fresh conversion: 2/2')
code = code.replace('Fresh finalization: 10/10', 'Fresh finalization: 2/2')
code = code.replace('Preservation: 151/151 mappings and 1,343/1,343 physical source lines.', 'Preservation: 33/33 mappings and 301/301 physical source lines.')
code = code.replace('Validation: 5/5 authorized isolated-dual workspaces and 5/5 standalone clean', 'Validation: 1/1 authorized isolated-dual workspace and 1/1 standalone clean')
code = code.replace('Deterministic consumers: 10/10 production-bound maps/parity runs, 10/10 checklists, and 10/10 renders', 'Deterministic consumers: 2/2 production-bound maps/parity runs, 2/2 checklists, and 2/2 renders')
code = code.replace('Fail-closed probes: 35/35 pass.', 'Fail-closed probes: 7/7 pass.')
code = code.replace('Replacement evidence: exact 25 forward rows, 25 inverse rows, and five apply/target/rollback simulations pass.', 'Replacement evidence: exact five forward rows, five inverse rows, and one apply/target/rollback simulation pass.')
code = code.replace('Post-state: 45/45 live and 15/15 candidate bindings unchanged; five live SOW paths remain absent.', 'Post-state: 9/9 live and 3/3 candidate bindings unchanged; the live SOW path remains absent.')
code = code.replace('Post-state: 45/45 live and 15/15 candidate bindings unchanged; the live SOW path remains absent.', 'Post-state: 9/9 live and 3/3 candidate bindings unchanged; the live SOW path remains absent.')
code = code.replace('standalone clean `SOW_V1` candidates pass.', 'standalone clean `SOW_V1` candidate passes.')
exec(compile(code, str(template), "exec"), {"__name__": "__main__", "__file__": str(template)})
