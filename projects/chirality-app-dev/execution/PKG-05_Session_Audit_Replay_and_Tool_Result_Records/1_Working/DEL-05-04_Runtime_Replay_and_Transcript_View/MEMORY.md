# MEMORY - DEL-05-04

## Decisions And Evidence

- 2026-08-17 - Accepted the dedicated canonical replay/restart integration
  proof at candidate blob `310e0c9539dbac6af89159bd312b2a93a082689b`.
  A real daemon, authenticated Desktop compatibility port, and Root CLI
  `runCli session replay --json` façade lazily migrate legacy manager/child
  sessions without changing legacy bytes; both decoded surfaces then replay
  structurally equal parsed canonical records before and
  after a fresh service restart. Exact recorded role, parent session, ordered
  events, and `pi` / `omlx` / `recorded-model` attribution survive, and the
  Woven hierarchy remains manager-rooted even with child-first input. Focused
  Vitest and worktree-correct typecheck passed. Integrated review corrected an
  evidence-wording overclaim: the assertions establish structural/value
  equality of parsed replay objects, while byte identity is proven only for the
  preserved legacy source files. A second integrated finding that the original
  fixture used only a second `RuntimeClient` was remediated by exercising and
  decoding captured output from the actual Root `runCli` boundary. Fresh
  review additionally required raw `Buffer` capture/comparison to support
  legacy-byte preservation; that correction and backcheck passed. No App
  product-source defect was exposed. Evidence:
  `_run_records/CANONICAL_REPLAY_RESTART_2026-08-17.md`. Rerun on Root daemon,
  client, session-migration, or replay contract changes, or App runtime-client
  or Woven hierarchy changes. Lifecycle remains `IN_PROGRESS`.
- 2026-08-03 - D-APP-86 Option A derivative evidence proves the exact
  real-daemon transcript-item-rendering residual for one admitted
  `WORKING_ITEMS` / `agent1` session: two canonical events produced one
  read-only replay transcript item and terminal event
  `a26a661d-721e-491d-ab9f-66b2aa3b2dd0`. No parent/child attribution existed
  and none is inferred. The evidence pointer is
  `_run_records/R3_DAPP86_REAL_DAEMON_REPLAY_2026-08-03.md`; lifecycle remains
  `IN_PROGRESS`, and the separate Desktop/CLI restart-and-migration residual
  remains gated. A later accepted D-APP-88 distinct-helper implementation is a
  non-blocking parity-rerun trigger.
- 2026-07-12 - D-APP-56 R5 P44 docs executed UPD-098: the normative transcript-replay and types pointers now name the harness-contract package; dated assessment evidence received a forward relocation annotation. No lifecycle transition occurred.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-21 - ADQ-09 implemented the runtime transcript projection/view over canonical replay events: `deriveTranscriptView` in `frontend/src/lib/harness/transcript-replay.ts`, replay API enrichment in `frontend/src/app/api/harness/session/[id]/events/route.ts`, sidebar Transcript tab/component, read-time replay redaction for imported JSONL, and Section 9 `section9.sdk_session_link_resume` coverage. Evidence record: `execution/PKG-05_Session_Audit_Replay_and_Tool_Result_Records/1_Working/Evidence_ADQ-09_Runtime_Transcript_View.md`.
- 2026-09-04 - SCA-APP-010 seating, outside the thirteen carriers (D-APP-108): Remaining items DEL-05-04-V3-02; read `_STATUS.md` with this file before any write; the applied decomposition row L339 (unchanged by SCA-APP-010) states the responsibility; this carrier was seated only and not aligned in this pass, so `ScopeOfWork.md` keeps its earlier pin and carries no SCA-APP-010 section; nothing here is authority. No lifecycle, Checking Approval SHA, dependency, product, or release change.
