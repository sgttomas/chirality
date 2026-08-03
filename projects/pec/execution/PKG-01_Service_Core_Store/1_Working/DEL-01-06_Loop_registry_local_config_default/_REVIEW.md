# Review — DEL-01-06 Loop registry local-config default

**Review stage:** SELF_CHECK RERUN COMPLETE — RF-001 RESOLVED; SCA-004 CONTRACT-CURRENCY FINDING OPEN; `INITIALIZED`

**Review Type:** SELF_CHECK

**Reviewer(s):** AGENT_CHECK (mechanical review; no peer reviewer inferred)

**Target transition:** `INITIALIZED → CHECKING`

**Lifecycle:** `INITIALIZED`, unchanged

**Owner Gate 1 ruling (verbatim, 2026-08-02):**

> APPROVE:
>
> 1. Merge PR #462 at source SHA
>    d4f53a70e4328101ba4756f0919b8bdb35cc9188.
>
> 2. DEL-01-06 REVIEW Gate 1 — select SELF_CHECK and authorize
>    review from INITIALIZED under the D-PEC-75 O-A source-production
>    phase.
>
>    Use the deterministic six-item SOW checklist, AC-001 through
>    AC-006. Evaluate the recorded pending VER-005 condition explicitly.
>
>    This opens mechanical review only. It does not accept the produced
>    artifacts, advance lifecycle, authorize another P1 node, release,
>    or professional reliance.

The ruling selects SELF_CHECK and expressly overrides review entry from
`INITIALIZED`. It creates no artifact acceptance or lifecycle transition.

**Owner Gate 4 disposition and Gate 5 ruling (verbatim, 2026-08-02):**

> APPROVE:
>
> 1. DEL-01-06 RF-001 — DEFER.
>
>    Retain the DEL-01-05 enforcement rerun as mandatory future
>    SELF_CHECK evidence. Do not waive VER-005. Reopen RF-001 and
>    rerun SELF_CHECK when DEL-01-05 is available.
>
> 2. DEL-01-06 REVIEW Gate 5 — HOLD.
>
>    Retain DEL-01-06 at INITIALIZED. This does not accept the
>    produced artifacts, satisfy AC-005 or AC-006, authorize another
>    P1 node, release, or professional reliance.

The disposition is final for this review checkpoint but conditional in
operation: RF-001 must be reopened and SELF_CHECK rerun when DEL-01-05 is
available. It waives no evidence obligation.

## Review basis

- Accepted production contract: `ScopeOfWork.md`, valid `SOW_V1`, SHA-256
  `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`.
- Producer source: PR #462 source
  `d4f53a70e4328101ba4756f0919b8bdb35cc9188`, merged as
  `ccd9a2178ffd8029fdd1cd779910e954e0612e21`.
- Checklist compiler: `chirality-review-checklist/v1`, tool version 1;
  exactly six source-ordered criteria.
- Producer evidence: `D-PEC-75_REGISTERED_CHECKS.json`, SHA-256
  `690ea5141051d6cbe68545d46512e641b20ddcea5e16cd8b363588ed7ca954ec`.
- DEL-01-05 accepted enforcement: lifecycle `CHECKING`; exact inventory
  accepted through packet SHA-256
  `e3d6f2ae9e52b149abb75f5bba8815a7eb65a549ebf3be258eae8581ff43b596`.
- Mandatory VER-005 rerun evidence:
  `D-PEC-77_VER005_RERUN.json`, SHA-256
  `1e0bd26f5bcda92996ed66e6373a6c67f2fe23270e48c98688c5cf6d488a1210`.
- Current decomposition: revision 1.4 under SCA-004; it adds SOW-077 to
  DEL-01-06 and resolves OI-003. The accepted revision-1.3 SOW has not been
  rebuilt and is therefore stale exactly as recorded by the SCA-004 handoff.

## Gate 1 — preconditions

| Precondition | Result | Evidence |
|---|---|---|
| Deliverable folder | PASS | Governed folder and control files exist |
| Lifecycle entry | PASS BY OWNER OVERRIDE | Review entered from `INITIALIZED`; state remains unchanged |
| Contract format | PASS | `SOW_V1`, exact accepted hash |
| Review type | SELECTED | `SELF_CHECK` |
| Context/decomposition consistency | FAIL — NEW CURRENCY FINDING | Current revision 1.4 covers SOW-077;SOW-094 and resolves OI-003, while the accepted SOW remains bound to revision 1.3 / SOW-094 and says OI-003 is open |
| Dependency posture | PASS | Root node; no upstream execution predecessor |

## Gate 2 — deterministic checklist and Gate 3 outcomes

The exact compiler-emitted criterion text and order are preserved. `PARTIAL`
means the available portion passes but the criterion cannot close at this
review state.

