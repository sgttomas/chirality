# D-PEC-75 O-A contract-currency handoff

**State:** BOTH PREREQUISITES SATISFIED / SOURCE PRODUCTION OPEN / READY FOR WORKING_ITEMS

**Selected deliverable:** PKG-01 / DEL-01-06 Loop registry (local config
default), and no other node

**Governing packet:** `PACKET.md`, especially §§4 and 5.1–5.2

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. Merge PR #458 at source SHA
>    5ea7c116d32aa8f133536a1a1de6c7c1cb4a9f88.
>
> 2. D-T0-27: O-A.
>
> 3. D-PEC-75: O-A.

The third item rules D-PEC-75 O-A. The first and second items remain governed
by CHANGE and the Tier-0 Domain Engine decision respectively; this handoff
does not duplicate either act.

## Completed producer act — contract currency only

Under the recorded O-A authority, WORKING_ITEMS performed one bounded repair
of only:

`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md`

The repair is limited to the exact packet §5.2 fence:

- replace revision 1.2 / `3623b958b` currency with accepted revision 1.3 /
  `11a494e9a` in frontmatter and accepted-basis references;
- change CLM-007 and any direct lifecycle mirror from `OPEN` to current
  `INITIALIZED`, still with no implementation; and
- remove only obsolete prose claiming `_REFERENCES.md` names revision 1.1.

No requirement, output, AC/VER identifier, field obligation, objective,
dependency, lifecycle state, or OI-003 posture may change. The deterministic
SOW validator must remain `PASS format=SOW_V1`, and the derived checklist must
remain exactly AC-001 through AC-006.

The mechanical producer fan-in records:

| Evidence | Result |
|---|---|
| Repaired SOW SHA-256 | `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a` |
| Deterministic validation | `PASS format=SOW_V1` |
| Derived checklist | six items, unchanged identifiers AC-001 through AC-006 |
| Lifecycle | `INITIALIZED`, unchanged |
| Source phase | dormant; no source authority |

Neither the ruling nor this fan-in selects a REVIEW type, authorizes review
from `INITIALIZED`, accepts the repaired SOW, or advances lifecycle. The
repaired exact hash and unchanged six-item checklist now await separate REVIEW
Gate 1 and later owner artifact-fitness acts.

## Mechanical contract-fitness REVIEW

The owner subsequently selected `SELF_CHECK`, authorized review from
`INITIALIZED`, and bound the exact six-item checklist to SOW SHA-256
`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`.
The verbatim ruling is recorded in the deliverable-local `_REVIEW.md`.

REVIEW populated AC-001 through AC-006 as `PENDING FUTURE PRODUCTION`. No row
is marked implementation-PASS because no format, default, loader, interface,
dependency surface, or test suite exists. Contract validation, checklist
identity/order/text, matrix closure, objective/scope trace, repair containment,
TBD/OI-003 preservation, strict registers, and dependency closure pass. Zero
findings were opened; Gate 4 disposition is not applicable.

Immutable evidence is
`projects/pec/execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-02_0904/`.
Gate 5 recommends `HOLD` lifecycle at `INITIALIZED` and routing a separate
owner acceptance or rejection of the exact repaired SOW hash as the production
contract. That later contract-fitness act must not satisfy future-production
AC-001 through AC-006 or itself advance lifecycle.

## Owner Gate 5 and exact-hash contract disposition

The owner subsequently ruled Gate 5 `HOLD`, retaining DEL-01-06 at
`INITIALIZED`, and separately accepted ScopeOfWork SHA-256
`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`
as the production contract. The full verbatim three-item message is recorded
in the deliverable-local `_REVIEW.md`; its D-T0-29 item remains owned by the
Tier-0 instrument and creates no REVIEW effect.

AC-001 through AC-006 remain `PENDING FUTURE PRODUCTION`; zero findings remain
open. No lifecycle transition was applied. Immutable final disposition
evidence is
`projects/pec/execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-02_0954/`.
The SOW acceptance does not make D-T0-27 effective or independently open
source. Any downstream activation requires owning-manager verification of the
distinct D-PEC-75 prerequisites against serialized durable state.

## Source-production phase — open after serialized fan-in

Both conditional gates are durably evidenced:

1. the repaired DEL-01-06 SOW completes separately authorized REVIEW with all
   six criteria populated, every finding dispositioned, and exact-hash owner
   acceptance as the production contract; and
2. D-T0-27 is effective.

D-T0-27 O-A is ruled and its exact SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`
postimage is effective at `ADOPTED / READ_ONLY`. PR #459 source
`0e47c218c26830a4efeb29eb2d2f3ea99142b987` merged as
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; current main basis
`556ae59a34ac2f06ef924d367843a72ea00d1f37` descends from it. D-T0-28
application-manifest SHA-256 is
`36959f0a5bd039881f6ebef5bf191079ed546f7da7281d9d6123e8318391d2b1`;
D-T0-29 application-manifest SHA-256 is
`94d24507f9c6a9ae111f525262ac994dffd063cf51f9a4175d84c15cb1f787d3`.

The conditional D-PEC-75 O-A authority is therefore active for one bounded
WORKING_ITEMS production act. Only these paths are open:

- projects/pec/v2/config/loops.schema.json;
- projects/pec/v2/config/loops.json;
- projects/pec/v2/src/pec_v2/__init__.py;
- projects/pec/v2/src/pec_v2/core/__init__.py;
- projects/pec/v2/src/pec_v2/core/ports/__init__.py;
- projects/pec/v2/src/pec_v2/core/ports/loop_registry.py;
- projects/pec/v2/src/pec_v2/adapters/__init__.py;
- projects/pec/v2/src/pec_v2/adapters/config/__init__.py;
- projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py;
- projects/pec/v2/tests/config/test_loop_registry_contract.py;
- projects/pec/v2/tests/config/test_json_loop_registry.py;
- projects/pec/v2/tests/config/fixtures/missing_loop_id.json;
- projects/pec/v2/tests/config/fixtures/duplicate_loop_id.json;
- projects/pec/v2/tests/config/fixtures/malformed.json;
- projects/pec/software-workflow.json with exact packet §5.5 bytes;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_ACTIVATION.md;
- projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_REGISTERED_CHECKS.json;
- projects/pec/execution/_Coordination/D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md and manifest updates; and
- governed D-PEC-75 decision/register, PEC status, and loop-receipt updates
  required to record production and later owner gates.

WORKING_ITEMS must use the exact core/adapter contract in packet §5.3, exact
project-workflow bytes in §5.5, and all eleven producer checks in §5.6. Every
unlisted path and act remains closed.

## Strict non-effects and next return

This fan-in record and REVIEW make no further DEL-01-06 SOW change and create
no PEC source, test, adapter, configuration, project-workflow, or run-record
byte. They grant no domain-profile edit or adoption, lifecycle transition,
artifact acceptance, `ISSUED`, later P1 node, service/store/transport/runtime
act, release, professional reliance, or cross-loop mandate.

The exact-hash SOW-fitness and D-T0-27 effectiveness gates are satisfied.
Source production is `OPEN / READY FOR WORKING_ITEMS` only within the exact
fence above. Producer output remains candidate work; AC-001 through AC-006,
any post-production REVIEW, lifecycle transition, exact-hash artifact fitness,
`ISSUED`, release, and professional reliance remain separate later gates.
