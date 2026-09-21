# V-DEL-01-03_A verifier notes (DEL-01-03_A, ledger of record)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 6 | 5 | 0 | 1 |
| a30 (other non-ALIGNED) | 9 | 8 | 0 | 1 |
| b (ALIGNED) | 2 | 2 | 0 | 0 |
| c (reverse PARTIAL) | 5 | 5 | 0 | 0 |
| e (errata) | 3 | 3 | 0 | 0 |
| **Total** | **25** | **23** | **0** | **2** |

No verdict field was refuted. The two CONTESTED items are:
- CLM-009.7, on Disposition and HumanDecisionNeeded;
- CLM-009.4, on CauseTag only.

## (ii) Patterns

1. **Authority order applied correctly on the AUTHORITY_CONFLICT rows** (STATE-1, STATE-3, CLM-024).
   - The rows keep unamended App DIRECTIVE §2.8 above the lower PRD and CONTRACT Codex-only preambles (§0). They do not treat those preambles as overriding.
   - They route the undercut from D-GOV-43, which does not name §2.8, to AUTHORITY_CONFLICT (CONVENTIONS §1, bullet 3).
   - Checked at the frozen tree: neither the D-GOV-43 record nor D-APP-127 names App DIRECTIVE §2.8 or the key-aware default.
   - D-GOV-43 `IMPACT.md:56` is a Root DIRECTIVE row, and the App-loop list at `IMPACT.md:102-129` omits App DIRECTIVE entirely. This supports the rows; CLM-024's gloss is only imprecise.
   - R4-Q1 is cited by rule 3, because only LEGACY_ONLY code meets these claims. The exception is CLM-009.7.
2. **CLM-009.7 applies the conflict route to a copy rule.**
   - The live permission copy (`chat-panel.tsx:130-133`) names an explicit, user-selected Codex sandbox and approval mode. It does not name prompt text or an opaque default.
   - Read literally, REQ-07 is therefore met on the live path (ALIGNED, no R4-Q1).
   - The row's alternative reading is enforcement ownership (§2.9 / K-RELIANCE-2 versus D-GOV-43). That is defensible, but it fits CLM-024 better.
   - Graded CONTESTED.
3. **Reachability self-corrections.** Both sealed REACH mistakes were caught by the worker's own errata, and both errata are correct:
   - CLM-009.2: `api-key-settings` renders on the not-found route through the default-variant ShellFrame.
   - CLM-009.6: ActivityShelf is not rendered in production.
   - The forward a30 item for CLM-009.6 is graded on the errata-applied value.
4. **CauseTag on missing user-facing notices.** A `git log -S` search shows that no user-facing draft or decision-support string ever existed in `frontend/src/components`. The residual gap on CLM-009.4 therefore predates v3 (PRE_V3_DRIFT is arguable over CODEX_SOLE_ENGINE). Graded CONTESTED.
5. **CLM-009.8 and .9 (LOW).** The §2.3 legacy rule is applied literally. The vacuous-ALIGNED alternative is recorded as LEAST-CONFIDENT. Graded CONFIRMED.

**Other checks.**
- Line anchors: all verified; no drift beyond 2 lines.
- PostReleaseBasis: `app-owned-composition.ts:17-20` is outside the ranges touched by `da95ec194`. NO is correct.

## (iii) Effort

- Files read: about 30 (deliverable files, App DIRECTIVE/CONTRACT/PRD slices, the D-GOV-43 IMPACT and proposal files, the D-APP-127 and D-APP-56 records, and about 20 frontend/runtime files at the cited lines).
- Git: read-only `log -S` / `show` on the frozen tree.
- Context budget: not tight.
