# Host addition: interim independent integration review

PASS for the two packaging-script changes and three associated test changes against HEAD `77a6fd233`; qualification and signing review remain pending. TASK / Type 2, gpt-6-astra medium; independent of author, no delegation. Read-only source review; no test duplication, supplier execution, build, download or live-state access.

The producer requires an executable regular sibling host before supplier staging and rejects missing, directory, non-executable and symlink inputs. Full-tree staging preserves the sibling; the v2 manifest producer separately refuses a missing host. Tests exercise these failures and successful copied content without changing historical Runtime reader requirements. No actionable defect found in these five files. The adjacent RUN_LOG update is not product code.

Existing private staging in `hosted-private-composition.ts:174–240` consumes every admitted closure entry, creates contained private copies with executable modes, verifies the resulting full closure and revalidates the packaged source. It is not a codex-only copy when the operational exact-supply verifier is supplied. Thus the newly measured host must be included in the new signed supplier closure; no generic staging rewrite is indicated.

The descendant tracker follows parent relationships independently of process group and reconciles surviving separate-group descendants as detached. Supervisor retirement rejects remaining detached/owned processes and census/identity failures. This preserves the existing failure boundary; it does not prove that the real host exits on cancellation or supplier retirement. Actual paired cleanup evidence already required by the approved proposal remains necessary, including the host's separate process group. No relaxation or speculative orphan-killing repair is recommended from source inspection alone.

This interim return does not qualify the official payload, final host entitlements, enforced native execution, or the next package. Review those measured outputs and final signing/procedure changes when frozen. Parent-reported 43 passing tests were not rerun.

## Signer backcheck

PASS for the additional signer, host entitlement plist and focused test diff. `createRuntimeV2SignOptions` selects the new plist only for the exact `Contents/Resources/supplier/codex-code-mode-host` path within the current App; codex, another directory, another App and suffix lookalikes retain their prior policy. The plist grants only `com.apple.security.cs.allow-jit`. Hardened runtime, outer-only resealing and all other signing behavior remain intact. The test exercises the real options factory and reads the actual selected plist rather than reimplementing its selection logic.

The lead reports the real host traps under empty hardened entitlements and passes its host probe with allow-jit alone. This supports the bounded policy change; paired signed qualification is still pending and was not inferred from the unit test. The new plist must be included by exact hash among the next procedure's static packaging inputs alongside the changed signer; that future binding has not yet been presented or verified in this backcheck. No source defect identified.

## Qualification backcheck

Reviewed the host and tightened pair probe scripts and selected evidence under `/private/tmp/chirality-supplier-code-mode-host-20260911-01`. Actual signed-host evidence passes value persistence, callback, second session, cell termination and clean exit. The tightened `final-signed-pair-reviewed.json` reports two completed turns, four fake-provider requests, two actual callbacks, and the same observed host in a separate process group on both turns. Final census is empty and supplier exit is code 0 with no signal. The script checks census command success and rejects termination-fallback exits. This is sufficient for the proposed account-free public-pair behavior check, not native authenticated private-admission qualification.

Final host signature evidence reports hardened runtime, valid strict signature and only allow-jit; its entitlement file hash is `85d97186afc33c073b2c524f88c5f8031601c844b3e10d9c71c82f845fcc3a6f`. Acquisition records retain the approved archive digest and unchanged build05 codex identity. No independent execution performed.

Minor required evidence wiring correction reported to lead: `QUALIFICATION_RETURN.json` still names the earlier `final-signed-pair-probe` rather than tightened `final-signed-pair-reviewed`; bind the latter in the final qualification return and Stage24. Existing successful tightened evidence can be reused without rerunning. The one-line test fixture `NODE_ENV: 'test'` correction is appropriate and does not change product behavior. Final packaging procedure/static-input binding remains pending.
