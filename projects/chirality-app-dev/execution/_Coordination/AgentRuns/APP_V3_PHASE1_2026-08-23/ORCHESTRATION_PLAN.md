# App v3 Phase 1 — Orchestration Plan

**Selection:** `HUMAN_SELECTED`
**Execution shape:** `TERMINAL_FAN_OUT_IN`
**Basis:** `f485b5d3b663f42be8f8cab8432ced9024d7381b`
**Branch:** `codex/app-v3-phase1-2026-08-23`
**Steer:** `plans/steers/chirality_app_v3_phase1_steer_app_2026-08-23.md`, SHA-256 `7d700af0b05c754e468d958a7580fff713f743ad789540d8c4176bf8711ed394`

## Execution graph

1. N1 drafts the exact Gate-3 amendment package.
2. Candidate whitespace runs after N1 because N2 pins N1 candidate bytes.
3. N2 drafts the Gate-4 propagation plan from the whitespace-clean N1 post-image candidates.
4. N3 is independent of N1 and N2 and may run concurrently.
5. Fan-in waits for N1, whitespace, N2, and N3.
6. A fresh independent package review runs only after fan-in. Repairs require a fresh review.
7. HELP_HUMAN performs byte verification and owns the closeout receipt/handoff; no node creates a final handoff or receipt independently.

## Dependency statement

```text
N1 -> CANDIDATE_WHITESPACE -> N2 ---+
                                      +-> FAN_IN -> FRESH_REVIEW -> HELP_HUMAN
N3 ---------------------------------+
```

## Fixed fences

- N1 content: one new Gate-3 candidate file under the frozen SCA-APP-008 folder.
- N2/N3: their steer-fixed addition-only paths.
- Run evidence: this run root only.
- No existing accepted SCA assessment file is modified.
- No `_LATEST.md`, register, contract, SOW, status, dependency, lifecycle, code, docs, frontend, plans, Root, or foreign-project write.
- No staging, commit, push, merge, or network access by N1.

## Close condition

Fan-in is eligible only when each node returns claim-calibrated evidence, the candidate write set is contained, frozen-byte invariants remain exact, and the fresh package review passes. Gate-3/Gate-4 approval and any later Gate-5 act remain owner decisions.
