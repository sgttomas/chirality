# APP RULING RECORD A15 — per-response CSP nonce and release-preparation host acts authorized — owner ruling of 2026-09-04

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: (clause 1) the renderer-CSP rendering-mode decision gating `DEL-09-06-V3-04`; (clause 2) the owner-host Syft `v1.18.1` install needed by `DEL-09-05-V3-02`; and (clause 3) creation of the disposable self-signed identity and performance of the seated `DEL-09-05-V3-04` drill. Target workspace: App-dev loop. Supersedes nothing and changes no accepted Scope of Work row. A14 (`chirality_app_v3_app_ruling_record_a14_2026-09-03.md`, SHA-256 `f5d332f2f3ba9d99ca33f821c9054cc3656ff8a59472eaaff2f7295f1c168e06`) remains truthful dated history; its two host-act deferrals are lifted prospectively only by clauses 2 and 3 below. Run evidence: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_M_2026-09-04/`.

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session chat on
2026-09-04. The owner typed each reply in plain text through the mobile
fallback; no clickable response control was used. HELP_HUMAN relayed the
three rulings to a sealed ephemeral Agent 2 generalist for a
record-only transcription tranche (node M) on branch
`codex/app-v3-nodeM-a15-owner-rulings-2026-09-04` from basis
`719fe5e34cefc40fe0dab4b045f5f2a89341ae2f` (PR #693 merge). The chat
transcription is evidence of the owner acts; this record is their durable
form.

## Context

`DEL-09-06-V3-04` was gated on an owner rendering-mode ruling because a
per-response CSP nonce replacing `'unsafe-inline'` in `script-src` makes
the four currently prerendered packaged routes (`/`, `/chat`, `/pipeline`,
and `/workbench`) dynamic. The item also permits a hash result, but no
implementation result was previously selected.

A14 recorded the owner's 2026-09-03 deferral of two owner-only host acts:
installing the pinned Syft `v1.18.1` needed for the residual CycloneDX SBOM
evidence, and creating the disposable self-signed identity needed for the
seated credential-transition drill. On the A15 basis, Syft `v1.18.1` and
the required disposable identity are not observable on the owner host.
`DEL-04-05-V3-01`, the drill's typed-storage-state dependency, has landed.

## Owner rulings — verbatim

Clause 1 — renderer CSP (`DEL-09-06-V3-04`):

```text
Question: Do you authorize the recommended per-response CSP nonce with dynamic rendering for DEL-09-06-V3-04?
Answer (typed plain-text mobile fallback): Yes, so authorized.
```

Clause 2 — Syft owner-host install (`DEL-09-05-V3-02`):

```text
Question: Do you authorize installing Syft v1.18.1 on the owner host to unblock DEL-09-05-V3-02?
Answer (typed plain-text mobile fallback): Yes, so authorized.
```

Clause 3 — disposable drill identity and seated drill (`DEL-09-05-V3-04`):

```text
Question: Do you authorize creation of the disposable self-signed identity and the seated credential-transition drill, without authorizing Developer ID signing, notarization, Apple calls, distribution, or release-readiness claims?
Answer (typed plain-text mobile fallback): Yes, so authorized.
```

## Applied meaning

- A15 selects a per-response CSP nonce with dynamic rendering for the four
  packaged routes `/`, `/chat`, `/pipeline`, and `/workbench`.
  `DEL-09-06-V3-04` becomes `SELECTABLE` once A15 lands. This grants the
  required outcome, not an exact code shape: Next middleware or a header
  set before the packaged handler in `startPackagedRendererServer` remain
  possible implementation forms. Hash/SRI is not selected.
- The owner-host installation of Syft `v1.18.1` is authorized
  prospectively. A14's dated deferral remains valid history and is lifted
  prospectively only. This record-only tranche does not install Syft;
  `DEL-09-05-V3-02` remains operationally blocked until the required
  version is observable on the owner host. No `SYFT_PIN` re-pin is ruled.
- Creation of the disposable identity and performance of the seated
  disposable self-signed A→B credential-transition drill are authorized
  prospectively. A14's dated deferral remains valid history and is lifted
  prospectively only. This record-only tranche creates no identity and
  performs no drill; `DEL-09-05-V3-04` remains blocked until the
  owner-created disposable identity actually exists. Its typed-state
  dependency `DEL-04-05-V3-01` is already landed.
- This tranche changes only this record, the bounded ruling/gate
  annotations and History lines in the two affected `_STATUS.md` files,
  one loop receipt, and the node M run record. No `frontend/` path is
  touched, so the A1 re-stage rule is not applicable and no re-stage
  declaration is needed.

## Not ruled or performed here

- No exact nonce implementation shape and no hash/SRI result.
- No Syft installation, download, network operation, identity creation,
  credential-transition drill, or other owner-host mutation.
- No Developer ID signing, notarization, Apple call, distribution,
  publication, release-readiness, or production identity act or claim.
- No retagging or split of `DEL-09-06-V3-03`; it remains byte-unchanged.
- No SCOPE_CHANGE ruling or action. The separately authorized SCOPE_CHANGE
  conversation is outside this A15 record and tranche.
- No product, `frontend/`, Root, register, decomposition, lifecycle, or
  Checking Approval SHA change.
