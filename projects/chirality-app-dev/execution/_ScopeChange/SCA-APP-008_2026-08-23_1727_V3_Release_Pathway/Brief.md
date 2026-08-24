# SCA-APP-008 — v3 Release Pathway Gate-1 Assessment

**Status:** `AWAITING_OWNER_ACCEPTANCE`
**Variant:** `SOFTWARE` / `SOFTWARE_DECOMP`
**Basis:** `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
**Requested by:** Ryan Tufts through HELP_HUMAN, 2026-08-23
**Stage:** Gate 1 assessment only; no decomposition amendment or propagation has been accepted or applied.

## Human request

Assess the App-side changes needed to seat the v3 release pathway after the owner ruled G0.25 passed. Produce the proposed carrier map, contract amendments, and objective-relative App DAG. Preserve every human gate: this package is not authority, does not activate implementation, and does not modify decomposition truth, contracts, code, registers, lifecycle, pointers, frontend, docs, Root surfaces, or release state.

## Accepted inputs

| Input | Basis identity | Role |
| --- | --- | --- |
| Re-issued App Phase-0 steer | `plans/steers/chirality_app_v3_phase0_steer_app_reissued_2026-08-23.md`, SHA-256 `fef516fda00a713785dd1cbfa38e4fdcea30ce2edfa0a265b81754fa84e86ab0` | Human-carried direction |
| G0 owner-ruling record | `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b` | Owner amendments to Revision 3.1 |
| A1 owner-ruling record | `plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md`, SHA-256 `f9b02806eeab1a578e6729c41fc367074758a2b95cc0eda9c8d2edbda446f314` | G0.25 PASS and re-stage rule |
| Release execution plan | `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, SHA-256 `b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` | Input, not authority |
| Active App decomposition | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, SHA-256 `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | Current decomposition truth, read-only |
| App contract | `projects/chirality-app-dev/docs/CONTRACT.md`, SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | Current contract truth, read-only |
| D-GOV-35 routed notice | `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md`, SHA-256 `9b8ebfe16e5241bc2c58b4bbc71032837632f5b07d776e82f11a273d2469cee7` | Coordination evidence, not App authority |
| Root SCA-004 state | Gate-5 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2`; owner confirmation R6-A; seven Root carriers with accepted SOWs at R7-A | Accepted Root context; cite, do not re-derive |

The active pointer `projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md` entered this assessment at SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` and remains read-only.

## Parsed Gate-1 actions

| Seq | Action | Entity | Assessment request | Validation |
| --- | --- | --- | --- | --- |
| 1 | `MODIFY` | App carrier set | Seat WP-01 through WP-11 App responsibilities on exact live deliverables, preserving DEL-04-01 as a probe and DEL-08-04 as the managed-delegation carrier. | Valid existing carrier IDs and live folders; proposed wording only. |
| 2 | `MODIFY` | DEL-08-04 / DEL-08-05 | Prospectively supersede the D-APP-74 tranche-scoped exclusion for v3 carriers, admit multi-child managed execution and the Root Agent 0/1/2 graph as App capabilities, and incorporate the D-GOV-35 native class without retroactive edit. | Human initiated by G0 D1; current D-APP-74 lines 101–104 contain the exclusion. |
| 3 | `MODIFY` | App role/UX carrier | Require Agent 0/1/2 entry for Codex sessions and offer Agent 2/TASK as `role not mechanically enforced` when G-ROLE fails, with `instruction-asserted` evidence calibration. | Human initiated by G0 A3; no mechanism-proof claim is added. |
| 4 | `MODIFY` | App account/consent, session, and security carriers | Seat `HostedEngineConsentPort`, root-private login explanation, three per-root command-network postures, resume continuity, v2→v3 migration, typed credential-storage states, and sender authorization for all six credential IPC handlers. | Existing live App surfaces identified; Root semantic ownership preserved. |
| 5 | `MODIFY` | App preparation, validation, and release carriers | Seat two-job installer via runtime-control IPC, unsigned preparation runbook, Shared Runtime Gate mapping, exact-candidate hold lifting at G6a, and owner-operated release lane. | Preparation and owner release acts remain distinct; F-APP-2 stays active. |
| 6 | `MODIFY` | App contract proposal | Draft K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, consent-port, and untyped-code text. | Proposal only; no `docs/CONTRACT.md` write. |
| 7 | `MODIFY` | App objective-relative dependency graph | Add the App DAG, typed Root notice edges, SCCs, proposed cycle moves, and non-gating cycle edges. | No dependency register write; subject to owner acceptance and later extraction. |

No action changes IDs, retires an entity, changes parent lineage, or applies decomposition truth. `ALLOW_RENUMBERING=false`.

## Gate-1 findings

1. The smallest assessed topology reuses live deliverables. “New carrier” means a newly explicit v3 responsibility seated by prospective amendment on an existing stable deliverable, not a new folder or ID in this assessment:
   - DEL-02-05 becomes the explicit App account/consent UX carrier while retaining its credential/runtime-feedback scope.
   - DEL-09-05 becomes the explicit release-operations carrier, with WP-09 runbook authoring/review strictly separated from WP-11 owner release acts.
2. DEL-04-01 remains probe-only. Exact App Server supply acceptance and protocol freeze remain Root-owned and separately gated.
3. DEL-08-04 remains the managed delegation bridge. The delegated-harness-native class is an additional Root-originated descendant class to be consumed and evidenced; it does not silently become managed delegation.
4. The D-APP-74 exclusion at lines 101–104 was limited to the SCA-APP-004 Woven Dialogue tranche by G0 D1. SCA-APP-008 may prospectively authorize the v3 carrier capability without rewriting D-APP-74.
5. G0.25/WP-00 is closed by A1. The old blanket frontend freeze is replaced by the re-stage rule: any future frontend mutation invalidates the staged R20 procedure for any future proof claim and requires a new staged revision plus fresh owner proof. This assessment itself writes no frontend bytes.
6. Root D-GOV-35 and Root SCA-004 are accepted upstream context. Their relationship to App work is represented only as typed notice edges.

## Exact interaction statements and preserved dispositions

**D-APP-103 interaction statement:** D-APP-103 **defers**: the per-attempt decision-replay packet is prepared after SCA-APP-008 applies so it covers both descendant classes once.

- D-APP-97 and F-APP-2 remain active through preparation and lift only at G6a for the exact candidate (G0 D2).
- TM-APP-030 remains for G-HELPER (G0 B2); this assessment makes no bundle-identity decision.
- TM-ROOT-122 / Electron 43.2.0 drift is a G1 blocker only (G0 B4), not a pin amendment here.
- Current packaging posture is the R18/Tranche-A frozen local `electronDist` supply: version 43.2.0, arm64 zip size `122090802`, SHA-256 `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`, verified before `electron-builder` receives `-c.electronDist=<verified-directory>`.
- App Sandbox is declined for rc.1; hardened runtime, Developer ID, and notarization remain later gates (G0 A5).
- Target is macOS arm64 only; a second target is deferred to a post-rc.1 scope change (G0 B1).
- Product posture label is `Opt-in Preview` (G0 A8).

## Gate posture

This package completes only the requested assessment output. Gate 2 impact material is presented for owner review, but the owner has not yet accepted the assessment, proposed amendment text, propagation plan, or execution. Therefore:

- `SCAStatus = AWAITING_OWNER_ACCEPTANCE`
- `DecompositionTruthState = UNCHANGED`
- `ImplementationAuthority = NONE`
- `LifecycleAuthority = NONE`
- `ReleaseAuthority = NONE`
