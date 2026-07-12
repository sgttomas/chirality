# DEL-01-02 concordance notes — R2 Wave 5 (PKG-01)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; source state frontend/ at
`fac46e33f` (byte-identical through HEAD `242900ae9` per W5 dispatch);
method: pinned plan §§6–7 @ `551f84ef6` + `R2_METHOD_ADDENDUM.md` MR-1..MR-11.

## Census

Rows: **33** total.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 25 |
| ACCEPTANCE | 2 |
| EXCLUSION | 4 |
| REMAINING_WORK | 1 |
| REGISTER_DEFECT | 1 |

By Disposition:

| Disposition | Count |
|---|---:|
| ALIGNED | 15 |
| STALE_ASSESSMENT | 9 |
| STALE_SPECIFICATION | 6 |
| PARTIALLY_IMPLEMENTED | 2 |
| REMAINING_STATE_MISMATCH | 1 |

(Post-fan-in: RBR-014 moved STALE_ASSESSMENT → STALE_SPECIFICATION; see the
fan-in resolution note below.)

## Headline findings (register-says-X vs product-enforces-X)

1. **The register artifact exists and its enforcement claims are live** — the
   INSP-03 picture (register missing; 24 dependency rows unsatisfied; REF-006
   hash mismatch) is wholly overtaken. Every P0 enforcement surface the
   register names was spot-verified against the live tree, and the register's
   PromptOnlyAllowed=NO / SDKDefaultOnlyAllowed=NO posture is 13/13 true.
2. **Four register enforcement-surface citations are stale paths**
   (`frontend/src/lib/harness/{agent-engine-port,event-schema,tool-descriptor,tool-catalog}.ts`
   → now `frontend/packages/harness-contract/src/*` after the D-APP-48-era
   extraction). Enforcement itself is live at the new paths; the pointer drift
   was already observed in `Evidence_D53A_...` lines 60-65 but is in no
   `## Remaining`. Carried on RBR-001 (PARTIALLY_IMPLEMENTED) and RBR-025.
3. **Corpus-version label lag**: kit and register hardcode "D-APP-38 corpus
   v1" while the live corpus is **v6**; `_REFERENCES.md` hashes are v6-current
   (reproduced by live recompute this run), so substance is current and only
   the labels are false. Carried on RBR-021 (STALE_SPECIFICATION).
4. **Two "future/TBD" Section 9 IDs are implemented**
   (`section9.reliance_boundary_register`, `section9.sdk_session_link_resume`;
   plus `section9.domain_profile_validation` absent from the Datasheet index).
   Kit says unimplemented; manifest + script + gate-passing tests say
   implemented. Carried on RBR-007 and ACC-002.

## Fan-in resolution note (W5 verifier round-trip)

- **RBR-014 contest RESOLVED — flip accepted (STALE_ASSESSMENT →
  STALE_SPECIFICATION).** I re-verified the deciding fact myself before
  accepting: `session-manager.ts` line 10 sets `DEFAULT_MODE = 'direct'`,
  which `normalizeHarnessPermissionMode` (permission-overlay.ts lines 57-71)
  falls through to `'ask'`; workspaceWrite auto-allows Bash after hooks
  (lines 141-168). So register lines 50 and 110 flatly assert "Bash …
  denied by default" as CURRENT handling while the live default-mode
  decision is `ask` and the until-clause conditions are satisfied
  (D-APP-04 lane, D-APP-43 closure). A live register surface carrying
  now-false wording means live surfaces do not agree, which under MR-1
  removes the STALE_ASSESSMENT reservation; MR-8 then classifies the flat
  now-false kit/register text as STALE_SPECIFICATION. INSP-03's overtaken
  PARTIAL is still recorded in AssessmentEvidence (OVERTAKEN token).
