# App-loop execution return: D-GOV-43 application tranche (2026-09-12)

Bounded TASK return. Worktree `claude/chirality-codex-replatform-3999f1`;
no Git write operations were performed. Write scope honoured:
`projects/chirality-app-dev/execution/**` and
`projects/pec/execution/_Coordination/`. No `docs/`, `frontend/` or
`projects/chirality-app-dev/AGENTS.md` change.

## Files created

- `_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`
- `_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/REVISION_2026-09-12_D-GOV-43_A2.md`
- `_Coordination/NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md` (App loop)
- `projects/pec/execution/_Coordination/NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md` (PEC loop)
- `_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`
- `_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/NATIVE_CHECKLIST.md`
- `_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/R14_TOOL_HOST_PROPOSAL/RETIREMENT_NOTE_2026-09-12.md`
- `_Coordination/AgentRuns/CODEX_MVP_PACKAGING_20260910/SUPERSESSION_NOTE_2026-09-12.md`
- this file

## Files changed

- `_Coordination/_DECISIONS/_REGISTER.md`: D-APP-127 row after D-APP-126.
- `_Coordination/APP_HOLD_REGISTER.csv`: `APP-HOLD-1-INIT-DEL-09-07` row
  removed (retired; header only remains).
- `_Scripts/tests/test_app_hold.py`: `SowInitializationTests` now load the
  historical SOW_INITIALIZATION row from commit
  `e079cbc397e4208c4c82d6a55a6dffacf67165e4` instead of the live register.
- `_ScopeChange/SCA-APP-008_.../{Brief,Contract_Amendments.proposed,Carrier_Map,Handoff_State}.md`:
  revision block after the title; original text preserved.
- `_ScopeChange/_LATEST.md`: D-GOV-43 application paragraph; active snapshot unchanged.
- `PKG-09/DEL-09-03/_STATUS.md`: V3-02 kept and re-pointed to the short
  procedure; V3-01 gate re-expressed to the extensible representation.
- `PKG-09/DEL-09-04/_STATUS.md`: LaunchAgent owner-act item moved to
  "Retired under D-GOV-43 (preserved, not Remaining)"; V3-01 revised to the
  bundled stock dependency and Runtime service child.
- `PKG-09/DEL-09-05/_STATUS.md`: V3-04 (self-signed drill) removed as a gate;
  V3-02 marked optional; V3-05 and V3-06 re-pointed to the short procedure.
- `PKG-09/DEL-09-06/_STATUS.md`: network, key and renderer checks kept;
  consent postures, Root DEL-02-09/10 gates and the drill dropped; supplier
  containment evidence dropped; A1 re-stage declaration superseded.
- `PKG-09/DEL-09-07/_STATUS.md`: Current State `RETIRED` with rationale.
- `PKG-03/DEL-03-03/_STATUS.md`: "retained and repaired" (A2) transport
  repair and extensible representation.
- `PKG-03/DEL-03-01`, `DEL-03-02`, `DEL-03-04`, `PKG-05/DEL-05-02`,
  `PKG-02/DEL-02-05` `_STATUS.md`: port, lifecycle, event-schema and
  API-key UI clauses revised; history entries added.
- `_Coordination/AgentRuns/APP_V3_TRIAL_COMPLETION_20260910/NEXT_AGENT_HANDOFF.md`:
  appended successor section; earlier text unchanged.
- Supersession or revision headers (text below preserved):
  `NOTICE_CODEX_MVP_PACKAGING_CARRIERS_20260910.md`,
  `NOTICE_2026-09-10_ROOT_APP_METHOD_AND_ENGINE_POLICY.md` (Codex-only
  ruling kept; CI controlled runtime is a test fixture, not an admission),
  `NOTICE_2026-09-07_ROOT_D-GOV-36_*`, `NOTICE_D-GOV-35_*`,
  `NOTICE_2026-09-03_APP_TM-ROOT-122_*`, six `NOTICE_ROOT_RUNTIME_*`.
