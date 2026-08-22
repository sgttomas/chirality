# Validation — N3 D-GOV-34 and TM-ROOT-124 CHANGE Amendment

Verdict: `PASS`

AcceptedBasis: `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`

## Exact identity checks

- `git cat-file -t 33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`
  returned `commit` before preparation and again at completion.
- `git rev-parse HEAD` remained
  `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0` throughout N3 execution.
- Accepted-basis `agents/AGENT_CHANGE.md` SHA-256 reproduced as
  `950e96f4cfff13af48b9edd93a4b47356e8b388a430d70977fd528ffbd4120fa`.
- Candidate `agents/AGENT_CHANGE.md` is 17,626 bytes, Git blob
  `bbaafd3186dbdfc19751a581002e505e04b75bb7`, SHA-256
  `bb2922c5761395687caf120097276806769ec38f4fee8935d9e6c7bbb8506a06`.
- Exactly one `D-GOV-34` row exists in the live D-GOV register.
- All three routed notices contain the exact pre/post SHA-256 values.
- Scripted comparison of the owner-transcript D4 string to the D-GOV-34
  verbatim ruling block passed.

## Deterministic validation

| Check | Result |
|---|---|
| `python3 tools/validation/validate_instruction_tranche_manifest.py` | `G4 PASS`; 42 manifests schema-valid |
| `python3 tools/validation/validate_agent_instructions.py` | 34 files; 0 errors; 0 warnings |
| `python3 tools/validation/validate_instruction_entrypoints.py` | `PASS` |
| Focused three-module validator pytest | 88 passed |
| `git diff --check` | `PASS` |
| Protected-path manifest coverage | exact four changed instruction paths declared |
| Notice route existence | App, Piping, and domain-engine paths present |

Focused pytest command:

```text
python3 -m pytest -q \
  tools/validation/test_validate_instruction_tranche_manifest.py \
  tools/validation/test_validate_agent_instructions.py \
  tools/validation/test_validate_instruction_entrypoints.py
```

## Fresh independent review

Review `N3-R1-DGOV34-CHANGE` returned `PASS` with zero findings. It reran the
identity, G4, agent, entrypoint, focused-test, D4, row-count, hash, notice,
coverage, and whitespace gates. No repair or re-review cycle was required.

Review return SHA-256:
`1c4caab90b896455bc5823abd3c92be97e2019de7cbcc8ce67b9e27933f0c7f9`.

## Containment

N3 changed only its allowed D-GOV record/register row, CHANGE instruction,
manifest, three notices, and instance evidence. It did not edit a Task
Management register or receipt and performed no commit, push, PR, merge,
implementation, lifecycle, release, publication, or reliance act. Concurrent
N1/N2 paths in the shared checkout were excluded from N3 attribution.
