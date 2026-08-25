# ROOT LOOP STEER — v3 supply resumption 2: egress inventory and ancillary executables — 2026-08-24

> **Plans-folder status:** ACTIVE owner-carried steer — non-governing
> coordination instrument. Owner: Ryan Tufts. Target workspace: Root loop
> (DEL-02-08 lane). Authorizing ruling: R14
> (`chirality_app_v3_root_ruling_record_r14_2026-08-24.md`; SHA-256 recorded
> in the PR that published this steer — the files merged together). This
> steer further amends and resumes the supply tranche. The original
> supply-pinning steer (`1384b216889d4357b332fa3507f573d887b11aa009f49ba9b29797b23d312391`)
> and the first resume steer (`248317951603551eafd54754e79fc04b1d8082906653136ff7042dfd5132c701`)
> remain the contract except as amended by R13, R14, and this steer. Read
> them all in full before any write.

## Basis gate

1. Work on a fresh branch `codex/root-supply-resume2-2026-08-<DD>` from
   current `origin/main`. Record the exact basis commit.
2. Verify the four prior supply instruments at the SHA-256 values R14 cites,
   and incorporate this steer and R14 by immutable path and SHA-256 from the
   PR that published them.
3. Confirm no residue: no quarantine contents, no supply-run additions on
   any branch, ledger still ends at Receipt 128. Preserved stop evidence
   from the prior runs may be incorporated into this run's evidence by copy,
   with its provenance recorded.
4. If any check fails, stop and report.

## Amendments (cumulative with R13)

1. **Egress rule (R14-A).** A sandbox-denied egress attempt is recorded
   inventory: full trace, exact destination, triggering operation, all
   carried into OUT-002 and the N4 candidate.
   `https://api.github.com/repos/openai/plugins` is an admitted observed
   destination. Any completed connection, any credential prompt, or any
   write outside the disposable tree remains an immediate fail-closed stop.
   Verify before every execution run that the sandbox network-deny profile
   is in force.
2. **Plugin-sync switch probe (R14-A).** Probe the exact 0.149.0
   configuration surface for a switch governing curated-plugin
   synchronization; record its exact name, default, and readback, or record
   that none exists. Ground claims only in the artifact's own behavior and
   current official documentation, each cited.
3. **Ancillary executables (R14-B).** To produce schema/types, config
   readback, precedence, and method-inventory evidence, executables
   contained within the three pinned assets may be executed under identical
   containment, each file's SHA-256 recorded before execution. Nothing
   outside those assets may be executed or downloaded. Evidence that still
   cannot be produced is recorded `UNAVAILABLE_UNDER_BOUNDS`, not chased by
   loosening a bound.
4. **N4.** The candidate records: the complete evidence set (or documented
   gaps); the R13-B G5 vendor-signature finding; the observed-destination
   inventory with the plugin-sync switch result; and the state
   `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`.

Everything else — write set, quarantine discipline, validators, Receipt 129,
run evidence under `AgentRuns/ROOT_SUPPLY_PINNING_2026-08-<DD>/`,
PR-without-merge, sync rule, rollback extended to all downloaded assets, and
discipline — applies unchanged from the prior steers.
