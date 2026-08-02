# D-PEC-75 O-A — DEL-01-06 source-production activation

**State:** PRODUCER COMPLETE / CANDIDATE OUTPUT / REVIEW AND OWNER GATES OPEN

**Run date:** 2026-08-02

**Manager:** WORKING_ITEMS, managed by HELP_HUMAN

**Package / deliverable:** PKG-01 / DEL-01-06 only

**Authority:** D-PEC-75 O-A, packet §§5.3–5.8 and §8–9

## Preconditions

- Owner-accepted SOW SHA-256:
  `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`.
- Final contract REVIEW snapshot:
  `projects/pec/execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-02_0954/`;
  six of six checklist rows populated, zero findings, Gate 5 `HOLD`, lifecycle
  `INITIALIZED`, exact SOW fitness owner-accepted.
- D-T0-27 effective identity: PR #459 merge
  `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; adopted live profile SHA-256
  `be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`.
- Pre-production D-PEC-75 outer manifest SHA-256:
  `702ef2c03e4b4ad160274eee2b055e3f73dc8aae7ee2c811eca7c9f7ffb1e133`;
  all entries verified.
- Active-reliance-hold preflight for `dispatch-for-production`: `ALLOW`.
- SOW validation: `PASS format=SOW_V1`; checklist remains exactly AC-001
  through AC-006.

## Frozen work graph

One serialized WORKING_ITEMS integration node owned all source, config, test,
fixture, profile, and evidence writes. Its dependencies were the four
preconditions above; its fan-in gate was all eleven packet §5.6 checks. No
concurrent writer, brief amendment, scope expansion, or cross-package act
occurred.

## Producer outputs

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
| `D-PEC-75_REGISTERED_CHECKS.json` | `690ea5141051d6cbe68545d46512e641b20ddcea5e16cd8b363588ed7ca954ec` |

The core owns immutable `RegisteredLoop` and the `LoopRegistry` capability
port. The JSON path, serialization, and adapter exception remain outside that
port. The checked-in default contains exactly `pec` at
`_DomainEngines/pec/LOOP_INIT.md`. This semantic locator grants no authority,
and no governed act depends on the registry.

## Verification

1. D-T0-27 effectivity and reliance preflight: PASS.
2. Accepted SOW and exact AC-001..AC-006 checklist: PASS.
3. Five accepted D-PEC-74 API hashes: unchanged.
4. Exact §5.5 workflow profile: byte-equal; every O-A path selects
   `v2-loop-registry` plus always-run `v2-api-contract` and
   `harness-self-check`.
5. Registered checks: all PASS — six API tests, twelve registry tests, and
   harness self-check.
6. Valid-single-loop, malformed, duplicate, missing-field, absent-file, and
   unreadable-path cases: exercised; failures are explicit and located.
7. Core boundary: no adapter/outer-I/O import; port exposes only
   `registered_loops() -> tuple[RegisteredLoop, ...]`; no path, JSON,
   serialization, or adapter exception leaks. `loop_init_path` remains
   semantic locator data.
8. Imports: standard library or PEC-local only; no network module or call.
   VER-005's later DEL-01-05 enforcement rerun remains `PENDING`, not passed.
9. Strict registers: 64 / 254 / zero findings. Dependency closure: 119 edges /
   zero SCCs.
10. Exact-path containment, manifest, current harness self-check baseline, and
    whitespace: PASS. CHANGE must rerun `coord-check` over the eventual
    committed range.
11. No frozen-corpus, store, service, transport, runtime, external-network,
    other-loop, lifecycle, ruling, Task Management, decomposition, PRD,
    accepted ADR/SPEC, or unlisted-profile write occurred.

## Handoff and authority fence

Producer fan-in is complete candidate work. It does not accept an artifact,
satisfy an AC by owner act, change DEL-01-06 from `INITIALIZED`, mark it
`ISSUED`, open a later P1 node, release, merge, or create professional-reliance
authority. OI-003 remains open and the local JSON format remains replaceable.

Recommended next gate is owner selection of `SELF_CHECK` and explicit review
from `INITIALIZED` using AC-001 through AC-006. The review is mechanical only;
finding disposition, Gate 5, exact-hash artifact fitness, later P1 work, and
publication remain separate acts.
