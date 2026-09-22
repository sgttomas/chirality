# DEL-01-03 — reverse-pass notes (worker A, pass 2)

The sealed ledger is unchanged: SHA-256 `509da4b44e91eed72d30f34299367ae180a9d2b69f1e676d7ff10390b106ba00`.

The manager named ten capability files. They were concatenated in this order: BUILD, ELECTRON, HARNESS,
ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WORKSPACE, WOVEN (452 capabilities).

## Responses

| Response | Count |
|---|---:|
| CLAIMED_BY | 0 |
| PARTIAL | 19 |
| NOT_MINE | 433 |

DEL-01-03 is a DOC_UPDATE copy-guidance deliverable, so it owns no capability outright. Its interest is
limited to the copy strings on each surface. Every PARTIAL row points to the forward row that cited or
judged those strings.

| Forward row | PARTIAL capabilities |
|---|---|
| CLM-009.1 (identity) | BUILD-009, ELECTRON-031, ROUTES-039, SHELL-008, SHELL-012, SHELL-016 |
| CLM-009.2 | ROUTES-044, SETTINGS-009 |
| CLM-009.3 | SETTINGS-002, SETTINGS-007 |
| CLM-009.4 | HARNESS-040 |
| CLM-009.5 | SHELL-038 |
| CLM-009.6 | WOVEN-022, WOVEN-035, WOVEN-042 |
| CLM-009.7 | SHELL-025 |
| CLM-009.8 | HARNESS-053 |
| CLM-009.9 | HARNESS-055 |
| CLM-024 | RTCONTRACT-019 |

RTCORE-003 (Codex as the sole engine) is evidence against STATE-1, not something the deliverable claims,
so it is NOT_MINE.

## Reach disagreements and errata

There are 3 errata rows on 2 claims. No Disposition changes.

1. **CLM-009.2, ImplementationEvidence and Notes.**
   - I tagged `api-key-settings.tsx:88` ("Anthropic API Key") as `REACH=LEGACY_ONLY` / UNREACHED.
   - It is in fact rendered on the live **not-found route**. The chain is `app/not-found.tsx:6` → AppShell →
     default-variant ShellFrame → the "Runtime & credentials" disclosure (`shell-frame.tsx:297-303`,
     rendered at `:337`). CAP-SHELL-008 records that AppShell renders the default variant on the 404 route.
   - CAP-SETTINGS-009 marks the panel `STATE=DISABLED` and cites only the woven gating. It misses this path.
     REACHABILITY.csv's module-level LIVE tag is right.
   - The Disposition stays ALIGNED: a provider-key label does not present Chirality as an Anthropic product.
     The finding is copy for a retired engine on a live page. That page is the legacy PORTAL chrome
     ("Return to PORTAL").
2. **CLM-009.6, ImplementationEvidence.**
   - I tagged `activity-shelf.tsx:38` ("Live runtime projection") `REACH=LIVE`.
   - The line is inside `ActivityShelf`, and no production component renders it. CAP-WOVEN-035 marks it
     STATE=DISABLED. The production imports are ActivityView and ActivityStrip.
   - Corrected to `REACH=LEGACY_ONLY` with UNREACHED. PARTIALLY_IMPLEMENTED still holds on the live
     replay-lens labels (CAP-WOVEN-022).

## Other capability notes checked against my ledger (agree)

- **SHELL-009:** the workspace variant returns early at `shell-frame.tsx:307`, which matches my
  citation of `:307-311`.
- **ROUTES-039:** its notes flag the stale PORTAL/PIPELINE/WORKBENCH metadata description, as my
  CLM-009.1 does.
- **HARNESS-040, -053, -055:** all LEGACY_ONLY and DISABLED. This matches my tags and the R4-Q1
  citations on CLM-009.8 and .9.
- **SETTINGS-002 and -007:** LIVE and rendered in the hosted branch, matching my tags.
- **SHELL-025:** LIVE and woven-only, matching the CLM-009.7 citation of `chat-panel.tsx:130-133`.

## Census: sealed vs errata-applied

The errata correct evidence and Notes only, so both columns are the same.

| Disposition | Sealed | Errata-applied |
|---|---:|---:|
| ALIGNED | 12 | 12 |
| STALE_SPECIFICATION | 12 | 12 |
| NOT_AUDITABLE | 8 | 8 |
| PARTIALLY_IMPLEMENTED | 7 | 7 |
| AUTHORITY_CONFLICT | 4 | 4 |
| DOCUMENTED_UNIMPLEMENTED | 2 | 2 |
| REMAINING_STATE_MISMATCH | 1 | 1 |
| **Total** | **46** | **46** |

## Coverage gaps (no forward row; for the manager)

- **Live not-found page.** The page shows the legacy PORTAL chrome with an "Anthropic API Key" panel.
  Codex is the sole live engine. No forward row judges this as retired-engine copy on a live surface. It
  is closest to STATE-1/STATE-3, but those rows concern carrier text, not UI. The owner is probably
  DEL-02-01 (shell), with DEL-01-03 review.
- **Codex/OpenAI disclosure copy.** Examples: the "Codex" activity tab and "Codex needs your input"
  (CAP-WOVEN-033, CAP-SHELL-038), and ChatGPT sign-in (CAP-SETTINGS-003). No boundary review covers it,
  and the SoW's identity boundary lists only Claude Code/Anthropic (already noted in pass 1).
- **Update wording (CAP-SHELL-015, "never claims install") vs checklist PB-08.** PB-08 covers
  release/distribution wording, but DEL-01-03 has no forward row for PB-08 conformance of update copy.
