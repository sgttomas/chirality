# DEL-02-06 selection application trace

- Status: `AUTHOR_REMEDIATION_1_TRACE_COMPLETE_PENDING_MANAGER_VALIDATION`
- Selection package: `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`
- Authority transcript: `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`
- Signer/date: `Ryan Tufts`, `2026-08-03`
- Coverage: `27/27` exact rows, each mapped once
- Census tuple: `(TBD-005-A, TBD-011-A, TBD-013-A, CENSUS-A)` — allowed tuple 1

## Source bindings

The complete source identities are recorded in
`candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md#exact-source-identities`.
This trace additionally binds the patch plan
`e51075494a14576aa8d9357b6ad21928ea47065a2aa2488a02b6a4b96359cee1`,
N2 `14abde6b3b5eb188555c55749c4b6105d8b4fad08d21e9cf3998a76ea9f4ee52`,
N3 `e05b56d3b3a1bd349cd0b9da8e2df761126f2c46c44baf1c9282c6cf55180dd0`,
and accepted handoff
`bf8020460d475c0e101c8675bf5721cc1358299e3e5b799ecead9901eb74d151`.

## Exact one-to-one application

| # | Selected row | Candidate locus | Applied clause | Dependencies preserved | No-effect fence |
|---:|---|---|---|---|---|
| 1 | `D1-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#recovery-terminal-policy` | distinct `turn.recovery_indeterminate`; five explicit status mappings | D3,D4,D7,TBD-006,TBD-016 | no current event/status byte |
| 2 | `D2-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#retry-replay-and-resume` | no retry/resume; later act is independent | D1,D3,D4,TBD-006,TBD-008,TBD-016 | no resend/retry command |
| 3 | `D3-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#recovery-audit-and-redaction` | append-only run record plus immutable checkout manifest | D1,D4,D7,D8,TBD-008,TBD-014,TBD-016 | no audit mechanism created |
| 4 | `D4-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#transaction-durability-and-writer-ownership` | one writer; per-turn atomic compare/append; final batch manifest | D1,D3,D7,D9,TBD-006,TBD-016 | no persistence/runtime write |
| 5 | `D5-B` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#drain-reconstruction` | proven-local numeric ledger plus ambiguous blocker ledger | D6,D8,TBD-016 | no model/residency action |
| 6 | `D6-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md#recovery-readiness-and-retained-functions` | truthful non-mutating diagnostics retained; all consequential/mutating paths blocked | D3,D5,D7,D8,TBD-009,TBD-016,CENSUS | no route/client change |
| 7 | `D7-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#malformed-and-contradictory-evidence` | exact-unit preservation/quarantine and global consequential hold | D1,D3,D4,D6,TBD-008,TBD-016 | no quarantine/repair act |
| 8 | `D8-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#acceptance-time-attribution` | persist provider/engine/model/locality/residency epoch | D3,D5,D6,TBD-016 | no schema/model change |
| 9 | `D9-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md#cutover-rollback-and-irreversible-boundary` | rollback before first mutation; then proven old reader or forward repair | D1,D4,TBD-006,TBD-014,COMPAT-DELTA | no cutover/Git/deployment |
| 10 | `TBD-001-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#identity-grammar` | decimal epoch grammar with conspicuous unresolved owner placeholder | TBD-015,COMPAT-DELTA | no epoch or identity minted |
| 11 | `TBD-002-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#declaration-and-comparison` | two-sided per-operation preflight and request-bound exact equality | TBD-001,TBD-003,TBD-004,COMPAT-DELTA | no protocol/client behavior |
| 12 | `TBD-003-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#mismatch-envelope` | distinct exact mismatch class/envelope | TBD-001,TBD-002,TBD-007,TBD-009,CENSUS | no error/CLI/App byte |
| 13 | `TBD-004-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#compatibility-binding-record` | one immutable complete binding manifest | TBD-001,TBD-005,TBD-014,TBD-015,CENSUS,COMPAT-DELTA | no binding/release act |
| 14 | `TBD-005-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md#accepted-census-disposition` | Root CLI/App affected; Piping/Tier-0 not; PEC unresolved | TBD-009,TBD-011,TBD-013,CENSUS,COMPAT-DELTA | no client/foreign work |
| 15 | `TBD-006-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md#recovery-cutover-replay-and-indeterminate-completion` | staged no-replay, partial-output-preserving policy | D1,D2,D4,D9,TBD-016 | no migration/cutover/replay |
| 16 | `TBD-007-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md#ten-condition-identifiers-and-envelopes` | ten distinct exact machine identifiers/envelopes | D1,D7,TBD-003,TBD-008,TBD-016 | no constants/adapters/UI |
| 17 | `TBD-008-A` | `DEGRADED_MODE_CONTRACT_COMPOSITE_CANDIDATE_V2.md#precedence-retry-and-evidence-fields` | deterministic first blocker, complete redacted audit, retry false | D2,D3,D7,TBD-007,TBD-016 | no response/retry/audit behavior |
| 18 | `TBD-009-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md#client-conformance-package-partition` | separate Root CLI and App matrices; PEC conditional on PEC gate | D6,TBD-005,TBD-011,CENSUS | no client conformance work |
| 19 | `TBD-010-A` | `OWNER_DECISION_RECORD_CANDIDATE_V2.md#tier-0-relationship-routing` | prepare/route continue-separate candidate under later coordination act | TBD-001,TBD-004,COMPAT-DELTA | no Tier-0 decision/write |
| 20 | `TBD-011-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md#pec-v2-disposition` | PEC unresolved; route PEC-owned exact-operation/no-effect ruling | TBD-005,TBD-009,TBD-013,CENSUS | no PEC work/dependency/veto |
| 21 | `TBD-012-A` | `OWNER_DECISION_RECORD_CANDIDATE_V2.md#uncovered-ownership-seams` | no additional seam proven; later seam source-cited and routed | CENSUS | no owner/work invented |
| 22 | `TBD-013-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md#piping-disposition` | Piping not affected on current evidence | TBD-005,CENSUS | no Piping work/dependency |
| 23 | `TBD-014-A` | `EVIDENCE_AND_CUTOVER_PLAN_CANDIDATE_V2.md#semantic-conformance-and-regression-matrix` | full N3 design required and explicitly unexecuted | D1-D9,TBD-009 | no check/pass/closure claim |
| 24 | `TBD-015-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#epoch-change-criteria` | new epoch for consequential client-visible delta; not for proven non-observable change | TBD-001,TBD-004,COMPAT-DELTA | no epoch/repin/release |
| 25 | `TBD-016-A` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#daemon-recovery-state-machine` | exact four states, corpus classes, and transitions | D1-D8,TBD-006,TBD-007,TBD-008 | no readiness/runtime change |
| 26 | `CENSUS-A` | `AFFECTED_CLIENT_CENSUS_CANDIDATE_V2.md#accountable-human-census-ruling` | exact five-row census with foreign gates preserved | TBD-005,TBD-009,TBD-011,TBD-013,COMPAT-DELTA | no migration/conformance/release |
| 27 | `COMPAT-DELTA-A` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#recovery-compatibility-disposition` | conditional delta on later semantic adoption; future identity/binding required | D1,D6,TBD-001,TBD-002,TBD-003,TBD-004,TBD-005,TBD-015,CENSUS | no current delta/identity/implementation |

