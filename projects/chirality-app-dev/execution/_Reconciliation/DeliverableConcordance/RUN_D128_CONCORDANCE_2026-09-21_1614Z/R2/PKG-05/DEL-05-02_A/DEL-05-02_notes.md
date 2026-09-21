# DEL-05-02 notes: worker A, R2 forward pass

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-05 wave 2, frozen basis `00115c719`.
Ledger: `DEL-05-02_claims.csv` (51 rows, sealed after validation).

## 1. Census

- **Rows:** 51. That is 33 indexed units, 15 extra sub-rows from splitting CLM-010, 3 `REGISTER-n` rows and 1 `STATE-n` row.
- **ClaimType:**

  | ClaimType | Rows |
  |---|---:|
  | REQUIREMENT | 26 |
  | STATE_ASSERTION | 8 |
  | CONTEXT_CLAIM | 8 |
  | ACCEPTANCE | 4 |
  | REGISTER_DEFECT | 3 |
  | REMAINING_WORK | 2 |

- **Disposition:**

  | Disposition | All rows | SEE rows | Excluding SEE |
  |---|---:|---:|---:|
  | STALE_SPECIFICATION | 25 | 9 | 16 |
  | ALIGNED | 11 | 0 | 11 |
  | PARTIALLY_IMPLEMENTED | 5 | 1 | 4 |
  | REMAINING_STATE_MISMATCH | 4 | 1 | 3 |
  | ACCEPTED_DIVERGENCE | 3 | 2 | 1 |
  | DOCUMENTED_UNIMPLEMENTED | 1 | 0 | 1 |
  | IMPLEMENTED_DIFFERENTLY | 1 | 0 | 1 |
  | NOT_AUDITABLE | 1 | 0 | 1 |
  | **Total** | **51** | **13** | **38** |

- **Split rate:** 1 of 33 units was split, CLM-010 into `.1`–`.15`, one row per DEL-05-02-RQ-001..015. The Requirements table has independently dispositionable rows.
  - CLM-013 lists AC-001 and CLM-019 lists VER-001, one sub-item each. Each has a single row, and Notes names the item.
- **Errata:** none. This is pass 1.

## 2. Least-confident rows

- **CLM-010.12 (RQ-012, provider-neutral terms). Confidence LOW, verdict IMPLEMENTED_DIFFERENTLY.**
  - The canonical `HarnessEventType` union carries `codex.notification`, `codex.steer`, `codex.request` and `codex.request.resolved`. `UIEvent` `session:init` carries `claudeSessionId`.
  - Alternative 1, AUTHORITY_CONFLICT: D-GOV-43 item 2 (extensible representation, upstream names preserved) is read as requiring these names, which would undercut the unamended K-CORE-1 and K-ENGINE-4.
  - Alternative 2, ALIGNED: the `codex.` prefix is treated as adapter metadata.
  - HDN = R4.
- **REM-1. Confidence MEDIUM.**
  - I set MechanicallyUnblocked = YES because the gated representation is live at the frozen basis:
    - Runtime adapter passthrough;
    - App views for reasoning, plan and generic cards, rendered through `activity-shelf.tsx`.
  - Alternative: UNKNOWN, if MR-6 is read as requiring an App carrier for Runtime-landed code. I treated amended CONTRACT K-EVENT-1 as that carrier.
- **CLM-010.8 (malformed tail). Confidence MEDIUM, verdict ALIGNED.**
  - Alternative: PARTIALLY_IMPLEMENTED, because no Runtime test writes a malformed tail.
  - `appendJsonLine` does not repair a torn final line, so the next record would join the fragment.
- **CLM-010.13 (schema evolution). Verdict PARTIALLY_IMPLEMENTED.**
  - Alternative: ALIGNED. Replay handles v1 and v2 lines explicitly, and the persist path rejects other versions.
  - I judged it partial because the 2026-06-21 INSP-03 gap is still open: I found no replay-compatibility fixture.
- **CLM-005, CLM-009, CLM-015. Verdict ACCEPTED_DIVERGENCE.**
  - The schema, writer and replay constructions exist, but in `chirality-runtime`.
  - The SoW's controlling SCA-APP-010 Gate-5 section (applied row L337, D-APP-108 seating) moves ownership.
  - Alternative: ALIGNED, judging product behaviour only.
