# APP-HOLD-1 Candidate — DEL-09-07 Structural Bootstrap

Status: `CANDIDATE_NOT_APPLIED_AWAITING_INDEPENDENT_REVIEW`
Revision: `R6 / remediation R2 — nonregular-fileset and receipt-evidence repair`
Prepared: 2026-09-04
Prepared by: delegated-harness-native ephemeral Agent 2 under HELPS_HUMANS
Role posture: role not mechanically enforced; governed-workflow evidence is
instruction-asserted; K-SUBAGENT/non-delegation is instruction+config
asserted, not mechanism-proven; no descendant was launched
Git preparation basis: `287b82f16c0d3970bac71e40b0e41fdd50569b08`
Preparation-basis receipt cursor: `Receipt-225`
Owner authority: prepare an exact candidate only; no application authority
Artifact class: proposal; non-authoritative until independently reviewed,
explicitly ruled by Ryan Tufts, applied, validated, and merged

## Problem

SCA-APP-009 Gate 5 must create the PREPARATION-owned structural folder for
new `DEL-09-07` before the post-change decomposition audit can pass. The
current APP-HOLD-1 tool correctly rejects `DEL-09-07` as unknown because no
`ScopeOfWork.md` exists. The accepted PREPARATION sequence intentionally does
not create a Scope of Work, so ordinary contract discovery cannot make the
preflight known without defeating the structural-only boundary.

The live preimage remains coherent: 53 contracts, no active holds, header-only
register, and unknown `DEL-09-07` rejected. The exact approved SCA-APP-009
decomposition and companion postimages and the old pointer preimage were
independently recomputed at preparation. An exact-one-ref
`git ls-remote --refs origin refs/heads/main` check fixed current main at the
preparation basis. PR #700 changes five plan-only paths and has no overlap with
any of the 61 future application paths.

## Proposed mechanism

Extend the APP-HOLD register with explicit record kinds:

- `HOLD` retains the complete existing scan-authoritative behavior. It binds
  every operation and entry path and always wins.
- `STRUCTURAL_BOOTSTRAP` is not a hold release or exception. It is a typed,
  exact admission predicate for one unknown target before contract creation.

The sole candidate row is `DEL-09-07` / `PKG-09`. It returns ordinary
`ALLOW` with `admission_kind=STRUCTURAL_BOOTSTRAP` only when all conditions
hold:

1. operation is exactly `dispatch`;
2. entry path is exactly
   `SCA-APP-009:GATE5:PREPARATION:CANDIDATE_MIRROR` or
   `SCA-APP-009:GATE5:PREPARATION:ACTUAL_WORKTREE`;
3. the live decomposition SHA-256 is
   `e46084abc0f85970dbe4ed49d1366a99e9930bbb9d9bd87b86f998f98155ab97`;
4. the live companion-register SHA-256 is
   `e47fced6f0bea32b1d18f987a7e33af0432271c4ff49bb196cdad6fb91742b70`;
5. the live `_ScopeChange/_LATEST.md` SHA-256 remains
   `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`;
