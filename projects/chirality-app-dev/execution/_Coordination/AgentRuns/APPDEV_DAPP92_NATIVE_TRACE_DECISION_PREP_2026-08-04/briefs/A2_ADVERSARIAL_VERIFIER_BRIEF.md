# Agent 2 brief — D-APP-92 packet adversarial verification

## Role and objective

Act as a genuinely fresh read-only ephemeral-generalist Agent 2. Determine
whether the D-APP-92 proposal packet and register row are decision-ready,
evidence-calibrated, internally consistent, authority-contained, and complete
for owner presentation.

Return exactly one verdict: `ACCEPT`, `ACCEPT_WITH_NONBLOCKING_NOTES`, or
`BLOCK`.

## Sealed read scope

- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-92_PACKET_NATIVE_SIGNAL_TRACE_AND_REPLAY_2026-08-04.md`;
- the D-APP-92 row only in
  `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`;
- this run root's `ACTIVATION.md`, `EVIDENCE_BINDING.md`, and
  `DECISION_DESIGN.md`;
- D-APP-88 packet/ruling, D-APP-89 ruling, and D-APP-91 ruling;
- Receipt 117 and the Root TM-ROOT-112 notice;
- the R3 `VALIDATION.md`, `MANAGER_RETURN.md`, `HANDOFF_STATE.md`,
  `ROOT_EVIDENCE_FITNESS.md`, implementer-02 return/first-signal proof,
  diagnosis-02-R2 return/causal matrix/evidence inventory, and verifier-02
  return; and
- current DEL-09-04 `_STATUS.md` and the historical-relation ledger only for
  the claims cited by the packet.

Read-only filesystem, hashing, Git status/diff, and text-search inspection are
allowed. No writes, Git mutation, network, provider, native tracing, process
signals, credential access, delegation, product execution, or ruling is
allowed.

## Required checks

1. Confirm D-APP-92 is the next free unique App ID, appears in exactly one
   register row, is `PROPOSAL — AWAITING_RULING`, and has no ruling record.
2. Reproduce the packet SHA-256
   `c83a7504013484fb276ae5d3c5682ee48dd4b5e05df20f714654cc1071fea91d`
   and confirm the register row cites it exactly.
3. Confirm every cited R3 and authority hash material to the decision and flag
   any mismatch or unsupported upgrade.
4. Verify the fast-reject/owner-class reason: the next step requires native
   tracing/tool/privilege or entitlement exposure beyond the approved item.
5. Verify options are mutually distinguishable and decision-complete:
   - A is bounded interactive GUI-session native trace plus sealed exact
     uninstrumented replay and is the non-binding recommendation;
   - B is sealed uninstrumented repetition without native tracing, expressly
     lower-value/non-causal and inadequate by itself for remedy/acceptance;
   - C defers/parks while D-APP-88 remains open and the shared-identity
     recovery baseline remains operative.
6. Challenge Option A for implicit broad authority. Every tracing command/tool
   and any privilege/entitlement must remain individually bounded; credential
   access, persistent entitlement/security changes, generic shell/tracing
   grants, and product instrumentation must remain prohibited.
7. Confirm the mandatory first-signal gate is not weakened and no product
   remedy is fabricated or silently authorized.
8. Confirm preservation of Root TM-ROOT-112 calibration, D-APP-89 baseline,
   D-APP-91 planning-only/TM-PIP-025 rider, six D-APP-81 UNKNOWN rows, Node
   22.19/safeStorage/premerge/release-quality/practitioner limitations, and no
   D-APP-88/DEL-09-04/TM-APP-036 closure.
9. Confirm exact owner return tokens, no selected option or ruling, and no
   release/Git/product/receipt/foreign-loop effect.
10. Distinguish the pre-existing R3/deliverable dirty paths from this run's
    allowed writes and confirm this run writes only its run root, the packet,
    and the single register row.

## Return contract

Return a compact durable report with:

- verdict and freshness/tool declaration;
- check-by-check result;
- packet hash and register consistency result;
- blocking findings with exact path/section and required repair;
- nonblocking notes; and
- explicit confirmation that no selection, ruling, or execution authority was
  created by the review.

Do not write the return. The manager will preserve it under this run root's
`reviews/` directory and compute its content hash.
