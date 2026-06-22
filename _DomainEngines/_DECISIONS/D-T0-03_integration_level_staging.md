# D-T0-03 — INTEGRATION_LEVEL target + staging  (PROPOSAL; HumanRuling: TBD)

**Decision:** First target level and staging order across L0–L4; is L3 the destination or an intermediate?

**Why the owner's:** sets how far automation may go; top of the ladder is irreversible.

**Verified facts:** ladder `AGENT_DOMAIN_ENGINE.md:162-172`; today L0. Risk-classing NOT implemented in the engine (no `risk_class` field; uniform `professional_boundary`).

**Options:** (a) L3 destination, reached per-operation; (b) cap at L2; (c) L1 read-only only.

**Recommendation:** (a) risk-graded — L0→L1 (read) → L2 (validated-kernel headless runs) → L3 per operation risk class, **not wholesale**; L4 future-only. Subordinate to this ruling. Bind the human gate to the existing `AnalysisStatus` lifecycle (worker → `HUMAN_REVIEW_REQUIRED`; engineer → `HUMAN_APPROVED_FOR_PROJECT`).

**Unblocks:** staged build plan. **Forecloses:** one undifferentiated proposal bucket.

---
**HumanRuling:** **(a) L3 is the destination**, reached risk-graded **per-operation** (engine-checkable vs engine-silent); staging L0→L1→L2→L3; L4 future-only. Human gate binds to `AnalysisStatus`.   **RuledBy:** owner (in-session)   **Ruling SHA:** TBD (binds at CHANGE publish)   **Date:** 2026-06-21
