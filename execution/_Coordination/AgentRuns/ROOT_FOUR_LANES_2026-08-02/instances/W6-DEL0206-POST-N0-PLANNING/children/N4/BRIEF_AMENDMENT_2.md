# W6 N4 brief amendment 2 — disposition of N5-R2-F01

- RequestedBy: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING`
- Runtime integration owner: `/root/w1_del0206/n4_w6`
- Predecessor amendment SHA-256: `49eb4a79bb1e5e52a47b245fbbe30b205603dc619da0c0ff584dac14d42982aa`.
- Accepted N5-R2 finding capture: `children/N5-R2/SESSION_RETURN.md`, SHA-256 `33f9e22cb25bf9a44a83f11a90deac84bab93b98c3b1ca336432d42c20e73de1`.
- Accepted N5-R2 finding: the degraded-mode candidate contains the nonexistent decision reference `D16`; the accepted instruments contain D1-D9 and stable open item `TBD-016`.
- Disposition: `EXACT_REFERENCE_CORRECTION_WITHIN_EXISTING_N4_SCOPE_AND_FRESH_RECHECK`.

## Bounded objective

Change only the defective token sequence in
`integration/DEGRADED_MODE_DELTA_CANDIDATE.md` from `D1/D6/D16` to
`D1/D6/TBD-016`. Make no other
semantic or matrix change. Then update only `integration/N4_SELF_CHECK.md`
and `integration/N4_RETURN.md` with attempt-3 provenance, exact hashes, and a
decision-reference integrity check proving that only D1-D9 are used as
decision identifiers and TBD-016 remains an open item.

Preserve the other four N4 outputs byte-identically. Reads remain the existing
N4 declared inputs plus this manager-relayed finding. No read, write, scope,
authority, semantic, client, dependency, profile/check, or lifecycle
expansion. Use non-shell Node reads/hashes/parsing and apply_patch only for
the exact three targets. No Bash, network, executable checks, runtime
execution, implementation, delegation, Git, or foreign write.

Return exact pre/post hashes, preserved hashes, proof of zero `D10`-or-higher
decision tokens across all seven N4 outputs, verdict
`ADMIT_FOR_FRESH_N5_RECHECK`, and the no-effect/write-containment statement.
