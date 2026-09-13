# Independent dependency and production-probe review

Verdict: **PASS — no actionable finding in the frozen source repair or the bounded probe design.** This is source/security engineering review, not a passed HTTP execution, a repaired signed artifact, owner acceptance or publishing approval.

Candidate: `61ca362a2c9ffd1e73028bf3550515ebad7ad74d`. Base: `9eaddb5965642a783ad700743eecdf876e9e0104`. All eleven changed files were read, including the complete lock change through textual and structural comparison. Product changes are exactly package.json, package-lock.json and next.config.mjs. The other eight files are campaign/packaging/advisory evidence. The explicitly authorized external probe was read in full and is identified below.

Reviewer: independent TASK / Type 2, gpt-6-astra high, `/root/candidate_independent_review`, under the parent's standing bounded security/packaging exception. Same previously declared Root/App/TASK/software-code-review basis. No delegation, product edit, dependency install, audit rerun, test/probe execution, build, signing, App operation, protected-state access or Git mutation. Only this return was written. Precise public advisory pages, source, installed dependency code/package metadata and the specified probe were inspected.

## Dependency and lock correctness

- Next changes from exact 15.5.21 to exact 15.5.25. Next/env and all recorded SWC binaries agree on 15.5.25. The new Next optional sharp range accepts 0.35.4.
- The existing sharp override changes only from 0.35.3 to 0.35.4. Its native packages and libvips package pins move coherently to 0.35.4 and 1.3.3. The emnapi runtime update 1.11.2 → 1.11.3 satisfies the new wasm dependency's minimum. CPU/OS/engine/license/dev flags are not changed by the repair.
- The sole recorded frontend nanoid instance moves 3.3.16 → 3.3.18, satisfying PostCSS's unchanged ^3.3.16 range. No direct nanoid dependency, new override or major-version change remains.
- Independently parsed old/new lockfiles: **40 changed package records including root; zero added or removed records**. Every change belongs to these closures; non-version changes are the corresponding dependency pins/ranges and root Next pin. Unrelated Runtime link metadata and legacy dependency integrity records remain unchanged. Root dependency/devDependency maps match package.json exactly. Changed tarball URLs remain the npm registry and SHA-512 integrity entries remain present and structurally valid; this is not an independent tarball-content verification.
- Read installed package manifests independently: Next 15.5.25, sharp 0.35.4 and nanoid 3.3.18 match the lock. All three final source hashes match the author's frozen hashes. No new clean-install or native sharp execution was performed by this reviewer.

## Precise security basis

The cited Next AVIF advisory identifies 15.5.24 as the first patched 15.5 release, so 15.5.25 is outside its affected range. The separate Windows-hosted Next advisory has the same patch boundary; the preserved macOS artifact's missing Windows precondition must remain a specific platform observation, not a general safety claim. Sources: [Next AVIF advisory](https://github.com/advisories/GHSA-2xp9-vwfh-vxw4), [Next Windows advisory](https://github.com/advisories/GHSA-p293-qw3h-jr36).

