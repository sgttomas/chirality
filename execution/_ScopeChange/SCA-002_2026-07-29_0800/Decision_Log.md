# SCA-002 Decision Log

## Authorizing basis

| Item | Value |
|---|---|
| Instrument | `docs/governance_harness/_DECISIONS/D-GOV-31_merge_gate_policy_succession.md` |
| Ruling (verbatim, recorded in that instrument) | `APPROVE D-GOV-31 15fba9c3 — Ryan Tufts 2026-07-29` |
| Adopted subject | PRD Revision 7, SHA-256 `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748` |
| Effective merge | `ea3db3607fbcbb7ce5f65bab31268a7eca431adb` (merge of PR #416; the record's `EffectiveSHA` field is backfilled per the D-GOV-18/19/21/22 convention) |
| Obligation drawn on | D-GOV-31 Effects §4 / POLICY_DELTA §4 row 1: SOW-042 restatement owned by SCOPE_CHANGE, plus the RB-1 row-2 census addition (`_CONTEXT.md` lines 11 and 21) carried into this plan's row-2 enumeration |

D-GOV-31 authorized the **drafting** of this amendment. It did not accept the
amendment, pre-approve any SCOPE_CHANGE gate, issue or exercise any grant, or
authorize application to live decomposition surfaces. **Owner acceptance of
this amendment is pending and is a separate act.**

## Recorded decisions

| Decision | Date | State | Effect |
|---|---|---|---|
| D-GOV-31 adoption | 2026-07-29 | `RECORDED_DRAFTING_AUTHORITY` | Obligates and bounds this candidate drafting; see above |
| Gate 1 (intake) | 2026-07-29 | `PENDING_OWNER_CONFIRMATION` | Deterministic intake checks pass (`Gate_1_Validation.md`); owner confirmation not yet requested or given |
| Gate 2 (impact) | 2026-07-29 | `PENDING_OWNER_ACCEPTANCE` | `Impact_Assessment.md` drafted; not accepted |
| Gate 3 (amendment) | 2026-07-29 | `PENDING_OWNER_APPROVAL` | Exact candidate drafted and deterministically validated (37/37 PASS); not approved |
| Gate 4 (propagation) | 2026-07-29 | `PENDING_OWNER_APPROVAL` | `Propagation_Plan.md` drafted; not approved |
| Gate 5 (execute + validate) | — | `NOT_OPENED` | No application has occurred; live surfaces byte-identical to basis |

## Manager determinations (drafting run)

1. `DECOMP_VARIANT=SOFTWARE`; `CONTEXT_ROOT=execution/`;
   `ALLOW_RENUMBERING=false`; next available ID `SCA-002`.
2. The amendment surface is the canonical working package only: two
   authoritative companion-register rows plus the working surface's change
   register, revision metadata, and REF-001 source pin. Derived and
   downstream surfaces are excluded and enumerated as other-owner work.
3. The SOW-042 `SourceRef` bracket `[TRANSCRIBED]` is retained per the sealed
   drafting brief; the resulting label-vs-live-provenance tension is surfaced
   as a flagged owner decision (`Impact_Assessment.md`), not silently
   reconciled (F6 discipline; AGENT_SCOPE_CHANGE precedence rule).
4. The candidate working surface avoids the literal superseded phrase so the
   post-application old-text census of `execution/_Decomposition/` returns
   zero hits.
5. `_LATEST.md` is repointed to this snapshot as the single active working
   snapshot (SCA-001 Gate-2 pointer precedent for an incomplete active
   snapshot), with the accepted decomposition basis explicitly stated as
   unchanged revision 1.1 and SCA-001 named as the last closed amendment.
6. Pre-change `AUDIT_DECOMP` could not be dispatched by this bounded run (no
   delegation); the deterministic register baseline substitutes at drafting
   time and the audit pair is recorded as an application-phase obligation.
7. No supersession binding exists: the amendment follows adopted upstream
   authority; it overrides no admitted authority fact. `Supersession_Map.csv`
   is generated header-only through the deterministic accumulator, carrying
   forward the SCA-001 header-only map; no `Supersession_Delta.csv` is
   authored (SCA-001 precedent).

## Current gate condition

All five owner gates are open items for the owner. Nothing is accepted,
approved, applied, or closed. The package is complete as a decision-ready
candidate and stops here.