- **RBR-021 enumeration gap accepted**: register lines 112 ("Current corpus
  is v1 and MATCH" — flatly false at v6) and 122 (cross-check "preserve
  D-APP-38 corpus v1") added to the RBR-021 RemainingWork repair
  enumeration alongside line 9; no new row (same accepted fact class).

## Least-confident rows (mandatory self-flagging)

- **RBR-014 (STALE_SPECIFICATION, MEDIUM — contest resolved at fan-in, see
  above)** — retained flag: the residual uncertainty is whether "denied by
  default" could still be defended as shorthand for "denied outside
  explicitly granted modes"; I judge the `ask`-default fact defeats that
  defense, so the row is no longer contested from my side.
- **RBR-024 (STALE_SPECIFICATION, MEDIUM)** — I treated "shall remain TBD
  until downstream deliverables produce inspectable artifacts" as overtaken
  because the artifacts exist and the register correctly fills paths.
  Alternative reading: the "until" clause is self-resolving, the register
  behaved exactly as required, and remaining TBDs (RB-HUMAN-GATE ValidationID)
  are legitimate → ALIGNED.
- **RBR-022 (STALE_ASSESSMENT, MEDIUM)** — the row-trace mechanism is live and
  I pushed the stale "v1" label entirely onto RBR-021. Alternative reading:
  the version label is itself part of the row-level trace, so RBR-022 should
  also be STALE_SPECIFICATION rather than only assessment-stale.
- **ACC-001 (STALE_SPECIFICATION, MEDIUM)** — Procedure.md line 12 flatly
  says "current state is CHECKING" (false since D-APP-54). Alternative
  reading: the Prerequisites table is a run-time snapshot record of the
  drafting run, hence historical context, not a current-state claim → no row
  needed (drop to note).
- **REGISTER-1 (REMAINING_STATE_MISMATCH, LOW)** — REF-007's machine-absolute
  path is an internal convention inconsistency that binds a different checkout
  than the reviewed tree. Alternative reading: deliberate scaffold convention
  for out-of-project (repo-root) sources, hash MATCH reproduces from the
  reviewed tree, therefore informational only and not a register defect.
- **RBR-025 (PARTIALLY_IMPLEMENTED, MEDIUM)** — alternative reading: the
  requirement demanded a post-generation cross-check, which occurred and is
  recorded; keeping it current is maintenance, not partial implementation →
  ALIGNED with RemainingWork.

The nine STALE_ASSESSMENT rows all follow the R0 DEL-02-01 REQ-001 pattern and
the W3-settled superseding-note test: `Assessment_INSP-03_DEL-01-02.md`
carries **no ADQ superseding note**, so its PARTIAL/FAIL conclusions (all
premised on the then-missing register) still read as current truth while the
live surfaces agree.

## Register-defect summary

- 1 defect row: **REGISTER-1** (`_REFERENCES.md` REF-007 machine-absolute
  path; content hash currently reproduces from the reviewed tree — low
  severity, see self-flag).
- `Dependencies.csv` re-verified live this run: 24 rows, unique IDs, all
  ACTIVE/SATISFIED, class/direction counts (6 ANCHOR-UP / 7 EXEC-UP /
  11 EXEC-DOWN) exactly match the `_DEPENDENCIES.md` summary tables; the
  D53A snapshot was used as provenance baseline only. No stale file paths in
  Dependencies.csv notes (the D-APP-53 pass already cites the
  packages/harness-contract locations). Declared Upstream/Downstream sections
  point at the extracted register ("See Dependencies.csv"), not bare TBD — no
  defect per the Wave-5 rule.

## Method notes / deviations

- **R1 parser gap applies**: `REQUIREMENT_INDEX.csv` contains zero rows for
  DEL-01-02 (spec uses `RBR-nnn` IDs). The 25-claim set was re-derived
  directly from `Specification.md` lines 29-53 per the brief.
- No tests executed; behavioral evidence binds to
  `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4
  skipped; `reliance-boundary-register.test.ts` pass is visible at transcript
  line 14). Register/kit content checks use `RUN-INSPECTION@fac46e33f`; hash
  claims were re-verified by live `shasum -a 256` recompute this run
  (values compared, never copied beyond the already-public register cells).
- "No test exists"-type negative claims (RBR-018 approval-claiming UI copy)
  were backed by a real grep over `frontend/src/**/*.tsx` at the source state
  (no hits); copy assertions are owned by sibling DEL-01-03 per decomposition
  v3.2 — cross-deliverable handle noted instead of an
  IMPLEMENTED_UNDOCUMENTED row.
- No IMPLEMENTED_UNMAPPED rows: all material register/test content maps to
  RBR requirements or to ruled decisions (`section9.domain_profile_validation`
  → D-APP-51/D-APP-52 + DEL-09-02 ownership of Section 9 additions; the kit
  lag it exposes is carried as ACC-002 STALE_SPECIFICATION rather than an
  unmapped-behavior claim).
- No AUTHORITY_CONFLICT and no DEFERRED_AGENT_WORKFLOW rows arose.
- Write scope respected: exactly this file and `DEL-01-02_claims.csv`.
