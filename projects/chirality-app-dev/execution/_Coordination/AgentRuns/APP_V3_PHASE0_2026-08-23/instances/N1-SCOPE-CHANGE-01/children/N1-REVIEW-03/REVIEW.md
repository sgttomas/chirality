# N1 Final Fresh Independent Review 03 — SCA-APP-008

- `Verdict`: `RETURN_FOR_REPAIR`
- `Basis`: `3af765222bbd4f43a52dcbe17bd151c13942e5ac`
- `Subject`: `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/**`
- `ReviewType`: final fresh independent bounded review after handoff finalization
- `CandidateManifestDigest`: SHA-256 `bdd9eb71bfbf95d5bb496d4d90881a2f719e3a24e851292e5c71fb1b440d1798` over the sorted eleven-line per-file SHA-256 manifest
- `CandidateModifiedByReviewer`: `NO`

## Decision

Gates 1–4 and 7 pass. Gate 5 fails because the human-readable DAG depicts one solid proposed gating edge that does not exist in the authoritative `WORK_GRAPH.json`. Gate 6 consequently fails because the finalized handoff's statement that no finding remains open is no longer true. The package therefore requires one bounded repair and another fresh review before HELP_HUMAN fan-in.

## Finding N1-RF-002

- `Severity`: `MAJOR` — blocks internal agreement between the two required DAG artifacts and the final handoff.
- `Gates`: 5 (DAG closure) and, consequentially, 6 (handoff truth).
- `Origin`: independent comparison of every depicted solid/dashed relationship in `DAG.md` with the 32 authoritative edges in `WORK_GRAPH.json`.
- `Locations`:
  - `DAG.md:20-24`
  - `Handoff_State.md:26,53,77-84`
- `Observed`: `DAG.md:20-24` draws a vertical solid arrow from `DEL-02-05` to `DEL-02-02`. `DAG.md:9` defines every solid edge as proposed gating order, while `DAG.md:35` says `WORK_GRAPH.json` is authoritative. The JSON contains no `DEL-02-05` → `DEL-02-02` edge among its 32 edges. Its only edge involving `DEL-02-02` is `E-023`, `DEL-02-02` → `DEL-09-03`. The visual therefore invents an undeclared gating relationship. Once this review records the issue, `Handoff_State.md:26` is also stale where it says no finding remains open, and its review-history section does not yet represent the final repair/re-review state.
- `RequiredCorrection`: make the `DAG.md` drawing match `WORK_GRAPH.json` without silently changing the assessed graph. The minimal correction is to remove the visual `DEL-02-05` → `DEL-02-02` arrow while retaining the declared `DEL-02-02` → `DEL-09-03` edge. If the parent instead proposes a new graph edge, it must update the JSON, DAG prose, SCC/closure evidence, and rerun the named dependency audit. After the chosen repair, refresh `Handoff_State.md` so its audit/review state and exact review hashes describe the final candidate truthfully.
- `ReReview`: required. Dispatch a fresh reviewer after repair; this reviewer must not review the repaired candidate.

## Gate results

