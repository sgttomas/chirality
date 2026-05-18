# Industry-Practices PDF2MD Campaign — Resume Plan

**Persona:** PDF2MD (`agents/AGENT_PDF2MD.md`)
**Corpus:** `domain-test/domains/piping-design/_Sources/industry-practices/` — 108 PDFs across 19 chapter folders, 3,423 total pages
**Origin plan:** `/Users/ryan/.claude/plans/read-init-md-and-agents-md-noble-dolphin.md` (in-conversation plan from the prior session)
**Paused:** 2026-05-18 after Chapter 01 complete (T1 done)
**Resume point:** T2 — Chapter 02

---

## Campaign summary

Convert 108 PDFs to per-PDF Markdown via the merged `pdf2md-page-full` skill (single multimodal vision read per page, emits both Markdown and asset JSON), then concatenate into one root document `industry-practices.md` with a unioned asset manifest.

**Per-PDF runbook:** `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` is the authoritative step-by-step. It was updated this session — see "Workflow changes mid-campaign" below.

**Dispatch model:** PDF2MD (the main agent) dispatches Sonnet workers directly via `Agent(subagent_type: general-purpose, model: sonnet)`. Each worker handles ONE page. Up to 40 workers per wave, all in one message for parallelism. After every wave, audit on-disk by counting `page_*.md` and `page_*_assets.json` in WORK_DIR; re-dispatch any missing page solo before proceeding (worker rejections can happen without a clear signal in the agent's return text — trust the filesystem).

**Execution rhythm:** Chapter-gated. Process one chapter at a time, in `01-…` → `19-…` order. After every chapter completes, pause at an explicit gate for compaction opportunity.

---

## Workflow changes mid-campaign (IMPORTANT — read before resuming)

During Chapter 01, we discovered the industry-source redactor (`tools/pdf2md/redact_industry_sources.py`) had a precision problem: the bare "Shell" alias collided with engineering nouns (shell-and-tube, head-to-shell seam, shell-side flow). This produced semantic corruption in PDF 10 (Chevron manual: 6/6 hits were false positives) and PDF 08 (Shell DEP: 8 false positives mixed in with 153 legitimate doc-number substitutions + 4 lines of true Shell-the-company refs).

**Decisions made:**
1. **Redaction step removed from the workflow.** The per-PDF pipeline is now Materialize + Rewrite (no Redact). Future PDFs retain source-organization names verbatim. Downstream consumers can apply their own obscuration if needed.
2. **`tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` was edited** to reflect: (a) Step 6 no longer invokes the redactor; (b) BATCH_SIZE raised from 8 to up to 40 (validated zero rejections across PDFs 06–10); (c) Step 8 smoke checks dropped leak-grep and Industry-Source histogram; (d) VOCAB path removed from derived paths; (e) Report template removed LEAK_GREP_HITS and INDUSTRY_SOURCE_IDS fields; (f) on-disk-audit guidance added between waves.
3. **`tools/pdf2md/redact_industry_sources.py` and `tools/pdf2md/industry_sources_vocab.yaml` were NOT deleted** — they're inert (no callers in the workflow) but available if needed.
4. **Already-redacted Chapter 01 outputs stay redacted (user decision).** Content is correct after the false-positive fixes. Chapter 02+ outputs will contain "Shell"/"Chevron"/"DEP" verbatim. The stylistic inconsistency between chapters is accepted — downstream consumers should treat Chapter 01 as redacted-with-canonical-name-mapping-in-`00-MASTER-INDEX.csv` and Chapter 02+ as verbatim.

---

## Task list (23 tasks)

| # | Task | Status | Notes |
|---|---|---|---|
| T0 | Phase A — Pre-flight (tooling smoke test, vocab spot-check, residue archive, dry-run gate) | **completed** | |
| T1 | Chapter 01 — overall-piping-design-standards (10 PDFs / 480 pages) | **completed** | All 10 PDFs PASS. See per-PDF status below. |
| T2 | Chapter 02 — plant-layout-and-equipment-spacing (4 PDFs / 125 pages) | **pending** ← RESUME HERE | |
| T3 | Chapter 03 — piping-materials-and-line-classes (17 PDFs / 745 pages) | pending | Largest chapter. Existing residue (`_assets/`, `*_pdf2md_work/`, stray `.md`) was archived in T0; folder is clean. |
| T4 | Chapter 04 — branch-connections-vents-drains (2 PDFs / 124 pages) | pending | |
| T5 | Chapter 05 — bolting-gaskets-and-flange-joints (3 PDFs / 56 pages) | pending | |
| T6 | Chapter 06 — pipe-supports (3 PDFs / 198 pages) | pending | |
| T7 | Chapter 07 — stress-flexibility-and-mechanical-analysis (3 PDFs / 38 pages) | pending | |
| T8 | Chapter 08 — pressure-design-and-overpressure-relief (3 PDFs / 40 pages) | pending | T0 archived prior residue. |
| T9 | Chapter 09 — welding-and-nde (6 PDFs / 100 pages) | pending | |
| T10 | Chapter 10 — shop-and-field-fabrication (6 PDFs / 141 pages) | pending | |
| T11 | Chapter 11 — pressure-testing-examination-and-cleaning (4 PDFs / 58 pages) | pending | |
| T12 | Chapter 12 — thermal-insulation-and-heat-tracing (5 PDFs / 250 pages) | pending | |
| T13 | Chapter 13 — painting-coatings-and-corrosion-protection (8 PDFs / 159 pages) | pending | |
| T14 | Chapter 14 — non-metallic-and-specialty-piping (6 PDFs / 232 pages) | pending | |
| T15 | Chapter 15 — hot-tapping-and-leak-repair (3 PDFs / 84 pages) | pending | |
| T16 | Chapter 16 — cross-country-pipelines-and-offshore (6 PDFs / 216 pages) | pending | |
| T17 | Chapter 17 — specific-service-utility-systems (11 PDFs / 273 pages) | pending | |
| T18 | Chapter 18 — safety-isolation-and-metering-philosophies (3 PDFs / 20 pages) | pending | |
| T19 | Chapter 19 — project-engineering-and-documentation (5 PDFs / 84 pages) | pending | T0 archived prior residue. |
| T20 | Phase C — Campaign assembly (concatenator + asset manifest aggregator + root validate) | pending | Requires two ★NEW tools to be written: `tools/pdf2md/concatenate_industry_practices.py` and `tools/pdf2md/aggregate_campaign_asset_manifest.py`. Designs in the origin plan. |
| T21 | Phase D — Equation audit handoff decision (inspect assembled .md for `$$…$$`; surface EQUATION_AUDIT recommendation) | pending | Defer decision until after T20 — equation density visible then. |
| T22 | Final report to user (campaign metrics, degraded list, asset count, residual blockers) | pending | |

**Folio extraction (Phase 1.5):** Origin plan scoped this as additive after Phase B, with the user-flagged caveat that it adds ~3,423 Sonnet dispatches. **Not run for Chapter 01.** Decision still open for the remaining chapters. Per AGENT_PDF2MD.md it is nullable and can be deferred to a follow-up campaign without affecting `industry-practices.md`.

---

## T1 (Chapter 01) — per-PDF outcomes

All 10 PDFs in `domain-test/domains/piping-design/_Sources/industry-practices/01-overall-piping-design-standards/`:

| PDF | Pages | Output bytes | Assets | asset_validation | Notes |
|---|---|---|---|---|---|
| 01-overall-piping-design-standards-01 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-02 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-03 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-04 | 23 | 46,069 | — | PASS | Page 1 used pdftotext deterministic fallback (multimodal vision blocked 3× by content-filter on the PIP "Purpose and Use" boilerplate). See `page_0001_assets.json` `issues` field. |
| 01-overall-piping-design-standards-05 | (small) | 20,188 | — | PASS | |
| 01-overall-piping-design-standards-06 | (medium) | 128,533 | — | PASS | One worker rejection in wave 2 (page 54), re-dispatched solo as NO_ASSETS. Lesson recorded in runbook (on-disk audit). |
| 01-overall-piping-design-standards-07 | 27 | 64,279 | — | PASS | Phillips 66 General Piping Design REP 5-1-1. Triggered vocab fix (added "Phillips HF" alias). |
| 01-overall-piping-design-standards-08 | 141 | ~278K (post-FP-fix) | 73 | PASS | Shell DEP. Largest in Ch01. **8 false-positive redactions fixed post-completion** — see "Mid-campaign discovery" below. |
| 01-overall-piping-design-standards-09 | 15 | 36,274 | 1 | PASS | Chevron Piping Manual section 100. |
| 01-overall-piping-design-standards-10 | 65 | ~138K (post-FP-fix) | 25 | PASS | Chevron Piping Manual section 300. **6 false-positive redactions fixed post-completion.** Also: an asset filename containing "shell" was renamed before the FP discovery — that rename was based on a wrong assumption and should be considered cosmetic, not a correctness fix. The current filename is `..._fig-300-21-heat-exchanger-reversal.png` (the "-shell" suffix was stripped). |

**Final Chapter 01 totals:** 10/10 PDFs, 480/480 pages, all `asset_validation=PASS`.

---

## Mid-campaign discovery — false-positive redactions

**Symptom:** PDF 10 leak_grep returned 1 hit after the standard pipeline; investigation showed the redactor had correctly substituted "Shell" → "Industry Source 08" in the markdown body of figure captions, but the asset filename was slugged BEFORE redaction and still contained "shell". I initially renamed the file and patched references — that was wrong-direction.

**Root cause:** The bare "Shell" alias in `industry_sources_vocab.yaml` (Industry Source 08) collides with engineering nouns. The corpus contains many legitimate uses of "shell" meaning the physical shell of a heat exchanger / pressure vessel / tank.

**False positives found and reverted (this session):**

PDF 10 (Chevron — 6 FPs, 0 true Shell-org refs):
- "Bottom head-to-shell seam" × 2 (vessel seam, table cell, page 9)
- "Shell and Tube" heading + "shell and tubing" + "shell-side flow" (page 48)
- "Reversal of Shell-Side Flow" (page 49 figure caption)

PDF 08 (Shell DEP — 8 FPs, 4 lines of true Shell-org refs, plus 153 legitimate "Shell Doc XX-XX" doc-number prefix substitutions):
- "tube bundles and shell/channel covers" (page 39)
- "Shell and channel box piping" + "shell-and-tube exchangers" + "shell and tube side" (page 46)
- "outward movement of the shell" × 2 (page 62)
- "equipment shell flanges" (page 68)
- "Shell and tube heat exchangers" (page 86, in Standards references list)

**Plural "shells/Shells" survived redaction correctly** via the redactor's word-boundary regex (no trailing-char match for the alias).

**Files patched to revert FPs:** Each PDF's assembled `.md`, the affected `page_NNNN.anchored.md` files, and (for PDF 10) the page 49 materialized JSON + per-PDF asset manifest. The per-page raw `.md` files (pre-anchoring) were not touched — they never had redaction applied.

---

## Files changed this session (audit)

**Instruction files modified:**
1. `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` — removed redaction from per-PDF pipeline (Step 6 + Step 8 + Report template + derived-paths block). Updated BATCH_SIZE to "up to 40" with on-disk-audit guidance.
2. `tools/pdf2md/industry_sources_vocab.yaml` — added "Phillips HF" alias to Industry Source 05. **Now inert** — vocab file no longer consulted by the workflow.

**Other files modified (content fixes from the FP discovery):**
- `domain-test/domains/piping-design/_Sources/industry-practices/01-overall-piping-design-standards/01-overall-piping-design-standards-08.md` — 8 substitutions
- `domain-test/domains/piping-design/_Sources/industry-practices/01-overall-piping-design-standards/01-overall-piping-design-standards-10.md` — 5 substitutions
- Several `page_NNNN.anchored.md` files for PDFs 08 and 10
- PDF 10 page 49 materialized JSON + manifest (the cosmetic filename rename)

**Not touched (verified clean):** `agents/AGENT_PDF2MD.md`, all skill files, all test files.

---

## How to resume

1. **Read `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md`** — that is the authoritative per-PDF runbook. It has been updated this session.
2. **Read `agents/AGENT_PDF2MD.md`** — the agent operating contract.
3. **Spot-check `domain-test/domains/piping-design/_Sources/industry-practices/NOTE.md` and `00-MASTER-INDEX.csv`** — corpus provenance and source-org → Industry Source NN mapping (mapping is now only meaningful for already-completed Chapter 01 outputs, not for future chapters).
4. **Mark T1 completed and T2 in_progress** in TaskUpdate at session start.
5. **Begin Chapter 02:** 4 PDFs / 125 pages in `domain-test/domains/piping-design/_Sources/industry-practices/02-plant-layout-and-equipment-spacing/`. Run the per-PDF runbook against each sequentially within the chapter. The per-PDF flow is: rasterize → build merged page-full briefs → dispatch up to 40 Sonnet workers per wave with on-disk audit between waves → postprocess+clean → filter_logo → materialize+rewrite (no redact) → aggregate manifest → assemble → validate. Expected final line of validate: `asset_validation=PASS`.
6. **Per-PDF resume safety:** the `manifest.json` written by `rasterize_pdf.py` includes `pdf_sha256` + `dpi`. If a per-PDF `.md` already exists with a matching SHA + DPI, the PDF is done; skip it.
7. **Chapter gate:** after all PDFs in the chapter complete, pause for compaction opportunity, then mark the chapter task completed and continue.
8. **Phase C (T20)** requires writing two new tools — see origin plan ("New tool — campaign concatenator" and "New tool — campaign asset manifest aggregator"). Don't start these until all 19 chapter tasks are completed; the relative-path conventions of `validate_assets.py` should be inspected once before authoring. Note that the concatenator and union manifest will need to span a redacted Chapter 01 + verbatim Chapters 02-19 — no special handling required, but downstream readers of `industry-practices.md` should be aware.

---

## Known good baselines

- Vocab spot-check (NOTE.md → vocab): 12 source orgs all represented in `industry_sources_vocab.yaml`. (Now inert, but kept for reference / downstream use.)
- Smoke-test: `pytest tools/pdf2md/` was clean at T0 start.
- Dispatch contract: merged `pdf2md-page-full` skill, NOT the legacy two-skill split (`pdf2md-page` + `pdf2md-page-assets`). Resuming PDFs from the old contract is NOT a concern in this corpus — Chapter 01 was the first work on it.
- Concurrency: 40-wide waves validated across PDFs 06–10 with zero rejections (one isolated mid-PDF-06 worker rejection in wave 2 handled by solo re-dispatch). The runbook captures this.
