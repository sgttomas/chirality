# D-PEC-75 — Second P1 source slice

**Status:** AWAITING_RULING / SOURCE CLOSED

**DecisionID:** D-PEC-75

**Date presented:** 2026-08-02

**Owner:** Ryan Tufts

**Owning loop:** PEC

**Presentation basis:** `f98e678b1cfd80d7d03e035e5a434bdb58ca13ae`

**Decision packet:**
`../D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/PACKET.md`

## Question

Which exact P1 slice should follow accepted DEL-08-02, subject to bounded SOW
currency review and the separately adopted D-T0-27 PEC-v2 domain-profile
successor?

## Options

### O-A — DEL-01-06 typed local loop registry (recommended)

Select only DEL-01-06. First normalize only its revision/lifecycle currency
statements and return the unchanged six-item acceptance checklist for owner
review. After SOW fitness and effective D-T0-27, conditionally open the exact
typed core-port, local-JSON adapter, test, run-record, and additive project-
workflow paths in the packet. OI-003 stays open; the P1 default contains only
PEC; no governed act depends on the registry.

### O-B — DEL-01-01 record-tier model and DDL

Select only DEL-01-01. First normalize its revision/lifecycle and accepted-
hexagonal-ADR currency statements and return the same 12 AC identifiers for
owner review. After SOW fitness and effective D-T0-27, conditionally open the
exact 14-type core model, declarative DDL, in-memory tests, run-record, and
additive project-workflow paths in the packet. No live database, connector,
migration runner, parser, service, or runtime integration is included.

### O-C — Amend

State a different exact deliverable, path fence, profile posture, production
choice, check, gate, verification, or rollback condition. Consequential
amendment requires a revised packet.

### O-D — Defer or decline

Change no SOW, source, project profile, status, or domain profile. Keep
`F-PEC-1` closed over the second slice.

## Profile prerequisite and non-effects

The live PEC profile is `STALE` and denies profile-mediated invocation. Both
O-A's filesystem adapter and O-B's DDL/persistence representation are held
behind separate D-T0-27 adoption. The exact tier-0 packet is
`_DomainEngines/bridge/PEC_V2_PROFILE_SUCCESSOR_D-T0-27_2026-08-02/PACKET.md`
with candidate SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`.
D-PEC-76 is the PEC-side pointer/request row following the D-PEC-11 precedent;
it creates no duplicate adoption act. The semantic profile ruling is D-T0-27.
D-PEC-75 does not adopt, amend, or narrow a domain profile.

`projects/pec/software-workflow.json` is a project check registry, not the
domain-engine profile. The exact profile bytes, paths, checks, rollback,
lifecycle/review/fitness gates, bootstrap effects, prohibited acts, and
strict non-effects are normative in the linked packet.

No option is selected. No SOW or source path is open. No artifact acceptance,
lifecycle transition, `ISSUED`, later node, release, merge, professional
reliance, service/store/transport/runtime act, or cross-loop mandate is
inferred.

## Recommendation and ruling syntax

Recommend O-A as the smaller directed-bootstrap slice, explicitly contingent
on effective D-T0-27.

```text
D-PEC-75: O-A.
D-PEC-75: O-B.
D-PEC-75: O-C — <exact amendment>.
D-PEC-75: O-D.
```
