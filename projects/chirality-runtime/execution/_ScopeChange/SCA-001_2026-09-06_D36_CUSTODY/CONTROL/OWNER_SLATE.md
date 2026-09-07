# Runtime canonical application decision slate v1

**PROPOSED — not ruled.** Recommend option A: apply and validate the exact bounded canonical amendment, retaining the disclosed audit warning. This does not reopen the three settled D36/D126 custody choices or introduce a capability-policy decision.

## Reviewed basis

After freshness at 2026-09-07T03:53:38Z, HEAD/origin/main remained e1dee343. Parent verified the corrected prechange audit's 22-member handoff manifest `919e4c5a93de216847e6501f53fc0ca2fc7419a1e25ffd7358dc22012b88e428` and auditor identity `b63085403c0ab447ff9f534fc8973fcef9044978a14b023f02a8f9751f5ce297` at `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_D36_PRECHANGE_AUTHORIZED_2026-09-06_2145`. Parent read the audit, manager return and independent review, and verified the existing 37-member canonical candidate manifest `2770f5b5b21942b3418df0121ee6050ed92b120e830a5e58f4947286e2efe4ba`. No findings were identified against the exact change.

The prechange audit has zero blockers, one Check 9b warning for absence of an explicit companion inventory, and 40 informational filename observations at INITIALIZED. All 12 check dispositions are retained, including Checks 9 and 10 marked SKIPPED. These observations do not establish product absence or completion. Recommend accepting this audit as a usable baseline and retaining Check 9b as disclosed nonblocking debt for this bounded amendment; no inventory repair, waiver or debt-closure claim is proposed.

## Exact amendment

Review the [canonical patch](/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CUSTODY_AMENDMENT_PREPARATION_2026-09-06/AMENDMENT/CANONICAL.patch), [postimage index](/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CUSTODY_AMENDMENT_PREPARATION_2026-09-06/AMENDMENT/POSTIMAGE_INDEX.json), and controlling [impact, propagation and application checklist](/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_CUSTODY_AMENDMENT_PREPARATION_2026-09-06/AMENDMENT/CORRECTION_V2/IMPACT_PROPAGATION_AND_APPLICATION.md).

The amendment transfers settled D36/D126 decisions into Runtime canonical truth: add a claim-level custody supplement, bind it in the main document with its change entry, and update only DecisionRef/Notes in the ledger. Seven deliverable IDs, 66 requirements, four objectives, nine holds and topology are conserved. Historical maps remain unchanged.

Exact canonical postimage SHA-256 identities:

| Target | SHA-256 |
|---|---|
| Main document | `d26e03f580f1d33a7c906f8509418ab6d0f5774b7b5102a593dbae400eb381e1` |
| Ledger | `3d9b7210994804c53e7433fd497a8b417dcd7bae67c95b1bc9168abd8063e2d9` |
| Custody supplement | `e475a28d003cbbe44728ddc3cb24e407f7b286f24d9c105fba744a24ca46b309` |

## Owner options

**A — recommended: exact bounded application and validation.** Authorize Gate 2 impact, Gate 3 exact amendment and Gate 4 Stage 1 propagation as specified in the controlling checklist. SCOPE_CHANGE applies only the three canonical targets and creates the owning immutable SCA snapshot, application journal, claim delta, tool-generated cumulative supersession map, handoff and permitted pointer with truthful pending state.

Include exactly **one postchange AUDIT_DECOMP** run. Reauthorize the mapping in `AUDIT_BINDING_OVERRIDE_PROPOSED.md`, SHA-256 `a84c904be6802b5254a09c73b21ce45b705f6cdd097967a4d3a652d909d2a8d9`, solely for this postchange run. Refresh the three canonical pins and add D36 supplement authority only following the actual application act; retain all 12 checks and every unchanged binding. Require independent pre/post review. Check 10 records the actual pointer state at audit time; after normal snapshot/pointer creation, require a final snapshot/pointer backcheck. No circular self-hash or advance acceptance of unknown findings.

This complete validation scope is confirmed by the Runtime SCOPE_CHANGE relay. DEL06/DEL09 SOWs remain pending Stage 2 and are not edited now. Their later sequence remains actual accepted decomposition commit, then refrozen and reviewed SOW-basis repin, then owning application.

**B — pause:** prepare a separately specified explicit-inventory repair first. That requires a new bounded candidate and review; this slate does not authorize that repair.

## Approval boundary and next return

AGENT_SCOPE_CHANGE requires explicit Gate 2/3/4 authorization and the Gate 5 postchange audit. The earlier one-run prechange audit-method exception has been consumed; it is not reusable authority for the proposed postchange audit. Option A supplies only the exact staged scope above. Present the validated poststate for owner acceptance. Final postchange acceptance and Git acts remain existing gates.

No CHANGE commit, publication, merge, product source implementation, supplier acceptance, login/credential operation, protected-fixture retry or release is granted. This is an immutable derivative decision slate, not authority adoption, a standing queue, register update or activation.
