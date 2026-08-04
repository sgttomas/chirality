# Launch brief — SCA-003 S3 post-application AUDIT_DECOMP

- Parent: Root `SCOPE_CHANGE`, SCA-003, under HELP_HUMAN run
  `ROOT_FOUR_LANES_2026-08-02`, node `S3`.
- Agent role/type: `AUDIT_DECOMP`, Agent 2. Load
  `agents/AGENT_AUDIT_DECOMP.md` in full before acting. Do not delegate.
- Objective: perform a fresh read-only post-application audit of the live Root
  SOFTWARE decomposition and determine whether the prior current-state
  authority-consistency blocker is closed by the exact S3 application.
- Frozen post-application identities:
  - live PRD SHA-256
    `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4`;
  - live decomposition SHA-256
    `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c`;
  - scope ledger SHA-256
    `3deed192a6f760708f552891b74285f0157e66a9f86e25a1b3cecebf0baf59c2`;
  - deliverable register SHA-256
    `a29759be51aa749ebad22fd3f4d08a1c12ef8f477ae95b846cfc880cc2241395`;
  - preserved `_ScopeChange/_LATEST.md` SHA-256
    `b2849c6ee9466692e6f1f8b97a32391145093654e510b9a3c5f08fcd7dfc80a1`.
- Decomposition variant: `SOFTWARE`.
- Context root: `execution/`.
- Decomposition path:
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`.
- Scope: recheck the four original carriers (`DEL-02-04`, `DEL-03-01`,
  `DEL-02-06`, `DEL-06-04`) and their PKG-02/03/06 full-package referential
  context, plus the current PRD/decomposition/SCA-002 pointer and acceptance
  consistency required to disposition prior blocker `COV-001`.
- Required freshness rule: read and hash the current live files. Do not copy,
  restate, or treat the pre-application
  `Evidence/AUDIT_DECOMP/RETURN.md` as the new result. It may be read only as
  the prior finding to backcheck.
- Required authority-state check: verify that the live decomposition now says
  revision 1.2 is the accepted current basis, cites the exact SCA-002
  acceptance/application lineage, pins REF-001 to the live PRD SHA, preserves
  DEC-023 as proposal history, adds DEC-024 as the current disposition, and
  remains consistent with the unchanged SCA-002 pointer/application evidence.
- Allowed reads: Root decomposition and companion registers; live Root PRD;
  SCA-002/SCA-003 snapshots and pointer; affected deliverable contexts,
  statuses, sibling memory when required, and ScopeOfWork files.
- Allowed writes: only
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/Evidence/AUDIT_DECOMP_POST_APPLY/`.
  Do not modify live PRD/decomposition, companion registers, `_LATEST.md`,
  deliverable files, Task Management, project-loop surfaces, runtime,
  lifecycle/release/reliance, or Git.
- Required outputs: a fresh `RETURN.md` with verdict, applied-state input
  hashes, structural coverage, authority-state consistency, explicit
  disposition of prior `COV-001`, severity counts, closure-readiness verdict,
  and no-write attestation; any supporting structured evidence remains in the
  same folder.
- Acceptance checks: exact live hashes reproduced; structural and
  authority-state results distinguished; every finding cites current evidence;
  prior blocker explicitly `CLOSED` or remains open with exact reason; no
  out-of-scope write; return is independently hashable.
