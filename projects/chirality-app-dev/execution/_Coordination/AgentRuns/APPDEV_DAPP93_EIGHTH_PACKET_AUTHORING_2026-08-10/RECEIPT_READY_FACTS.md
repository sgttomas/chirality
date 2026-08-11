# Receipt-ready facts — D-APP-93 eighth-lineage pre-dispatch block

- Parent receipt: Receipt 155.
- Baseline: `7d05b16dc7b48778856aa08a54c85f573887bea4`.
- Gate outcome:
  `STOPPED — BLOCK_DAPP93_EIGHTH_PREDISPATCH_PS_PROBE_SANDBOX_DENIED`.
- Citations/intake/recursive identities/F01–F08: PASS; no clearance rerun or
  historical authored packet reuse.
- Exact blocker: sealed F09 `/bin/ps -p $$ -o pid=,ppid=,comm=` returned
  sandbox `operation not permitted`, exit 127; it should not have been in a
  harmless no-system-state probe.
- N1: never dispatched; no child clock or authored output.
- Freeze/verifier/approval request: absent; N2 never dispatched.
- Runtime/product/keychain/system/Git/receipt/register/lifecycle/Task
  Management/foreign-loop effect: none.
- Frontend gates: skip at CHANGE closeout because no runtime source changed.
- Ninth lineage: not authorized and not begun.
