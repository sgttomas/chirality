# REVIEW_NODE_G_R1 — DEL-09-06-V3-05 egress-probe destination restriction (independent read-only review, round 1)

- **Reviewer:** Claude Fable 5.1 (`claude-fable-5-1`), fresh read-only ephemeral Agent 2 (TASK + `software-code-review` pattern) under a sealed brief from HELP_HUMAN. No tracked file was edited anywhere; nothing committed or pushed; the review ran in its own detached scratch worktree (`<scratchpad>/wt-reviewG1`), removed and pruned at the end.
- **Basis:** `e59efa4830fb54143c86e511ec35a6d1a476f72e` (origin/main at PR #686 merge)
- **Frozen head:** `39adfa6a6c5972d489dbe3b4cc6d60f0ade172d8` — exactly one commit; `git rev-parse 39adfa6a6^` = `e59efa4830fb54143c86e511ec35a6d1a476f72e`
- **Diff reviewed:** 100% of `git diff e59efa483..39adfa6a6` — 20 files, +2,149 / −39. Every changed file was read in full (not hunks only). `frontend/electron/main.ts` (unchanged) was additionally read around `evaluateRendererEgressPolicy`, `registerRendererEgressPolicy`, and the probe wiring at `main.ts:549-550`, because the change's safety argument rests on it.

## Files reviewed (20)

Product paths relative to `projects/chirality-app-dev/`; record paths relative to the repo root.

| # | File | Status |
|---|---|---|
| 1 | `frontend/electron/renderer-window-policy.ts` | M |
| 2 | `frontend/scripts/run-packaged-security-proof.mjs` | M |
| 3 | `frontend/src/__tests__/contract-pins.manifest.ts` | M |
| 4 | `frontend/src/__tests__/electron/renderer-window-policy.test.ts` | M |
| 5 | `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts` | M |
| 6 | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/EVIDENCE.md` | A |
| 7 | `…/Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/packaged-security-proof/MANIFEST.sha256` | A |
| 8 | `…/packaged-security-proof/cleanup.json` | A |
| 9 | `…/packaged-security-proof/packaged-daemon.log` | A |
| 10 | `…/packaged-security-proof/packaged-gui.log` | A |
| 11 | `…/packaged-security-proof/summary.json` | A |
| 12 | `…/packaged-security-proof/tcp-snapshots.json` | A |
| 13 | `…/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/TASK_RUN_2026-09-03_NODE_G.md` | A |
| 14 | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_G_2026-09-03/CHECKS.json` | A |
| 15 | `…/APPDEV_V3_NODE_G_2026-09-03/COORDINATOR_DECISIONS.md` | A |
| 16 | `…/APPDEV_V3_NODE_G_2026-09-03/ORCHESTRATION_PLAN.md` | A |
| 17 | `…/APPDEV_V3_NODE_G_2026-09-03/RETURN.md` | A |
| 18 | `…/APPDEV_V3_NODE_G_2026-09-03/STEP0_DISCOVERY.md` | A |
| 19 | `…/APPDEV_V3_NODE_G_2026-09-03/WORK_GRAPH.json` | A |
| 20 | `…/APPDEV_V3_NODE_G_2026-09-03/instances/G1_IMPLEMENTER/LAUNCH_BRIEF.md` | A |

Confirmed NOT in the diff (`git diff --name-status` and targeted `git diff --stat … -- <path>` both empty): `frontend/electron/main.ts`, DEL-09-06 `_STATUS.md`, `loop/LOOP_RECEIPTS.md`, `package.json` / lockfiles, `runtime/**`, `.github/**`, `docs/**`.

## Commands run (cwd = review worktree root unless stated; exit codes as observed)

| # | Command | cwd | Exit / result |
|---|---|---|---|
| 1 | `git -C /Users/ryan/dev/chirality worktree add --detach <scratchpad>/wt-reviewG1 39adfa6a6c…` | — | 0 |
| 2 | `git diff --stat e59efa483..39adfa6a6` / `--name-status` / `git log --oneline e59efa483..39adfa6a6` | wt | 0 — 20 files, one commit |
| 3 | `git diff --check e59efa483..39adfa6a6` | wt | **0** (no whitespace errors) |
| 4 | `git rev-parse 39adfa6a6^` | wt | `e59efa483…` (parent = basis) |
| 5 | `git diff --stat e59efa483..39adfa6a6 -- projects/chirality-app-dev/frontend/electron/main.ts` and `-- …/DEL-09-06_…/_STATUS.md` | wt | empty (both unchanged) |
| 6 | `python3 tools/software_workflow/validate_change_scope.py . --base e59efa483 --head 39adfa6a6 --allowed <root>` ×5 (one `--allowed` per root; the brief's `frontend/…` roots prefixed with `projects/chirality-app-dev/` because that is where the frontend lives) | wt | **0 — `status: PASS`, `violations: []`, 20 paths**. (Two earlier attempts passing the roots as one space-separated list exited 2 with an argparse usage error — the validator accepts one path per `--allowed`; recorded for reproducibility.) |
| 7 | `shasum -a 256 -c MANIFEST.sha256` | manifest dir | **0 — 5/5 OK** |
| 8 | `shasum -a 256 -c <path>/MANIFEST.sha256` | repo root | 1 — 5 × "FAILED open or read" (manifest lists bare filenames; see G1-F3) |
| 9 | python: re-append the one trailing space to line 1 of the retained `packaged-gui.log` and hash | wt | 3,710 B, `f5a71eee…ecaf13` — reproduces the raw hash recorded in EVIDENCE.md §4 / CHECKS.json exactly; retained file is 3,709 B = `ba9d2379…0288` |
| 10 | `grep -rniE 'notariz|codesign|signed|release[- ]ready|publish' <20 changed files>` | wt | 0 — 14 hits, every one a disclaimer / exclusion / process word (see G1-F8) |
| 11 | `grep -rn CHIRALITY_EGRESS_LAYER_PROBE_URL` over `*.ts,*.tsx,*.mjs,*.js,*.json,*.md,*.sh,*.py,*.yml,*.yaml` (excl. node_modules/dist) | wt | only: proof-script env block (decoy), pins (`notContains` ×2, decoy `contains`), tests (set-and-ignored), run records / evidence / historical node-A records. No `.yml`, no `docs/**`, no `runtime/**`. |
| 12 | `grep -n … electron/main.ts` for `runEgressLayerProbe`, the port rule, `CHIRALITY_NETWORK_POLICY_PROBE_URLS` | frontend | wiring at `main.ts:550` `runEgressLayerProbe(window, { env: process.env });`; port rule at `main.ts:255-260` |
| 13 | `grep -cF <each pinned string>` against the real pinned files | frontend | every `contains` pin ≥1, every `notContains` pin 0 (table in G1 verified-claims below) |
| 14 | `npm ci --ignore-scripts --no-audit --no-fund` | wt/runtime | 0 — 61 packages |
| 15 | `npm run build` (`tsc -b`) | wt/runtime | 0 — `packages/client/dist/src/index.js` present |
| 16 | `npm ci --ignore-scripts --no-audit --no-fund` | wt/…/frontend | 0 — 753 packages; no lockfile change (`git status --porcelain` empty) |
| 17 | `npm run typecheck` | wt/…/frontend | **0** |
| 18 | `npx vitest run src/__tests__/electron/renderer-window-policy.test.ts src/__tests__/scripts/run-packaged-security-proof.test.ts src/__tests__/contract-pins.test.ts` (+ `--reporter=json`) | wt/…/frontend | **0 — 3 files, 91/91 passed: renderer-window-policy 65, contract-pins 16, run-packaged-security-proof 10** (matches EVIDENCE.md §3 and CHECKS.json `frontend-test-focused`) |
| 19 | `node --input-type=module -e …` calling the real `summarizeNetworkEvidence` with (a) no `[egress-layer-probe]` line, (b) a malformed one, (c) the expected one | wt/…/frontend | (a) `egressProbePayloadCount 0, egressProbeObserved false, pass false`; (b) `egressProbeObserved false, egressProbeUnexpectedDestinations [null], pass false`; (c) `egressProbeObserved true, unexpected [], pass true` |
| 20 | python scan of `tcp-snapshots.json` (endpoint classes/hosts, distinct process command lines) and grep for secret-shaped strings across the bundle | wt | classes `{loopback}`, hosts `{127.0.0.1}`; 7 distinct command lines (Electron helper/renderer/gpu/network-service + GUI + daemon); no `sk-ant`, `Bearer`, `api_key=`, `token=`, `password` |
| 21 | `git -C /Users/ryan/dev/chirality worktree remove --force <scratchpad>/wt-reviewG1 && git -C /Users/ryan/dev/chirality worktree prune` | — | see final line of this report |

**Deliberately not run** (per brief): `npm run desktop:pack`, `npm run proof:packaged-security`, full `npm test`, premerge. The packaged claims are judged from the retained bundle + manifest verification only.

## Verified claims (implementer statements checked against the bytes)

| Claim | Where | Result |
|---|---|---|
| Probe requests only the constant | `renderer-window-policy.ts:455-456` `export const EGRESS_LAYER_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked';`; `:488` `new URL(EGRESS_LAYER_PROBE_URL)`; `:491-496` `.fetch(EGRESS_LAYER_PROBE_URL, { method: 'GET', cache: 'no-store', signal: AbortSignal.timeout(3000) })` | **Confirmed.** The function body references no other URL value; `options.env` is read only at `:485` (`CHIRALITY_RENDERER_SECURITY_PROBE !== '1'`) and inside `probeDelayMs` (`:338-341`, `_DELAY_MS`). Signature `(window, { env })` — no URL parameter (`:470-484`). |
| Module never reads `process.env` | whole file | **Confirmed** — `grep -c process.env` = 0; env is injected by `main.ts:550`. No `process.argv`, IPC, or config read anywhere in the module. |
| No remaining redirect path (env/argv/config/IPC) | repo grep (cmd 11), `main.ts:222` (`CHIRALITY_NETWORK_POLICY_PROBE_URLS` is the separate, pre-existing in-page probe list — unrelated to `runEgressLayerProbe` and out of scope) | **Confirmed.** The retired name survives only as a negative-control assignment in the proof script and as `notContains` pins. |
| Destination is denied by the real policy | `main.ts:245-260`: Anthropic host → `https:` required, then `if (parsed.port !== '' && parsed.port !== '443')` → `anthropic_port_not_allowlisted:${parsed.port}`; the fetch goes through `session.webRequest.onBeforeRequest` (`main.ts:277-297`) | **Confirmed** by code and by the retained `packaged-gui.log:15-24` (`reason: 'anthropic_port_not_allowlisted:8443'` … `[egress-layer-probe] … "port":"8443","outcome":"rejected","error":"net::ERR_BLOCKED_BY_CLIENT"`). |
| Window-open / `shell.openExternal` http(s)-only path, navigation containment, CSP header helper unchanged | `renderer-window-policy.ts:1-334` | **Confirmed unchanged** — the diff touches only lines 444-515 (constant, doc comment, `runEgressLayerProbe` body). `evaluateWindowOpen`, `installRendererWindowPolicy`, `applyContentSecurityPolicyHeader`, `buildRendererContentSecurityPolicy`, `summarizeDestination` are byte-identical to basis. |
| Payload shape `{protocol, hostname, port}`, no path | `:489`, `:500`, `:506-511`; unit test `:604-628` asserts the literal JSON and `not.toContain('chirality-packaged-security-egress-blocked')` | **Confirmed.** |
| Proof summarizer matches protocol+hostname+port and fails on any unexpected destination | `run-packaged-security-proof.mjs:369-383`, `:396`, `:405` (`egressProbeUnexpectedDestinations.length === 0` inside `pass`) | **Confirmed.** Also confirmed non-vacuous: zero egress payloads → `egressProbeObserved false` → `pass false` (cmd 19a); malformed line → `[null]` unexpected → `pass false` (cmd 19b); `egressDiagnostics > 0` (`:361`, `:401`) still required independently. |
| Decoy negative control actually exercises the retired path | `:67` `EGRESS_PROBE_DECOY_URL = 'http://127.0.0.1:9/…'`; `:619` `CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_DECOY_URL` | **Confirmed effective.** If the basis-era code (`const url = options.env.CHIRALITY_EGRESS_LAYER_PROBE_URL?.trim()` + `summarizeDestination(url)`) were reinstated, the app would fetch the loopback decoy (policy allows loopback → real connect to 127.0.0.1:9 → refused) and log `{protocol:'http:', hostname:'127.0.0.1'}` (no port) → not the expected destination → listed in `egressProbeUnexpectedDestinations` → `pass false`; additionally `egressLayerDiagnostics` would be 0 and `egressProbeObserved` false. Nothing leaves the host. Both regression shapes (decoy logged with port, and port-less) are covered by the unit test (`run-packaged-security-proof.test.ts:120-134`). |
| Whole-directive CSP compare untouched | `summarizeRendererSecurityEvidence` `:415-458` | **Confirmed** unchanged. |
| `main.ts` untouched | cmd 5 | **Confirmed.** |
| Contract pins assert the claims | cmd 13: policy file — `export const EGRESS_LAYER_PROBE_URL =` 1, literal 1, `.fetch(EGRESS_LAYER_PROBE_URL, {` 1, `process.env` 0, `CHIRALITY_EGRESS_LAYER_PROBE_URL` 0; `main.ts` — port rule 1, reason template 1, wiring line 1, retired name 0; proof script — both `export const` lines 1, decoy env line 1, `egressProbeUnexpectedDestinations.length === 0` 1 | **Confirmed.** No pin loosened: the removed `contains "'https://api.anthropic.com:8443/…'"` on the script is subsumed by the stricter `contains "export const EGRESS_PROBE_URL = '…'"`; the two removed env-var pins are replaced by `notContains` (policy, `main.ts`) and by the decoy line (script), and the byte-equality of the two literals is asserted by `run-packaged-security-proof.test.ts:66`. |
| Tests exercise real module behaviour | `renderer-window-policy.test.ts:499-664`, `run-packaged-security-proof.test.ts:63-140` | **Confirmed.** Both import the real modules; the only fake is a minimal `session.fetch` spy (the injection point). Coverage: env var set but ignored (`:562-591`, six allowlisted/foreign URLs incl. Anthropic :443 and default port, loopback 127.0.0.1/localhost/[::1], example.com); gate-only firing (`:550-561`, incl. `'0'`, `'true'`, and the retired var set without the gate); arity (`:594-597`); payload shape rejected/response (`:599-664`); summarizer negatives for port 443, port-less, decoy destination, extra destination beside the expected one (`:114-139`). Gap noted in G1-F1. |
| Evidence internal consistency | EVIDENCE.md §3-4, CHECKS.json `proof-packaged-security`, `summary.json`, logs | **Consistent.** 7 snapshots / `nonAllowlistedOutboundTcp: []` / `blockedRendererDiagnostics 1` = `egressLayerDiagnostics 1` / `egressProbePayloadCount 1` / `egressProbeObserved true` / `egressProbeUnexpectedDestinations []` / cleanup pass, all present in `summary.json:158-253` and matching the prose; the raw→retained gui-log hash normalisation reproduces exactly (cmd 9); focused test counts 65/16/10 reproduce (cmd 18); `sourceRevision e59efa483` (pre-commit working tree) is declared in EVIDENCE.md §4 and RETURN.md §5.5. |
| A1 re-stage declaration present | `STEP0_DISCOVERY.md` §3 (verbatim quote of the A1 record + explicit declaration); echoed in `TASK_RUN_…_NODE_G.md` "A1 re-stage declaration", EVIDENCE.md §5, WORK_GRAPH `human_gates`, ORCHESTRATION_PLAN "Human decision points" | **Confirmed.** |
| `_STATUS.md` unchanged at freeze | cmd 5 | **Confirmed.** |
| Fences F-APP-1..5 | RETURN.md §6, ORCHESTRATION_PLAN constraints, cmd 10 | **No violation found.** No destination added to REQ-NET-001 (the only requestable destination is the already-denied `:8443` form; the decoy is loopback and lives only in the proof's own env). No signing/notarization/publication/readiness claim anywhere in the diff (G1-F8). No lifecycle, domain-engine, or new standing surface. |

## Findings

| ID | Severity | File:line | Claim / observation | Evidence | Required fix / suggestion |
|---|---|---|---|---|---|
| G1-F1 | MINOR | `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts:79-140` | The summarizer test has no case where the `[egress-layer-probe]` line is entirely absent (probe never fired) nor where it is malformed. The brief asks that "missing probe diagnostics" be covered; only the missing `anthropic_port_not_allowlisted:8443` diagnostic is covered (`cspOnly`, `:104-108`). | Code inspection (`.mjs:373-378` `.some()` over an empty array is `false`; `:381-383` a `{parseError:true}` payload maps to `null` in `egressProbeUnexpectedDestinations`) and my direct call (cmd 19) show the summarizer already fails closed in both cases — this is a test-coverage gap, not a behaviour defect. | Suggestion (non-blocking, may be folded into a later tranche): add two lines to the existing test — `logText` with the `[egress-layer-probe]` line removed → `egressProbePayloadCount 0`, `egressProbeObserved false`, `pass false`; and `[egress-layer-probe] not-json` → `egressProbeUnexpectedDestinations` `[null]`, `pass false`. |
| G1-F2 | NOTE | `…/Node_G_Egress_Probe_Restriction_2026-09-03/EVIDENCE.md:154-157`; `RETURN.md:71` | The declaration says "the retained `packaged-gui.log` carries the scratch-worktree `appPath` and the launcher opt-out path". In fact the scratch path also appears in `summary.json` (`artifactIdentity.appPath`, 1×), `packaged-daemon.log` (2×), and `tcp-snapshots.json` (46×, in the Electron helper command lines together with `--user-data-dir=/tmp/chirality-psp-Nd6HxN/user-data`). | cmd 20 / grep counts: summary.json 1, packaged-daemon.log 2, packaged-gui.log 1, tcp-snapshots.json 46, cleanup.json 0. No secret, no home-directory content beyond `/Users/ryan/.local/bin/chirality` (declared); same class as the node-A bundles already on `main` (node-A review NOTE-7). | Optional: at closeout, widen the sentence to "the retained bundle (`summary.json`, both logs, `tcp-snapshots.json`) carries the scratch-worktree path". Evidence-text only; no product or bundle change needed. |
| G1-F3 | NOTE | `…/packaged-security-proof/MANIFEST.sha256:1-5` | Manifest entries are bare filenames, so `shasum -a 256 -c` verifies only when run from the manifest's own directory (EVIDENCE.md §4 says exactly that: "verify with `shasum -a 256 -c MANIFEST.sha256` in the directory"). From the repo root, as the review brief phrased it, the command reports 5 × "FAILED open or read". | cmd 7 (dir: 5/5 OK, exit 0) vs cmd 8 (root: exit 1). Bytes verify; only the invocation location differs. | None required. If the loop wants repo-root verifiability as a convention, future manifests could list paths relative to the repo root — a convention question for the owner, not a defect of this tranche. |
| G1-F4 | NOTE | `…/APPDEV_V3_NODE_G_2026-09-03/CHECKS.json:193,212` | The recorded `validate_change_scope.py` fence includes a sixth root, `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`, which is not in the frozen diff (reserved for closeout). | cmd 6 with the brief's five roots: PASS, 0 violations, 20 paths — the extra root is harmless and does not admit anything present in the diff. | None. |
| G1-F5 | NOTE | `frontend/src/__tests__/contract-pins.manifest.ts:271` | `{ kind: 'notContains', value: 'process.env' }` on `electron/renderer-window-policy.ts` is a whole-file textual pin: a future doc comment that merely mentions `process.env` in that module would trip it. | `contract-pins.test.ts:41-42` is plain `raw.includes`. | Acceptable as intended (it is exactly the property being asserted); noting so the next editor of that file is not surprised. |
| G1-F6 | NOTE | `frontend/scripts/run-packaged-security-proof.mjs:381-383` | A malformed `[egress-layer-probe]` line (JSON parse error) is surfaced as `null` in `egressProbeUnexpectedDestinations` and fails the proof. This is fail-closed and correct; it just means a `null` entry in a future `summary.json` should be read as "unparseable payload", not "no destination". | cmd 19b. | None. |
| G1-F7 | NOTE | `summary.json:9-10`, EVIDENCE.md §4, RETURN.md §5.5 | The retained packaged proof was executed against a bundle built from the pre-commit working tree (`sourceRevision: e59efa483…`); the proved bytes are identified by the three file hashes and `identitySha256 e716439f…`, not by the frozen commit. Declared; the `artifact-proof` CI label is named as the binding to the merged SHA. Not re-executed by this review (per brief). | As cited. | None for this round; the owner may want the `artifact-proof` run on the PR as usual. |
| G1-F8 | NOTE | cmd 10 hits | F-APP-2 check: every hit is a disclaimer or exclusion — EVIDENCE.md:12 ("makes no release-readiness, signing, notarization … claim"), :128 "Unsigned bundles are not byte-deterministic", `summary.json:6` `proofBoundary: 'fresh-unsigned-…'`, `:257` `signingOrNotarization: false` (pre-existing script output, `.mjs:754,764`), CHECKS.json:131 "unsigned bundles", STEP0 :40 (quoted A1 text), RETURN :70,:77 (disclaimers), pins :121 ("unsigned desktop packaging"), ORCHESTRATION_PLAN :8 "Required verdict to publish" and LAUNCH_BRIEF :19 (`gh pr create` at closeout) — "publish" there means pushing the branch/PR after `REVIEW_PASS`, not a release act. | — | None. No F-APP-2 violation. |

No BLOCKER or MAJOR findings.

## Verdict

**PASS** — zero BLOCKER / MAJOR findings. One MINOR (G1-F1, a test-coverage suggestion where the code already fails closed) and seven NOTEs, none of which require a re-freeze before `REVIEW_PASS`. G1-F1 and G1-F2 may be taken at the implementer's or owner's discretion (in this tranche's closeout or later) without affecting this verdict.

Review worktree: removed with `git worktree remove --force` and `git worktree prune` after this report was written (see final command result in the reviewer's return message).
