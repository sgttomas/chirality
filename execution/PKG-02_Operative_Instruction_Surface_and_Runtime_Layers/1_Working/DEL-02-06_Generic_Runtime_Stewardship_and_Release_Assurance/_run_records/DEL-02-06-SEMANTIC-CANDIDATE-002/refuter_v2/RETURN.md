# REFUTER V2 return — DEL-02-06-SEMANTIC-CANDIDATE-002

- Child role: genuinely fresh bounded ephemeral Agent 2 `REFUTER V2`
- Governing brief: `briefs/REFUTER_V2.md` plus the unchanged method and
  exclusions in `briefs/REFUTER.md`
- Review posture: independent read-only semantic refutation; no repair
- Verdict: `ADMIT_FOR_HUMAN_SEMANTIC_BYTE_REVIEW`
- Material findings: `0`
- Minor findings: `1`
- Candidate/source/history writes: `NONE`
- Sole refuter write: this return

## Frozen V2 review subject

All seven hashes declared by `validation/V2_AUTHOR_FANIN.md` independently
reproduce exactly. Candidate membership is exactly six files and the V2 trace
directory contains exactly the one frozen trace.

| Frozen file | SHA-256 | Result |
|---|---|---|
| `candidate_v2/AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md` | `2bff966d3806078472370cfd0e7f1546064660f325d4a0e2534a71a1a67c7d13` | `MATCH` |
| `candidate_v2/DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md` | `7f64cfd2ef567bbceab2d89046137b9d6fbf7ccd49920fa34a76f373547f9153` | `MATCH` |
| `candidate_v2/EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md` | `d7c1838cf244595cb287173e44b073dfe73db2bdecd9b9946e851978ed89d95a` | `MATCH` |
| `candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md` | `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c` | `MATCH` |
| `candidate_v2/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md` | `cbe36a275bfe882c575673c8c70d8598b7f0c724b96fdf9ccae962a036677bc1` | `MATCH` |
| `candidate_v2/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md` | `9b023b347dca4bd255e6c7f2fb499e5654d3ab455f90004be29dd1b545eaf5f8` | `MATCH` |
| `application_trace_v2/SELECTION_APPLICATION_TRACE.md` | `bcea5d119dc84b56edf5c3ebeb4c3b1c0d6b4be9c0f54a4ffc044ff9b7877a5c` | `MATCH` |

The V2 author return independently hashes to
`3566e9b2ea28fc0543007363ca3cbf0ab1b11a24792c8663fc312d724212e854`.
The immutable first refuter return independently hashes to
`a5340f2f7396aa3d08ff0bffe6b960abd4d15e93a70bd20d3638efa3e9408a49`.

## Authority and source identity reproduction

| Source | SHA-256 | Result |
|---|---|---|
| signed owner ruling transcript | `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06` | `MATCH` |
| accepted `ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | `MATCH` |
| semantic patch plan | `e51075494a14576aa8d9357b6ad21928ea47065a2aa2488a02b6a4b96359cee1` | `MATCH` |
| accepted upstream owner-gate handoff | `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151` | `MATCH` |
| decision-support package manifest | `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d` | `MATCH` |
| owner selection matrix | `57b27b486e4c06d23425e3dd0760904a1b4a04bf0bcf49e0610b6c677a398c92` | `MATCH` |
| owner selection slate | `35006e9e862e26bcd3356d4dc3a95bec31f7f4ca361142b0431c6e35ca9b5598` | `MATCH` |
| N2 client census | `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52` | `MATCH` |
| N3 evidence design | `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0` | `MATCH` |
| N4 recovery candidate | `5f16ca9e1a11f0035110655d400153ad5d57aeee3e25ba6032b0c91f66467bc7` | `MATCH` |
| N4 compatibility disposition | `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1` | `MATCH` |
| N4 degraded-mode delta | `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b` | `MATCH` |
| N4 open-item map | `38149d3292234a071064300c826c2707a8f6b445e878558f31c3c6c7ece66eaf` | `MATCH` |
| N4 implementation plan | `e2f4fda9fa44eff9caf3c6894b6112c4eec39fc9bbac43b8e840382fc3b17bd9` | `MATCH` |

Signer/date reproduce as `Ryan Tufts`, `2026-08-03`. The manifest membership
is exactly the slate, matrix, and semantic-patch-plan identities above.

## Exact prior-finding closure

### `REFUTER-F01` — `CLOSED`

`candidate_v2/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md`, `## Daemon recovery
state machine`, now makes every startup enter `RECOVERY_REQUIRED`; failure to
establish safe single-writer ownership or the exact corpus basis then requires
the explicit `RECOVERY_REQUIRED -> RECOVERY_BLOCKED` transition before scan or
mutation, while success requires `RECOVERY_REQUIRED -> RECOVERY_SCANNING`.
Direct initial entry, implicit stay, and unlisted transitions are forbidden.
This deterministically closes the pre-scan ambiguity using the already
selected TBD-016-A and D4-A semantics. It adds no state, authorizes no
mutation, and does not weaken fail-closed behavior.

### `REFUTER-F02` — `CLOSED`

`candidate_v2/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md`,
`## Compatibility binding record`, now requires the one binding manifest to
carry the exact SHA-256 of each of all six accepted V2 semantic-contract
members and the exact SHA-256 of the sorted immutable V2 package manifest
containing those six member entries, in addition to the already required
source, release, client, evidence, census, disposition, cutover, rollback, and
human-act bindings. Any absent, stale, mixed-version, or mismatched semantic
member or package identity makes the binding incomplete. This closes the
complete-contract-set ambiguity under selected TBD-004-A without narrowing
the selected binding posture.

