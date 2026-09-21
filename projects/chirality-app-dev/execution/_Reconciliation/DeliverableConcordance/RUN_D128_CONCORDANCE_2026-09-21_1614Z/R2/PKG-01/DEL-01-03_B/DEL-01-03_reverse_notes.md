# DEL-01-03 — R2 reverse-pass notes (worker B)

This is pass 2 against ten capability files, taken in this order: BUILD, ELECTRON, HARNESS,
ROUTES, RTCONTRACT, RTCORE, SETTINGS, SHELL, WORKSPACE, WOVEN. That is 452 capabilities in total.
The sealed ledger's SHA-256 is unchanged:
`98da94b9763827825efeea1cf9c8cfd37a06777eaff05613cd4db7bcc785121c`.

## Responses

- **CLAIMED_BY: 0.** DEL-01-03 is a copy-guidance deliverable (DOC_UPDATE). It owns no
  mechanism, so no capability is wholly its own.
- **PARTIAL: 13.** These are capabilities whose user-facing copy is the evidence that a REQ row
  relies on.

  | Row | Capabilities |
  |---|---|
  | CLM-009.1 (identity) | BUILD-009, BUILD-018, ELECTRON-031, ROUTES-039, SHELL-009, SHELL-016 |
  | CLM-009.2 (vendor identity) | SETTINGS-002, SETTINGS-009 |
  | CLM-009.3 (SDK/provider framing, R4-Q5) | WOVEN-033 |
  | CLM-009.5 (human approval) | SHELL-037 |
  | CLM-009.6 (non-binding records) | WOVEN-022 |
  | CLM-009.7 (reliance copy) | SHELL-025 |
  | CLM-009.8 (domain notice, legacy) | HARNESS-055 |

- **NOT_MINE: 439.**

## REACH disagreements, and the errata filed

The capability notes found three surfaces that are statically LIVE by import but never
rendered. I checked each one at the frozen tree.

- **Pipeline and Workbench surfaces (CAP-WORKSPACE-032 and CAP-WORKSPACE-034:
  RETIRED-UNMOUNTED, STATE=DISABLED).**
  - Their only mount is `components/shell/tertiary-sidebar-tabs.tsx:14-15`.
  - That mount is used only by the legacy loop shells, and `woven-dialogue-route.tsx:18`
    discards those shells (`void legacy`).
  - `REACHABILITY.csv` tags `pipeline-surface.tsx` as LIVE. My sealed ledger tagged
    `workbench-surface.tsx:386`, `pipeline-surface.tsx:563` and `pipeline-surface.tsx:73` as
    `REACH=LIVE`. By the brief's rule (a symbol no entry reaches is not live), those tags are
    wrong.
- **Anthropic API-key panel (CAP-SETTINGS-009: STATE=DISABLED).**
  - It sits in the non-hosted branch at `settings-view.tsx:35`.
  - `shell-frame.tsx:404` always supplies the hosted controller, so that branch never renders.
  - My sealed tag `api-key-settings.tsx:88 REACH=LIVE` is wrong. My Notes calling it an
    "unhosted settings detail" understated this: the panel is never shown.

`DEL-01-03_errata.csv` has five rows, all on the `ImplementationEvidence` field, and each
corrects the REACH tag to `LEGACY_ONLY (UNREACHED)`:

- CLM-009.2
- CLM-009.5
- CLM-009.6
- CLM-009.8
- CLM-028

No Disposition, Confidence or HumanDecisionNeeded changes:

- **CLM-009.2, CLM-009.5 and CLM-009.6** are still met by LIVE code: `hosted-bootstrap-view.tsx`,
  `request-card.tsx:132` and `selected-session-replay-lens.tsx` respectively. Rule 3 therefore
  gives no new R4-Q1.
- **CLM-009.8** already cites R4-Q1.
- **CLM-028** is a documentary term-normalization row, and its definitions still match the
  cited clauses.
- **One substantive nuance for CLM-009.6 and CLM-028.** No lifecycle-transition UI is rendered
  on the live path. The approvalSha gate survives only in the served API route (CAP-ROUTES-032 /
  CAP-WORKSPACE-022), which has no rendered caller. The live distinction between binding and
  non-binding records therefore rests on the replay-lens labels alone.

`request-card.tsx` (CAP-HARNESS-004 / CAP-ROUTES-012) is mounted by `chat-panel.tsx:56` and
`chat-attention.tsx:4`, so it is live, as the sealed ledger says.

## Census: sealed vs errata-applied

The errata change no verdict field, so the two figures are identical: ALIGNED 25 ·
STALE_SPECIFICATION 11 · NOT_AUDITABLE 6 · AUTHORITY_CONFLICT 3 (45 rows). HumanDecisionNeeded
is also unchanged: NO 40, R4 2, R4-Q1 2, R4-Q5 1.

## Coverage gaps (no forward row; not errata)

1. **CAP-ROUTES-039.** The root layout's metadata description names
   PORTAL/PIPELINE/WORKBENCH, which is stale product copy. This was already in the forward
   notes' Coverage gaps. The capability's own note confirms it.
2. **CAP-SHELL-008 / CAP-ROUTES-043.** The legacy shell chrome still carries the brand and the
   PIPELINE/WORKBENCH section titles. It is rendered only on the 404 route (CAP-SHELL-008) and
   in the discarded legacy prop (CAP-ROUTES-043). No DEL-01-03 unit covers this retained
   identity copy, and it may belong to DEL-02-01.
3. **CAP-ELECTRON-018.** The renderer egress allowlist still permits `api.anthropic.com:443`.
   This is not copy, but it is the same compatibility-history posture as the checklist line
   "Anthropic key-aware loopback default stands". It belongs to a network or reliance
   deliverable, not DEL-01-03.
4. **Several capabilities carry vendor-named copy but are STATE=DISABLED.** They are:
   - CAP-ELECTRON-033 (legacy Anthropic key channels);
   - CAP-SETTINGS-014 and CAP-SETTINGS-016 to CAP-SETTINGS-018 (consent-port copy, including
     the "Opt-in Preview" posture label).

   No DEL-01-03 row reviews their copy. They matter only if the owner rules (R4-Q1) that the
   retained paths are obligations.
5. **CAP-HARNESS-015 (LIVE, ENABLED).** The error-display mapping still includes an "Anthropic
   API key is missing for provider-backed turns" message (`error-display.ts:59`). It is live copy
   that names a vendor path which is compatibility history on the Codex engine. No forward row
   reviewed error-message copy (REQ-01/02 name "runtime messages"). This is a small live-copy
   gap, and it is not an identity breach.
