# DEL-02-06 owner-selection slate

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Status: `DERIVATIVE_DECISION_SUPPORT_NOT_ADOPTED`
- Basis: 35/35 launch-declared inputs reproduced at their sealed SHA-256 identities.
- Scope: D1-D9, TBD-001 through TBD-016, affected-client census, and compatibility delta only.

## Authority and use

This slate makes explicit, evidence-grounded recommendations so the accountable
human can choose exact option identifiers. Every recommendation is
**non-authoritative decision support**. Nothing here is a default, selection,
approval, acceptance, semantic contract, or implementation instruction.
Silence, delay, partial response, file presence, validation, or reuse has no
effect.

Root may decide Root semantics and accept a Root census. Root may not decide
App implementation or conformance, PEC applicability, a Piping-owned future
obligation, or a Tier-0 relationship act. App remains App-owned. PEC remains
`UNRESOLVED`; this slate creates no PEC work, dependency, or closure veto.

## Coherent option families for D1-D9

### D1 — terminal truth

- `D1-A_INTERRUPTED_WITH_RECOVERY_PAYLOAD` preserves the four observed terminal
  forms, uses `turn.interrupted` for process-loss reconciliation, carries a
  typed recovery payload, and maps session status to `interrupted`.
- `D1-B_NEW_RECOVERY_TERMINAL` adds a distinct recovery terminal and a distinct
  session-status mapping.
- **Non-authoritative recommendation:** `D1-A_INTERRUPTED_WITH_RECOVERY_PAYLOAD`.
  It preserves existing terminal cardinality while retaining the recovery cause
  in a typed payload. Alternative: `D1-B_NEW_RECOVERY_TERMINAL` if the owner
  requires recovery to remain a first-class terminal distinct from interruption.

### D2 — retry without replay

- `D2-A_NEW_TURN_EXPLICIT_RETRY` permits only an operator-initiated new turn
  with a new identity, a bound prior-turn reference, completed preflight, and
  proof that reconciliation is terminal; automatic replay/resume stays closed.
- `D2-B_NO_RETRY_FOR_INDETERMINATE` prohibits retry of an indeterminate accepted
  turn until a later case-specific human act.
- **Non-authoritative recommendation:** `D2-A_NEW_TURN_EXPLICIT_RETRY` because
  it keeps replay separate from reconciliation while preserving a controlled
  recovery path. Alternative: `D2-B_NO_RETRY_FOR_INDETERMINATE` for the lowest
  ambiguity posture.

### D3 — checkout-reconstructible audit

- `D3-A_CANONICAL_HASHED_AUDIT` requires a canonical append-only audit record
  with run/corpus/turn identities, input/output hashes, classification,
  authority, before/after state, result, ordering, retention, and explicit
  redaction fields.
- `D3-B_MINIMAL_EVENT_LINKED_AUDIT` records only event linkage, disposition,
  hashes, and redaction outcome, leaving richer context to a later tranche.
- **Non-authoritative recommendation:** `D3-A_CANONICAL_HASHED_AUDIT`; N3-R09,
  N3-R10, and N3-R15 require independently reconstructible evidence. Alternative:
  `D3-B_MINIMAL_EVENT_LINKED_AUDIT` only if the owner accepts the resulting
  evidence limitation explicitly.

### D4 — durability boundary

- `D4-A_PER_TURN_ATOMIC_RECONCILIATION` uses an authenticated single-writer
  compare-and-append transaction per turn spanning terminal/marker, session
  status, audit, and ownership; the batch summary follows only after all units.
- `D4-B_WHOLE_CORPUS_ATOMIC_RECONCILIATION` makes the entire corpus one atomic
  reconciliation transaction.
- **Non-authoritative recommendation:** `D4-A_PER_TURN_ATOMIC_RECONCILIATION`;
  it satisfies exactly-once truth and crash repair without making unrelated
  sessions one failure domain. Alternative: `D4-B_WHOLE_CORPUS_ATOMIC_RECONCILIATION`
  if all-or-nothing corpus visibility is required.

### D5 — durable drain accounting

- `D5-A_COUNT_UNTIL_DURABLE_DISPOSITION` counts every unresolved accepted local
  turn against drain until its D4 unit is durable; missing or stale attribution
  keeps activation closed.
- `D5-B_QUARANTINE_UNKNOWN_WITH_GLOBAL_LATCH` does not assign a numeric drain
  count to unknown attribution but keeps the global readiness latch closed.
- **Non-authoritative recommendation:** `D5-A_COUNT_UNTIL_DURABLE_DISPOSITION`
  because memory-only counts are the recorded gap and unresolved local work
  must not disappear after restart. Alternative:
  `D5-B_QUARANTINE_UNKNOWN_WITH_GLOBAL_LATCH` where a truthful count cannot be
  reconstructed.

### D6 — readiness and retained functions

- `D6-A_STRICT_LATCH_WITH_READ_ONLY_INSPECTION` blocks every consequential path
  and retains only truthful health/status, byte-stable replay, and mutation-free
  list/get inspection proven individually read-only.
