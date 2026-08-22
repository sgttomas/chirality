# Root Governance Loop Handoff State

Four-field form per owner ruling 2026-07-31 (Receipt 72; the ruling
verbatim is in that receipt): this file carries only the fields no other
instrument lawfully holds. Posture lives in `CURRENT_WORKPLAN.md`; session
history and owner directions live in `LOOP_RECEIPTS.md`; attention residue
lives in `_TaskManagement/REGISTER.csv` (rows are never scope, acceptance,
or authority — K-TM-5). Per-run and per-phase handoff states remain inside
their run and snapshot directories per the AGENTS.md handoff-state rule.

## 1. Accepted upstream basis

- Root PRD Revision 8 (`docs/PRD_ROOT.md`), merge-gate policy per annex
  §5.3.1 as simplified 2026-07-29 (Receipt 64).
- Root SOFTWARE decomposition revision 1.2 (SCA-002 applied 2026-07-29;
  snapshot `execution/_ScopeChange/SCA-002_2026-07-29_0800/`). All 46
  deliverables `INITIALIZED`; none activated.
- Chirality Task Management PRD Revision 2, adopted by D-GOV-32 (subject
  SHA-256 `97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`,
  effective `main@c1156837f`); K-TM-1..6 ratified at `docs/CONTRACT.md`
  §1.14 (effective `main@c8c2a6146`). Stage-A instruments: Receipts 66–73;
  workplan `WORKPLAN_2026-07-31_task_management_stage_a.md` (CLOSED) and
  its Amendments 1–2; program register at
  `execution/_Coordination/_TaskManagement/REGISTER.csv` (21 live rows:
  11 OPEN / 10 DEFERRED; 104 rows archived in `REGISTER_CLOSED.csv`). Receipt
  91 repaired the earlier stale handoff to the then-current generational-pass
  state of 27 live (16 OPEN / 11 DEFERRED) and 95 archived. Receipt 92 then
  recorded the separately owner-ruled closure and archival of TM-ROOT-105,
  TM-ROOT-109, and TM-ROOT-121, producing 24 live (13 OPEN / 11 DEFERRED) and
  98 archived. Receipt 96 subsequently recorded the accepted-repair closure
  and archival of TM-ROOT-112, producing 23 live (12 OPEN / 11 DEFERRED) and
  99 archived. Receipt 102 then recorded the 2026-08-08 generational pass:
  one DEFERRED promotion followed by three owner-ruled closures/archives,
  producing 21 live (12 OPEN / 9 DEFERRED) and 102 archived. This
  2026-08-09 bounded currentness session independently re-derived those
  entry counts from the CSVs; the owner-ruled deferral of TM-ROOT-119 then
  changed only the live split to the current 11 OPEN / 10 DEFERRED, leaving
  the validated totals at 21 live / 102 archived. The immediately following
  owner-directed evidence-pin class closure changed only `EvidenceSha` and
  Notes on archived `TM-ROOT-109` and `TM-ROOT-121`; counts remain 21 live /
  102 archived and neither row was re-closed or reinterpreted.
- Receipts 107 and 109 subsequently promoted `TM-ROOT-124` and
  `TM-ROOT-125`, producing 23 live / 102 archived. Receipt 110 then records
  the owner-directed validator/frontmatter tranche and the sole closure of
  `TM-ROOT-125` as `RESOLVED_WITH_CHANGE`, producing 22 live
  (`OPEN=12`, `DEFERRED=10`) / 103 archived. Receipt 111 then records the
  owner-selected Option-R re-scope and the sole closure of `TM-ROOT-117` as
  `RESOLVED_BY_DECISION`, producing 21 live (`OPEN=11`, `DEFERRED=10`) / 104
  archived. Receipt 112 then records the owner-directed closure/archive of
  `TM-ROOT-116` and creation of attention-only `TM-ROOT-126`/`TM-ROOT-127`,
  producing the current 22 live (`OPEN=12`, `DEFERRED=10`) / 105 archived
  state. No D-APP-48 successor identity was accepted.
- Stage-A trailing merges (step 8, closure) record their own approved and
  effective SHAs in their PRs and Receipts 72–73 per §5.3.1.
