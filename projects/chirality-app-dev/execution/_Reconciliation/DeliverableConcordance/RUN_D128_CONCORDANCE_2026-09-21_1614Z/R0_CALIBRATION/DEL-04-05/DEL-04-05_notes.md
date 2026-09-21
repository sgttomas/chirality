# DEL-04-05: forward-pass notes (RUN_D128 R0 calibration, unit F-04)

Source state: frozen tree at `00115c719`. Ledger: `DEL-04-05_claims.csv` (63 rows). These are agent dispositions, not rulings.

## 1. Census

- **Index units:** 36 (CLM-001..035 and REM-1). All are covered.
- **Rows:** 63.
  - 56 CLM rows.
  - 1 REM row.
  - 4 REGISTER rows (run-local keys).
  - 2 STATE rows (run-local keys).
- **Split rate:** 4 of 36 units (11%).
  - CLM-009 is split into 17 rows, one per requirement RQ-001..017.
  - CLM-004 is split into 4 rows, one per condition group.
  - CLM-014 is split in two: the source-state warning, and AC-001.
  - CLM-022 is split in two: the human-rulings table, and VER-001.
- **Un-indexed text:** OUT-001 (SoW line 16) is un-indexed and is covered under CLM-014.2.

Rows by ClaimType: REQUIREMENT 26, CONTEXT_CLAIM 15, STATE_ASSERTION 11, ACCEPTANCE 4, REGISTER_DEFECT 4, EXCLUSION 2, REMAINING_WORK 1.

Rows by Disposition: STALE_SPECIFICATION 24, IMPLEMENTED_DIFFERENTLY 14, PARTIALLY_IMPLEMENTED 9, ALIGNED 5, NOT_AUDITABLE 5, AUTHORITY_CONFLICT 2, UNKNOWN 1, REMAINING_STATE_MISMATCH 1, STALE_ASSESSMENT 1, STALE_VERIFICATION 1.

**Core finding.** The deliverable's Anthropic provider boundary still exists in code, and its tests pass in the APP gate transcript. The code conforms to the SoW. None of it is on the shipped path:

- `frontend/src/lib/harness/runtime.ts` is the only importer of `AnthropicAgentSdkManager` and `ClaudeAgentSdkManager`. Only tests and the same unwired `mcp/` island import `runtime.ts`.
- `POST /api/harness/turn` goes to the Runtime daemon port.
- The App-owned Codex composition wires a null credential port (`app-owned-composition.ts:225`). As a result:
  - the UI key store IPC reaches no safeStorage store;
  - `SafeStorageCredentialStore` is never instantiated.
- The renderer egress policy in `electron/main.ts` is the only live part. It is ALIGNED.

## 2. Least-confident rows (LOW = 4)

- **CLM-004.2 and CLM-009.10: remote MCP/plugins out of scope.** Disposition AUTHORITY_CONFLICT.
  - The effective Codex home links every user `~/.codex` entry except auth and the models cache, including config that carries MCP and plugin settings.
  - CONTRACT K-NET-1 still says remote MCP fails closed.
  - Alternative reading: IMPLEMENTED_DIFFERENTLY, with D-APP-127 / D-GOV-43 ("shares the user's configuration and resources") governing over untranscribed K-NET-1 text.
- **CLM-009.9: Node/SDK must not silently broaden the network.** Disposition PARTIALLY_IMPLEMENTED.
  - Command sandbox network is off for read-only and workspace-write.
  - No product-owned egress allowlist was found for the Runtime child or the codex app-server.
  - Alternative reading: ALIGNED, if K-NET-1 item 4 is read as delegating network posture to the user's Codex configuration and sandbox choice.
- **CLM-009.14: provider identifiers stay adapter metadata.** Disposition UNKNOWN.
  - Projection of Codex-path events into public contracts was not inspected in this unit.
  - Alternative reading: ALIGNED. It belongs to the DEL-03/DEL-04-03 audits.

**Other judgment calls, all MEDIUM:**

- The 13 Anthropic-adapter requirement rows are IMPLEMENTED_DIFFERENTLY, not ALIGNED. The conforming code is unwired, and PRD FR-027 makes stock Codex the sole production provider.
  - The alternative reading is ALIGNED at adapter level. PRD §8.5 and SPEC 12.3/16.2 remain in the GOVERNING text, and CONTRACT K-NET-1 labels the path "compatibility history".
