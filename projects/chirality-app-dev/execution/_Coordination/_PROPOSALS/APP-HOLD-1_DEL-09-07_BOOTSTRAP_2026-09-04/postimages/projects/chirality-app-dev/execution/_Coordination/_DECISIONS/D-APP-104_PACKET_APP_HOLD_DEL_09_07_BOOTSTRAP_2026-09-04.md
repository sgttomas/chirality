# D-APP-104 — APP-HOLD-1 DEL-09-07 Structural-Bootstrap Amendment

Status: `PROPOSAL — AWAITING OWNER RULING`

DecisionID: `D-APP-104`

Date: 2026-09-04

Owner: Ryan Tufts

Owning loop: Chirality App Dev

Application-payload hash-list SHA-256:
`c9e549f7c7c48f7e200b32fb112ddc754e8b0926df242ee9556e77a8cc5188e3`

Approval identity: the owner question cites the SHA-256 of
`APPROVAL_EFFECT_MANIFEST.sha256`. That acyclic root binds this packet, the
decision-register postimage, exact question/ruling templates and deterministic
transform, and the complete authoritative application contract. The root is
rendered only after all bound leaves are frozen; it is intentionally not
embedded in this root-bound packet.

Candidate directory:
`execution/_Coordination/_PROPOSALS/APP-HOLD-1_DEL-09-07_BOOTSTRAP_2026-09-04/`

## Decision requested

Whether to apply the exact APP-HOLD-1 structural-bootstrap amendment that
allows the two already owner-authorized SCA-APP-009 Gate-5 PREPARATION
preflights for not-yet-contracted `DEL-09-07`, while preserving every ordinary
hold and mechanically expiring the admission when the scope-change pointer
moves or any other pinned condition changes.

## Options

1. **Approve the exact candidate.** Apply only the frozen live postimages and
   materialize the conditional D-APP-104 ruling/register row. The two exact
   Gate-5 dispatch contexts may pass only while every pinned condition holds.
2. **Return a bounded amendment.** Keep APP-HOLD-1 unchanged and identify the
   exact condition, token, surface, or evidence that must change before a new
   candidate is prepared.
3. **Decline or defer.** Keep APP-HOLD-1 unchanged. DEL-09-07 remains unknown
   and the two PREPARATION dispatch preflights remain blocked.

## Recommendation

Approve Option 1. The candidate is narrower than a generic exception: it
admits only `DEL-09-07` / `PKG-09`, only `dispatch`, and only the exact
`CANDIDATE_MIRROR` and `ACTUAL_WORKTREE` tokens. Both approved authority
postimages, the old pointer preimage, absence of `ScopeOfWork.md`, and a
five-file-only regular-file folder shape are rechecked on every invocation.
A held target cannot use the path, and any mismatch fails closed.

## Risks and controls

- **Half-applied authority:** the admission remains dormant until both exact
  approved SCA-APP-009 authority postimages are present. Applying only the
  guard cannot admit DEL-09-07 on the preimage basis.
- **Over-broad exception:** there is no wildcard target, package, operation,
  entry path, or folder. The schema distinguishes `HOLD` from
  `STRUCTURAL_BOOTSTRAP`; a hold always wins.
- **Admission persistence:** `_ScopeChange/_LATEST.md` is hash-pinned to its
  old preimage. Pointer movement expires the admission mechanically. Contract
  appearance and authority or folder drift also expire it. Later row removal
  is separate maintenance.
- **Scaffold expansion:** the target folder may be absent or contain only any
  subset of `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`,
  and `_SEMANTIC.md`; symlinks, non-regular authorized names, nesting, and any
  extra path block.

## Validation implications

The exact candidate must pass the existing APP-HOLD regressions, new positive
checks for both tokens and absent/subset scaffold states, an adversarial
negative matrix, registered harness checks, receipt/corpus validation,
manifest verification, strict JSON/CSV parsing, and `git diff --check`.
Frontend checks are not selected because no frontend/runtime product path is
changed.

## Exact effect if approved

Approval would authorize only application of the frozen APP-HOLD-1 guard,
typed register row, project instruction, tool README, tests/fixtures,
D-APP-104 packet/ruling/register bytes, proposal package, and the later
reminted minimal loop receipt. It would let the two separately authorized
PREPARATION dispatch preflights return
`admission_kind=STRUCTURAL_BOOTSTRAP` while every condition holds.

Only the exact owner answer `Yes` to the deterministically rendered question
may materialize the conditional ruling. Non-authoritative proposal/evidence
bytes may accompany application only when the artifact-manifest SHA-256
exactly matches the fresh independent PASS report presented with that
question.

## Non-effects

Approval would not:

- authorize PREPARATION itself or create the DEL-09-07 scaffold;
- create a Scope of Work, repin any contract, or change scope authority;
- waive the Gate-5 audit, move `_ScopeChange/_LATEST.md`, or make SCA-APP-009
  current;
- alter any product, frontend, Root, plan, Task Management, lifecycle,
  release, signing, notarization, publication, distribution, or professional
  reliance surface or claim; or
- create a generic APP-HOLD bypass.

## Affected live files

The exact later application set is enumerated in the candidate
`LIVE_SURFACE_MANIFEST.csv`. No file named there changes until an owner answers
the frozen question affirmatively and the application is separately executed.