Normalized V1/V2 comparison found only V1-to-V2 identifiers and references,
the two sealed finding-closure clauses, and the matching V2 trace remediation.
No unrelated semantic choice or selected-package weakening was introduced.

## Independent refutation checks

| Check | Result | Evidence |
|---|---|---|
| exact census-tuple gate | `PASS` | `(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)` is exact allowed member 1 of 4 |
| exact ordered selection and uniqueness | `PASS` | 27 numbered mappings, one each for D1-D9, TBD-001..016, CENSUS, and COMPAT-DELTA |
| dependency and no-effect fences | `PASS` | all 27 trace rows reproduce the selected patch-plan dependencies and hold current effects |
| selected/unselected separation | `PASS` | 27 selected and 27 unselected IDs and meanings are retained; no unselected option was merged |
| package membership and binding | `PASS` | exact six V2 members; F02 clause binds all six plus sorted V2 package manifest without narrowing other bindings |
| state machine and corpus classes | `PASS` | four states, eight distinct corpus classes, complete pre-scan relation, deterministic precedence, no inferred resume |
| terminal/cardinality and no replay | `PASS` | distinct recovery terminal plus four observed forms; no retry, replay, resume, resend, or inferred completion |
| audit, redaction, writer, durability | `PASS` | checkout-contained append-only audit and sorted manifest; one writer; per-turn atomic compare/append; final batch manifest; crash convergence |
| drain and attribution | `PASS` | complete mutually exclusive numeric-local and blocker ledgers; durable acceptance-time provider/engine/model/locality/epoch; no inference |
| malformed evidence | `PASS` | exact-unit byte preservation/quarantine, no repair or winner inference, global consequential hold |
| ten failure conditions | `PASS` | ten distinct codes, common envelope, deterministic first blocker, complete safely observable audit, retry false |
| retained functions and readiness | `PASS` | only proven truthful non-mutating diagnostics may remain; every consequential/mutating route and direct entry stays blocked |
| rollback and cutover | `PASS` | rollback only before first accepted recovery mutation; later old-reader proof or separately approved forward repair required |
| client and foreign boundaries | `PASS` | App remains separately owned; PEC `UNRESOLVED`; Piping `NOT_AFFECTED`; Tier-0 preparation/routing only |
| evidence posture | `PASS` | N3 remains `DESIGN_COMPLETE_NOT_EXECUTED`; no executable or pass claim |
| future epoch and compatibility delta | `PASS` | no `root-runtime-<digits>` value; exact unresolved placeholder retained; delta remains conditional on later adoption |
| implementation and authority separation | `PASS` | semantic-byte acceptance, profile/check, implementation, client conformance, cutover, release, reliance, Git, and foreign-owner gates remain separate |

No package-binding cycle, new semantic ambiguity, transition contradiction,
authority expansion, implementation implication, or client-ownership transfer
was found.

## Finding

### `REFUTER-V2-F01` — two V2 trace references name the V1 directory

- Severity: `MINOR — NON_SEMANTIC — NOT_ADMISSION_BLOCKING`
- Evidence/locus:
  `application_trace_v2/SELECTION_APPLICATION_TRACE.md`, lines 13 and 56,
  cites
  `candidate/OWNER_DECISION_RECORD_CANDIDATE_V2.md#exact-source-identities`
  and
  `candidate/OWNER_DECISION_RECORD_CANDIDATE_V2.md#selected-and-unselected-options`.
  The exact frozen V2 file is actually
  `candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md` at SHA-256
  `2ce3aeae17212c87fa60f02c96ae5cbb0e6d3b9bf2f734417039178230af2e6c`.
- Consequence: the two human-readable references do not resolve literally.
  The identities, selections, and unselected meanings themselves remain
  present, hash-bound, and independently verified in the frozen V2 owner
  record, so this does not create semantic ambiguity, missing authority,
  unselected-option leakage, or implementation effect.
- Disposition: carry this clerical defect explicitly into human byte review.
  REFUTER V2 does not repair it. If exact link-path accuracy is required for
  package closure, AUTHOR must issue a new immutable trace version and a fresh
  refuter must rehash and recheck that revised frozen subject.

## Reruns and held gates

- If any V2 candidate or trace byte changes, rerun all seven hashes, all
  fourteen source identities, exact membership, the four-member census-tuple
  gate, 27/27 selection/dependency/no-effect coverage, F01/F02 closure,
  state/precedence, complete binding, client/foreign boundaries, no-epoch,
  and no-implementation checks with a genuinely fresh refuter.
- If any accepted input or relied source drifts, return to the owning basis,
  census, integration, and handoff stages before refutation.
- Human semantic-byte review must bind the exact seven V2 hashes above and
  expressly carry or disposition `REFUTER-V2-F01`; no candidate byte is
  accepted by this return.
- Implementation, software checks, client conformance, cutover, lifecycle,
  release, reliance, Git, notice, register, dependency, and foreign-loop work
  remain held behind their separate gates.

## Required verdict

`ADMIT_FOR_HUMAN_SEMANTIC_BYTE_REVIEW`

Both original material blockers are closed, every frozen and authority hash
matches, and no material contradiction, semantic ambiguity, boundary breach,
authority expansion, or implementation implication remains. The sole minor
trace-path defect is explicit and does not prevent accountable-human review of
the exact V2 semantic bytes.
