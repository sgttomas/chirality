# DEL-04-03 — forward-pass notes (RUN_D128, R2, PKG-04)

Target: DEL-04-03 SdkMessageMapper and Provider-Neutral Translation, read at the frozen basis `00115c719`.
Ledger: `DEL-04-03_claims.csv` (53 rows). Validator: `RULES errors none | warnings none`, `RESULT PASS errors=0 warnings=0`.

## 1. Census

Sealed figures only. There is no errata file.

- **Rows:** 53 in total.
  - 48 cover the 27 indexed units.
  - 5 are run-local: REGISTER-1..3 and STATE-1..2.
- **By ClaimType:**

  | ClaimType | Rows |
  |---|---|
  | REQUIREMENT | 29 |
  | CONTEXT_CLAIM | 12 |
  | STATE_ASSERTION | 5 |
  | ACCEPTANCE | 4 |
  | REGISTER_DEFECT | 3 |

- **By Disposition:**

  | Disposition | Rows |
  |---|---|
  | STALE_SPECIFICATION | 14 |
  | ALIGNED | 9 |
  | IMPLEMENTED_DIFFERENTLY | 9 |
  | NOT_AUDITABLE | 9 |
  | PARTIALLY_IMPLEMENTED | 6 |
  | DOCUMENTED_UNIMPLEMENTED | 3 |
  | REMAINING_STATE_MISMATCH | 3 |

- **HumanDecisionNeeded:** R4-Q1 on 20 rows, R4-Q2 on 2, NO on 31.
- **Split rate:** 4 of the 27 units were split (15%).
  - CLM-004: 7 rows, one per Conditions table row.
  - CLM-009: 14 rows, REQ001..REQ014.
  - CLM-013: 2 rows, the amendment and AC-001.
  - CLM-019: 2 rows, the Records list and VER-001.
  - The SubItems units CLM-013 (AC-001) and CLM-019 (VER-001) each list one item. Each has a named `.2` row.
- **SEE rows (MR-4), counted separately: 4.**

  | SEE row | Target |
  |---|---|
  | CLM-009.9 | CLM-004.4 |
  | CLM-009.11 | CLM-004.1 |
  | CLM-009.12 | CLM-004.5 |
  | CLM-015 | CLM-008 |

## 2. Least-confident rows

- **CLM-004.5: redaction boundary** (DOCUMENTED_UNIMPLEMENTED, LOW).
  - Finding: the live Runtime event path (`delegated-engine-adapter.ts`, `turn-coordinator.ts` persistEvent) persists upstream Codex `params` verbatim, with no redaction step.
  - Alternative reading: Codex custodies the credentials (D-APP-127), so no App-held API key exists to leak, and App-side redaction under PKG-05 may cover display. On that reading the row is ACCEPTED_DIVERGENCE, or out of this deliverable's scope.
