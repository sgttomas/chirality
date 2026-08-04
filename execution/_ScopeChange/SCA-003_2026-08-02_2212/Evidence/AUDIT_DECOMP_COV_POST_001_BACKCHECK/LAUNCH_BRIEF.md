# Launch brief — fresh COV-POST-001 applied-state backcheck

- Parent: Root `SCOPE_CHANGE`, SCA-003, run
  `ROOT_FOUR_LANES_2026-08-02`, node `S5`.
- Role: `AUDIT_DECOMP`, Agent 2. Load `agents/AGENT_AUDIT_DECOMP.md` in full;
  do not delegate.
- Objective: freshly read/hash the current applied Root SOFTWARE decomposition
  and independently disposition `COV-POST-001`. Distinguish audit evidence
  from human Gate-1 confirmation or SCA closure.
- Frozen live identities:
  - PRD `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`;
  - decomposition `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`;
  - scope ledger `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`;
  - deliverable register `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`;
  - `_LATEST.md` `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`;
  - S5 applied hashes `33ea624ad3396a15f1f242d0d7cebad8dba9a3e5704046d1a4b7f867723ff3de`;
  - S5 validation `a8bbb5750bbdca7131700aa6c9d92936983f5387038f84cffe5400ab11a85bf8`.
- Required freshness: read current live bytes. The prior post-apply audit return
  SHA-256 `0c49c5e1…630a5` is only the finding to backcheck; do not copy or reuse its
  verdict as the new result.
- Required checks:
  1. reproduce all frozen live hashes;
  2. verify the three corrected current-facing passages state completed exact
     acceptance/application with the cited ruling/applied evidence hashes;
  3. verify those passages refer human confirmation status only to SCA-003
     `Decision_Log.md` and contain no current-facing `pending` or `confirmed`;
  4. explicitly close or retain `COV-POST-001` with exact evidence;
  5. recheck structural coverage for the original four carriers and full
     PKG-02/03/06 referential context;
  6. report severity counts and closure readiness while stating that audit
     PASS is not human confirmation or SCA closure.
- Allowed reads: current Root PRD/decomposition/companion registers,
  SCA-002/SCA-003 evidence and pointer, and original affected-carrier contexts,
  statuses/memory pair where required, and ScopeOfWork files.
- Allowed writes: only
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/Evidence/AUDIT_DECOMP_COV_POST_001_BACKCHECK/`.
- Required output: fresh `RETURN.md`, independently hashable, with verdict,
  current hashes, COV-POST-001 disposition, structural summary, finding counts,
  closure readiness, confirmation boundary, and no-write attestation.
- Prohibited: live PRD/decomposition, companions, `_LATEST.md`, DEL/N0,
  runtime/client/project, lifecycle/release/reliance, Task Management,
  coordination/Git writes, confirmation, or closure.
