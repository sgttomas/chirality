# DEL-01-01 concordance notes — R2 Wave 5 (PKG-01)

- Run: `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; method: pinned plan §§6–7 @ `551f84ef6` + R2_METHOD_ADDENDUM MR-1..MR-11 + Wave-5 fan-in rules.
- Source state: frontend/ at `fac46e33f`, byte-identical through current HEAD `242900ae9` = `main`. Doc-only re-reads this run cite `RUN-INSPECTION@242900ae9` (the actual HEAD at which non-frontend surfaces were read); behavioral rows cite `GATE-TRANSCRIPT(W1@fac46e33f)`.

## Census

15 rows.

By ClaimType:

| ClaimType | Count |
|---|---:|
| REQUIREMENT | 10 |
| ACCEPTANCE | 2 |
| EXCLUSION | 1 |
| REMAINING_WORK | 1 |
| REGISTER_DEFECT | 1 |

By Disposition:

| Disposition | Count |
|---|---:|
| ALIGNED | 9 |
| STALE_ASSESSMENT | 2 (REQ-006, REQ-010) |
| STALE_SPECIFICATION | 2 (REQ-009, ACC-001) |
| DOCUMENTED_UNIMPLEMENTED | 1 (ACC-002) |
| REMAINING_STATE_MISMATCH | 1 (REGISTER-1) |

IMPLEMENTED_UNMAPPED rows: none. DEL-01-01's surface is the governance-doc
corpus; the material live behaviors adjacent to it (reliance register + test,
human-gate copy, audit event store) all carry accepted mappings to sibling
deliverables (DEL-01-02, DEL-01-03, PKG-03..PKG-07 owners per decomposition
v3.2 lines 280–283 and the register's enforcement matrix), so per the Wave-5
IMPLEMENTED_UNDOCUMENTED rule they are cross-referenced on the REQ rows
instead of emitted as unmapped rows.

## Least-confident rows (mandatory self-flagging)

1. **DEL-01-01-ACC-001 (STALE_SPECIFICATION, MEDIUM)** — the kit's "D-APP-38
   corpus v1" wording. Alternative reading that would flip it: the phrase is
   historical provenance ("was reconciled under v1"), and every substantive
   claim (REF-006 MATCH; hash-warning superseded) is TRUE at v6 — under that
   reading the row is ALIGNED with a cosmetic provenance label, not a stale
   specification. I chose STALE_SPECIFICATION because Procedure.md step 2
   line 27 makes "the current D-APP-38 corpus version" load-bearing for
   issue-readiness reliance, and a reader following the kit today would bind
   reliance to v1 rather than v6 (MR-8: text asserting a now-false state).
2. **DEL-01-01-ACC-002 (DOCUMENTED_UNIMPLEMENTED, MEDIUM)** — the seven
   expected documentation artifacts (checklists/notes/conflict table) do not
   exist as files. Alternative reading: the Specification itself declares the
   filenames `TBD` and INSP-03 rated the posture rows PASS on the kit text
   alone, so one could read the four-doc kit as *being* the artifacts in
   embryo and score this ALIGNED-with-declared-TBD. I kept
   DOCUMENTED_UNIMPLEMENTED because the Documentation section is a current
   claim ("expected documentation artifacts are…"), nothing produces them, no
   ruling defers them, and `## Remaining` does not carry the residual —
   flagged NEW-PACKET via Guidance ruling R004 (no decision-register row
   exists).
3. **DEL-01-01-REQ-009 vs REQ-010/REQ-006 split** — I put the operative
   defect for REQ-009 on the kit (STALE_SPECIFICATION: live surfaces do NOT
   agree — kit says CHECKING, _STATUS says IN_PROGRESS) and for
   REQ-006/REQ-010 on the assessment (STALE_ASSESSMENT: live surfaces agree
   and INSP-03, which carries no superseding note, still presents
   PARTIAL/FAIL as current). Alternative reading: fold all three into one
   pattern. MR-1's reservation rule is what forces the split.
