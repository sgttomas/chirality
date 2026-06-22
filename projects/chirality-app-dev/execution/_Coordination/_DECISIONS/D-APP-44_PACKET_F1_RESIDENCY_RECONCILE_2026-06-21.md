# D-APP-44 — PROPOSAL: Reconcile fence F1 to tier-0 D-T0-04 (OPEN RESIDENCY)

**Status:** PROPOSAL — `AWAITING_RULING`. Agents propose; the owner rules; CHANGE publishes. This packet
records no ruling and claims no approval or ruling SHA it does not hold (K-AUTH).
**Date:** 2026-06-21
**Decision ID:** D-APP-44
**Persona:** WORKING_ITEMS
**Companion artifacts:**
- Reviewable doc-edit diffs (before/after, **not applied**): `plans/artifacts/dapp44_f1_residency_doc_diffs_2026-06-21.md`

## Decision to rule

Adopt (on the app-dev side) the F1 reconciliation that tier-0 ruling **D-T0-04 (OPEN RESIDENCY)** requires:
amend fence **F1** from a **categorical hard-deny** of provider/network expansion beyond the Anthropic path
into an **owner-permitted configuration** — non-Anthropic providers and private-data-to-provider are
permitted *only* under an explicit owner provider/residency configuration; absent that configuration the
Anthropic key-aware loopback default stands and the harness does not auto-egress.

## Why this is the owner's to rule

F1 is a **hard fence**. Amending it changes the shipped product's provider/network/privacy posture — a
material, security-relevant, public-contract change. Under the decision-latitude model the agent decides
forks *within* the fences but escalates changes *to* a fence as a PROPOSAL. D-T0-04's `RES-RECONCILE`
directs the app-dev loop to perform this reconciliation; this packet **is** that reconciliation, drafted
for the owner's app-dev-side ruling.

## Upstream basis — verified cold against source (not trusted from the relay)

| Fact | Source | Verified |
|---|---|---|
| D-T0-04 = **OPEN RESIDENCY**, owner-ruled in-session 2026-06-21, framed *"for now"* | `{REPO_ROOT}/_DomainEngines/_DECISIONS/D-T0-04_data_residency.md:18` | ✅ read |
| Harness may see the private model + Class-B inputs; app does **not** enforce privacy/residency; **any** provider (local/Anthropic/other) permitted; L3 not residency-blocked | same, `:18` | ✅ |
| `RES-RECONCILE`: app-dev fence **F1** (PRD `FR-089`/`FR-125` P0 deny) "must be reconciled" by the **app-dev loop**; tier-0 cannot edit it | `{REPO_ROOT}/_DomainEngines/RULINGS_PUBLISHED.md:26-32` | ✅ |
| Ruling text committed at `6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45` (HEAD); ruling's own `Ruling SHA` is **`TBD (binds at CHANGE publish)`** per K-AUTH-2 | `D-T0-04…md:20`; `git merge-base` | ✅ — SHA-binding still pending; not over-claimed here |
| F1 canonical definition = hard fence **#1**, "Provider/network expansion beyond the Anthropic path" | `execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md:23` | ✅ (prompt mislocated this at `plans/artifacts/`) |
| "Live binding must not proceed against an unreconciled fence." | `RULINGS_PUBLISHED.md:32` | ✅ |

## Options

- **Option A (recommended) — Amend F1 to owner-permitted configuration.** Apply the 7 canonical edits in
  the diffs artifact (D-APP-39 fence #1 note; BOUNDARY_REVIEW_CHECKLISTS; PLAN §6.3 + §11; PRD FR-089 +
  FR-125; CONTRACT K-ENGINE-3 clarifying-only). Default stays Anthropic loopback / no auto-egress; expansion
  is owner-configured and stays human-gated.
- **Option B — Defer (no amendment now).** F1's hard-deny and D-T0-04 remain in conflict **on record**
  (K-CONFLICT-1, surfaced not silently resolved). Gate-safe — nothing egresses — but **live binding /
  L3 cannot proceed** while the fence is unreconciled, which blocks the tier-0 bridge's residency-dependent
  path.
