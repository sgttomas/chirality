# DOC-RELIANCE notes (`projects/chirality-app-dev/docs/harness/reliance_boundary_register.md`)

Worker: EXT TASK W_DOC_VAL (RUN_D128, R2 scope extension, wave 5). Frozen basis `00115c719`.
Owning deliverable: DEL-01-02 (the Status table names it as the source deliverable; lifecycle IN_PROGRESS).
Audit question: does the section match what shipped?

## 1. Census

- **Units and rows.** 13 units (`DOC:RELIANCE#1`..`#13`), all covered, in 51 rows.
- **Split rate.** 4 of 13 units are split (31%), into 42 sub-rows:
  - `#3` Boundary Register: 14 rows.
  - `#4` Enforcement Matrix: 14 rows.
  - `#11` SCA-APP-003 addendum: 8 rows.
  - `#13` SCA-APP-004 addendum: 6 rows.
- **Units kept whole.**
  - The Residual Risks (`#8`) and Cross-Check (`#9`) tables each state one posture, so each is one row.
  - The Section 9 index (`#6`) makes one claim about its 16 rows, so it is one row.
- **SEE rows: 14.** Each `#4.n` restates `#3.n` for the same boundary, with the same Disposition and `SEE:DOC:RELIANCE#3.n`. Without the SEE rows the ledger has 37 rows.
- **By ClaimType.** REQUIREMENT 43 (14 of them SEE), STATE_ASSERTION 7, CONTEXT_CLAIM 1.
- **By Disposition (all 51 rows).**

  | Disposition | Rows |
  |---|---|
  | IMPLEMENTED_DIFFERENTLY | 16 |
  | ALIGNED | 12 |
  | STALE_SPECIFICATION | 9 |
  | PARTIALLY_IMPLEMENTED | 9 |
  | DOCUMENTED_UNIMPLEMENTED | 2 |
  | STALE_VERIFICATION | 1 |
  | RETIRED_BY_RULING | 1 |
  | NOT_AUDITABLE | 1 |

- **By Disposition, SEE rows excluded (37 rows).**

  | Disposition | Rows |
  |---|---|
  | ALIGNED | 12 |
  | IMPLEMENTED_DIFFERENTLY | 8 |
  | STALE_SPECIFICATION | 7 |
  | PARTIALLY_IMPLEMENTED | 6 |
  | DOCUMENTED_UNIMPLEMENTED | 1 |
  | STALE_VERIFICATION | 1 |
  | RETIRED_BY_RULING | 1 |
  | NOT_AUDITABLE | 1 |

- **By Confidence.** HIGH 17, MEDIUM 29, LOW 5.
- **HumanDecisionNeeded.**

  | Token | Rows |
  |---|---|
  | NO | 22 |
  | R4-Q1 | 13 |
  | R4-Q3 | 4 |
  | R4-Q5 | 4 |
  | R4-Q2; R4-Q5 | 2 |
  | R4-Q2 | 2 |
  | R4-Q4 | 2 |
  | R4 | 2 |

  Counts include SEE rows.
- **`RELEASE_PROCESS_NOT_RUN` rows.**
  - `#3.2`: packaged offline Pi proof. It cannot pass on the A2 package.
  - `#8`: network-proof rerun for a release-significant review. No run is recorded for v3.0.0.
  - `#11.1`: packaged S-6 and disconnect repeat on the stapled App.
- **Errata.** No errata file.

## 2. Least-confident rows (with alternative readings)

- **`#3.10` / `#4.10` RB-HUMAN-GATE: PARTIALLY_IMPLEMENTED (LOW).**
  - Alternative: ALIGNED. This reads the row as procedural human-gate policy, with no product mechanism to audit.
  - Why PARTIALLY_IMPLEMENTED: read as a product guarantee, the only live control is the lifecycle route's HUMAN actor, and that actor is a caller-supplied string.
- **`#11.7` RB-PEC-ADAPTER: STALE_SPECIFICATION (LOW).**
  - Alternative: ALIGNED. `#12` states the D-GOV-43 supersession directly below the row, and D-GOV-43 supersedes D-GOV-20 items 2-4 only on the App MVP Codex path.
