# Fresh Review — N2 D-GOV-34 / D-GOV-35 SHA Backfill

Verdict: `PASS — ZERO ACTIONABLE N2 FINDINGS`

Review basis: `origin/main@8635e40995b05f494ae35c6083dabdd50068bb52`

Review posture: independent, bounded, non-delegating Agent-2 review. No N2
governed output was modified. This review is evidence only; it is not
publication, merge, lifecycle, release, or reliance authority.

## Git-act identity verification

### D-GOV-34

The three backfilled values are established by the recorded Root evidence and
the repository's exact Git objects, without semantic-content inference:

| Slot | Value | Verification |
| --- | --- | --- |
| `CandidateSHA` | `8e704f2b63302c8568c48f8fee7c4681e3ec4262` | Receipt 113 lines 3689–3695 identifies this exact commit as the N3 act that authored and registered D-GOV-34. The originating run `VALIDATION.md` lines 15–16 and `HANDOFF_STATE.md` line 9 repeat it. The object resolves as a commit. |
| `PublicationSHA` | `d1a53697e6b7f54dcdb5862357bd0b395f51fff2` | The commit resolves as `record receipt 113 and root handoff`, descends from the candidate, and is the second parent of the recorded PR #607 merge. Receipt 113 lines 3703–3708 and the run `VALIDATION.md` lines 40–46 establish that PR #607 publication was to use the final head after the receipt commit. |
| `EffectiveSHA` | `9f95250e4091a789ca82fb207deec6471d7044d1` | The object resolves as `Merge pull request #607 from sgttomas/codex/root-del0206-acceptance-governance-20260821` with PublicationSHA as its second parent. It is an ancestor of Receipt 114's branch basis `main@6b0c5219…` recorded at lines 3715–3720 and of the Phase-0c basis. |

Ancestry checks pass candidate → publication → effective. The N2 return
correctly leaves the D-GOV-34 `Status` and historical publication-posture
prose unchanged because the steer prescribes no replacement status for that
record and confines the record diff to its SHA slots.

### D-GOV-35

The record and register reproduce the steer-prescribed values exactly:

- `CandidateSHA`: `294e846bc762b96ac780d49f0137f61eb4dde779`
- `PublicationSHA`: `ade6ecf33d4e10dab1441aeedb240061e140ff1b`
- `EffectiveSHA`: `8deca1489a3e5921288f71d4960d555e183a6f3f`
- `Status`: `RULED — APPLIED 2026-08-22; EFFECTIVE 8deca1489…`

All three objects resolve as commits. Candidate is an ancestor of
PublicationSHA, and PublicationSHA is the second parent of the PR #622 merge
object. The live register changes only the D-GOV-35 row; D-GOV-34's row is
byte-identical to basis because it carried no affected SHA or status text.

## Diff shape and output identities

- D-GOV-34 changes exactly three removed and three added lines: the three SHA
  slots only.
- D-GOV-35 changes exactly four removed and four added lines: the prescribed
  status slot and three SHA slots only.
- `_REGISTER.md` changes exactly one removed and one added line: the D-GOV-35
  row only.

| Path | SHA-256 |
| --- | --- |
| `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md` | `e300923a42a233619c9425b324ad309d79d8441e0613e4408e29ca17a294d3f2` |
| `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` | `e7c1e532a9d46cdc27957c85003515c46b5193e21438c905cf1cfb4e56433efa` |
| `docs/governance_harness/_DECISIONS/_REGISTER.md` | `a9ffd0e3c07300bd22080ddc65bb1f10c834f8c7220092afd9a457b0349f1882` |
| `docs/governance_harness/tranche_manifests/ROOT-DGOV34-DGOV35-SHA-BACKFILL-2026-08-23.yaml` | `91841b2ec68a8522129902ab90068e19d2008cc41e13b0863351ee2c49dd1609` |

## Manifest and authority checks

- Schema is exactly `instruction-tranche-manifest/v1`; basis is current
  branch-time main `8635e40995b05f494ae35c6083dabdd50068bb52`.
- Parsed `m2_gate.authorization` is byte-identical to the complete Phase-0c N2
  steer section: `1799` bytes on each side.
- `merge_gate` is `human-gated-pr`; `self_merge` is false.
- M6 is `pending` with `routed_to: []`.
- `exports/chirality-app/**` is explicitly deferred with no export write.
- `instruction_surface_paths` covers the two decision records, the sole
  changed register row's file, and the new manifest itself—every N2
  instruction-surface change.
- Direct `validate_manifest` returns `failures=[]`; its sole note is the
  expected non-blocking pending-M6 notice.

## Reproduced validation and containment

| Check | Result |
| --- | --- |
| `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` | PASS; 45 manifests schema-valid. As expected before the N2 commit, the range contains 0 changed paths and 0 added covering manifests; parent must rerun after commit. |
| Direct `validate_manifest` on the new manifest | PASS; `failures=[]` |
| `validate_agent_instructions.py` | PASS; 34 files, 0 errors, 0 warnings |
| `validate_instruction_entrypoints.py` | PASS |
| N2-scoped `validate_candidate_whitespace.py --base-ref origin/main --paths ...` | PASS |
| `git diff --check` | PASS |
| Git object/type/parent/ancestry checks for all six Git-act SHAs | PASS |
| `git diff origin/main -- AGENTS.md agents` | empty |

Basis `AGENTS.md` remains byte-identical at SHA-256
`377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`;
no file under `agents/**` differs. N2 governed writes are confined to the four
declared content paths, with control-plane evidence confined to its instance
folder.

The unscoped whole-worktree whitespace invocation currently reports trailing
spaces only in N1-owned untracked
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Gate_3_Exact_Amendment.diff`.
The N2-scoped invocation passes, so this concurrent N1 condition is not an N2
finding. Integrated closeout still requires the owner's prescribed unscoped
validator to pass after all node repairs and commits.

## Findings and return

Actionable N2 findings: `0`.

N2 is ready for serialized parent fan-in and commit after N1. The exact
CI-form G4 command must be rerun after the N2 commit so the committed candidate
range, added manifest, and four instruction-surface paths are assessed.
Receipt 116, integrated validation, push, and human-gated PR remain parent
work. Merge is not authorized.
