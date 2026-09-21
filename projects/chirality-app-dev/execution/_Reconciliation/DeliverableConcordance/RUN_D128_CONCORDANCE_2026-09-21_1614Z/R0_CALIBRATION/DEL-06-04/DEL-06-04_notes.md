# DEL-06-04 — forward-pass notes (RUN_D128 R0 calibration, unit F-06)

Source state: frozen tree at `00115c719`. Ledger: `DEL-06-04_claims.csv` (56 data rows). All 32
indexed units (CLM-001..CLM-032) are covered. There are no REM, REMTXT or SEC units, and
`_STATUS.md` Remaining is empty.

## 1. Census

**By ClaimType:**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 23 |
| CONTEXT_CLAIM | 13 |
| STATE_ASSERTION | 12 |
| ACCEPTANCE | 5 |
| REGISTER_DEFECT | 3 |

**By Disposition:**

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 20 |
| IMPLEMENTED_DIFFERENTLY | 17 |
| ALIGNED | 8 |
| PARTIALLY_IMPLEMENTED | 5 |
| NOT_AUDITABLE | 5 |
| STALE_ASSESSMENT | 1 |

**Other counts:**

- **CauseTag:** CODEX_SOLE_ENGINE 23, NONE 13, CARRIER_PROPAGATION 13, DOC_HYGIENE 6,
  NATIVE_DELEGATION 1. No OTHER tokens.
- **Confidence:** HIGH 26, MEDIUM 29, LOW 1.
- **HumanDecisionNeeded:** R4 on 23 rows, NO on 33.

**Split rate:** 4 of 32 units were split (12.5%), into 25 sub-rows:

- CLM-009 into 16 (one per REQ);
- CLM-004 into 3 (requirement conditions, dependency-state assertion, PRD state assertion);
- CLM-013 into 2 (traceability and AC-001);
- CLM-018 into 2 (checks and PRD-warning row).

The file also has 5 run-local rows: REGISTER-1..3 and STATE-1..2.

**Headline finding.** The DEL-06-04 gate is intact and tested at the frozen basis. It
includes:

- `frontend/src/lib/harness/chirality-hooks.ts` and `tool-path-policy.ts`;
- `permission-overlay.ts`;
- the mutating MCP wrapper in `mcp/read-tools.ts`.

The gate is reached **only on the retained Claude Agent SDK path**, through
`harness/runtime.ts` → `ClaudeAgentSdkManager` → `sdk-options-builder.ts` →
`createChiralityToolHooks`.

The App's production turn routes use `lib/runtime-client/daemon-harness-port.ts`, which
goes to the Runtime service and then Codex. No App route imports `harness/runtime.ts`.

On the Codex path (`projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts`),
native file changes are bounded only by the user-chosen Codex sandbox and approval policy:

- **Sandbox:** `workspaceWrite` with `writableRoots: [cwd]`, or `read-only`, or
  `dangerFullAccess`.
- **Approvals:** fileChange/applyPatch approval requests wait for a user verdict.

The Codex path has **no** instruction-root denial, symlink-write rejection, Chirality
exact-edit check, hard-deny input or Chirality provenance hook.

## 2. Least-confident rows

- **DEL-06-04#CLM-009.5 (REQ-005 exact edit, LOW).** Recorded as PARTIALLY_IMPLEMENTED.
  - **Alternative reading:** IMPLEMENTED_DIFFERENTLY. Upstream Codex `apply_patch` context
    matching may be an equivalent exact precondition, but that behavior is in the Codex
    binary, outside the evidence roots.
  - D-APP-43 3B framed exact-edit on SDK `Edit`.
- **The IMPLEMENTED_DIFFERENTLY family (CLM-003, 004.1, 008, 009.x, 013.2, 018.1, 022,
  025, 029, 030; MEDIUM).**
  - **Alternative reading 1:** STALE_SPECIFICATION under MR-11. D-GOV-43 item 4 makes
    approval and sandbox the user's choice ("permissionMode grants nothing by itself"), and
    item 8 preserves upstream tool behavior. Both are GOVERNING and would stand over the
    untranscribed SoW text.
  - **Alternative reading 2:** AUTHORITY_CONFLICT. App `docs/CONTRACT.md` K-PATH-2,
    K-PATH-3, K-ROOT-2, K-HOOK-1 and `docs/SPEC.md` §15.2 were left unamended in the
    D-GOV-43 amendment pass, while item 4 retires the App's power to veto the Codex
    configuration.
  - I did not choose between the governing sources. I recorded the code fact
    (IMPLEMENTED_DIFFERENTLY) with HumanDecisionNeeded = R4.
- **REQ-003 and REQ-004 (CLM-009.3/009.4).** Recorded as PARTIALLY_IMPLEMENTED, not
  IMPLEMENTED_DIFFERENTLY, because the Codex path has no equivalent mechanism.
  - Instruction-root protection there is only incidental: the instruction root lies outside
    `cwd` under workspace-write.
  - The alternative is to treat them like the rest of the family.
- **CLM-009.10 (REQ-010) and CLM-009.11 (REQ-011), ALIGNED MEDIUM.**
  - REQ-010 is conditional ("before mutation behavior is enabled"). The Codex path enables
    no Chirality write tools: the App binds no application tools. One could instead read
    this as vacuous and so IMPLEMENTED_DIFFERENTLY.
  - REQ-011: atomicity is proven for Chirality-owned writers, but not for Codex-native
    writes.
