# DEL-06-01 — forward-pass notes (R2, PKG-06)

Ledger: `DEL-06-01_claims.csv` (59 rows, sealed after validation). Basis: frozen tree at `00115c719`.

## 1. Census

- **Indexed units:** 34 (CLM-001..CLM-034). All are covered.
- **Rows:** 59. That is 49 rows for the indexed units (including split sub-rows) plus 10 run-local rows (REGISTER-1..4, STATE-1..3).
- **Split rate:** 4 of 34 units were split (12%).
  - CLM-009 → 15 rows, one per DEL-06-01-REQ-001..015. The index `SubItems` column is empty for this unit because the REQ IDs carry the `DEL-06-01-` prefix, but the rule allows the split and the dispositions differ.
  - CLM-015 → 2 rows: narrative and AC-001.
  - CLM-022 → 2 rows: narrative and VER-001.
  - CLM-034 → 3 rows: narrative, AC-002 and VER-002.

**By ClaimType**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 28 |
| STATE_ASSERTION | 10 |
| CONTEXT_CLAIM | 10 |
| ACCEPTANCE | 7 |
| REGISTER_DEFECT | 4 |

**By Disposition** (all rows, then non-SEE and SEE)

| Disposition | All | Non-SEE | SEE |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 19 | 14 | 5 |
| AUTHORITY_CONFLICT | 12 | 7 | 5 |
| IMPLEMENTED_DIFFERENTLY | 10 | 10 | 0 |
| NOT_AUDITABLE | 5 | 5 | 0 |
| PARTIALLY_IMPLEMENTED | 4 | 4 | 0 |
| ALIGNED | 4 | 4 | 0 |
| REMAINING_STATE_MISMATCH | 3 | 3 | 0 |
| STALE_VERIFICATION | 2 | 2 | 0 |

**SEE rows (10, counted separately per MR-4)**

- CLM-007, CLM-013, CLM-016, CLM-023 and CLM-033 point to CLM-001 (the repeated "REF-006 PRD MATCH" note).
- CLM-009.3 and CLM-009.4 point to CLM-003.
- CLM-009.5, CLM-009.6 and CLM-009.9 point to CLM-004.

**HumanDecisionNeeded:** R4-Q1 on 33 rows; NO on 26. No errata file exists; this is pass 1 only.

## 2. Least-confident rows

- **DEL-06-01#CLM-034.1 (LOW).** Recorded as STALE_SPECIFICATION with CauseTag FACADE_DEPRECATION.
  - The SoW cites `frontend/packages/harness-contract/src/tool-descriptor.ts` as evidence. At the frozen basis that file is a `@deprecated` re-export of `@chirality/runtime-contracts/tool-descriptor`.
  - Alternative reading: a working re-export is still valid evidence, which would make the row ALIGNED at module level.
  - Coordination tools are LEGACY_ONLY, so the ownership mapping may itself be history (R4-Q1).
- **AUTHORITY_CONFLICT versus IMPLEMENTED_DIFFERENTLY (MEDIUM rows CLM-003, CLM-009.3/.4, CLM-024, CLM-025).**
  - Alternative reading: D-GOV-43 item 4 and TYPES §12 `PolicySelection` would be read as fully replacing the overlay model. The rows would then be IMPLEMENTED_DIFFERENTLY with `GOV:` direction.
  - I kept AUTHORITY_CONFLICT for three reasons:
    1. CONTRACT K-PERM-1..6, TYPES §8.1 and SPEC §15.1/§15.2 carry no D-GOV-43 amendment.
    2. D-GOV-43 does not name them.
    3. TYPES itself disagrees internally: §8.1 says `bypass` is never shipped, while §12 lets `permissionMode` map onto a user-chosen `danger-full-access`.
- **CLM-009.11 (ALIGNED, MEDIUM).**
  - Live enforcement comes from the Codex sandbox and approval policy plus Runtime tool filtering.
  - Alternative reading: without a dedicated negative test ("prompt-only permission claims cannot authorize"), the row could be PARTIALLY_IMPLEMENTED on the verification side.

## 3. Register-defect summary

| Key | Defect | Disposition |
|---|---|---|
| REGISTER-1 | `_REFERENCES.md` records CONTRACT, SPEC and PRD as MATCH, but all three recomputed hashes differ (`REFERENCE_HASHES.csv`, Match=NO). All three docs carry D-GOV-43 "Amended" headers. Ten SoW units restate the PRD MATCH (CLM-001 family, CLM-006, CLM-010, CLM-029, CLM-032) and cite this key. | STALE_SPECIFICATION |
| REGISTER-2 | The `_DEPENDENCIES.md` mirror is stale. Its row table shows DEP-06-01-011..013 ACTIVE, while `Dependencies.csv` says RETIRED. Its count table (11 ACTIVE / 3 RETIRED) contradicts its own row table. "Declared Upstream: no accepted dependency edges extracted yet" is also stale. | REMAINING_STATE_MISMATCH |
| REGISTER-3 | `_STATUS.md` shows Last Updated 2026-07-12, but the History has a 2026-07-19 entry. The CHECKING-era Authorization Basis and Checking Approval SHA are still shown after the D-APP-54 rebaseline. | REMAINING_STATE_MISMATCH |
| REGISTER-4 | In `Dependencies.csv`, DEP-06-01-014 targets the legacy `frontend/src/lib/harness/session-events.ts` appendHarnessEvent (LEGACY_ONLY), while live persistence is Runtime `turn-coordinator.ts` persistEvent. DEP-06-01-010 is SATISFIED on the failed MATCH. | STALE_SPECIFICATION |

