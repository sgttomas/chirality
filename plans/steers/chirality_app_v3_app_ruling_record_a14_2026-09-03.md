# APP RULING RECORD A14 — 3.0.0-rc.1 version identity deferred to G5 fan-in; host acts deferred — owner ruling of 2026-09-03

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: (clause 1) the disposition of the parked item `DEL-09-05-V3-06` — application of the staged 3.0.0-rc.1 version-identity patch to product — and (clause 2) the owner's answer to the two open host-act questions of the same session, the Syft `v1.18.1` install for `DEL-09-05-V3-02` and the disposable self-signed signing identity for `DEL-09-05-V3-04`. Target workspace: App-dev loop. Supersedes nothing; changes no accepted Scope of Work row. Companion instruments: A13 (`chirality_app_v3_app_ruling_record_a13_2026-09-03.md`, SHA-256 `557c64aaf765b20b877cd3a5331d0f6a4c73e562c5463eaf5f9c5e122e325271`); A12 (`chirality_app_v3_app_ruling_record_a12_2026-09-03.md`, SHA-256 `21b77b378a6511b48ea2e60e676ea1c9b7ee013d8c042769392decf57ceb29ec`; the seating that parked V3-06 on this ruling); the node B evidence `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-05_CI_Artifact_and_Release_Verification_Workflow/Evidence/VERSION_IDENTITY_3.0.0-rc.1/` (staged patch `staged_version_patch.diff`, SHA-256 `311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82`, `git apply --check` exit 0, not applied). Run evidence: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_V3_NODE_I_2026-09-03/`.

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session chat on
2026-09-03 by selecting one option per question. "[click]" marks the option
the owner selected. HELP_HUMAN relayed the ruling to a sealed ephemeral
Agent 2 generalist (Claude Fable 5.1) for a record-only transcription
tranche (node I) on branch
`codex/app-v3-nodeI-a14-version-identity-deferral-2026-09-03` from basis
`e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge). The chat
transcription is evidence of the owner act; this record is its durable
form.

## Context

A12 seated `DEL-09-05-V3-06` as `NOT_SELECTABLE_UNTIL: owner ruling
applying the 3.0.0-rc.1 version identity to product (a recorded A-series
ruling)`. Development node B (2026-09-03; Receipt 211; run record
`APPDEV_V3_NODE_B_2026-09-03`) landed `DEL-09-05-V3-03`: the
identity-consistency check `frontend/scripts/verify-version-identity.mjs`
and the staged patch that would change only `frontend/package.json` line 3
and `frontend/package-lock.json` lines 3 and 9 from `"version": "2.0.0"` to
`"version": "3.0.0-rc.1"`. Node B staged the patch without applying it;
`package.json` `version` remains `2.0.0` on `main`.

In the same node B tranche two host acts were found to be owner-only and
were left blocked as tagged: `DEL-09-05-V3-02`'s CycloneDX SBOM is
`UNAVAILABLE_UNDER_BOUNDS` because Syft `v1.18.1` is not installed on the
executing host and installing it is an owner host act (no agent download or
network act); `DEL-09-05-V3-04`'s disposable self-signed A→B
credential-transition drill is `NOT_SELECTABLE_UNTIL` the owner authorizes
creation of the host self-signed identity (and `DEL-04-05-V3-01`, since
landed by node A, PR #686). HELP_HUMAN presented both as one host-acts
question in the same exchange.

## Owner ruling — verbatim

Clause 1 — version identity (`DEL-09-05-V3-06`):

```text
Question "DEL-09-05-V3-06 is parked on an owner ruling applying the 3.0.0-rc.1 version identity to product. Node B staged the patch (package.json and lockfile version bumps, SHA 311844f0...) without applying it. What is your ruling?"
  [click] "Defer until G5 fan-in (Recommended)" — Keep product at 2.0.0 for now. The staged patch stays recorded; apply it as a bounded item when the preparation lane reaches G5 so intermediate merges do not carry an rc identity. Record as an A-series ruling deferring V3-06.
  "Apply 3.0.0-rc.1 now" — not selected.
```

Clause 2 — host acts (`DEL-09-05-V3-02`, `DEL-09-05-V3-04`):

In the same exchange HELP_HUMAN asked whether the owner would perform either
of the two pending host acts this session — installing Syft `v1.18.1` for
`DEL-09-05-V3-02` and creating the disposable self-signed signing identity
for `DEL-09-05-V3-04`. The owner answered:

```text
  [click] "Defer both"
```

The relayed dispatch reproduces the owner's selected answer verbatim; the
host-acts question is characterized here by its subject as relayed by
HELP_HUMAN rather than reproduced word-for-word. No host act occurred in
the session; both items stay blocked exactly as tagged.

## Applied meaning

- `DEL-09-05-V3-06` is deferred, not executed: product stays `2.0.0`; the
  staged patch (SHA-256
  `311844f0a8b447085bf038ccbdda353a1240a5b44ae7a91df6754c9c154b1d82`)
  remains recorded and unapplied under
  `Evidence/VERSION_IDENTITY_3.0.0-rc.1/`. The item's gate text becomes
  `NOT_SELECTABLE_UNTIL: G5 fan-in per owner ruling A14 (2026-09-03)`; the
  application is a bounded item when the preparation lane reaches G5, so
  that intermediate merges do not carry an rc identity. The rest of the
  item (trace, plan, dependencies, write locus, checks, return contract,
  removal condition) is unchanged.
- `DEL-09-05-V3-02`: the Syft `v1.18.1` host install is deferred by the
  owner on 2026-09-03; the SBOM residual stays `UNAVAILABLE_UNDER_BOUNDS`
  with the blocker as named; no `SYFT_PIN` re-pin is ruled.
- `DEL-09-05-V3-04`: creation of the disposable self-signed identity is
  deferred by the owner on 2026-09-03; the item stays `NOT_SELECTABLE_UNTIL`
  as tagged.
- This tranche is record-only: this record, the three `_STATUS.md` item
  annotations and one History line, one loop receipt, and the run record.
  No product byte, `frontend/` path, lifecycle state, Checking Approval SHA,
  host, signing, release, or Root surface is touched.

## Not ruled here

- When G5 fan-in occurs, or what evidence constitutes it (the successor
  workplan's gate discipline and the preparation lane's own items).
- Whether the staged patch bytes are still the correct application at G5
  (re-verified by `verify:version-identity` at that time; a stale patch is
  re-staged under `DEL-09-05-V3-03`'s tooling, not applied blind).
- The AT-043 UI/runtime version-reporting surfaces found ABSENT by node B
  (product work outside `DEL-09-05-V3-06`'s write locus).
- Any later performance of either host act (Syft install; self-signed
  identity), or any `SYFT_PIN` change.
- `DEL-09-05-V3-05` (G6a), G-KEY, G6a, G-HELPER, and every later gate; any
  signing, notarization, distribution, release, publication, lifecycle, or
  Root act.