- **Option C — Broader reversal.** Drop the deny outright / treat providers as freely interchangeable.
  **Not recommended:** it discards the gate-safe default, contradicts the owner's *"for now"* framing, and
  would also touch K-ENGINE-6 strategy (out of this packet's scope).

## Recommendation

**Option A.** It satisfies D-T0-04 exactly, preserves the gate-safe default the owner relied on, keeps
expansion human/owner-gated (no silent or agent-initiated egress), and is reversible as a configuration
change (honoring *"for now"*). It changes posture only — it authorizes no implementation.

## Scope boundaries (what this packet does NOT do)

- **Only F1.** Fences **F2 (release/distribution), F3 (R7 domain-engine impl), F4 (`CHECKING→ISSUED`)** and
  **K-AUTH (truthful attribution)** are explicitly untouched.
- **No implementation.** Lifting the categorical fence does not build non-Anthropic routing or private-data
  egress. Any real backend still must pass the **K-ENGINE-2** engine-conformance gate and respect **F2**;
  those are separate, intact gates.
- **No K-ENGINE-6 reversal.** Provider-adapter generality was already the strategic architecture
  (`SCA-APP-001`); F1 was the *shipping* fence, not the strategy. This packet does not reopen K-ENGINE-6.
- **Not applied, not committed, not ruled.** Diffs are review-only; CHANGE applies and commits after the
  owner rules. No `D-APP-44_RULING_*.md` exists or should be inferred.

## Conflict-on-record status (until ruled + published)

Until the owner rules D-APP-44 and CHANGE publishes, **F1's hard-deny remains in force** and conflicts on
record with D-T0-04 (K-CONFLICT-1). Per `RULINGS_PUBLISHED.md:32`, **live binding must not proceed against
this unreconciled fence.** This packet surfaces the conflict and proposes its resolution; it does not
resolve it.

## Risks

- **Residency/egress surface opens by configuration.** Mitigated by default-closed: no egress without an
  explicit owner provider/residency config; the harness never auto-expands.
- **Editing a ruled record (D-APP-39).** Mitigated by appending an amendment note and preserving the
  original fence text (no history rewrite), per the register rule.
- **"for now" provisionality.** Mitigated by keeping the change reversible (a config default-flip, not a
  code rollback) and by recording the owner's provisional framing in every edit.

## Validation implications (if ruled Option A)

- Governance/docs tranche gates (D-APP-39 §4 / queue plan §4): `git diff --check`; reference/link existence;
  stale-pointer search.
- **D-APP-38 authority-corpus** `status`/`bump`/`apply` is triggered — `docs/PRD.md`, `docs/PLAN.md`,
  `docs/CONTRACT.md` are authority documents; editing them bumps the corpus version and re-reconciles
  deliverable reference rows.
- App-dev-only staging; `git diff --cached --name-only` must show **only** `projects/chirality-app-dev/`.

## Affected files (for CHANGE; see diffs artifact for exact before/after)

Canonical edits (7): `execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md` ·
`docs/BOUNDARY_REVIEW_CHECKLISTS.md` · `docs/PLAN.md` (×2: §6.3, §11) · `docs/PRD.md` (×2: FR-089, FR-125) ·
`docs/CONTRACT.md` (K-ENGINE-3, optional). Recommended forward-ref (1): the ACTIVE queue
`plans/PLAN_2026-06-21_inspection_orphan_remediation.md`. New proposal files (this turn):
this packet + `plans/artifacts/dapp44_f1_residency_doc_diffs_2026-06-21.md` + the `_REGISTER.md` row.

---

## Implications Note (deliverable 3)

**What F1 protected.** The app was built Anthropic-loopback-only (`docs/PLAN.md:351`). F1 was a categorical
hard-deny preventing: (a) any non-Anthropic provider backend; (b) renderer network egress beyond loopback +
the Anthropic API; (c) private-data / IP egress to any provider; (d) silent or agent-initiated expansion of
the provider/network surface. It backstopped the privacy posture (no private data leaves the
loopback+Anthropic boundary) and the P0 hard-deny precedence (`FR-089`/`FR-125`).

**What changes.** D-T0-04 removes the *categorical* deny. The harness may see the private model + Class-B
inputs; any provider (local/Anthropic/other) is permitted; the app does not enforce privacy/residency. F1
becomes an owner-permitted configuration.

**The new guardrail that replaces the hard deny.** **Explicit owner provider/residency configuration** is
the gate. Default = Anthropic key-aware loopback, **no egress, default-closed**. The deny survives for the
unconfigured/default state and is lifted only by explicit owner configuration. Expansion stays
human/owner-gated — never silent, never agent-initiated. This preserves D-T0-04's gate-safe default.

**Security / architecture follow-ups** (none required to land the posture change; flagged for the eventual
implementation tranche, which is still gated):
1. **Renderer network allowlist must become configuration-driven and default-closed.** The Electron
   blocked-URL guardrail currently hard-codes loopback + Anthropic; an owner-configured provider implies an
   owner-set allowlist, not a code constant. (Related surface: ORN-02 sanitizes the blocked-URL log.)
2. **Redaction must extend to any configured provider's logs/stderr** (`docs/PLAN.md:350,352`), which today
   assume the Anthropic path.
3. **Secret handling / evidence re-scope.** A non-Anthropic provider implies new secret types; the
   secret-scan + network-proof evidence (ADQ-15/ADQ-16) was built against the Anthropic-only assumption and
   must be re-scoped if a provider is actually configured.
4. **Provisional ("for now").** Keep the amendment reversible — a config default-flip, not a code rollback —
   so the owner can re-close residency without reverting code.
5. **This is policy only.** Building non-Anthropic routing or private-data egress remains net-new work
   behind the K-ENGINE-2 conformance gate and the F2 release fence; those stay intact.
