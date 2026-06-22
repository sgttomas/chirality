# D-T0-02 — ProfileStatus INVALID/UNKNOWN  (PROPOSAL; HumanRuling: TBD)

**Decision:** Reconcile the persona's `ProfileStatus` self-inconsistency.

**Why the owner's:** edits the canonical persona enum (framework maintenance; not self-ruled).

**Verified facts:** `UNKNOWN` at `AGENT_DOMAIN_ENGINE.md:197`; `INVALID` at `:657` and `:378`; free field at `:830`. Epistemic Gap-vs-resolved-negative distinction `docs/TYPES.md` §10.

**Options:** (a) keep both — `NONE|DRAFT|VALIDATED|ADOPTED|STALE|INVALID|UNKNOWN`; (b) `INVALID` only (app-dev default); (c) `UNKNOWN` only.

**Recommendation:** (a). **Interpretation (this proposal's, not a TYPES.md citation):** map `UNKNOWN`≈Gap (not yet determined at intake); `INVALID`≈resolved-negative (malformed). `docs/TYPES.md` §10 defines Gap vs resolved-negative as distinct primitives but does not prescribe the enum mapping; the mapping is the working rationale offered for this ruling. Collapsing the two tokens would erase a distinction the ontology motivates. Exact diff: FM-01.

**Unblocks:** clean enum across profile + Handoff State. **Forecloses:** intake-vs-validation ambiguity.

---
**HumanRuling:** **(a) Keep both** — 7-token enum `NONE|DRAFT|VALIDATED|ADOPTED|STALE|INVALID|UNKNOWN` (apply FM-01).   **RuledBy:** owner (in-session)   **Ruling SHA:** TBD (binds at CHANGE publish)   **Date:** 2026-06-21
