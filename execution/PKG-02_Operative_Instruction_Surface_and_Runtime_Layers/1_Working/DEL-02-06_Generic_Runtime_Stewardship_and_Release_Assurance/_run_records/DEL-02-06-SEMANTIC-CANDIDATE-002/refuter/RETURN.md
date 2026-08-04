# REFUTER return — DEL-02-06-SEMANTIC-CANDIDATE-002

- ChildInstanceID: `REFUTER-DEL0206-SEMANTIC-CANDIDATE-002`
- Agent form: genuinely fresh bounded ephemeral Agent 2 generalist
- Review posture: independent read-only semantic refutation; no repair
- Verdict: `RETURN_TO_AUTHOR_OR_HUMAN_GATE`
- Material findings: `2`
- Candidate writes: `NONE`
- Sole refuter write: this return

## Frozen review subject

All seven frozen review-subject hashes independently reproduced exactly:

| Frozen file | SHA-256 | Result |
|---|---|---|
| `candidate/AFFECTED_CLIENT_CENSUS_CANDIDATE_V1.md` | `6578357f894cb30243764b512593ab2b1856675b0ac34d2cac513b235320061e` | `MATCH` |
| `candidate/DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V1.md` | `60522ec49032c15b62aab86405b113eac5e46d08dca1054af759313e05843b5f` | `MATCH` |
| `candidate/EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V1.md` | `00fb1b716efcd61fb9a4fefd4438c9406f17c0938ae9113cfef5bcf574af8480` | `MATCH` |
| `candidate/OWNER_DECISION_RECORD_CANDIDATE_V1.md` | `64882a27df256f85b5c105b691805a3f4fa208995e920b7792cfc9b8cf004ecb` | `MATCH` |
| `candidate/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md` | `5b4aff46f32432e816bcebe39984758b86d81b7f9321153d73b2de5adde0f7c4` | `MATCH` |
| `candidate/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md` | `798cebc5175d8b07c95d0bd3af390c7466b94fc7e33102ee350e0b84b1f864ba` | `MATCH` |
| `application_trace/SELECTION_APPLICATION_TRACE.md` | `bf9a17b87f273e974deaed805029f42e16a1bc6817f0e48e862e08b01ea896f1` | `MATCH` |

The candidate directory contains exactly the six planned candidate files, and
the application-trace directory contains the one planned trace. No hash drift
or membership drift was found.

## Reviewed source identities

All fourteen authority and source identities bound by the activation and
author return independently reproduced:

| Source | SHA-256 | Result |
|---|---|---|
| signed owner ruling transcript | `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06` | `MATCH` |
| accepted `ScopeOfWork.md` | `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` | `MATCH` |
| semantic patch plan | `e51075494a14576aa8d9357b6ad21928ea47065a2aa2488a02b6a4b96359cee1` | `MATCH` |
| accepted upstream handoff | `bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151` | `MATCH` |
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

Signer/date reproduce as `Ryan Tufts`, `2026-08-03`. The package manifest
contains exactly the slate, matrix, and semantic-patch-plan identities stated
above.

## Independent checks

| Check | Result | Refuter evidence |
|---|---|---|
| exact allowed census-tuple set reapplied | `PASS` | selected ordered tuple `(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)` is exact allowed member 1 of 4 |
| 27 selections, uniqueness, and trace loci | `PASS` | 27 numbered trace rows; one selected option per D1-D9, TBD-001..016, CENSUS, and COMPAT-DELTA; no missing or duplicate selected row |
| selected dependency and no-effect fences | `PASS_WITH_FINDINGS_BELOW` | trace dependencies/fences reproduce the selected patch-plan rows; two candidate-clause ambiguities remain |
| selected versus unselected semantics | `PASS` | no unselected recovery, retry, audit, transaction, drain, retained-function, quarantine, attribution, rollback, identity, comparison, mismatch, binding-shape, census, evidence-reduction, Boolean-state, or no-change option was silently substituted |
| App/client ownership | `PASS` | App remains affected only for planning and later App-owned implementation, presentation, conformance, retained-function, and evidence gates |
| PEC and Piping | `PASS` | PEC remains `UNRESOLVED` with no prescribed outcome/work/dependency/veto; Piping remains `NOT_AFFECTED` with no work/dependency |
| Tier-0 | `PASS` | preparation/routing only under a separate coordination act; no relationship record, identity, or semantic effect |
| N3 evidence posture | `PASS` | exact `DESIGN_COMPLETE_NOT_EXECUTED` posture is retained; no row is reported as executed or passing |
| compatibility delta | `PASS` | `DELTA` is conditional on later semantic adoption; no present delta, epoch, identity, binding, repin, or implementation effect |
| future epoch | `PASS` | grammar only; exact placeholder `<OWNER_SUPPLIED_FUTURE_POSITIVE_DECIMAL_EPOCH__UNRESOLVED>` remains; no `root-runtime-<digits>` value exists |
| recovery terminal/cardinality and no replay | `PASS_WITH_FINDINGS_BELOW` | distinct fifth recovery terminal, four observed forms, no automatic retry/replay/resume, and later independent-turn posture are explicit; state-transition ambiguity remains |
| audit/redaction and per-turn durability | `PASS` | append-only checkout record, immutable sorted manifest, redaction exclusions, single writer, per-turn atomic compare/append, durable summaries, final manifest, crash convergence, and readiness hold are present |
| drain/blocker and attribution | `PASS` | mutually exclusive proven-local numeric ledger and ambiguous-attribution blocker ledger cover every unresolved accepted turn; acceptance-time provider/engine/model/locality/epoch is required and inference forbidden |
| malformed evidence | `PASS` | exact-unit byte preservation/quarantine, safe diagnostics, no repair/winner inference, and global consequential hold are present |
| ten-condition identity/precedence | `PASS` | ten distinct codes, common envelope, deterministic first blocker, complete safely observable redacted audit, and retry false are present |
| retained functions | `PASS` | three named diagnostic families are conditional on proof of no mutation/truth; consequential and mutating routes/direct entries are blocked; client ownership is retained |
| irreversible rollback | `PASS` | rollback is allowed only before the first accepted recovery mutation; afterward old-reader proof or separately approved forward repair is required; evidence and separate Git/deployment gates remain |
| implementation/release/reliance boundaries | `PASS` | semantic-byte acceptance, fresh refutation, lawful profile/check authority, implementation, client conformance, cutover, lifecycle, release, reliance, Git, and foreign-owner gates remain separate |

