# DEL-05-05 R2 concordance notes — ToolResultStore and Session Artifacts

Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`. Source state: `4c8ed8907` (frontend
byte-identical through `fac46e33f`; behavioral verification cites
`GATE-TRANSCRIPT(W1@fac46e33f)` per MR-3). Discovery is read-only.

## Census

Total rows: 21.

By ClaimType:
- REQUIREMENT: 14 (REQ-001..014)
- EXCLUSION: 3 (EXC-001..003)
- IMPLEMENTED_UNMAPPED: 1 (UNMAPPED-1)
- REMAINING_WORK: 2 (REMAINING-1, REMAINING-2)
- REGISTER_DEFECT: 1 (REGISTER-1)

By Disposition:
- ALIGNED: 15
- PARTIALLY_IMPLEMENTED: 3 (REQ-004, REQ-010, REQ-014)
- IMPLEMENTED_UNDOCUMENTED: 1 (UNMAPPED-1)
- ACCEPTED_DIVERGENCE: 1 (REMAINING-1)
- REMAINING_STATE_MISMATCH: 1 (REGISTER-1)

INSP-03 recency (MR-1 tokens in AssessmentEvidence): all requirement rows carry
STILL CURRENT (assessment dated 2026-06-21 on the ADQ-10 tree after `43b039ba4`;
frontend behavior unchanged to `fac46e33f`). UNMAPPED-1, REMAINING-1/2, and
REGISTER-1 carry NOT APPLICABLE (not in the INSP-03 conformance matrix). The
Specification requirement IDs were not rewritten after INSP-03 (assessment
`REQ001..014` map 1:1 to spec `REQ-001..014`), so MR-9 old-ID remapping is not
triggered.

MR-4: Datasheet Attributes/Conditions restate the requirements (e.g.
'Artifact metadata fields' = REQ-005, 'Replay requirement' = REQ-008,
'Sensitive payload storage' = REQ-007); folded into the covering REQ rows. No
datasheet-distinct acceptance condition warranted a separate ACCEPTANCE row.

## Least-confident rows (with the reading that would flip them)

- **REQ-007 (ALIGNED, MEDIUM)** — I read REQ-007 ("sensitive values MUST NOT be
  stored unless a redaction pass has approved the payload") as satisfied because
  `redactJsonLike` runs unconditionally before every artifact write and tests
  confirm secrets are replaced with `[REDACTED_API_KEY]`. INSP-03 rated it
  PARTIAL. **Flip:** if REQ-007 is read to require an explicit approval/withheld
  *gate* that blocks raw storage (beyond blanket redaction), this becomes
  PARTIALLY_IMPLEMENTED. This is deliberately the mirror of the sibling
  DEL-05-03 R7 row (also ALIGNED with the same withheld residual noted), so the
  two ledgers agree on substance; the DEL-05-03 R13 row holds the
  DEL-05-05-gated verification residual (preview + withheld paths).

- **REQ-004 (PARTIALLY_IMPLEMENTED, MEDIUM; HumanDecisionNeeded NEW-PACKET)** —
  the impl has no distinct medium band (`classifyResultBudget` is inline /
  requires-artifact-overflow / exceeds-artifact-budget; preview appears only on
  truncation past `artifactByteLimit`). **Flip:** D-APP-42 explicitly left
  "thresholds, preview length, and naming unchanged"; if that is read as a
  ruling that *accepts* the current no-medium-band behavior for this tranche,
  REQ-004 becomes ACCEPTED_DIVERGENCE (no repair implied) rather than a
  requirement-vs-impl gap needing a new packet. REQ-010 and REQ-014 are the
  test-coverage siblings of the same band and would move with it.

- **REQ-012 (ALIGNED, HIGH) stale-path caveat** — Specification REQ-012 source
  and Datasheet line 28 cite `frontend/src/lib/harness/tool-descriptor.ts`, but
  the file moved to `frontend/packages/harness-contract/src/tool-descriptor.ts`
  under D-APP-48. The requirement substance (thresholds unchanged, SHA-256 +
  session-lifetime) is verified against the moved file and holds, so the row is
  ALIGNED with an R5 doc-repair note. **Flip:** if the moved-path citation is
  treated as kit text asserting a now-false location (MR-8), the row could be
  read as STALE_SPECIFICATION. I kept ALIGNED because it is a source pointer,
  not a state assertion, and the policy claim is true.

- **UNMAPPED-1 (IMPLEMENTED_UNDOCUMENTED, MEDIUM)** — `persistChildOutputArtifact`
  stores subagent child output under `artifacts/subagents/` using its own
  hardcoded 16KB/512KB constants (NOT descriptor-derived, unlike REQ-012's
  descriptor policy). **Flip:** if child-output artifacts are read as implicitly
  in-scope of DEL-05-05's "session artifacts" scope line, this is not unmapped
  but a documentation gap on an in-scope surface (still IMPLEMENTED_UNDOCUMENTED,
  but ownership packet unnecessary). I flagged it for a PKG-08-vs-DEL-05-05
  ownership decision because no requirement or ruling names it.

## Boundary with sibling DEL-05-03 (no duplication)

DEL-05-03's R13 row records the preview/withheld verification paths as
`PARTIALLY_IMPLEMENTED`, gated on DEL-05-05 thresholds/retention acceptance
(DEP-05-03-012). My side of that boundary is captured on REQ-004/REQ-010/REQ-014
(medium-preview band) and REQ-007 (withheld classification) without restating the
DEL-05-03 requirement rows. The DEL-05-05 verification residual is the same
underlying gap viewed from the owning (threshold/retention policy) side.

## Register-defect summary (MR-5)

- **REGISTER-1** (REMAINING_STATE_MISMATCH, LOW): `Dependencies.csv`
  DEP-05-05-010 names its target "Output budget checksum and retention policy"
  (TargetRefID D-APP-42) while `_DEPENDENCIES.md`'s Extracted Dependency Register
  summary table labels the same row "Output budget policy parameters". Benign
  summary-table naming lag; both resolve to the same SATISFIED D-APP-42
  constraint. No satisfaction or graph impact.

DepClosure re-verification (plan §5): DEL-05-05's 10 register rows re-checked
against the live tree — all seven `_REFERENCES.md` hashes MATCH (incl. REF-006
`docs/PRD.md` under D-APP-38), the impl path
`frontend/src/lib/harness/tool-result-artifacts.ts` exists and is test-covered,
and the D-APP-42 ruling record exists. DEL-05-05 was not among the D53A 11 open
residual rows and not on the D-APP-53 Option A dep-reconciliation list (it was an
Option C hardening item). No further register defect found; the
`TargetType=UNKNOWN` on the two OBJ- anchors is a documented v3.1 schema
limitation (no OBJECTIVE enum), not a defect.

## Method notes / deviations

- No method deviation. 19-column header copied verbatim from the R0 exemplar.
- Verification-basis vocabulary (MR-10) used verbatim on non-behavioral rows:
  `DOC-BASIS(D-APP-42)`, `RULING-RECORD(D-APP-53)`, `RULING-RECORD(D-APP-55)`,
  `GATE-TRANSCRIPT(W1@fac46e33f)`. Doc-only rows (REGISTER-1) use
  `documentary claim` + exact doc sections in ImplementationEvidence.
- REMAINING-1 (D-APP-42 Option C) classified ACCEPTED_DIVERGENCE per MR-8: the
  deferral is ruling-acknowledged (D-APP-42 logs Option C as a deferred future
  enhancement; D-APP-53 ruled Option A only). Gate suffix preserved verbatim
  (MR-6); SelectableUnderCurrentLoop = NO (gated on a new owner ruling).
  HumanDecisionNeeded = NO because the current Option-A state is the ruled state
  and nothing is pending.
- REMAINING-2 (concordance bootstrap) is UNGATED and Selectable YES; this run is
  its in-progress execution (D-APP-55).
