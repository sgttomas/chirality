# PKG-09 W4 fan-in verification record — RUN_D55_CONCORDANCE_2026-07-11_1904Z

- **Wave:** R2 W4 (PKG-09, DEL-09-01..06; 6 deliverables). Discovery: six opus
  agents, sub-batched 4+2 per the Receipt 18 steer. Fan-in: one fable
  high-effort verification agent over the derived recheck set (every
  self-flagged ClaimID ∪ every non-ALIGNED row), plus the two mandated
  cross-deliverable handle checks. Orchestrator-authored record; all verdicts
  and resolutions below are agent judgments, never human rulings.
- **Source-state binding:** frontend/ at `fac46e33f`, byte-identical through
  HEAD `6f7c06814` (orchestrator-verified at dispatch; independently
  re-verified by the fan-in agent). Behavioral evidence bound to
  GATE-TRANSCRIPT(W1@fac46e33f). Live `shasum -a 256 docs/PRD.md` reproduces
  `ac35fba4…` = the REF-006 MATCH recorded in every PKG-09 `_REFERENCES.md`.
- **Deterministic validation:** all six ledgers 0 errors before fan-in
  (109 rows) and after corrections (113 rows) — 19-column header, §7
  dispositions, MR-1/MR-2/MR-5 checks.

> **Epistemic status: immutable, source-state-bound evidence artifact.**

## 1. Recheck coverage

47 rows rechecked (self-flagged ∪ non-ALIGNED): DEL-09-01 ×7, DEL-09-02 ×8,
DEL-09-03 ×3, DEL-09-04 ×10, DEL-09-05 ×12, DEL-09-06 ×7. Initial verdicts:
**43 CONFIRMED, 2 REFUTED, 2 CONTESTED**, plus notes-level factual findings in
four deliverables. Every refutation, contest, and notes finding was returned
to its owning discovery agent for independent re-verification; no row was
orchestrator-edited.

## 2. Refutations (2) — both accepted by owning agents after independent re-verification