- **`#11.8` RB-PUBLIC-RUNTIME: STALE_SPECIFICATION (LOW).**
  - Alternative: UNKNOWN. The export tooling is outside my evidence roots.
  - Why STALE_SPECIFICATION: the closure condition "after both pilots" names pilots that D-GOV-43 retired.
- **`#13.4` RB-WORK-SOURCE: PARTIALLY_IMPLEMENTED (LOW).**
  - Alternative: DOCUMENTED_UNIMPLEMENTED. The authority-class displays lived in the retired Work projection.
- **`#3.4` RB-PERMISSION: IMPLEMENTED_DIFFERENTLY, HumanDecisionNeeded R4 (MEDIUM).**
  - Alternative: AUTHORITY_CONFLICT. The unamended K-PERM-1/K-PERM-3 "deny-first" wording conflicts with D-GOV-43's user-chosen approval and sandbox policy. I did not resolve it; it is carried to R4.
- **`#3.5` RB-FILESYSTEM and `#3.11` RB-TOOL-SURFACE: R4-Q1.**
  - I cite R4-Q1 because no Chirality code on the live path meets the guarantee. `delegated.ts:324-329` only selects the Codex sandbox, which is another mechanism.
  - Alternative: treat the sandbox mapping as live code that partly meets the claim. Then rule 3 would not cite R4-Q1, and the row would still turn on K-ROOT/K-PATH, the invariants R4-Q1 names.
- **`#6` Section 9 index: STALE_VERIFICATION.**
  - Alternative: ALIGNED at module level. The IDs are implemented and pass.
  - I applied rule 2 because the "Boundary coverage" column claims coverage of product guarantees.

## 3. Register-defect summary

- **`#1`: REF-006 `docs/PRD.md` stated as "currently MATCH".** The hash does not reproduce: `REFERENCE_HASHES.csv` has DEL-01-02,PRD with `Match=NO`, and CONTRACT and SPEC are also NO.
  - The text names no snapshot. Under tie-break rules 1 and 3 it is STALE_SPECIFICATION on the section row, not a `REGISTER-n` row.
  - This file is not DEL-01-02's `_REFERENCES.md`. The per-deliverable REGISTER row for DEL-01-02's own `_REFERENCES.md` belongs to the PKG-01 ledger, not here.
- **`#8` and `#9` repeat the MATCH premise.**
  - `#8`: "Current corpus snapshot is MATCH". Folded into that row's STALE_SPECIFICATION.
  - `#9`: "Source traceability ... current D-APP-38 corpus snapshot". Left ALIGNED, with a note, because the check records traceability, not the hash.
- **Other register bookkeeping.**
  - The DecisionStatus `PROPOSED` fields hold.
  - The Status "Generated by ADQ-02" field holds.

## 4. Direction and cause

### CauseTags

| CauseTag | Rows | Scope |
|---|---|---|
| CODEX_SOLE_ENGINE | 27 | Dominant: SDK, Pi, hooks, path policy and settings boundaries superseded by the Codex host |
| A2_TOPOLOGY | 3 | RB-RESIDENCY, RB-PEC-ADAPTER, RB-PUBLIC-RUNTIME |
| SHELL_REDESIGN | 3 | SCA-APP-004 rows affected by the retired Work view and context references |
| RUNTIME_EXTRACTION | 2 | RB-AUDIT: store moved to the Runtime |
| NATIVE_DELEGATION | 2 | RB-SUBAGENT |
| DOC_HYGIENE | 1 | `#1` |

Counts include SEE rows.

### `CAUSE2:` secondaries and OTHER tokens

- FACADE_DEPRECATION (RB-ENGINE)
- CODEX_SOLE_ENGINE (RB-AUDIT)
- PRE_V3_DRIFT (RB-LIFECYCLE, RB-HUMAN-GATE)
- CREDENTIAL_CUSTODY (RB-REDACTION)
- DOC_HYGIENE (`#8`)
- `OTHER:V3_ROLE_ADOPTION` (RB-SUBAGENT; the prescribed token)

No other `OTHER:` token is used.

### Governing and CONTEXT records cited

