# N3.5 G-APPR Return

- **Role:** bounded ephemeral Agent 2; no delegation performed.
- **Verdict:** `SUPPORTED_FOR_DESIGN`.
- **Gate status:** no G-APPR pass claimed.
- **Primary evidence:**
  `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/_run_records/R16-G05-NONHOST-FEASIBILITY-2026-08-27/G_APPR_FEASIBILITY.md`
- **Primary evidence SHA-256:**
  `36ba3e54a0d25be05e572a1f9c0e1b093822a4515bf9ff3479908af4f6909b15`.

## Exact result

Twelve deterministic cases ran twice against synthetic `/private/tmp`
fixtures with identical canonical result SHA-256
`4a8a25f9c0e8282f3b291bfcc4cd034149d44b882b9dd170bd73eac27a84270c`:
12 passed and 0 failed.

- Three posture cases passed: default no command network denied without a
  prompt; ask per destination carried attributed `networkApprovalContext`
  with visible host/protocol and the exact grouping caveat to the synthetic
  Root API v2 managed-prompt route; labelled `network_access=true` was
  representable without execution.
- Four decision cases passed: attributed denial shape; rejection of an
  unattributed decision; rejection of `acceptForSession=true` without an
  explicit user act; and structural eligibility with an explicit user act
  while `decision=not_evaluated` and `decisionApplied=false`.
- Five refusal cases passed: missing host, missing protocol, unattributed ask
  request, unlabelled command-network-on posture, and a default posture that
  incorrectly set `network_access=true`.

The fixture SHA-256 was
`3e3db63b58a6ee69e64960d77d850955c0eeeaca2f30e165273f86db7b8054a5`;
the evaluator SHA-256 was
`6c5772e9179ba49a0e4219fcf841edbbcfca113a64a06d7ee52902581c40db6f`.
No App Server binary was needed or executed.

## Limitations and implementation implication

Empirical prompt delivery and same-destination queued-request grouping remain
`UNAVAILABLE_UNDER_BOUNDS`; R16 withholds the network-enabled, live-request
work needed to prove them. No live network, request, approval, connection,
account, generated schema/type, or production change was used or claimed.

Implementation should use a closed root-scoped three-posture policy; require
request/decision attribution and ask-route host/protocol; preserve the
grouping caveat; reject unlabelled on-state and malformed/unattributed
records; and enforce `acceptForSession => explicitUserAct`. A later separately
authorized exact-pin integration test must prove live prompt delivery and
observe destination grouping.

## Validation and cleanup

- `git diff --check` for the primary evidence: `PASS`.
- The transient directory
  `/private/tmp/chirality-r16-g-appr-n3-5-20260827` was deleted; direct absence
  and name-scan checks found no remaining path.
- Writes were confined to the primary evidence file and this return file.
- No commit was created.