- `_Coordination/_LATEST.md` and `_COORDINATION.md`: successor pointer entries.

## Superseded parts per D-APP record (as recorded in D-APP-127)

- D-APP-125: item 3 only (isolated per-root homes, per-root consent,
  brokerage custody, switch and revocation contracts). Items 1, 2, 4, 5 stand.
- D-APP-126: all three boundaries on the App path (daemon-owned supplier
  authentication with keyring exception; bootstrap namespace; hosted logout
  fencing and remote-revoke order); D-GOV-36 exception superseded with them.
- D-APP-122: daemon-target and host-gated parts (daemon target of account and
  Settings actions; residency and oMLX statements; Root DEL-02-09 and
  G3/G-CSP/G4 gates; A1 re-stage rule). Presentation loci (PR #745) stand.
- D-APP-100: "packaged daemon" subject, app/CLI/daemon agreement regression
  and packaged-under-isolation proof; the resolution rule carries forward.
- D-APP-88: helper bundle identity, LaunchAgent target, one-daemon and
  RunAtLoad obligations; the 2026-08-13 SIGTERM finding and PR #552 remedy
  stand as history.
- D-APP-107: in whole (SOW_INITIALIZATION admission, Phase 2.2 resumption,
  preflight token); DEL-09-07 retired.

## Validators

- `validate_app_dev_loop_receipts.py`: VALID (targets `loop/LOOP_RECEIPTS.md`, untouched).
- `validate_scope_change_packet.py` on SCA-APP-008: FAIL, pre-existing; the
  packet predates the PKG-00 consumable-packet layout and never had
  `Packet_Contract.md` etc. Not caused by this tranche.
- `validate_path_anchors.py --text`: PASS (4331 surfaces).
- `execution/_Scripts/tests/test_app_hold.py`: 39 passed after the test fix
  (11 `SowInitializationTests` failed against the retired live row before it).
- `app_hold.py check --operation reliance --target DEL-09-04`: ALLOW.

## Judgment calls

1. APP-HOLD-1 retirement by row removal: `app_hold.py` accepts no `RETIRED`
   status and the CSV has no rationale column; removal is the loop's own
   precedent (D-APP-107 retired the D-APP-104 row). Rationale lives in
   D-APP-127 and DEL-09-07 `_STATUS.md`.
2. The hold tests were adjusted rather than deleted so the retained tool
   logic keeps regression coverage from historical bytes.
3. Deliverable Remaining items were revised in place (gate, description,
   Depends, Return, Removed-when) with a dated History entry naming the prior
   gate; History entries were not rewritten. The " — " item separator and
   DEL-09-07's "date — event" history form follow each file's convention.
4. DEL-09-03 V3-01 and the A1 re-stage declarations were re-expressed
   although IMPACT.md names only V3-02; both were architecture-bound gates
   that could never clear.
5. SCA-APP-008 has no prior revision convention; a revision note file plus
   four short in-file blocks was chosen over editing the packet body.
6. `_COORDINATION.md` is a ruled-record pointer surface; one pointer line
   was added under "Pointers" and no status was accumulated.
7. Out of this write scope and flagged for follow-up: the "Shared Runtime
   Boundary" and D-APP-107 preflight paragraphs of
   `projects/chirality-app-dev/AGENTS.md`; `docs/harness/reliance_boundary_register.md`;
   `docs/RELEASE_QUALITY_GATES.md`; the corpus-hashed App docs;
   `frontend/docs/harness/*`; the `desktop:dist` supply-model script chain
   in `frontend/package.json` (PACKAGING_PROCEDURE.md names it as the
   current entry pending re-authoring).
8. External state observed and left untouched: another session modified
   every deliverable's `_REFERENCES.md` and
   `_Reconciliation/References/AUTHORITY_CORPUS.json` (corpus re-hash), the
   Root `docs/` files and `RUN_LOG.md` plus `tranche/RUNTIME_RETURN.md` in
   this run directory.
