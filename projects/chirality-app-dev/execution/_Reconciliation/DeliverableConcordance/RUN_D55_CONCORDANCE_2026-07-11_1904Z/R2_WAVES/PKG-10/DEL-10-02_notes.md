# DEL-10-02 concordance notes — R2 Wave 6 (PKG-10)

Run `RUN_D55_CONCORDANCE_2026-07-11_1904Z`; frontend reviewed at `fac46e33f`
(byte-identical through HEAD `1976b379d` per the W6 dispatch); documents and
registers read at `1976b379d`. Discovery only; no file outside the two wave
artifacts touched. F-APP-3 heightened fence observed: no other project's
execution tree was read; cross-engine facts derive only from this
deliverable's own register (`Dependencies.csv` DEP-10-02-003 note, D53A
evidence record), the decision register, and the shared root-level
`_DomainEngines/profiles/*.yaml` surfaces those register rows explicitly cite.

## Census

**22 rows total.**

By ClaimType:

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 12 |
| EXCLUSION | 4 |
| ACCEPTANCE | 3 |
| REMAINING_WORK | 2 |
| REGISTER_DEFECT | 1 |

By Disposition:

| Disposition | Rows |
|---|---:|
| ALIGNED | 18 |
| STALE_SPECIFICATION | 2 |
| STALE_ASSESSMENT | 1 |
| REMAINING_STATE_MISMATCH | 1 |

Requirement re-derivation: the R1 REQUIREMENT_INDEX carries all 12
`DEL-10-02-REQ-###` IDs (no parser gap for this deliverable); the re-derived
set from `Specification.md` lines 27–38 matches it exactly. MR-4 fold: the
Datasheet Attributes rows restate the REQ set and were folded into the REQ
rows; the three ACCEPTANCE rows carry only datasheet/kit-distinct conditions
(the REF-006 hash-mismatch posture, the concrete-path-patterns TBD posture,
and the ResponsibleParty TBD condition). INSP-03 uses its own REQ001–REQ012
numbering that is not 1:1 with the current spec IDs; each row's
AssessmentEvidence cites the `old-REQnnn` mapping per MR-9.

## Enforcement-truth checks performed (PKG-10 duty)

Where a claim touches enforced product behavior, the live surface was
checked, not just the documents:

- **No apply surface:** no accept/apply/force tool registered anywhere
  (`domain-proposal-tools.ts` module comments lines 35–46/584–588;
  `tool-catalog.ts` lines 110–133; grep clean); test-pinned at
  `domain-proposal-tools.test.ts` lines 541–580.
- **No `/api/domain/*` route:** `frontend/src/app/api` holds only
  `project/`, `harness/`, `working-root/`; the `/api/projects/...` strings in
  the proposal tools are pec-engine endpoints on the loopback transport.
- **Proposal-path write allowance is permission-graded live:**
  `domain_propose_operation` denies in readOnly and allows in workspaceWrite
  (test lines 250–318); `domain_proposal_validate` is read-grade, one GET.
- **Boundary copy is live in every tool envelope:**
  `PEC_PROPOSAL_RESULT_SEMANTICS` (lines 101–102) and
  `NO_VERDICT_RESULT_SEMANTICS` (`domain-profile-registry.ts` lines 44–45).
- **No protected-path hook exists** (`permission-overlay.ts`,
  `persona-manager.ts` greps clean) — consistent with, not contradicting, the
  kit's declared-TBD hook posture.
- **"No test exists" claims (REQ-011/012)** rest on a real search: the only
  test-tree reference to `protected_write_paths` is fixture data in
  `domain-profile.test.ts` line 34; VERIFICATION_INDEX.csv has no DEL-10-02
  row.

## Zero IMPLEMENTED_UNMAPPED rows — justification

The live domain surface adjacent to this policy (profile registry, read
wrappers, pec proposal transport, permission grading, project-root
containment) is fully mapped elsewhere: the D-APP-49..52 rulings authorize it
and the decomposition assigns the OperationProposal/human-gate workflow to
sibling DEL-10-03 and the fixture/validation posture to DEL-10-04. Per the W6
rule (a behavior assigned to a sibling deliverable counts as an accepted
mapping), no IMPLEMENTED_UNMAPPED row is warranted here; the cross-deliverable
handles are DEL-10-03 (proposal workflow) and DEL-10-04 (fixture/validation).

## Least-confident rows (mandatory self-flagging)

- **DEL-10-02-REQ-001 (STALE_ASSESSMENT, MEDIUM).** Coded stale because
  INSP-03's evidence sentence ("static source scans found no frontend domain
  path or route") is now false and carries no superseding note, while kit and
  live surfaces agree with reality (MR-1 pattern). Alternative reading that
  would flip it: the old-REQ001 *conclusion* (no runtime scope creep) remains
  true under the rulings, so the row could be ALIGNED with AssessmentEvidence
  OVERTAKEN and the annotation need recorded only as RemainingWork. I kept
  STALE_ASSESSMENT because the overtaken factual sentence is the operative
  defect a reader would take as current truth.
