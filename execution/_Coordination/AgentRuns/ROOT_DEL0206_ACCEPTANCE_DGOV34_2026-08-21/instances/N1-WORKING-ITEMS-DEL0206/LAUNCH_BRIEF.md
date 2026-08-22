# Launch brief — N1 WORKING_ITEMS DEL-02-06 exact-byte acceptance

RequestedBy: `HELP_HUMAN`

RunID: `ROOT_DEL0206_ACCEPTANCE_DGOV34_2026-08-21`

InstanceID: `N1-WORKING-ITEMS-DEL0206`

Role: `WORKING_ITEMS`

PackageID: `PKG-02`

DeliverableID: `DEL-02-06`

AcceptedBasis: `33e871fc38d8ef4bb51f7c25cdc6ca2e8dcb69e0`

Objective: Execute only the owner-authorized exact-byte acceptance-record activation described in the owner transcript. Create `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005` in the form of `DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003`, update `_STATUS.md` only as authorized, and route the one App carrier notice without touching an App register.

RequiredReads:

- root `AGENTS.md`, `agents/AGENT_WORKING_ITEMS.md`;
- `OWNER_DIRECTION_TRANSCRIPT_2026-08-21.md` and the D1 ruling verbatim;
- DEL-02-06 accepted `ScopeOfWork.md`, `_STATUS.md`, run `DEL-02-06-COMPATIBILITY-COMPLETION-004`, and precedent `DEL-02-06-SEMANTIC-BYTE-ACCEPTANCE-003`;
- App `TM-APP-032` row and applicable notice convention.

AllowedWriteTargets:

- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/**`;
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-08-21_ROOT_DEL0206_COMPATIBILITY_ACCEPTANCE.md`;
- this instance directory.

AcceptanceContract:

- rehash candidate at current basis and require exactly 14,191 bytes / `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`;
- record accountable human, D1 verbatim, transcript SHA-256, candidate path/size/hash, source run, package-manifest SHA `4e6b7062cd4776e7561c0d6a3040342132b1e1641381afe4581219b0bf244e05`;
- member verification manifest, `SNAPSHOT_MANIFEST.sha256`, fresh validation, `HANDOFF_STATE`;
- preserve REM-002/003, every held binding, and `INITIALIZED` unless the accepted Scope of Work explicitly prescribes a package-acceptance transition (cite it if and only if found);
- fresh independent review with repair/re-review until PASS;
- return exact acceptance-record path and SHA-256, changed paths, checks, holds, and blockers.

Exclusions: implementation, cutover, inferred lifecycle change, release, publication, reliance, foreign-loop work, App register write, Git commit/push/PR/merge.