6. exact DEL-09-07 `ScopeOfWork.md` is absent; and
7. the exact target folder is absent or contains only any subset of
   `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and
   `_SEMANTIC.md`, each a regular non-symlink file, with no nesting or extras.

The two tokens were searched across the live repo and frozen SCA Gate-3/4/5
evidence and had no pre-existing conflicting definition.

## Fail-closed behavior

Normal ScopeOfWork scanning and hold-register parity run first. Any known held
target blocks unchanged. Unknown non-bootstrap targets remain errors. A wrong
target, package, row field, operation, token, authority hash, pointer hash,
appearing Scope of Work, unexpected/nested/non-regular path, symlink, malformed
or duplicate row, or hold collision cannot produce admission.

The row may be structurally valid but dormant on the current decomposition
preimage. This is safe: `scan --require-register-match` can confirm that the
candidate register itself is well formed, while `check` for DEL-09-07 blocks
until both approved authority postimages are actually present. No partial
application produces an admitting state.

Pointer movement, contract appearance, authority drift, or folder drift
mechanically expires admission. The row can remain inert until a separately
reviewed maintenance act removes it.

## Exact identity

- application payload hash-list SHA-256:
  `c9e549f7c7c48f7e200b32fb112ddc754e8b0926df242ee9556e77a8cc5188e3`
- approval-effect-manifest SHA-256:
  `2236de0840fde97efbbfb36ab29aa6a9e11fc839117c75beb81234852f6a9413`
- proposal-artifact-manifest SHA-256: rendered literally in
  `OWNER_QUESTION.md` and reported externally after final freeze; it is not
  repeated in an artifact-manifest leaf because that would create a digest
  cycle
- preparation basis: `287b82f16c0d3970bac71e40b0e41fdd50569b08`
- receipt basis cursor: `Receipt-225`; the application receipt is
  `NEXT_AVAILABLE` and must be reminted from the later live cursor

`APPROVAL_EFFECT_MANIFEST.sha256` is the acyclic owner-approval root. It binds
every authoritative later live effect, the deterministic question/ruling
transform, and the complete application contract without containing its own
digest. `PROPOSAL_FILESET.txt` and one literal manifest row per proposal file
make omission detectable. `ARTIFACT_HASHES.sha256` separately binds every
proposal file except exactly itself and the two digest-dependent deterministic
outputs: the rendered owner question and rendered ruling postimage. Its own
digest must be independently reported and is inserted into both excluded
outputs by the bound renderer. `COMPLETE_CANDIDATE.diff` is an all-binary Git
patch over the exact current basis and excludes its own bytes, the subsequently
generated artifact manifest, and those two rendered outputs. Applying its 53
static paths, adding the two manifest/patch files, and rendering the two outputs
reconstructs all 57 intended candidate paths exactly.

Every Python preparation, review, application, and PR-head check is required
to suppress bytecode writes or use an absolute cache prefix outside the
worktree. The exact proposal-file-set verification rejects symlinks and every
observed entry that is neither a directory nor a regular file, with a
path-naming diagnostic. It is the last filesystem-sensitive check before
staging, preventing ignored cache, bytecode, FIFO, or other nonregular
artifacts from escaping the literal inventory gate.

## Remediation R2 disposition

The immutable artifact-remediation review R1 at
`/private/tmp/chirality-app-v3-app-hold-bootstrap-20260904/remediation/reviews/REVIEW_REMEDIATION_R1.md`
has SHA-256
`39e43788ea83d1f44d8526976bd2e0c850af2d1a1209d8f151c6b20296fb909e`
and returned `FAIL` with zero BLOCKER and two MAJOR findings.

| Finding | R6 disposition |
| --- | --- |
| M-1 — observed proposal fileset silently ignored a FIFO or other nonregular entry | Remediated without scope expansion. The renderer now rejects every entry that is neither a directory nor a regular file after its existing symlink rejection, names the offending relative path, and has a POSIX FIFO regression plus an injected verifier check. |
| M-2 — simulated future receipt used invalid `SIMULATION_ONLY` Gate-Outcome | Remediated in evidence only. The disposable future application uses lawful provisional `AWAITING_OWNER`, explicitly disclaims authority and every unperformed act, passes receipt and harness validation, and is never appended live. Any actual later application still remints `NEXT_AVAILABLE` from the then-live cursor and uses `EXECUTED` only when true. |

Neither finding required approval-model redesign, expanded authoritative bytes,
or a changed 61-row future scope. The approval root and artifact digest are
nevertheless newly reminted because M-1 changes a bound renderer leaf and
artifact evidence bytes. The prior R5 digest pair supplies no authority.

## Application boundary

The candidate modifies APP-HOLD instruction/tool/register/test surfaces and
adds D-APP-104 decision records plus this frozen proposal. It does not modify
the SCA authority postimages, pointer, DEL-09-07 folder, any Scope of Work,
product/frontend, Root, plans, Task Management, or release surface.

The later application may land first on `main` in a dormant state. After that
merge, the SCA-APP-009 Gate-5 worktree must rebase onto the merged guard,
reverify all identities, and apply its separately authorized decomposition and
companion postimages before either PREPARATION preflight can admit. The
disposable candidate mirror receives byte-identical guard inputs for its own
preflight; it is not a second authoritative application.

## Non-effects

This candidate does not create a sixth Scope of Work, repin anything, waive
the decomposition audit, change scope authority, authorize PREPARATION,
create DEL-09-07 files, move `_LATEST.md`, make SCA-APP-009 current, or
authorize downstream work. It changes no product, frontend, Root, plan, Task
Management, lifecycle, signing, notarization, publication, distribution,
release-readiness, certification, or professional-reliance state or claim.

Preparation, tests, review, Git state, and merge evidence are not owner
acceptance. Only the frozen owner question and an affirmative owner response
can authorize later application.

## Historical approval preserved, not reused

The prior exact owner question was the R4 `OWNER_QUESTION.md` question:

> Do you approve and authorize application of the D-APP-104 authoritative
> live-effect set rooted at the approval-effect-manifest SHA-256 cited above?
> That root binds the exact eight-file
> APP-HOLD payload, D-APP-104 packet and decision-register postimage, this
> question template, the conditional ruling template and deterministic render
> transform, the literal live-surface and proposal-file-set contracts, the
> integration contract, and complete application/rollback instructions. It
> does not identify the non-authoritative proposal evidence bytes; those may
> be added only when their separate artifact-manifest SHA-256 exactly matches
> the fresh independent PASS report. Approval remains limited to the two
> SCA-APP-009 Gate-5 PREPARATION dispatch contexts and expires mechanically
> when `_ScopeChange/_LATEST.md` moves, with no other authority. Please answer
> **Yes** or **No**.

Ryan Tufts answered exactly `Yes` on 2026-09-04 for approval root
`4f0f72d14ffbabd1fd9e5ed47d911fd95cbf3ffe98c32a1b0b5d966572e7c139`
and proposal-artifact-manifest digest
`091817d7107f91b9175470b6c6a6403240c52dcb2e86a180d282b6fddeae622c`.
Those exact bytes and that answer remain dated historical evidence. They do
not authorize this replacement artifact, its new digest pair, or a second
application. A fresh independent PASS and a new exact owner answer `Yes` to
the replacement two-digest question are mandatory.
