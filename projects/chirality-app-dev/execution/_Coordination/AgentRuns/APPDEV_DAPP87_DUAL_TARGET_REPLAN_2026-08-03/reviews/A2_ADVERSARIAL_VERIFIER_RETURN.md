# Independent Adversarial Verifier Return — D-APP-87 Re-plan / D-APP-90

Role: fresh ephemeral Agent 2 generalist; no delegation

Verdict: `PASS`

Owner readiness: `READY FOR OWNER GATE`

## Findings

### F-01 — MAJOR — D-APP-90 register state is not a valid live-register state

The D-APP-90 packet states `PROPOSAL — AWAITING_RULING — NO OPTION
SELECTED`, and the register row's final cell says `awaiting owner ruling`, but
the row's State cell is `PROPOSAL`. The register defines its row-state
transition as `NOT_PREPARED -> AWAITING_RULING -> RULED`; `PROPOSAL` is not a
declared row state. The packet is therefore owner-ready in substance but the
register row is internally inconsistent and structurally nonconforming.

Exact repair:

- In
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`,
  change only the D-APP-90 State cell from `PROPOSAL` to `AWAITING_RULING`.
- Do not alter the packet, options, recommendation, return tokens, or any
  other register row.
- Re-run the six-column row check, D-APP ID uniqueness check, and
  `git diff --check` after the one-cell repair.

No `BLOCKER` findings and no other `MAJOR` or `MINOR` findings were found.

## Verification results

1. **PASS — adopted authority.** The D-APP-87 ruling reproduces at SHA-256
   `d13543f7164a688cd6ee5472455564e76eeba5f30acc1c157beb87017a82f0fe`
   and the selected packet at
   `079d9b9874a3a0e37d6778d907329a360efab63996a134fa67738ef3f186a577`.
   The package preserves both required targets and domain-first delivery while
   leaving implementation form unselected.
2. **PASS — architecture comparison.** A lightly skinned application graph,
   shared core with target-specific shells, and the evidence-grounded
   build-time-product-profile variant are compared with distinct strengths,
   risks, evidence needs, and elimination signals. No run file silently
   selects A, B, or C.
3. **PASS — six lanes.** UI, packaging, affected-client runtime,
   deliverables/work order, validation, and later decisions each have a
   dedicated completed lane and are summarized in the manager return and
   D-APP-90 packet.
4. **PASS — Root containment.** Generic runtime, sandbox, runtime identity,
   version, resume, and Bash are consistently `BLOCKED_BY_ROOT`. App-side
   affected-client requirements are stated without defining generic
   semantics.
5. **PASS — D-APP-88/89 discipline.** D-APP-89 is used as completed,
   validated migration evidence while Git fan-in, landed-tree census, and
   facade retirement remain separate. D-APP-88 R2 is used only as
   `BLOCKED/PARTIAL`, rolled-back structural/diagnostic evidence; its
   Unix-socket/SSE explanation remains explicitly a hypothesis rather than a
   Root cause.
6. **PASS — evidence classes.** PRD, decomposition and SCA handoffs,
   validation/build guidance, current source/package topology, Remaining
   state, D-APP-88/89 derivative evidence, and the Root response are correctly
   classified. Live source, live `_STATUS.md` files, notices, child reviews,
   and the re-plan are not elevated to authority.
7. **PASS — proposal-only effects.** Candidate deliverable amendments remain
   later PRD/SCOPE_CHANGE/owner acts. No new topology, PKG-10 execution,
   domain operation application, package identity, source change, or generic
   contract is adopted.
8. **PASS except F-01 — D-APP-90 gate.** D-APP-90 occurs exactly once in the
   live register and is the unique highest/next ID. Options A-E have clear
   effects, tradeoffs, and exact owner return tokens. Recommendation D
   authorizes comparative evidence only and does not preselect A/B/C. The sole
   defect is the State-cell mismatch in F-01.
9. **PASS — preservation and write containment.** Declared run outputs are
   confined to this AgentRuns root, the D-APP-90 packet, and the D-APP-90
   register row. Preserved planning-return hashes reproduce as
   `ee770571705d4a9d77df3c8abfdb1c8334a983af9dfa598b72148ef72a7d5a48`
   (`APPDEV_PLANNING_GATES.../MANAGER_RETURN.md`) and
   `0984d6d21b90872146cdece3699b33084453182023e30424ef7c0be2b9aec9cf`
   (`.../VERIFIER_RETURN.md`). The routed D-APP-88 notice reproduces at
   `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656`.
   The immutable six-row historical-relation file reproduces at
   `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`;
   all six rows remain `HISTORICAL_RELATION_UNKNOWN` and that surface has no
   diff.
10. **PASS — references and structure.** All 24 `BASIS_MANIFEST.csv` rows
    resolve and reproduce their SHA-256 values. `REMAINING_SNAPSHOT.csv`
    contains 36 unique reviewed deliverables, reproduces at SHA-256
    `44485ab4702aa7214ffeea1529dddff9d2f5baa30ad0c1b81a69a898b3580551`,
    and every referenced `_STATUS.md` hash and top-level Remaining count
    matches. The two child-return hashes reproduce exactly as recorded in
    `MANAGER_RETURN.md`; the D-APP-90 packet reproduces at
    `eda5303254f5d1fdf624bf49c1f6652735235f7ee59e899af6f284107d7b3c57`.
    Markdown tables and CSV field counts are structurally sound, referenced
    paths resolve, and `git diff --check` passes.

## Final disposition

F-01 has been repaired and independently rechecked. The package is suitable
to return to App `HELP_HUMAN` and Ryan Tufts for the D-APP-90 owner gate. This
verifier does not accept an option, amend authority, or authorize
implementation.

## Repair Recheck

`PASS` — on the repaired current bytes, D-APP-90 appears exactly once in the
register, its row has six content columns, its State is exactly
`AWAITING_RULING`, and scoped `git diff --check` passes for the register and
this verifier return. F-01 is closed. Terminal verdict: `PASS`; owner
readiness: `READY FOR OWNER GATE`.
