# D-APP-63 — DEP-04-01-012 Referral Resolution (DEL-04-01 → DEL-04-04 Handover Row Retirement)

**Status:** RULED — Option A with the rider (owner ruling 2026-07-18,
transcribed verbatim in §Human Ruling below; mechanics executed after the
ruling existed)

**Date prepared:** 2026-07-18

**Prepared by:** WI-PKG04-01 (WORKING_ITEMS, PKG-04), under brief amendment
v2 of `execution/_Coordination/AgentRuns/DEL-04-01_HANDOVER_EVIDENCE_2026-07-18/ORCHESTRATION_PLAN.md`.
Packet preparation and mechanics are agent work; the disposition recorded
here is the **owner's ruling** (K-AUTH-1; D-GOV-04) — not an agent decision.

## Context

The 2026-07-18 DEL-04-01 handover-consumption evidence tranche (PR #279,
merged by owner direction at `460ebd9399ba6e1d03909ef60720fff1310e091f`)
disposed of HANDOVER rows DEP-04-01-010..013 under the D-APP-60 instrument.
Three rows were exercised as disposition-class; **DEP-04-01-012** (DEL-04-01
→ DEL-04-04 "hand applicable implementation requirements" row, extracted from
the routing step now at DEL-04-01 `ScopeOfWork.md` CLM-018 step 13) failed
the D-APP-60 class test's determinism gate (b) and was **referred to the
owner in near-miss form** rather than decided.

Live-tree findings underlying the referral (verified 2026-07-18, both
directions): DEL-04-04 records no DEL-04-01 dependency in any register or
document; DEL-04-04 `ScopeOfWork.md` CLM-008 explicitly assigns SDK
option/message/provider concerns to DEL-04-02/03/05;
`frontend/src/lib/harness/persona-manager.ts` consumes no DEL-04-01 output;
any future SDK-version/tool-name boot-fingerprint input (PC-REQ-010) has a
recorded mediated route via DEP-04-04-004 (DEL-04-02 INTERFACE).

## Options as presented

The durable options-as-presented record is the **PR #279 body** (terminus
slate item 1) together with the tranche rationale artifact's referral slate:
`execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-01_SDK_Probe_and_Version_Pinned_Adoption_Decision/_run_records/TASK_RUN_2026-07-18_DEP-04-01-010-013_handover_evidence.md`
(§Referral slate), with full basis analysis in
`Evidence_HANDOVER_CONSUMPTION_2026-07-18.md` §C (same folder). As presented:

- **Option A — retire:** set DEP-04-01-012 to `RETIRED` /
  `NOT_APPLICABLE` with a recorded basis (no consumer-recorded need, no
  consumption trace, explicit CLM-008 scope exclusions, mediated future
  route via DEP-04-04-004).
- **Option B — keep/re-scope:** leave the row open, re-scoped pending the
  D-APP-52-gated live probe (PC-REQ-010 fingerprint inputs; the
  DEP-04-01-008 retirement-by-ruling precedent).

**Recommendation:** none was given — the referral was presented as a
recorded either/or with cited bases, per the D-APP-60 near-miss form.

## Human Ruling and Disposition

<!-- BEGIN OWNER RULING VERBATIM -->
Option A with the rider.
<!-- END OWNER RULING VERBATIM -->

**Canonical ruling-text SHA-256:**
`d6398afa4c500cff304a8bcaabf28224a5efcbc4083976b686bc822123a53279`
(UTF-8 text between the verbatim markers, excluding the marker lines and
delimiter newlines; independently recomputed by the executing instance from
the ruling text on 2026-07-18 before recording, and again from this packet's
marker span after writing — both equal the recorded value)

**Ruling context:** ruled in-session by Ryan Tufts on 2026-07-18, after the
PR #279 merge (`460ebd9399ba6e1d03909ef60720fff1310e091f`) placed the
referral on the terminus slate. "Option A" selects retirement of
DEP-04-01-012 as `RETIRED` / `NOT_APPLICABLE`. "The rider" attaches the
revival rule to the retirement note: **any DEL-04-04-relevant output from
the future D-APP-52 live probe mints a NEW row — revival by new recorded
basis** — the retired row itself is never reactivated or edited back to
life. The rider preserves Option B's live concern (future probe-derived
fingerprint requirements) without keeping a phantom open row.

## On-ruling mechanics (executed 2026-07-18, after the ruling existed)

1. This packet written with the verbatim ruling between markers; canonical
   hash recomputed before and after writing (both match the recorded value).
2. One `D-APP-63` row appended to
   `execution/_Coordination/_DECISIONS/_REGISTER.md` under the existing
   column contract; ruled rows above it untouched (register convention,
   owner-ruled 2026-07-03: ruled rows are immutable).
3. DEL-04-01 `Dependencies.csv` row DEP-04-01-012: `Status`
   `ACTIVE`→`RETIRED`, `SatisfactionStatus` `TBD`→`NOT_APPLICABLE`,
   `LastSeen` bumped; dated FACT note appended citing D-APP-63 and carrying
   the rider verbatim; all prior note text retained (supersede-never-edit).
4. DEL-04-01 `_DEPENDENCIES.md` synced (row table, ACTIVE/RETIRED and
   satisfaction counts, dated run note); `_STATUS.md` referral item removed
   from `## Remaining` with one dated History line citing D-APP-63 (no state
   change; `Checking Approval SHA` untouched); `MEMORY.md` dated note;
   run record
   `_run_records/TASK_RUN_2026-07-18_DEP-04-01-012_ruling_execution.md`
   records the mechanics with truthful attribution (retirement is the
   owner's act; the executing agent performed mechanical conformance only).
5. No lifecycle transition, no fence contact (F-APP-1..5), no DEL-04-04
   write, no commit, no receipt append — closeout belongs to N5 of the
   amended orchestration plan.

This ruling record grants no implementation approval beyond its text: it
retires one dependency row with the stated rider and nothing else.
