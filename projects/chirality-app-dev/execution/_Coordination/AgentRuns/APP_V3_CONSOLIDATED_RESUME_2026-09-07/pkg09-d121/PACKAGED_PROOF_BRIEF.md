# Sealed future brief — D121 PKG09 packaged security proof

Status: `READY_TO_FREEZE_AFTER_CARRIER_APPLICATION`; do not dispatch from this draft until HELP_HUMAN supplies every pending identity and releases the process lane.

RequestedBy: HELP_HUMAN

RunID: to be assigned by parent

ParentInstanceID: PKG09 WORKING_ITEMS instance named by parent

ChildInstanceID: to be assigned

Role: TASK Agent 2, `TaskSkill: software-bounded-implementation`

Model: `gpt-5.6-sol`

Reasoning: `medium`

ForkTurns: `none` or a positive bounded value selected by parent

RoleEnforcement: delegated-harness-native, instruction-asserted; Agent 2 must not delegate.

PackageID: `PKG-09`

DeliverableID: `DEL-09-06`

RemainingItem: `DEL-09-06-V3-07`

Trace: `OUT-001`, `AC-001`, `VER-001`, retained `DEL-09-06-REQ-005/006/014/015`.

Objective: extend the existing packaged-security proof and its unit test for the exact frozen D121 candidate. Own only loci 11 and 12. Prove the accepted security assertions without changing production policy or relaxing the design.

AcceptedBasis, to be frozen literally before dispatch:

- D121 ruling SHA-256 `fa410ae195c74fab2ad3de7cb5d64e244a327905ea3d1f76849f6b51fb74caeb`.
- D121 design SHA-256 `c42f617eafd3cce21047d4cf5977fd058207ef55fd8b090b337b2422f62bc687`.
- Accepted carrier patch SHA-256 `e37b19f489ad616b272e8f2aa511208bc7c32487cfbbc90734e12c18d222bb32` and observable applied-carrier bytes/checks/run records on the run branch; no separate carrier merge is required solely by D121.
- Parent-supplied exact commit and SHA-256 identities for all twelve approved loci after PKG02 freezes loci 1–10.
- Parent-supplied accepted PKG02 implementation return and full frozen diff identity.
- Fresh APP-HOLD dispatch result for DEL-09-06.
- Current pre-freeze PKG09 proof-locus hashes are orientation only: script `99249b5d00d215a989aad884ac2ab1d0b4238d6e19e07cb8faa651b6212e2d51`; test `a92e42b559a39c65dff3d0836fa1d50918ffed00a4e8aa4ddb90a0fc427263b7`. Replace these with parent-frozen current hashes at dispatch.

DeclaredReads: all twelve frozen loci; D121 ruling/design/carrier evidence; DEL-09-06 SOW/status/dependencies; existing packaged-security proof evidence and registered validation instructions; installed Electron/Next code cited by the accepted design when needed to interpret output.

AllowedTools: read, bounded edits to the two allowed loci, exact registered unit/check commands released by parent. Native/package/browser/build launches require the separately serialized parent process-lane release.

AllowedWriteTargets:

1. `projects/chirality-app-dev/frontend/scripts/run-packaged-security-proof.mjs`
2. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`
3. The exact run-local author evidence directory named by parent.

EXCLUSIONS: the first ten D121 loci; package scripts; lockfiles; dependencies; any new file/locus; IPC/capability API; broad `/api` exemption; alternate renderer; policy weakening; environment bypass; live supplier/provider; credentials; protected fixture; signing; distribution; publication; lifecycle, release-readiness, or capability acceptance.

Required proof coverage:

- central finalizer is the sole trusted classification/policy owner; reserved marker spoof/reflection, sole-emitter, duplicate/conflicting header, unexpected CSP, status/method/path/origin and selector/descriptor negatives fail closed;
- packaged and development policy parity, including `writeHead` overloads, `flushHeaders`, implicit `write`/`end`, one-shot restoration, errors, redirects, late headers, and unchanged nonce HTML CSP for `/`, `/chat`, `/pipeline`, `/workbench`;
- exact raw/normalized encoded-path, dot-segment and duplicate-slash findings; foreign/blob/data/file/extension/object/webview/wildcard framing remains denied;
- `.pdf`, `%PDF-`, opened-descriptor containment/identity, regular-file, positive-size, instruction-root/`.git`, unknown/duplicate selector and mutation controls;
- full-response semantics: Range/If-Range ignored with 200, no `Accept-Ranges` or `Content-Range`, bounded streaming, first-read/precommit/postcommit failure, cancellation/disconnect and exactly-once descriptor close;
- actual unsigned unpublished packaged readable multi-page PDF and page navigation through the right panel; iframe load or HTTP 200 alone is insufficient; record internal-viewer resource observations and any range requirement;
- preserved window/IPC/egress controls, nonce equality/freshness, no foreign/other-resource framing or control regressions.

ExpectedOutputs: two-locus source/test diff; per-file pre/post hashes; focused unit output; machine-readable proof result and canonical stdout/stderr; exact package/source/fixture/image/tool/runtime identities; sorted recomputable manifest; cleanup evidence; bounded rerun instructions; calibrated return stating `PASS`, `FAIL`, or `BLOCKED` without inferring publication capability.

AcceptanceCriteria: no writes outside the three declared targets; 100% required matrix represented and executed where the released lane permits; exact frozen source remains unchanged during proof; native readable multi-page/page-navigation PASS under the restrictive policy; all applicable registered gates pass; evidence is independently recomputable; fresh separate `TASK + software-code-review` reviews 100% of the complete frozen D121 diff and returns PASS. The reviewer has no write target and must not be the author context.

Escalation: stop and return to HELP_HUMAN on any source drift, missing process lane, additional-locus need, policy relaxation, package/lock/dependency need, Chromium range requirement, native failure, malformed/mutation ambiguity, incomplete cleanup, or evidence gap. Failure keeps published `inlinePdfPreview` false; success qualifies only the unchanged isolated candidate and does not authorize publication.
