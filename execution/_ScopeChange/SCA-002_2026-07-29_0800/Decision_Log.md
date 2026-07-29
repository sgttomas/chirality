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

---

## Application append — 2026-07-29 (run GOV-STEP4-APPLICATION-20260729)

This append records the owner rulings and the application act. Everything
above this line is the frozen drafting-time record and is unedited.

### Owner acceptance of record

The owner accepted SCA-002 in-session on 2026-07-29, returning one line to
the Agent 0 session of record. It is recorded verbatim (49 bytes UTF-8,
SHA-256
`cfd81bc53f29c051b8d59b89b3566c36a459011c52d8deaa2eb39ddbe592208b`):

<!-- BEGIN OWNER RULING VERBATIM -->
ACCEPT SCA-002 271d456a — Ryan Tufts 2026-07-29
<!-- END OWNER RULING VERBATIM -->

The token's SHA8 `271d456a` binds the acceptance to the candidate package
commit `271d456abe854346b903f1dfbd98d8cc37fdf09e` (the commit that authored
this SCA-002 snapshot, including the exact `Gate_3_Candidate/` bytes and
`Gate_3_Validation.json` identities). The acceptance covers Gates 1–4 as
presented by this package: intake, impact, the exact Gate 3 candidate bytes,
and the propagation plan.

### Owner application ruling — SOW-042 SourceRef bracket

Drafting had surfaced the SOW-042 `SourceRef` bracket
(`[TRANSCRIBED]` vs the live PROPOSED-then-adopted D-8 row) as flagged owner
decision 1 (`Impact_Assessment.md`; manager determination 3 above). The owner
ruled in-session on 2026-07-29, recorded verbatim (116 bytes UTF-8, SHA-256
`a34878f59dcd4365a5f95fd68b7da70a452c875cc398724148c4a189d8db035a`):

<!-- BEGIN OWNER RULING VERBATIM -->
BRACKET AS RECOMMENDED: at application, update SOW-042 SourceRef to cite D-GOV-31 adoption — Ryan Tufts 2026-07-29
<!-- END OWNER RULING VERBATIM -->

Effect: at application, the SOW-042 `SourceRef` cell becomes
`PRD §5.3 D-8 [ADOPTED-D-GOV-31]`. The bracket form follows the ledger's
existing single-token bracket vocabulary (`[TRANSCRIBED]`, `[PROPOSED]`,
`[CLARIFIED]`, `[OWNER_DECLARED]` — no spaces or em dashes inside brackets).
This is an **owner-ruled application delta beyond the accepted Gate 3
candidate bytes**: exactly one cell of ledger record line 43 differs from the
candidate, and `validate_gate5_applied.py` proves that bound. The frozen
`Gate_3_Candidate/` bytes are unedited.

### Gate statuses after the owner rulings and application

| Decision | Date | State | Effect |
|---|---|---|---|
| Gate 1 (intake) | 2026-07-29 | `CONFIRMED_BY_ACCEPTANCE_TOKEN` | Covered by the acceptance act above |
| Gate 2 (impact) | 2026-07-29 | `ACCEPTED_BY_ACCEPTANCE_TOKEN` | Covered by the acceptance act above; flagged item 1 resolved by the bracket ruling |
| Gate 3 (amendment) | 2026-07-29 | `APPROVED_BY_ACCEPTANCE_TOKEN` | Exact candidate bytes approved via the SHA8-bound token; the bracket ruling adds one owner-ruled application delta on top |
| Gate 4 (propagation) | 2026-07-29 | `APPROVED_BY_ACCEPTANCE_TOKEN` | Propagation plan approved; §2 copy discipline executed with the one ruled delta |
| Gate 5 (execute + validate) | 2026-07-29 | `EXECUTED_AND_DETERMINISTICALLY_VALIDATED` | Applied in run GOV-STEP4-APPLICATION-20260729 at basis `main@204321467b567ede862636a36dd67bcac1ff326a`; `Gate_5_Validation.json` 33/33 PASS; `Applied_File_Hashes.json` records before/candidate/applied identities; Git closeout of the applied bytes is a human-gated PR whose merge authorization is a separate owner act on the exact final branch HEAD |

### Application record

1. Pre-application: the three live surfaces matched the v1.1 basis SHA-256
   identities and `validate_gate3_candidate.py` re-ran PASS 37/37 with the
   regenerated `Gate_3_Validation.json` byte-identical to the frozen copy.
2. The exact accepted candidate bytes were copied to the three authoritative
   paths; nothing was regenerated.
3. The owner-ruled bracket delta was applied to the live ledger only
   (SOW-042 `SourceRef` cell), CRLF preserved.
4. `validate_gate5_applied.py` (new, this append) validated the LIVE files:
   PASS 33/33 (`Gate_5_Validation.json`).
5. The pre-change AUDIT_DECOMP pair obligation (manager determination 6) is
   dispositioned in `Handoff_State.md`'s application append: the
   deterministic application validation plus the register baseline stand in;
   any full AUDIT_DECOMP run is deferred to the next regular audit cycle.

Decomposition revision 1.2 is the accepted current basis as of the owner
acceptance and this application; the Git publication of the applied bytes
remains a separately owner-gated human-gated PR.
