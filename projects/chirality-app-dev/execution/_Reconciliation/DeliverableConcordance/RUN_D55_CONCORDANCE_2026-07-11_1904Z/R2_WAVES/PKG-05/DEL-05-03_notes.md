# R2 notes — DEL-05-03 Redacted RunLogger and Secret Hygiene (PKG-05, Wave 2)

Source state: `fac46e33f` (frontend byte-identical through HEAD `1625b396a`; `git diff` on
`src/lib/harness` and `src/__tests__` empty). Behavioral binding: `GATE-TRANSCRIPT(W1@fac46e33f)`
(typecheck exit 0; Vitest 667 passed / 4 skipped) plus named test files/cases per row.

## Census

- Total rows: 24
- By ClaimType: REQUIREMENT 13, ACCEPTANCE 2, EXCLUSION 3, IMPLEMENTED_UNMAPPED 2,
  REMAINING_WORK 2, REGISTER_DEFECT 2.
- By Disposition: ALIGNED 17, PARTIALLY_IMPLEMENTED 2 (R12, R13), STALE_SPECIFICATION 1
  (ACC-002), IMPLEMENTED_UNDOCUMENTED 2 (UNMAPPED-1/2), REMAINING_STATE_MISMATCH 2
  (REGISTER-1/2).
- Selectable REMAINING: REMAINING-2 = YES (concordance bootstrap, UNGATED); REMAINING-1 = NO
  (arbitrary-secret registry, gated on a new owner ruling).
- HumanDecisionNeeded = NEW-PACKET on 4 rows (UNMAPPED-1, UNMAPPED-2, REMAINING-1).

## R1 index gap (recorded per dispatch)

The R1 `REQUIREMENT_INDEX.csv`, `IMPLEMENTATION_SURFACES.csv`, and `VERIFICATION_INDEX.csv`
contain ZERO rows for DEL-05-03 — the known regex-parser gap. The real claim set (R1–R13,
plus datasheet-distinct ACC/EXC) was re-derived from `Specification.md` lines 22–36 and the
Datasheet Conditions/Slots. `REMAINING_INVENTORY.csv` correctly carries BOTH `## Remaining`
items (rows 27–28); `ASSESSMENT_INDEX.csv` and `DECISION_INDEX.csv` do have DEL-05-03 /
relevant-ruling rows and were used.

## Key evidence pivot: ORN-11 postdates INSP-03

INSP-03 (2026-06-21, SHA `18511e933`) rated R1/R2/R3/R4/R5/R11 PARTIAL largely on a
"no whole-product proof matrix" basis. `Evidence_ORN-11_Runtime_Redaction_Path_Matrix.md`
(2026-07-10) built exactly that matrix with per-path named fixtures, all of which exist and
pass at `fac46e33f`. Those six PARTIAL conclusions are therefore recorded OVERTAKEN and the
rows disposition to ALIGNED. R6/R8/R9/R10 (INSP-03 PASS) stay STILL CURRENT / ALIGNED.
R12/R13 PARTIAL conclusions persist (STILL CURRENT) and disposition PARTIALLY_IMPLEMENTED.

## Least-confident rows (with the reading that would flip them)

- **R1 (ALIGNED, MEDIUM).** Reads "redact secrets" as satisfied by the configured-API-key
  contract. Flip reading: if "secrets" is read to require the arbitrary configured-secret
  registry, R1 becomes PARTIALLY_IMPLEMENTED/ACCEPTED_DIVERGENCE with the gap = REMAINING-1.
- **R3 (ALIGNED, MEDIUM).** Adopts the reading that "configured secret variants" = the
  encoded/derived variants of configured API keys (raw/URL/lowercase/double/query), which are
  implemented and tested (`run-logger.ts` 19-77; `run-logger.test.ts`). Flip reading: if
  "configured secret variants" demands a non-API secret registry, R3 → PARTIALLY_IMPLEMENTED
  (gap tracked at REMAINING-1). This is the single most load-bearing interpretive call in the
  packet.
