# DEL-06-06 Hook Lifecycle and Compaction Mirror — forward-pass notes

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 wave 1, PKG-06. Basis: frozen tree at `00115c719`.
Ledger: `DEL-06-06_claims.csv` (52 rows). Pass 1 (forward) only.

## 1. Census

Coverage: 33 indexed units (CLM-001..CLM-033), plus 3 `REGISTER-n` and 2 `STATE-n` run-local rows.

**Split rate.** 1 of 33 units was split (3%). CLM-010 holds 15 separately numbered requirements
(DEL-06-06-REQ-001..015), so it became `CLM-010.1`..`.15`. Its `SubItems` cell is empty because the
REQ IDs carry the deliverable prefix. CLM-015 (AC-001) and CLM-022 (VER-001) each list one sub-item
and have one row, with the item named in Notes.

**Rows by ClaimType:** REQUIREMENT 29 · STATE_ASSERTION 8 · CONTEXT_CLAIM 8 · ACCEPTANCE 4 · REGISTER_DEFECT 3.

**Rows by Disposition** (all rows / SEE rows / rows excluding SEE):

| Disposition | All | SEE | Excl. SEE |
|---|---:|---:|---:|
| STALE_SPECIFICATION | 22 | 8 | 14 |
| IMPLEMENTED_DIFFERENTLY | 11 | 6 | 5 |
| ALIGNED | 8 | 0 | 8 |
| PARTIALLY_IMPLEMENTED | 5 | 1 | 4 |
| AUTHORITY_CONFLICT | 2 | 0 | 2 |
| NOT_AUDITABLE | 2 | 0 | 2 |
| DOCUMENTED_UNIMPLEMENTED | 1 | 0 | 1 |
| REMAINING_STATE_MISMATCH | 1 | 0 | 1 |
| **Total** | **52** | **15** | **37** |

The 15 SEE rows are CLM-008/016/023/028 → CLM-001; CLM-010.15/013/021 → CLM-005; CLM-011 → CLM-007;
CLM-014 → CLM-006; CLM-020 → CLM-015; CLM-024 → CLM-009; CLM-025 → CLM-003; CLM-030/033 → CLM-027;
and CLM-031 → CLM-019.

**Other columns.** Confidence: HIGH 32, MEDIUM 18, LOW 2. HumanDecisionNeeded: NO 30, R4-Q1 19,
R4 3. No errata file (pass 1).

## 2. Least-confident rows

- **DEL-06-06#CLM-010.7** (REQ-007, PreCompact boundary persisted when available). Sealed as
  IMPLEMENTED_DIFFERENTLY. The live Codex path records any upstream notification unchanged as
  `codex.notification`. It has no compaction projection, even though the delegated adapter
  descriptor declares `compaction: true`.
  - Alternative 1: if the pinned stock Codex never emits a compaction notification, the row is
    DOCUMENTED_UNIMPLEMENTED.
  - Alternative 2: if SPEC §15.2 (unamended) is read as binding the Codex path, the row is
    AUTHORITY_CONFLICT under R4-Q1.
  - I did not verify which notifications Codex emits at the pin, because the only wire captures are
    under `projects/chirality-runtime/execution/**`, which is out of bounds.
- **DEL-06-06#CLM-010.11** (REQ-011, no secrets; large payloads go to artifacts). Sealed as
  PARTIALLY_IMPLEMENTED.
  - `session-store.ts` `persistEvent`/`appendEvent` write events without a redaction step.
  - `codex.notification` keeps the raw upstream `params`. Only `tool.progress` deltas are capped
    (65,536 chars).
  - A grep for `redact|sanitiz|scrub` over runtime `core/src` found nothing.
  - Alternative: redaction happens in an upstream layer I did not trace, which would make the row
    ALIGNED. Amended K-EVENT-6 requires structural redaction before every sink, so this row is worth
    a verifier look.
- **MEDIUM rows that could flip:**
  - CLM-010.1 and CLM-010.12 are ALIGNED on the reading that amended CONTRACT K-EVENT-6 outranks the
    SPEC §10.3 translate-hook-names rule (DIRECTIVE §0 order). A stricter reading of K-ENGINE-4/K-CORE-1
    would make them PARTIALLY_IMPLEMENTED.
  - CLM-010.4 is IMPLEMENTED_DIFFERENTLY rather than DOCUMENTED_UNIMPLEMENTED, on the same
    Codex-emission uncertainty as CLM-010.7.

