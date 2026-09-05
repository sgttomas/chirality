# DEL-08-02 R0 coverage

Source basis: faf22452528b5ba895e88ba0ad3770855100de08. Derivative calibration;
not accepted scope, repair authority, release or lifecycle disposition.

## Complete contract accounting

All 27 production stable IDs have exactly one compound claim row:
OUT-001..002, CLM-001..004, TBD-001..004, REQ-001..004, AC-001..005,
VER-001..002, AX-001..006. All 11 REQ/AC/VER IDs are covered, with no omissions.
The additional DEL-08-02::TM-PEC-022 row preserves the existing stable TM ID,
not a minted production obligation. The contract fully covers stable scope
SOW-042; current revision-1.4 ScopeLedger row preserves its exact versioned,
additive API statement and OBJ-001 attribution. No fallback scope ID needed.

Purpose/source-chain text, output matrix, production sequence and closing prose
repeat these stable IDs and are not additional independent requirements.
Sequence decision-before-authoring is evidenced by D-PEC-74 activation authority
at 49676473884e07a78fa197a23451e13a12850427, preceding tested source
 d99bf2ef923d640d956718b113f86c4755f837de. OUT/TBD/CLM/AX statements remain
individually accounted even where historical or explicitly optional.

## Current verification

READ_MANIFEST.json retains exact commands, stdout/stderr, interpreter and exit
codes. Run from projects/pec with PYTHONDONTWRITEBYTECODE=1:
`python3 -m unittest discover -s v2/tests/contracts/api -p 'test_*.py' -v`.
Result: six tests PASS, exit 0. No product service, network, mutable database,
or frozen legacy product check ran. No bytecode or in-tree cache writes.

Version test verifies top-level version 1 and const 1 on both shape definitions.
Manual artifact inspection confirms request capability/use_case/input and
response capability/use_case/outcome/output fields under the named version;
this is an interface artifact claim, not a running orientation service claim.
The comparator recursively rejects removal/type/value changes and specifically
labels x-pec-meaning changes. Seeded additive, removal, meaning-change cases,
unknown additions and required-property additions are exercised. This supports
the exact accepted canary taxonomy, not universal semantic proof or future
schema enforcement. No additional obligation to implement a transport,
JSON-Schema validator or consumer behavior is inferred.

All five accepted source artifacts were rehashed against current files,
the final owner ruling, and historical tested source
`d99bf2ef923d640d956718b113f86c4755f837de`; all match. The old registered check
artifact is preserved as historical evidence; the current rerun supplies current
verification. The workflow profile has later additions; historical profile
bytes are not claimed current or part of the five-byte-set acceptance.
Owner records were independently read from origin/main and match local hashes.
No network fetch was performed by the worker; the parent supplied the fetched,
effective basis, and this worker verified the exact remote-tracking bytes.

## Claim-class semantics and false positives

Behavioral ALIGNED means mapped source plus current test evidence for the bounded
mechanism. Artifact ALIGNED means the declared schema structure is present,
version-bound and exact-byte accepted, supported by inspection and version test.
Human-act ALIGNED requires the explicit owner record: AC-005 is satisfied by
qualified attribution confirmation, never by passing tests. Scope/validation
ALIGNED cites accepted boundary and producer SELF_CHECK plus separate owner
fitness. It does not invent an independent human peer review. Documentary and
historical ALIGNED means the dated statement and its authority/provenance remain
truthfully interpretable; it is not an assertion that old OPEN/no-source text
is current. TBD-001 is truthful unresolved metadata, not a new scope mandate.

D-PEC-66 explicitly preserved CLM-002/AX-006 frozen-exhibit wording while
 declining E-N13 in the live dependency mirror. ACCEPTED_DIVERGENCE records that
exact owner exception. It must not restore an edge or trigger a repair.
CLM-003/AX-002 belong to the drafting-era contract, and later D-PEC-74 records
implementation and CHECKING. AX-004's old basis/pointer statement is similarly
historical; revision-1.4 context/reference currency is already completed.
No new currency repair is proposed from these frozen words.

COV-040 is a folder-local artifact matcher warning despite exact accepted bytes
in v2 source paths. It is not evidence of missing implementation. TM-PEC-022's
owner-deferred next-lifecycle handling is retained as a candidate residual,
not an immediate lifecycle defect or permission to demote CHECKING.

## Gates and residual accounting

28 claim rows: 25 ALIGNED, 2 ACCEPTED_DIVERGENCE, 1 DEFERRED_AGENT_WORKFLOW.
One residual, DEL-08-02-REM-001, linked only to TM-PEC-022. Assessment:
ASSESSED_WITH_RESIDUALS. No UNKNOWN or STALE_INPUT row; source hashes unchanged.
No warranted NONE claim is made, and absent Remaining is recorded explicitly.

Depends: NONE. Target Dependencies.csv contains only two satisfied ANCHOR rows,
no upstream prerequisite. LOOP_INIT dependency blocking requires ACTIVE +
PREREQUISITE + TBD/PENDING/IN_PROGRESS + target named by Depends; thus no local
dependency blocks the proposed deferred concern. Informational downstream
relations, including declined E-N13, supply no invented gate.

Exact target ScopeOfWork.md preflight with operation
exact-correction-preparation returns ALLOW; header-only hold register is valid.
This does not authorize production or reliance. Every proposal remains
NON_SELECTABLE_PENDING_OWNER_APPLICATION. Owner gates need accepted acts on
origin/main. Predecessor commits/checks/run records on the run branch never
substitute. Any later status edit must first respect the frozen CHECKING path
and receive an exact application ruling. No automatic Remaining write or
lifecycle repair follows from R0.

TM-PEC-023 mapping hold is separate and unrelated to DEL-08-02; no new urgency
or downstream gate. PRDv2.3/D-PEC-79 remain adopted-not-applied, live PRD v2.2
and accepted decomposition revision 1.4 remain the current basis. D-PEC-80
retired workplans supply no selectable work. Ordinary currency is not reopened.

## Owner choices and calibration lesson

Accept this evidence and retain TM-PEC-022 only in its existing TM home until
its trigger; or direct an exact gated Remaining mirror at a lawful later
application stage. Both preserve its next-lifecycle trigger and avoid duplicate
uncontrolled work selection. No immediate lifecycle advancement is proposed.
Calibrate whether an owner-deferred administrative concern counts in the future
warranted Remaining census, as this candidate convention does, or stays solely
in TM with an explicit no-duplicate disposition. Scale-out and application are
separate owner gates. No product implementation residual is evidenced here.