- D-GOV-33 invocation-local federation-survey ruling and completed managed
  run at
  `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/`
  (Receipts 82 and 85). The validated implementation commit is
  `bb44d71c93cc5431d5fc8a902e716cc88966ea9f`; PR #478 published exact
  approved source `08ed85ae1a1ae2be9eba971e6567fad2bb202b56` from final base
  `4d55dea0f375034b66949723a7b849a2c962d8a3`, effective at merge
  `2c25bd2c47c4b2f4190275ad39579a983f8786aa`. All three required checks
  succeeded; the checked-PR publication lane is closed.

## 2. Derivative-package currency

- `execution/_Coordination/_TaskManagement/.candidates/` — taskmgmt scan
  and federation projections: gitignored, rebuildable, never authority
  (D-GOV-01). Project/domain/Domain Engine federation projections follow the
  same beside-register `.candidates/` rule.
- `/tmp/TM-FEDERATION-SURVEY-20260802-*.json` and verifier/acceptance copies —
  historical pre-publication validation evidence; derived, disposable, and
  not accepted register truth.
- `TRIAGE_2026-07-31_SEED_PROPOSALS.md` and
  `AgentRuns/GOV-TM-TRIAGE-CLUSTER-20260731/` — historical decision
  support and run evidence for the first triage; not current state.
- Public export under `exports/chirality-app/` — stale derivative,
  deferred to the next export release (posture unchanged since SCA-002).
- Current Root Task Management decision support under
  `execution/_Coordination/_TaskManagement/`: TM-ROOT-116 is now archived
  `RESOLVED_WITH_CHANGE` against the exact live Step-0 workplan bytes;
  TM-ROOT-126/-127 are attention-only OPEN rows; and the current session
  report prepares, but does not rule, promotion of trigger-fired TM-ROOT-035
  and TM-ROOT-042. The report is derivative closeout support, not authority.
- `EVIDENCE_PIN_CLASS_CLOSURE_2026-08-09.md` is derivative audit evidence for
  the owner-ruled `TM-ROOT-109`/`TM-ROOT-121` mechanical re-pins. Its
  class-complete sweep found 11 exact-path-resolvable single-hash rows: 11
  current after repair and zero mismatches. The separately prepared
  `OWNER_SOURCED_CANDIDATE_2026-08-09_EVIDENCE_PIN_CURRENCY_VALIDATION.md`
  is unpromoted decision support for the next owner slate.
- Candidate-harvest provenance is split explicitly: the owner accepted the
  7,006-byte `bee380de…3cab` report; the repository path carries a later
  six-byte whitespace cleanup at `3ca25470…bac1`. The exact reversible delta
  and rationale are in
  `AMENDMENT_2026-08-09_CANDIDATE_HARVEST_POST_ACCEPTANCE_WHITESPACE.md`.
  The cleaned version is not treated as freshly accepted.
- `AgentRuns/ROOT_DEL0206_CHANGE_HOUSEKEEPING_2026-08-21/` is the current
  derivative run package. Its exact-byte and Task Management slate is decision
  support only. Historical App DEL-09-06 instruction-root evidence and the
  D-APP-86 parity baseline remain immutable historical evidence.

## 3. Closure verdict

`TASK MANAGEMENT STAGE A CLOSED — ROOT LOOP IDLE AND RESUMABLE.`
Steps 0–6 complete with owner rulings recorded and merged; step 7 packets
presented on all three loop surfaces with rulings deliberately trailing to
the individual development loops (owner direction, Receipt 72); step 8
shipped. PRD §19.1 falsification clause satisfied (seed triaged in the
first session, 46/101 closures). No root production phase is active;
Task Management runs on demand or owner-scheduled routine via
TASK_MANAGEMENT — never bound to loop entry.

`FEDERATION SURVEY COMPONENT PUBLISHED AND EFFECTIVE — PR #478 CLOSED.`
HELPS_HUMANS and TASK_MANAGEMENT both returned `READY`; all four validation
surveys were `COMPLETE` with unchanged register hashes. D-GOV-33, the shared
agent/tool, tests, manifest, and notices became repository state at effective
merge `2c25bd2c47c4b2f4190275ad39579a983f8786aa` after all required checks
succeeded.

