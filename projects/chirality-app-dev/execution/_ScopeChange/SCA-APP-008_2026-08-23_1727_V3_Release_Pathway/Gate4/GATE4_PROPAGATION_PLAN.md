# SCA-APP-008 Gate 4 — Exact Propagation Plan

**State:** `AWAITING_OWNER_APPROVAL`
**ReadyForNextPhase:** `NO`
**Authority effect:** `CANDIDATE_ONLY — NOTHING_APPLIED`
**Basis commit:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Gate-3 source:** `Gate3/GATE3_AMENDMENT_PACKAGE.md`, SHA-256 `1a8048f4840cffd9932202d1822f497de5f7aa07aa1872e250c6e870846cf6df`

## Owner decision requested

Approve, revise, or reject this Gate-4 plan for a later, separately authorized Gate-5 application. Approval of this plan would not apply either candidate post-image, accept the concordance-gated contract wording, move `_LATEST.md`, alter a carrier SOW or lifecycle, dispatch implementation, route the Root notice, or authorize any release act.

The decomposition and contract groups are deliberately separable. The decomposition group may proceed in a later Gate-5 act if the owner approves its exact bytes. The contract group remains ineligible until Root/App concordance resolves the K-EVENT-4 path/schema question, confirms invariant-ID collision freedom, produces any required exact companion-register update, and the owner approves the resolved exact group.

## Drafting sequence and mechanical hash proof

HELP_HUMAN ran candidate whitespace against basis `f485b5d3b663f42be8f8cab8432ced9024d7381b` on the final N1 plus N3 candidate set before this hash-pinning artifact was generated and reported `PASS`; `git diff --check` also passed. The earlier N2 brief was stopped before any N2 write when N1 changed after its first release boundary. The V2 grant at `execution/_Coordination/AgentRuns/APP_V3_PHASE1_2026-08-23/amendments/N2-SCOPE-CHANGE-01/V2.md` supersedes that brief and fixes the final N1 identity above. These are sequencing facts, not owner approval.

N2 mechanically reconstructed both complete candidate files in `/private/tmp` by applying the N1 transactions in their stated order. Every pre-image or insertion anchor was required to occur exactly once. The reconstruction failed closed on missing or duplicate bytes. The computed post-image identities exactly match N1:

| Target | Current pre-image SHA-256 | Mechanically reconstructed post-image SHA-256 | Reconstructed bytes | Match |
| --- | --- | --- | ---: | --- |
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` | 112419 | `PASS` |
| `projects/chirality-app-dev/docs/CONTRACT.md` | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` | `41cb6a62c6991c37559d1fcffeb75d9c76be2432ea84b1d1c5f864d8a3d9c9a6` | 34198 | `PASS` |

No candidate file produced in `/private/tmp` is authoritative or an application artifact.

## Package-role classification

| Surface | Package role | Gate-5 classification | Requirement |
| --- | --- | --- | --- |
| Active SOFTWARE_DECOMP markdown | `working surface` / authoritative decomposition truth | `DIRECT_EDIT`, decomposition group | Apply only exact D-01 through D-05 bytes after matching the pre-image SHA-256. |
| App `docs/CONTRACT.md` | authoritative product contract | `DIRECT_EDIT`, concordance-gated contract group | Apply only the exact resolved and owner-approved C-01 through C-11 group. The current question-bearing candidate is not yet eligible. |
| `execution/_Decomposition/contract_invariant_coverage_register.csv` | `authoritative companion register` | `STALE_REBUILD_REQUIRED_IF_CONTRACT_APPLIES` | Current SHA-256 is `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`. Before contract application, concordance must produce and the owner must approve an exact post-image covering every changed/new invariant. No post-image is invented here. |
| Existing carrier SOW, `_CONTEXT.md`, `_STATUS.md`, `_DEPENDENCIES.md`, and lifecycle files | working surfaces downstream of accepted decomposition | `NO_CHANGE_IN_THIS_GATE5_PLAN` | N1 supplies no exact transaction for these files. Carrier activation and implementation remain separate owner-gated acts. |
| Deliverable dependency records and extracted graph | authoritative local dependency records plus derivative graph | `STALE_REBUILD_REQUIRED_AFTER_DECOMPOSITION_APPLICATION` | Re-extract dependencies for amended carriers, then audit the resulting graph. Do not hand-edit a dependency to mimic extraction. |
| `DAG.md`, `WORK_GRAPH.json`, and the frozen Phase-0 audit | `derived publication artifact` / assessment evidence | `HISTORICAL_ASSESSMENT_ONLY` | Preserve frozen bytes. The assessment PASS cannot substitute for post-application evidence. |
| This Gate-3/Gate-4 package and later Gate-5 run evidence | `snapshot / handoff artifact` | `DIRECT_EDIT_ONLY_IN_SEPARATELY_AUTHORIZED_GATE5_ADDITIONS` | Preserve the accepted Gate-1/2 files. Add new application evidence; never rewrite frozen assessment bytes. |
| `execution/_ScopeChange/_LATEST.md` | active snapshot pointer | `SEPARATE_OWNER_APPROVED_GATE5_POINTER_WRITE` | Current SHA-256 is `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`. It moves only if the owner expressly authorizes exact pointer bytes in the Gate-5 act and all named pre-pointer gates pass. |
| App Task Management register | coordination register | `NO_CHANGE` | Must remain byte-identical at SHA-256 `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`. |
| Frontend tree | product source/package tree | `NO_CHANGE` | Must remain tree object `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`. A mutation also invokes the A1 re-stage rule. |
| `DRAFT_NOTICE_TO_ROOT.md` | unrouted snapshot candidate | `NO_CHANGE_UNROUTED` | Routing is not part of Gate 5 unless separately authorized after application. |

