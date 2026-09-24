# Same-ID Open RAF diagnosis

**Confirmed cause: a stale hover callback erases a freshly captured label-position hint.** After the second same-ID Open retires captured Box, node00011's ordinary plate lies beneath the stationary held pointer. Its enter handler captures the correct center, but an older label updater still closes over hover=null and clears that new hint solely for key mismatch. The committed hover layout then moves the plate away, generating leave; ordinary placement returns it under the pointer, generating enter again. Repeated presentation invalidation prevents the owned RAF count from settling.

This finding is established by the original and exact-repeat failures, actual pointer boundaries in journal07, and capture/validation/result ordering in journal08. No repair has been implemented or accepted by this reviewer. The earlier FOUNDATION_STARTUP_DIAGNOSIS files remain byte-identical and historical.

## Failure and earliest divergence

At `8589065f6d86389babd7bc18a3bfc6c42643f3be`, `source-foundation-compact-lazy-04` passes 28 cases, including 10k startup, then fails the same-ID Open case at `ui-foundation.spec.ts:2178`, through the unchanged 10-second settle predicate at `:2101` (expected pending RAF 0, received 1). Eight cases do not run. The manager's unchanged exact compact reproduction `source-foundation-open-repro-05` fails identically. The extra reproduction attachment is browser identity, HeadlessChrome 148.0.7778.96.

The first ordinary Open commits generation 2 and settles at camera sequence 13/frame 12/RAF 0 with project selection. After selecting node00010 and beginning a genuine captured Box, state settles again at frame 14. The second keyboard Open advances generation to 3 and selects Project. The captured rectangle disappears; the witness records CANVAS lostpointercapture with buttons=1. Delayed pointer movement/up and their final assertions have not run when the later settle fails.

All 14 post-Open reads in each trace report RAF 1. Main submissions advance 19→520 in the original and 19→527 in the exact reproduction, while the complete camera stays identical at sequence 15 and canvas stays 531×559 at origin `(705,217)`. Context/total labels alternate 0/22 and 1/23. Created/disposed measurement observers advance 13/11→513/511 and 13/11→521/519 respectively; live observers remain 2 and live event bindings 8. The pointer/key witness stays at 22 events, with no additional pointermove. This is continuing presentation-effect turnover, not one dormant handle, camera damping, accumulation of live observers or uncommitted model replacement.

## Direct boundary and hint evidence

Journal07's diagnostic copy preserves and rethrows the original assertion. Its bounded 160-entry journal contains 25 entries from capture loss onward. At 2960.4 ms, loss leaves the stationary point `(803.2349853515625,605.5050048828125)`, buttons=1, over node00011. Canvas out/leave and node00011 over/enter follow at 2960.5–2960.7 with context count 0 and actual plate rectangle `(797.171875,580.625,58,32)`. Node00011 out/leave and canvas over/enter occur at 3213.6–3213.9 after the plate moves to `(1049.171875,432.625,58,32)` with context count 1. The sequence repeats at 3233.8–3253.5 with identical pointer coordinates and camera. The measured height is 32px; the initial trace analysis's 26px was only the base CSS declaration.

Journal08 retains the same failing assertion and records three optional, bounded observation points. Its first decisive sequence is:

- **3070.5 ms — capture:** node00011 has an applied ordinary rectangle `(92.1813155,363.6309036)–(150.1813155,395.6309036)` in canvas coordinates. The handler writes preferred center `(121.1813155,379.6309036)`, generation `3:3`, camera 15, canvas 531×559.
- **3085.6 ms — validation:** the older updater has `closureHover: null`; `invalid.key` is true. Hide, generation, camera, width, height and radii mismatch booleans are all false. The existing conditional clears the hint.
- **3312.7 ms — committed hover placement:** the updater now has hover=node00011 and hint=null. The hover plate is placed at `(344.1813155,215.6309036)–(402.1813155,247.6309036)`, away from the stationary pointer.

