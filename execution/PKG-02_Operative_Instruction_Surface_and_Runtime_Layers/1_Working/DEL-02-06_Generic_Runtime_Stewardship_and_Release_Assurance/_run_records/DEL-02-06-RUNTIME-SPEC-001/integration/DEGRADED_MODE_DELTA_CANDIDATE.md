# Degraded-mode recovery delta candidate

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Status: `CANDIDATE_NOT_ADOPTED`
- Candidate delta: introduce a fail-closed recovery posture before readiness
- Accepted base candidate binding: `accepted_inputs/DEGRADED_MODE_CONTRACT_CANDIDATE.md` SHA-256 `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917`

## Boundary

The names and behavior below are proposals for owner review, not present
runtime bytes or accepted operational states. D1-D9 and TBD-006 through
TBD-009, TBD-014, and TBD-016 remain unresolved. No retained function is
adopted by this document.

This is an additive delta bound to the exact accepted base identity above.
N4 did not read, reproduce, weaken, or replace the accepted base bytes. A later
composite may be adopted only if it binds that exact base identity and proves
that every base clause remains present alongside the complete ten-condition
delta below. A base-hash mismatch returns to the owner; it is never treated as
equivalent content.

## Candidate state delta

`RECOVERY_REQUIRED` is the proposed generic posture whenever the registered
session corpus has not completed a successful reconciliation pass, contains
accepted-without-terminal residue, contains malformed or contradictory
evidence, has ambiguous recovery-writer ownership, or cannot establish the
owner-selected drain/attribution facts. Exact state identifiers and precedence
remain D1/D6/TBD-016 owner decisions.

## Required ten-condition one-to-one matrix

This matrix contains exactly the ten independent Scope-of-Work semantic
conditions. `UNRESOLVED` entries are explicit owner-gate inputs, not defaults.
Every verification entry is a later evidence obligation and remains
`DESIGNED_NOT_EXECUTED`.