## Ordered Gate-5 application plan

### 0. Open only under a new exact owner act

The later Gate-5 brief must name:

1. the exact basis commit and this Gate-3/Gate-4 package identities;
2. whether it authorizes the decomposition group only or both groups;
3. if the contract group is included, the owner-approved concordance answer for K-EVENT-4, collision disposition for `K-CONSENT-1` and `K-UNTYPED-1`, exact resolved contract bytes, and exact invariant-coverage companion-register bytes;
4. whether exact `_LATEST.md` bytes may move after all validation and rerun gates pass.

Absent any item, hold only the affected group. Never infer approval from this plan.

### 1. Freeze and prove all pre-images before write

1. Require `HEAD` and the owner-approved Gate-5 basis to have the expected ancestry and a clean owned write set.
2. Re-hash the final Gate-3 and Gate-4 files.
3. Require the decomposition target to equal `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83`.
4. If the contract group is authorized, require the contract target to equal `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` and the companion register to equal its owner-approved pre-image.
5. Require `_LATEST.md`, the App Task Management register, and the frontend tree to equal the identities in the classification table.
6. Materialize recovery copies from exact Git blobs into a private temporary directory and verify their SHA-256 values. Do not rely on mutable worktree copies as rollback truth.
7. Reconstruct every authorized candidate in a temporary directory from the exact transactions; require each declared post-image SHA-256 before replacing any target.

Any mismatch aborts before write and returns the drift to the owner. Do not rebase, paraphrase a transaction, or opportunistically refresh a hash.

### 2. Apply the decomposition group atomically

Apply D-01 through D-05 exactly and in this order to one candidate file:

1. D-01: DEL-02-05 account/consent UX carrier row;
2. D-02: DEL-08-04 managed/native class semantics and managed-delegation carrier row;
3. D-03: DEL-08-05 descendant evidence row;
4. D-04: DEL-09-05 release-operations carrier row with strict WP-09/WP-11 separation;
5. D-05: insert DEC-023 and the SCA-APP-008 change-log row after their exact anchors.

Require the complete file to hash to `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` before atomically replacing the live target. Confirm unchanged 10-package/51-deliverable topology, stable IDs, objectives, SOW relations, context-envelope relations, and scope mappings. D-APP-103 continues to **defer**; no decision-replay packet is created in this act.

### 3. Apply the contract group only after concordance and owner approval

The contract group is one atomic candidate set. Apply nothing from it while the K-EVENT-4 question remains unresolved or the two proposed invariant IDs remain collision-unconfirmed.

Once eligible, apply C-01 through C-11 in N1 order:

1. replace K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3, K-EVENT-4, and K-EVENT-6;
2. insert K-CONSENT-1 after the post-C-04 K-KEY-1 row;
3. insert K-UNTYPED-1 after K-SUBAGENT-3;
4. insert all six consequential enforcement-map rows after the retained `Release validation` row;
5. insert the SCA-APP-008 accepted-scope-change row after SCA-APP-004.

For the currently published question-bearing candidate, the mechanically reconstructed identity is `41cb6a62c6991c37559d1fcffeb75d9c76be2432ea84b1d1c5f864d8a3d9c9a6`. That hash proves N1 reproducibility but is explicitly not an eligible authoritative contract post-image. Concordance must publish the resolved exact contract candidate and its new SHA-256; the owner must approve that exact identity before application.

