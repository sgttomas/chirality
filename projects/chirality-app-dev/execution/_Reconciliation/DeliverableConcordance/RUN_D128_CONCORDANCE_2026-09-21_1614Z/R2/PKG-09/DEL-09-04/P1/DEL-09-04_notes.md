# DEL-09-04 — forward-pass notes, split part P1 (SEC-1, CLM-001..CLM-012)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-09 R2 (wave 5). TASK (Type 2) worker, part P1.
Basis: frozen tree at `00115c719`. Ledger: `DEL-09-04_claims.csv` in this folder (44 rows).
Run-local rows in this part: `STATE-1` (numbering range STATE-1..49). No REGISTER rows arise inside the
P1 sections. The `_REFERENCES.md` hash REGISTER row belongs to part P2.

## 1. Census

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| ALIGNED | 17 | 5 |
| STALE_SPECIFICATION | 13 | 6 |
| PARTIALLY_IMPLEMENTED | 9 | 1 |
| NOT_AUDITABLE | 4 | 0 |
| DOCUMENTED_UNIMPLEMENTED | 1 | 0 |
| **Total** | **44** | **12** |

- By ClaimType: REQUIREMENT 24, ACCEPTANCE 11, CONTEXT_CLAIM 4, STATE_ASSERTION 3 (CLM-001, CLM-003.8, STATE-1), EXCLUSION 2.
- Without SEE rows (MR-4): 32 primary rows. ALIGNED 12, STALE_SPECIFICATION 7, PARTIALLY_IMPLEMENTED 8, NOT_AUDITABLE 4, DOCUMENTED_UNIMPLEMENTED 1.
- Confidence: HIGH 26, MEDIUM 18, LOW 0.
- Split rate: 5 of 13 indexed units split (38%).
  - CLM-003 (attributes table, 8 rows).
  - CLM-004 (conditions table, 4).
  - CLM-009 (REQ-001..REQ-011, 11).
  - CLM-011 (verification table plus closing rule, 10).
  - CLM-012 (documentation list plus AC-001, 2).
  - The index lists no SubItems of k ≥ 2 for P1 units. CLM-012 lists AC-001, which has its own row (CLM-012.2).
- SEE targets all lie inside this part's ledger. No SEE token points into P2.
- No errata file (pass 1).

## 2. Least-confident rows (with alternative readings)

No row is LOW. The MEDIUM rows most open to another reading:

- **CLM-004.4 / CLM-009.9 / CLM-011.9 (network guardrails) — STALE_SPECIFICATION.**
  - Alternative: PARTIALLY_IMPLEMENTED. The live Codex sandbox mapping (`codex-supervisor.ts:104-109`, networkAccess false for read-only and workspace-write) is a guardrail, and only the packaged proof is missing.
  - Chosen reading: the object named, "accepted Codex supplier network guardrails", no longer exists after D-GOV-43 / D-APP-127. The repair is to the text, with evidence to follow. `ALSO:PARTIALLY_IMPLEMENTED` is recorded.
- **CLM-011.4 (minimum-OS inspection) — DOCUMENTED_UNIMPLEMENTED.**
  - Alternative: PARTIALLY_IMPLEMENTED. `minimumSystemVersion` 15.0.0 is configured (`package.json:158`) and test-pinned.
  - Chosen reading: the verification item is an *inspected* output value, and no inspection is recorded or scripted in-root.
  - CLM-011.5 (architecture) went PARTIALLY_IMPLEMENTED because PA-2 at least states arm64 identity for the built product.
- **CLM-003.6 (SDK subprocess posture) — ALIGNED.**
  - Alternative: PARTIALLY_IMPLEMENTED. PRD NFR-030 now asks for the Runtime-service-spawned app-server under signature and notarization, and the in-root probe is `codex --version` only.
  - The attribute text asks only for find-and-execute, which the live chain does. The NFR-030 shortfall is dispositioned at CLM-009.8.
- **CLM-003.7 (source completeness as P0 gate) — ALIGNED.**
  - Alternative: PARTIALLY_IMPLEMENTED. The KG-001 candidate rows (`tools/REGISTRY.md`, `examples`) stay `remediation_required` without gating `status`.
  - Chosen reading: the required-asset gate is fail-closed, and the attribute hedges ("may be incomplete").