| Condition | Boundary | Candidate required behavior | Recovery | Exact class or unresolved item | Retry posture | Redaction/evidence | Positive verification | Negative/adversarial verification |
|---|---|---|---|---|---|---|---|---|
| 1. Client configuration / project access | Client-owned configuration and checkout-contained project-access material, before any request is sent | Prevent the consequential request; do not recast the condition as socket or daemon absence and do not mutate project authority | Owning client/project repairs exact configuration or access, then all preconditions are rerun | `UNRESOLVED:TBD-007`; boundary fixed by REQ-017 | `UNRESOLVED:TBD-008`; no automatic resend | Preserve project/configuration evidence without secrets or machine-specific paths; exact redaction is `UNRESOLVED:TBD-008` | Valid configuration and access permit progression to the next independent gate, with no runtime work yet | Missing, stale, unauthorized, secret-bearing, or wrong-project material blocks before transport and cannot trigger alternate runtime behavior |
| 2. Runtime credential readiness | Daemon-owned provider/runtime credential custody after client/project access and before engine work | Reject the operation without transferring credential custody or repair authority to the client | Authorized daemon credential repair, then rerun every precondition | `UNRESOLVED:TBD-007`; must remain distinct from client access and transport | `UNRESOLVED:TBD-008`; no automatic retry | Record truthful credential-readiness class and provider boundary while redacting credential material under `UNRESOLVED:TBD-008` | Ready runtime credentials allow progression without exposing credential values | Missing, invalid, inaccessible, or unauthorized credentials reject without client-side entry, fallback, or recast as daemon absence |
| 3. Registration | Root project identity, manifest currency, registration, and enabled-adapter record before project runtime admission | Prevent project runtime work until separately authorized registration or re-registration succeeds | Perform only a separately authorized registration act, then rerun all preconditions | `UNRESOLVED:TBD-007`; registration remains distinct from authorization | `UNRESOLVED:TBD-008`; no implicit re-registration or retry | Bind project identity, manifest/registration evidence, and adapter status without secrets; redaction exactness remains open | Current accepted registration and enabled adapter permit progression | Missing, stale, mismatched, disabled, or foreign registration blocks without altering manifests or local registration by implication |
| 4. Authorization | Project-scoped identity, required scopes, and requested-operation permission after registration | Reject only the unauthorized operation; never broaden scopes or authority automatically | Owning authority separately grants or corrects the exact scope, then all preconditions rerun | `UNRESOLVED:TBD-007`; distinct from provider authentication | `UNRESOLVED:TBD-008`; no automatic privilege escalation or resend | Preserve requested operation, required scope, decision, and authority source with `UNRESOLVED:TBD-008` redaction | Exact authorized project/operation pair progresses to adapter evaluation | Wrong identity, missing scope, expired authority, cross-project token, or unauthorized operation blocks with zero authority mutation |
| 5. Project adapter | Project-owned adapter availability, authority, and protocol consistency after registration/authorization | Block only operations that require the unavailable or nonconformant adapter; generic transport acquires no project authority | Owning project repairs or accepts the adapter under its own gate, then reruns preconditions | `UNRESOLVED:TBD-007`; required adapter and exact operation must be named | `UNRESOLVED:TBD-008`; no silent adapter fallback | Record adapter identity, operation, authority and protocol result without private adapter evidence leakage; exact redaction remains open | Required accepted adapter handles the exact authorized operation while ownership remains project-local | Missing, disabled, unauthorized, incompatible, or wrong-project adapter blocks; generic transport and another adapter cannot substitute |
| 6. Unix-socket transport | Authenticated HTTP/1.1 over the protected Unix-domain socket, after client/project gates and before compatibility-dependent work | Fail the runtime-dependent operation closed; no TCP, in-process, alternate-daemon, or alternate-runtime transport | Reconnect or rebind only to an authorized daemon and rerun every precondition | `UNRESOLVED:TBD-007`; transport remains distinct from protocol and daemon operational state | `UNRESOLVED:TBD-008`; reconnect is recovery, not fallback, and never silently resends | Record authorized endpoint identity and transport cause without absolute-path or credential leakage; exact redaction remains open | Reachable authorized Unix socket carries one request only after prior gates pass | Absent socket, stale socket, refused connection, midstream loss, wrong owner, TCP offer, or in-process substitute fails closed without replay |
| 7. Compatibility mismatch | Exact Root-owned daemon/client compatibility identity comparison before consequential work | Compare exact equality and reject mismatch before consequential work; no range, downgrade, alternate runtime, daemon, model, or inference from route success | Bind an exact owner-accepted compatible pair and rerun every precondition | `UNRESOLVED:TBD-003/TBD-007`; identity/grammar also `TBD-001/TBD-002` | `UNRESOLVED:TBD-008`; no automatic negotiation, downgrade, or resend | Bind compared identities and accepted contract bases; exact failure envelope/redaction remain open | Exact-equal, accepted identities permit progression and preserve the binding evidence | Unequal, absent, malformed, inferred, range-compatible, package-version-only, or route-success-only identity rejects before work |
| 8. Wire / protocol validity | Contract-valid request, response, SSE/event schema, identity attribution, and terminal vocabulary after transport | Fail closed as a truthful protocol class; never recast malformed behavior as transport absence or accept partial/foreign attribution | Repair or adopt exact contract bytes through the owning gate, rebind compatibility where required, and rerun preconditions | `UNRESOLVED:TBD-007`; malformed/contradictory recovery treatment also D7/TBD-016 | `UNRESOLVED:TBD-008`; malformed or indeterminate exchange is never silently replayed | Preserve exact source hash, line/offset or field locus, schema identity, and safe payload evidence; redaction remains open | Canonical attributed messages satisfy the exact adopted schema and terminal-cardinality rules | Invalid UTF-8/JSON/schema/type, torn event, foreign session/turn, duplicate/conflicting terminal, or partial response fails closed and preserves evidence |
| 9. Provider / engine / model | Daemon-owned execution domain after transport, compatibility, project, and protocol gates pass | Preserve the actual execution-domain cause; do not recast it as daemon absence or choose another provider, engine, or model | Authorized repair or explicit model activation under its own evidence-bearing gate, then rerun preconditions without replay | `UNRESOLVED:TBD-007`; actual attribution required by REQ-045 | `UNRESOLVED:TBD-008`; no automatic model load, switch, alias, fallback, or resend | Retain actual engine/provider/model/residency attribution when exposed, redact sensitive data under open policy, and report missing attribution | Exact ready engine/provider/model executes only after all earlier gates and records actual attribution | Provider auth failure, engine failure, model absent/drifted, unknown helper, residency ambiguity, or alternate-model offer fails without automatic action |
| 10. Daemon operational / recovery state | Session, delegation, tools, turn locks, interruption, model residency, startup reconciliation, and recovery-readiness state | Reject or halt only the affected operation; before readiness enumerate residue, preserve exactly-one-terminal truth, block consequential routes, and never invent completion, replay, authority, or alternate state | Complete an evidence-bearing idempotent pass under `OWNER_SELECTED_RECOVERY_TERMINAL_POLICY`, transaction, drain, attribution, retained-function, and cutover decisions D1-D9 | `UNRESOLVED:TBD-016` plus D1-D9; all four observed terminal forms remain distinct | `UNRESOLVED:TBD-008/TBD-016`; automatic replay/resume prohibited, operator retry requires D2 | Stable recovery-run identity, corpus/input/output hashes, classification, before/after state, disposition authority and actual attribution; D3 controls exact schema/redaction | Clean startup reports zero residue; orphan recovery converges once; repeated passes add no terminal; readiness opens only after complete success | Crash after acceptance or each write boundary, duplicate/conflicting/malformed evidence, concurrent reconciler, stale drain count, readiness race, or Agent 1 orphan remains fail-closed |

