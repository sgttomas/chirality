# DEL-01-05 exact-hash acceptance packet

**Status:** PRESENTED FOR OWNER RULING
**Committed basis:** main merge commit
`379b8b19b12b29eda4fa307e497499d6fe414f8a`
**Deliverable:** DEL-01-05
**Lifecycle:** `INITIALIZED` under standing HOLD
**Review type:** `INDEPENDENT_VERIFICATION`; review from `INITIALIZED` was
previously authorized

## 1. Fitness result

**Recommendation: ACCEPT the exact candidate inventory below.** RF-001 and
RF-002 are owner-dispositioned `REVISE / RESOLVED`; the independent review has
zero open findings. The revised checker/test pair passes all 19 enforcement
tests, the live posture returns dependency/locality/registration `PASS` with
zero findings and `PEC_RELEASE_BLOCKING`, all 18 activation inventory rows
reproduce, and the final D-PEC-77 manifest reproduces 7/7.

This recommendation concerns only the exact bytes listed here. It does not
itself satisfy AC-010 or AC-011, advance lifecycle, accept another artifact,
close TM-PEC-009, release PEC, or authorize professional reliance.

## 2. Exact candidate artifact inventory

| Artifact | SHA-256 |
|---|---|
| `projects/pec/v2/config/service_core_posture.json` | `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed` |
| `projects/pec/v2/tools/check_service_core_posture.py` | `3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643` |
| `projects/pec/v2/docs/SERVICE_CORE_POSTURE.md` | `7448c86628c51179eb611536fbcb48914ef900678993cd63a1a820b464f9e489` |
| `projects/pec/v2/tests/enforcement/test_dependency_assertion.py` | `0de9c85f1613a204eef1a0357cf4ec20d72646d21170553d7737e804ec68c9cf` |
| `projects/pec/v2/tests/enforcement/test_locality_assertion.py` | `69051b4c127009c821886c4cc6aea70222f57c3ad51013bdebe53a6211d92d20` |
| `projects/pec/v2/tests/enforcement/test_gate_registration.py` | `9e9519e6eaded2e9db427a6609c5880c5316f6528facae80776307793bb0071d` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/conforming/core/app.py` | `8966d0088ea15ad37854ecfd0f4869c67b61ce5f8809848d380f1fb858e450a0` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/core/app.py` | `206cc544fa564634ea413a2e6ff1eed7cb062d5c5cf7a2b4e8156c4fede7d416` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/workspace_contract/contracts/chirality_contracts/__init__.py` | `e38af91183e30927c8d990a76ba715f3e1f300ac1e6b489a2408b48741632522` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_direct/core/app.py` | `2f691060cef7a41af2530909638f9612725eab441b515ac10f37071ee15c8870` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/app.py` | `48f739f0169f93a303c2c754209ecdc343b4aa7607ee750bc3c943377902d0bc` |
| `projects/pec/v2/tests/enforcement/fixtures/dependency/third_party_transitive/core/helper.py` | `476b8cef2afeabe4dddd5173009cee02a7a709e6ebadfe886160a1f4c3000fe9` |
| `projects/pec/v2/tests/enforcement/fixtures/locality/external_call/core/app.py` | `44a1f3d683fc27ef15595f9dacfdd37f98476eac6ec4b88da4cd43ba8b472e31` |
| `projects/pec/v2/tests/enforcement/fixtures/locality/external_config/core/settings.py` | `54671ebf7071f04e3d2cea8411895d9429c84036efa82f7223aa7c440d2d9bad` |
| `projects/pec/v2/tests/enforcement/fixtures/locality/local_unix/core/app.py` | `c35fff6dba0aaa2d114b0d4e252d561d361979254e4ecf91cdd6c16236f7d425` |
| `projects/pec/v2/tests/enforcement/fixtures/locality/local_loopback/core/app.py` | `f9ec548b059cdcbc1080da4c0f53ef97d5cf7e9a7b75ce5ad12c74a9b86be091` |
| `projects/pec/software-workflow.json` | `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b` |

## 3. Exact fitness/reproducibility evidence

| Evidence | SHA-256 / result |
|---|---|
| Normalized activation record | `992926ad5651f949dc9b15e2b211c078ab559ee054a6b6472c6c0990860bd4b2`; 18/18 inventory rows reproduce |
| Registered checks record | `074f0a155c0471b1c3f16e9bb37be75ce77173b37f8efd6585ff11e07cff1812` |
| Resealed D-PEC-77 manifest | `3fb4c499213203c594353fa6c63d3eb2b05289cd6912a7292d5c21d885671fe8`; 7/7 rows reproduce |
| Final deliverable review | `f3c4b935c9ace5b3808298bfe0c78e0e15ba6f295522cc6e4b088c1f7a7c5195` |
| Final findings register | `414339c78c45598ff75d247f7456c30c5b37b7b440b39a2d37c064db391ac00a`; RF-001/RF-002 resolved, zero open |
| D-PEC-77 decision | `7eb123ea93facc3b1a6a42626afd11d3c2ce44c45396af626b74ca6642df34d0`; O-A / G-A |
| DEL-01-05 status | `f7cb08a6e229b6195a239547c09b47f00cdccd73a723f93ea05a8cb25feae9d9`; `INITIALIZED` |
| Enforcement tests | 19/19 PASS on committed main |
| Live posture | dependency/locality/registration PASS; zero findings; exact config/workflow/core-tree hashes; `PEC_RELEASE_BLOCKING` |

The inherited practitioner-harness generated-disclaimer finding is preserved
in the historical registered-check record and is outside DEL-01-05's exact
path/act fence. Repository PR checks `harness` and `pec` both passed on source
head `90fe520363338018f07c5de9c7827832971a4a4f` before merge
`379b8b19b12b29eda4fa307e497499d6fe414f8a`.

## 4. AC-010 confirmation

### Exact criterion

> An accountable owner confirms that neither the posture note nor either
> assertion resolves, pre-empts, or forecloses `OI-009` / `SOW-083`, and that
> the enforcement makes no governed act depend on PEC-held state.

### Exact evidence

- Accepted SOW SHA-256
  `53ba3be304151a35775eb9e117c28f1b7564a19f4dd5076869a7f73994e5de53`,
  output/evaluation matrix lines 154 and criterion AC-010.
- Posture note SHA-256
  `7448c86628c51179eb611536fbcb48914ef900678993cd63a1a820b464f9e489`,
  lines 40–44: read-only checker, no network/service/write/authoritative state,
  graceful absence; lines 46–52: OI-009/SOW-083 remains open and is neither
  authorized nor pre-empted.
- Checker SHA-256
  `3d88b013e967a66d9cb6a8e5ac9d5f9511c99d02aea04525d2f47bf74ce31643`
  and live result: reads repository state only, zero findings, no network or
  source write.
- Independent review SHA-256
  `f3c4b935c9ace5b3808298bfe0c78e0e15ba6f295522cc6e4b088c1f7a7c5195`:
  AC-003 PASS under external/local and transport-neutral controls; AC-008 and
  containment CU-001 PASS; AC-010 remains solely this owner confirmation.

**Recommended owner act:** `DEL-01-05 AC-010 — CONFIRM` on the exact accepted
candidate inventory. A decline leaves AC-010 unsatisfied and Gate 5 on HOLD.

## 5. AC-011 confirmation

### Exact criterion

> An accountable owner confirms, or declines to confirm, that the enforcement
> delivered under this contract carries release-gating authority — that its
> blocking verdict blocks a release candidate — given that `C-08`'s
> standing-node classification carries "owner confirmation requested" and was
> accepted at `D-PEC-62` §1.4 as a recorded-but-unresolved, non-gating
> annotation (CLM-006, CON-002). A decline leaves the mechanism's verdicts
> advisory and invalidates no other criterion in this contract; the standing
> framing of the contract stands either way, because it is how the contract is
> written rather than a claim about the gate's force.

### Exact evidence and faithful choices

- D-PEC-77 decision SHA-256
  `7eb123ea93facc3b1a6a42626afd11d3c2ce44c45396af626b74ca6642df34d0`
  records owner-selected `CON-002: G-A`: failed, missing, or unevaluated
  enforcement blocks a PEC release candidate only.
- Workflow SHA-256
  `cad1d94bff71ffbefae9e550f847a2bc2cabd2a2a090536d22210838b8760c0b`
  registers `v2-core-posture` as an always-run check and binds all enforcement
  paths to it.
- Posture note SHA-256
  `7448c86628c51179eb611536fbcb48914ef900678993cd63a1a820b464f9e489`,
  lines 32–44, states the exact PEC-only release force and cross-loop boundary.
- Live checker returns `release_force = PEC_RELEASE_BLOCKING`; registration,
  missing-check, disabled-check, withheld-check, and violation fixtures fail
  closed; independent review records AC-005 PASS mechanically.

**Option A — CONFIRM G-A (recommended):** the exact delivered enforcement's
failed, missing, or unevaluated verdict blocks a PEC release candidate only.
It grants no Git veto, cross-loop force, lifecycle act, release act, or
professional-reliance authority.

**Option B — DECLINE / advisory:** the exact mechanism remains advisory. This
satisfies AC-011 as a recorded declination under the contract, invalidates no
other criterion, and requires authority-neutral status prose before lifecycle
advancement if any live artifact currently asserts blocking force.

## 6. REVIEW Gate 5 proposal

If the owner accepts the exact candidate inventory, confirms AC-010, and
confirms AC-011 Option A, REVIEW recommends:

`DEL-01-05 Gate 5 — RECOMMEND_ADVANCE from INITIALIZED to CHECKING under the recorded review-from-INITIALIZED override.`

Evidence: the deterministic eleven-item checklist is populated; AC-001 through
AC-009 pass mechanically; AC-010/AC-011 would be owner-confirmed; both MAJOR
findings are `REVISE / RESOLVED`; zero finding remains open; the exact
candidate and final manifest reproduce. The transition would be lifecycle-only
and would not issue the deliverable, release PEC, close TM-PEC-009, or
authorize professional reliance.

If artifact fitness is declined, AC-010 is not confirmed, or AC-011 selects
the advisory alternative without any required authority-neutral repair,
REVIEW recommends `HOLD` at `INITIALIZED` and returns the exact blocker.

## 7. Contingent DEL-01-06 / TM-PEC-009 sequence

Only after the owner acceptance and DEL-01-05 confirmations above, REVIEW may
reopen DEL-01-06 RF-001 and rerun its exact six-item SELF_CHECK with VER-005
bound to this accepted DEL-01-05 inventory. That rerun is not performed by
this presentation packet. Its later result controls the evidence needed for
TM-PEC-009 closure; no VER-005 waiver is available.

## Owner ruling interface

1. `DEL-01-05 artifact fitness — ACCEPT` or `REJECT`, bound to this packet's
   exact inventory.
2. `DEL-01-05 AC-010 — CONFIRM` or `DECLINE`.
3. `DEL-01-05 AC-011 — CONFIRM G-A` or `DECLINE / advisory`.
4. `DEL-01-05 Gate 5 — APPROVE advance to CHECKING` or `HOLD`.