| Row | Recorded → Final | Owning agent's accepted basis |
|---|---|---|
| DEL-09-01 UNMAPPED-1 | IMPLEMENTED_DIFFERENTLY → ALIGNED | The wrapper's Section 9 block has an accepted corpus mapping: DEL-09-02-RQ-012 claims the identical surface (same line ranges) as ALIGNED coverage; Guidance line 15 + decomposition v3.2 assign Section 9 to DEL-09-02. Under the Wave-4 corpus-wide mapping test a divergence disposition misfits §7. ClaimType stays IMPLEMENTED_UNMAPPED (unmapped within DEL-09-01's own kit); cross-deliverable handle retained; HumanDecisionNeeded → NO. |
| DEL-09-05 REQ-003 | ALIGNED → PARTIALLY_IMPLEMENTED | Spec line 29 is a MUST on outputs; `frontend/dist/` and `frontend/artifacts/` are absent at the source state (gitignored); sibling DEL-09-04 ledgers the identical packaging-output surface as PARTIALLY_IMPLEMENTED — plan §6 denies PASS-equivalence without verification evidence. AssessmentEvidence token also corrected OVERTAKEN → STILL CURRENT (the INSP-03 FAIL's artifact-absence state persists unchanged). Restores same-surface consistency across the package. |

## 3. Contests (2)

| Row | Outcome | Resolution record |
|---|---|---|
| DEL-09-02 RQ-015 | RESOLVED → STALE_SPECIFICATION (HIGH) | Owner adopted Reading B on its own re-derivation: the SHOULD is satisfied (manifest carries all required fields; "when available" satisfied vacuously — empty warning/blocker arrays are the honest content); its original RemainingWork contained only doc repair, contradicting PARTIALLY_IMPLEMENTED's definition; the operative defect is Specification.md line 31's now-false sentence → MR-8 tie-break → STALE_SPECIFICATION. Restores tie-break uniformity with RQ-001. |
| DEL-09-05 REQ-008 | **STANDS CONTESTED** (remains ALIGNED, MEDIUM) | Owner re-verified both readings and kept ALIGNED: SPEC §19.1 structurally separates the four required checks from a distinct "Packaging:" block; RUNBOOK §6 keeps packaging evidence separate; the deliverable's own Spec mirrors the split. Verifier's Reading B (docs/CONTRACT.md K-VALIDATE-1 line 128 lists `desktop:dist` among required checks for release-significant changes, and no packaging evidence passes at the source state → PARTIALLY_IMPLEMENTED) is acknowledged as defensible. **Deciding question routed to R3:** does K-VALIDATE-1's Enforcement list bind packaging into every release-significant acceptance, or only packaging-significant ones? Recorded verbatim on the row's RemainingWork. |

## 4. Notes corrections and coverage additions (owning-agent edits)

- **DEL-09-03** (2 accepted): REQ-002 evidence citation corrected —
  `tool:result` is asserted by `agent-engine-port.test.ts:10` (the
  PUBLIC_UI_EVENT_NAMES contract test), not `sdk-message-mapper.test.ts`
  47-112; conclusion (ALIGNED) unchanged. Coverage miss repaired: new
  **ACC-001** STALE_SPECIFICATION row for the kit's stale `86cb…`/`fb1c…`
  PRD-hash assertions (Datasheet line 32 cluster), following the sibling
  ACC-001 pattern (13 → 14 rows).
- **PRD-hash register-lag class (three additions):** the verifier found stale,
  unannotated REF-006 HASH_MISMATCH-era warnings in five of six
  `_DEPENDENCIES.md` files but ledgered in only two (09-02, 09-04); the
  owning agents' notes for 09-01/05/06 were factually wrong or silent about
  their own registers. All three owners verified and corrected:
  **DEL-09-01 REGISTER-2** (line 61 + Run History line 66; 16 → 17 rows),
  **DEL-09-05 REGISTER-1** (line 69; notes "lives in the four-document kit"
  claim retracted; 22 → 23 rows), **DEL-09-06 REGISTER-1** (line 61 plus the
  stronger present-tense `Dependencies.csv` DEP-09-06-007 Notes cell;
  20 → 21 rows). Each records the alternative dated-run-note (no-defect)
  reading as a self-flag. DEL-09-03 is genuinely clean (dated D-APP-53
  correction note — the model practice). **R3 must harmonize the class**
  (ledgered-defect vs historical-run-note reading) run-wide.

## 5. Cross-deliverable handles (verified)

- **Packaged-SDK surface (mandate from the accepted W3 DEL-08-01 refutation):**
  DEL-09-04's ledger DOES cover it — REQ-008 spans all three sub-surfaces
  including `verifyUnpackedSdkBundle` (`verify-instruction-root-integrity.mjs:382`);
  decomposition v3.2 line 363 + DEL-09-04 Spec line 32 verified. DEL-09-02
  correctly keeps out (ADQ-14 scopes the packaged-SDK proof refresh to
  ADQ-15). No ownership conflict. Handle CLOSED.
- **CI ownership (DEL-09-01 ↔ DEL-09-05):** compatible, not incompatible.
  Both identify the repo-root `.github/workflows/harness-premerge.yml` as the
  sole executed workflow (the project-local copy under
  `projects/chirality-app-dev/.github/workflows/` is a non-executing
  initial-migration duplicate — Actions runs only repo-root workflows);
  identical gate mechanics verified against the YAML; ownership with
  DEL-09-05 per decomposition line 364 (DEL-09-01 REQ-007
  IMPLEMENTED_DIFFERENTLY defers; DEL-09-05 REQ-004 owns). DEL-09-01
  REGISTER-1 (artifact-name lag `harness-section8-summary` vs live
  `harness-validation-summaries`) and DEL-09-05's disclosed-TBD dep row are
  complementary.
- **Packaging-output surface (DEL-09-04 ↔ DEL-09-05):** consistent after the
  accepted REQ-003 refutation (both PARTIALLY_IMPLEMENTED on the
  artifact-absent state).

## 6. Items routed to R3 (not resolved at W4)

1. DEL-09-05 REQ-008 standing contest — the K-VALIDATE-1
   packaging-enforcement interpretation question (§3 above).
2. PRD-hash register-lag class harmonization (§4 above) — also touches
   earlier waves' register-row practice.
3. **Cross-package (noted by DEL-09-05, verified by fan-in):** repo-root
   `.github/workflows/desktop-release-template.yml` is a live executable
   surface (`on: push tags v*` + `workflow_dispatch`) containing a
   `build-windows` job producing Windows NSIS artifacts — in tension with
   K-RELEASE-1's macOS-only posture, DEL-09-04-REQ-010, and
   DEL-09-05-EXC-005. Additional verified fact: the template's paths do not
   match this repo's layout (`working-directory: frontend` at repo root;
   artifacts under `frontend/dist-electron/*` vs actual electron-builder
   output `dist`), so its jobs as written cannot succeed against this tree —
   evidence of an unadapted template rather than an operating release path,
   but it remains an executable surface claiming a non-macOS target.
   Ownership question (DEL-09-04 packaging vs DEL-09-05 CI) rides with it.
4. DEL-09-04 UNMAPPED-1 enrichment for the R4 packet: `desktop:pack` is
   documented in `docs/BUILD_AND_RELEASE.md` (lines 62, 117, 129) as a live
   packaging-review command — the gap is deliverable/requirement ownership,
   not documentation.
5. REF-006 kit-staleness family (six ACC/REQ STALE_SPECIFICATION rows across
   the package) joins the PKG-07 R5 doc-repair tranche under the existing
   D-APP-35 authorization.

## 7. Method compliance

Spot-checked clean across all six ledgers: 19-column header, MR-1 single
tokens, MR-2 (YES only on REMAINING_WORK rows), MR-5 bare REGISTER ClaimIDs,
MR-10 vocabulary, no secret/key values anywhere, F-APP-3 respected, no test
execution, no lifecycle transitions. Zero AUTHORITY_CONFLICT / UNKNOWN /
DEFERRED_AGENT_WORKFLOW rows.

## 8. Final tally

Initial fan-in: **47 rechecked — 43 confirmed, 2 refuted, 2 contested.**
Post fan-in: both refutations accepted; 1 contest resolved by owner
(RQ-015 → STALE_SPECIFICATION); 1 standing contested (DEL-09-05 REQ-008);
4 rows added by owning agents (1 coverage ACC + 3 REGISTER); 109 → 113 rows,
re-validated 0 errors.
