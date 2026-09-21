# V-DEL-06-04 — verifier notes (DEL-06-04)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 19 | 16 | 2 | 1 |
| a30 (30% of other non-ALIGNED) | 12 | 5 | 2 | 5 |
| b (ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse) | 3 | 3 | 0 | 0 |
| **Total** | **36** | **26** | **4** | **6** |

All four REFUTED verdicts are at field level. No Disposition was refuted.

## (ii) Systematic patterns

1. **The AUTHORITY_CONFLICT / R4-Q1 cluster holds.** Examples: CLM-003, CLM-009.1–.4, .6, .7, .9, .13, CLM-022 and CLM-025.
   - App CONTRACT K-PATH-2 (line 100), K-PATH-3 (101), K-ROOT-2 (52), K-HOOK-1 (99) and SPEC 15.1/15.2 are unamended.
   - K-UNTYPED-1 (line 128), D-GOV-43 and D-APP-127 re-express the envelope as a user-chosen Codex policy without naming those clauses. D-APP-127 has no K-PATH, K-HOOK or SPEC 15 reference.
   - The live path maps `bypass` to `danger-full-access` with approval `never` (`delegated.ts:322-331`, `chat-panel.tsx:129-134`). DIRECTIVE §0 does not resolve the conflict, so grading key 4 applies. R4-Q1 is the right named question.
   - All live and legacy line anchors reproduce at `00115c719`. Every cited test case exists. PostReleaseBasis NO is correct: the relied-on `codex-supervisor.ts` lines 40, 104-110, 259-261 and 719-728 lie outside every TOUCHED_PATHS range.
2. **MR-8(iv) snapshot contest on the REF-006 "MATCH under D-APP-38" note** (CLM-001, CLM-004.1, CLM-006, CLM-007).
   - The rows take STALE_SPECIFICATION and cite REGISTER-1.
   - The text is labelled a "current-state note", which supports MR-8(i). But the MATCH is true of the recorded D-APP-38 snapshot, which supports MR-8(iv). By grading key 5 the verdict is CONTESTED. R0 raised the same contest on this unit.
   - CLM-004.7 is a related case: STALE_SPECIFICATION versus REMAINING_STATE_MISMATCH. The SoW row accurately restates `_DEPENDENCIES.md` TBD text, which lags the v3.1 register.
3. **LatestDecision is NONE_FOUND while DirectionEvidence is GOV:D-GOV-43** (CLM-009.12, CLM-009.14). Under MR-7 the value should be at least `D-GOV-43 (context)`, so these rows are REFUTED on LatestDecision.
4. **Wrong line anchor** (CLM-004.2, CLM-009.9). `permission-overlay.ts:224-228` is the coordination-tool (control-plane) mode gate, not the write/edit gate. The readOnly write deny is at `:285-291`, and the workspaceWrite allow-after-hooks is at `:262-270`. These rows are REFUTED on ImplementationEvidence; the Disposition holds.
5. **Contested disposition on CLM-032.1** (managed-child scopes, D-APP-68 item 3 naming DEL-06-04). K-UNTYPED-1 governs only native descent, and no ruling retires managed delegation, so the row could equally be DOCUMENTED_UNIMPLEMENTED with R4-Q1 on the legacy-only rule rather than AUTHORITY_CONFLICT.

Minor observations that do not change any verdict:
- CLM-009.5: DOCUMENTED_UNIMPLEMENTED follows the §2.3 legacy-only rule. The self-flagged alternative is recorded. The module note is verified: line 264 denies only when the match count is 0, so uniqueness is not checked.
- CLM-004.4: ALIGNED at module level is sound. The live runtime tools are read or control only (`runtime-method-service.ts:413-414,486`) and `mcpServers` is `[]` (`runtime-service.ts:580`), so no live Chirality MCP write tool bypasses policy.
- CLM-009.12: PARTIALLY_IMPLEMENTED is also arguable, because there is no evidence of a record for silent sandbox denials.
- CLM-030: the Examples table could have been split. Its GOVERNANCE_INVARIANT tier is accepted by inference from the restated K-clauses.

## (iii) Effort

- Files read: about 30. These were the rulebook, RUN_BASIS, the selection, the ledger rows, reverse rows, three capability rows, and REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES and DECISION_HITS.
- Deliverable files: SoW, `_DEPENDENCIES`, `Dependencies.csv`, `_CONTEXT`, MEMORY and the INSP-03 assessment.
- Code: `codex-supervisor`, `delegated.ts`, `chat-panel`, `chirality-hooks`, `tool-path-policy`, `permission-overlay`, `sdk-options-builder`, `read-tools`, `atomic-write`, `delegated-engine-adapter`, `agent1-run-coordinator` and `runtime-method-service`, each read over line ranges.
- Governance: App CONTRACT and SPEC 15/16, and the D-GOV-43, D-APP-127, D-APP-43 and D-APP-68 records.
- Git: none needed; blame was settled from TOUCHED_PATHS ranges. The context budget was adequate.
