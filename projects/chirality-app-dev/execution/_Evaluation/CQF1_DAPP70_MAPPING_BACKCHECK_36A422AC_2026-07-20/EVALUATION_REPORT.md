# D-APP-70 Mapping Application Evaluation Report

## Verdict

`ACCEPT`

The D-APP-70 documentary mapping application is authority-faithful, complete
for the ruled scope, internally valid, preserved, and contained. This verdict
does not rule D-APP-71, select a preload physical lead, authorize source
repair, release CHANGE, or perform a Git action.

## Basis and method

- Branch: `codex/app-dev-dapp70-mapping-application-20260720`
- HEAD/application basis: `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`
- W1 state: terminal `APPLICATION_COMPLETE_AWAITING_V2`
- W1 RETURN / STATUS / applied MANIFEST SHA-256:
  `4228184e5eadcced8de6d261f87c42918c72c075002728fba2565366c803ed38` /
  `fdf1e9a2052fed915607696706eb24aeced275cf8cd9885e17322929463eb655` /
  `40c1ff5e7a0f9befb1e4b6c728fcebf66777211b059403e27fff92472ed2ee3e`

The manager independently re-extracted the subject from the accepted authority
and current bytes using strict JSON/CSV parsing, SHA-256 recomputation,
read-only Git comparison, inventory and manifest closure, status-diff review,
receipt and authority validators, repository self-check, and diff hygiene.
Two fresh sealed Agent-2 audits separately covered application content and
governance/preservation.

## Validated return inventory

| Audit | Verdict | SHA-256 | Validation |
|---|---|---|---|
| Application content | `PASS` | `63041440b1745061f779293c1e9f305046268366304de1d1ae3c68572e04194d` | Required basis, methods, counts, row/group, boundary, status/record, disposition, preservation, findings, unknowns, conflicts, and rerun fields present |
| Governance/preservation | `PASS` | `1bf0849b6e2b12604135d1493130f9156611b77a69b9ecadad1ba2f9d1e87952` | Required basis, methods, population, D-APP-71/receipt, preservation, validators, containment, findings, unknowns, conflicts, and rerun fields present |

Both returns lie in their unique authorized directories, cite in-scope
evidence, cover disjoint audit concerns, and agree with manager recomputation.
There are no partial returns, provenance gaps, or conflicts.

## Coverage and results

| Concern | Exact coverage | Verdict |
|---|---:|---|
| Frozen W1 population | 29/29; ordered-list hash `3a40c42bf979a502077320e4423df6343760cb7cde9c789c0ce545c1304e1005` | PASS |
| Pre-v16 HANDOFF_STATE prefix | 27,671 bytes; hash `bc332225643ae9a51855bef5e02b30c4167d0e28d23b7d9154eb2b69d593dc26` | PASS |
| Mapping paths | 22/22 unique, existing, exact CQF1 order and source hashes | PASS |
| Groups | 9; `5+4+6+1+1+1+1+1+2` | PASS |
| Treatments | 21 physical/primary + 1 blank-owner shared-only preload | PASS |
| Applied derivative | 7/7 files, manifest closure, no extras | PASS |
| Status outcomes | 5 changes; 4 closures + 1 narrowed D-APP-71 residual | PASS |
| Local provenance | 5/5 records with exact declared hashes and truthful bindings | PASS |
| Immutable source/SOW/dependencies | 22/22 + 5/5 + 10/10 | PASS |
| Upstream derivative / R3 / accepted V1 | 14/14 + 4/4 + 2/2 | PASS |
| Concurrent origin advance | 58/58 paths under `projects/chirality-piping/**`; zero overlap | PASS |

### Authority and retained boundaries

D-APP-70 is exactly `RULED (Option A)` and all nine recommendations are
applied without semantic transfer. Every owner, consumer, security, evidence,
UI-state, shared/split, capability, and integration boundary in the ruling is
retained. In particular, `frontend/electron/preload.ts` alone has blank
physical owner and
`SHARED_BOUNDARY_APPLIED_PHYSICAL_LEAD_UNRESOLVED`, retaining DEL-02-03
`selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
`safeStorage`/security.

### Status, residual, and record truth

DEL-02-01, DEL-03-03, DEL-06-02, and DEL-10-04 close only their ruled CQ-F1
Remaining entry. DEL-09-04 closes the ruled typing, proof-fixture, and
contract-lint portions and retains exactly one executable `(gated: D-APP-71)`
preload residual. That residual offers only DEL-02-03, DEL-02-05, DEL-09-06,
or deferral and denies path-level owner/source repair. DEL-09-04's unrelated
packaging/release line is byte-identical to the basis. The five local records
reproduce all status-before/status-after, source, SOW, dependency, ruling,
derivative, and retained-boundary claims.

All five status metadata prefixes remain byte-identical, so lifecycle,
Authorization Basis, and Checking Approval SHA are unchanged. MEMORY, source,
SOW, dependencies, decomposition, authority corpus, prior evidence,
release/publication, and hard-fence state are outside the change population.

### D-APP-71 and Receipt-80

Exactly one D-APP-71 packet and one register row exist. The row is
`AWAITING_RULING`; there is no ruling file and selection is null. The packet
neutrally presents DEL-02-03, DEL-02-05, DEL-09-06, and deferral, preserves the
other interests for each option, provides exact response syntax, attributes no
recommendation or selection, and authorizes no frontend repair.

Receipt-80 is unique and latest, has parent Receipt-79 and Examined-Through
`36a422ac5568a02ecf120c214f8e1fc96fd6ab45`, binds the actual W1, applied,
D-APP-71, and register outputs, and preserves both the V2 and D-APP-71 gates.

### Deterministic checks

- Strict duplicate-key JSON: every JSON bound into V2 passes. The known
  duplicate-key STATUS in terminal failed historical `R1-REPAIR2` remains
  excluded, preserved evidence and is not an accepted predecessor.
- Receipt validator: exit 0.
- Authority corpus: v9, 8/8 MATCH, no drift.
- Repository self-check: exit 0 at the existing 3 REVIEW / 6 WARN baseline.
- `git diff --check` and cached diff check: exit 0.
- Frontend/runtime gates: correctly skipped because all 22 source paths are
  byte-identical and none is in the changed population.
- Read/write containment: PASS; evaluation writes are confined to the
  additive evaluation root and V2 instance.

## Findings, conflicts, and unknowns

- Findings: 0.
- Blocking findings: 0.
- Conflicts: 0.
- Unknown mandatory evidence: 0.
- Waivers: 0.
- Repair recommendations: none.
- Required rerun: none for the audited bytes.

The known failed historical parser artifact is neither suppressed nor
promoted into the accepted V2 basis; it does not conflict with the corrected,
accepted V1-RECHECK3 evidence bound by this run.

## Decision queue and handoff

HELP_HUMAN may accept this V2 derivative and consider the evaluated D-APP-70
application eligible for a later, separately released CHANGE handoff. Any
change to the basis, ruling, mapping/application package, status/record bytes,
preservation surfaces, D-APP-71 state, receipt/register state, or origin
disjointness requires rerunning V2. D-APP-71 remains `AWAITING_RULING` and
silence selects nothing.
