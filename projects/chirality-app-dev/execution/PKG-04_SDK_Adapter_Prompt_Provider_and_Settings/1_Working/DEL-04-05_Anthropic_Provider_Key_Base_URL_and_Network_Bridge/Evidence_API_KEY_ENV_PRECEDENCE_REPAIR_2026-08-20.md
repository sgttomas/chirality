# Evidence — API-key environment precedence repair

Date: 2026-08-20
RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`

## Proven slice

The Electron daemon credential store now resolves Anthropic credentials in
the order required by `DEL-04-05-RQ-001`, `docs/SPEC.md` Section 12.3, and
`docs/PRD.md` FR-030:

1. persisted UI safeStorage credential;
2. `ANTHROPIC_API_KEY`;
3. `CHIRALITY_ANTHROPIC_API_KEY`.

The production repair is implemented in
`frontend/electron/api-key-storage.ts`. The credential store now uses one
provider-isolated resolver for both `get` and `status`; status exposes only the
non-secret discriminator `source: ui | env | none`, while preserving the
accepted fallback order above. The former self-expiring expected failure is
replaced by ordinary positive regression coverage in
`frontend/src/__tests__/electron/api-key-storage.test.ts` for stored UI
precedence, each environment variable alone, both variables together,
whitespace fallthrough, status-source classification, oMLX isolation, and an
unconfigured result. The runtime daemon serializes the complete status object,
so the held PKG-02 consumer can use this fact without inspecting credential
values or re-inferring source from its environment. Storage paths, safeStorage
behavior, process-global compatibility, corruption handling, and error
semantics are unchanged.

## Verification

- focused API-key storage Vitest: PASS, 1 file / 20 tests;
- full frontend Vitest: PASS, 150 files passed, 1 skipped; 1,167 tests passed,
  4 skipped;
- frontend plus Electron typecheck: PASS;
- frontend build: PASS;
- practitioner harness: PASS, 350 tests;
- repository self-check: exit 0, with the disclosed pre-existing 4 REVIEW / 31
  WARN baseline outside this node;
- APP-HOLD integrity: PASS, register match and zero held deliverables;
- APP-HOLD reliance for DEL-04-05, DEL-02-05, DEL-09-06, and DEL-09-04:
  ALLOW;
- amendment secret scan: PASS, 5,833 files and zero blocked findings;
- explicit two-path scope validation and diff whitespace: PASS;
- fresh Review 03: PASS, all 12 frozen v3 hashes matched, 100% of both
  product/test files and exact basis diff reviewed, zero actionable findings.

Primary evidence:

- `_run_records/TASK_RUN_2026-08-20_0939.md`
- `_run_records/TASK_RUN_2026-08-20_0939_REGISTERED_CHECKS.json`
- `execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/FROZEN_DIFF_MANIFEST_V3.md`
- `execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_REGISTERED_CHECKS_V2.json`
- `execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-PKG04-API-KEY-STATUS-SOURCE-REVIEW-03/RETURN.md`

## Calibration

This evidence proves the RQ-001 precedence slice and the PKG-04-owned
non-secret status-source fact required by dependent DEL-02-05-R03. It removes
the specific Receipt-180 store-side blocker for downstream consumers, but N2
must still consume the discriminator and N3 must still re-run packaged proof.
It does not independently re-prove every broader OUT-001/AC-001/VER-001
network, redaction, packaging, or provider-error claim; it does not transition
lifecycle, alter Remaining, change the Checking Approval SHA, or make a
release/readiness claim.
