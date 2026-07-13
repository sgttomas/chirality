# Root Stage-1 Checks

Basis: `codex/sow-stage1-execution` from
`main@2770fda4c63c98ee9f18cffbafd14c9aa59f497f`.

| Check | Result |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tools` | PASS; 782 passed |
| `python3 tools/practitioner_harness/harness.py self-check` | PASS exit 0; no BLOCK; pre-existing REVIEW/WARN/INFO findings retained |
| App workspace deliverable-contract scanner focused Vitest | PASS; 6/6 |
| Root independent ten-candidate validator/parity/render reproduction | PASS; 10/10 `PILOT_DUAL`, all parity PASS, repeated HTML byte-identical |
| Active HTML resource scan | PASS; no script/form/active external resource; inert preserved URL text is not an active dependency |
| Protected pilot input comparison to frozen main | PASS for all 40 source documents and ten `_STATUS.md` files |
| Main checkout | clean tracked state at `main...origin/main`; pre-existing untracked `.claude-worktrees/` preserved |

The self-check findings are the frozen repository baseline and are unrelated to
candidate pilot paths; the command's objective BLOCK contract passed. Detailed
project checks remain in the App/Piping package handoffs and commits.
