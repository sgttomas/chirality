# Sealed brief — exact three-byte repair and remaining validation

- Child: `A2-PKG09-R20-PHASEB-REPAIR-VALIDATE-04`, delegated-harness-native explicit Agent-2 session; role/non-delegation instruction-asserted; no delegation.
- Objective: verify exact preimages/tails; remove exactly one final LF from each of the three authorized VALIDATE-02 records; prove one-byte-only lineage; run only still-unreached gates.
- Write scope: only the three named VALIDATE-02 files and `instances/A2-PKG09-R20-PHASEB-REPAIR-VALIDATE-04/`. No other shared/run/source/build byte.
- Repair gates: exact preimage hashes; exact `0a0a` tails; byte count decreases by one; postimage ends in one LF but not two; `postimage + 0a` equals preimage byte-for-byte; no other path changes during repair; freeze postimage hashes.
- Immutable gates before/after: historical executor RETURN `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`; raw pack log `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`; all 15 raw-log inventory hashes from prior validator; shared R20/status/TM hashes.
- Validation: semantic whitespace remainder under accepted 15-log plus executor-RETURN-lines-23–25 exemptions; scope validator; formal final index empty; aggregate diff under exact exemptions; instruction-root refresh; exact R20 root/plist/public/failed metadata-only absence and exact service 113/two-line read-only absence; App containment/full and scoped porcelain; frontend `PROOF_REVISION..HEAD` stat empty; deterministic ordered candidate inventory/per-file/combined freeze; immutable hashes after.
- Read restriction: do not traverse an existing proof root; stop if its metadata-only absence gate fails. Do not access owner R19 Desktop evidence, private-root contents, default operator surfaces, network, or GUI.
- Do not rerun supply/build/precheck/full/focused/typecheck/practitioner/corpus/self-check/package/receipt-prior or any proof/Git action.
- Write ACTIVATION.md, REPAIR_LINEAGE.md, VALIDATION.md, RETURN.md in the instance. PASS only if exact repair and every remaining gate pass; otherwise stop exact.