- `D6-B_STRICT_LATCH_NO_RUNTIME_ENDPOINTS` exposes no runtime endpoint until
  successful corpus reconciliation.
- **Non-authoritative recommendation:** `D6-A_STRICT_LATCH_WITH_READ_ONLY_INSPECTION`
  because bounded inspection supports diagnosis without becoming an alternate
  runtime. Alternative: `D6-B_STRICT_LATCH_NO_RUNTIME_ENDPOINTS` if read-only
  behavior cannot be proven.

### D7 — malformed evidence

- `D7-A_SESSION_QUARANTINE_GLOBAL_READINESS_HOLD` byte-preserves the evidence,
  quarantines the affected session, permits only D6 read-only inspection, and
  holds global consequential readiness until human-authorized repair and rescan.
- `D7-B_WHOLE_CORPUS_QUARANTINE` quarantines the entire corpus on any malformed
  or contradictory unit.
- **Non-authoritative recommendation:**
  `D7-A_SESSION_QUARANTINE_GLOBAL_READINESS_HOLD`; it preserves evidence and
  limits quarantine scope without relaxing the readiness gate. Alternative:
  `D7-B_WHOLE_CORPUS_QUARANTINE` for the most conservative containment posture.

### D8 — attribution

- `D8-A_EVENT_BOUND_ATTRIBUTION_TUPLE` binds execution mode, provider, engine,
  model, and residency epoch at acceptance and carries explicit `UNKNOWN`
  values rather than recovery-time inference.
- `D8-B_BATCH_BOUND_ATTRIBUTION_WITH_UNKNOWN` binds only a recovery-run/corpus
  attribution record and preserves unknown per-turn dimensions.
- **Non-authoritative recommendation:** `D8-A_EVENT_BOUND_ATTRIBUTION_TUPLE`
  because drain and recovery decisions are turn-specific and present state may
  drift. Alternative: `D8-B_BATCH_BOUND_ATTRIBUTION_WITH_UNKNOWN` when historic
  per-turn evidence is absent, with readiness still closed.

### D9 — cutover and restore

- `D9-A_STAGED_SCAN_CUTOVER_RESTORE` requires a no-write shadow scan, exact
  preimage and candidate identities, fail-closed abort thresholds, a separately
  authorized cutover, evidence-preserving restore, post-restore compatibility
  check, and no silent replay; Git/deployment/release remain separate acts.
- `D9-B_DEFER_CUTOVER` leaves the semantic package unadopted and performs no
  cutover until a later exact plan is accepted.
- **Non-authoritative recommendation:** `D9-A_STAGED_SCAN_CUTOVER_RESTORE`
  because N3-R14 requires cutover, failed-cutover, restore, and restart evidence.
  Alternative: `D9-B_DEFER_CUTOVER` if any required preimage, abort, or restore
  identity is unavailable.

## Sixteen TBD recommendations

Each line is non-authoritative decision support and preserves the named later
gate.

| Row | Recommended option | Consequence and preserved unknown |
|---|---|---|
| TBD-001 | `TBD001-A_ROOT_OPAQUE_EPOCH_GRAMMAR` | Use Root-owned `root-runtime-contract/v{N}` grammar; the issued integer remains for the later versioned candidate. |
| TBD-002 | `TBD002-A_AUTHENTICATED_PREFLIGHT_EQUALITY` | Declare through an authenticated preflight before consequential work and compare exact equality; the exact endpoint/field bytes remain future-candidate work. |
| TBD-003 | `TBD003-A_TYPED_COMPATIBILITY_MISMATCH` | Preserve a distinct mismatch class and expected/actual identities through Root presentation; App mapping remains App-owned. |
| TBD-004 | `TBD004-A_IMMUTABLE_BINDING_MANIFEST` | Require a hash-bound identity/contract/source/release/client/evidence/disposition manifest before release. |
| TBD-005 | `TBD005-A_ACCEPT_CURRENT_CENSUS_BOUNDARIES` | Accept Root CLI/App `AFFECTED`, Piping/Tier-0 `NOT_AFFECTED`, PEC `UNRESOLVED`; no client implementation is accepted. |
| TBD-006 | `TBD006-A_STAGED_FAIL_CLOSED_MIGRATION` | Bind D1/D2/D4/D9, preserve partial output and indeterminate completion, prohibit replay, and require exact restore evidence. |
| TBD-007 | `TBD007-A_DISTINCT_TEN_CONDITION_CLASSES` | Give every independent degraded-mode condition a distinct typed identifier/envelope. |
| TBD-008 | `TBD008-A_TOTAL_PRECEDENCE_DENY_DEFAULT_RETRY` | Define a total precedence table; retry is false unless an accepted row says otherwise; retain redacted hash-bound evidence. |
| TBD-009 | `TBD009-A_ROUTE_SEPARATE_CLIENT_MATRICES` | Route Root CLI evidence to Root and App evidence to App; retain PEC unresolved pending PEC-owned ruling. |
| TBD-010 | `TBD010-A_ROUTE_TIER0_RELATIONSHIP_ACT` | Preserve `PREPARATION_SELECTED_NOT_ADOPTED` and route a separate Tier-0 act; infer no relationship act here. |
| TBD-011 | `TBD011-A_RETAIN_PEC_UNRESOLVED_AND_ROUTE` | Root retains `UNRESOLVED` and routes the exact affected/no-effect question to PEC; creates no PEC work or veto. |
| TBD-012 | `TBD012-A_NO_SEAM_PROVEN_ROUTE_IF_EVIDENCED` | Record no additional seam on current evidence; any future seam must be source-cited and owner-routed. |
| TBD-013 | `TBD013-A_STATE_NO_CURRENT_ROOT_EFFECT` | Preserve Piping `NOT_AFFECTED` on current evidence; only a later Piping-owned accepted obligation may change it. |
| TBD-014 | `TBD014-A_N3_MATRIX_AS_MINIMUM_OBLIGATION` | Carry N3-R01..R16 and RR-01..RR-18 as minimum unexecuted evidence obligations; no check result is inferred. |
| TBD-015 | `TBD015-A_ADOPTION_CAUSES_NEW_EPOCH` | If the recovery specification is adopted, require a new Root compatibility identity; non-adoption makes no `NO_CHANGE` ruling. |
| TBD-016 | `TBD016-A_EXPLICIT_RECOVERY_STATE_MACHINE` | Define ordered recovery-required, blocked, reconciling, and ready classes; no resume/inference and unknown stays indeterminate. |