- Those rows carry `HumanDecisionNeeded = R4`. The owner has not framed whether the §8.5 Anthropic requirements are retained compatibility obligations or retired.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` records ActualSHA256 equal to ExpectedSHA256, and MATCH, for REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD. The frozen files hash differently:
  - CONTRACT `57411f8d…`;
  - SPEC `8b0d805b…`;
  - PRD `17ca3f3c…`.

  The four repeated SoW notes "REF-006 is MATCH under D-APP-38" (CLM-001/007/015/023, CLM-014.1, CLM-004.4) are stale on that basis.
- **REGISTER-2.** `Dependencies.csv` EvidenceFile, SoW CLM-013/021, the `_DEPENDENCIES.md` run notes and the assessment all cite `Datasheet.md`, `Specification.md`, `Procedure.md` and `Guidance.md`. None of these files exists in the folder.
- **REGISTER-3.** The `_DEPENDENCIES.md` sections "Declared Upstream/Downstream: TBD — no accepted edges", and SoW CLM-017, contradict the 13-row register.
- **REGISTER-4.** Two assessment evidence pointers are stale (STALE_ASSESSMENT):
  - `build-network-policy.test.ts` is absent; the nearest file is `run-network-policy-proof.test.ts`;
  - the `harness-contract` `tool-descriptor.ts` pointer now targets a deprecated re-export of `@chirality/runtime-contracts`.

## 4. Direction and cause

**CauseTags:**

| CauseTag | Rows |
|---|---|
| CODEX_SOLE_ENGINE | 21 |
| DOC_HYGIENE | 15 |
| NONE | 10 |
| A2_TOPOLOGY | 7 |
| CARRIER_PROPAGATION | 3 |
| PRE_V3_DRIFT | 3 |
| CREDENTIAL_CUSTODY | 2 |
| RUNTIME_EXTRACTION | 1 |
| FACADE_DEPRECATION | 1 |

No OTHER tokens were used.

**CONTEXT records used:**

- `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md` ("Files changed").
  - It revised the DEL-09-06 and DEL-02-05 carriers: it dropped consent postures and the Root DEL-02-09/10 gates.
  - It did not touch DEL-04-05. This is the basis for REM-1 = REMAINING_STATE_MISMATCH / CARRIER_PROPAGATION.
- `…/TOPOLOGY_COMPARISON.md` C4, which shares config, plugins and MCP by link.
- The GOVERNING D-APP-127 ruling record is cited in LatestDecision. It supersedes D-APP-126 daemon custody and records credentials as custodied by Codex. STATE-1 (the `_CONTEXT.md` / decomposition line "daemon exclusively owns runtime credentials") is stale per MR-11.
- D-APP-65 governs RQ-011. Its timeout-assertion criterion is met in code.

**REM-1 (DEL-04-05-V3-02).**

- The gate names a Root/App account/consent contract that D-APP-127 retired.
- DEP-04-05-013 is PENDING.
- MechanicallyUnblocked is therefore NO.
- Partial substance exists:
  - sandbox-derived network posture;
  - typed `loginId`/`authUrl` login transport. This is not the `verificationUrl`/`userCode` form the item names.
- Per-destination `networkApprovalContext` prompts were not found in Runtime packages.

## 5. Method friction (R0 input)

1. **PostReleaseBasis cannot be determined without git.** Workers may not run git, so they cannot tell whether evidence lines come from `da95ec194`/`cb08dbe2f`/`9ecbdecdf`/`ccb95e06a`. All rows are `NO` by default.
   - Proposal: the manager supplies a per-file list of paths touched by those commits. Alternatively, drop the column from worker scope.
2. **The vocabulary has no token for conforming code that is unreachable from the product.** It does not distinguish "code conforms but is unreachable from the product (retained compatibility code)" from "code does something different".
   - IMPLEMENTED_DIFFERENTLY was used, but this over-states a mismatch.
   - Proposal: add `UNWIRED_IMPLEMENTATION`, or a CauseTag qualifier for it.
3. **ACCEPTED_DIVERGENCE needs text acknowledgment, but a ruling plus untranscribed wording is MR-11 STALE_SPECIFICATION.** For requirement rows whose premise was superseded (for example CLM-026), the choice between STALE_SPECIFICATION and IMPLEMENTED_DIFFERENTLY depends on whether the row is a state assertion or a requirement.
   - Proposal: state explicitly that superseded *requirements* are STALE_SPECIFICATION when a GOVERNING ruling directly contradicts them.
4. **The GOVERNING sources disagree internally.** PRD §8.5 and SPEC §12.3/§16 still carry Anthropic requirements, while PRD FR-027, CONTRACT K-NET-1 and D-APP-127 moved to Codex.
   - It is unclear whether this intra-GOVERNING drift should be AUTHORITY_CONFLICT on every row. It was used only where the conflict bites (remote MCP).
   - Proposal: allow one deliverable-level AUTHORITY_CONFLICT row that other rows reference.
5. **"MechanicallyUnblocked" is ambiguous when a later ruling retired the gate's premise.** Proposal: define `NO` for that case explicitly.

## 6. Effort

- **Files read:** about 45 distinct files, with ranged reads and greps.
  - 11 deliverable files.
  - About 25 App/Runtime source and test files.
  - 3 docs (CONTRACT, SPEC and PRD, by section).
  - 3 decision/CONTEXT records.
  - The conventions, basis, gate transcripts and validator.
- **Context budget:** comfortable, not tight.
- **Oversize threshold:** a 522-line SoW with a 17-row requirement table is manageable in one worker.
