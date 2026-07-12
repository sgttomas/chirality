# Assessment INSP-03: DEL-10-02 Protected Path and Proposal Path Policy

Deliverable: DEL-10-02
Package: PKG-10 Domain Engine Future Boundary
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `0aea715f573cfd7759d7fe3f13ca03285b53ef98`
Spec source: `Specification.md`

## Scope

This assessment inspected the future protected/proposal path policy and its boundary between domain truth, agent-writable proposal artifacts, adapter workflow, and human acceptance. It did not treat any protected path enforcement or `/api/domain/*` route as currently implemented.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| REQ001 - Policy remains future-boundary/gated. | PASS | `Specification.md` lines 3-21 excludes current domain operation execution, concrete OpenPipeStress behavior, concrete path patterns, and `/api/domain/*` endpoints; static source scans found no frontend domain path or route. | No runtime scope creep was found. |
| REQ002 - Protected paths and proposal paths are distinct concepts. | PASS | `Specification.md` lines 27-38 defines protected/proposal separation; `docs/TYPES.md` lines 534-542 defines the terms. | Vocabulary aligns with governed docs. |
| REQ003 - Agents may write proposals/summaries/review aids. | PASS | `Specification.md` lines 27-38 and `docs/PLAN.md` lines 293-298 preserve proposal-only agent output. | This is policy only. |
| REQ004 - Protected paths are write-quarantined. | PARTIAL | `docs/CONTRACT.md` lines 131-138 requires protected path quarantine; `Specification.md` lines 27-38 records the same policy. | Runtime enforcement hooks are not implemented for PKG-10. |
| REQ005 - Accepted mutation routes through adapter/workflow plus human gate. | PARTIAL | `docs/SPEC.md` lines 843-856 requires explicit human acceptance before applying domain operations. | Adapter/workflow and acceptance artifact are future/TBD. |
| REQ006 - Truth separation is preserved. | PASS | `docs/CONTRACT.md` lines 131-138 says domain engines own domain truth and Chirality cannot claim solver truth. | The local policy preserves the split. |
| REQ007 - Boundary notices are required. | PASS | `Specification.md` lines 27-38 requires boundary notices; `docs/CONTRACT.md` lines 131-138 forbids professional/code/external/solver-truth claims. | Final copy remains surface-specific. |
| REQ008 - Enforcement is not prompt-only; future hooks/workflow must enforce it. | PARTIAL | `Specification.md` lines 27-38 calls out profile/path hooks/workflow; `docs/CONTRACT.md` lines 81-83 says prompts are not runtime safety boundaries. | Future enforcement evidence is absent. |
| REQ009 - Concrete globs, manifests, and evidence slots remain TBD until accepted. | PASS | `Specification.md` lines 53-78 records concrete paths, manifests, ResponsibleParty, and fixture categories as TBD. | Unknowns are not prematurely specified. |
| REQ010 - Future protected-write fail-closed evidence is required. | TBD | `Specification.md` lines 53-63 names future evidence slots; no tests or fixtures exist. | This cannot pass until a future implementation exists. |
| REQ011 - Future proposal-write allowance evidence is required. | TBD | `Specification.md` lines 53-63 names future evidence slots; no tests or fixtures exist. | This cannot pass until a future implementation exists. |
| REQ012 - Future human-gate evidence is required. | TBD | `docs/SPEC.md` lines 843-856 and `docs/PRD.md` lines 712-727 require human acceptance; no concrete acceptance evidence format is accepted. | Human-gate proof remains a later ruling/work item. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Doc-only acceptance basis unresolved | High | The policy is documentation-only and cannot satisfy runtime enforcement criteria without a PKG-10 basis ruling. | INSP-04 / human ruling |
| Status-history truth mismatch | High | `_STATUS.md` says active code implementation is underway, conflicting with the future-boundary package posture. | INSP-05 roadmap / status repair |
| No concrete path syntax or enforcement tests | Medium | Protected/proposal path globs, manifests, fail-closed checks, proposal-write allowance checks, and human-gate evidence are all future/TBD. | Future R7 amendment |
| Dependency closure open | Medium | 5 active dependency rows remain open, including 3 TBD rows. | Dependency reconciliation |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-10-02 has 5 active rows: 2 `SATISFIED` and 3 `TBD`; closure remains open until the TBD rows are resolved.

## Forward Development Recommendation

1. Decide the PKG-10 doc-only acceptance basis before issuance. Type: governance ruling. Size: S. Strategic fit: ON-STRATEGY.
2. Repair the stale status-history wording for all PKG-10 deliverables without creating implementation scope. Type: status/documentation repair. Size: S. Strategic fit: ON-STRATEGY.
3. In the future R7 amendment, define protected/proposal glob syntax, manifest ownership, deterministic fail-closed tests, proposal-write tests, and human-gate records. Type: future domain enforcement design. Size: M. Strategic fit: ON-STRATEGY only if kept behind the domain-engine amendment gate.
4. Keep `/api/domain/*` and protected-write mechanics out of current scope until the amendment accepts them. Type: governance control. Size: S. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

This deliverable should not be issued under normal implementation gates until the owner decides how doc-only future-boundary deliverables are accepted. Runtime safety claims need actual hooks and tests; this wave only verifies that the draft policy is conservative and fenced.

## D-APP-56 R5 P43 annotation (2026-07-12)

The old-REQ001 static-scan sentence saying no frontend domain path existed is
preserved historical evidence at the Reviewed SHA. D-APP-49 through D-APP-52
subsequently authorized bounded profile and proposal-tool code. No
`/api/domain/*`, accept, apply, or force surface was introduced, so the
future-boundary/no-scope-creep conclusion remains valid while its former
absence evidence is superseded. No assessment verdict or lifecycle state
changes here.