The pattern repeats. All **33 captured-hint validations** in the 200-entry journal report only that stale key mismatch, with hover=null. This rules out absent capture or changed geometry/basis as the recorded reason for discarding these hints. Boundary journal07 supplies the resulting enter/leave cycle; the unchanged original/reproduction runs show the failure existed before diagnostic source logging. Logging perturbs timing, so these are causal observations for this witness, not timing qualification.

## Responsible source and narrow repair

`PipeViewport.tsx:2440–2450` captures the current applied center before requesting a React hover-state update. Its installed updater at `:1386–1392` instead validates that shared mutable hint against the render callback's captured hoveredEntityKey. A previously scheduled callback can therefore invalidate newer interaction state. The hover-dependent layout effect recreates its measurement observer and invalidates the resource on every turnover (`:1349–1471`); resource hover presentation and observer callbacks schedule more work. The source and raw observations support this chain.

Use one synchronous current-hover identity ref/publication path for **every actual hover transition**, including plate enter/leave, canvas picking/departure, gesture/visibility clearing and generation replacement. Hint key validation must compare against this current identity, while label-policy input remains the committed React hover state. Preserve every existing Hide, generation, camera, size and radii guard. Clear retired or mismatched hints when live hover changes, while preserving a fresh matching hint captured for the incoming key. Do not merely mirror possibly stale React state into the ref during render, remove all mismatch guards, disable hover, or force RAF counters to zero.

A deterministic regression should enact the measured order: capture the ordinary node plate, run the previously installed hover-null updater before React's new hover commit, then commit hover. The hint must survive the old callback and retain the valid plate rectangle. Separately verify actual departure, replacement generation, Hide and changed projection invalidate it. Then rerun the unchanged exact compact same-ID Open case with genuine held capture and the existing RAF-zero assertion, plus the full compact connected lane. These checks must cover the actual repaired candidate; no repair pass is asserted here.

The lazy-disclosure delta only adds generation-bound open state, closes it on unavailable projection and conditionally mounts disclosure contents. The failing snapshots keep it closed with applied projection and no projection error. It introduces no direct hover/RAF scheduling call. The identified defect is the pre-existing C4 hover-hint lifetime race; reverting lazy contents or relaxing the timeout would not repair that measured cause.

## Evidence boundaries and provenance

The instrumentation diff consists only of a bounded optional journal helper and logs at capture, pre-invalidation and placement. Original/instrumented PipeViewport hashes match `_run_records/hint-diagnostic-source-binding.json`; the archived diagnostic spec matches its run command hash. After diagnostic08, this reviewer verified current PipeViewport equals exact candidate 8589065f6, SHA-256 `6f8df9f0824eba9ef82e783808279079fbbe427e6193b2478ccd9df5bf66ac50`, and the temporary spec is absent. Original cases, all failed attempts, journal07 and journal08 remain distinct records.

Reviewer `/root/c4_manager/basis_integration_review` is the resumed TASK Type 2 child under `/root/c4_manager`, with no descendants. Full TASK/diagnosis instructions and retained unchanged Root/project/loop instructions govern this read-only assignment. All commands used `{REPO_ROOT}`. Only this diagnosis and its adjacent JSON were written; no tests/browser/build/resources/network/Git/source mutation was performed. The manager owns all runtime and repair execution. [RAF_REPLACEMENT_DIAGNOSIS.json](RAF_REPLACEMENT_DIAGNOSIS.json) binds source/evidence origins and hashes, decoded polling, boundary samples and decisive hint records.


## Portable evidence view

This is a portable derivative of the [exact original bytes](_run_records/portability-originals/RAF_REPLACEMENT_DIAGNOSIS.md), SHA-256 `41faf4e54e1e578da114c45adad501296f95fb4c2987789262a170ce32b53dff`. `{REPO_ROOT}` denotes the Git root of the isolated checkout used for the observation. Existing source/hash assertions describe the historical checked bytes; PORTABILITY_DISPOSITION.json at the connected-stage root maps transformed records back to their originals. No observation, result, limit or original hash was changed.
