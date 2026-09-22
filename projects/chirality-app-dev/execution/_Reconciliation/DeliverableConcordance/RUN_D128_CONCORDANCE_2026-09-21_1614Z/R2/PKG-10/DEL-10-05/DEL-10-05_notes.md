# DEL-10-05: forward-pass notes (R2, PKG-10)

- **Deliverable:** DEL-10-05, Domain Boundary Notices and Solver Truth Separation (DOC_UPDATE, IN_PROGRESS).
- **Basis:** frozen tree `00115c719`.
- **Rules applied:** CONVENTIONS as amended by RUN_BASIS Addenda 4–6. That covers the R4-Q4
  token, the STALE_SPECIFICATION / REMAINING_STATE_MISMATCH tie-break and the R4-Q1 subject
  test. Addendum 6 arrived mid-pass and was applied before sealing.

## 1. Census

**55 rows.**

- 36 indexed units (CLM-001..CLM-036). Split rate: 4 of 36 units were split, into 14 rows:
  - CLM-004: the conditions table, 4 rows;
  - CLM-009: REQ-001..REQ-008, 8 rows;
  - CLM-012: AC-001 plus the documentation list;
  - CLM-020: VER-001 plus the records list.
- Run-local rows: REGISTER-1..4 and STATE-1..3.

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| ALIGNED | 23 | 0 |
| STALE_SPECIFICATION | 19 | 9 (all `SEE:DEL-10-05#REGISTER-1`) |
| PARTIALLY_IMPLEMENTED | 4 | 0 |
| NOT_AUDITABLE | 3 | 0 |
| REMAINING_STATE_MISMATCH | 3 | 0 |
| AUTHORITY_CONFLICT | 2 | 1 (`SEE:DEL-10-05#CLM-004.1`) |
| DOCUMENTED_UNIMPLEMENTED | 1 | 0 |

- **SEE rows (10), counted separately:**
  - CLM-001, 007, 013, 021, 012.2, 017, 020.2, 024 and 035 point to REGISTER-1;
  - CLM-009.7 points to CLM-004.1.
- **Non-SEE rows:** 45.

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 30 |
| STATE_ASSERTION | 10 |
| CONTEXT_CLAIM | 5 |
| ACCEPTANCE | 5 |
| REGISTER_DEFECT | 4 |
| EXCLUSION | 1 |

Other counts:

- **Confidence:** HIGH 36, MEDIUM 15, LOW 4.
- **HumanDecisionNeeded other than NO:** 2 rows (CLM-004.1 and CLM-009.7, both `R4-Q1`).
- **PostReleaseBasis:** `NO` on all rows. No cited file appears in `TOUCHED_PATHS.csv`: the
  deliverable folder, the App docs, the domain modules and the runtime contracts were all
  checked.
- **Errata:** none (forward pass only).

## 2. Least-confident rows (with alternative readings)

- **CLM-009.1 (REQ-001), PARTIALLY_IMPLEMENTED, LOW.**
  - Finding: the Standard Notice omits a plain "validate". The Compact Notice omits
    certify, issue, sign and seal.
  - Alternative: ALIGNED. The TYPES §11.3 boundary-notice definition (code-validate,
    externally validate) is fully met, and the notices together cover every verb.
- **CLM-020.1 (VER-001), PARTIALLY_IMPLEMENTED, LOW.**
  - Finding: the per-line parity markers existed at migration commit `9ccbbea99` and were
    removed at finalize `b5c9a1760`. No parity report remains in the deliverable.
  - Alternative: ALIGNED. The finalize commit is the "render deterministically" step of a
    parity-checked migration.
- **STATE-2 (MEMORY.md 2026-06-16 entry), STALE_SPECIFICATION, LOW.**
  - Finding: the entry still says "active code implementation is underway", although
    `_STATUS.md:16` was repaired.
  - Alternative: the entry is dated history, not a present claim.
- **STATE-3 (`_STATUS` empty `## Remaining`), REMAINING_STATE_MISMATCH, LOW.**
  - Finding: the SoW carries four open human rulings (CLM-036), and the closure evidence is
    absent (CLM-019).
  - Alternative: ALIGNED. Items gated on a future amendment need not appear as
    deliverable-local Remaining.
- **MEDIUM rows worth a second look:**
  - CLM-004.1 and CLM-009.7 (AUTHORITY_CONFLICT). The competing readings are STALE_SPECIFICATION
    or ALIGNED, and the ALIGNED reading is recorded as `ALSO_MODULE:ALIGNED`.
  - CLM-009.3 and CLM-011 (PARTIALLY_IMPLEMENTED). The alternative is ALIGNED if verification
    of future surfaces is treated as gated rather than missing.

