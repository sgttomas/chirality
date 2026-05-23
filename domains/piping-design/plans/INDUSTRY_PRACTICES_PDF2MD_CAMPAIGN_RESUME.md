# Industry-Practices PDF2MD Campaign — Resume Plan

**Persona:** PDF2MD (`agents/AGENT_PDF2MD.md`)
**Corpus:** `domains/piping-design/_Sources/industry-practices/` — 108 PDFs across 19 chapter folders, 3,423 total pages
**Origin plan:** `/Users/ryan/.claude/plans/read-init-md-and-agents-md-noble-dolphin.md` (in-conversation plan from the prior session)
**Last updated:** 2026-05-20 — Chapters 01–17 complete (T1–T17 done). Cumulative: 100/108 PDFs (92.6%), 3,319/3,423 pages (96.9%), zero validation failures (1 DEGRADED page on Ch17 PDF-05 p1 via pdftotext fallback after 2× content-filter blocks).
**Resume point:** T18 — Chapter 18 safety-isolation-and-metering-philosophies (3 PDFs / 20p)

---

## Campaign summary

Convert 108 PDFs to per-PDF Markdown via the merged `pdf2md-page-full` skill (single multimodal vision read per page, emits both Markdown and asset JSON), then concatenate into one root document `industry-practices.md` with a unioned asset manifest.

**Per-PDF runbook:** `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md` is the authoritative step-by-step. It was updated this session — see "Workflow updates before resuming" below.

