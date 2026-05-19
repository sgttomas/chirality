# QA Report — EQ_MWK_1956_2026-05-16_2035_proof-case

## Closure-eligibility checks (SPEC §S1–S3)

| Check | Required | Observed | Status |
|---|---|---|---|
| flagged == 0 | Yes | 4 | ⚠ OVERRIDDEN (proof case) |
| backcheck == 0 | Yes | 8 | ⚠ OVERRIDDEN (proof case) |
| unreviewed ≤ ALLOW_UNREVIEWED | Yes | 1011 | ⚠ OVERRIDDEN (proof case) |
| overlaps == 0 | Yes | 8 | ⚠ OVERRIDDEN (proof case) |

This snapshot does NOT satisfy real closure eligibility. It is labeled PROOF-CASE in Brief.md to make this explicit. A real closure of MWK_1956's audit would require completing Phase 2 (human review of all 1050 equations), Phase 3-5 (loop until flagged=0 and backcheck=0), and Phase 6 with ALLOW_UNREVIEWED=0.

## Tool invocations (SPEC §S4)

All tool calls in Phases 0, 1, 3a-brief, 3b, 3c-dry-run, and 6 used deterministic Python tools. No LLM reasoning was embedded inside a tool subprocess. LLM reasoning occurred only inside the Phase 3a TASK + equation-flag-interpret dispatch.

## Dispatch contract conformance (SPEC §S5)

The Phase 3a dispatch used:
- INIT-TASK brief rendered by tools/pdf2md/build_equation_interpret_brief.py (not hand-composed)
- TaskSkill: equation-flag-interpret
- AllowedWriteTargets: /tmp/eq_proof/interpret_out.json (single write boundary)
- Worker output: single JSON file with the contracted shape {key, page, hash, current_latex, interpreted_latex, source_note}
