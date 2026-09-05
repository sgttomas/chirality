# Negative fixture relocation — 2026-09-05

Basis: `4b6d2bb2c1b6e798c0000f51b38755d92055f65d`.

The ordinary APP-HOLD scan was reproduced before repair and exited 2 with
`APP_HOLD_ERROR: missing YAML front matter` at the negative fixture below.
Its canonical `ScopeOfWork.md` filename made evidence discoverable as a contract.

Paths relative to this deliverable:

- Old: `_run_records/VERIFY_2026-09-04/invalid/ScopeOfWork.md`
- New: `_run_records/VERIFY_2026-09-04/invalid/ScopeOfWork.invalid.fixture.md`
- Old and new SHA-256: `f215d66d85070116f2bbe47b119306806ece6badd47e8c70c5a23b0cc2acdff4`

The relocation preserves the fixture bytes. The production `ScopeOfWork.md`
remains SHA-256 `0773d528d62e293443c08229f2933e3d50dcfa3de4d54abcaeb23fc1c2de6ebe`.
No guard, production contract, or control was changed.

The original reviewer report, launch/return records, and negative-check command
remain historical and unedited. Their old fixture path is no longer the live
reproduction path. The earlier reported final APP-HOLD pass predated creation
of this fixture; it did not verify the fixture-inclusive state. This record
corrects that state attribution without rewriting the original evidence.

For future negative-check reproduction, create a temporary directory outside
`execution`, copy the relocated fixture there as `ScopeOfWork.md`, then run
`python3 tools/scope_of_work/derive_review_checklist.py <temporary-directory> --output <temporary-directory>/invalid-output.json`
from the repository root. Expect rejection (nonzero exit) and no output file.
Do not restore the canonical fixture filename inside `execution`.

After relocation, from the App root:

- `python3 execution/_Scripts/app_hold.py scan --require-register-match`:
  PASS, exit 0, 54 contracts, zero holds, register match true.
- `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path PROJECT_SETUP --target DEL-09-07`:
  ALLOW, exit 0, contract CLEAR and NOT_HELD.

Execution attribution: delegated-harness-native ephemeral Agent 2; role not
mechanically enforced; instruction-asserted. Non-delegation is instruction/config
asserted, not mechanism-proven. Session identifies the GPT-6 family, not an exact
model ID. This bounded repair performed no delegation. An attempted `git mv`
could not acquire the shared Git index lock under sandbox permissions; relocation
was completed with `apply_patch` instead. No commit was made by this repair agent.
