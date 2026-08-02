# Review — DEL-08-02 Versioned additive API schema

**Review stage:** GATE 2 COMPLETE — MECHANICAL SELF_CHECK POPULATED; OWNER GATES PENDING

**Review Type:** SELF_CHECK

**Reviewer(s):** AGENT_CHECK (producer-side mechanical self-check; no human peer reviewer inferred)

**Target transition:** INITIALIZED → CHECKING (not authorized or applied)

**Owner Gate 1 ruling (verbatim, 2026-08-01):**

> DEL-08-02 REVIEW Gate 1 — select SELF_CHECK and authorize
> review from INITIALIZED under D-PEC-74.
>
> Use the deterministic five-item SOW acceptance checklist. This opens
> mechanical producer-side review only; it does not accept the artifacts,
> advance lifecycle state, authorize another P1 node, release, or professional
> reliance.

This ruling selects `SELF_CHECK` and overrides only the normal review-entry
state. It grants no finding disposition, artifact fitness, lifecycle, later-P1,
release, or reliance authority.

## Review basis

- Contract: `ScopeOfWork.md`, valid `SOW_V1`, SHA-256
  `eb171e9dac40b313be8ea8ff75ad395171b599a41d2a1dbf290a9c5b44290c20`.
- Schema: `projects/pec/v2/contracts/api/v1/schema.json`, SHA-256
  `0a4e42737e628be604bd163e8c6f835cda488f7978ae9e973cff03d1f8695c67`.
- Compatibility test: `projects/pec/v2/tests/contracts/api/test_api_schema_compatibility.py`,
  SHA-256 `efdd32f24c0045160d7a736b1ffbdc2b8685246a66c8c362aba8899747decc92`.
- Fixtures: additive `b3ed8554e93e1380617ceb9d1de6030e684ddd91c89763d0d7565af56e079718`;
  removed element `eb25e52b14e4fcf98e48fec7a66d4988e5bfac590c6c30806cde3ed78338bacb`;
  meaning changed `bd2617a7cc47049af503c45fe6f86ec2c5f8270ae47950c9970288780c318cb8`.
- Registered-check evidence: `_run_records/D-PEC-74_REGISTERED_CHECKS.json`,
  SHA-256 `1505fc3973509f81feb62449d8d917076ce6891e37cc426081e6aa233736fa89`.
- Producer authority commit: `49676473884e07a78fa197a23451e13a12850427`.
- Review basis commit: `21546b6acd184c9d007eafcbc86800a83a7a9a21`.

The D-PEC-74 manifest reproduces without mismatch. The contract compiler
emits `chirality-review-checklist/v1`, tool version 1, with exactly five
source-ordered criteria. The six contract tests pass. Strict decomposition
register validation passes with 64 registers, 254 rows, and zero findings;
dependency closure reports 119 execution edges and zero nontrivial SCCs.

## Gate 1 preconditions

| Precondition | Result | Evidence |
|---|---|---|
| Deliverable folder | PASS | Governed deliverable folder and control files exist |
| Lifecycle entry | PASS BY OWNER OVERRIDE | `_STATUS.md` remains `INITIALIZED` |
| Production format | PASS | `SOW_V1`, zero validation issues |
| Anticipated artifacts | PRESENT | Versioned schema and compatibility tests exist at packet-bound paths |
| Dependency posture | PASS | Root node; no upstream execution predecessor |
| Review type | SELECTED | `SELF_CHECK`, by owner Gate 1 ruling |
| Reviewer identity | AGENT_CHECK | Mechanical producer-side assessment only |

## Deterministic checklist

| ID | Exact criterion | Verification | Addressed |
|---|---|---|---|
| AC-001 | The delivered schema declares an explicit version identifier, and any consumer can determine from the artifact alone which schema version a given request or response shape belongs to. | VER-001 | Y — top-level `api_schema_version` and request/response `const: 1` bindings make the version machine-readable from the artifact |
| AC-002 | The delivered check, run against the recorded baseline schema version and a candidate, passes candidates that only add and fails candidates that remove a published element or change a published element's meaning. Those two properties are the accepted floor stated at REQ-002; the finer taxonomy of permitted additive changes remains TBD-004, which this criterion neither resolves nor forecloses. The criterion binds the delivered mechanism's behaviour, not the content of schema versions authored after this deliverable closes. | VER-002 | Y — the additive fixture passes; removal and meaning-change fixtures are rejected; six tests pass |
| AC-003 | The initial schema version is recorded as the baseline predecessor the check runs against, and the delivered compatibility tests execute the check over seeded candidates — one purely additive, one that removes a published element, and one that changes a published element's meaning — with their outcomes retained as evidence. | VER-002 | Y — v1 is the recorded baseline; all three seeded candidates execute; registered-check evidence retains PASS output |
| AC-004 | The delivered schema and compatibility tests trace to SOW-042 and OBJ-001 and introduce no scope beyond SOW-042; in particular they do not absorb the transport, access-class, latency, response-format, or subscription scope held by the sibling deliverables named in CLM-004. | HUMAN_REVIEW: REVIEW confirms traceability and boundary | Y — artifact and tests implement only schema versioning/additive compatibility; no sibling transport, access, latency, response-format, or subscription behavior is introduced |
| AC-005 | An accountable owner confirms that the single-objective attribution `DEL-08-02 → OBJ-001` remains acceptable given the recorded MEDIUM-confidence qualification — that `PEC-API-003`'s "textual link to any single outcome is weak" and that `OBJ-001` "is recommended only because orientation is the API's primary consumer in §12's P1 sequencing, not because the text selects it" — and given the recorded unadopted alternatives `OBJ-001;OBJ-004` and the full consumer set. | HUMAN_REVIEW: accountable owner confirmation | PENDING OWNER — the qualification and alternatives are surfaced exactly; no confirmation is inferred |

## Findings and next gates

No CRITICAL, MAJOR, MINOR, or OBSERVATION finding was opened. AC-005 is an
explicit owner acceptance criterion, not an artifact defect, and remains open.

**Recommendation:** MECHANICALLY READY FOR SEPARATE OWNER RULING

The next ruling should keep three effects distinct: (1) Gate 5 lifecycle
approval or rejection for `INITIALIZED → CHECKING`; (2) AC-005 confirmation or
declination of the qualified `DEL-08-02 → OBJ-001` attribution; and (3)
acceptance or rejection of the exact schema, test, and fixture hashes as fit for
DEL-08-02. None is performed here, and no later P1 node, release, or
professional reliance is authorized.
