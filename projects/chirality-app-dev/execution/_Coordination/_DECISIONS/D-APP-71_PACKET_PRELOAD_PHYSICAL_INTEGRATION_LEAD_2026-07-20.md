# D-APP-71 — Preload Physical Integration Lead

**Status:** PROPOSAL / `AWAITING_RULING`
**Decision ID:** D-APP-71
**Prepared:** 2026-07-20
**Authority posture:** owner decision required; this packet is not a ruling
**Basis:** D-APP-70 `RULED (Option A)` and post-main application basis `36a422ac5568a02ecf120c214f8e1fc96fd6ab45`

## Decision requested

Select the physical integration lead, or explicit deferral, for the single
shared file `projects/chirality-app-dev/frontend/electron/preload.ts`.
D-APP-70 already applies the shared implementation boundary across DEL-02-03
`selectDirectory`, DEL-02-05 `apiKey`, and DEL-09-06
`safeStorage`/security. This packet does not reopen those semantics. No option
is preferred or selected.

## Neutral options

1. **DEL-02-03 physical lead.** Retain DEL-02-05 `apiKey` and DEL-09-06
   `safeStorage`/security as distinct semantic boundaries. Exact response:
   `APPROVE: D-APP-71 Option 1 — DEL-02-03 physical lead`.
2. **DEL-02-05 physical lead.** Retain DEL-02-03 `selectDirectory` and
   DEL-09-06 `safeStorage`/security as distinct semantic boundaries. Exact
   response: `APPROVE: D-APP-71 Option 2 — DEL-02-05 physical lead`.
3. **DEL-09-06 physical lead.** Retain DEL-02-03 `selectDirectory` and
   DEL-02-05 `apiKey` as distinct semantic boundaries. Exact response:
   `APPROVE: D-APP-71 Option 3 — DEL-09-06 physical lead`.
4. **Defer unnamed.** Preserve the applied shared boundary with no physical
   lead and no path-level ownership or repair. Exact response:
   `APPROVE: D-APP-71 Option 4 — defer unnamed`.

Silence selects nothing. Partial or ambiguous wording does not select a lead.

## Fixed boundaries and risks

- A physical lead coordinates the shared file; it does not absorb or transfer
  the other two semantic interests.
- The source SHA-256 at preparation is
  `189b0d30bd8f6daf84862e14cfc3ec68c2c211b5c123283c7108c50c3b750ba0`.
- Selecting a lead could be mistaken for source-repair authority. This packet
  grants none: no preload edit, path-level owner application, lifecycle
  transition, release/publication, hard-fence crossing, waiver, or Git action.
- Option 4 keeps the one CQ-F1 owner-class residual open and requires a later
  decision before any physical-lead-dependent application.

## Recording and future application

A response has effect only when a separate D-APP-71 ruling record is created
and the register row moves from `AWAITING_RULING` to `RULED`. Any physical
lead or deferral application is a future separately released post-main stage
with fresh source, status, dependency, authority, containment, and
post-change validation. This packet itself makes no owner choice.

## Affected governed surfaces

- Decision packet: this file.
- Decision register: one D-APP-71 `AWAITING_RULING` row.
- Existing residual: DEL-09-04 `_STATUS.md`, exactly one CQ-F1 entry gated by
  D-APP-71.
- Applied derivative: `execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/APPLIED_DAPP70_36A422AC/`.

No source, SOW, dependency, lifecycle, release, publication, hard-fence, or
Git effect is authorized by packet preparation.
