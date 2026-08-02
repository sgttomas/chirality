# D-PEC-75 — Second P1 source slice

**Status:** RULED O-A / PRODUCER COMPLETE / REVIEW AND OWNER GATES OPEN

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

The D-T0-27 O-A application is effective at `ADOPTED / READ_ONLY` through PR
#459 merge `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`. D-T0-28 and D-T0-29
are effective supporting amendments. The exact tier-0 packet is
`_DomainEngines/bridge/PEC_V2_PROFILE_SUCCESSOR_D-T0-27_2026-08-02/PACKET.md`
with candidate SHA-256
`be3044d3b3d402d3c3268332d4386f76ddadd67f9e8bb258ba7aabee6d0cdc1d`.
D-PEC-76 is the PEC-side pointer row following the D-PEC-11 precedent; it
creates no duplicate adoption act. The semantic profile ruling is D-T0-27.
D-PEC-75 does not adopt, amend, or narrow a domain profile. D-T0-27
effectiveness satisfies only the separately governed profile prerequisite; it
does not independently open DEL-01-06 source.

`projects/pec/software-workflow.json` is a project check registry, not the
domain-engine profile. The exact profile bytes, paths, checks, rollback,
lifecycle/review/fitness gates, bootstrap effects, prohibited acts, and
strict non-effects are normative in the linked packet.

O-A selects only DEL-01-06. Its bounded SOW-currency repair completed REVIEW;
the owner held lifecycle at `INITIALIZED` and accepted only exact SOW SHA-256
`7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`
as the production contract. AC-001 through AC-006 remain `PENDING FUTURE
PRODUCTION`, with zero findings. The serialized owning-manager fan-in now
proves both packet prerequisites, so only the exact O-A source-production
phase in §§5.3–5.6 is open and ready for WORKING_ITEMS. This fan-in creates no
source byte and no `ISSUED`, later node, release, professional reliance,
service/store/transport/runtime act, or cross-loop mandate.

## Owner ruling

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. Merge PR #458 at source SHA
>    5ea7c116d32aa8f133536a1a1de6c7c1cb4a9f88.
>
> 2. D-T0-27: O-A.
>
> 3. D-PEC-75: O-A.

For D-PEC-75, this rules O-A and opens only the exact DEL-01-06 contract-
currency phase in the packet. It does not select a REVIEW type, authorize
review from `INITIALIZED`, accept a repaired SOW hash, make D-T0-27 effective,
or open source production.

## Owner Gate 5 and contract-fitness disposition

Ryan Tufts, in-session, 2026-08-02 (verbatim):

> APPROVE:
>
> 1. D-T0-29: O-A.
>
> 2. DEL-01-06 REVIEW Gate 5 — HOLD.
>
>    Retain DEL-01-06 at INITIALIZED. The SELF_CHECK populated
>    AC-001 through AC-006 as PENDING FUTURE PRODUCTION, recorded
>    zero findings, and recommends no lifecycle transition.
>
> 3. DEL-01-06 ScopeOfWork contract fitness — ACCEPT.
>
>    I accept ScopeOfWork.md at SHA-256
>    7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a
>    as the production contract for DEL-01-06.
>
>    AC-001 through AC-006 remain future-production obligations and
>    are not satisfied by this act. This acceptance does not advance
>    lifecycle, make D-T0-27 effective, independently open source,
>    authorize another P1 node, release, or professional reliance.

Item 1 remains owned by the Tier-0 instrument. For D-PEC-75, item 2 closes
Gate 5 with `HOLD` and no transition; item 3 accepts only the exact SOW bytes
as the DEL-01-06 production contract. Immutable final REVIEW evidence is
`projects/pec/execution/_Evaluation/Reviews/REV_DEL-01-06_2026-08-02_0954/`.
No source authority is independently created by REVIEW or SOW acceptance.

## Serialized effectiveness and source-gate fan-in

The two conditional O-A prerequisites are now durably satisfied:

1. DEL-01-06 exact SOW SHA-256
   `7dfa008b44d7425ab7e4fc47260d089c3d739416d666f52657d7093492ecf38a`
   is owner-accepted as the production contract after final SELF_CHECK
   snapshot `REV_DEL-01-06_2026-08-02_0954`; zero findings remain, AC-001
   through AC-006 remain `PENDING FUTURE PRODUCTION`, and lifecycle remains
   `INITIALIZED`; and
2. D-T0-27 is effective at `ADOPTED / READ_ONLY` through PR #459 source
   `0e47c218c26830a4efeb29eb2d2f3ea99142b987` and effective merge
   `d9dc65804a0719fdf869af1ef60d53dc8cb0a895`; current main basis
   `556ae59a34ac2f06ef924d367843a72ea00d1f37` descends from that merge.

Accordingly, the conditional authority already granted by D-PEC-75 O-A now
opens only packet §§5.3–5.6 for one bounded WORKING_ITEMS source-production
act. The exact path list, exact project-workflow bytes, checks, rollback, and
strict non-effects remain those in the packet. This fan-in does not itself
write source, change lifecycle, satisfy an AC, accept a future artifact,
authorize another P1 node, release, or create professional reliance.

## Recorded outcome

O-A is ruled; its contract-currency, REVIEW, Gate 5 HOLD, and exact-hash SOW-
fitness gates are complete. DEL-01-06 remains `INITIALIZED`; AC-001 through
AC-006 remain future-production obligations; zero findings remain. D-T0-27 is
effective through exact PR #459 merge identity, and serialized prerequisite
fan-in is complete. The exact O-A source-production phase is therefore
**OPEN / READY FOR WORKING_ITEMS**; no production has yet occurred.

## Source-production outcome

WORKING_ITEMS completed only packet §§5.3–5.6. The immutable core
`RegisteredLoop`, core-owned `LoopRegistry` port, replaceable JSON adapter,
one-entry PEC default/schema, fixtures/tests, exact project workflow profile,
and two deliverable run records now exist. Twelve registry tests, the six
accepted API regression tests, and harness self-check pass. Exact hashes and
all eleven verification dispositions are in
`../D-PEC-75_SECOND_P1_SOURCE_SLICE_2026-08-02/EXECUTION_HANDOFF.md`.

This is producer-complete candidate work. DEL-01-06 remains `INITIALIZED` and
AC-001 through AC-006 remain pending owner disposition. REVIEW type selection,
review-from-`INITIALIZED`, findings, Gate 5, exact-hash artifact fitness, Git
publication/merge, later P1 work, release, and professional reliance remain
separate owner acts. OI-003 stays open; no governed act depends on the local
registry.
