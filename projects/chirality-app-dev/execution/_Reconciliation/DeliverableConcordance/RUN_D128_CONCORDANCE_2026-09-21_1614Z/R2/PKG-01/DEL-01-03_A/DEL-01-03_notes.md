# DEL-01-03 — forward-pass notes (worker A, pass 1)

Run `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, PKG-01 wave 4, double-blind worker A. Frozen basis `00115c719`.
Ledger: `DEL-01-03_claims.csv` (46 rows). There was no split worker and no pregather.

## 1. Census

Indexed units: 31 (CLM-001..CLM-031). Rows: 46 = 40 unit rows + 3 `STATE-n` + 3 `REGISTER-n`.

- **Split rate:** 1 of 31 units (3%). CLM-009 is split `.1`–`.10` because its table has one numbered row
  per requirement, REQ-01..REQ-10. The index lists no SubItems for it. CLM-013 (AC-001) and CLM-022
  (VER-001) each list only one SubItem, so each takes one row.
- **SEE rows:** 9, counted separately: CLM-006, CLM-010, CLM-030, STATE-2 and REGISTER-2 point to
  REGISTER-1; CLM-012 and CLM-016 point to CLM-008; CLM-019 and CLM-020 point to CLM-011. Every SEE row
  carries `STALE_SPECIFICATION`.

| Disposition | Rows | of which SEE |
|---|---:|---:|
| ALIGNED | 12 | 0 |
| STALE_SPECIFICATION | 12 | 9 |
| NOT_AUDITABLE | 8 | 0 |
| PARTIALLY_IMPLEMENTED | 7 | 0 |
| AUTHORITY_CONFLICT | 4 | 0 |
| DOCUMENTED_UNIMPLEMENTED | 2 | 0 |
| REMAINING_STATE_MISMATCH | 1 | 0 |

| ClaimType | Rows | Dispositions |
|---|---:|---|
| REQUIREMENT | 22 | ALIGNED 9, PARTIALLY_IMPLEMENTED 6, STALE_SPECIFICATION 3, AUTHORITY_CONFLICT 2, DOCUMENTED_UNIMPLEMENTED 2 |
| CONTEXT_CLAIM | 12 | NOT_AUDITABLE 8, STALE_SPECIFICATION 4 |
| ACCEPTANCE | 4 | ALIGNED 2, STALE_SPECIFICATION 1, PARTIALLY_IMPLEMENTED 1 |
| STATE_ASSERTION | 4 | AUTHORITY_CONFLICT 2, ALIGNED 1, STALE_SPECIFICATION 1 |
| REGISTER_DEFECT | 3 | STALE_SPECIFICATION 2, REMAINING_STATE_MISMATCH 1 |
| EXCLUSION | 1 | STALE_SPECIFICATION 1 |

Other figures:

- HumanDecisionNeeded: `R4-Q1` on 6 rows (CLM-009.7, .8, .9, CLM-024, STATE-1, STATE-3). Every other row is `NO`.
- Confidence: HIGH 21, MEDIUM 23, LOW 2.
- PostReleaseBasis: `NO` on every row. The only cited file on the touched-path list is
  `projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts`. Lines 17–20 blame to
  `95364569ae` (2026-09-12), which is not one of the four release commits.
- No errata file exists yet.

## 2. Least-confident rows

- **CLM-009.8 (REQ-08, LOW): DOCUMENTED_UNIMPLEMENTED.** The domain-truth notices exist only in
  legacy MCP domain tools (`REACH=LEGACY_ONLY`), and the live path has no domain surface.
  - *Alternative reading:* ALIGNED. The requirement applies to *future* domain surfaces, and none is live,
    so the live path conforms trivially.
  - R4-Q1 is cited by rule 3.
- **CLM-009.9 (REQ-09, LOW):** same basis and alternative as CLM-009.8.
- **Next least confident (MEDIUM):**
  - CLM-009.7, CLM-024, STATE-1 and STATE-3 (AUTHORITY_CONFLICT). The alternative reading applies
    DIRECTIVE §0 literally: an unamended DIRECTIVE outranks the amended CONTRACT and PRD preambles. That
    would make STATE-1 and STATE-3 ALIGNED and CLM-024 IMPLEMENTED_DIFFERENTLY. I did not take it,
    because D-GOV-43 is itself a GOVERNING ruling whose effect contradicts the unnamed clauses.
  - CLM-009.3 (REQ-03, ALIGNED). The alternative is IMPLEMENTED_DIFFERENTLY: the live permission copy is
    written in Codex policy terms, and DIRECTIVE §2.10 says permission modes are adapter metadata.

## 3. Register-defect summary

- **REGISTER-1 (STALE_SPECIFICATION):** `_REFERENCES.md` records REF-002 (CONTRACT), REF-003 (SPEC) and
  REF-006 (PRD) as `MATCH`, and none of the three reproduces at `00115c719` (`REFERENCE_HASHES.csv`).
  - My own recompute: REF-001 DIRECTIVE, REF-004 TYPES and REF-005 PLAN still reproduce.
  - REF-007, REF-009 and REF-010 are Root workflow files. I did not recompute them because they are
    outside the reading scope.
  - SoW CLM-006, CLM-010 and CLM-030, the checklist (STATE-2) and the dependency register (REGISTER-2)
    restate the same MATCH and point here with SEE.
- **REGISTER-2 (STALE_SPECIFICATION):** Dependencies.csv DEP-01-03-011 ("FACT: … now records REF-006
  MATCH …; dependency is SATISFIED") and `_DEPENDENCIES.md`:31 restate MATCH as current. Whether the
  dependencies remain satisfied is left open.
- **REGISTER-3 (REMAINING_STATE_MISMATCH):** the `_STATUS.md` header still gives the Authorization
  Basis as D-APP-19, but the current IN_PROGRESS state was set by D-APP-54. The field lags; nothing
  false is said about the product.
- **Stale SoW text (not register rows):**
  - Dependencies are called TBD although all 12 rows have been SATISFIED since D-APP-53 (CLM-008, CLM-012, CLM-016).
  - CT-001 is called TBD although D-APP-56 P35 ruled it (CLM-011, CLM-019, CLM-020). CLM-030 in the same
    SoW records that ruling.
- **D-APP-127 application map:** every DEL-01-03 carrier is `NO`. `_CONTEXT.md` still describes the
  SCA-APP-001 Claude/Anthropic path as current (STATE-1).
- **Minor items, noted only:**
  - `_DEPENDENCIES.md`:26–27 has machine-specific absolute paths in historical run notes.
  - `_CONTEXT.md`:52 names four-document files (`Guidance.md` etc.) that consolidation has since
    replaced. The sentence is past tense, so it is historical.
  - `frontend/src/app/layout.tsx`:59 has a metadata description that still names PORTAL/PIPELINE/WORKBENCH.

## 4. Direction and cause

**Main CauseTags:**

- CODEX_SOLE_ENGINE (8): the live engine is the stock Codex App Server. The Claude/Anthropic path,
  the persona composer, the MCP domain tools and Chirality-owned permission enforcement exist only on
  `LEGACY_ONLY` modules.
- DOC_HYGIENE (8) and CARRIER_PROPAGATION (6): hash drift after the D-GOV-43 amendments to CONTRACT and
  PRD, and D-APP-53 and D-APP-56 outcomes not copied into the SoW text.
- SHELL_REDESIGN (2): the header-less frame drops the only governed-posture subtitle; the non-approval
  notice in `workflow-detail.tsx` is not mounted.
- LIFECYCLE_GATE_PENDING (1): CLM-022, human review of the SoW candidate.
- UNRECORDED_JUDGMENT (1): CLM-017. No boundary-review record exists for any shipped release, and no
  decision records skipping it.

**Secondary causes (`CAUSE2:`):**

| Secondary | Rows |
|---|---|
| CARRIER_PROPAGATION | CLM-006, CLM-009.10, STATE-1, STATE-3, REGISTER-1 |
| DOC_HYGIENE | CLM-009.1 |
| A2_TOPOLOGY | CLM-024 |

**Records used (all `GOV:`):**

- D-GOV-43 and D-APP-127: Codex host and topology A2.
- D-APP-53: dependency reconciliation.
- D-APP-56: CT-001 ruling (P35) and the P43/P45 annotations.
- D-APP-54: lifecycle rebaseline.
- D-APP-108: SCA-APP-010 seating. It also records that the copy-table candidate for this deliverable was
  offered and not adopted.

No CONTEXT (`CTX:`) record was needed.

**Searches behind each NONE_FOUND DirectionEvidence:**

- **CLM-009.6:** grep of `_DECISIONS/_REGISTER.md` and the `plans/steers/chirality_app_v3_*` names for
  workflow-detail, "not an approval" and "boundary copy". No hit.
- **CLM-017:**
  - grep across `projects/chirality-app-dev` docs and execution for `BOUNDARY_REVIEW_CHECKLISTS`. It found
    only plans, closed concordance runs, D-APP-44/49 records and the register row. It found no completed
    review record and no reference in `docs/RELEASE_QUALITY_GATES.md` or `RELEASE_QUALITY_RUNBOOK.md`.
  - grep of `_REGISTER.md` for DEL-01-03, "product identity", "boundary copy" and "Codex-only". This found
    only D-APP-44, the D-APP-55 rows and the D-APP-108/126/127 rows, none of which addresses this deliverable.

**Authority routes on governance-invariant rows:**

- **Route 1 (MR-11, a ruling explicitly addresses the clause):** not used. No ruling names this
  deliverable's clauses.
- **Route 2 (DIRECTIVE §0 resolves):** no row needed it. Where DIRECTIVE, CONTRACT and PRD agree
  (CLM-003, CLM-009.1/.2/.5, CLM-025, CLM-028), there is no disagreement to resolve.
- **Route 3 (AUTHORITY_CONFLICT):**
  - **CLM-009.7:** D-GOV-43 has the App leave approval and sandbox policy to the user and Codex, against
    unamended K-RELIANCE-2 and DIRECTIVE §2.9.
  - **CLM-024:** D-GOV-43 against unamended DIRECTIVE §2.8, which says Chirality owns permission policy.
  - **STATE-1 and STATE-3:** D-GOV-43 plus the Codex-only preambles against unamended DIRECTIVE §2.8,
    where Claude/Anthropic is the key-aware default.
  - D-GOV-43's impact list names DIRECTIVE §5 and §7 only (IMPACT.md:56), so these clauses are
    undercut without being named. All four rows cite R4-Q1.

## 5. Method friction

- **Copy requirements on a DOC_UPDATE deliverable.** Under the subject test, "copy MUST …" names
  user-visible outcomes, so it is product behaviour and I judged it on the live UI. The same
  requirements are also met *documentarily* by the checklist.
  - *Proposed revision:* allow a `documentary` sub-tag, or give explicit guidance for guidance-only
    deliverables.
- **Conditional future-scope requirements (REQ-08/09).** Rule 3 forces R4-Q1 when the only code is
  legacy, even when the live path has no surface to which the requirement applies.
  - *Proposed revision:* a rule for vacuous conformance, or an explicit `NOT_APPLICABLE_LIVE` treatment.
- **Tie-break rule 3.** The wording "the current D-APP-38 corpus snapshot records a match" both names a
  snapshot and calls it current. I treated it as restated-as-current. The rule could say which wins.
- **Reachability at the symbol level.** `REACHABILITY.csv` tags `api-key-settings.tsx` and `shell-frame.tsx`
  LIVE, but the Anthropic key panel is never rendered from `/chat`. I tagged it `LEGACY_ONLY` and recorded
  `UNREACHED` in Notes (CLM-009.2).
- **Packaging metadata.** `frontend/package.json` matches the CODE_PATH pattern, so it needs a REACH tag
  although it is not a module. I tagged it LIVE and said so in Notes.

## 6. Effort

- About 30 files read in part: the deliverable carriers, the App DIRECTIVE, CONTRACT, PRD, PLAN and TYPES
  slices, the checklist, 3 ruling records and D-GOV-43 IMPACT, about 15 frontend and Runtime modules
  (line ranges), and the evidence pack.
- Read-only git: blame (1), log (4), show (1).
- The context budget was comfortable, not tight.

## Coverage gaps

- **Shipped copy with no owner review.** The App shipped v3.0.x with Codex/OpenAI-facing copy: sign-in,
  sandbox and permission descriptions, and a "Codex" activity tab. No DEL-01-03 boundary review covers any
  of it (CLM-017), and the SoW's identity boundary lists only Claude Code and Anthropic. It is unclear
  whether reviewing Codex/OpenAI disclosure copy belongs to DEL-01-03 or to the shell deliverables
  (DEL-02-01 copy pass). I added no forward row for it.
- **SB-02 in the shared checklist.** SB-02 (`BOUNDARY_REVIEW_CHECKLISTS.md`:46, ambient Claude settings,
  `settingSources: []`) is DEL-01-04's row and has the same engine drift. It is not dispositioned here.
