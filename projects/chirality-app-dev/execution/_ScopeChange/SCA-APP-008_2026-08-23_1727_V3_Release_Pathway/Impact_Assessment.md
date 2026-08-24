# Impact Assessment — SCA-APP-008

**Status:** `AWAITING_OWNER_ACCEPTANCE`
**Assessment basis:** `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
**Effect today:** none outside this immutable assessment folder.

## Summary

SCA-APP-008 is a prospective App carrier and contract amendment for the v3 rc.1 pathway. It does not transfer Root runtime ownership to App and does not activate product work. The proposed scope is structural in the sense of broadening explicit duties on existing stable deliverables, but it adds, removes, reclassifies, merges, or splits no package/deliverable identity. This avoids orphan and parent-lineage risk while making the new work dispatchable only after owner acceptance and later gate-specific activations.

## Evidence basis

| Evidence | Reproducible fact | SHA-256 |
| --- | --- | --- |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md:101-104` | SCA-APP-004 excluded arbitrary Agent 0/1/2 graphs and multi-child execution. G0 D1 limits that exclusion to that tranche and directs prospective v3 supersession. | `1e59194a4f651346c9a7204ace0084fe8ac2115200881799485a9e70443e5ec3` |
| `projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts:205-213` | Untyped and ephemeral Agent 2 delegation are currently denied together; D-GOV-35 requires App disposition in WP-06. | `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c` |
| `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts:480-496` | Managed delegation already checks active sibling write overlap and fails closed on unproved status. | `0a3dec1309bde70548daee39a48b280ece6886f837d8c4d4b40b85f4f6a6d180` |
| `projects/chirality-app-dev/frontend/electron/api-key-ipc.ts:110-176` | Six credential IPC handlers currently lack the sender check required by the proposed security carrier. | `3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb` |
| `projects/chirality-app-dev/frontend/electron/runtime-control-ipc.ts:85-95` | `isAuthorizedSender` supplies the policy pattern to adopt. | `5006bef6922295eb24c54f4a034f2d42929c71b80704b4fe03f8e7e5af36026a` |
| `projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md:161-178` | §13 Shared Runtime Gate is validation evidence only and grants no release or lifecycle authority. | `dbfa56aa71ae9934f84247ec115721129e3aac4fb2cedfd5b5cab212c74bc382` |
| `projects/chirality-app-dev/execution/_Coordination/NOTICE_D-GOV-35_DELEGATED_HARNESS_NATIVE_CLASS.md` | Root recognizes managed and native executable delegation classes and routes App follow-on to SCA-APP-008/WP-06. | `9b8ebfe16e5241bc2c58b4bbc71032837632f5b07d776e82f11a273d2469cee7` |
| `projects/chirality-app-dev/frontend/scripts/verify-electron-dist.mjs:9-18` and `pack-electron-with-supply.mjs:7-17,46-47` | Frozen Electron supply is exact-version/size/hash checked and injected as local `electronDist`. | `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457`; `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db` |

## Impact by action

