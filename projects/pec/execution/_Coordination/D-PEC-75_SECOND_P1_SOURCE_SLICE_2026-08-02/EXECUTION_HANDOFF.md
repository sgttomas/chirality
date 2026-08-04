# D-PEC-75 O-A DEL-01-06 execution handoff

**State:** PRODUCER AND REVIEW MERGED / RF-001 DEFERRED / GATE 5 HOLD AT
`INITIALIZED`

**Authority basis:** D-PEC-75 O-A; owner-accepted SOW SHA-256
`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`;
D-T0-27 effective through PR #459 merge
`d9dc65804a0719fdf869af1ef60d53dc8cb0a895`

**Producer publication:** PR #462 source
`d4f53a70e4328101ba4756f0919b8bdb35cc9188`, merged as
`ccd9a2178ffd8029fdd1cd779910e954e0612e21`.

**Review publication:** PR #463 source
`922ca0ea68d255b65292d59db89a98ef4cf59bc5`, merged as
`a753a7b0894371437a6add0f92653037e2df2dec`; the exact review source is the
merge commit's second parent.

## Exact producer outputs

| Path | SHA-256 |
|---|---|
| `projects/pec/v2/config/loops.schema.json` | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` |
| `projects/pec/v2/config/loops.json` | `e24db354841e1b33d3ec4f74330351deaa7a18df0e0cd9e26bde248b6aed503e` |
| `projects/pec/v2/src/pec_v2/__init__.py` | `ae46d431c13413d5bcbb6ab60a97f6db09510dd97903c1f2a8586a3567b17c1e` |
| `projects/pec/v2/src/pec_v2/core/__init__.py` | `33c54e244e8e19b66cb2c53c81fa747979f6d512f227f7a56e3f8d57cfb9ff4a` |
| `projects/pec/v2/src/pec_v2/core/ports/__init__.py` | `669e1569216722509dcea0ae5ed42dc4a0ca856a196676568ee78d7a38a1edeb` |
| `projects/pec/v2/src/pec_v2/core/ports/loop_registry.py` | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` |
| `projects/pec/v2/src/pec_v2/adapters/__init__.py` | `8c80e607671eef1a35dca0334503deb151418c03b618af0c4577514d0184ef22` |
| `projects/pec/v2/src/pec_v2/adapters/config/__init__.py` | `7a9bdbc59b96d3c9f306af483d18d6c0b23b7071481fd6ab79204ba398513cba` |
| `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py` | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` |
| `projects/pec/v2/tests/config/test_loop_registry_contract.py` | `7147104bf077e0e041484d0e25a6626694237815c6b8cedfb879f52e98c5d8f0` |
| `projects/pec/v2/tests/config/test_json_loop_registry.py` | `3a8e9d6d85484232924d94f9a3834f843c5964c87e9a9524d09050e2e4763084` |
| `projects/pec/v2/tests/config/fixtures/missing_loop_id.json` | `3a04c92dd280f91a04c9e7916c7074ba260405dce5d65347f4870ff7f5590b4d` |
| `projects/pec/v2/tests/config/fixtures/duplicate_loop_id.json` | `b6573d451df18576821e40de440a113998d8fe8762ed35e34c513b9de1cacb06` |
| `projects/pec/v2/tests/config/fixtures/malformed.json` | `f37303491c50fa74756f547929f09c99900abfad5a9310cc2b46beb5027425b0` |
| `projects/pec/software-workflow.json` | `4ef630f4ab0bf51480ff83e3e8844e71cc827cf4ddddb1268c727a03d1b45cbc` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_REGISTERED_CHECKS.json` | `690ea5141051d6cbe68545d46512e641b20ddcea5e16cd8b363588ed7ca954ec` |

The companion activation record is
`projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-75_ACTIVATION.md`.

## Behavioral result

- `RegisteredLoop` is an immutable core value carrying only stable loop ID
  and the allowed semantic repository-relative LOOP_INIT locator.
- `LoopRegistry` is a core-owned typed port exposing only
  `registered_loops() -> tuple[RegisteredLoop, ...]`.
- `JsonLoopRegistry` is a replaceable outer adapter. Its path, JSON format,
  and located exception type do not enter the port.
