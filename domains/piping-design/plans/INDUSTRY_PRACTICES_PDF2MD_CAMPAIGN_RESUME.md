# Industry-Practices PDF2MD Campaign — Resume Plan

**Persona:** PDF2MD (`agents/AGENT_PDF2MD.md`)
**Corpus:** `domains/piping-design/_Sources/industry-practices/` — 108 PDFs across 19 chapter folders, 3,423 total pages
**Origin plan:** `/Users/ryan/.claude/plans/read-init-md-and-agents-md-noble-dolphin.md` (in-conversation plan from the prior session)
**Paused:** 2026-05-18 after Chapter 01 complete (T1 done)
**Resume point:** T2 — Chapter 02

---

## Campaign summary

Convert 108 PDFs to per-PDF Markdown via the merged `pdf2md-page-full` skill (single multimodal vision read per page, emits both Markdown and asset JSON), then concatenate into one root document `industry-practices.md` with a unioned asset manifest.

**Per-PDF runbook:** `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` is the authoritative step-by-step. It was updated this session — see "Workflow updates before resuming" below.

**Dispatch model:** PDF2MD (the main agent) dispatches Sonnet workers directly via `Agent(subagent_type: general-purpose, model: sonnet)`. Each worker handles ONE page. Up to 40 workers per wave, all in one message for parallelism. After every wave, audit on-disk by counting `page_*.md` and `page_*_assets.json` in WORK_DIR; re-dispatch any missing page solo before proceeding (worker rejections can happen without a clear signal in the agent's return text — trust the filesystem).

**Execution rhythm:** Chapter-gated. Process one chapter at a time, in `01-…` → `19-…` order. After every chapter completes, pause at an explicit gate for compaction opportunity.

---

## Workflow updates before resuming

`tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` is the current per-PDF runbook. It captures the Chapter 01 operating lessons:

1. Use the merged `pdf2md-page-full` skill.
2. Use BATCH_SIZE up to 40 per wave.
3. Audit the filesystem after every wave by counting `page_*.md` and `page_*_assets.json` in `WORK_DIR`.
4. Re-dispatch any missing page solo before continuing.

---

## Task list (23 tasks)

| # | Task | Status | Notes |
|---|---|---|---|
| T0 | Phase A — Pre-flight (tooling smoke test, residue archive, dry-run gate) | **completed** | |
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

All 10 PDFs in `domains/piping-design/_Sources/industry-practices/01-overall-piping-design-standards/`:

| PDF | Pages | Output bytes | Assets | asset_validation | Notes |
|---|---|---|---|---|---|
| 01-overall-piping-design-standards-01 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-02 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-03 | (small, pre-this-session) | — | — | PASS | Done before current session. |
| 01-overall-piping-design-standards-04 | 23 | 46,069 | — | PASS | Page 1 used pdftotext deterministic fallback (multimodal vision blocked 3× by content-filter on the PIP "Purpose and Use" boilerplate). See `page_0001_assets.json` `issues` field. |
| 01-overall-piping-design-standards-05 | (small) | 20,188 | — | PASS | |
| 01-overall-piping-design-standards-06 | (medium) | 128,533 | — | PASS | One worker rejection in wave 2 (page 54), re-dispatched solo as NO_ASSETS. Lesson recorded in runbook (on-disk audit). |
| 01-overall-piping-design-standards-07 | 27 | 64,279 | — | PASS | |
| 01-overall-piping-design-standards-08 | 141 | ~278K | 73 | PASS | Largest in Ch01. |
| 01-overall-piping-design-standards-09 | 15 | 36,274 | 1 | PASS | |
| 01-overall-piping-design-standards-10 | 65 | ~138K | 25 | PASS | |

**Final Chapter 01 totals:** 10/10 PDFs, 480/480 pages, all `asset_validation=PASS`.

---

## Files changed this session (audit)

**Instruction files modified:**
1. `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` — updated BATCH_SIZE to "up to 40" with on-disk-audit guidance.

**Other files modified:**
- Chapter 01 output files and per-page artifacts for completed PDFs.

**Not touched (verified clean):** `agents/AGENT_PDF2MD.md`, all skill files, all test files.

---

## How to resume

1. **Read `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md`** — that is the authoritative per-PDF runbook. It has been updated this session.
2. **Read `agents/AGENT_PDF2MD.md`** — the agent operating contract.
3. **Spot-check `domains/piping-design/_Sources/industry-practices/NOTE.md` and `00-MASTER-INDEX.csv`** — corpus provenance and master file inventory.
4. **Mark T1 completed and T2 in_progress** in TaskUpdate at session start.
5. **Begin Chapter 02:** 4 PDFs / 125 pages in `domains/piping-design/_Sources/industry-practices/02-plant-layout-and-equipment-spacing/`. Run the per-PDF runbook against each sequentially within the chapter. The per-PDF flow is: rasterize → build merged page-full briefs → dispatch up to 40 Sonnet workers per wave with on-disk audit between waves → postprocess+clean → filter_logo → materialize+rewrite → aggregate manifest → assemble → validate. Expected final line of validate: `asset_validation=PASS`.
6. **Per-PDF resume safety:** the `manifest.json` written by `rasterize_pdf.py` includes `pdf_sha256` + `dpi`. If a per-PDF `.md` already exists with a matching SHA + DPI, the PDF is done; skip it.
7. **Chapter gate:** after all PDFs in the chapter complete, pause for compaction opportunity, then mark the chapter task completed and continue.
8. **Phase C (T20)** requires writing two new tools — see origin plan ("New tool — campaign concatenator" and "New tool — campaign asset manifest aggregator"). Don't start these until all 19 chapter tasks are completed; the relative-path conventions of `validate_assets.py` should be inspected once before authoring.

---

## Known good baselines

- Smoke-test: `pytest tools/pdf2md/` was clean at T0 start.
- Dispatch contract: merged `pdf2md-page-full` skill, NOT the legacy two-skill split (`pdf2md-page` + `pdf2md-page-assets`). 
- Concurrency: 40-wide waves validated across PDFs 06–10 with zero rejections (one isolated mid-PDF-06 worker rejection in wave 2 handled by solo re-dispatch). The runbook captures this.