**Dispatch model:** PDF2MD (the main agent) dispatches Sonnet workers directly via `Agent(subagent_type: general-purpose, model: sonnet)`. Each worker handles ONE page. Up to 40 workers per wave, all in one message for parallelism. After every wave, audit on-disk by counting `page_*.md` and `page_*_assets.json` in WORK_DIR; re-dispatch any missing page solo before proceeding (worker rejections can happen without a clear signal in the agent's return text — trust the filesystem).

1. Use the `pdf2md-page-full` skill.
2. Use BATCH_SIZE 6 in parallel.
3. Audit the filesystem after every wave by counting `page_*.md` and `page_*_assets.json` in `WORK_DIR`.
4. Re-dispatch any missing page solo before continuing.

---

## Task list (23 tasks)

| # | Task | Status | Notes |
|---|---|---|---|
| T0 | Phase A — Pre-flight (tooling smoke test, residue archive, dry-run gate) | **completed** | |
| T1 | Chapter 01 — overall-piping-design-standards (10 PDFs / 480 pages) | **completed** | All 10 PDFs PASS. See per-PDF status below. |
| T2 | Chapter 02 — plant-layout-and-equipment-spacing (4 PDFs / 125 pages) | **completed** | All 4 PDFs PASS. |
| T3 | Chapter 03 — piping-materials-and-line-classes (17 PDFs / 745 pages) | **completed** | Largest chapter. All 17 PDFs PASS across Chunks A–F. |
| T4 | Chapter 04 — branch-connections-vents-drains (2 PDFs / 124 pages) | **completed** | 04-01 (2p, 3 assets) PASS; 04-02 (122p, 145 assets) PASS. One content-filter retry on 04-02 p1. |
| T5 | Chapter 05 — bolting-gaskets-and-flange-joints (3 PDFs / 56 pages) | **completed** | All PASS. |
| T6 | Chapter 06 — pipe-supports (3 PDFs / 198 pages) | **completed** | All PASS. |
| T7 | Chapter 07 — stress-flexibility-and-mechanical-analysis (3 PDFs / 38 pages) | **completed** | All PASS. |
| T8 | Chapter 08 — pressure-design-and-overpressure-relief (3 PDFs / 40 pages) | **completed** | All PASS. |
| T9 | Chapter 09 — welding-and-nde (6 PDFs / 100 pages) | **completed** | All PASS. |
| T10 | Chapter 10 — shop-and-field-fabrication (6 PDFs / 141 pages) | **completed** | All PASS. |
| T11 | Chapter 11 — pressure-testing-examination-and-cleaning (4 PDFs / 58 pages) | **completed** | All PASS. |
| T12 | Chapter 12 — thermal-insulation-and-heat-tracing (5 PDFs / 250 pages) | **completed** | All PASS. |
| T13 | Chapter 13 — painting-coatings-and-corrosion-protection (8 PDFs / 159 pages) | **completed** | All PASS. |
| T14 | Chapter 14 — non-metallic-and-specialty-piping (6 PDFs / 232 pages) | **completed** | All PASS. |
| T15 | Chapter 15 — hot-tapping-and-leak-repair (3 PDFs / 84 pages) | **completed** | All 3 PASS (9+5+9 = 23 assets). |
| T16 | Chapter 16 — cross-country-pipelines-and-offshore (6 PDFs / 216 pages) | **completed** | All 6 PASS (21+12+22+16+3+18 = 92 assets). |
| T17 | Chapter 17 — specific-service-utility-systems (11 PDFs / 273 pages) | **completed** | All 11 PASS (12+11+5+14+4+0+9+14+3+2+5 = 79 assets). 1 DEGRADED page (PDF-05 p1) via pdftotext fallback after 2× content-filter blocks on PIP boilerplate. |
| T18 | Chapter 18 — safety-isolation-and-metering-philosophies (3 PDFs / 20 pages) | **pending** ← RESUME HERE | |
| T19 | Chapter 19 — project-engineering-and-documentation (5 PDFs / 84 pages) | pending | T0 archived prior residue. |
| T20 | Phase C — Campaign assembly (concatenator + asset manifest aggregator + root validate) | pending | Requires two ★NEW tools to be written: `tools/pdf2md/concatenate_industry_practices.py` and `tools/pdf2md/aggregate_campaign_asset_manifest.py`. Designs in the origin plan. |
| T21 | Phase D — Equation audit handoff decision (inspect assembled .md for `$$…$$`; surface EQUATION_AUDIT recommendation) | pending | Defer decision until after T20 — equation density visible then. |
| T22 | Final report to user (campaign metrics, degraded list, asset count, residual blockers) | pending | |

---

## How to resume

1. **Read `tools/pdf2md/PILOT_ORCHESTRATOR_BRIEF.md`** — that is the authoritative per-PDF runbook. It has been updated this session.
2. **Read `agents/AGENT_PDF2MD.md`** — the agent operating contract.
3. **Begin Chapter 18:** 3 PDFs / 20 pages in `domains/piping-design/_Sources/industry-practices/18-safety-isolation-and-metering-philosophies/`. Run the per-PDF runbook against each sequentially within the chapter. The per-PDF flow is: rasterize → build merged page-full briefs → dispatch 6 workers per wave with on-disk audit between waves → postprocess → filter_logo → materialize+rewrite → aggregate manifest → assemble → validate. Expected final line of validate: `asset_validation=PASS`. Note: `clean_anchored_pages.py` does NOT exist; that step in the original runbook is a no-op.
   - **Content-filter fallback (known recurring):** the PIP "Purpose and Use" boilerplate page in PIP-sourced PDFs (e.g., Ch01 PDF-04 p1, Ch17 PDF-05 p1) triggers a vision-API content filter that two retries cannot clear. Fall back deterministically: `pdftotext -f N -l N -layout <pdf> <work>/page_NNNN.md`, then write a `pdf2md-page-assets/v1` JSON with `run_status: "DEGRADED"`, empty `assets`, and an `issues` field naming the cause. Both files must exist before the finalize loop runs.
6. **Per-PDF resume safety:** the `manifest.json` written by `rasterize_pdf.py` includes `pdf_sha256` + `dpi`. If a per-PDF `.md` already exists with a matching SHA + DPI, the PDF is done; skip it.
7. **Chapter gate:** after all PDFs in the chapter complete, pause for human review gate, then mark the chapter task completed and continue.
8. **Phase C (T20)** requires writing two new tools — stop and plan with the user now to do this.  Review the originating plan for details on what was previously discussed to bring that forward to the user to begin with `/Users/ryan/.claude/plans/read-init-md-and-agents-md-noble-dolphin.md`

---

## Known good baselines

- Smoke-test: `pytest tools/pdf2md/` was clean at T0 start.
- Dispatch contract: merged `pdf2md-page-full` skill, NOT the legacy two-skill split (`pdf2md-page` + `pdf2md-page-assets`). 