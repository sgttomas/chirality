# N4 open-item and accepted-finding map

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Status: `CANDIDATE_MAP_NOT_DISPOSITION`

## Stable Scope-of-Work items

| Item | Current posture | N4 treatment | Required later owner/gate |
|---|---|---|---|
| TBD-001 / OD6-OPEN-001 | `PROPOSED` | exact compatibility identity and grammar remain open | Root compatibility decision |
| TBD-002 / OD6-OPEN-002 | `PROPOSED` | declaration/preflight locus and comparison behavior remain open | Root compatibility decision |
| TBD-003 / OD6-OPEN-003 | `PROPOSED` | mismatch identifier, envelope, presentation mapping remain open | Root compatibility plus affected-client gates |
| TBD-004 / OD6-OPEN-004 | `OPEN` | complete contract/source/release/client/evidence binding remains open | Root binding and release fan-in |
| TBD-005 / OD6-OPEN-005 | `OPEN` | current census: Root CLI/App affected; Piping/Tier-0 not affected; PEC unresolved; census itself remains owner-gated | affected-client census acceptance |
| TBD-006 / OD6-OPEN-006 | `PROPOSED` | cutover, rollback, replay, partial-output, indeterminate-completion values remain open | D1/D2/D4/D9 decisions |
| TBD-007 / OD6-OPEN-007 | `PROPOSED` | exact failure identifiers and envelopes remain open | Root semantic contract decision |
| TBD-008 / OD6-OPEN-008 | `PROPOSED` | precedence, retryability/timing, redaction and evidence fields remain open | D2/D3 decisions |
| TBD-009 / OD6-OPEN-009 | `OPEN` | retained-function matrices and proof remain open | D6 plus client-owned gates |
| TBD-010 / OD6-OPEN-010 | `PREPARATION_SELECTED_NOT_ADOPTED` | continue-separate candidate only; no Tier-0 act inferred | Tier-0 owner relationship act |
| TBD-011 / OD6-OPEN-011 | `OPEN` | PEC remains `UNRESOLVED`; no obligation, dependency, or closure veto | PEC-owned owner-ruling or explicit no-effect ruling |
| TBD-012 / OD6-OPEN-012 | `OPEN` | no additional seam proven; any later seam must be source-cited and owner-routed | owning authority |
| TBD-013 / OD6-OPEN-013 | `OPEN` | Piping remains metadata-only and `NOT_AFFECTED` on current evidence | later Piping-owned accepted obligation, if any |
| TBD-014 / OD6-OPEN-014 | `PROPOSED` | N3 design exists but is unexecuted; exact conformance/regression matrix remains open | implementation/check and evidence acceptance |
| TBD-015 / OD6-OPEN-015 | `PROPOSED` | N4 proposes delta if recovery is adopted; exact epoch-change/no-change rule remains open | Root compatibility decision |
| TBD-016 / OD6-OPEN-016 | `PROPOSED` | recovery state classes, precedence, resumability, indeterminate completion and fields remain open | D1-D8 semantic decisions |

## Accepted N1 findings preserved

| Finding | Preserved consequence |
|---|---|
| N1-F01 | require corpus discovery before readiness |
| N1-F02 | require persisted-history guard before ordinary and governed admission |
| N1-F03 | require owner-ruled turn-level idempotent reconciliation; event-ID suppression is insufficient |
| N1-F04 | require owner-ruled durable drain treatment after restart |
| N1-F05 | require truthful indeterminate/recovery class through Root CLI/client without resend |
| N1-F06 | keep descriptive replay distinct from reconciliation |
| N1-F07 | preserve all four observed terminal forms and hold exact terminal/status mapping under D1 |
| N1-F08 | require new restart, replay, idempotence, drain, and admission evidence; no existing-test claim |

## Accepted N2 finding preserved

| Finding | Preserved consequence |
|---|---|
| N2-F-001 | PEC future seam does not prove an exact obligation; classification remains `UNRESOLVED` and creates no work, dependency, or closure veto |

## Accepted N3 findings preserved

| Finding | Severity | N4 treatment |
|---|---|---|
| N3-F01 | `BLOCKING_FOR_IMPLEMENTATION` | startup recovery phase required in candidate; no implementation authorized |
| N3-F02 | `BLOCKING_FOR_IMPLEMENTATION` | drain reconstruction held for D5/D8 and later implementation evidence |
| N3-F03 | `BLOCKING_FOR_IMPLEMENTATION` | skip-and-count replay rejected as recovery proof; malformed policy held for D7 |
| N3-F04 | `BLOCKING_FOR_IMPLEMENTATION` | turn-level uniqueness/durability held for D1/D4 |
| N3-F05 | `BLOCKING_FOR_IMPLEMENTATION` | governed Agent 1 parity required |
| N3-F06 | `HUMAN_DECISION_REQUIRED` | all D1-D9 values remain open; no vocabulary or recovery semantics inferred |
| N3-F07 | `EVIDENCE_GAP` | N3 matrices remain `DESIGNED_NOT_EXECUTED`; executable evidence is later-gated |

## Decision ledger

D1 recovery terminal policy, D2 retry/replay/resume, D3 audit/redaction, D4
transaction/durability, D5 drain reconstruction, D6 readiness and retained
functions, D7 malformed/contradictory evidence, D8 attribution, and D9
cutover/rollback all remain unresolved. Their required instruments are listed
in `RECOVERY_SPEC_CANDIDATE.md`; none is closed, narrowed by implication, or
converted into implementation behavior by this map.