## Census and compatibility-delta recommendations

- **CENSUS non-authoritative recommendation:**
  `CENSUS-A_ACCEPT_CURRENT_CLASSIFICATIONS`. Consequence: accept the planning
  classifications only—Root CLI/App `AFFECTED`, Piping/Tier-0 `NOT_AFFECTED`,
  PEC `UNRESOLVED`. App conformance stays App-owned; PEC remains owner-routed.
  Alternative: `CENSUS-B_RETURN_FOR_NEW_EVIDENCE`.
- **COMPAT-DELTA non-authoritative recommendation:**
  `COMPATDELTA-A_DELTA_IF_RECOVERY_ADOPTED`. Consequence: a later adoption of
  recovery requires an exact new Root identity and binding; the choice neither
  supplies that identity nor adopts recovery. Alternative:
  `COMPATDELTA-B_DEFER_DISPOSITION`.

## Exact owner response grammar — placeholders only

The response is ineffective unless every placeholder is replaced by one valid
identifier for its row and the three artifact identities match the presented
derivative package. This grammar records requested selections only; future
semantic bytes still require their own exact acceptance. No omission or silence
selects a recommendation.

```text
SELECT DEL-02-06 OWNER OPTIONS
SLATE_SHA256=<OWNER_SELECTION_SLATE_SHA256>
MATRIX_SHA256=<OWNER_SELECTION_MATRIX_SHA256>
PATCH_PLAN_SHA256=<SEMANTIC_PATCH_PLAN_SHA256>
D1=<D1_OPTION_ID>
D2=<D2_OPTION_ID>
D3=<D3_OPTION_ID>
D4=<D4_OPTION_ID>
D5=<D5_OPTION_ID>
D6=<D6_OPTION_ID>
D7=<D7_OPTION_ID>
D8=<D8_OPTION_ID>
D9=<D9_OPTION_ID>
TBD-001=<TBD001_OPTION_ID>
TBD-002=<TBD002_OPTION_ID>
TBD-003=<TBD003_OPTION_ID>
TBD-004=<TBD004_OPTION_ID>
TBD-005=<TBD005_OPTION_ID>
TBD-006=<TBD006_OPTION_ID>
TBD-007=<TBD007_OPTION_ID>
TBD-008=<TBD008_OPTION_ID>
TBD-009=<TBD009_OPTION_ID>
TBD-010=<TBD010_OPTION_ID>
TBD-011=<TBD011_OPTION_ID>
TBD-012=<TBD012_OPTION_ID>
TBD-013=<TBD013_OPTION_ID>
TBD-014=<TBD014_OPTION_ID>
TBD-015=<TBD015_OPTION_ID>
TBD-016=<TBD016_OPTION_ID>
CENSUS=<CENSUS_OPTION_ID>
COMPAT-DELTA=<COMPATDELTA_OPTION_ID>
FUTURE_VERSION=<VNN>
ACCOUNTABLE_OWNER=<OWNER_ID>
RULING_DATE=<YYYY-MM-DD>
END SELECT DEL-02-06 OWNER OPTIONS
```

## No-effect boundary

This derivative slate changes no current accepted/candidate/handoff semantic
byte and causes no implementation, executable check, runtime/client/project
write, profile/check adoption, dependency, SCA/decomposition/PRD, Task
Management, lifecycle, release, publication, issuance, reliance, Git, PR,
merge, or foreign-loop effect.