## 3. Register-defect summary

- **REGISTER-1: `_REFERENCES.md`, STALE_SPECIFICATION.**
  - REF-002 (CONTRACT), REF-003 (SPEC) and REF-006 (PRD) record `MATCH`, but none reproduces
    (`HASH-RECOMPUTE@00115c719`, `REFERENCE_HASHES.csv`).
  - Recorded vs recomputed: `fa8fc9dc…` vs `57411f8d…`; `01e1c75c…` vs `8b0d805b…`;
    `8649ccba…` vs `17ca3f3c…`.
  - These pins were written by `23b3879b3` (the 2026-09-12 D-GOV-43 application tranche).
    The three docs then changed again the same day (`7f1e9f387`, `9eaddb596`, `95b342519`).
  - My own recompute shows REF-001, 004, 005, 007, 009 and 010 reproduce.
  - The SoW restates "REF-006 is MATCH under D-APP-38" nine times. These are the SEE rows.
    The attribution to D-APP-38 is itself wrong: the current pin came from the D-GOV-43
    tranche.
- **REGISTER-2: `Dependencies.csv` and `Evidence_D53A`, REMAINING_STATE_MISMATCH.**
  - The notes date from D-APP-53 (2026-07-10) and are snapshot-bound (ALSO:STALE_SPECIFICATION).
  - Their decomposition line anchors have moved: PKG-10 row 270 → 288, DEL-10-05 row
    375 → 394, SOW-071 229 → 241.
  - The quoted reference SHAs match neither the current `_REFERENCES.md` nor a recompute.
- **REGISTER-3: `_DEPENDENCIES.md`, STALE_SPECIFICATION.**
  - It says "Declared Upstream/Downstream: TBD - no accepted dependency edges have been
    extracted yet" and "satisfaction lifecycle remains TBD".
  - The same file and `Dependencies.csv` record 10 extracted rows, all SATISFIED.
- **REGISTER-4: `_STATUS.md` header, REMAINING_STATE_MISMATCH.**
  - The header still names the D-APP-19 Authorization Basis and the Checking Approval SHA,
    although state is IN_PROGRESS under D-APP-54.
  - The P06 Record line says the concordance Remaining "stays open for R6", but history
    line 26 records that R6 removed it.
- **Related carrier defects, recorded as STATE rows:**
  - STATE-1: `_CONTEXT.md` still says "Claude Agent SDK / Anthropic remains the first
    concrete/current path". The D-APP-127 map shows it was not revised.
  - CLM-006: the SoW's REF-007 is the decomposition, but `_REFERENCES.md` REF-007 is the
    software-decomp workflow.
  - CLM-015, 016, 018, 020.2 and 033: dangling references to the deleted four-document kit
    (`Guidance.md`, `Procedure.md`).

## 4. Direction and cause

- **CauseTags:**

  | CauseTag | Rows |
  |---|---:|
  | NONE | 26 |
  | PRE_V3_DRIFT | 12 |
  | DOC_HYGIENE | 11 |
  | CODEX_SOLE_ENGINE | 3 |
  | LIFECYCLE_GATE_PENDING | 3 |

  - PRE_V3_DRIFT covers divergences dated 2026-07-10 to 2026-07-14: the SOW_V1 migration
    (the kit was deleted but references to it remain), the D-APP-53 register lag, and the
    stale CLM-004 WARNING row.
  - DOC_HYGIENE is used where the divergence arose after 2026-08-22: the hash drift after
    the 2026-09-12 repin.
- **`CAUSE2:` secondaries:**
  - DOC_HYGIENE on the PRE_V3_DRIFT rows CLM-004.4, 006, 015, 016, 018, 033 and
    REGISTER-3/4;
  - PRE_V3_DRIFT on CLM-020.2;
  - CARRIER_PROPAGATION on STATE-1.
- **CODEX_SOLE_ENGINE rows:**
  - CLM-004.1 and CLM-009.7 carry `GOV:D-GOV-43; GOV:D-APP-127; CTX:<done-declaration
    candidate> OOS-12`. OOS-12 is "Runtime CLI and PEC compatibility … as MVP
    prerequisites", and it is CONTEXT only.
  - STATE-1 carries `GOV:D-GOV-43; GOV:D-APP-127`.
- **LIFECYCLE_GATE_PENDING** (CLM-009.3, CLM-011, CLM-019) cites the decomposition future
  gate: `GOV:` OI-005 / DEC-006.