| Action | Direct proposed surface after owner acceptance | Downstream consumers | Main risk and control |
| --- | --- | --- | --- |
| Seat v3 carriers | Decomposition deliverable rows, Scope Ledger bindings, exact SOWs/contexts in a later approved Gate-5 tranche | WORKING_ITEMS, preparation, dependency extraction, Task Management | Work could appear dispatchable too early. Control: every carrier remains `PROPOSED_HELD` until owner acceptance and later gate activation. |
| Prospectively supersede D-APP-74 exclusion | DEL-08-04/05 amendment and a future App decision/supersession binding | Managed delegation, native-descendant consumption, UX, evidence records | Could conflate native descent with managed Agent 2. Control: preserve two classes, attribution, and `instruction-asserted` calibration. |
| Add Agent 0/1/2 role-entry parity | DEL-02-02/DEL-02-05 UX and DEL-08-04/05 governance evidence | Session creation, Work/Agents UI, conformance | UX could claim mechanical non-delegation it cannot prove. Control: mandatory `role not mechanically enforced` label on G-ROLE failure. |
| Add account/consent boundary | DEL-02-05, DEL-04-05, DEL-05-01, DEL-09-06 | Root account/consent contract and worker acquisition | Root/account mismatch or hidden ambient auth. Control: root-private `CODEX_HOME`, per-root login explanation, exact consent identity, fail closed. |
| Add three command-network postures | DEL-02-05 consent UI and DEL-09-06 security evidence | Root API v2 `networkApprovalContext` | Prompt grouping may exceed a single request. Control: show host/protocol and caveat; `acceptForSession` only by explicit user act; default off. |
| Add v2→v3/resume continuity | DEL-05-01/04 and DEL-03-03 | Session store, replay, Woven Dialogue | False in-flight reattach or destructive migration. Control: no in-flight reattach claim; `thread/resume` only when root/account/policy digest match, otherwise fresh thread. |
| Add installer/release lanes | DEL-09-04/05/06 and DEL-09-01/02/03 | Runtime-control IPC, packaging, signing/notary owner acts | Preparation evidence could be misrepresented as release readiness. Control: F-APP-2/D-APP-97 active through preparation; exact-candidate G6a owner gate. |
| Propose contract amendments | `Contract_Amendments.proposed.md` only in this assessment | Later App contract SCA | Proposed wording could be mistaken for binding contract. Control: repeated `PROPOSED_NOT_APPLIED` state and no docs write. |

## Carrier effect and package-role classification

| Surface | Package role | This tranche | If later accepted |
| --- | --- | --- | --- |
| Active SOFTWARE_DECOMP document | Working surface / authoritative decomposition truth | `NO_CHANGE` | Direct edit only through accepted SCOPE_CHANGE Gate 5. |
| Active App `docs/CONTRACT.md` | Authoritative product contract | `NO_CHANGE` | Direct edit only after explicit contract-amendment acceptance. |
| Existing deliverable folders and SOWs | Working surfaces derived from accepted decomposition/carrier activation | `NO_CHANGE` | Direct edits only through the exact approved propagation plan. |
| This SCA folder | Snapshot / handoff assessment artifact | `DIRECT_EDIT` | Remains immutable after publication; it does not become active until owner acceptance/application. |
| `WORK_GRAPH.json` / `DAG.md` | Derivative assessment package | `DIRECT_EDIT` | Dependency extraction/regeneration required after accepted carrier application. |
| Root D-GOV-35 notice / Root SCA-004 | External accepted context and notice evidence | `NO_CHANGE` | Consumed through notice edges only. |
| App `_ScopeChange/_LATEST.md` | Active snapshot pointer | `NO_CHANGE` | May move only in a later explicitly approved Gate-5 act. |

## App work-package coverage

| WP | App impact | Proposed exact carrier posture |
| --- | --- | --- |
| WP-00 | Closed evidence context only. | DEL-09-04 R20 proof remains the subject evidence; A1 re-stage rule governs future frontend mutation. |
| WP-01 | Governance/carrier assessment. | SCA-APP-008 plus DEL-01-01 and exact affected deliverables; no implementation. |
| WP-02 | Supply/protocol evidence. | DEL-04-01 stays probe-only; Electron 43.2.0 frozen supply is current packaging posture, not a governed pin amendment. |
| WP-03 | Two-job supervisor installation and packaged-host evidence. | DEL-09-04 carries App installer/package integration through runtime-control IPC; Root owns supervisor/control semantics. |
| WP-04 | Account/consent and typed credential state. | DEL-02-05 is the new explicit App account/consent UX carrier; DEL-04-05 carries credential bridge conformance. |
| WP-05 | Adapter/event/API-v2 consumption. | DEL-03-03 and DEL-05-02 consume the Root closed protocol/event schema; no Root semantics are redefined. |
| WP-06 | Delegation, approval, containment. | DEL-08-04/05; native and managed class distinction; `subagent-governance.ts:205-213`; D-APP-103 interaction referenced from `Brief.md`. |
| WP-07 | Desktop UX/privacy/accessibility/security. | DEL-02-02/05 and DEL-09-06; role labels, login/consent, six credential sender checks, `Opt-in Preview`. |
| WP-08 | Migration/restart continuity. | DEL-05-01/04 and DEL-03-03; lazy v2→v3, typed account/storage transitions, resume-or-fresh behavior. |
| WP-09 | Unsigned preparation and reviewed runbook. | DEL-09-04/05/06; runbook authored/reviewed; no production signing/notary call. |
| WP-10 | Conformance/release-readiness evidence fan-in. | DEL-09-01/02/03/06 with RQG §13; exact gates remain owner/reviewer acts. |
| WP-11 | Actual release operation. | DEL-09-05 receives the new explicit release-operations carrier responsibility, but it cannot act before G6a and the owner-exact artifact ruling. |