- **CLM-008 (scope) — STALE_SPECIFICATION.**
  - Alternative: ALIGNED. Signing acts (identity, notarization) remain owner acts, so "signing beyond unsigned/adhoc is out of scope" could still describe what this deliverable does.
  - Chosen reading: the deliverable's own packaging glue now contains the Developer ID signing hook and post-sign pin check, and SPEC §19.4 makes the signed/notarized candidate the release verification target.
- **CLM-009.11 (desktop:pack) — ALIGNED.**
  - The rationale text (the D-APP-18 live agentSdk proof) is historical. No A2-era `desktop:pack` run is recorded, so a PARTIALLY_IMPLEMENTED reading of "run or review the proof" is possible.

## 3. Register-defect summary

- No REGISTER rows in P1.
- CLM-001 and CLM-003.8 restate REF-006 `MATCH` as current. By tie-break rule 3 they take STALE_SPECIFICATION, with `HASH-RECOMPUTE@00115c719`: recorded `8649ccba…` against recomputed `17ca3f3c…` for `docs/PRD.md`.
  - The per-deliverable hash REGISTER row is P2's (numbered from 51).
  - The merge should link CLM-001 to it. I wrote no `SEE:` token, because the target is outside this part's ledger and the part validator would reject it.
- Frontmatter `decomposition_basis` pin `d6f6cadb2` (SoW L5) sits outside P1's indexed sections. See Coverage gaps.

## 4. Direction and cause

- **Main CauseTags** (all rows):
  - A2_TOPOLOGY 12.
  - CARRIER_PROPAGATION 6.
  - DOC_HYGIENE 2.
  - CODEX_SOLE_ENGINE 2.
  - PRE_V3_DRIFT 1.
- **Secondaries used:** `CAUSE2:CARRIER_PROPAGATION`, `CAUSE2:A2_TOPOLOGY`, `CAUSE2:CODEX_SOLE_ENGINE`.
- **Core finding.** The SoW was last edited on 2026-09-10 (`2f825f180`), one day before D-GOV-43.
  - D-APP-127 names DEL-09-04 "revised", but only `_STATUS.md` was revised. The D-APP-127 application map gives the SoW as `NO`.
  - As a result, SEC-1, the attributes, conditions, scope, REQ-001/009 and AC-001 still describe:
    - the unsigned/unnotarized release target;
    - the "admitted Codex supplier" and its containment safeguards.
- **Governing change**, cited with `GOV:`:
  - `docs/CONTRACT.md:17` reads K-RELEASE-1 with D-GOV-43 and names bundle signing and notarization as ordinary integrity.
  - `docs/SPEC.md:1203` (§19.4): the consolidated candidate is signed and notarized.
  - PRD §7.12, §12.8 and NFR-030 are amended.