## 3. Register-defect summary

- **REGISTER-1.** The `_REFERENCES.md` MATCH hashes for CONTRACT, SPEC and PRD do not reproduce
  (`HASH-RECOMPUTE@00115c719`, pack `REFERENCE_HASHES.csv`: all `Match=NO`). Ten rows restate it:
  CLM-001/007/008/011/016/018/023/028/032 and CLM-010.14. The SoW's four dated "D-APP-56 R5 P40
  current-state notes" all assert a MATCH that is now false.
- **REGISTER-2.** `_DEPENDENCIES.md` and `Dependencies.csv` have lagging metadata:
  - The declared edges are still "TBD", and implementation, test and writer paths are still "TBD",
    although the SoW names them.
  - EvidenceFile pointers name `Specification.md`/`Guidance.md`/`Procedure.md`, which no longer exist
    because they were merged into `ScopeOfWork.md`.
  - DEP-06-06-008 is SATISFIED on the broken REF-006 MATCH.
  - DEP-06-06-004 targets the DEL-05-02 writer, but the live writer is the Runtime `session-store.ts`.
- **REGISTER-3.** `_CONTEXT.md` is stale on engine and topology:
  - It still says "Claude Agent SDK / Anthropic remains the first concrete/current path".
  - Its scope says "map daemon hook/compaction operational events"; D-GOV-43 retired the daemon.
  - It lists refreshed files that no longer exist.
  - The D-APP-127 application map shows `NO` for every DEL-06-06 carrier.
- **Other stale items, recorded in their own rows:**
  - The SoW frontmatter pins decomposition `7b0be4d87`. The SoW scope never took up the current
    decomposition row, which moved to hook-policy supply plus observation of daemon events (CLM-009).
  - The conflict table (CLM-032) records no post-D-GOV-43 conflict.
  - Several "path TBD" dispositions (CLM-006/012/014/019) contradict the paths named elsewhere in the
    same SoW.

## 4. Direction and cause

- **Main CauseTags:**
  - CODEX_SOLE_ENGINE (17): the SoW describes the in-process Claude SDK mapper. All of it is
    `LEGACY_ONLY` per `REACHABILITY.csv`: `chirality-hooks.ts`, `sdk-message-mapper.ts`,
    `session-events.ts`, `tool-result-artifacts.ts`.
  - DOC_HYGIENE (12).
  - PRE_V3_DRIFT (6): the stale TBDs, and `hook.failed`.
  - RUNTIME_EXTRACTION (4).
  - A2_TOPOLOGY (2).
  - CARRIER_PROPAGATION (1).
- **CAUSE2 secondaries:** RUNTIME_EXTRACTION 12, A2_TOPOLOGY 5, CODEX_SOLE_ENGINE 4,
  CARRIER_PROPAGATION 2, NATIVE_DELEGATION 1, DOC_HYGIENE 1.
- **Live-path picture:**
  - `codex-supervisor.ts:546` pushes every Codex notification unchanged.
  - `delegated-engine-adapter.ts:257-290` projects only `turn/started`, tool items and output deltas.
    Everything else, including any hook or compaction notification, is persisted as
    `codex.notification`.
  - No live producer of `hook.*` or `context.compacted` exists (grep over
    `projects/chirality-runtime/packages`).
  - Terminal outcomes are live and aligned: `delegated-runtime.ts:404-410`, and
    `turn-coordinator.ts:267-273` enforces a single terminal.
- **GOVERNING records used:**
  - D-GOV-43 via CONTRACT K-EVENT-4 (canonical store moved to the Root-owned `{userData}/runtime`
    path; the project-local `.chirality/sessions` path is legacy). MR-11 applies, since the clause
    names the path.
  - D-GOV-43 via K-EVENT-6 (upstream notifications cross with method names preserved).
  - D-APP-43, which rules that adapter lifecycle mapping satisfies PreCompact/Stop (MR-11 for
    REQ-006/007/010).
  - D-APP-56 P04 (`hook.progress`).
  - D-APP-38 (reference integrity).
  - The decomposition v3.2 DEL-06-06 row, cited as `GOV:`.