The targeted sharp/libheif advisory names sharp 0.35.4 as patched. The nanoid size-zero custom-generator advisory names 3.3.18 as the patched 3.x version. The chosen pins therefore address the specific reported ranges without requiring a broader migration. Sources: [sharp advisory](https://github.com/advisories/GHSA-rgj7-g3m4-5g8c), [nanoid advisory](https://github.com/advisories/GHSA-2v37-7h3g-55p8).

PostCSS 8.5.22 remains affected by the disclosed moderate sourceMappingURL issue when from is absent; the advisory identifies 8.5.23 as patched. Its presence remains a residual warning, not an assertion that this App exposes the vulnerable processing path. The scoped repair does not change that package or claim all vulnerabilities are removed. [PostCSS advisory](https://github.com/advisories/GHSA-fxqj-rqcc-2cmp).

Author reports production audit **0 high / 0 critical, 2 moderate package rows**, with the Next moderate row propagated from PostCSS; audit still exits 1. Full audit remains **9 high / 9 moderate / 1 low**, with no critical. Independently inspected every lock node for the reported remaining high package families (Pi, xmldom, ajv, brace-expansion, fast-uri, ip-address, js-yaml, minimatch, undici): all are dev:true. That supports the frontend production-closure distinction; it does not make their tooling use safe. Historical ASAR/source-map exclusion evidence was read as attributed packaging evidence, not independently repeated against an artifact. Runtime workspace dependencies were not changed.

## Optimizer removal and probe validity

`images: { unoptimized: true }` is the supported configuration and leaves the other Next settings intact. Search of product src/electron surfaces outside tests found no next/image, optimizer endpoint, imageOptimizer or sharp caller. Local artifact rendering does not depend on this endpoint in the inspected source.

Read the installed Next 15.5.25 handler directly: it checks the unoptimized setting and returns render404 before parameter validation, source fetching or image decoding. Optimizer definitions/cache objects can load before the guard; disabling the endpoint does not mean sharp packages disappear. The later handler path would return 400 for missing parameters if optimization were enabled. No maintained test based on extracting private upstream source delimiters remains in the candidate.

Reviewed `/Users/ryan/.claude/chirality-user-journeys-20260913/verify-production-image-endpoint.mjs`, SHA-256 `9c6ec80733070019c0305328c265e4522df36d1fb2161695874727dfd6aa6132`:

1. It resolves the explicitly supplied frontend root and loads that root's installed Next. `next({dev:false, dir:frontendRoot})`, prepare and the normal request handler match the production factory/handler used by Electron. Its server binds a newly assigned port only on 127.0.0.1.
2. The ordinary root page must return 200 and contain Chirality. A script URL extracted from that actual HTML must then return 200 with a nonempty body. This rejects an all-404 server, a missing build and a fabricated static source. Fetching the script does not execute browser JavaScript.
3. Bare `/_next/image` must return 404. Given the inspected production handler, enabled optimization would instead validate missing parameters and return 400. This discriminates route removal from an unavailable source image.
4. A second request points the optimizer at the same proven-existing local script, with valid width/quality syntax, and requires 404. It uses ordinary JS bytes, not an image exploit. Together with the guard ordering, this checks refusal before source decoding rather than relying on an absent source. It does not measure decoder invocation dynamically or test image-codec safety.
5. Requests use fifteen-second abort signals and reject redirects. The script closes connections/server and Next in finally. It requests no harness/account/model endpoint, invokes no Electron/profile API, and makes no remote target request. The inspected root route/layout uses ordinary server rendering of the client shell; a fetch does not run its browser effects.

The probe is suitable for the stated one-off production endpoint proof after a build. It does not itself assert a Git SHA or exact Next version; its caller must supply the intended newly built root and associate the printed root/version and results with that build record. It does not run Electron's additional response-policy wrapper, inspect ASAR contents, establish installed-app preservation or qualify signing. Those are explicit scope limits, not defects in this targeted test. Only parent-reported node--check has occurred so far; no HTTP PASS is claimed here.

## Evidence and handoff

The first signed installer remains the old 9eaddb596 build with old dependency bytes. OWNER_TRIAL_NOTES, PLAN and the later RUN_LOG explicitly preserve it and hold it from public distribution pending replacement. Earlier packaging statements of no blocker are historical stage returns and are qualified by the later advisory finding; they are not evidence that this source patch changed the signed artifact. Signing, Gatekeeper's unnotarized result, install-over checks and publishing authorization remain distinct. No source or evidence file claims the replacement artifact already exists.

APP-HOLD reliance passed ALLOW/CLEAR/NOT_HELD for DEL-09-06 at candidate 61ca362a2, entry `APP_V3_USER_JOURNEYS_20260912:INDEPENDENT_DEPENDENCY_REVIEW`. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan SHA-256 `f263ac89e254905997bf772227341171faa60236301a0673b433f45e2395acc5`.

No unresolved actionable review finding remains. Parent owns remaining CI, executing the reviewed probe against the replacement production build, verifying packaged dependency/config identity, and the qualified owner handoff. Subsequent source or probe changes require affected-scope review. This is derivative review evidence over the frozen candidate and precise cited advisories, not an authority-pointer update or release approval.

## Exact coverage

- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_20260913.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/OWNER_TRIAL_NOTES.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PLAN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/RUN_LOG.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/DEPENDENCY_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/DEPENDENCY_WARNING_TRIAGE.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/PACKAGING_RETURN.md`
- `projects/chirality-app-dev/frontend/next.config.mjs`
- `projects/chirality-app-dev/frontend/package-lock.json`
- `projects/chirality-app-dev/frontend/package.json`

Additional authorized review target: the production HTTP probe at the absolute path and hash above. Connecting source included Electron production server construction, Next 15.5.25 image routing, App root page/layout/client route and installed dependency manifests.
