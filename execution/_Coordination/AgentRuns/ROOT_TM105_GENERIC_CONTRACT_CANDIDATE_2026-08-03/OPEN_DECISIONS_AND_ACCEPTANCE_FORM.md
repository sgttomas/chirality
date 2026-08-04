# Open decisions and next semantic-acceptance form

Status: `UNSIGNED DECISION PREPARATION — NO SELECTION RECORDED`

The accountable human must select exact semantics before implementation. An
acceptance token that leaves an implementation-critical `TBD` unresolved does
not authorize implementation.

## Open decisions

| ID | Question | Bounded options | Recommendation / reason |
|---|---|---|---|
| TBD-105-01 | Is the sandbox lifetime one run or one session? | A: one sandbox per run; B: one sandbox per session with immutable binding; C: return for evidence | A — strongest isolation; operational cost needs evidence. |
| TBD-105-02 | Which backend ID/version is accepted? | A: named OS-enforced backend after proof; B: fully brokered native tools after proof; C: return/defer | `TBD` — no backend proof is in this carrier. |
| TBD-105-03 | What exact identity schema/version and field encodings apply? | A: commission versioned schema candidate; B: bind to a revised existing session schema; C: return | A — avoids silently overloading current `chirality.session/v2`. |
| TBD-105-04 | What changes force new run versus new session? | A: every identity component change forces both; B: new run under new session identity; C: matrix by field | `TBD` — must align with DEL-02-06 identity work. |
| TBD-105-05 | Is trusted broker/daemon identity separate? | A: yes, separately version/hash bind; B: no, backend identity suffices; C: architecture-dependent | C — topology is unselected. |
| TBD-105-06 | What receipt authenticity, expiry, replay, and evaluator contract applies? | A: signed/hash-chained receipts; B: authenticated durable event-log receipts; C: return for threat model | C — threat model and persistence basis are absent. |
| TBD-105-07 | What conformance evidence is required to bind/change an implementation family? | A: contract plus adapter/tool/profile test suite and independent review; B: narrower tool-class suite; C: return | A in principle; exact suite still needs a sealed design. |
| TBD-105-08 | Are test-only fixture profiles allowed? | A: prohibit all fixtures in runtime profiles; B: allow separately identified non-authoritative test profiles only; C: return | B — supports tests without success substitution; isolation details needed. |
| TBD-105-09 | What event schema, hashing, ordering, clock, retention, redaction, and storage rules apply? | A: commission versioned durable schema; B: extend current events; C: return | `TBD` — privacy and store impacts require evidence. |
| TBD-105-10 | What exact interruption state tokens/transitions apply? | A: accept proposed four-phase lifecycle with exact schema; B: reduce to requested/terminal plus evidence; C: return | A — exposes cleanup progress; implementation fit needs validation. |
| TBD-105-11 | What acknowledgement, grace, forced termination, and cleanup deadlines/obligations apply? | A: choose exact bounded values and force semantics; B: tool-class profile values; C: return for experiments | C — no timing evidence exists here. |
| TBD-105-12 | How are partial interrupted outputs quarantined or continued? | A: quarantine, never continue; B: explicit continuation if identity-bound; C: consumer-selected within generic carrier | `TBD` — interacts with result budgets and DEL-02-06 resume. |
| TBD-105-13 | Which budget dimensions and numeric defaults/maximums apply? | A: accept all candidate dimensions with profile values; B: bytes/time/calls only initially; C: return for workload data | C — values cannot be invented. |
| TBD-105-14 | Which overflow outcomes are allowed per tool/effect class? | A: exact class matrix; B: fail only; C: artifact/continuation only for read class | A — exact matrix still requires owner-selected semantics. |
| TBD-105-15 | What continuation-token identity, expiry, and stale-refusal rules apply? | A: bind all identity fields and event cursor; B: no continuation this generation; C: delegate to DEL-02-06 | C — avoid silently merging resume semantics. |
| TBD-105-16 | Are truncation and budget exhaustion states or orthogonal facts; how do unknowns map? | A: terminal-state expansion; B: base terminal plus reason/facts; C: return | B — avoids false exclusivity, subject to schema review. |
| TBD-105-17 | What exact resource-rights grammar/profile families apply? | A: mount/process/network/env/IPC/device/credential/channel grammar; B: minimal filesystem/process grammar first; C: return | A in coverage; exact syntax and defaults remain unselected. |
| TBD-105-18 | What supported platform matrix and unsupported-platform behavior apply? | A: explicit allowlisted platform/backend pairs, otherwise unavailable; B: one platform first; C: return | A; membership remains `TBD`. |
| TBD-105-19 | Which trusted-daemon versus sandboxed-worker/broker topology is accepted? | A: tool/session in worker; B: model in daemon but every native tool brokered; C: profile-specific explicit topology | `TBD` — either can conform only with bypass proof. |
| TBD-105-20 | What exact grant, capability-matching, applicability/precedence, authentication/replay, and deterministic policy-decision contract applies? | A: versioned authenticated replay-safe grants with explicit issuer/evaluator, schema/vocabulary, issue, activate, applicability, precedence/conflict, compose, expire, revoke, supersede, capability matching, stale refusal, exact bound policy-decision inputs/outputs, and exact-`ALLOW` semantics; B: authenticated non-persistent request-scoped grants with the same exact matching, precedence, replay, policy binding, and exact-`ALLOW` rule; C: return for authorization threat model | `TBD` — authorization-critical semantics cannot be inferred from current client scopes; receipt semantics remain separately owned by TBD-105-06. |
| TBD-105-21 | What common digest algorithm and canonicalization govern every digest-bearing contract? | A: one Root-wide versioned digest profile across identities, briefs, profiles, policy, registries, schemas, implementations, inputs, artifacts, events, and packages; B: type-specific profiles with explicit algorithm/canonicalization identity; C: return for compatibility analysis | `TBD` — current SHA-256 evidence does not by itself select runtime canonicalization rules. |