Other stale items:

- The conflict table (CLM-032) claims "no direct source conflict", which is now false.
- `_CONTEXT.md` has two stale statements: the daemon wording (STATE-1) and the Claude/Anthropic "current path" (STATE-2).
- The empty Remaining section (STATE-3) contrasts with a History line saying surviving items were retained.

## 4. Direction and cause

**Main mechanism: CODEX_SOLE_ENGINE (30 rows).**

- The SoW specifies an SDK-side overlay: `canUseTool`, `bypassPermissions`, five modes and hard-deny precedence. At the frozen basis that overlay exists only in LEGACY_ONLY code:
  - `frontend/src/lib/harness/permission-overlay.ts`;
  - `sdk-options-builder.ts`;
  - `subagent-bridge.ts`;
  - `session-events.ts`.
- Its tests pass in the APP gate transcript.
- The live Codex path works differently:
  - It maps four modes to a fixed Codex `PolicySelection` (`runtime/contracts/src/delegated.ts:320-330`).
  - It has no `dontAsk`: `delegated-runtime.ts:304` rejects it.
  - It ships `bypass` as the ordinary "Full access" composer option (`chat-panel.tsx:133`).
  - It filters application tools by mode, role and method (`runtime-method-service.ts:507-529`).
  - It projects Codex approval server requests as persisted `tool.permission` ask then allow/deny events, answered through `createDelegatedPermissionBroker`.

**Other causes**

- DOC_HYGIENE: 12 rows, the hash and MATCH family.
- PRE_V3_DRIFT: 4 rows, TBD paths never refreshed after implementation, and the SDK Agent bridge disabled on 2026-07-11 while CLM-015 (2026-07-12) still says workspaceWrite allows it.
- A2_TOPOLOGY: 3 rows (daemon wording, DEP-014, conflict table).
- FACADE_DEPRECATION: 1 row.
- Secondary causes (`CAUSE2:`): A2_TOPOLOGY, PRE_V3_DRIFT, NATIVE_DELEGATION, CARRIER_PROPAGATION, DOC_HYGIENE, CODEX_SOLE_ENGINE.

**Direction records used**

- `GOV:D-GOV-43` item 4: approval and sandbox are the user's choice. Its consequence is TYPES §12 `PolicySelection`.
- `GOV:D-APP-127`: App-owned Runtime service.
- `CTX:` the v3 done-declaration candidate DONE-05. It is CONTEXT only.
- D-APP-127_APPLICATION_MAP shows no DEL-06-01 carrier citing D-APP-127 or D-GOV-43.

**Searches behind NONE_FOUND**

- `_REGISTER.md` was searched for `DEL-06-01`, `delegate_agent`, `Agent bridge`, `R4-P33`, `sandbox`, `approval policy`, `permission mode`, `bypass` and `dontAsk`. The only hit was D-APP-84 (Pi sandbox posture, not applicable).
- The done-declaration candidate was searched for permission, overlay and sandbox; that search yielded DONE-05.
- Neither search found any record of the Agent-bridge disabling, the stale TBD paths or the facade deprecation, so those rows carry NONE_FOUND.

**PostReleaseBasis:** NO on all rows.

- Two cited files are touched paths:
  - `codex-supervisor.ts`: `blame -L 718,731` gives 95364569a, 0ed1a1a7f and 2f825f180.
  - `app-owned-composition.ts`: `blame -L 226,226` gives 9eaddb596.
- None of these are the four post-release commits.
- No other cited file appears in `TOUCHED_PATHS.csv`.

## 5. Method friction

- **MR-4 and bundled tables.** CLM-003 (Attributes) and CLM-004 (Conditions) bundle several K-PERM rules that later recur as individual REQs.
  - I made the REQ rows SEE rows to the earlier bundles only where the statement matched (REQ-003/004 → CLM-003; REQ-005/006/009 → CLM-004).
  - CLM-027 and CLM-031 combine several rules, so they got their own rows.
  - Proposal: allow a SEE target to be the more specific later REQ row when the earlier unit is a summary table.
- **SubItems index gap.** REQ IDs with a deliverable prefix (`DEL-06-01-REQ-001`) are not captured in `SubItems`, so V-SUBITEMS does not require the CLM-009 split.
  - Proposal: extend the index regex to accept `DEL-xx-yy-REQ-nnn`.
- **Conflict routing.** R4-Q1 names K-PATH, K-ROOT, K-HOOK and SPEC §15.2, but not K-PERM-1..6 or SPEC §15.1, which are the same family of unamended clauses.
  - I cited R4-Q1 for them rather than plain R4.
  - Proposal: widen the R4-Q1 wording to include K-PERM and SPEC §15.1.

## 6. Effort

- **Files read:** about 25, by excerpt. They were the deliverable files (SoW, _STATUS, _CONTEXT, MEMORY, _REFERENCES, _DEPENDENCIES, Dependencies.csv, INSP-03), `permission-overlay.ts` in full, and slices of Runtime `delegated.ts`, `delegated-engine-adapter.ts`, `runtime-service.ts`, `runtime-method-service.ts`, `turn-coordinator.ts`, `codex-supervisor.ts`, `chat-panel.tsx`, the permission route and cards, CONTRACT/SPEC/TYPES permission sections, and the D-GOV-43 and D-APP-127 records.
- **Not read in full:** `_SEMANTIC.md` and `_SEMANTIC_LENSING.md`. They are large and contain no indexed units.
- **Context budget:** adequate, not tight.
