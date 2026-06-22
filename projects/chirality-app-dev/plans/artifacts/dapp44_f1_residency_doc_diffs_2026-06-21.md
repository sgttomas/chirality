# D-APP-44 — Reviewable Doc-Edit Diffs (F1 residency reconciliation)

**Status:** RULED + APPLIED. Owner ruled D-APP-44 = Option A (incl. the K-ENGINE-3 clarifying edit)
in-session 2026-06-21; these edits were applied to source in that tranche. Ruling record:
`execution/_Coordination/_DECISIONS/D-APP-44_RULING_2026-06-21.md`. (Edit 1's applied text reads "ruled
2026-06-21" rather than the "ruling pending" draft wording below, and Edit 7 was included per ruling.)
This artifact is retained as the before/after record of what landed.
**Date:** 2026-06-21
**Persona:** WORKING_ITEMS
**Companion record:** `execution/_Coordination/_DECISIONS/D-APP-44_PACKET_F1_RESIDENCY_RECONCILE_2026-06-21.md`
**Upstream basis (verified cold):** tier-0 ruling **D-T0-04 = OPEN RESIDENCY**
(`{REPO_ROOT}/_DomainEngines/_DECISIONS/D-T0-04_data_residency.md`,
`{REPO_ROOT}/_DomainEngines/RULINGS_PUBLISHED.md` → `RES-RECONCILE`), owner-ruled in-session 2026-06-21,
framed *"for now"*. Ruling text committed at `6e70b5aace4a3a7c4ebb20490a3bf57bfd912f45`; the ruling's own
`Ruling SHA` is recorded `TBD (binds at CHANGE publish)` (K-AUTH-2) — this proposal does not claim a bound
ruling SHA it does not hold.

## Scope and method

- **Only F1 is in scope.** Fences **F2 / F3 / F4** and **K-AUTH** are untouched by every diff below.
- The amendment converts F1 from a **categorical hard-deny** ("anything beyond the Anthropic loopback is
  denied") into an **owner-permitted configuration** ("non-Anthropic providers and private-data-to-provider
  are permitted *only* under an explicit owner provider/residency configuration; absent that, the Anthropic
  key-aware loopback default stands and the harness does not auto-egress"). The deny survives for the
  *unconfigured/default* state — it is lifted only by explicit owner configuration.
- For the **ruled** record (D-APP-39) the diff **appends an amendment note and preserves the original fence
  text** rather than rewriting history — consistent with the register rule "RULED decisions remain subject
  to their ruling record."

---

## Edit 1 — `execution/_Coordination/_DECISIONS/D-APP-39_RULING_2026-06-20.md` (canonical F1, line 23)

> **Path note:** the task prompt located this file at `plans/artifacts/D-APP-39_RULING_2026-06-20.md`; it
> actually lives under `execution/_Coordination/_DECISIONS/`. Lines 21–27 are the "Hard Fences" block;
> fence **#1** is F1.

**BEFORE**
```md
## Hard Fences (always human-gated; never autonomous)

1. Provider/network expansion beyond the Anthropic path.
2. Release/distribution posture: signing, notarization, publication, external distribution, or any
```

**AFTER**
```md
## Hard Fences (always human-gated; never autonomous)

1. Provider/network expansion beyond the Anthropic path. **[Amended by D-APP-44, 2026-06-21 — owner
   ruling pending.]** Per tier-0 D-T0-04 (OPEN RESIDENCY, owner-ruled 2026-06-21), non-Anthropic
   providers and private-data-to-provider are an **owner-permitted configuration**, not a categorical
   deny. The harness must not auto-egress or silently expand the provider/network surface; egress
   occurs only under an explicit owner-set provider/residency configuration. Absent that configuration
   the default remains the Anthropic key-aware loopback and unconfigured expansion stays denied
   (still human/owner-gated — this fence governs *who decides*, not an absolute ban). See
   `execution/_Coordination/_DECISIONS/D-APP-44_PACKET_F1_RESIDENCY_RECONCILE_2026-06-21.md`.
2. Release/distribution posture: signing, notarization, publication, external distribution, or any
```

---

## Edit 2 — `docs/BOUNDARY_REVIEW_CHECKLISTS.md` (line 25)

**BEFORE**
```md
| Scope | Keep provider/network expansion, release/distribution posture, R7 domain-engine implementation, and `CHECKING -> ISSUED` issuance behind their hard fences. |
```

**AFTER**
```md
| Scope | Keep release/distribution posture, R7 domain-engine implementation, and `CHECKING -> ISSUED` issuance behind their hard fences. Provider/network expansion is an **owner-configured** capability per D-T0-04 / D-APP-44 (OPEN RESIDENCY): not a categorical deny, but it must not auto-egress — it occurs only under an explicit owner provider/residency configuration; absent that, the Anthropic key-aware loopback default stands. |
```

---

## Edit 3 — `docs/PLAN.md` §6.3 Security and Privacy (line 351)

**BEFORE**
```md
- Current shipped renderer network guardrails remain loopback + Anthropic API.
```

**AFTER**
```md
- Current shipped renderer network guardrails default to loopback + Anthropic API. Per D-T0-04 / D-APP-44 (OPEN RESIDENCY), the owner may configure additional providers/residency (local / Anthropic / other); the renderer must not egress beyond loopback + the configured provider(s), and absent an explicit owner provider/residency configuration the loopback + Anthropic default stands. The app does not itself enforce privacy/residency, but it also does not auto-egress (default-closed).
```

---

## Edit 4 — `docs/PLAN.md` §11 Out-of-Scope Until Amendment (line 457)

> D-APP-44 **is** the amendment this line anticipated; the gate moves from "bounded future implementation
> scope" to "explicit owner provider/residency configuration."

**BEFORE**
```md
- Concrete non-Anthropic provider implementation without bounded future implementation scope.
```

**AFTER**
```md
- Concrete non-Anthropic provider *implementation* without an explicit owner provider/residency configuration and its own governed implementation tranche (per D-T0-04 / D-APP-44, OPEN RESIDENCY: provider/residency is owner-configurable, but actually building non-Anthropic routing or private-data egress remains net-new work that must still pass the engine-conformance gate (K-ENGINE-2) and respect the release fence F2; absent owner configuration the Anthropic default stands and the app does not auto-egress).
```

---

## Edit 5 — `docs/PRD.md` FR-089 (line 668, P0 hard-deny precedence)

> Minimal edit: the existing word **"unvalidated"** already left room; replace it with the precise gate so
> owner-configured expansion is permitted while *unconfigured* expansion stays a P0 deny.

**BEFORE**
```md
| FR-089 | P0 | Explicit hard-deny rules shall override all allow decisions. | Explicit provider/SDK `disallowedTools`, Chirality hook denials, path/governance denials, protected-path rules, professional/release boundaries, and unvalidated provider/network expansion blocks persona/session/operator allows and even developer-only bypass. |
```

**AFTER**
```md
| FR-089 | P0 | Explicit hard-deny rules shall override all allow decisions. | Explicit provider/SDK `disallowedTools`, Chirality hook denials, path/governance denials, protected-path rules, professional/release boundaries, and provider/network expansion **not enabled by an explicit owner provider/residency configuration** (per D-T0-04 / D-APP-44) block persona/session/operator allows and even developer-only bypass. |
```

---

## Edit 6 — `docs/PRD.md` FR-125 (line 710, product-critical denies)

**BEFORE**
```md
| FR-125 | P0 | Product-critical denies shall be enforced in Chirality-owned code or verified adapter callbacks/hooks. | Protected path writes, instruction-root writes, ambient settings, unapproved bash, ungated subagent delegation, unvalidated provider/network expansion, and human-gate transitions are denied even if provider/SDK defaults would allow them. |
```

**AFTER**
```md
| FR-125 | P0 | Product-critical denies shall be enforced in Chirality-owned code or verified adapter callbacks/hooks. | Protected path writes, instruction-root writes, ambient settings, unapproved bash, ungated subagent delegation, provider/network expansion **not enabled by an explicit owner provider/residency configuration** (per D-T0-04 / D-APP-44), and human-gate transitions are denied even if provider/SDK defaults would allow them. |
```

---

## Edit 7 — `docs/CONTRACT.md` K-ENGINE-3 (line 54) — OPTIONAL / clarifying only

> **Assessment: K-ENGINE-3 is *not reversed* by this ruling.** Its invariant — providers are substrates
> behind adapters, and *further provider expansion remains human-gated* — is fully consistent with
> "owner-configured" expansion (the owner is the human gate). The only gap is that K-ENGINE-3 is silent on
> residency/private-data. This edit is a **clarifying addendum, not a posture reversal**; the owner may
> decline it without leaving K-ENGINE-3 in conflict.

**BEFORE**
```md
| **K-ENGINE-3** | External SDKs and providers are implementation substrates behind Chirality adapters, not product identity or governance authority. Claude Agent SDK / Anthropic is the first concrete adapter and the key-aware default provider; the default-provider cutover was human-gated and ruled by D-APP-18 (Option A), and further provider expansion remains human-gated. | DIRECTIVE; PRD; product copy review; adapter implementation. |
```

**AFTER**
```md
| **K-ENGINE-3** | External SDKs and providers are implementation substrates behind Chirality adapters, not product identity or governance authority. Claude Agent SDK / Anthropic is the first concrete adapter and the key-aware default provider; the default-provider cutover was human-gated and ruled by D-APP-18 (Option A), and further provider expansion remains human-gated — now expressed as an explicit owner provider/residency configuration (D-T0-04 / D-APP-44, OPEN RESIDENCY): the app does not enforce privacy/residency and does not auto-egress, and absent an owner configuration the Anthropic key-aware loopback default stands. | DIRECTIVE; PRD; product copy review; adapter implementation. |
```

---

## Subordinate restatements (inherit the change; not part of the 7 canonical edits above)

These restate the fences operationally rather than *defining* F1. They inherit the amendment once the
canonical edits land. To avoid an on-record contradiction (K-CONFLICT-1), a one-line forward-reference is
**recommended only for the ACTIVE queue**; the rest are historical/closed and should be left intact:

| File | Location | Disposition |
|---|---|---|
| `plans/PLAN_2026-06-21_inspection_orphan_remediation.md` | active-queue fence restatement | **Recommend** a one-line note: "Fence #1 (provider/network) reconciled by D-APP-44 — owner-configured per D-T0-04; ruling pending." |
| `plans/PLAN_2026-06-20_autonomous_development_queue.md` | §2 fence #1 (line 23) | Leave intact (CLOSED/exhausted queue; historical). |
| `plans/artifacts/insp05_roadmap_addendum_2026-06-21_inspection_orphans.md` | §5 "hard fences #1/#2" (line ~72) | Leave intact (frozen backlog source). |
| `docs/ISSUE_READINESS_PROFILES.md` | line ~84 ("all PLAN §11 fences … remain in force") | Inherits via Edit 4; no separate edit needed (it references §11 generically). |
| `plans/artifacts/bridge_appdev_contribution_for_tier0_2026-06-21.md` | fence map (F1–F4) | Leave intact (historical tier-0 input doc). |

## Net behavioral change after all edits

- **Default (no owner provider/residency config): unchanged.** Anthropic key-aware loopback; no egress; the
  app does not enforce privacy but does not auto-egress. The shipped product behaves exactly as today.
- **With an explicit owner provider/residency config:** non-Anthropic providers and private-data-to-provider
  become permitted (subject to K-ENGINE-2 conformance for any real backend and the F2 release fence for
  distribution). Provider expansion stays human/owner-gated; it is never silent or agent-initiated.