- **CONTEXT consulted:**
  - `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`, searched for
    domain, pec, PKG-10 and OpenPipeStress. The only relevant line sits in §9 ("Work does
    not edit unrelated domain-engine or OpenPipeStress surfaces…"). §9 is outside the
    RUN_BASIS §5 CONTEXT slice (§3, §10), so it is not cited.
  - The v3 done-declaration candidate: OOS-08 and OOS-12 name PKG-10.
- **Search behind each `NONE_FOUND`:**
  - A grep of `_DECISIONS/_REGISTER.md` for DEL-10-05, domain, pec, D-APP-38 and notice.
    This covered D-APP-19, 38, 45, 49–54, 56 and 58. It found no ruling on notice acceptance
    and no ruling moving the domain tools onto the Codex path.
  - The decomposition DEC-006 and OI-005 rows (`:599`, `:615`).
  - `docs/harness/reliance_boundary_register.md`: only RB-HOOKS and the Section 9
    domain-profile validation row mention domain.
  - CONTRACT K-DOMAIN-1..4.
  - The D-APP-127 ruling and application map.
  - The CONTEXT sources above.
- **R4-Q1 subject test (Addendum 6):**
  - CLM-004.1 is a product-behaviour claim ("tools … live"). Only the contract types and
    descriptors are LIVE; the tool handlers, registry and read tools are LEGACY_ONLY. The row
    therefore takes AUTHORITY_CONFLICT with `R4-Q1` and `ALSO_MODULE:ALIGNED`.
  - The eight REQ rows and the notice-copy rows are copy requirements on the deliverable
    text. They are judged as documentary claims, and legacy code is mentioned only in Notes,
    never as the evidence meeting the claim.
  - Consistent measure: every behavioural row is judged on the live path; every copy row is
    judged on the deliverable text.
  - No LIVE App UI or event surface presents domain output. A grep of `frontend/src/app` and
    `frontend/src/components` found only unrelated hits.

## 5. Method friction

- **Splitting CLM-012 and CLM-020.** Each unit holds one numbered AC or VER item plus a
  separate unnumbered list that dispositions differently. V-SUBITEMS only requires ≥1 row,
  but I split into `.1` (the numbered item) and `.2` (the list), reading the splitting rule
  ("holds separately numbered … items") as permitting it. **Proposal:** state explicitly
  that a unit with one numbered item and other material may split into item and remainder.
- **SEE and a unit's other content.** A SEE row must copy its target's Disposition. That
  forces a unit whose main defect is a restated register fact (for example CLM-012.2 or
  CLM-024) to carry STALE_SPECIFICATION even when the unit also holds unimplemented
  content; I mention that content in Notes only. **Proposal:** allow `SEE:` as an annotation
  on a row whose own Disposition differs, or add a separate `RESTATES:` token.
- **Tie-break rule 3 and dated notes.** Rule 3 does not settle whether a dated current-state
  note counts as a named snapshot. The case here is "D-APP-56 R5 P40 current-state note
  (2026-07-12): REF-006 is MATCH". I treated it as present-tense because it calls itself
  "current-state". **Proposal:** a note that asserts current state is present-tense whatever
  its date.
- **Scaffold hash drift.** The deliverable's hash drift was introduced by a D-GOV-43 tranche
  that re-pinned the hashes hours before the release commits changed the docs. The per-deliverable
  REGISTER row cannot express that the drift is corpus-wide and same-day. R3 may want to
  cluster these rows.

## 6. Effort

- **Files read:** about 25 in full or by range, plus scripted CSV filters.
  - Deliverable: ScopeOfWork, _STATUS, _REFERENCES, _DEPENDENCIES, Dependencies.csv,
    MEMORY, _CONTEXT, INSP-03, part of Evidence_D53A.
  - Code: domain-proposal-tools.ts header, tool-descriptor.ts domain range,
    domain-profile.ts, operation-proposal.ts, the domain-profile-registry.ts header, and
    test case names.
  - Governing slices: CONTRACT K-DOMAIN rows, PRD §8.17 and KG-016/017, SPEC §18,
    TYPES §11.3, decomposition rows.
  - Git: log, show and blame on the frozen tree.
- **Not read:**
  - `_SEMANTIC*.md` and the May `_run_records`. `_DEPENDENCIES.md` run notes rule the
    semantic files invalid evidence, and the run records hold no current-state claims.
  - Closed-run ledgers under `_Reconciliation/DeliverableConcordance/RUN_D55_*` and the
    other closed-run folders.
- **Context budget:** comfortable, not tight.
