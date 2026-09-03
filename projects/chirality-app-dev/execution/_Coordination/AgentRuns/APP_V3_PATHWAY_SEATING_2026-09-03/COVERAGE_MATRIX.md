# COVERAGE MATRIX — every proposed App `Remaining` item is contained by its accepted decomposition row and (after re-basis) its Scope of Work; every plan-only row is non-selectable

**RunID:** `APP_V3_PATHWAY_SEATING_2026-09-03` · **Node:** N0/N4 · **Decomposition:** `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` at `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f` (SHA-256 `932b890e4de38c0fc59c2bcf4830be9d436c74aeac6b2535a7d4f5185168716f`)

Containment rule applied: an item is seated only when the applied row's
Description, Principal outputs, or Notes cell states the obligation; after
re-basis every carrier `ScopeOfWork.md` pins that commit, and the four
carriers whose rows changed at Gate 5 carry the row text verbatim as
`CLM-0nn` with `OUT-002`/`REQ-*`/`AC-002`/`VER-002` restating it and nothing
more. Where containment failed the obligation is in `MAPPING.md` §D and no
item exists.

## Part 1 — item containment

| Item | State after merge | Row (line) clause relied on | SOW trace | Contained |
|---|---|---|---|---|
| DEL-01-01-V3-01 | `SELECTABLE` | L284: "Keep PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and active decomposition mutually consistent while preserving human authority …"; outputs "Governance consistency notes; … acceptance checklist" | OUT-001, AC-001, VER-001 | yes |
| DEL-02-02-V3-01 | `SELECTABLE` | L294: "present explicitly recorded plans/tasks and agent/session selections with source, authority class, responsible reference, currency, and evidence"; outputs "Work/Agents coordination presentation; provenance labels; stale/empty-state … tests"; Notes: DEL-08-05 retains child records | OUT-001, AC-001, VER-001 | yes (role-entry state and its labels are authority-class/provenance labels on agent/session selections; fixtures only) |
| DEL-02-02-V3-02 | `NOT_SELECTABLE_UNTIL` | same clauses, live path | OUT-001 | yes |
| DEL-02-05-V3-01 | `SELECTABLE` | L297: "distinguishing `missing`, `storageUnavailable`, `decryptFailed`, and `available`"; outputs "typed storage/runtime error display" | OUT-002, REQ-002, AC-002, VER-002 | yes |
| DEL-02-05-V3-02 | `SELECTABLE` | L297: consent-port consumption, per-root login explanation, root-private `CODEX_HOME`, login/logout/account and consent/revocation state, three command-network postures, role entry label, `Opt-in Preview`; outputs "per-root login and command-network consent controls; … consent/revocation and retry-state tests" | OUT-002, REQ-001/003/004/005 | yes (fixtures behind a fake port; live claims excluded per Notes) |
| DEL-02-05-V3-03 | `NOT_SELECTABLE_UNTIL` | L297 Notes: "Live claims remain gated by the accepted Root/App account/consent contract, G3, G-CSP, and G4" | OUT-002, REQ-001/003/005 | yes |
| DEL-03-01-V3-01 | `NOT_SELECTABLE_UNTIL` | L303: "Verify the App client against Root-owned runtime contracts … and produce conformance evidence without redefining generic runtime semantics" | OUT-001, AC-001, VER-001 | yes |
| DEL-03-03-V3-01 | `NOT_SELECTABLE_UNTIL` | L305: "Keep `/api/harness/*` shapes and browser SSE event names stable while runtime policy moves behind services"; outputs route adapter tests, SSE fixtures | OUT-001, AC-001, VER-001 | yes (resume decision logic excluded → S-3) |
| DEL-04-05-V3-01 | `SELECTABLE` | L316: "Preserve App credential entry/status and packaged-daemon `safeStorage` boundary participation … without creating a second credential owner"; outputs "packaged-daemon safeStorage conformance" | OUT-001, AC-001, VER-001; RQ-002/003/004/012 | yes |
| DEL-04-05-V3-02 | `NOT_SELECTABLE_UNTIL` | L316: "verify ruled provider/network behavior and redacted client handoff, and prevent unauthorized expansion" | OUT-001; RQ-008/009/010/014; CONTRACT K-NET-1/K-KEY-1 | yes (OAuth/device-code/keyring semantics excluded → S-5) |
| DEL-05-01-V3-01 | `SELECTABLE` | L322: "lazy non-destructive access to and migration of legacy project-local session records while preserving list, resume, and delete behavior"; outputs "legacy-read/migration fixtures" | OUT-001; R003/R004/R010/R015 | yes |
| DEL-05-01-V3-02 | `NOT_SELECTABLE_UNTIL` | L322: "Maintain App-client compatibility for daemon-centralized sessions"; Notes: "daemon sessions remain Root-owned" | OUT-001; R003/R004/R011/R012 | yes (consent/root-home/account-change migration excluded → S-4) |
| DEL-05-02-V3-01 | `NOT_SELECTABLE_UNTIL` | L323: "Consume Root-owned daemon `HarnessEvent` records for App audit/replay surfaces and verify accepted-turn and terminal-event persistence" | OUT-001; RQ-007/008/009/013/015 | yes |
| DEL-05-03-V3-01 | `NOT_SELECTABLE_UNTIL` | L324: "verify that Root-runtime operational records exclude credentials and secrets" | OUT-001; R10/R11/R13 | yes |
| DEL-05-04-V3-01 | `NOT_SELECTABLE_UNTIL` | L325: "live versus replayed state and primary versus observational interaction authority remain explicit"; "selected-session read-only replay lens" | OUT-001; REQ-014/016/018/019 | yes |
| DEL-08-04-V3-01 | `NOT_SELECTABLE_UNTIL` | L357 (entire amended row) | OUT-002, REQ-001..005 | yes |
| DEL-08-05-V3-01 | `NOT_SELECTABLE_UNTIL` | L358 (entire amended row) | OUT-002, REQ-001..004 | yes |
| DEL-09-01-V3-01 | `NOT_SELECTABLE_UNTIL` | L364: "Preserve baseline harness validation, current local checks, and stable premerge summary behavior" | OUT-001; REQ-004/006/008 | yes |
| DEL-09-02-V3-01 | `NOT_SELECTABLE_UNTIL` | L365: "Add runtime validation IDs for provider-adapter conformance, first-adapter mapper, event log, … and subagents" | OUT-001; RQ-003/004/011/012/014 | yes |
| DEL-09-03-V3-01 | `NOT_SELECTABLE_UNTIL` | L366: "focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions"; Notes: "bounded to named behaviors" | OUT-001; REQ-002/004/005/009/011 | yes (other test families excluded; carried by owning carriers) |
| DEL-09-03-V3-02 | `NOT_SELECTABLE_UNTIL` | L366 same; evidence rerun of the named groups | OUT-001; REQ-012 | yes |
| DEL-09-04-V3-01 | `NOT_SELECTABLE_UNTIL` | L367: "Produce the macOS arm64 unsigned DMG and prove required instruction-root assets plus SDK packaging posture are valid"; Notes: one release target | OUT-001; REQ-001/002/005/006/008/010 | yes (installer/IPC excluded → S-2) |
| DEL-09-05-V3-01 | `SELECTABLE` | L368: "WP-09 may author and review the exact signing, nested-signing-order, fuses/entitlements, notarization/stapling/Gatekeeper, recovery/rollback, version-identity, custody, GitHub-prerelease, and download-backcheck runbook"; outputs "WP-09 reviewed preparation/release runbook candidate; exact-candidate identity and custody checklist" | OUT-002, REQ-001..004 | yes |
| DEL-09-05-V3-02 | `SELECTABLE` | L368: "Maintain CI premerge and stable artifact verification"; outputs "CI workflow and stable artifact evidence; exact-candidate identity and custody checklist" | OUT-002, REQ-001 | yes (SBOM/notices are artifact-identity evidence; workflow wiring excluded → S-6) |
| DEL-09-05-V3-03 | `SELECTABLE` | L368: "version-identity" runbook content; "exact-candidate identity" checklist | OUT-002, REQ-002 | yes (product application waits for G5) |
| DEL-09-05-V3-04 | `NOT_SELECTABLE_UNTIL` | L368: "recovery/rollback … custody" | OUT-002, REQ-002 | yes |
| DEL-09-05-V3-05 | `NOT_SELECTABLE_UNTIL` | L368: "WP-11 may execute release acts only after Ryan Tufts names and rules the exact candidate at G6a"; outputs "separately authorized WP-11 owner/CHANGE execution record" | OUT-002, REQ-003 | yes (owner/CHANGE acts only) |
| DEL-09-06-V3-01 | `SELECTABLE` | L369: "Verify renderer allowlist, API key redaction/storage …"; outputs "Security tests; … key storage checks"; L297 Notes: "DEL-09-06 retains server-side attachment, network, key, credential-IPC, and renderer security validation" | OUT-001; REQ-002/003/005/006/014/015 | yes |
| DEL-09-06-V3-02 | `NOT_SELECTABLE_UNTIL` | L369: "current provider endpoint policy, no unauthorized provider/network expansion" | OUT-001; REQ-004/005/007 | yes |
| DEL-09-06-V3-03 | `NOT_SELECTABLE_UNTIL` | L369: "API key redaction/storage" checks under identity transition; "Security tests" | OUT-001; REQ-002/003/015 | yes |

