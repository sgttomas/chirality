# Launch brief — SCA-003 Gate-1 decomposition baseline

- Parent: Root `SCOPE_CHANGE`, SCA-003, under HELP_HUMAN run
  `ROOT_FOUR_LANES_2026-08-02`, node `S1`.
- Agent role/type: `AUDIT_DECOMP`, Agent 2. Load
  `agents/AGENT_AUDIT_DECOMP.md` in full before acting. Do not delegate.
- Objective: produce the read-only pre-change decomposition audit required by
  `AGENT_SCOPE_CHANGE` Gate 1 for the current Root SOFTWARE decomposition,
  scoped to the affected carriers and their full-package integrity context.
- Frozen audit basis: repository HEAD
  `97678a841ef58345c73d3470ed8de57c9b1405d2`; authoritative decomposition
  surface SHA-256
  `6f43f3fbc25e0663697464a7a20f3b1bac4b731b01efbe473642e238b93a4d49`.
- Decomposition variant: `SOFTWARE`.
- Context root: `execution/`.
- Decomposition path:
  `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`.
- Scope: `PKG-02`, `PKG-03`, and the downward-variant relation in `PKG-06`;
  specifically `DEL-02-04`, `DEL-03-01`, `DEL-02-06`, and `DEL-06-04`, while
  checking full authoritative-package referential and coverage integrity where
  the role requires it.
- Required discrepancy check: independently assess the current-state mismatch
  between the live decomposition's candidate/not-accepted labels and the
  accepted/applied SCA-002 state recorded in
  `execution/_ScopeChange/SCA-002_2026-07-29_0800/Decision_Log.md`,
  `Handoff_State.md`, and `execution/_ScopeChange/_LATEST.md`. Treat the parent
  relay as an observation, not authority.
- Allowed reads: Root decomposition and companion registers; the SCA-002
  snapshot and pointer; `docs/PRD_ROOT.md`; affected deliverable contexts,
  statuses, and `ScopeOfWork.md` files. If reading DEL-02-06 `_STATUS.md`, also
  read sibling `_MEMORY.md` and treat it as non-authoritative context only.
- Allowed writes: only
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/Evidence/AUDIT_DECOMP/`.
  Do not modify `_LATEST.md`, live decomposition, companion registers,
  deliverable files, Task Management registers, App/Piping surfaces, Git state,
  or any path outside that audit evidence folder.
- Required outputs: `RETURN.md` with verdict, coverage summary, evidence-linked
  findings, exact blocker severity, and SHA-256 identities; any structured
  findings/coverage files required by the role, written in the same evidence
  folder.
- Acceptance checks: no out-of-scope write; every finding cites exact current
  evidence; the candidate/accepted contradiction receives an explicit verdict;
  report distinguishes structural coverage from authority-state consistency.
