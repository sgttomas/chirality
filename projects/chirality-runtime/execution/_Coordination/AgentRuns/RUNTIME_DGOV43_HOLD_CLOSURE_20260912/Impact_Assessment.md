# Impact assessment

Authority: D-GOV-43 item 11 (bounded coordinated authority) with the A2
supplement; family dispositions per the proposal packet's `IMPACT.md`
"Purpose test by family" and its Runtime table.

| Action | Surface | Classification | Result |
|---|---|---|---|
| Close nine held bindings | `_Decomposition/HOLD_SUCCESSOR_MAP.csv` (`CurrentDisposition`, `ReleasingEvidence`, `State`) | DIRECT_EDIT | Nine rows `CLOSED_D-GOV-43_SCA-004`; Tier-0 row unchanged (R16-B) |
| Retire six carriers | `PKG-02/1_Working/DEL-02-07` to `DEL-02-12` `_STATUS.md` | HISTORY_ENTRY | Retired in place; lifecycle state stays `INITIALIZED` (the loop vocabulary has no retirement state); executed content untouched |
| Revise one carrier | `DEL-02-06/_STATUS.md` history and the revision notes below | HISTORY_ENTRY | `ScopeOfWork.md` bytes unchanged (Root-pinned effective state); the revision is recorded here |
| Supersede readiness record | `_Decomposition/GATE_READINESS.md` | DIRECT_EDIT | Supersession note; table preserved |
| Revise product charter reading | `PRD_REVISION.md` (this packet), `docs/PRD_AUTHORITY.md` | RECORD | `docs/PRD.md` bytes unchanged (Root-pinned); revision recorded in this packet; two loop-owned hashes re-issued once |
| Supersede coordination entries | `_Coordination/HANDOFF_STATE.md`, `MIGRATION_ACCEPTANCE_2026-09-06.md` | APPEND | Supersession entries; earlier text preserved. `MIGRATION_APPLICATION.md` and `_ScopeChange/_LATEST.md` are Root-pinned and unchanged |
| Registers | `RUNTIME_DELIVERABLE_REGISTER.csv`, `RUNTIME_SCOPE_LEDGER.csv`, `RUNTIME_OBJECTIVE_REGISTER.csv`, `SOURCE_SCOPE_REQUIREMENTS/`, DECOMP | NO_CHANGE | Frozen Gate3 basis; retirement is carried by `_STATUS.md` and this packet |
| Historical runs | `_Coordination/AgentRuns/RUNTIME_*` | NO_CHANGE | History |

No new register, hash table or acceptance programme is built. SOW-104, the
four objectives, `root-runtime-1` epoch 1 as history, and every executed
record are conserved.

## DEL-02-06 carrier revision notes (recorded here; `ScopeOfWork.md` unchanged)

Fan-in paragraph: DEL-02-07 through DEL-02-12 are retired under D-GOV-43
items 7 and 11 (A2 supplement); their six fan-in inputs no longer gate this
carrier. The nine held bindings are closed by this packet, not released by
evidence. The carrier's remaining stewardship is the application-owned
Runtime service and the lockfile-pinned stock Codex dependency; release
readiness is established by ordinary checks and the three retained human
decisions.

REQ-010: the `HOST-P1` lease, the atomic supplier snapshot with opaque
account and workspace identifiers, and the capability or version-mismatch
refusal are superseded. The stock Codex version is pinned by the package
manifest and lockfile and updated as an ordinary dependency update with
re-validation; upstream drift is not a stop condition. Account identity
comes from Codex's own account methods within the App's effective home. The
fail-closed precondition posture otherwise stands, read against the
application-owned service.

REQ-041: the daemon-owned trusted supplier authentication process, exact
supplier qualification and the D-GOV-36 custody exception are superseded on
the App path. Sign-in and sign-out use Codex's own account methods inside
the Chirality effective home; credentials are custodied by Codex and never
read, copied or relayed by the Runtime. DEL-02-09 is retired; the separation
purpose is verified by the S-8 check.