- **CLM-007 and CLM-027. Verdict REMAINING_STATE_MISMATCH, tie-break rule 2b.**
  - The "11 ACTIVE / 1 RETIRED" count lags the register, which now has 15 ACTIVE and 1 RETIRED.
  - Alternative: STALE_SPECIFICATION (recorded as ALSO:).

## 3. Register-defect summary

- **REGISTER-1, STALE_SPECIFICATION:**
  - `_REFERENCES.md` records REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD as ActualSHA256 = Expected, `MATCH`.
  - None reproduces at `00115c719` (HASH-RECOMPUTE, `REFERENCE_HASHES.csv`).
  - These SoW rows restate it: CLM-001, CLM-008, CLM-011, CLM-020, CLM-023 and CLM-024. CLM-006 restates it and also has its own defect.
- **REGISTER-2, REMAINING_STATE_MISMATCH:**
  - `_REFERENCES.md` reuses REF-009 and REF-010 in two tables: the software-decomp resources and the SCA-APP-010 Gate3/Propagation_Plan.
  - SoW REF-007 is `AGENT_SOFTWARE_DECOMP.md`. That file now exists only under `AgentRuns/FOUR_ROLE_OVERHAUL_20260909/source_basis/`. `_REFERENCES.md` REF-007 is `workflows/software-decomp/WORKFLOW.md`.
- **REGISTER-3, STALE_SPECIFICATION:**
  - `Dependencies.csv` DEP-05-02-013 still says the closed schema v2 gates consumption.
  - DEP-05-02-015 is PENDING on Root DEL-02-10 acceptance.
  - D-APP-127 retires both premises. The application map shows Dependencies.csv Revised = NO.
  - DEP-05-02-012 targets the SDK mapper, which is now LEGACY_ONLY.
- **Other stale metadata, recorded on indexed rows:**
  - CLM-016 prerequisites contradict themselves: dependencies "TBD" vs extracted edges, HASH_MISMATCH vs MATCH. They also omit DEP-05-02-013..016.
  - SEC-3 says DEP-013 and DEP-014 "await" writes that were made on 2026-09-05.
  - REM-1's Trace cites row L323. The SoW and DEP-05-02-013 use L337.
  - STATE-1: `_CONTEXT.md` still says daemon and Root acceptance (application map: NO).

## 4. Direction and cause

- **Main CauseTags:** DOC_HYGIENE 16; RUNTIME_EXTRACTION 11; CODEX_SOLE_ENGINE 4; A2_TOPOLOGY 3; CARRIER_PROPAGATION 3; PRE_V3_DRIFT 1; FACADE_DEPRECATION 1.
- **CAUSE2 secondaries:**
  - CARRIER_PROPAGATION: SEC-1, SEC-2, STATE-1.
  - A2_TOPOLOGY: REM-1, REM-2, REGISTER-3.
  - PRE_V3_DRIFT: CLM-003. SPEC renamed `sdk.system.init` on 2026-06-13 (`6b23eb96c`); the 2026-07-13 migration `0da38db4d` carried the old kit names.
  - CREDENTIAL_CUSTODY: CLM-010.9.
  - CODEX_SOLE_ENGINE: CLM-017.
  - RUNTIME_EXTRACTION: CLM-028.
  - DOC_HYGIENE: CLM-004, CLM-013.
- **GOVERNING records used:**
  - D-APP-127: it names "PKG-05 DEL-05-02 architecture-bound clauses revised" and retires the closed event vocabulary. MR-11 applies to SEC-1, SEC-2, REGISTER-3, STATE-1 and REM-2.
  - Amended CONTRACT K-EVENT-1, -3, -4 and -6 (blame `23b3879b3`, 2026-09-12).
  - D-APP-108 and D-APP-109.
  - K-EVENT-4 (userData Runtime store canonical; project-local is legacy) outranks SPEC 8.2 (project-local layout) under DIRECTIVE §0. So these are stale rows, not AUTHORITY_CONFLICT.
- **CONTEXT records used:**
  - `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md`, "Event representation (clarified)".
  - `SPIKE_DESIGN.md` §6.
  - `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` (G-WIRE: typed redaction before every sink).
