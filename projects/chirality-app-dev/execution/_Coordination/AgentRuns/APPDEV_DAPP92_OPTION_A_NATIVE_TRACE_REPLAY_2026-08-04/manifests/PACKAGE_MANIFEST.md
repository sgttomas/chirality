# Frozen package manifest contract — D-APP-92 Option A

Status: `EXPECTED STRUCTURE — ACTUAL HASHES PENDING AUTHORIZED BUILD`

- Electron version: exact package lock / built package must resolve `43.2.0`.
- GUI identifier: `com.chirality.app`.
- Helper identifier: `com.chirality.app.runtime-helper`.
- Helper `LSUIElement`: `true`.
- GUI `Contents/Library/LoginItems` contains exactly one top-level helper app.
- Builder-generated child identifiers remain `.helper`, `.helper.GPU`,
  `.helper.Plugin`, and `.helper.Renderer` under the helper identifier.
- Standalone and embedded helper trees must be byte/topology identical.
- Every helper symlink must be relative; no global Node dependency or TCP
  listener may be introduced.
- Exact helper executable, helper `app.asar`, helper `Info.plist`, GUI
  executable, GUI `app.asar`, packaged CLI, and instruction-root hashes must be
  recorded before launch.
- Generated packages are derivative evidence only and are removed at cleanup.

Stop before runtime if any identity, topology, dependency, hash, or
uninstrumented-source condition differs from this contract.

## Approval-stop derivative bindings

No actual package identity was accepted in this run. C178 constructed the
Electron 43.2.0 helper/GUI packages and passed its packaged-dependency check,
but the overall command failed when redundant `-- --publish never` arguments
forwarded positional `never` to the instruction-root verifier. C179-C184 were
not invoked, so actual package hashes, topology, instruction-root PASS, and
package-runtime fitness remain `UNKNOWN`.

The approval-stop closeout binds:

- implementer terminal return SHA-256:
  `c5b726474a8a8c93c09c9419d53291080bcf2da53626f6612446dc1073993cdf`;
- preparation attempt-2 return SHA-256:
  `c249b0afd8a1ff5b2770ba9007df491a97253aff69b0ec27206854688d0c190f`;
- C196/C197 approval request SHA-256:
  `527765a1f6162be8d2bc3d92fbd38464b934e01b0d904339099fb50f86fc49c3`;
- fresh current-byte R2 verifier return SHA-256:
  `3ea8ac736a5a41da29ac12c37a2414bca3bf2fb698ac6bf84cbfdc48f216c1e3`;
- cleanup/rollback record SHA-256:
  `d7b4dd06e27dabe7f67d7cf716044a7fd4ef6bc7cae023bc5c3f109b14680deb`;
- whitespace-repair backcheck SHA-256:
  `609fbd2e4a4528fe3e3796bbe88cbb90a6345d09133b71e11563d661a6420333`;
- run-local runtime event ledger SHA-256:
  `c062d7505b9ebbb08f7500588bb10e39343d3cd267c123ba7e5448643f49f5d5`;
- run-local runtime summary SHA-256:
  `d480c3642f205fab75e6509ab50a8d0a97c54bdace676411eba2b39363e026f6`.

`RUNTIME_SUMMARY.json` reports `PASS` for the paired closeout-only session.
The ledger truthfully records that telemetry was not initialized before the
implementer/verifier work, so earlier exact session timings, durations,
retry timing, token use, and context occupancy are unavailable and receive no
inferred value.

The pre-repair approval request and verifier hashes
`12e9e070dae902c8bf552c60b1c65ec49dc90ee0a27b5656d0b12449283c8f95`
and `dc73abac76e141a335f725a1be8bb2da32d0bad2f19807c9a0435eda1b0e2b5a`
are retained only as immutable history. The backcheck and R2 verifier prove
the one-LF repair and bind the current bytes above.
