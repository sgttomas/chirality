# DEL-07-05 concordance notes (R2 Wave-3)

Deliverable: DEL-07-05 Dependencies.csv v3.1 Reader, Writer, and Linter (PKG-07).
Source state: `frontend/` at `fac46e33f`, byte-identical through HEAD `74150b3a8`.
Behavioral verification base: `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed/4 skipped).

## Census

Total rows: 22.

By ClaimType:
- REQUIREMENT: 18 (REQ-DEL-07-05-001..018)
- ACCEPTANCE: 1 (ACC-DEL-07-05-001, 29-core-column schema width — datasheet-distinct)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-DEL-07-05-001)
- REMAINING_WORK: 1 (concordance bootstrap)
- REGISTER_DEFECT: 1 (REGISTER-1)

By Disposition:
- ALIGNED: 18
- PARTIALLY_IMPLEMENTED: 2 (REQ-010, REQ-017)
- IMPLEMENTED_DIFFERENTLY: 1 (REQ-009)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

(UNMAPPED-001 was initially IMPLEMENTED_UNDOCUMENTED and was re-dispositioned to ALIGNED
after fan-in contest; contest record below.)

## Requirement re-derivation and parser gap

`R1_INVENTORY/REQUIREMENT_INDEX.csv` scanned ZERO IDs for DEL-07-05 (the known R1
regex parser gap). The 18 REQ rows were re-derived directly from `Specification.md`
Requirements table (lines 27-46). The Datasheet restatements (Attributes/Conditions
tables) fold into the covering REQ rows per MR-4; only the "29 core columns" width is
datasheet-distinct and gets ACC-DEL-07-05-001.

## Three INSP-03 PARTIALs are now OVERTAKEN (the deliverable matured after 210b5b7427)

The assessment (2026-06-21, SHA 210b5b7427) rated four requirements PARTIAL. At
`fac46e33f` three are resolved with passing tests, so their AssessmentEvidence = OVERTAKEN:
- REQ-008 / REQ-012 retire-vs-delete: `register-writer.ts` `validateRowRetention`
  (lines 342-362, invoked 419) throws `MISSING_RETIRED_ROW`; tested at
  `dependencies-register-contract.test.ts` lines 149-191. Now ALIGNED.
- REQ-015 direct-API leaf symlink: `deliverable-contracts.ts` line 509 calls
  `assertDependencyWriteLeafIsNotSymlink` (helper 143-171); tested at
  `deliverable-contracts.test.ts` lines 493-560 (external-target and dangling symlink,
  `SYMLINK_WRITE_DENIED`, bytes preserved). Now ALIGNED.
REQ-010 (target-ID existence resolution) remains genuinely PARTIAL and STILL CURRENT.

## Register-defect summary (MR-5)

REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH): `Dependencies.csv` row DEP-07-05-026 asserts
`REF-006`/`docs/PRD.md` HASH_MISMATCH as an ACTIVE CONSTRAINT, and the four-doc kit
(Specification line 96, Datasheet line 33, Guidance C-DEL-07-05-001, Procedure line 13)
still carries PRD HASH_MISMATCH source-warnings. But `_REFERENCES.md` REF-006 now records
Status MATCH (expected=actual `ac35fba4...30bfd`), and I verified at `fac46e33f` that
`shasum -a 256 docs/PRD.md = ac35fba4...30bfd` — the mismatch is genuinely resolved. The
stale HASH_MISMATCH assertion is metadata lag (register not refreshed since 2026-05-20).
Repair is an R5 doc-repair tranche; no scope decision needed.

Only one register defect. Row-count and lifecycle counts are internally consistent:
`_DEPENDENCIES.md` reports 26 ACTIVE extracted rows and `Dependencies.csv` carries exactly
26 data rows; DepClosure `CLOSURE_D53A...` coverage.csv line 35 shows `DEL-07-05,Y,26,Y,Y`
(satisfied/covered, not among the 11 deliberately-open residuals). Per the W3 rule, the
`_DEPENDENCIES.md` Declared Upstream/Downstream "TBD" sections are human-owned declaration
sections (docs/SPEC.md §5.2) and are NOT emitted as register defects.

## Least-confident rows (self-flagged; mandatory recheck at fan-in)

All non-ALIGNED rows (REQ-009, REQ-010, REQ-017, REGISTER-1), the contested UNMAPPED-001,
plus these:

- **REQ-009 (IMPLEMENTED_DIFFERENTLY, MEDIUM; disposition CONFIRMED at fan-in).** The spec
  allows "EvidenceFile+SourceRef OR explicit location TBD" and scopes to *extracted* rows;
  the code (`register-writer.ts` 292-300) requires non-empty EvidenceFile AND SourceRef on
  *every* ACTIVE row and has no distinct location-TBD branch. Precision note (per fan-in):
  the code does not strictly foreclose the location-TBD path — a literal "TBD" string in
  both fields would pass the presence check — but the spec's alternative is not modeled as
  such, and the Origin-scoping difference (all ACTIVE rows vs active *extracted* rows) is
  still material; disposition stands. Alternative reading that flips it to ALIGNED: the
  stricter presence requirement satisfies the invariant's intent and the location-TBD
  allowance is a degenerate edge case, so the difference is immaterial.
- **REQ-017 (PARTIALLY_IMPLEMENTED, MEDIUM).** The generic runtime-options unknown-key
  warning exists and is tested (`harness/options.ts` `warnOnUnknownOpts` 70-85) but is not
  wired to the dependency reader/writer/MCP option surface. Alternative reading that flips
  it to ALIGNED: SPEC §13.1 names *runtime/tool options* generally, so the shared
  harness-options mechanism is the accepted cross-deliverable mapping and the requirement
  is met.
- **UNMAPPED-001 (ALIGNED after contest, MEDIUM) — fan-in contest record.** The
  `ANCHOR_IMPLEMENTS_NODE_COUNT_NOT_ONE` parent-anchor warning (`register-writer.ts`
  410-417) has no deliverable-local Specification requirement. Initial disposition
  (Reading A): IMPLEMENTED_UNDOCUMENTED — no accepted mapping found; I had cited only the
  dependency-extract method surface. Fan-in verification CONTESTED the row with a corpus
  citation I had not consulted: docs/TYPES.md Section 6.2 line 211, IMPLEMENTS_NODE =
  "Parent definition node; normally one per deliverable" — live ratified (v6) corpus text
  that the warning directly implements, with the "normally" wording matching the
  warning-not-error severity. Re-verified at `fac46e33f` (wording confirmed verbatim).
  Reading B (adopted): under the W3 rule that IMPLEMENTED_UNDOCUMENTED requires no accepted
  mapping ANYWHERE in the corpus, TYPES.md 6.2 is the accepted corpus mapping, so the row
  is re-dispositioned ALIGNED with a spec-refresh residual (fold the warning under REQ-006
  anchor-row discipline in Specification.md, citing TYPES.md 6.2). Deciding fact still open
  for R3: whether TYPES.md descriptive-normative wording ("normally ...") counts as an
  "accepted mapping" under the corpus-wide test — an R3-level classification question; this
  remains a standing contested row and Confidence stays MEDIUM. Reading A would flip it
  back to IMPLEMENTED_UNDOCUMENTED if R3 rules that vocabulary-table glosses are not
  mappings.
- **REQ-007 (ALIGNED, MEDIUM).** Enforcement exists (`register-writer.ts` 268-274) but no
  dedicated negative test asserts rejection of EXECUTION rows with a non-NOT_APPLICABLE
  anchor at `fac46e33f`; only valid rows are exercised. Alternative: STALE_VERIFICATION if
  the promised linter-fixture coverage is treated as required-but-absent.
- **REQ-016 (ALIGNED, MEDIUM).** Extension-column preservation is structural
  (`collectHeaders` 364-387 + reader pass-through 77-81) but no named test asserts a
  read→write→read round-trip. Alternative: STALE_VERIFICATION on the same basis as REQ-007.

## Method notes / deviations

- No behavioral tests were executed; all behavioral evidence binds to
  `GATE-TRANSCRIPT(W1@fac46e33f)` plus named test files/line anchors (MR-3).
- No DECISION_INDEX entry governs DEL-07-05 requirement claims; requirement rows carry
  `NONE_FOUND`. D-APP-53 is cited `(context)` on the dependency/register rows (REQ-008,
  REQ-012, REGISTER-1) because it reconciled the dependency corpus without adjudicating this
  hash-lag. D-APP-55 governs the REMAINING_WORK bootstrap row.
- The "linter" is not a standalone module; validation is embedded in
  `serializeDependencyRegister`/`validateRow` and reader warnings — evidence cites those.
- No secrets/hash key material beyond the already-public REF-006 digest (needed to
  substantiate REGISTER-1) appear in any cell.