- **DEL-10-02-ACC-002 (STALE_SPECIFICATION, MEDIUM).** The Datasheet's
  "patterns are not defined in the accessible sources" clause is superseded
  by the deliverable's own register citing the ADOPTED profiles' live
  `protected_write_paths` blocks. Alternative reading: the kit means
  *policy-accepted glob syntax*, which the D53A record confirms is still TBD
  (DEP-10-02-005 open) — under that reading the row is ALIGNED and only a
  wording sharpen is desirable. I coded STALE_SPECIFICATION because the
  clause as written is a current-state assertion a reader would take as "no
  concrete patterns exist anywhere," which is no longer true.
- **DEL-10-02-EXC-001 (ALIGNED, MEDIUM).** Live write-graded propose/refresh
  against the local pec engine is proposal-record creation, not "domain
  operation execution" (apply remains excluded). Alternative reading: treat
  the live mutating proposal transport as a bounded transitional divergence
  from the exclusion, deliberately permitted by D-APP-52 →
  ACCEPTED_DIVERGENCE. I kept ALIGNED because the exclusion's plain subject
  (operation execution/apply) is still fully excluded; D-APP-52 permits an
  adjacent surface, which per the W5-settled rule does not convert this row.
- **DEL-10-02-REQ-003 (ALIGNED, MEDIUM).** TYPES §11.3 renamed the term to
  "Agent-writable path" with an expanded folder list; SPEC §18 and PRD FR-111
  retain "proposal path." Flip reading: the kit's "defined in TYPES §11.3 as
  proposal path" citation is now literally false → STALE_SPECIFICATION. Kept
  ALIGNED because the definition is a compatible subset and the authority
  corpus itself uses both vocabularies (any repair is cosmetic drift).
- **DEL-10-02-REQ-010 (ALIGNED, MEDIUM).** The "TBD until DEL-10-01 defines
  the profile contract" premise is partially satisfied (contract draft
  materialized; glob syntax still TBD per D53A). Flip reading:
  STALE_SPECIFICATION on the premise clause. Kept ALIGNED because the
  operative TBD (glob syntax, manifest schema, examples) remains true and is
  already carried by the live gated Remaining item.
- **DEL-10-02-REQ-012 / EXC-003 (ALIGNED, MEDIUM).** Same underlying facts as
  ACC-002/REQ-010: live pec-scoped forerunners exist for postures the kit
  declares wholly future. If the fan-in verifier reads ACC-002 as ALIGNED,
  these stay ALIGNED too (consistent set); if it hardens ACC-002's stale
  reading, EXC-003's "policy stays category-level" declaration survives but
  its Guidance line 22 support clause shares the ACC-002 defect.

## Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH):** `_REFERENCES.md` REF-007
  uses the machine-absolute path
  `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md`
  (known run-wide class per the W6 brief). Content integrity holds — the
  repo-relative copy's SHA256 reproduces both recorded hashes.
- **Considered and NOT coded:** the dated D-APP-53 reconciliation notes in
  `Dependencies.csv` DEP-10-02-003 and `_DEPENDENCIES.md` line 33 say
  "DEL-10-01 remains CHECKING," which was true on 2026-07-10 and was
  overtaken by the D-APP-54 rebaseline on 2026-07-11 (live DEL-10-01
  `_STATUS.md` is IN_PROGRESS). Because the sentence sits inside an
  explicitly dated reconciliation annotation, I treated it as historical
  evidence rather than a current-truth assertion (consistent with the
  superseding-note discipline); flagging here so the fan-in verifier can
  overrule with a REGISTER-2 if the dated-note reading is judged too
  charitable.
- Register otherwise healthy: `_DEPENDENCIES.md` counts/lifecycle tables are
  in sync with the CSV post-D53A (ACTIVE 4 / RETIRED 1; SATISFIED 3 / TBD 1 /
  NOT_APPLICABLE 1); all seven `_REFERENCES.md` hashes reproduce by direct
  recomputation at `1976b379d`; the Declared Upstream/Downstream TBD sections
  are by-design (docs/SPEC.md §5.2), not defects.

## F-APP-3 UNKNOWN cells

None written. No cell required cross-project engine status beyond what this
project's own pinned surfaces state; pec and open_pipe_stress facts cite this
deliverable's register rows, the D-APP-50..52 rulings, and the shared
root-level profile files those rows name. No fence reads occurred.

## Method deviations

None. MR-1 tokens present on every row; MR-2 Selectable derived only on the
two REMAINING rows (REMAINING-2 YES, REMAINING-1 NO — its stage-gate is
unsatisfied); MR-5 bare `REGISTER-1` ClaimID; MR-6 gate suffixes verbatim;
MR-10 vocabulary used verbatim (doc-only rows carry `documentary claim`
implementation evidence). Behavioral evidence binds to
GATE-TRANSCRIPT(W1@fac46e33f) plus named test files/cases with line anchors;
no tests were executed and no dependencies installed.
