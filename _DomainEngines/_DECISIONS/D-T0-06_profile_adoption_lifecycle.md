# D-T0-06 — Profile adoption lifecycle + sub-gates  (PROPOSAL; HumanRuling: TBD)

**Decision:** Adopt the `DRAFT→VALIDATED→ADOPTED` lifecycle and the protected-write / mutating-tool / proposal-application / external-prover / reliance sub-gates.

**Why the owner's:** adoption and each consequential transition are human gates (persona Gates 2–5; QA contract).

**Verified facts:** `VALIDATED` requires a deterministic profile-schema validator — **not built** (TOOLMAKER handoff). Current profile is DRAFT (`profiles/open_pipe_stress.DRAFT.yaml`).

**Recommendation:** adopt the persona cadence; commission the profile-schema validator via a TOOLMAKER requirement brief before any `VALIDATED` claim. Keep `operation_applier.apply` human-confirmed (K-DOMAIN-3).

**Unblocks:** moving the profile off DRAFT. **Forecloses:** "adopted" without a validator.

---
**HumanRuling:** **Persona cadence** `DRAFT→VALIDATED→ADOPTED`; `VALIDATED` gated on the **TOOLMAKER profile-schema validator** (briefed, not built — see `TOOLMAKER_BRIEF-profile_schema_validator.md`). Profile stays DRAFT until the validator exists.   **RuledBy:** owner (in-session)   **Ruling SHA:** TBD (binds at CHANGE publish)   **Date:** 2026-06-21