Totals: thirty items on eighteen carriers; ten `SELECTABLE`
(DEL-01-01-V3-01, DEL-02-02-V3-01, DEL-02-05-V3-01, DEL-02-05-V3-02,
DEL-04-05-V3-01, DEL-05-01-V3-01, DEL-09-05-V3-01, DEL-09-05-V3-02,
DEL-09-05-V3-03, DEL-09-06-V3-01); twenty `NOT_SELECTABLE_UNTIL` a named
Root acceptance, owner act, or gate. DEL-04-01 carries no v3 item (S-1).
Pre-existing `Remaining` items are retained unchanged (DEL-03-01 D-APP-89
packet, DEL-08-04 D-APP-103 packet, DEL-09-04 owner daemon-deployment act,
DEL-02-02 D-APP-88 rerun trigger, DEL-05-04 and DEL-09-06 "none" notes).

## Part 2 — plan-only rows are non-selectable

Every WP-00..WP-11 row, every gate, and every AT-001..AT-058 row in
`MAPPING.md` resolves to one of: an App deliverable-local item (selectable
only through that item's own state), a Root carrier (`ROOT_OWNED`; parked in
App as `NOT_SELECTABLE_UNTIL` a routed notice), an owner act (`HELD`), or
`SCOPE_AMENDMENT_REQUIRED` (unseated). No plan row is selectable from the
plan; the successor workplan keeps `plans/**` non-selectable (F-APP-5) and
cites the pinned HTML for completion meaning only.

## Part 3 — nothing lifted

- Lifecycle: every carrier `Current State`, `Checking Approval SHA`,
  `Authorization Basis`, and `Directive` line is byte-identical to the basis
  (proved in `VALIDATION_EVIDENCE.md`).
- Implementation act, host mutation, signing, notarization, release,
  publication, reliance: no product, runtime, `frontend/**`, workflow,
  register, decision, or Root byte changed (see `git diff --stat` in
  `VALIDATION_EVIDENCE.md`).
- Held bindings: the ten DEL-02-06 bindings, TM-ROOT-106/122, TM-APP-030,
  D-APP-97/F-APP-2, G1, G6a remain exactly as on the basis; this candidate
  cites them only.
- Root surfaces: none written; Root notices consumed as read-only context.
- Concurrent E2 tranche (PR #680): disjoint write set; its Receipt 204 and
  this Receipt 205 share `Parent-Receipt: Receipt-203` under ledger rule 7.