## Package-level ruling options

### `TM105-SEM-A` — accept exact candidate clauses after resolving all TBDs

Accept a versioned successor of `CONTRACT_CANDIDATE.md` with every selected
value substituted, exact SHA-256 named, and no `TBD-105-*` that affects
implementation. This accepts semantics only. It does not authorize source,
tests, App/Piping changes, release, or merge.

### `TM105-SEM-B` — accept a bounded subset

Name exact accepted clause IDs and bytes/hash; list returned clauses and their
evidence trigger. No omitted clause is inferred.

### `TM105-SEM-C` — return/defer

Name exact missing evidence and re-entry trigger. The package remains a
non-authoritative candidate and no implementation may rely on it.

## Unsigned return form

```text
DECIDE ROOT-TM105-SEMANTICS-01 <TM105-SEM-A|TM105-SEM-B|TM105-SEM-C> —
CANDIDATE SHA-256 <EXACT_SHA_OR_NA> — TBD SELECTIONS <EXACT ID=OPTION LIST OR
NA> — ACCEPTED CLAUSES <EXACT IDS OR NONE> — RETURNED CLAUSES <EXACT IDS OR
NONE> — MISSING EVIDENCE/REENTRY <EXACT TEXT OR NA> — SEMANTIC ACCEPTANCE ONLY;
NO IMPLEMENTATION, SCOPE_CHANGE, AFFECTED-CLIENT, RELEASE, OR MERGE AUTHORIZED —
<ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

Before presenting `TM105-SEM-A`, HELPS_HUMANS must materialize a no-TBD exact
candidate, refresh all hashes and compatibility analysis, and commission a new
independent refutation. The current candidate is not eligible for `SEM-A`
because `TBD-105-01` through `TBD-105-21` remain unresolved.