- **R4 (ALIGNED, MEDIUM).** The seven typed SDK_FAILURE classes and their redaction are all
  present in `anthropic-agent-sdk-manager.ts` (INVALID_BASE_URL 189, NETWORK_POLICY_VIOLATION
  199-245, RATE_LIMITED 626-629, auth 613, timeout 298-306, network 648-657, stream 508-512).
  Flip reading: that classifier file is co-owned with DEL-04-05 (DEP-05-03-010 PENDING); if the
  reviewer holds the full typed enumeration to be DEL-04-05's deliverable, R4 → PARTIALLY_IMPLEMENTED
  (interface-dependent).
- **R5 (ALIGNED, MEDIUM).** ALIGNED depends on ORN-11's finding that the SDK exposes no
  separate first-class debug-log sink — only hook stdout/stderr diagnostics, which are redacted.
  Flip: if a discrete SDK debug-log surface were found unredacted, R5 → PARTIALLY_IMPLEMENTED.
- **R7 (ALIGNED, MEDIUM).** R7's OR-list (budget/preview/artifact/redact) is satisfied; the
  distinct typed "withheld" outcome is absent but not required by R7. Flip: if "withheld" is
  read as mandatory, R7 → PARTIALLY_IMPLEMENTED (aligns with the R13 residual / DEL-05-05 gate).
- **R11 (ALIGNED, MEDIUM).** The "every path" completeness claim rests on ORN-11, which is
  DEL-05-03 self-evidence, not an independent release gate, and is scoped to the configured-API-key
  contract. Flip: a reviewer treating "every path" as an unmet release-quality bar would rate
  PARTIALLY_IMPLEMENTED.
- **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM).** Domain-proposal credential/cookie hygiene
  could instead be read as an instance of R6/R11 rather than unmapped; classified UNMAPPED
  because it handles a non-configured-API-key secret class the requirements do not name.

## Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH).** `Dependencies.csv` DEP-05-03-009 and
  `_DEPENDENCIES.md` (line 28 warning; Lifecycle Summary 5 PENDING) still carry REF-006
  docs/PRD.md as a PENDING HASH_MISMATCH, but `_REFERENCES.md` at `fac46e33f` records REF-006
  Expected == Actual == `ac35fba40…`, Status MATCH (resolved via D-APP-35/D-APP-38). Register
  metadata lag. Paired with the doc-side ACC-002 STALE_SPECIFICATION.
- **REGISTER-2 (REMAINING_STATE_MISMATCH).** The two dependency registers disagree on
  DEP-05-03-011 (DEL-05-02 interface): `Dependencies.csv` marks it RETIRED / NOT_APPLICABLE
  (RUL-SCC-001-RESIDUAL-001, CHANGE retired 2026-05-24), while `_DEPENDENCIES.md` still shows it
  ACTIVE / PENDING and reports ACTIVE 13 / RETIRED 0. The markdown register should read
  ACTIVE 12 / RETIRED 1.

## Cross-reference / dependency check (plan §5 provenance re-verify)

DEP rows re-checked against the live tree at `fac46e33f`: 001-005 (anchor/trace) and 006-008
(CONTRACT/SPEC/PLAN, all `_REFERENCES.md` MATCH) hold. 009 (REF-006) is now MATCH → REGISTER-1.
010 (DEL-04-05 provider bridge) and 012 (DEL-05-05 ToolResultStore, DOWNSTREAM) remain genuinely
PENDING interfaces, cited as context in R4 and R7/R13 respectively (F-APP-3 respected — no other
deliverable's execution tree was read; boundary inferred from this deliverable's own registers and
the shared source files). 011 discrepancy → REGISTER-2. 013 (final module paths / secret schema)
partially resolved for module path/API but schema-TBD persists → cited in R12.

## Method deviations

None. 19-column §6 header copied verbatim from the R0 exemplar; MR-1..MR-11 applied. No secret,
key value, or redaction fixture credential was copied into any cell (redaction behavior cited by
file/line only; the `[REDACTED_API_KEY]` token is the product's own non-secret replacement string).
No lifecycle transition proposed; R5 repairs named only as forward work.