- **CLM-009.12: REQ012** (SEE CLM-004.5, LOW). The same alternative applies.
- **CLM-009.3: REQ003, name translation** (IMPLEMENTED_DIFFERENTLY, LOW).
  - Finding: identifiers are confined to `data.codex`, but `toolName` carries the raw Codex item type.
  - Alternative reading: DIRECTIVE §2.10 and the unamended SPEC §10.3 ("translate external names") conflict with SPEC §11 as revised under D-GOV-43 ("preserve upstream App Server method names, identifiers and payloads"). If the DIRECTIVE §0 order is held not to reconcile them, the row is AUTHORITY_CONFLICT (R4-Q1).
  - Why I did not choose AUTHORITY_CONFLICT: DIRECTIVE §2.10 already allows provider names as adapter metadata, and the live envelope keeps them inside `data`.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` records MATCH for CONTRACT, SPEC and PRD. None of the three reproduces (`REFERENCE_HASHES.csv`, Match=NO).
  - The SoW (CLM-002, CLM-016, CLM-027) meanwhile still says that REF-006 PRD has a HASH_MISMATCH. That claim rests on an even older expected hash.
  - DIRECTIVE, TYPES and PLAN are not in the pack and were not recomputed.
- **REGISTER-2.** In `Dependencies.csv`, the EvidenceFile, SourceRef and TargetLocation fields of DEP-04-03-007..011 still point to `Specification.md` and `Datasheet.md`.
  - Commit 603384787 (the SOW_V1 migration) deleted those files, both here and in DEL-03-03.
- **REGISTER-3.** `_DEPENDENCIES.md` gives "Declared Upstream/Downstream: TBD - no accepted dependency edges", while `Dependencies.csv` holds 11 ACTIVE rows.
  - One run note also carries a machine-specific absolute path.
- **Carriers.** `D-APP-127_APPLICATION_MAP.csv` shows no DEL-04-03 carrier revised.
  - STATE-1 records the stale daemon wording in `_CONTEXT.md`: the package scope says "packaged-daemon credential-boundary participation", and the deliverable scope says "daemon/provider outputs".
  - STATE-2 records the stale SCA-APP-001 line that "Claude Agent SDK / Anthropic remains the first concrete/current path".

## 4. Direction and cause

- **Main CauseTags:**

  | CauseTag | Rows | What it covers |
  |---|---|---|
  | CODEX_SOLE_ENGINE | 21 | The SDK mapper `sdk-message-mapper.ts` is LEGACY_ONLY. The live translation is Codex App Server → `codex-supervisor.ts` → `delegated-engine-adapter.ts`, in Runtime core. |
  | DOC_HYGIENE | 5 | Register and hash defects. |
  | CARRIER_PROPAGATION | 4 | Probe closure not propagated to the SoW. |
  | PRE_V3_DRIFT | 4 | Determinism test gap and TBD verification statuses already stale at INSP-03 (2026-06-20); absent records and fixture docs. |
  | A2_TOPOLOGY | 1 | STATE-1. |

- **CAUSE2 secondaries:**
  - A2_TOPOLOGY: CLM-004.1, CLM-009.4, CLM-009.11, CLM-010, REGISTER-1.
  - RUNTIME_EXTRACTION: CLM-004.4, CLM-005, CLM-008, CLM-015.
  - CREDENTIAL_CUSTODY: CLM-004.5, CLM-009.12.
  - CARRIER_PROPAGATION: CLM-003, STATE-1, STATE-2.
  - CODEX_SOLE_ENGINE: CLM-009.14, CLM-011, CLM-023.
  - PRE_V3_DRIFT: CLM-017.
  - DOC_HYGIENE: CLM-016.
- **GOVERNING records used:**
  - D-GOV-43, as transcribed into App SPEC §11 and TYPES §7.4 (revised 2026-09-12: the fixed UIEvent set is superseded) and into the SPEC and PRD "Current Codex-only MVP release basis" preambles.
  - D-APP-127, for STATE-1.
  - MR-11 is applied only where D-GOV-43's revision addresses the restated clause: SPEC §11 and TYPES §7.4. Those rows are CLM-004.1, CLM-009.4, CLM-009.11 and CLM-010, with LatestDecision `D-GOV-43`. Elsewhere it is cited as `(context)`.
- **CONTEXT records used:**
  - the `Dependencies.csv` DEP-04-03-007 Notes, which record the D-APP-52 live-probe closure on 2026-07-18;
  - the `_DEPENDENCIES.md` run notes of 2026-07-18;
  - the `_CONTEXT.md` Deliverable Scope.
- **Searches behind each NONE_FOUND:**
  - `_DECISIONS/_REGISTER.md`, grepped for `DEL-04-03|mapper|Mapper|PKG-04`. Only D-APP-06, 52, 56, 72 and 127 matched, and none addresses the model.* lane, determinism, redaction on the Codex path, or conformance of the Codex engine.
  - `DECISION_HITS.csv` for DEL-04-03 (22 rows).
  - `grep redact` over `chirality-runtime/packages/*/src`: the only hit is the stderr e-mail redaction in `codex-app-server-client.ts`.
  - `grep -i determinis` over the mapper and Runtime tests: no hits.
  - Runtime tests grepped for a conformance run of the Codex or delegated engine: none found.
  - `ls frontend/docs/harness/`: no mapper fixture document.
- **Done-declaration.** No Q-01..Q-13 was used.

## 5. Method friction

- **One SoW, two engines.** The deliverable's whole SoW is written for the Claude SDK mapper. Applying the live-path rule turns most requirements into IMPLEMENTED_DIFFERENTLY with R4-Q1.
  - Proposal: allow one whole-section row with per-REQ SEE rows when a deliverable's target engine is demoted wholesale by a preamble rather than by a ruling that names the deliverable. RETIRED_BY_RULING does not fit, because no ruling names DEL-04-03.
- **An unexpected MR-11 split.** SPEC §10.3 is unamended ("translate external names") while SPEC §11 was revised under D-GOV-43 ("preserve upstream names"). MR-11 therefore applies to the browser-contract rows but not to the name-translation rows.
  - Proposal: frame this as an explicit R4 sub-question, or fold it into R4-Q1's list of unamended clauses (SPEC §10.3 beside §15.2).
- **AC-001 and VER-001 (SOW_V1 conversion parity).** The conventions give ACCEPTANCE rows about kit conversion no verification token.
  - I used `RUN-INSPECTION` with a line-parity recompute against `603384787^`: 0 non-heading lines missing.
- **Validation script tag.** `validate-harness-section9.mjs` is a script, not a product entry, so it takes REACH=LEGACY_ONLY (UNREACHED). That tag reads oddly for a validation tool.

## 6. Effort

- **Files read:** about 25.
  - Deliverable: ScopeOfWork, _STATUS, _CONTEXT, MEMORY, _REFERENCES, Dependencies.csv, _DEPENDENCIES, Assessment.
  - GOVERNING docs, as slices: App SPEC §9–11, TYPES §7 and §9, DIRECTIVE §0 and §2.8–2.10, and the PRD preamble and FRs.
  - Code, as line ranges: `sdk-message-mapper.ts`, `delegated-engine-adapter.ts`, `codex-supervisor.ts`, `turn-coordinator.ts`, `types.ts`, `event-schema.ts`, the turn route, and the section9 validator.
  - Tests: case-name greps.
  - The pack CSVs and the gate transcripts.
  - Git: `show` for 603384787 (the parity check) and `blame -L` on `codex-supervisor.ts` lines 546–565 (no touched commit).
- **Context budget:** comfortable, not tight.