- **AUTHORITY_CONFLICT (R4-Q1):**
  - REQ-005: K-HOOK-1 and SPEC §15.2 fail-closed still name `ChiralityHooks`. D-GOV-43 leaves
    approval and sandbox to the user without amending them.
  - REQ-006: the TYPES §8.5 hook terms have no live counterpart.
- **CONTEXT records:** none used as DirectionEvidence. The only CONTEXT hit was
  `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` App. B.2 "Project trust"
  (project-scoped Codex hooks untrusted and skipped). It sits outside the §3/§10 sections that
  RUN_BASIS names as CONTEXT, so it is noted here only. It suggests the absence of a live hook layer
  was intended.
- **NONE_FOUND searches:**
  - The decision register `_REGISTER.md` (hook, compaction, `hook.failed`, DEL-06-06).
  - The D-APP-43/56/127 ruling records.
  - A grep over `plans/steers/chirality_app_v3_*` and the final release plan (`hook|compaction`).
  - The done-declaration candidate (no hits).
  - No record adopts `hook.failed`. It has been emitted since `e2b4c708b` (2026-06-14, via
    `git log -S`) and sits in the runtime-contracts registry (`event-schema.ts:28`), while SPEC §9.4
    lists neither `hook.failed` nor `hook.progress`.
- **Cross-deliverable observations** for PKG-03/05/09:
  - The delegated adapter descriptor declares `compaction: true` but maps no compaction event
    (`delegated-engine-adapter.ts:106`).
  - `harness-section9-manifest.json` maps `section9.context_compaction_boundary` to PRD FR-098
    (FR-099 is the persistence row) and to legacy tests only.
- **PostReleaseBasis:** all rows are `NO`.
  - Blamed lines in touched files: `codex-supervisor.ts` 546, 584-600 and 705-733, and
    `session-store.ts` 654-668, 813-821, 969 and 1126. All attribute to 95364569a, 25818258a,
    5c43b3a20, 9eaddb596, 0ed1a1a7f, 2f825f180, 8b3643e6c or 9b005c23a. None of the four
    post-release commits appears.
  - Line 40 of `codex-supervisor.ts` is not cited as a relied-on line.

## 5. Method friction

- **Unlisted sub-items.** CLM-010's REQ items are not listed in `SubItems`: the index pattern misses
  the `DEL-06-06-REQ-nnn` prefix. The split was done by hand under §2.2. Proposal: extend the R1
  `SubItems` regex to the `<DEL-ID>-REQ-nnn` form, so V-SUBITEMS enforces it.
- **Stale pointer inside a mostly-valid table.** CLM-003/004/012/018 mix valid normative rows with one
  or two stale factual rows (PRD MATCH, dependency state). One Disposition per unit forces
  STALE_SPECIFICATION on the whole unit. Proposal: allow an optional `.n` split for tables of
  independently dispositionable rows, which §2.2 already permits, but with a note convention that
  keeps the split rate from inflating.
- **SEE for partial restatement.** CLM-025 (five principles) SEEs CLM-003 because principle 2 is the
  stale statement, but principles 3-5 map to other rows. The SEE token cannot express "partly
  restates". Proposal: allow `SEE:<key>` plus a named-part qualifier.
- **Legacy gate evidence.** The App gate transcript gives totals only, so a named legacy test case
  passes only by inference from "all passed".

## 6. Effort

- **Read in full:** about 12 deliverable files (SoW, `_STATUS`, `_CONTEXT`, MEMORY, `_REFERENCES`,
  `_DEPENDENCIES`, Dependencies.csv, Assessment INSP-03, one run record), the evidence-pack manifest,
  and the filtered pack rows.
- **Read in ranges:** about 10 runtime/frontend source files, plus governing-doc slices (SPEC §9,
  §10.3, §15.2; CONTRACT K-rows; TYPES §8.5; PRD FR-098/099; DIRECTIVE §0) and the decomposition rows.
- **Not read:** `_SEMANTIC*.md` and most `_run_records` (no claims used).
- **Context budget:** moderate; not tight.