`2026-08-09 BOUNDED GOVERNANCE-CURRENTNESS SESSION CLOSED — ROOT LOOP IDLE AND
RESUMABLE.` Receipt 103 records the terminal Task Management breadcrumb.
TM-ROOT-119 is ruled DEFERRED and recorded verbatim, with no partial
convergence implementation. The stale register counts are refreshed above.
The owner-accepted Step 0 is applied to the standing idle workplan while
`CURRENT_WORKPLAN.md` remains unchanged; TM-ROOT-116 remains OPEN pending
later disposition after publication/merge evidence. Archived TM-ROOT-105 now
pins the current normalized bytes with both-hash/commit provenance; its
EvidenceRef, Disposition, Closed date, EvidenceQuote, ruling text, and closure
meaning are unchanged, and this was not a re-close. The bounded tranche is on
`codex/root-governance-currentness-20260809` for CHANGE publication by
non-draft PR; commit, push, PR, and merge are not closeout facts at this
handoff, and merge remains prohibited in-session.

`2026-08-09 EVIDENCE-PIN CLASS CLOSURE COMPLETE — ROOT LOOP IDLE AND
RESUMABLE.` The owner-stated finding reproduced exactly. Archived
`TM-ROOT-109` and `TM-ROOT-121` now pin the current transcript bytes with the
same both-hash/commit provenance as the `TM-ROOT-105` Option-A precedent;
their evidence refs, dispositions, closed dates, evidence quotes, and closure
meanings are unchanged. The class-complete committed-byte sweep is clean for
all 11 mechanically pinnable rows. The validator-currency gap is prepared as
an owner-sourced candidate only; it is not promoted, folded, disposed, or
implemented. Publication remains on PR #532 at the accountable human's merge
gate; no merge is authorized in-session.

`PR #532 PROVENANCE HOLD — OWNER RE-VERIFICATION REQUIRED.` Receipt 106
corrects the harvest identity handling without editing Receipt 104. The
accepted identity is `bee380de…3cab`; `3ca25470…bac1` is a distinct
post-acceptance whitespace amendment. All other tranche work remains approved
pending this repair, but merge is prohibited until the owner re-verifies.

`2026-08-21 TM-ROOT-125 ENGINEERING AND REGISTER CLOSURE COMPLETE — PR
PUBLICATION PENDING.` Engineering commit
`702d88a4c14a291f647c2a2e6e5fa40185839318` narrowly aligns the Root
validator, tests, and HELP_HUMAN metadata with the ratified Agent 0 direct
canonical-TASK / opted-in-generalist doctrine while preserving the other
fail-closed paths. `TM-ROOT-125` is archived `RESOLVED_WITH_CHANGE` under the
owner's explicit in-session direction; Receipt 110 and
`_TaskManagement/CLOSEOUT_2026-08-21_TM-ROOT-125.md` carry the closure.
Required App/Piping/domain coordination notices are routed. No App adoption,
semantic acceptance, lifecycle, release, reliance, PR approval, or merge is
inferred. Older Agent-1-only narrative in `docs/TYPES.md` §4.3,
`docs/WORKFLOW_COMPONENT_STANDARD.md` §4.1, and
`docs/DBM_Agent_Instruction_Architecture.md` §2 remains a separately recorded
Root concordance residual.

`2026-08-21 PR #602 BASIS REPAIR AND CARRIER RULINGS COMPLETE — OWNER REVIEW
AND MERGE REMAIN.` Receipt 111 binds the exact four-file correction from the
nonexistent basis SHA to existing commit
`e3e18d27740018efd12e73193c02395a9eca93c2`; archives `TM-ROOT-117`
`RESOLVED_BY_DECISION`; and routes the exact App trigger-re-scope notice with
no successor identity accepted. The owner also supplied DEL-02-06 epoch `1`,
yielding preparation candidate `root-runtime-1`, and authorized one sealed
preparation-only WORKING_ITEMS activation against accepted snapshot
`3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`.
That activation and all candidate output are excluded from PR #602 and must
run as a separate tranche/PR; exact prepared bytes and SHA-256 return to a
later owner acceptance gate.