While that posture holds:

- daemon readiness must not claim consequential availability;
- turn, governed Agent 1, session-boot, model-activation, and local-admission
  paths must stop before acceptance, engine, provider, model, tool,
  delegation, load, unload, or residency mutation;
- no TCP/in-process fallback, alternate daemon/model/runtime, downgrade,
  automatic scheduling, resend, replay, resume, or inferred completion is
  permitted;
- evidence must preserve the exact blocking class through Root client/CLI and,
  after a separate App-owned tranche, through App adapter/presentation layers;
- operational daemon state remains non-authoritative and checkout-contained
  evidence remains the reliance basis.

## Candidate retained-function matrix

| Surface | Candidate posture | Adoption status |
|---|---|---|
| health and daemon status | may be retained read-only only if it truthfully reports recovery-not-ready, leaks no protected evidence, and performs no mutation | `UNRESOLVED_D3_D6` |
| session/event replay | may be retained read-only only if it is byte-stable, exposes malformed/partial truth, and performs no repair-on-read | `UNRESOLVED_D6_D7` |
| project/session list and get | may be retained read-only only if no migration, registration, or status repair occurs | `UNRESOLVED_D6_D7` |
| turn and governed Agent 1 run | consequential; blocked until successful recovery | candidate only, pending D6 |
| session boot | consequential; blocked until successful recovery | candidate only, pending D6 |
| model activation and local admission | consequential; blocked until successful recovery and ruled drain treatment | candidate only, pending D5/D6/D8 |
| registration, session create/delete, credentials, scaffold, permissions | individually classified; no broad administrative bypass | `UNRESOLVED_D6` |
| file-native governance outside runtime | separately owned; may not be described as an alternate agent runtime | requires each owning loop's own acceptance |

## Recovery and exit

Exit from the proposed posture requires one successful, evidence-bearing,
idempotent pass over the exact corpus basis, no unresolved malformed or
contradictory unit at the owner-selected blocking granularity, stable
owner-selected drain accounting, and completion of the owner-selected
transaction/audit boundary. Repeated runs must append no duplicate terminal
and preserve the canonical outcome digest.

Reconnect or rebind after exit reruns every required precondition and is
recovery, not fallback. Any operator retry remains separately human-gated.
Partial output and unknown completion remain indeterminate and are never
silently replayed.

## Client boundary

Root CLI and App are `AFFECTED`, but App behavior and evidence require an
App-owned tranche. Piping and Tier-0 are `NOT_AFFECTED`. PEC remains
`UNRESOLVED`; this candidate creates no PEC work, dependency, or closure veto.

This file makes no implementation, executable evidence, cutover, rollback,
lifecycle, release, or reliance claim.
