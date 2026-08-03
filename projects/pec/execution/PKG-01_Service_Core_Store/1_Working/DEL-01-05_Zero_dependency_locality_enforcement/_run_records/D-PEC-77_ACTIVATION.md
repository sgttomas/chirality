# D-PEC-77 phase-2 activation evidence

**Status:** RF-002 REVISED CANDIDATE / INDEPENDENT REVIEW RERUN OPEN
**Date:** 2026-08-03
**Deliverable:** DEL-01-05
**Packet:** `execution/_Coordination/D-PEC-77_DEL-01-05_ENFORCEMENT_2026-08-02/PACKET.md`
**Packet SHA-256:** `f848d55557d4b59d4c425e3924b850d634011a4a7db6c6fbd2eee9fc46cc5c31`
**Accepted production contract SHA-256:** `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`

## Authority and boundary

The owner selected D-PEC-77 O-A and G-A, then accepted the exact
`ScopeOfWork.md` bytes above as the DEL-01-05 production contract and opened
packet phase 2. This record binds the resulting candidate bytes and required
verification. It accepts no produced artifact or acceptance criterion,
changes no lifecycle state, reopens no DEL-01-06 finding, closes no Task
Management row, and authorizes no release or professional reliance.

The phase-2 producer session did not return a complete manager fan-in. The
HELP_HUMAN shared integration owner completed only the missing bounded
phase-2 files and verification inside the packet's exact path and act fence;
the interrupted child return remains preserved in the Agent 0 run evidence.

## Candidate artifact inventory

| Path under `projects/pec/` | SHA-256 |
|---|---|
| `v2/config/service_core_posture.json` | `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed` |
| `v2/tools/check_service_core_posture.py` | `3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643` |
| `v2/docs/SERVICE_CORE_POSTURE.md` | `7448c86628c51179eb611536fbcb48914ef900678993cd63a1a820b464f9e489` |
| `v2/tests/enforcement/test_dependency_assertion.py` | `0de9c85f1613a204eef1a0357cf4ec20d72646d21170553d7737e804ec68c9cf` |
| `v2/tests/enforcement/test_locality_assertion.py` | `69051b4c127009c821886c4cc6aea70222f57c3ad51013bdebe53a6211d92d20` |
| `v2/tests/enforcement/test_gate_registration.py` | `9e9519e6eaded2e9db427a6609c5880c5316f6528facae80776307793bb0071d` |
| `v2/tests/enforcement/fixtures/dependency/conforming/core/app.py` | `8966d0088ea15ad37854ecfd0f4869c67b61ce5f8809848d380f1fb858e450a0` |
| `v2/tests/enforcement/fixtures/dependency/workspace_contract/core/app.py` | `206cc544fa564634ea413a2e6ff1eed7cb062d5c5cf7a2b4e8156c4fede7d416` |
| `v2/tests/enforcement/fixtures/dependency/workspace_contract/contracts/chirality_contracts/__init__.py` | `e38af91183e30927c8d990a76ba715f3e1f300ac1e6b489a2408b48741632522` |
| `v2/tests/enforcement/fixtures/dependency/third_party_direct/core/app.py` | `2f691060cef7a41af2530909638f9612725eab441b515ac10f37071ee15c8870` |
| `v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/app.py` | `48f739f0169f93a303c2c754209ecdc343b4aa7607ee750bc3c943377902d0bc` |
| `v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/helper.py` | `476b8cef2afeabe4dddd5173009cee02a7a709e6ebadfe886160a1f4c3000fe9` |
| `v2/tests/enforcement/fixtures/locality/external_call/core/app.py` | `44a1f3d683fc27ef15595f9dacfdd37f98476eac6ec4b88da4cd43ba8b472e31` |
| `v2/tests/enforcement/fixtures/locality/external_config/core/settings.py` | `54671ebf7071f04e3d2cea8411895d9429c84036efa82f7223aa7c440d2d9bad` |
| `v2/tests/enforcement/fixtures/locality/local_unix/core/app.py` | `c35fff6dba0aaa2d114b0d4e252d561d361979254e4ecf91cdd6c16236f7d425` |
| `v2/tests/enforcement/fixtures/locality/local_loopback/core/app.py` | `f9ec548b059cdcbc1080da4c0f53ef97d5cf7e9a7b75ce5ad12c74a9b86be091` |
| `software-workflow.json` | `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b` |
| `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_run_records/D-PEC-77_REGISTERED_CHECKS.json` | `074f0a155c0471b1c3f16e9bb37be75ce77173b37f8efd6585ff11e07cff1812` |

## Packet §3.5 verification

1. Reliance preflight returned `ALLOW` for `dispatch-for-production`,
   `rely-for-production`, and `candidate-validation` against the applicable
   SOW, checker, and handoff targets.