- **CLM-032 (D-APP-68 managed child), NATIVE_DELEGATION.** CODEX_SOLE_ENGINE is an equally
  good cause.

## 3. Register-defect summary

- **REGISTER-1.** `_REFERENCES.md` records REF-002 (CONTRACT), REF-003 (SPEC) and REF-006
  (PRD) as ActualSHA = ExpectedSHA, `MATCH`. At the frozen tree, all three hash
  differently (`57411f8d…`, `8b0d805b…`, `17ca3f3c…`); each was amended under D-GOV-43 on
  2026-09-12.
  - This makes every "REF-006 is MATCH under D-APP-38" carrier note stale: CLM-001, 004.3,
    007, 020, 028 and 009.16.
  - REF-001, REF-004, REF-005 and REF-007/009/010 still match.
- **REGISTER-2.** `_DEPENDENCIES.md` "Declared Upstream/Downstream: TBD - no accepted
  dependency edges" sits beside a 10-row extracted register (DEP-06-04-007 and -008 are
  PENDING). SoW CLM-004.2 repeats the stale claim.
- **REGISTER-3.** `_STATUS.md` "Last Updated 2026-07-12" predates its own 2026-07-19
  History entry. This is low impact.

## 4. Direction and cause

- **CODEX_SOLE_ENGINE (23 rows)**, explained by:
  - `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md`
    (CONTEXT);
  - GOVERNING D-GOV-43 items 4 and 8
    (`docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md`);
  - the Root `docs/AGENT_WORKFLOW_RUNTIME.md` permissionMode paragraph;
  - App application D-APP-127, cited "(context)" because it does not address PKG-06.

  No direction record says whether K-PATH, K-ROOT and K-HOOK apply to Codex-native file
  changes. Hence R4.
- **CARRIER_PROPAGATION (13 rows).** The ADQ-11/D-APP-43 closure (2026-06-21) reached
  MEMORY, `_DEPENDENCIES.md` and the Assessment, but never replaced the SoW's TBD cells
  (CLM-005, 012, 016, 017, 019, 026). The D-APP-56 P40 MATCH carrier notes also became
  stale after D-GOV-43.
- **DOC_HYGIENE (6 rows):** the reference register, the dependency register, `_STATUS.md`
  header, the garbled CLM-031 conflict row, and CLM-006.
- **STATE-1.** `_CONTEXT.md` still says "Claude Agent SDK / Anthropic remains the first
  concrete/current path" and names four kit files that no longer exist.
- **STATE-2.** Assessment INSP-03 is STALE_ASSESSMENT. Its PASS rows are scoped to the SDK
  path, and one cited path (`frontend/src/lib/harness/tool-descriptor.ts`) moved to
  `projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts`
  (RUNTIME_EXTRACTION).
- **UNRECORDED_JUDGMENT: not used.** The engine divergence is covered by recorded
  direction; only its consequence for PKG-06 invariants is unruled.

## 5. Method friction (R0 input)

1. **Live path vs legacy path.** The conventions have no way to say "implemented and
   tested, but on a code path the product no longer uses". I used IMPLEMENTED_DIFFERENTLY
   plus Notes. A small column or token would make this countable, e.g.
   `ImplementationReach = LIVE | LEGACY_ONLY | BOTH`.
2. **GOVERNING vs GOVERNING tension.** When a GOVERNING ruling (D-GOV-43) implicitly
   undercuts unamended GOVERNING invariants (CONTRACT K-PATH-3, SPEC §15.2), MR-11 and
   AUTHORITY_CONFLICT pull in different directions.
   - **Proposal:** MR-11 applies only when the ruling *explicitly* addresses the clause.
     Otherwise use AUTHORITY_CONFLICT, or the code-fact disposition with R4, as I did.
3. **PostReleaseBasis** cannot be determined without git: I cannot tell whether
   `codex-supervisor.ts` lines were touched by `da95ec194`/`cb08dbe2f`/`9ecbdecdf`/`ccb95e06a`.
   I set NO throughout.
   - **Proposal:** the manager supplies a per-file list of paths those commits touched.
4. **DirectionEvidence for GOVERNING records.** The column is defined over CONTEXT records,
   but the best explanation here is itself GOVERNING (D-GOV-43). I cited both, labelled.
5. **Stale-hash evidence.** VerificationEvidence for hash-drift rows uses
   `RUN-INSPECTION@00115c719` (a `shasum` of the frozen tree). An explicit
   `HASH-RECOMPUTE@<sha>` token would be clearer.

## 6. Effort

- **Files read:** about 30 in full or in part:
  - 9 deliverable files and the assessment;
  - 4 run files;
  - about 12 code and test files by line range or grep;
  - App CONTRACT/SPEC sections;
  - the D-APP-38, D-APP-43 and D-APP-127 rulings and register rows;
  - the D-GOV-43 proposal and Root AGENT_WORKFLOW_RUNTIME excerpts.
- `_SEMANTIC*.md` and `_run_records/` were not read.
- **Context:** moderate, not tight. The SoW (489 lines) was the largest single read. A
  deliverable of this size, with a 16-requirement table, fits comfortably in one worker.