## Dependency and cycle risks

Three objective-relative SCCs exist in the assessment DAG:

1. **Delegation evidence SCC** — DEL-08-04 governance and DEL-08-05 run records mutually inform each other. Proposed move: `DECOMPOSE`; freeze class/authority semantics first, then evidence schema. The evidence-feedback edge is non-gating until owner acceptance.
2. **Account/migration/UX SCC** — DEL-02-05 consent UX, DEL-05-01 migration, and DEL-05-04 replay/resume need a common state vocabulary. Proposed move: `DECOMPOSE`; accept Root account/consent schema and App contract first, then migration, then UX/replay fixtures. Cross-feedback edges remain non-gating.
3. **Runbook/validation SCC** — DEL-09-05 runbook content and DEL-09-06/01/02/03 evidence constrain each other. Proposed move: `INVERT`; author a preparation draft in WP-09, validate it, then gate the owner WP-11 procedure. Review feedback is non-gating until the owner accepts the move.

No cut or merge is silently selected. Any future cut/merge remains a human act.

## Orphan and structural risk

- Package additions: `0`
- Deliverable additions: `0`
- Deliverable removals/reclassifications: `0`
- Parent changes: `0`
- Stable ID reuse: `0`
- Current live App carrier folders resolved by the DAG: all App nodes; see `WORK_GRAPH.json`.
- Root relationships are named notice edges, not App-owned nodes.

The current 10-package / 51-deliverable topology stays intact. Any later owner preference for a new physical deliverable instead of the assessed stable-ID amendments requires a revised Gate-1 assessment before Gate 3.

## Derivative-package and rerun status

| Package | Owner | State after this assessment | Required action after owner acceptance |
| --- | --- | --- | --- |
| Active decomposition | SCOPE_CHANGE | `CURRENT_UNCHANGED` | Apply exact accepted text at Gate 5, then post-change audit. |
| Deliverable SOW/context set | WORKING_ITEMS / owning carrier | `CURRENT_UNCHANGED` | Amend only the accepted carriers under sealed briefs. |
| App contract/invariant coverage | App governance / SCOPE_CHANGE | `CURRENT_UNCHANGED` | Apply accepted contract wording and regenerate coverage register. |
| Dependencies / DAG derivatives | dependency extraction / AUDIT_DEP_CLOSURE | `ASSESSMENT_ONLY` | Re-extract after carrier application; validate closure. |
| Task Management register | TASK_MANAGEMENT | `CURRENT_UNCHANGED` | Owner triage is separate; no row write in this tranche. |
| Release/package evidence | WORKING_ITEMS / REVIEW | `FROZEN_SEPARATELY_GATED` | Run only at named WP gates and exact-candidate owner acts. |

## Holds and non-claims

- D-APP-97 / F-APP-2 remain active through preparation; lift only at G6a against the exact candidate.
- TM-APP-030 remains open for G-HELPER; no bundle-identity choice is inferred.
- TM-ROOT-122 is a G1 blocker only; this SCA does not amend the Electron pin.
- RQG §13 is mapped as validation evidence only and grants no release, publication, signing, notarization, lifecycle, or professional-reliance authority.
- macOS arm64 is the rc.1 target. A second target is deferred to a post-rc.1 scope change.
- No App Sandbox requirement is proposed.

## Assessment recommendation

Return the exact bytes to Ryan Tufts for Gate-1/Gate-2 acceptance consideration. Until the owner accepts them, all proposed carriers and contract wording remain non-dispatchable and `_LATEST.md` must not move.