2. `validate_scope_of_work.py` returned `PASS format=SOW_V1`; the deterministic
   checklist reproduces exactly eleven ordered rows, AC-001 through AC-011,
   bound to accepted SOW SHA-256
   `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`.
3. The dependency suite proves conforming standard-library and explicit
   workspace-contract PASS results plus located direct and transitive
   third-party BLOCK results.
4. The revised locality suite proves located external-call and
   external-endpoint BLOCK results through deterministic import-binding and
   AST call resolution, including aliased modules/symbols, assigned or aliased
   socket instances/bound methods, and inline socket constructors. Unix-domain
   and loopback-only forms remain PASS, and an explicit test proves the
   classifications are identical under both readings of OI-009.
5. Fault injection proves absent and malformed inputs, absent core,
   unclassifiable dynamic imports, and induced tooling failure all fail
   closed.
6. Scratch workflow mutation proves disabled and removed
   `v2-core-posture` registration fail closed.
7. The live posture run is `PASS` and binds configuration SHA-256
   `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed`,
   core-tree SHA-256
   `2c830d1fe9bc7f550c47d5f22223f330a3a95118360e61bb6d9c785b47c151ca`,
   and workflow SHA-256
   `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b`.
   The fixture tests recompute state and do not reuse prior results.
8. The checker is Python-standard-library only, contains no network call or
   write path, and a full run leaves `v2/src/pec_v2/core/**` and the accepted
   dependency/configuration surfaces outside the packet path list unchanged.
9. Element-by-element inspection of `SERVICE_CORE_POSTURE.md` reproduces
   REQ-009 definitions and every REQ-010 posture element, preserves OI-009 /
   SOW-083 as open, and makes no completion claim.
10. `software-workflow.json` reproduces the packet §3.4 semantic postimage.
    Affected-check selection returns all four checks. The registered run
    records API contract 6/6 PASS, loop registry 12/12 PASS, and core posture
    PASS. `harness-self-check` runs but returns the inherited repository
    baseline described below, so the aggregate registered-check status is
    honestly `FAIL` rather than a false pass.
11. `git diff` is empty for accepted D-PEC-74 and D-PEC-75 source paths outside
    the exact phase-2 list, including `v2/contracts/api/**`,
    `v2/config/loops*.json`, `v2/tests/config/**`, and `v2/src/**`.
12. Strict decomposition validation passes at 64 registers / 254 rows / zero
    errors or warnings. Dependency closure reports 119 execution edges and
    zero nontrivial SCCs or bidirectional pairs.
13. Graceful-absence and unreadable-surface tests fail explicitly without
    starting any service or network operation. The repository harness parity
    run reproduces one inherited `GENERATED_DISCLAIMER_MISSING` BLOCK at
    `_harness_generated/codex-pec-dpec75-registered-verify-20260802.json`,
    plus REVIEW=4, WARN=31, INFO=14, and NOT_APPLICABLE=1. Receipt 146 already
    records this generated-output-labeling BLOCK as outside D-PEC-77/78. No
    repair to that foreign generated artifact is authorized here.
14. All product and evidence writes are contained by packet §3.2. `git diff
    --check` passes. RF-001 deliberately reserves the packet-manifest reseal
    as the final act after every other candidate/review/evidence update lands.
    Committed-range `coord-check` remains a later CHANGE/Git-gate rerun because
    this candidate tranche is not committed.

## RF-002 revision evidence

The owner dispositioned RF-002 `REVISE`. WORKING_ITEMS replaced exact local
spelling assumptions with import-derived canonical bindings, fixed-point
callable/class/instance alias propagation, and AST receiver resolution. The
three exact review sources at SHA-256 `303b635b082646ef9b62979f779960a5a513ed8d9cafb489a431af9742095eaa`,
`ad74e807c6ffcb555cc84fe342bb131717423ad4bb3ec4f1c510564ae0627d4a`,
and `5c765f1daa1b8989dabf39c54658625a0f107aebbc5808847b49ad8f7b68de4a`
each now return overall/locality BLOCK with a located finding.

Producer-side novel probes cover an aliased `http.client` factory and an
aliased socket class/instance/bound method as BLOCK, while aliased Unix-domain
and inline IPv6 loopback forms remain PASS. The bounded producer return is
SHA-256 `33fe3d31f6ee092ce7fb31c35bada9984eb153b9512493ad60c0476817357bcc`.

The enforcement test command completed 19/19 PASS. The live checker reports
dependency/locality/registration `PASS` and `release_force` =
`PEC_RELEASE_BLOCKING`, faithfully implementing selected G-A for PEC release
candidates only.

## Open gates

These bytes are candidate producer output. REVIEW type, any review from
`INITIALIZED`, findings and Gate 5, AC-010, AC-011, exact-hash artifact
fitness, DEL-01-06 RF-001/VER-005 rerun, Task Management closure, release, and
professional reliance remain separate gates.