- The P1 default contains exactly `pec` at
  `_DomainEngines/pec/LOOP_INIT.md`; later entries remain additive and
  deferred.
- Registry contents are non-authoritative locator configuration. The code has
  no ruling, lifecycle, mutation, dispatch, runtime, service, store, transport,
  or network integration, and no governed act depends on registry presence.

## Verification result

- Preconditions and reliance preflight: PASS.
- SOW: `PASS format=SOW_V1`; exact AC-001..AC-006 checklist reproduced.
- Five accepted D-PEC-74 API hashes: unchanged.
- Exact workflow profile and affected-check selection: PASS.
- Registered checks: PASS — API 6/6, registry 12/12, harness self-check.
- Explicit located failures: malformed JSON, duplicate ID, missing field,
  absent file, and unreadable path. Invalid input never returns a partial,
  empty, or silently defaulted set.
- Boundary/import checks: core imports no adapter or outer I/O; implementation
  imports only standard-library/PEC-local modules and no network module.
- VER-005 future DEL-01-05 enforcement rerun: `PENDING`, not passed.
- Strict registers: 64 / 254 / zero findings. Closure: 119 execution edges /
  zero SCCs.
- Exact path containment, manifest, current harness baseline, and whitespace:
  PASS. Committed-range coordination checking remains for CHANGE.

## SELF_CHECK disposition and remaining gates

The owner-authorized mechanical SELF_CHECK and its final dispositions are
recorded in immutable snapshots `REV_DEL-01-06_2026-08-02_1110` and
`REV_DEL-01-06_2026-08-02_1118`:

- AC-001 through AC-004: `PASS`;
- AC-005 and AC-006: `PARTIAL`, because VER-005's exact DEL-01-05
  enforcement rerun remains unavailable and was not silently passed;
- RF-001: `MAJOR`, `DEFERRED`, owner disposition `DEFER`; and
- Gate 5: owner `HOLD` at `INITIALIZED`.

The DEL-01-05 rerun remains a mandatory later SELF_CHECK input. When that
separately governed deliverable becomes available, RF-001 must be reopened and
SELF_CHECK rerun; VER-005 is not waived. The owner HOLD does not satisfy
AC-005 or AC-006 or accept the DEL-01-06 bytes. Lifecycle advance, exact-hash
artifact fitness, another P1 node, release, and professional reliance remain
separate owner acts.

This REVIEW result and the deliverable-local `_REVIEW.md`, findings register,
and `_LATEST.md` pointer are durable on main through the review publication
above. The named remaining owner gate is the post-rerun disposition of RF-001
and DEL-01-06 Gate 5, followed separately by exact-hash artifact fitness if the
evidence supports acceptance. No artifact byte is accepted and no next P1
node, `ISSUED`, release, or professional reliance is authorized by this
closeout.

OI-003 remains open. No long-term registry home/shape, later loop entry,
consumer activation, `ISSUED`, or other-loop duty is inferred.

## Supersession annotation — 2026-08-03

This file remains point-in-time evidence; none of the recorded historical acts
above is rewritten. The DEL-01-05 trigger later fired: exact VER-005 rerun
evidence SHA-256
`1e0bd26f5bcda92996ed66e6373a6c67f2fe23270e48c98688c5cf6d488a1210`
records AC-005 and AC-006 PASS and RF-001 `RESOLVED` without waiver. D-PEC-78
O-A and SCA-004 revision 1.4 resolved OI-003 and selected the existing
PEC-owned strict-version-1 JSON/schema paths and core-owned typed port as the
long-term registry home and shape.

The accepted DEL-01-06 SOW remains revision-1.3 history and is now separately
stale under RF-002; DEL-01-06 remains `INITIALIZED`. Current pointers are:

- `execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md`;
- `execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md`;
- `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REVIEW.md`;
- `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv`;
- `execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-03_1458/`; and
- `execution/_Coordination/PROJECT_SETUP_SCA004_METADATA_ALIGNMENT_2026-08-03/HANDOFF_STATE.md`.

No SOW repair, lifecycle, artifact acceptance, release, reliance, or
foreign-loop act is created by this annotation.
