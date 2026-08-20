# Closeout Amendment 03 — V4 containment disposition

RunID: `APPDEV_DAPP86_HELPER_PARITY_RERUN_2026-08-20`
Package manager: `WI-PKG02-DAPP86-RERUN-01`
Amendment basis: Agent 0 disposition after V3
Package objective/basis change: none
Human gate: none

## Disposition

V3 remains preserved as rejected provenance with verdict
`REJECT_REPAIRED_FAN_IN`. Its rejection arose solely from an over-strict
containment criterion in its sealed brief: it treated the parent-owned Receipt
183 addition in
`projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` as a package-manager or
child-attributable write.

Agent 0 has ruled that Receipt 183 is the explicitly reserved fan-in shared
surface, is lawful external state for the package manager, is not attributable
to `WI-PKG02-DAPP86-RERUN-01` or its children, and must be excluded from the
package write-containment judgment. The later Agent 0 integrated review may
observe the receipt, but V4 must make no judgment about its semantics.

This disposition changes only the containment test applied by the fresh V4
verifier. It does not accept parity, establish the distinct-helper trigger,
authorize a rerun, restore the launcher, prove network/package retry
authorization, waive a required check, or change any package objective,
authority basis, product, deliverable, receipt, or prior evidence.

## V4 containment rule

V4 must require every write attributable to the package manager and its child
instances to remain inside this run root. The parent-owned Receipt 183 diff is
explicitly excluded from attribution and from the package containment verdict.
V4 must neither validate nor reject the receipt's content or lifecycle effect.

All other acceptance requirements remain unchanged. V3's brief, return, and
terminal status remain immutable evidence of the prior over-strict check.

## Mutation boundary

After V4 begins, no previously existing run-root artifact may change. The only
permitted V4-instance writes are its sealed `LAUNCH_BRIEF.md`, read-only
verifier `RETURN.md`, and manager-written terminal `STATUS.json`. This
amendment is frozen before V4 dispatch.