| Gate | Result | Independent evidence |
| --- | --- | --- |
| 1. Authority/basis | PASS | `HEAD` and `origin/main` are exact basis `3af765222bbd4f43a52dcbe17bd151c13942e5ac`; PR #639 merge `e8a6ac7bef255698bb9c1e98bcb52c79645c2abc`, D-GOV-35 effective commit `8deca1489a3e5921288f71d4960d555e183a6f3f`, and Root SCA-004 Gate-5 merge `6d4438d8d3a580b65d6d50ad497dadfe07f177f2` are ancestors. Steer/G0/A1 hashes reproduce exactly as `fef516fd…`, `86b9877c…`, and `f9b02806…`; the plan, notice, register, decomposition, contract, pointer, and frontend basis identities also reproduce. The package remains assessment-only and `AWAITING_OWNER_ACCEPTANCE`. |
| 2. Artifact completeness | PASS | All eleven candidate files are present, including the three-file AUDIT_DEP_CLOSURE evidence set, four-state handoff, and `DRAFT_UNROUTED` reciprocal Root notice. |
| 3. Carrier/G0/A1 seating | PASS | WP-00 through WP-11 and every directed carrier/amendment are seated: DEL-04-01 probe; DEL-08-04 managed carrier; prospective/tranche-scoped D-APP-74 treatment; exact one-sentence D-APP-103 `defers` disposition; G0 A3/A4/A5/A7/A8/A9/B1/B2/B4/D1/D2/D3; six credential sender checks; runtime-control two-job installer; migration/resume continuity; account/consent UX; RQG section 13; frozen `electronDist`; macOS-arm64-only scope; WP-09/WP-11 separation; and the A1 re-stage rule. |
| 4. Proposed contract text | PASS | `Contract_Amendments.proposed.md` contains proposed-not-applied K-CONTROL-1, K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3/4/6, K-CONSENT-1, and K-UNTYPED-1 rows. Root ownership, concordance, human holds, D-APP-97/F-APP-2, and non-release/non-implementation posture remain explicit. |
| 5. DAG/audit closure | FAIL | Independent JSON/Tarjan checks still pass: 21 unique nodes, 19 live App paths, two Root notice-edge nodes, 32 unique closed edges, WP-00…WP-11, three exact SCCs, and non-gating E-018/E-020/E-032. Audit outputs remain internally consistent. However, `DAG.md` depicts the undeclared solid `DEL-02-05` → `DEL-02-02` edge described in N1-RF-002. |
| 6. Four-state handoff | FAIL | Authority, truth, next-gate, rerun, and blocker fields are otherwise correct. Audit and REVIEW-02 hashes reproduce exactly. N1-RF-002 makes the current `no finding remains open` statement and final-review history stale until repair and a fresh PASS. |
| 7. Containment/hygiene | PASS | `_ScopeChange/_LATEST.md` remains SHA-256 `a0298fdc…`; frontend tree remains `74e3dbe8…`; no N1 write is present under frontend, App docs, runtime, Root docs, plans, registers, or any undeclared candidate descendant. Both candidate JSON files parse, candidate whitespace passes, all files end in one newline-compatible final LF, no symlink exists, and `git diff --check` emits no finding. Concurrent N2/N3 paths were not attributed to N1. |

## Finalized handoff and review-hash reproduction

| Handoff citation | Recorded | Reproduced | Result |
| --- | --- | --- | --- |
| `Audit/AUDIT_DEP_CLOSURE_RETURN.md` | `7ddc86e042547c90c7c9b9bd71fe5c2e842cbb885401d6aac2a749f8edc08d6e` | same | PASS |
| `Audit/closure_summary.json` | `30dd016f9e358b0989cd14cc46ea5d0ebe33f8ba1ae14272378bbf98b611bce9` | same | PASS |
| `Audit/Dependency_Closure_IssueLog.csv` | `deca04cd9717b8685c81cd4027638523d9193c02b10e5ffcfce189ca9dc27dcb` | same | PASS |
| `children/N1-REVIEW-02/REVIEW.md` | `449c139a418c0b7f19e1b34de01c6d7b62679f6e15d76e764dac85587ddb4893` | same | PASS |
| `children/N1-REVIEW-02/RETURN.md` | `8e0847ea23bb1e0a939bccfceb6d22c3545206bfe3bf5612ca1b0866f37200b0` | same | PASS |

The hashes are byte-accurate. They establish the prior audit/review identities but cannot erase the independently observed N1-RF-002 in the final candidate.

## Commands and checks used

1. Read the sealed REVIEW-03 brief, the seven-gate REVIEW-01 brief, every candidate file, the audit child return, and both prior review cycles.
2. Reproduced Git basis/ancestry, frontend-tree identity, and SHA-256 identities for the owner instruments, plan, notice, register, decomposition, contract, active pointer, candidate files, audit files, and REVIEW-02 files.
3. Reproduced cited basis blobs and line ranges for D-APP-74, `subagent-governance.ts`, `managed-delegation.ts`, six credential IPC registrations, `isAuthorizedSender`, RQG section 13, and frozen Electron supply scripts.
4. Parsed both JSON files and independently checked node/edge uniqueness, basis-tree App-path resolution, endpoint closure, Tarjan SCCs, non-gating feedback edges, and WP coverage.
5. Compared the `DAG.md` diagram and prose to the authoritative JSON edge set, identifying N1-RF-002.
6. Ran the candidate-scoped whitespace validator, direct trailing-whitespace/final-newline/symlink checks, JSON parsing, `git diff --check`, candidate manifest hashing, `_LATEST.md` hashing, frontend-tree verification, forbidden-surface identity checks, and N1 control-root inventory.

## Non-modification confirmation

This reviewer did not modify the SCA candidate, audit evidence, parent or sibling run artifacts, other nodes, Git state, pointers, decomposition, contract, deliverables, docs, frontend, runtime, plans, registers, lifecycle, or Root surfaces. It wrote only `REVIEW.md` and `RETURN.md` in the sealed N1-REVIEW-03 root.
