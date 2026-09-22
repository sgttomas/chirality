# DOC-RQGATES notes (EXT item 4, `docs/RELEASE_QUALITY_GATES.md`)

## 1. Census

- 23 rows over 14 indexed units (`#0`..`#13`). Coverage is complete.
- **ClaimType:** STATE_ASSERTION 14, REQUIREMENT 8, CONTEXT_CLAIM 1.
- **Disposition:** ALIGNED 14, STALE_SPECIFICATION 6, PARTIALLY_IMPLEMENTED 1, AUTHORITY_CONFLICT 1,
  NOT_AUDITABLE 1.
- **Confidence:** HIGH 7, MEDIUM 16.
- **HumanDecisionNeeded:** NO 20, R4-Q1 2 (`#2.3`, `#6`), R4-Q5 1 (`#5`).
- **Split rate:** 1 of 14 units split (7%). `#2` is the gate-routing table: 8 table rows plus 2 prose rows
  (`.9` mixed changes, `.10` the D-APP-38 authority-doc reconciliation).
- **SEE rows:** 0.
- **RELEASE_PROCESS_NOT_RUN:** `#12` (attestation and a wider release matrix).
  - The packaging gate did run for v3.0.0 (`#10`).
  - The release-quality wrapper runs in CI through `harness-premerge.yml`, as evidence only.

## 2. Least-confident rows

No rows are LOW. The MEDIUM rows most open to another reading:

- **`#5`, AUTHORITY_CONFLICT (R4-Q5).**
  - The last bullet restates unamended K-ENGINE-4.
  - §7 of the same document restates the D-GOV-43 rule that payloads are carried through.
  - Alternative: STALE_SPECIFICATION, if R4-Q5 is ruled for "stored as received".
- **`#6`, STALE_SPECIFICATION (R4-Q1).**
  - The deny-until-authorized guarantee is met only by legacy harness code. The Codex path applies the user's
    approval and sandbox choice.
  - Alternatives are recorded in Notes: `ALSO:IMPLEMENTED_DIFFERENTLY` and `ALSO_MODULE:ALIGNED`.
  - The row could also become AUTHORITY_CONFLICT if unamended CONTRACT permission invariants are held to conflict
    with D-GOV-43. I did not verify that in CONTRACT.
- **`#2.10`, PARTIALLY_IMPLEMENTED.**
  - The reconciliation tool exists.
  - REFERENCE_HASHES shows 51 of 54 deliverables with recorded MATCH hashes that no longer reproduce.
  - Alternative: DOCUMENTED_UNIMPLEMENTED, if the rule is read as "must run after every authority edit".
- **`#7` and `#13`, ALIGNED.** Two claims were taken from the capability files rather than re-read:
  - SSE keepalives;
  - socket permissions and the absence of a TCP listener.

## 3. Register-defect summary

None. This document has no register.

## 4. Direction and cause

- **CauseTags:**
  - CODEX_SOLE_ENGINE 6: routing examples, permission gate, runtime-contract bullet, network posture, open
    decisions;
  - CREDENTIAL_CUSTODY 1 (`#2.5`);
  - DOC_HYGIENE 1 (`#2.10`).
- **CAUSE2:**
  - CODEX_SOLE_ENGINE on `#2.5`;
  - CREDENTIAL_CUSTODY on `#8`;
  - V3_RELEASE_SCOPE on `#12`.
- **GOVERNING sources:** D-GOV-43 (App CONTRACT line 17: K-NET-1 and K-RELEASE-1 read with D-GOV-43 items 1
  and 4) and D-APP-127.
- **CONTEXT source:** `PUBLIC_RELEASE_20260913.md`.
- **NONE_FOUND (`#2.10`).** Search: `_DECISIONS/_REGISTER.md`, grepped for "reconcil" and "corpus", found only
  D-APP-38. RUN_BASIS §5 notes a 2026-09-19 work-graph deferral of authority-corpus drift, but that record is
  not a listed CONTEXT source.
- **Wider observation for the manager.** CI premerge (Section 8) runs against `scripts/controlled-ci-runtime.ts`,
  which composes the legacy stub engine. The harness-workflow gate's premerge evidence therefore exercises the
  legacy adapter, not Codex. This bears on R4-Q1 and R4-Q2.

## 5. Method friction

- **One section can restate two GOVERNING clauses in tension.** §5 restates K-ENGINE-4 while §7 restates the
  D-GOV-43 event rule. I used AUTHORITY_CONFLICT with R4-Q5 on the §5 row only, and left §7 ALIGNED.

## 6. Effort

- Evidence was shared with DOC-BUILDREL. In addition I read:
  - `REFERENCE_HASHES.csv`, by script;
  - the ROUTES capabilities, by grep;
  - CONTRACT K-ENGINE-4 and K-RELEASE-1, by grep.
- The context budget was comfortable.