`2026-08-21 DEL-02-06 COMPATIBILITY PREPARATION AND ROOT HOUSEKEEPING COMPLETE
WITH NODE-2 AUTHORITY BLOCKER — PR #605 OPEN.` Receipt 112 records exact
candidate bytes SHA-256
`e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`,
fresh zero-finding refutation, REM-001 satisfaction with lifecycle remaining
`INITIALIZED`, TM-ROOT-116 closure, and attention-only TM-ROOT-126/-127.
TM-ROOT-035/-042 are trigger-fired but unchanged pending owner rulings.
TM-ROOT-124 remains OPEN because its Assignment names no exact D-GOV identity;
no CHANGE instruction tranche or notices landed. Candidate-byte acceptance,
implementation, lifecycle promotion, release, publication, reliance, PR
approval, and merge remain human-gated.

## 4. Rerun requirement

Refresh this file only when a phase boundary moves: a Stage-B packet is
ruled in a development loop (that trigger has fired — D-APP-83, D-63, and
D-PEC-73 are ruled and TM-ROOT-098/099/100 are closed; the register-count
refresh above records it), a Root
production phase or DEL-02-06 activation is selected, the accepted
decomposition or PRD revision changes, or the owner selects a successor
posture other than idle.

The federation-survey rerun and publication requirement was discharged by
PR #478 (Receipts 82 and 85). No further action is required for that tranche.
Rerun its validation and federation matrix only if the shared Task Management
instruction/tool contract or canonical register-discovery shapes change.

TM-ROOT-116 is closed under the exact 2026-08-21 owner direction and requires
no later disposition-by-inference. Rerun Root live/archive register validation,
invocation-local federation,
available App/Piping receipt validators, Root G0–G4, candidate-whitespace, and
Git diff hygiene if publication rebasing changes any tranche byte. The
repository still has no Root-specific receipt validator at this basis; do not
misstate the App/Piping validators as Root coverage. Manual closeout checks
confirm Receipt 103 is append-only, unique as a new ID, and follows the latest
Receipt 102; they also expose two pre-existing historical headings numbered
Receipt 80. That historical duplicate was not created or altered here and is
outside this bounded repair. The loop remains idle; release requires a
separately authorized bounded lane or an owner-selected successor phase.

Present the prepared evidence-pin-currency candidate with the next owner
slate. Do not mint a new row, fold it into `TM-ROOT-113`/`TM-ROOT-115`, or
implement validator changes until the owner rules. Repeat the exact-path
class sweep if any later tranche changes Root evidence identities or the
validator contract.

For the 2026-08-21 carrier session, the owner has now selected the
`TM-ROOT-117` re-scope option and supplied DEL-02-06 epoch `1`, yielding
candidate identity `root-runtime-1`, with authorization for one sealed
preparation-only WORKING_ITEMS activation. Close `TM-ROOT-117`
`RESOLVED_BY_DECISION` and route the reciprocal App trigger-re-scope notice in
PR #602. Run the DEL-02-06 preparation only as a separate Root session,
branch, tranche, and PR against accepted snapshot
`3fc56807c4cd83fd2b5f967848b770adfd226541880629493ddfe8ad3df989aa`;
return exact candidate bytes and SHA-256 for a separate owner acceptance.
DEL-02-06 remains `INITIALIZED` until that separately governed activation;
do not infer package acceptance, implementation, lifecycle, release,
publication, reliance, or foreign-loop disposition.

For Receipt 112 / PR #605, return the exact candidate bytes and SHA-256 to the
owner for `ACCEPT_EXACT_BYTES | RETURN_EXACT_BYTES | DEFER_EXACT_BYTES`; do not
infer selection. Independently return TM-ROOT-035 and TM-ROOT-042 for
`PROMOTE_TO_OPEN | RETAIN_DEFERRED_WITH_NEW_TRIGGER`, and return TM-ROOT-124
for an exact D-GOV identity ruling. TM-ROOT-126/-127 await ordinary owner
triage. Any post-PR main advancement requires explicit authorization before a
non-rewriting sync; no merge is authorized.