## Findings

### REFUTER-F01 — incomplete transition relation for a pre-scan blocker

- Severity: `MAJOR — ADMISSION_BLOCKING`
- Selected basis: `TBD-016-A` requires the four explicit states, distinct
  corpus classes, and their transitions; D4 also requires ambiguous writer
  ownership to fail closed without mutation.
- Evidence/locus:
  `candidate/ROOT_RECOVERY_SEMANTIC_CANDIDATE_V1.md`, `## Daemon recovery state
  machine`, state table and precedence paragraph. `RECOVERY_REQUIRED` permits
  only exit to `RECOVERY_SCANNING` after single-writer ownership and exact
  basis are established. `RECOVERY_BLOCKED` nevertheless lists ambiguous
  ownership as an entry cause, and the immediately following precedence rule
  says an unsafe writer blocks. The candidate states neither an initial-state
  precedence nor a permitted `RECOVERY_REQUIRED -> RECOVERY_BLOCKED`
  transition for failure to establish safe ownership/basis.
- Consequence: the same pre-scan ownership failure can be read as indefinitely
  remaining `RECOVERY_REQUIRED`, directly entering `RECOVERY_BLOCKED`, or
  taking an unlisted transition. The claimed exact state machine is therefore
  not deterministic at a selected fail-closed boundary, and implementations
  could expose different machine states/envelopes for the same corpus basis.
- Disposition: return to AUTHOR for a new immutable candidate version, or to
  the human gate if choosing the transition is treated as a new semantic
  ruling. REFUTER does not select or repair the transition.

### REFUTER-F02 — compatibility manifest does not unambiguously bind the complete semantic contract set

- Severity: `MAJOR — ADMISSION_BLOCKING`
- Selected basis: `TBD-004-A` requires one immutable *complete* binding
  manifest for contract, source, release, clients, evidence, and disposition;
  `COMPAT-DELTA-A` requires that complete binding before implementation.
- Evidence/locus:
  `candidate/ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V1.md`,
  `## Compatibility binding record`, item 1 expressly requires the SHA-256 of
  “this accepted contract,” while item 5 refers generally to a “complete Root
  semantic/regression evidence bundle.” It does not expressly require the
  identities of all accepted contract-bearing members of this six-file
  semantic package (at minimum the recovery, degraded-mode, census,
  evidence/cutover, compatibility, and owner-decision bytes), nor bind an
  exact six-file candidate-package manifest.
- Consequence: a future manifest could satisfy the literal enumerated list
  while binding the epoch to the compatibility document and evidence bundle
  but omitting one or more accepted semantic-contract surfaces. That permits
  source/release/client evidence to be paired with an incomplete or mixed
  semantic package, contrary to the selected complete-binding posture.
- Disposition: return to AUTHOR for an unambiguous complete contract-byte
  membership requirement in a new immutable candidate version, or to the
  human gate if package membership is intentionally narrower. REFUTER does
  not choose or repair the binding scope.

## Blockers and reruns

- Admission blocker: `REFUTER-F01` must be dispositioned.
- Admission blocker: `REFUTER-F02` must be dispositioned.
- Required rerun after any revised bytes: reproduce all source identities;
  reapply the exact four-member census-tuple gate; repeat 27/27
  selection/dependency/no-effect review; repeat state/precedence,
  binding-completeness, boundary, and no-implementation refutation; then
  produce a new immutable candidate manifest and manager fan-in.
- No implementation, software check, client conformance, cutover, lifecycle,
  release, reliance, Git, notice, register, dependency, or foreign-loop work
  is released by this return.

## Required verdict

`RETURN_TO_AUTHOR_OR_HUMAN_GATE`

The exact frozen candidate is not admitted for human semantic-byte review
because two selected clauses remain materially ambiguous. This return makes
no repair and confers no acceptance or implementation effect.