## Unselected-option preservation

All 27 unselected option IDs and their short dispositions are recorded once in
`candidate_v2/OWNER_DECISION_RECORD_CANDIDATE_V2.md#selected-and-unselected-options`.
Their authoritative full text remains hash-bound in the owner selection matrix
and semantic patch plan. No unselected option was silently merged into a
selected clause.

## Admitted-refuter-finding remediation

| Finding | Exact V2 resolved clause | Selected-basis disposition | Semantic delta limit |
|---|---|---|---|
| `REFUTER-F01` | `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md#daemon-recovery-state-machine`: every startup enters `RECOVERY_REQUIRED`; failure to establish safe single-writer ownership or exact corpus basis deterministically transitions to `RECOVERY_BLOCKED` before scan/mutation; success transitions to `RECOVERY_SCANNING` | direct completeness application of `TBD-016-A` and D4-A | no new state, no relaxed fail-closed behavior, no other transition changed |
| `REFUTER-F02` | `ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md#compatibility-binding-record`: one immutable binding manifest must contain exact SHA-256 identities for all six accepted V2 semantic members and the exact sorted V2 package manifest, in addition to all existing source/release/client/evidence/disposition bindings | direct completeness application of `TBD-004-A` | no membership narrowing and no other package semantic changed |

- Refuter return bound: `a5340f2f7396aa3d08ff0bffe6b960abd4d15e93a70bd20d3638efa3e9408a49`.
- V1 remains immutable and is not repaired or superseded by edit.

## Closure check

- Exact rows: `27/27`, with no missing or duplicate mapping.
- Six candidate files: `6/6`.
- Allowed census tuple: `PASS`.
- Future epoch: `UNRESOLVED`; no positive decimal value minted.
- N3 result posture: `DESIGN_COMPLETE_NOT_EXECUTED`.
- PEC: `UNRESOLVED`; no work/dependency/veto/outcome prescribed.
- Piping: `NOT_AFFECTED`; no work/dependency.
- App: affected only at census/planning level; all App ownership preserved.
- Tier-0: preparation/routing only; no relationship record adopted.
- Compatibility delta: conditional on later adoption; no present delta.
- Implementation: held behind a separate exact gate.
- Current effect: none.