4. **Verification-basis SHA for doc-only rows** — I cite
   `RUN-INSPECTION@242900ae9` (current HEAD) rather than `fac46e33f`
   (frontend byte-identity anchor) because non-frontend doc surfaces were
   read at HEAD. If the fan-in verifier prefers a single anchor, every such
   row is unchanged at both SHAs (frontend byte-identical between them and
   the doc reads happened at HEAD).

## Register-defect summary

One row, metadata lag only:

- **REGISTER-1** — `Dependencies.csv` DEP-01-01-010 (Statement/Notes) and
  `_DEPENDENCIES.md` line 62 pin the REF-006 reconciliation to "D-APP-38
  corpus v1"; current corpus is **v6** (`AUTHORITY_CORPUS.json`
  current_version v6, binding commit `a9fb1af4a`). The `_REFERENCES.md` hash
  table itself already matches v6 exactly (verified by live `shasum`
  recomputation of all seven sources this run), so the defect is a stale
  version label, not a stale reconciliation.

Checked and NOT emitted as defects:

- Row counts/status/satisfaction totals are internally consistent across
  `Dependencies.csv` (12 ACTIVE: 4 ANCHOR SATISFIED, 8 EXECUTION PENDING) and
  `_DEPENDENCIES.md`, and agree with the D53A snapshot coverage row
  (`DEL-01-01,Y,12,Y,Y`) and with INSP-03's count of 12.
- `_DEPENDENCIES.md` "Declared Upstream/Downstream" sections are populated
  (not bare TBD), so the Declared-TBD rule was not needed.
- The 8 EXECUTION rows staying PENDING is deliberate register discipline
  (REQ-010: no satisfaction outside a governed tranche), not lag.
- DEL-01-01 is a D53A **orphan** (no strict execution edges) — the closure
  report explicitly calls this a topology fact, not a defect.
- Minor observations, notes-only: `Dependencies.csv` DEP-01-01-011 and
  `_REFERENCES.md` REF-007 use an absolute machine-specific path
  (`/Users/ryan/ai-env/...`) for the instruction-root agent file (consistent
  across both surfaces, hash verified live); `_DEPENDENCIES.md` Run Notes
  line 54 still carries the pre-extraction "until Dependencies.csv exists"
  instruction whose condition has been satisfied since 2026-05-20.

## Other observations (no rows)

- Guidance Conflict Table C002 (stale dispatch package-label path) and open
  rulings R002/R003 remain visible, correctly represented as open — that is
  REQ-008-conforming behavior, not a defect. R004 is carried on ACC-002.
- The reliance register itself (`docs/harness/reliance_boundary_register.md`,
  DEL-01-02 surface) says "Current corpus is v1 and MATCH" in its residual-risk
  table — flatly false at v6. That defect belongs to DEL-01-02's ledger; noted
  here as a cross-deliverable handle for the PKG-01 fan-in.
- "No test exists" checks performed by real search: grep of
  `frontend/src/__tests__/**` for approval/professional/certify copy
  assertions found targeted boundary assertions
  (`chirality-read-mcp.test.ts` lines 345/367; `domain-profile.test.ts`
  lines 54–55) but no whole-UI copy sweep — phrased accordingly on REQ-002;
  `session-events.test.ts` presence confirmed via VERIFICATION_INDEX.csv
  line 75 (5 cases) inside the passing W1 gate suite.
- REQUIREMENT_INDEX.csv fully enumerates DEL-01-01-REQ-001..010 (no parser
  gap for this deliverable); the claim set was still re-derived from
  `Specification.md` and matches 1:1.

## Method deviations

None. Read-only outside the two authorized files; no tests executed; no
lifecycle or register mutation; no cross-project execution tree read (the
only cross-project surface touched is the pinned instruction-root agent file
hash named by this deliverable's own register). No secret values copied.
