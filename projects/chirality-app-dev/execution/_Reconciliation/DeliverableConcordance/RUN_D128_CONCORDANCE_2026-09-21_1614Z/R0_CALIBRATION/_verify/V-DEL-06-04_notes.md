# V-DEL-06-04: verifier shard notes (RUN_D128 R0 calibration, unit V)

- **Scope.** 55 SELECTION items for DEL-06-04: 51 in class a, 2 in class b, 2 in class c.
- **Evidence.** All checks were made against the frozen tree `00115c719`.
- **Git use.** Only read-only `git log`, `show` and `blame` on the frozen tree.
- **Ledger files.** No ledger, notes or reverse file was edited.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 51 | 46 | 2 | 3 |
| b | 2 | 1 | 0 | 1 |
| c | 2 | 2 | 0 | 0 |
| **Total** | **55** | **49** | **2** | **4** |

**REFUTED:**
- CLM-009.6: VerificationEvidence.
- CLM-009.10: PostReleaseBasis.

**CONTESTED (all on Disposition):**
- CLM-009.2;
- CLM-009.5;
- CLM-018.2;
- CLM-009.11.

**What held up.** The forward worker's headline finding is solid:
- The DEL-06-04 gate exists and is tested, but only on the retained Claude SDK path.
- No non-test file imports `harness/runtime.ts`.
- The App turn routes use `daemon-harness-port`.
- The Codex path is bounded only by `sandboxPolicy` and the approval requests.

**Citation checks.**
- Every cited test case name exists verbatim.
- Every cited file exists.
- The hash drift for REF-002, REF-003 and REF-006 reproduces exactly.

## (ii) Systematic patterns

### 1. PostReleaseBasis was set by assumption

The only material instance is **CLM-009.10**:
- The Codex-path line it cites (`codex-supervisor.ts:653`, cited as `:655`) is blamed to `da95ec194`.
- At the frozen basis, `app-owned-composition.ts:170-171` wires an `ApplicationToolRegistry` (also `da95ec194`). The branch that actually runs therefore returns "No active application tool binding", not the quoted string.
- The load-bearing fact is different: the frontend binds no application tools, and `runtime-service.ts:580` passes `mcpServers: []`.
- The value should be **YES**. The disposition (ALIGNED) is unaffected, because the parent of `da95ec194` returned the same "no dynamic tools" refusal (line 576).

The reverse_notes revisit was correct.

Other rows were checked and hold at **NO**:
- `sandboxPolicy` at `:104-108` and the approval handling at `:696-734` are blamed to `95364569a` (2026-09-12).
- Only line 695, the dynamic-tool dispatch, is from `da95ec194`.
- `session-store.ts:95-97` predates all four post-release commits.

### 2. Codex-native divergence: IMPLEMENTED_DIFFERENTLY vs PARTIALLY_IMPLEMENTED vs AUTHORITY_CONFLICT

The same fact pattern gets different dispositions: a full implementation on the legacy path, and nothing or only an upstream substitute on the live path.

| Disposition | Rows |
|---|---|
| IMPLEMENTED_DIFFERENTLY | 009.1, 009.6, 009.7, 009.12, 009.13 |
| PARTIALLY_IMPLEMENTED | 009.3, 009.4, 009.5 |
| ALIGNED | 009.11 |

- **CLM-009.11** is ALIGNED although it treats Codex fileChange events as sufficient. That conflicts with how 009.13 treats the raw event log.
- **CLM-009.2** is a real AUTHORITY_CONFLICT candidate:
  - unamended CONTRACT K-PATH-2 (`docs/CONTRACT.md:100`) requires writes outside the project root to be rejected;
  - GOVERNING D-GOV-43 item 4 makes danger-full-access an explicit user choice.
- For the rest of the family the conflict is only implicit, so the code fact plus R4 is acceptable.

**Proposal.**
- Add a reach column, e.g. `ImplementationReach = LIVE | LEGACY_ONLY | BOTH`, as the worker suggested. Then one disposition rule can apply across the family.
- Tighten MR-11: it applies only when the ruling explicitly names the clause.

### 3. AuthorityTier and ClaimType convention drift

- **CONTEXT_CLAIM rows carrying `LOCAL_DESIGN`:** CLM-017, 024, 026 and 029. The rule table pairs CONTEXT_CLAIM with NOT_APPLICABLE.
- **CLM-029** also carries a code disposition. Its content is normative guidance, arguably REQUIREMENT.
- **"Highest tier restated" missed:**
  - CLM-005 and CLM-025 restate CONTRACT and SPEC, so they should be GOVERNANCE_INVARIANT, not LOCAL_DESIGN;
  - CLM-009.16 cites K-REF-1 loosely.
- **STATE-1** is tiered GOVERNANCE_INVARIANT, while the other STATE_ASSERTION rows use NOT_APPLICABLE.
- None of these changes a disposition.

### Lesser patterns

- **Verification citations that do not test the claim.** On CLM-009.6 (hook failure fails closed), the cited test covers policy denials. No test injects a hook exception, so the fail-closed catch at `chirality-hooks.ts:592-603` is code-only.
- **Small line-number offsets:**
  - `sandboxPolicy` `dangerFullAccess` is at `:108`, not inside `:104-107`;
  - `:655` should be `:653`;
  - the hook catch is at `:592-603`, not `:589-600`.
- **Cancelled item/fileChange approvals** return `cancel`, not `decline`.
- **Hash-drift circularity.** CLM-016 and CLM-018.2 use "REF-006 recorded MATCH" as evidence that the HASH_MISMATCH wording is stale. REGISTER-1, in the same ledger, shows that MATCH record is itself stale.
  - The PRD drifted again under D-GOV-43, so the warning-qualification is substantively live again. That is why CLM-018.2 is CONTESTED.
  - MR-8 does not say how to treat a premise that flipped twice.
- **CauseTag split for one fact.** The REF hash drift is tagged CARRIER_PROPAGATION on CLM-001, 007, 020, 028 and 004.3, but DOC_HYGIENE on CLM-006 and REGISTER-1. Both are defensible; the split is worth normalizing.
- **DirectionEvidence mixes sources.** It cites both the CONTEXT steer and GOVERNING D-GOV-43, and for D-GOV-43 it cites the proposal path. The ruling record is `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` (RULED 2026-09-11, adopting revision 3).

**MR-2 and MR-6.** MechanicallyUnblocked is NO on every selected row. All rows are non-REM, so this is correct.

## (iii) Effort

**Files read:** about 30, by line range or grep.
- **Run inputs:** the conventions, RUN_BASIS §3 and §5, the unit's four ledger files, and CLAIM_INDEX.
- **Deliverable files:** SoW (full), `_REFERENCES`, `_DEPENDENCIES`, `Dependencies.csv`, `_STATUS`, `_CONTEXT`, Assessment.
- **Governance:** CONTRACT K-rows, SPEC §14, §15 and §25.7, the D-GOV-43 proposal and ruling record, and D-APP-43, 68 and 127.
- **Code:** about 12 files, including `codex-supervisor.ts`, `chirality-hooks.ts`, `tool-path-policy.ts`, `permission-overlay.ts`, `read-tools.ts`, `tool-descriptor.ts`, `session-store.ts` and `app-owned-composition.ts`.
- **Git:** 4 commits shown, plus blame on 3 ranges.

**Context:** moderate, not tight. The 81 KB flattened ledger dump was the largest single input.