- **Searches behind each NONE_FOUND:**
  - `_DECISIONS/_REGISTER.md`, grepped for DEL-05-02, HarnessEvent, events.jsonl and redaction. The only relevant hit is D-APP-22, which covers hydration only.
  - The replatform AgentRuns HANDOFF, SPIKE_DESIGN and INDEPENDENT_REVIEW.
  - The v3 final plan and the `plans/steers` redaction hit.
  - No record explains three things: the missing Runtime-sink redaction, the missing large-payload referencing, and the PRD/CONTRACT/SPEC hash drift.
- **Key finding (CLM-010.9):** the live Runtime event sink (`session-store.ts` `appendEvent`/`persistEvent`) persists `data` unredacted, including raw `codex.notification` params.
  - Structural redaction exists only in the LEGACY_ONLY App `session-events.ts`.
  - K-EVENT-6 requires redaction before every sink. `_STATUS` V3-01 carries it as open.

## 5. Method friction

- **Live-path REACH.** `REACHABILITY.csv` marks Runtime core modules LIVE through a barrel import (`attachment-picker.ts` > `core/index.ts`). That does not show execution.
  - I instead confirmed reach through the packaged service: `main.ts` > `runtime-service-host.ts` spawns the service; `app-owned-composition.ts:169,226` constructs SessionStore and TurnCoordinator.
  - Proposal: add an `EntryPoint` for the packaged Runtime service composition to the pack.
- **Controlling-section preamble.** The Gate-5 preamble declares every conflicting legacy clause to be "dated compatibility history". No verdict fits these clauses cleanly:
  - RETIRED_BY_RULING needs a ruling that names the item;
  - ACCEPTED_DIVERGENCE is about gates.
  - I used ACCEPTED_DIVERGENCE for ownership-only conflicts, and STALE_SPECIFICATION where the legacy text asserts a fact that current governing text contradicts, such as the path or category names.
  - Proposal: add a rule for "subordinated by an in-document controlling section".
- **MR-8(iv) on dated notes.** For CLM-007 (a dated "current-state" note), rule 3 (snapshot → REGISTER) and rule 2b (lagging bookkeeping) overlap.
  - I used 2b on the indexed row instead of adding another REGISTER row.
- **Gate-status lag without a done/open contradiction.** No rule directly covers an item whose open status is right but whose `NOT_SELECTABLE` flag lags a satisfied gate (REM-1). I used 2b ("a lagging status field").

- **Addendum 6 (R4-Q1 legacy-versus-live subject test).** The notice arrived before sealing and was applied to every row.
  - CLM-010.9 (redaction) and CLM-010.10 (large-payload artifacts) are product-behaviour rows. The only code that meets them is tagged `REACH=LEGACY_ONLY`.
  - Both rows now cite `R4-Q1`: CLM-010.9 carries `ALSO_MODULE:ALIGNED` and CLM-010.10 carries `ALSO_MODULE:PARTIALLY_IMPLEMENTED`.
  - Every other row is met by LIVE code or has no code evidence, so none of them cites R4-Q1.

## 6. Effort

- **Files read:** about 45. That includes 8 deliverable files, the D-APP-127 ruling, CONTRACT/SPEC/TYPES/DIRECTIVE ranges, 12 Runtime/App source files in ranges, about 10 test files by grep and name, 2 gate transcripts, the evidence pack by script, and 3 CONTEXT records by grep.
- **Context budget:** adequate, but moderately tight. `_SEMANTIC*.md` and most `_run_records/` were not read. They are not indexed units.

## Coverage gaps

- **Undocumented delivered work:** App-side normalized views of the extensible representation already ship. They are LIVE:
  - `harness-event-views.ts` `deriveCodexNotifications`;
  - `native-progress.ts`;
  - `turn-activity.ts`.

  No DEL-05-02 text records them as delivered. REM-1 still reads as not selectable. The owner is plausibly DEL-05-02 (V3-01) or DEL-05-04 (replay/transcript).
- **Stale code comment (not a deliverable claim):** the `route.ts` comment on `/api/harness/session/[id]/events` still says it "reuses `replayHarnessEvents`". The route actually calls the Runtime port.
