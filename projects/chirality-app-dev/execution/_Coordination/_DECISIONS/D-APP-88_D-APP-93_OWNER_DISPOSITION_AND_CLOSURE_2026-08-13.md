# D-APP-93 disposition and D-APP-88 closure — owner ruling

Status: `RULED — D-APP-93 DISPOSED; D-APP-88 CONCLUDED`

Decision IDs: `D-APP-93`, `D-APP-88`

Date recorded: `2026-08-13`

Owner: `Ryan Tufts`

Owning loop: `Chirality App Dev`

## Verbatim owner ruling and direction

<!-- BEGIN OWNER RULING VERBATIM -->
**OWNER** **RULING** **+** **DIRECTION** **—** **D-APP-93** **disposition** **and** **D-APP-88** **closure** **(transcribe** **verbatim)**

Under K-AUTH-1, I rule as follows.

**D-APP-93 is disposed: evidence accepted, deliverable complete.** The owner-executed trace evidence landed on main via PR [#551](https://github.com/sgttomas/chirality/pull/551) (merge f84f7b03, normalized repository identities per NORMALIZATION_AMENDMENT.md, transcript 358228ac…, raw source 43763e06…) is accepted as the deliverable's complete and sufficient product. No further packet execution or lineage is required or authorized.
**D-APP-88 is concluded on the proven finding.** The trace proved that no SIGTERM handler was bound in the shipped helper at the stop instant; combined with the retired before-quit veto that swallowed SIGTERM, this is the accepted engineering explanation of the observed stall. The held-connection server.close() stall hypothesis is recorded as **neither confirmed nor refuted** and must not be recorded as a cause. The remedy is the signal binder, bounded teardown, and held-connection regression landed via PR [#552](https://github.com/sgttomas/chirality/pull/552) (merge b0598328e), accepted as closing the failure mode under either variant.
**Record, don't relitigate.** Transcribe this ruling into the loop's instruments, update D-APP-88/D-APP-93 status and any decision-register entries per your lifecycle vocabulary, and close out affected DEL-09-04 surfaces as your instruments require. No byte of landed evidence or packet changes; no new investigation; no product/runtime/source changes. One branch, one ready-for-review PR, publication gate as usual, no merge.
<!-- END OWNER RULING VERBATIM -->

## Applied lifecycle vocabulary

- Decision-register state remains `RULED`, the register's terminal decision-act
  state. D-APP-93 is annotated `DISPOSED — EVIDENCE ACCEPTED; DELIVERABLE
  COMPLETE`; D-APP-88 is annotated `CONCLUDED — FAILURE MODE CLOSED`.
- DEL-09-04 remains `IN_PROGRESS` because unrelated packaging, release-gated,
  deployment, instruction-root, and SIGKILL residuals remain. Its D-APP-88/
  D-APP-93 helper-stop residual is removed from `## Remaining` as closed.

## Binding application

- D-APP-93 requires no further packet execution or lineage.
- The accepted D-APP-88 explanation is the absence of a SIGTERM handler in the
  shipped helper at the trace stop instant combined with the retired
  `before-quit` veto that swallowed SIGTERM.
- The held-connection `server.close()` stall hypothesis is neither confirmed
  nor refuted and is not a cause.
- PR #552's signal binder, bounded teardown, and held-connection regression are
  accepted as closing the failure mode under either variant.
- Landed packet and evidence bytes remain unchanged. No product/runtime/source,
  foreign-loop, release, issuance, or broader lifecycle act follows.