In the same owner-approved contract application group, apply the exact companion-register candidate that adds/updates all affected invariant rows and relationships. If that exact candidate, its pre-image SHA-256, or its post-image SHA-256 is absent, abort the contract group. Never leave a changed contract with a stale 81-ID/48-family coverage claim.

### 4. Consume the A2-B SCC orderings without lifting downstream gates

| SCC | Accepted move and application consumption | Non-gating feedback | Downstream gate that remains |
| --- | --- | --- | --- |
| `SCC-DELEGATION-EVIDENCE` | `DECOMPOSE`: apply/freeze DEL-08-04 class and authority semantics before DEL-08-05 reconstructible evidence semantics. Preserve managed/native distinction and do not infer Agent 2 from native descent. | E-020, DEL-08-05 to DEL-08-04, remains non-gating. | Carrier application does not activate implementation; WP-03/WP-05 fixtures and their explicit later implementation act remain required. |
| `SCC-ACCOUNT-MIGRATION-UX` | `DECOMPOSE`: accepted account/consent vocabulary first, then non-destructive migration, then resume/fresh/replay UX. The Gate-5 carrier row seats DEL-02-05 but does not dispatch DEL-05-01 or DEL-05-04 work. | E-018, DEL-05-04 to DEL-02-05, remains non-gating. | **Accepted Root/App account/consent contract.** |
| `SCC-RUNBOOK-VALIDATION` | `INVERT`: preserve validation/security before freezing the exact owner procedure; keep WP-09 authoring/review separate from WP-11 execution. The Gate-5 carrier row does not authorize either release act. | E-032, DEL-09-05 to DEL-09-06, remains non-gating. | **G6a exact-candidate ruling.** |

No cycle is cut, merged, or silently linearized. A2-B accepted the orderings, not implementation or release authority.

### 5. Perform direct post-write validation before downstream reruns

1. Re-hash each applied target and require its exact owner-approved post-image SHA-256.
2. Re-run the transaction matcher against the applied files; every old pre-image must be absent and every expected post-image/inserted row must occur exactly once.
3. Recount topology and stable IDs; require 10 packages and 51 deliverables with no parent, objective, Scope Ledger, SOW, or context-envelope drift.
4. If the contract group was applied, run the exact Root/App concordance validator, invariant census/collision validation, enforcement-map checks, and decomposition companion-register validation. Reconcile the App authority corpus from `projects/chirality-app-dev` with `PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` after regenerating the governed corpus through its accepted workflow.
5. Confirm no SOW, status, dependency, lifecycle, code, frontend, Root, plan, or other-project surface changed outside the exact later Gate-5 write set.

Any failure triggers rollback before pointer movement.

### 6. Re-extract dependencies and run fresh closure evidence

After the decomposition carrier rows are applied, dispatch the registered dependency-extraction workflow for the amended carriers DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05. The extraction must cover both descendant classes once, preserve A2-B non-gating feedback edges, and produce exact evidence for all changed dependency records.

Then dispatch a fresh named audit:

`AUDIT_DEP_CLOSURE — SCA-APP-008-GATE5-POST-APPLICATION`

The audit must consume the post-application decomposition and newly extracted dependency records, resolve every endpoint, reproduce the accepted SCC moves and gating posture, identify any new SCC rather than linearizing it, and return a new immutable issue log, summary, and return. The frozen Phase-0 `Audit/AUDIT_DEP_CLOSURE_RETURN.md` PASS is assessment evidence only and cannot substitute for this run.

A blocking extraction or audit result keeps the SCA open, prevents `_LATEST.md` movement, and is recorded in the four-state handoff. It is not manually upgraded.

### 7. Run the full Gate-5/pre-push validator set

Run from repository root unless a command says otherwise:

```text
python3 tools/validation/validate_candidate_whitespace.py --base-ref <GATE5_BASIS_COMMIT>
python3 tools/validation/validate_agent_instructions.py
python3 tools/validation/validate_instruction_entrypoints.py
python3 tools/taskmgmt/taskmgmt.py validate --register projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv
python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
git diff --check
```

Additional exact checks:

