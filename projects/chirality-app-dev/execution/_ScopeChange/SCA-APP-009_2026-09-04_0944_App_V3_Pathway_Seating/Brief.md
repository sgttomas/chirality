# SCOPE_CHANGE Gate 1 Intake — App S-1..S-7 and Live Nine-Node SCC

**State:** `GATE1_READY_WITH_BASELINE_BLOCKER_FOR_HUMAN_CONFIRMATION`
**Date:** 2026-09-04
**Human initiator:** Ryan Tufts (`ryan@chirality.ai`)
**Authorization:** HELP_HUMAN asked, “Do you authorize SCOPE_CHANGE to assess S-1 through S-7 and the nine-node SCC, returning one amendment package for your later approval without applying any amendment yet?” Ryan Tufts answered, “Yes, so authorized.”
**Authority limit:** assessment and Gate-1 preparation only. No amendment, register edit, project write, implementation, commit, push, or reservation of an amendment ID is authorized.

## Resolved intake

| Field | Resolution |
| --- | --- |
| Basis | `origin/main` `719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` |
| Variant | `SOFTWARE` |
| Context root | `projects/chirality-app-dev/execution` |
| Decomposition | `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| Decomposition SHA-256 | `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f` |
| Companion register | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` |
| Companion SHA-256 | `62c9a318cf673b9b72bf31754aaf7dadb0f2db4b439eb79232c9e8d456d70bb3` |
| Semantic headings | Gate Log line 23; References 37; Intake 83; Vocabulary 116; SSOW 159; Objectives 244; Packages 261; Deliverables 278; Scope Ledger 383; Coverage 470; Decision/Change Log 584 |
| Active SCA pointer | `_ScopeChange/_LATEST.md`, lines 3–6; SHA-256 `12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b` |
| Candidate next App ID | `SCA-APP-009` (derived from the live `SCA-APP-*` directory set; not reserved) |
| Standing plan | `loop/WORKPLAN_2026-09-03_app_dev_loop.md`, selected by committed `LOOP_INIT.md` and read with `git show HEAD:<path>` |

The generic helper `tools/query/scan_next_amendment_id.sh` returns `SCA-001` for this folder because its pattern does not recognize the App-local `SCA-APP-*` namespace. Gate 1 therefore records the helper result as a tooling warning and derives `SCA-APP-009` by an explicit local namespace scan. No directory was created.

## Parsed intent and preliminary classification

The atomic rows are in `PARSED_ACTIONS.csv`. The source of S-1 through S-7 is `execution/_Coordination/AgentRuns/APP_V3_PATHWAY_SEATING_2026-09-03/MAPPING.md:147-157` (mapping SHA-256 `99ba8fb24a40a0eaafc37465a8f5c47b84d57cdc21eac3faa7280ba890b076c8`).

| Action | Gate-1 disposition | Reason |
| --- | --- | --- |
| S-1 | `MODIFY` candidate, DEL-04-01 | App owns a bounded second-adapter probe, while Root retains App Server supply authority. The live row at decomposition line 312 and current ScopeOfWork describe the first Root-runtime/SDK adapter, not the exact App Server supply/protocol/config/role probe. |
| S-2 | `MODIFY_OR_ADD` unresolved | The App-side installer transaction is real App work and is absent from DEL-09-04 line 367. Carrier Map line 29 names DEL-09-04, but the two-job runtime-control transaction is materially different from that deliverable's current DMG/instruction-root artifact kind. Gate 2 must validate whether widening DEL-09-04 preserves deliverable granularity or whether a new deliverable is required. |
| S-3 | `ROOT_OWNED` + `NO_AMENDMENT_CANDIDATE` | Root DEL-02-11 owns restart/fresh-thread policy. DEL-03-03 remains an App compatibility adapter and DEL-05-04 already owns truthful resume/fresh presentation. No accepted Root contract currently justifies adding App policy ownership. |
| S-4a | `MODIFY` candidate, DEL-05-01 | Only the App session-migration backup-before-write and rollback obligation is a candidate. The current row line 322 and ScopeOfWork cover non-destructive session-record conversion and byte-retention provenance, but do not state a rollback transaction. |
| S-4b | `ROOT_OWNED` + `NO_AMENDMENT_CANDIDATE` | Consent, root-home, account-change invalidation, and the resume/fresh decision are Root DEL-02-09/11 semantics. App can consume an accepted contract later; it must not invent it here. |
| S-5 | `ROOT_OWNED` + `NO_AMENDMENT_CANDIDATE` | OAuth/device-code/keyring/root-account semantics remain Root-owned. DEL-04-05 line 316 and its current Remaining item already seat App typed-transport/network-posture conformance without making App a second credential owner. |
| S-6 | `WRITE_SCOPE_ONLY` | DEL-09-05 already owns the CI workflow (`ScopeOfWork.md:109,164,172,261,268`). The missing authority is permission to write repo-root `.github/workflows/**`, not decomposition scope. It requires a separate owner grant/Root-surface tranche and cannot be conferred by an App decomposition amendment. |
| S-7 | `MODIFY` candidate, DEL-02-02 | The role-entry offer and required posture labels on Work/Agents are new App UX beyond line 294's presentation of already-recorded selections. Root still owns role semantics and G-ROLE evidence. |
| SCC-1 | `CYCLE_RESOLUTION_REQUIRED`, separate objective | The live dependency-register graph has one nine-node SCC. It is not the accepted SCA-APP-008 objective graph and must not be silently mapped to its three already-resolved SCCs. |

