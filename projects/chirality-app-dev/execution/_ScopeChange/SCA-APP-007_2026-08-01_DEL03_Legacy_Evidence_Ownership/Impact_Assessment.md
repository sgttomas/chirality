# Gate 2 Impact Assessment — DEL-03 Legacy Evidence Ownership

**Gate state:** `ACCEPTED_2026-08-01`

## Preferred disposition

Migrate the two historical network-policy proof bundles byte-for-byte from the
undeclared evidence-only container into accepted `DEL-09-06` under an explicit
`Evidence/Historical_DEL-03-06/` provenance boundary, repair future output
routing and current labels in the proof script, and remove the now-empty old
physical container. Do not amend the decomposition.

## Four-lens assessment

| Lens | Impact |
|---|---|
| Decomposition structure | No change to Packages, Deliverables, Scope Ledger, Objectives, Decision Log, Change Log, IDs, topology, envelopes, or ownership text. |
| Variant-local metadata | `DEL-09-06/_STATUS.md` and sibling `MEMORY.md` receive provenance-only append entries after paired read; lifecycle and Checking Approval SHA remain unchanged. No `_CONTEXT.md` change is required because it already matches accepted truth. |
| Downstream consumers | The proof runner default path and current labels change. Historical evidence citations remain immutable; the migration record maps their former paths to live locations. AUDIT_DECOMP must rerun after migration. The contract-pin test covering the script must pass. |
| Invariant/telemetry risk | Byte loss, path-citation ambiguity, accidental adoption of retired `DEL-03-06`, and semantic collision with current `OI-002` are the material risks. Hash manifest, Git rename review, provenance map, no-topology diff, and post-audit control them. |

## Package-role classification

| Surface | Package role | Candidate handling |
|---|---|---|
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | working surface / authoritative decomposition truth | `NO_CHANGE` |
| `execution/_ScopeChange/_LATEST.md` | active snapshot pointer | unchanged through Gates 1–4; advanced only after owner-confirmed Gate-5 closeout |
| Final SCA-APP-007 folder | immutable snapshot / handoff artifact | finalized after Gate-5 confirmation and named by the active pointer |
| Fresh AUDIT_DECOMP snapshot | derivative audit evidence | pre-change baseline; post-change rerun required after approval/execution |
| Orphan `DEL-03-06/.../Evidence/` | derivative deliverable evidence in an invalid physical owner container | byte-preserving migration |
| `DEL-09-06/.../Evidence/Historical_DEL-03-06/` | derivative deliverable evidence under accepted owner | receive historical proof bundles plus provenance/hash manifest |
| `frontend/scripts/run-network-policy-proof.mjs` | downstream implementation/validation consumer | exact routing and label correction |
| `DEL-09-06/_STATUS.md` and `MEMORY.md` | variant-local lifecycle/operational metadata | append provenance only; no lifecycle transition |
| Historical SCA/coordination/audit/proof artifacts | immutable historical evidence | `NO_CHANGE`; mapped, not rewritten |

## Evidence inventory and orphan risk

- Source container: 38 tracked files, 97,817 logical bytes, Git tree
  `a5ba2c806734feeb68f6160f2961c6597d44b40d`.
- Proof bundle 1: `OI-002_PROOF_2026-07-22_060044/` — 27 files, added by
  `4412157d1`.
- Proof bundle 2: `OI-002_PROOF_2026-07-23_061410/` — 11 files, added by
  `deed6f58f`.
- Source contains no child deliverable metadata, so there is no lifecycle or
  dependency state to retire or remap.
- After migration the expected undeclared-deliverable count for this residue is
  zero. `PKG-00` reverse-only control surfaces are unrelated and remain outside
  this candidate.

## Label collision

The retained script currently emits `OI-002` labels, but current decomposition
`OI-002` concerns SDK transcript placement, not network policy. Future output
must use neutral `NETWORK_POLICY_PROOF` labels while historical directory names
and file contents remain unchanged. The separately carried `CONF-002` OCSP/CRL
proof-limitation note is not dispositioned by this migration and must remain
unchanged unless separately ruled.

## Derivative-package state

| Package/surface | Owner | State after approved migration | Closure action |
|---|---|---|---|
| Accepted decomposition | SOFTWARE_DECOMP / SCOPE_CHANGE | CURRENT | prove zero diff |
| `DEL-09-06` evidence set | WORKING_ITEMS | CURRENT after hash/provenance validation | collect migration evidence |
| Proof runner | WORKING_ITEMS/TASK implementation owner | CURRENT after static/test validation | run contract-pin test and `node --check` |
| Decomposition coverage audit | AUDIT_DECOMP | STALE_REBUILD_REQUIRED | run scoped post-change audit |
| Historical SCA/coordination evidence | original owning workflows | CURRENT_AS_HISTORY | do not edit; use migration map |

## Alternatives

1. **Add `DEL-03-06` now — not recommended.** It duplicates current
   `DEL-09-06` and contradicts accepted no-topology-change evidence.
2. **Leave residue in place — not recommended.** It preserves a known
   reverse-coverage warning and lets future proofs continue colliding with a
   retired owner and the current meaning of `OI-002`.
3. **Copy rather than move — not recommended.** It creates two live evidence
   owners and leaves the undeclared container in scan scope.

## Gate 2 decision

The human accepted this impact assessment as written. The immutable-history
rule and post-change audit obligation are binding on Gate 5.
