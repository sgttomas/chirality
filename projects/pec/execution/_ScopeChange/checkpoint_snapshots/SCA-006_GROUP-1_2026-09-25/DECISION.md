# SCA-006 checkpoint group 1 — accepted impact assessment and change set

Recorded 2026-09-25 by HELP_HUMAN (undertaking
`HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node R1). This is a
faithful record of the owner's act in the session chat, transcribed under
K-AUTH-1. It is not a new request for the same decision, and it claims no
inspection the owner did not perform.

## What the owner had in front of them

HELP_HUMAN's chat messages of 2026-09-25 did three things:
- reported that the checkpoint-1 package merged as PR #922 (`b1145955e`);
- summarized the recommended set (DQ-a + ENV-a + BUD-a + GATE-a + INS-a), the 54-action change set, the nine affected Scopes of Work and the checkpoint-2 consequences;
- gave the one-line form for taking every recommendation.

HELP_HUMAN also noted that D-PEC-95 later changed deliverable metadata
after the package's baseline audit. The change touched re-pinned contexts and
references and refreshed evidence quotes, and no text that SCA-006 amends.

The owner then asked for the DQ-a and DQ-b implications. HELP_HUMAN
explained the difference:
- (a) adds a new read-only `agent` access class: least privilege, separately
  revocable, and attributable;
- (b) reuses the `harness` class, whose rights include the hooks CLI's
  presence and status writes: 49 actions and 7 affected SOWs, with no
  separate attribution.

HELP_HUMAN also said that neither option makes anything usable before a
release passes the §12 reliance gate, and recommended (a).

## The owner's act (verbatim)

> SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded

## HELP_HUMAN's interpretation (interpretation, not owner text)

| Item | Effect of this acceptance |
|---|---|
| CP1-A | The parsed change set in `Amendment_Actions.csv` (SHA-256 `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891`, 54 PROPOSED actions: 12 ADD / 42 MODIFY) is confirmed as the intake for the recommended set. The snapshot CSV is not rewritten. |
| CP1-B | `Impact_Assessment.md` is accepted at SHA-256 `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691`. Its §13 option deltas remain historical alternatives. |
| CP1-DQ | (a): direct query through tool calls is specified now, with a read-only `agent` access class. The rows specific to the agent class are Seq 3, 20, 31, 41 and the advisories Seq 50 and 51. The direct-query rows kept under every DQ option include Seq 4, 7, 9, 10, 15, 21, 26, 28 and 34 (Impact Assessment §13.1). The token mechanism stays the open §16.6 decision. |
| CP1-ENV | (a): a new PEC-ORI-007 mapped through SOW-097 to DEL-04-03. |
| CP1-BUD | (a): a new PEC-API-006 mapped through SOW-098 to DEL-08-03, with numeric values confirmed at P1. |
| CP1-GATE | (a): a standing §12 gate for any release that advertises operational reliance, with SOW-100 and a new DEL-10-13. The §12 P1 row text is not edited. |
| CP1-INS | (a): the `projects/pec/AGENTS.md` change is carried at checkpoint 3 as an instruction tranche with its own manifest and notices. |
| CP1-RC | R-C stays excluded, as `D-PEC-90` selected R-A. |

## What this acceptance authorizes and does not authorize

It authorizes preparation of the checkpoint-2 package only:
- the exact amendment: the PRD v2.4 successor candidate, the decomposition
  revision 1.6 amendment preview and postimage, and the
  `projects/pec/AGENTS.md` text;
- the propagation plan, including the Scope of Work set (Impact Assessment
  §7.1), PROJECT_SETUP for DEL-08-06 and DEL-10-13, the tier-0 profile act
  that must precede any declared or invoked PEC tool surface, and the notices;
- `Supersession_Delta.csv` for the candidate bindings SB-1..SB-6.

It applies no change to any of these: the PRD, `projects/pec/AGENTS.md`, the
decomposition or its registers, any pointer, Scope of Work, SPEC,
`_CONTEXT.md` or `_STATUS.md`, `v2/**`, `software-workflow.json`, the tier-0
profile, or any foreign surface. It changes no access class in any running
code. It adopts nothing for any consumer, lifts no reliance hold, and makes
no release, CHECKING, ISSUED or acceptance claim.

The amendment-qualified pointer `../../SCA-006_GROUP-1_AUTHORIZED.md` is
written under the scope-change method ("finalize the group-1 decision
snapshot and pointer"). `_ScopeChange/_LATEST.md` is not touched, and still
names SCA-005.

**Baseline note for checkpoint 2.** The package reused
`COV_SCA005_POSTSETUP_2026-09-25_1606` as its pre-change baseline. Its §2.1
says the audited inputs equal the pre-change state byte for byte. The
`D-PEC-95` act (PR #924, `abfd0897b`) has since changed 119 derivative
paths: the pointers, `_COORDINATION.md`, 42 contexts, 64 references and 10
dependency registers. So the §2.1 statement no longer holds exactly, although
no text SCA-006 amends changed. The checkpoint-2 package must state this. The
checkpoint-3 audit must attribute the resolution of COV-068/069/072/073 to
`D-PEC-95`, not to SCA-006.

Upstream instruments that remain current during preparation:
- accepted decomposition revision 1.5 (`SOFTWARE_DECOMP.md` SHA-256
  `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`);
- live PRD v2.3 (SHA-256
  `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`);
- the accepted SCA-005 snapshot;
- `D-PEC-90` R-A;
- fences F-PEC-1..4.