- **GOVERNING:**
  - D-GOV-43, the Codex host re-platform: sole-engine rule; approval and sandbox policy are the user's choice; retired residency requirements; supersedes D-GOV-20 items 2-4 on the App path.
  - D-GOV-35, native descendants.
  - D-APP-127.
  - SCA-APP-010, cited as `GOV:SCA-APP-010`.
- **CONTEXT:**
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/EVIDENCE.md`: S-2, S-5, S-6 and S-7 observations.
  - `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`.

### `NONE_FOUND` searches

- **`#1` DirectionEvidence.** I searched `_REGISTER.md` (the D-APP-38 row) and the CONTEXT AgentRuns folders `APP_V3_CODEX_HOST_REPLATFORM_20260912` and `APP_V3_USER_JOURNEYS_20260912` for a REF-006 re-snapshot direction. I found none.
  - `HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH` defers "authority corpus drift" (RUN_BASIS §5), but it is not a listed CONTEXT source.
- **`#11.7` and `#11.8` ImplementationEvidence.**
  - `#11.7`: I searched App `frontend/src` and the runtime packages for a PEC adapter service. None exists; only legacy rehearsal drivers do (CAP-BUILD-038/039).
  - `#11.8`: I searched the same roots for a runtime export allowlist. None was found; the export tooling is outside my roots.
- **`#13.6`.** I searched `src/__tests__` for context-receipt and anchor-restoration tests. None was found.

### Named R4 questions (by evidence, rule 3 and Addendum 8)

- **R4-Q1 (13 rows).** On these rows the only code meeting the claim is LEGACY_ONLY: RB-LOCAL-PROVIDER, RB-FILESYSTEM, RB-SETTINGS, RB-TOOL-SURFACE, RB-HOOKS (each in `#3` and `#4`), plus `#6`, `#8` and `#10`.
  - Rows met partly by LIVE code do not cite it: RB-ENGINE, RB-AUDIT, RB-PERMISSION, RB-TRANSCRIPT, RB-SUBAGENT and RB-REDACTION.
- **R4-Q2 (4 rows).** Codex never ran through engine conformance: RB-ENGINE and RB-FALLBACK.
- **R4-Q5 (6 rows).** Codex payloads are stored as received: RB-ENGINE, RB-AUDIT and RB-REDACTION.
- **R4-Q3 (4 rows).** The actor is self-supplied: RB-LIFECYCLE and RB-HUMAN-GATE.
- **R4-Q4 (2 rows).** RB-SUBAGENT uses the "Agent 0/1/2" vocabulary.

Done-declaration questions Q-01..Q-13 are CONTEXT only and are not cited.

## 5. Method friction

- **Addendum 6 rule 3 and "another mechanism".** The rule counts code meeting the claim. On the Codex path, several guarantees are met by the Codex binary: its sandbox and approvals. That is not repository code; repository code only selects it (`delegated.ts:324-329`).
  - I treated sandbox selection as not meeting the claim, so R4-Q1 applies.
  - Proposed: state explicitly whether a LIVE selector of an external mechanism counts as "code meeting the claim".
- **Enforcement Matrix as SEE rows.** The matrix restates the Boundary Register one-to-one, so 14 SEE rows add volume without information.
  - Proposed: allow one whole-table SEE row when a table mirrors another table row by row.
- **Register tables in a non-deliverable file.** MR-5's one-REGISTER-row-per-deliverable hash rule does not fit a doc-level register that restates a deliverable's reference posture. I used STALE_SPECIFICATION with HASH-RECOMPUTE.
- **`RELEASE_PROCESS_NOT_RUN`.** This is negative evidence from the release AgentRuns set I read: the replatform, user-journeys and packaging folders. A record elsewhere could overturn a token.

## 6. Effort

- **Evidence.** The same evidence sweep as DOC-VALSTRAT, plus reads of:
  - the reachability rows for about 45 modules;
  - the WOVEN and SHELL capability files;
  - the lifecycle transition code;
  - the project registry drift code;
  - the D-GOV-43 ruling;
  - the register rows for D-APP-38/56/72/98/120/124-127.
- **Totals.** About 60 files or excerpts overall.
- **Context budget.** Moderately tight; the ledgers were generated by script from one evidence pass.