| ID | Exact criterion | Verification | Outcome | Evidence |
|---|---|---|---|---|
| AC-001 | The configuration format documents every field it defines, names each served loop with a stable identifier, and is validatable deterministically, with a valid instance accepted and every malformed fixture rejected. | VER-001 | PASS | Schema/default inspection; valid default and malformed, duplicate, missing-field fixtures execute and pass |
| AC-002 | The checked-in default instance registers exactly one loop at P1, identified as PEC v2's own build per OI-010, and admits the remaining registered loops at P2 by adding entries only, with no format change and no entry for a loop not named in an accepted source. | VER-002 | PASS | Default contains exactly `pec`; schema is entry-additive and the only checked-in locator is the accepted PEC LOOP_INIT path |
| AC-003 | The loader rejects an invalid or unreadable configuration with an explicit failure that names the offending entry or field, and never returns a silently defaulted, partial, or empty loop set in its place. | VER-003 | PASS | Malformed, duplicate, missing-field, absent, unreadable, and no-partial/no-empty tests execute and pass |
| AC-004 | The loader exposes the registered-loop set through an interface whose signature carries no configuration path or serialization detail, so that relocating or reshaping the registry changes no consumer deliverable. | VER-004 | PASS | Core port exposes only `registered_loops() -> tuple[RegisteredLoop, ...]`; boundary test executes and passes |
| AC-005 | The format, the default instance, and the loader add no third-party runtime dependency and make no network call, leaving the DEL-01-05 zero-dependency and locality assertion intact. | VER-005 | PASS | Accepted DEL-01-05 checker rerun on current PEC core: dependency/locality/registration PASS, zero findings, core-tree SHA-256 `2c830d1f…`; exact evidence SHA-256 `1e0bd26f…` |
| AC-006 | The automated test suite implements VER-001 through VER-005, executes in the service-core test run, passes, and introduces no acceptance criterion absent from this contract. | VER-006 | PASS | Registered `v2-loop-registry` 12/12 PASS and `v2-core-posture` PASS in the same exact evidence record; enforcement regression suite separately 19/19 PASS |

### Mechanical verification

- Exact SOW validation and deterministic checklist derivation: PASS.
- Registry suite: PASS, 12/12.
- Accepted DEL-01-05 enforcement suite: PASS, 19/19.
- Registered VER-005 rerun: PASS; dependency/locality/registration all PASS,
  zero findings, `PEC_RELEASE_BLOCKING`; evidence SHA-256 `1e0bd26f…`.
- Existing API regression: PASS, 6/6 in bound producer evidence.
- Core/adaptor boundary, immutable value, standard-library-only imports, and
  no network-module import: PASS.
- Strict decomposition registers: PASS, 64 registers / 254 rows / zero
  findings.
- Dependency closure: PASS, 119 execution edges / zero nontrivial SCCs.
- D-PEC-75 manifest before review edits: PASS.

## Gates 3–4 — finding and owner disposition

The deferred mechanical finding is resolved by exact enforcement evidence.
A separate contract-currency finding is recorded because SCA-004 Gate 5
changed current decomposition truth after the accepted SOW was sealed. No SOW
repair is authorized by this review.

| Finding | Severity | Status | Proposed disposition | Human disposition |
|---|---|---|---|---|
| RF-001 — AC-005 and AC-006 required exact DEL-01-05 enforcement evidence | MAJOR | RESOLVED | Prior `DEFER`; reopen and resolve when exact rerun passes | DEFER condition fulfilled; exact rerun PASS |
| RF-002 — accepted SOW is stale against revision 1.4 / SCA-004 | MAJOR | OPEN | PROPOSAL: `REVISE` through the separately gated WORKING_ITEMS + REVIEW SOW-currency path named by the SCA-004 handoff | TBD |

The prior owner `DEFER` condition has fired. REVIEW reopened RF-001 and ran
the accepted DEL-01-05 checker against the current DEL-01-06-containing core.
Exact evidence SHA-256
`1e0bd26f5bcda92996ed66e6373a6c67f2fe23270e48c98688c5cf6d488a1210`
records the registry suite 12/12 PASS plus dependency/locality/registration
PASS with zero findings. AC-005 and AC-006 now PASS; VER-005 is not waived;
RF-001 is `RESOLVED`.

SCA-004 independently makes the accepted SOW stale: current decomposition
revision 1.4 maps SOW-077 and SOW-094 to DEL-01-06 and resolves OI-003, while
the accepted SOW is pinned to revision 1.3 / SOW-094 and states OI-003 is
open. RF-002 records that mismatch. Its repair is a separately gated
WORKING_ITEMS + REVIEW act named in the SCA-004 handoff, not part of this
SELF_CHECK rerun.

## Gate 5 owner outcome

**Outcome:** retain `HOLD` at `INITIALIZED`; no transition applied or proposed
while RF-002 is open and no fresh Gate 5 owner ruling exists.

AC-001 through AC-006 pass mechanically against the accepted revision-1.3 SOW,
and RF-001 is resolved with exact VER-005 evidence. The later SCA-004
contract-currency mismatch prevents a clean Gate 1 / Gate 5 posture until the
separately gated SOW repair and review occur. No lifecycle transition or
exact-hash DEL-01-06 artifact acceptance occurred.

The prior contract-fitness Gate 5 `HOLD` and exact-hash SOW contract
acceptance remain preserved in immutable snapshot
`REV_DEL-01-06_2026-08-02_0954`; this review neither reopens nor enlarges that
earlier act.
