# Successor core freeze for independent backcheck

Source geometry and pressure cancellation defects are repaired in the exact profile. One source OD/effective-wall annulus now supplies stiffness/recovery properties and named pressure surfaces. The pure area helper is shared unchanged with M35; legacy geometry and the original radii scalar arithmetic remain unchanged. The separately authorized M34 float_roundtrip feature fixes the measured large-value source parsing error, with both locks unchanged.

Pressure assembly groups source coefficients before multiplying their common pressure/geometry/direction factor. This retains small terminal and interior near-incompressible loads, while cap/eigen ledgers remain distinct and observational. Source recovery similarly forms effective force before publication rather than subtracting rounded wall/P rows. Different strongly cancelling source factors remain explicitly unqualified under the documented screening domain; no material-range cutoff or numerical passing receipt is invented.

Actual candidate checks:

- **34/34 public tests pass**, including the frozen pressure14 and source geometry/near9, X1/torque2, coverage/ties4, signed reactions/springs4 and explicit unshared-cancellation guard1.
- **156/206 product library tests pass; the same50 legacy-pressure fixture failures remain.** All new helper/grouping controls pass. Existing assertions/oracles were not weakened or moved to historical execution.
- Canonical JSON: **8 unit +2 integration tests pass** after the narrow parser-feature handoff.
- Stress crate: **48/48 pass** on unchanged stress source.
- The exact-sum helper received independent **7707 Fraction/bit checks**; its source hash remains unchanged from that review. The shared area helper passed5 controls here and M35 independently confirmed7 actual mass/parity cases using identical bytes.

SOURCE_MANIFEST.json binds19 files and candidate-content digest; source.patch is the complete diff from basef702, and source-geometry-pressure.delta.patch is the explicit successor delta from FREEZE_02. Original geometry, parser, near-load, coverage and tie failures remain preserved. CHECKS_AND_REFERENCES.json binds actual logs and independent reference packets. INTERFACE_SCHEMA.md describes the final proposed source fields and limits.

This source is held for the same independent whole-core reviewer. It is not merge-ready: the50 individually proposed regression dispositions, NUM/physics-1 consumer union, registered checks/CI and actual native/save/reopen/export witnesses remain open. No commit, acceptance or release is claimed.