- App register SHA-256 remains `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`.
- Frontend tree remains `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`, and the candidate diff contains no frontend path.
- `_LATEST.md` remains SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794` until the explicitly authorized pointer step.
- The frozen Gate-1/2 assessment file hashes remain exactly those accepted in A2.
- Instruction-surface diff is empty. After CHANGE creates the candidate commit, run CI-form G4 exactly as:

```text
python3 tools/validation/validate_instruction_tranche_manifest.py --base <GATE5_BASIS_COMMIT> --head <GATE5_CANDIDATE_COMMIT> --added-manifests-only
```

Expected G4 result: zero instruction-surface paths and zero required added manifests, with the live manifest corpus still schema-valid.

The post-application dependency extraction and fresh named closure audit must pass in addition to this validator set. Passing validators do not create owner acceptance, lifecycle, implementation, or release authority.

### 8. Move `_LATEST.md` only as an expressly authorized final Gate-5 write

The pointer is not changed merely because target files were written. Only after:

1. every owner-authorized target equals its exact approved post-image;
2. every required companion surface is current;
3. dependency re-extraction and `SCA-APP-008-GATE5-POST-APPLICATION` audit return non-blocking;
4. the full validator set passes; and
5. the Gate-5 owner direction expressly authorizes exact pointer bytes,

may `_LATEST.md` move to SCA-APP-008. Verify its exact post-image SHA-256 after the write. Without that separate authorization, leave it byte-identical and close the application run as awaiting pointer authority or derivative closure, as applicable.

## Rollback and abort protocol

Rollback restores bytes; it never rewrites history, rebases, force-pushes, or uses a broad destructive checkout/reset.

1. **Before first target replacement:** any identity, anchor, concordance, write-set, or candidate-hash mismatch aborts with no write.
2. **During candidate construction:** any missing/duplicate anchor or unexpected hash aborts without touching a live target.
3. **After one target replacement but before pointer movement:** stop all further application, restore every changed target from its exact verified basis blob, restore any companion-register pre-image, and verify the pre-image SHA-256 values in the target table. Remove only temporary candidate files owned by the failed run.
4. **If the contract group fails:** restore the whole atomic contract group and companion register. Never retain a partial C-01 through C-11 state.
5. **If dependency extraction, closure audit, or validators fail:** restore all Gate-5 target pre-images unless the owner had expressly authorized a non-closure diagnostic state. In either case `_LATEST.md` stays at its pre-image.
6. **If pointer movement itself fails or post-pointer verification fails:** restore the exact pointer pre-image and all Gate-5 target pre-images, verify every restoration hash, record the failed attempt, and return to the owner.
7. Preserve failure evidence inside the authorized Gate-5 run root; never claim closure from a rolled-back or partial state.

## Post-application state and rerun obligations

| Surface | State immediately after direct application | Owner / next workflow | Closure requirement |
| --- | --- | --- | --- |
| Decomposition truth | Candidate applied only after exact owner act | SCOPE_CHANGE | Exact target hash, topology/stable-ID checks, dependency re-extraction, fresh closure audit. |
| Contract truth | Held unless concordance and owner approval are complete | Root/App concordance, then SCOPE_CHANGE | Exact resolved contract plus exact companion-register parity and corpus reconciliation. |
| Carrier SOW/context/lifecycle | Unchanged | WORKING_ITEMS / owning carrier under later authority | Separate sealed carrier acts; no activation inferred from SCA application. |
| Dependencies/DAG | Stale after carrier amendment until rerun | dependency extraction / `AUDIT_DEP_CLOSURE` | Fresh post-application evidence; assessment PASS cannot substitute. |
| Root notice | Draft remains unrouted | HELP_HUMAN / owner | Route only after separately authorized post-application moment. |
| Release lane | Frozen | Ryan Tufts / CHANGE at WP-11 | G6a exact-candidate ruling; D-APP-97/F-APP-2 remain active until then. |

## Four-state handoff

| State | Value | Meaning |
| --- | --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` | Exact Gate-4 ordering, hash identities, checks, reruns, and rollback are drafted. |
| `AuthorityState` | `NO_NEW_AUTHORITY` | No Gate-5 application, pointer move, notice routing, activation, implementation, lifecycle, or release act has occurred. |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` | The two target files, companion register, SOWs, dependencies, register, pointer, code, frontend, Root, and other projects remain unchanged by this drafting phase. |
| `NextGateState` | `OWNER_GATE3_GATE4_APPROVAL_REQUIRED` | Ryan Tufts must approve, revise, or reject the exact Gate-3/Gate-4 package. Contract application also requires resolved Root/App concordance and another exact owner act. |

`ReadyForNextPhase = NO`.
