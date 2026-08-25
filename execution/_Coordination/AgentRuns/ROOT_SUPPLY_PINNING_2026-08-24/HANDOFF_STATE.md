# Root Supply Pinning R14 Handoff State

Date: 2026-08-24

Status: `AWAITING_OWNER_G2_ACCEPTANCE`

## Returned subject

The exact candidate is
`execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/_run_records/APP-SERVER-0.149.0-G2-CANDIDATE-2026-08-24/`.
It is marked `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`; its fresh review has
zero actionable findings.

## Established state

- The three official macOS arm64 release assets are exact and contain the same
  App Server payload, SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`.
- The R13-admitted vendor-signature defect is reproduced with no additional
  supply disagreement and remains a named G5 open finding.
- Exact 0.149.0 configuration, precedence, `multi_agent_v2`, and all 118
  features are recorded.
- `features.plugins` is the whole-plugin switch governing the observed startup
  operations; baseline/default is enabled and an explicit false override
  suppresses all three observed attempts.
- The three sandbox-denied destinations and their triggering operations are
  recorded for OUT-002. No committed trace records a completed connection.
- Generated JSON schema, generated TypeScript types, and the exhaustive
  schema-derived method inventory remain `UNAVAILABLE_UNDER_BOUNDS`.
- Nine of ten vendor runs have complete attributable per-run gate records.
  The `version` run's gate-hash record is absent and its committed preflight
  files are empty; that gate evidence is `UNAVAILABLE_UNDER_BOUNDS`. No new
  vendor execution was authorized or performed during correction.

## Owner decision and remaining blockers

The next act is the owner's G2 acceptance, hold, correction, or rejection of
the exact published candidate. Acceptance itself would not amend a pin,
dispose the G5 signature finding, authorize implementation/cutover/release, or
lift a blocker or hold. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers; all ten
existing DEL-02-06 bindings remain held. OUT-002 policy adoption and every App
act remain separately governed.

Artifact bytes and disposable state are absent. The branch is ready for the
human PR merge gate only; this run does not merge.