## Live graph versus accepted objective DAG

The current dependency registers were re-analyzed at the exact basis into `live_graph/`: 51 valid registers, 572 rows, 46 nodes, 99 distinct edges, five isolates, one bidirectional pair, and one nine-node SCC. `LIVE_SCC_INTERNAL_EDGES.csv` records all 15 active register rows that produce the 14 unique internal directed edges. The SCC members are:

`DEL-02-05`, `DEL-03-02`, `DEL-03-03`, `DEL-03-04`, `DEL-04-03`, `DEL-04-05`, `DEL-05-02`, `DEL-05-03`, and `DEL-05-05`.

This is a fresh delta from the immutable SCA-APP-008 Phase-5 audit (564 rows and 98 edges): eight more execution rows and one more distinct edge, while SCC membership, isolates, and the bidirectional pair are unchanged.

The accepted SCA-APP-008 objective-relative graph is a different derivative: `DAG.md:1-46` has 21 nodes and 32 edges. Its accepted sequencing moves are `DECOMPOSE`, `DECOMPOSE`, and `INVERT`; E-018, E-020, and E-032 remain explicit non-gating feedback (`DAG.md:77-106`; `Gate4/GATE4_PROPAGATION_PLAN.md:101-103`). Those accepted moves do not resolve the live register SCC.

For the live register SCC, exhaustive analysis of its 14 unique directed internal edges finds one unique minimum feedback edge: `DEL-04-05 -> DEL-02-05`, evidenced by `DEP-04-05-010` in `DEL-04-05/.../Dependencies.csv:11`. Removing or inverting that edge makes the current nine-node induced graph acyclic. This is diagnostic, not a ruling:

- `CUT DEP-04-05-010` is mechanically minimal but human-gated and cannot be selected at Gate 1.
- `INVERT DEP-04-05-010` is a viable candidate only if semantic review proves the registered direction is wrong; it would align with the existing `DEL-02-05 -> DEL-04-05` edge, but direction may encode a legitimate interface-feedback claim.
- `DECOMPOSE` is the preferred non-destructive investigation: define an execution-sequencing objective and separate contract/interface availability from implementation-complete prerequisites; satisfied and informational interface/constraint facts should remain recorded but need not all be gating edges. This requires a governed dependency-register/schema transaction, not silent filtering.
- `MERGE` all nine deliverables is human-gated, crosses four packages, conflicts with the current package/deliverable discipline, and is not recommended.

## Gate-1 structural recommendation

One assessment envelope is coherent, but one atomic amendment/apply transaction is not. Gate 1 recommends partitioning any later work into independently approved groups:

1. **App decomposition candidate (`SCA-APP-009`):** S-1, S-2 after `MODIFY` versus `ADD` granularity resolution, S-4a, and S-7.
2. **No-amendment boundary dispositions:** S-3, S-4b, and S-5 remain Root-owned; S-6 is a separate owner write-scope/Root-surface authorization.
3. **Dependency-cycle resolution:** separately establish the register graph's objective and select a named move; do not edit the registers until the owner accepts exact cycle semantics and any human-gated move.

This partition preserves stable IDs, avoids turning Root semantics into App obligations, and prevents a write-scope grant from masquerading as decomposition scope.

The required fresh `AUDIT_DECOMP` baseline returned `BLOCKERS` / closure `FAIL`. Its single blocker is that the currently active SCA-APP-008 snapshot root lacks six top-level artifacts required by the current SCOPE_CHANGE snapshot contract: `Propagation_Plan.md`, `Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Post_Change_Coverage.json`, `Decision_Log.md`, and `RUN_SUMMARY.md`. The pointer itself is unique/current, and the closure addendum correctly reconciles dated handoff history. This intake does not rewrite the immutable SCA-APP-008 bytes. If the owner confirms continued work, the next snapshot must use the complete current layout and must not claim closure or move `_LATEST.md` until the blocker is resolved or the owner separately rules its disposition.

The audit also records warnings, not amendment authority: reverse-only `PKG-00` / `DEL-00-01` / `DEL-00-02`; stale `_CONTEXT.md:28` descriptions for DEL-02-05, DEL-08-04, DEL-08-05, and DEL-09-05; stale decomposition summary counts (81 IDs / 48 families) versus the authoritative companion CSV (83 / 50); and conservative folder-local anticipated-artifact matching gaps. See `audit/AUDIT_DECOMP_RETURN.md` and `audit/Decomp_Coverage_Report.md`.

## Human-facing Gate-1 question

**Is this what you intend?**

- **Confirm recommended partition:** proceed to Gate 2 only for an App decomposition candidate covering S-1, S-2 (with carrier granularity resolved first), S-4a, and S-7; preserve the no-amendment/Root-owned and write-scope-only dispositions; assess the register SCC as a separate owner-gated transaction; and carry the active-snapshot blocker as a mandatory pre-closure obligation without rewriting SCA-APP-008.
- **Require one apply transaction:** return to Gate 1 to explain how decomposition changes, Root/no-amendment dispositions, a Root write-scope grant, and dependency-register cycle semantics can lawfully share one atomic transaction.
- **Revise or stop:** provide corrected actions/boundaries; no Gate-2 work begins.

No Gate-2 work is authorized until HELP_HUMAN relays the owner's answer.
