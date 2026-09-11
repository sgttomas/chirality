# Host addition: interim independent integration review

PASS for the two packaging-script changes and three associated test changes against HEAD `77a6fd233`; qualification and signing review remain pending. TASK / Type 2, gpt-6-astra medium; independent of author, no delegation. Read-only source review; no test duplication, supplier execution, build, download or live-state access.

The producer requires an executable regular sibling host before supplier staging and rejects missing, directory, non-executable and symlink inputs. Full-tree staging preserves the sibling; the v2 manifest producer separately refuses a missing host. Tests exercise these failures and successful copied content without changing historical Runtime reader requirements. No actionable defect found in these five files. The adjacent RUN_LOG update is not product code.

Existing private staging in `hosted-private-composition.ts:174–240` consumes every admitted closure entry, creates contained private copies with executable modes, verifies the resulting full closure and revalidates the packaged source. It is not a codex-only copy when the operational exact-supply verifier is supplied. Thus the newly measured host must be included in the new signed supplier closure; no generic staging rewrite is indicated.

The descendant tracker follows parent relationships independently of process group and reconciles surviving separate-group descendants as detached. Supervisor retirement rejects remaining detached/owned processes and census/identity failures. This preserves the existing failure boundary; it does not prove that the real host exits on cancellation or supplier retirement. Actual paired cleanup evidence already required by the approved proposal remains necessary, including the host's separate process group. No relaxation or speculative orphan-killing repair is recommended from source inspection alone.

This interim return does not qualify the official payload, final host entitlements, enforced native execution, or the next package. Review those measured outputs and final signing/procedure changes when frozen. Parent-reported 43 passing tests were not rerun.

## Signer backcheck

PASS for the additional signer, host entitlement plist and focused test diff. `createRuntimeV2SignOptions` selects the new plist only for the exact `Contents/Resources/supplier/codex-code-mode-host` path within the current App; codex, another directory, another App and suffix lookalikes retain their prior policy. The plist grants only `com.apple.security.cs.allow-jit`. Hardened runtime, outer-only resealing and all other signing behavior remain intact. The test exercises the real options factory and reads the actual selected plist rather than reimplementing its selection logic.

The lead reports the real host traps under empty hardened entitlements and passes its host probe with allow-jit alone. This supports the bounded policy change; paired signed qualification is still pending and was not inferred from the unit test. The new plist must be included by exact hash among the next procedure's static packaging inputs alongside the changed signer; that future binding has not yet been presented or verified in this backcheck. No source defect identified.
