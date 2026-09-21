# DOC-VALSTRAT notes (`projects/chirality-app-dev/docs/VALIDATION_STRATEGY.md`)

Worker: EXT TASK W_DOC_VAL (RUN_D128, R2 scope extension, wave 5). Frozen basis `00115c719`.
Audit question: does the section match what shipped?

## 1. Census

- Units: 9 (`DOC:VALSTRAT#0`..`#8`). All 9 are covered. The ledger has 22 rows.
- **Split rate:** 1 of 9 units is split (11%). §3 (`#4`) is a table of 14 command rows that can each take their own disposition, so it becomes `#4.1`..`#4.14`. No other unit is a numbered list or a table of that kind: the §2 class table is a single classification scheme and the §4 routing table is one routing rule.
- **SEE rows:** 0.
- **By ClaimType:** STATE_ASSERTION 16, REQUIREMENT 4, CONTEXT_CLAIM 2.
- **By Disposition:** ALIGNED 13, STALE_SPECIFICATION 7, NOT_AUDITABLE 2.
- **By Confidence:** HIGH 9, MEDIUM 13, LOW 0.
- **HumanDecisionNeeded:** NO 18; R4-Q1 4 (`#4.5`, `#4.6`, `#4.7`, `#5`).
- **Rows marked `RELEASE_PROCESS_NOT_RUN`:**
  - `#4.7`: packaged Agent SDK proof, which cannot pass on the A2 package.
  - `#4.11`: network-policy proof for the v3.0.0 package; no run is recorded.
  - `#7`: attestation.
  - `#8`: packaged S-6/S-8 and the disconnect repeat on the stapled App.
- No errata file.

## 2. Least-confident rows (with alternative readings)

No row is LOW. These MEDIUM rows had a plausible alternative reading:

- **`#4.5` and `#4.6` (SDK dev-turn and MCP-probe commands).** STALE_SPECIFICATION, because the section is titled "Current Local Command Surface" and the only code these commands exercise is LEGACY_ONLY.
  - Alternative: ALIGNED. The commands exist and pass, and the rows describe only what each command does. Recorded as `ALSO_MODULE:ALIGNED`.
- **`#4.11` (network-policy proof).** The literal claim, "loopback plus Anthropic", is still true of `electron/main.ts:133`.
  - I read "current shipped ... policy" as a claim about the product. The shipped product's model egress is now the Codex child, which this proof does not sample.
  - Alternative: ALIGNED as a description of the renderer allowlist.
- **`#4.14` (`desktop:dist`).** STALE_SPECIFICATION, because both the release candidate (3.0.0-rc.1) and the v3.0.0 release DMGs were produced by `desktop:dist` with Developer ID signing.
  - Alternative: ALIGNED. The default invocation is unsigned, and the script never notarizes.
- **`#8` (§7 shared-runtime addendum).** ALIGNED: every listed test family exists and passes, and S-1..S-8 passed on the source-run production path.
  - Alternative: PARTIALLY_IMPLEMENTED. S-5 passed only "with note", because the TASK role body was not supplied to the child. The fix (95b342519) has no recorded S-5 rerun.

## 3. Register-defect summary

None. This document is not a deliverable register and has no `_REFERENCES.md` hash rows. No `REGISTER-n` rows.

## 4. Direction and cause

**CauseTags**

- CODEX_SOLE_ENGINE: 6 rows.
  - The SDK and Pi commands and routes, the network proof, and the §6 open decisions.
  - These rows cite `GOV:D-GOV-43`. D-GOV-43 names the Codex sole-engine rule. The Root AGENTS.md statements are that "Codex is the sole engine" and that local models are Codex model providers.
- V3_RELEASE_SCOPE: 1 row, `#4.14`.
  - Signing entered v3 scope through the replatform build. Cited as `CTX:` `APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md` and `APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`.
- `CAUSE2:` secondaries:
  - PRE_V3_DRIFT on `#4.11`: the Anthropic-only allowlist predates v3.
  - DOC_HYGIENE on `#4.14`.
  - V3_RELEASE_SCOPE on `#7`.
- No `OTHER:` tokens were used.

**CONTEXT and governing records used**

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/EVIDENCE.md`: S-1..S-8 PASS from source.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md`: signed build. Packaged S-6/S-8 are left to the owner.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md` and `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/OWNER_TRIAL_NOTES.md`: v3.0.0 was notarized and published on 2026-09-13.
- D-GOV-43, the ruling record under Root `docs/governance_harness/_DECISIONS/`.

**Searches behind `NONE_FOUND` values**

- `#4.14` LatestDecision: I searched `_REGISTER.md` for a ruling on signing or the `desktop:dist` posture. D-APP-127 covers custody and topology, not signing, and I found no ruling.
- Several ALIGNED rows carry `NONE_FOUND` in LatestDecision. No decision governs a command description.

**R4-Q1 by evidence (rule 3)**

- `#4.5`, `#4.6` and `#4.7`: the only code these commands exercise is LEGACY_ONLY.
- `#5`: the SDK-options, canUseTool, hooks and packaged-SDK routing rows point only at LEGACY_ONLY modules and commands.
- I read these routing and validation-command rows as "evidence methods for retained code". They turn on whether that code is history, compatibility or obligation.

**Done-declaration context (not cited as HumanDecisionNeeded)**

- The release-evidence findings (`#7`, `#8`) touch the done-declaration questions about release completeness. They are CONTEXT only.

## 5. Method friction

- **Command tables in process documents.** Splitting a 14-row command table is correct under the brief. Most rows are unproblematic command descriptions, so this inflates the ALIGNED count.
  - Proposed: allow a single "table holds except rows X, Y" row, with sub-rows only for the divergent entries.
- **`RELEASE_PROCESS_NOT_RUN` placement.** The token is Notes-only, and "did not run" needs negative evidence, meaning absence from the release AgentRuns records.
  - I read only the replatform, user-journeys and packaging AgentRuns folders. A record elsewhere could overturn a token.
  - Proposed: the manager should treat these tokens as "no record found in the release AgentRuns set", not as proven non-runs.
- **LifecycleState for extension rows with `DeliverableID = NONE`.** There is no `_STATUS.md` to read, so I wrote `NOT_APPLICABLE (no owning deliverable)`. The validator does not check this column.

## 6. Effort

- About 45 files or excerpts read. These include:
  - the two source documents;
  - the rulebook;
  - the evidence pack CSVs and 5 surface capability files;
  - the gate transcripts and 2 workflow files;
  - about 10 AgentRuns records;
  - about 20 targeted code and test excerpts.
- Context budget was adequate but not loose. Both ledgers shared one evidence sweep.