- **Unamended text.** PRD §6.2 and decomposition SOW-072 still say unsigned. DIRECTIVE §0 order resolves this (CONTRACT and SPEC over PRD and the decomposition), so no AUTHORITY_CONFLICT.
- **CONTEXT sources used:**
  - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/PACKAGING_PROCEDURE.md`: the §Record section explains why A2 evidence lives in AgentRuns and not in `DEL/Evidence/`, and §Steps 4-5 omit any minimum-OS or architecture inspection.
  - `BUILD_EVIDENCE_20260912.md` (PA-1), `APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md` (PA-2) and `PUBLIC_RELEASE_20260913.md` (PUB): recorded runs, used as run inspection and never as rulings.
- **Node floor (CLM-004.1).** GOV:D-APP-72 (ruling L25 names the project Node floor `>=22.19.0`); commit `4412157d1` (2026-07-22), so PRE_V3_DRIFT.
- **No `NONE_FOUND` DirectionEvidence** and no UNRECORDED_JUDGMENT rows. Searches behind the directions:
  - `_DECISIONS/_REGISTER.md` rows D-APP-02, 18, 38, 56, 72, 80, 97, 100 and 127;
  - the D-APP-127 ruling body;
  - `loop/LOOP_INIT.md` F-APP-2;
  - the AgentRuns packaging records.
- **Done-declaration context (Notes only):** Q-02 on CLM-003.1, CLM-008 and CLM-012.2.
  - v3.0.0 shipped Developer ID signed and notarized (PUB L35-37), while F-APP-2 and D-APP-97 fence signing and notarization for loop work.
  - Whether the session publishing approval counts as the release act is Q-02's question and was not ruled on here.
- **R4-Q1 not cited.**
  - Every relied-on code path is a live packaging entry: `package.json` `desktop:dist`/`desktop:pack` chains, `build.afterPack`, `build.mac.sign`, the `verify:version-identity` operator script, and `electron/main.ts`. The Runtime `codex-supervisor.ts` is LIVE via `standalone-bin.ts`.
  - The legacy Claude SDK probe scripts do not meet the Codex-reading claims.
  - The signing hook is tagged LIVE and noted `DISABLED_BY_DEFAULT` without an identity.
- **PostReleaseBasis** is NO on every row.
  - No `frontend/**` path is in TOUCHED_PATHS.
  - `codex-supervisor.ts` is touched. Blame on the relied-on lines gives none of the four post-release commits:
    - lines 104-108 and 259-261: `95364569a`;
    - line 109 (closing brace): `1cb09c09d`.
  - Self-flag for pass 2: the sealed CLM-004.4 Note says the cited lines "blame to 95364569a". Line 109 blames to `1cb09c09d`. PostReleaseBasis NO is unaffected.

## 5. Method friction

- **Cross-part SEE.** The MR-5 rule "SoW rows restating [the hash drift] cite that key" cannot be met in a split part: the REGISTER row lives in P2, and `SEE:` must resolve inside the validated ledger.
  - Proposal: allow the manager to add the `SEE:` link at merge, or let split validation accept `SEE:` to a key in the sibling part's declared range.
- **Paths in documentary evidence.** Mentioning a `frontend/...` path inside a documentary (non-code) evidence cell trips the REACH check, which reads it as code, so I rephrased. Proposal: let `documentary claim:` prefixed cells skip REACH.
- **Recorded proof versus capability.** Verification-table items (CLM-011) ask for recorded evidence. The evidence exists only in AgentRuns (CONTEXT, run inspection), not in the deliverable.
  - I dispositioned these PARTIALLY_IMPLEMENTED (evidence exists but not deliverable-bound, and none for the current version 3.0.1).
  - A rule on whether AgentRuns evidence counts as "the deliverable's" evidence would reduce variance across PKG-09 workers.

## 6. Effort

About 35 files or ranges read:

- the SoW (full), `_STATUS` head, `_REFERENCES`, INSP-03;
- governing sections of the App CONTRACT, SPEC, PRD, TYPES and DIRECTIVE §0;
- `BUILD_AND_RELEASE` §4 and §8;
- the D-APP-127, D-APP-72 and D-APP-02 rulings and register rows;
- 9 packaging scripts (ranges), `package.json`, `main.ts` and `codex-executable.ts` ranges, `codex-supervisor.ts` ranges;
- test case lists, the gate transcript, PA-1, PA-2, PUB and the packaging procedure.

The context budget was adequate but not loose.

## Coverage gaps

- **OUT-001 (SoW L22, Purpose section, unindexed).** It restates "unsigned or adhoc" and the "admitted Codex supplier subprocess" and "accepted Codex supplier network guardrails". It carries the same staleness as SEC-1 and CLM-012.2 but has no indexed unit. SEC-1's Notes point to it, and the manager may want a run-local row or a note in R3.
- **Frontmatter (SoW L1-8).** The `decomposition_basis` pin `d6f6cadb2` (a known basis defect, RUN_BASIS §5) has no indexed unit and no P1 or P2 owner.
- **Output and Evaluation Matrix (SoW L371-375).** This follows P2's range. It traces OUT-001 to CLM-007 (a heading), a mapping that does not look meaningful. I did not audit it; it is flagged for P2 or the manager.
