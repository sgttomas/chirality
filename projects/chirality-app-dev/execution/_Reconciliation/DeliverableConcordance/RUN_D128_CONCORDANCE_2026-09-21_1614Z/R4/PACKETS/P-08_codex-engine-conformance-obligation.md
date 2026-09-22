<!-- PACKET
id: P-08
cluster: CL-08
title: No Codex run of the conformance suite in the tree
question: The repository has no test or record that runs the K-ENGINE-2 engine conformance suite against the shipped Codex engine; must it be, or does the D-GOV-43 acceptance set replace that obligation for the Codex path?
recommended: A — run suite against Codex adapter
depends_on: P-05
decision_type: owner; engineering
tier: GOVERNING
-->
# P-08 — No Codex run of the conformance suite in the tree

Cluster CL-08 · named question R4-Q2 · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** CONTRACT K-ENGINE-2 says any provider-backed engine must pass the engine conformance suite before it becomes the default production path. The Codex engine became the only engine without a suite run. Which do you want?
- Run the suite against Codex now.
- Treat the D-GOV-43 acceptance checks as meeting the obligation.
- Retire the obligation for the Codex path.

## What we found
- K-ENGINE-2 is unamended: "Any provider/SDK-backed adapter must pass engine conformance tests before becoming the default production path" (`docs/CONTRACT.md:62`). SPEC §10.3 repeats it (`docs/SPEC.md:680`). [GOVERNING]
- The CONTRACT preamble says historical engine qualification "does not establish Codex qualification" (`docs/CONTRACT.md:15`). [GOVERNING]
- D-GOV-43 sets its own measure of done. Item 12 names eight spike checks, S-1..S-8, as "an acceptance set". Item 11 retains "request and session correctness tests" and says "a test runs once per distinct condition". Neither item names K-ENGINE-2 or the suite (`D-GOV-43.proposed.md:253-299`). [GOVERNING]
- The suite exists in the Runtime contracts package (`projects/chirality-runtime/packages/contracts/src/harness/engine-conformance.ts`). [code]
- The tests that call the suite use a scripted `stub` subject and the legacy Claude Agent SDK manager (`frontend/src/__tests__/lib/engine-conformance.test.ts:208,270`), plus the Pi adapter (`pi-omlx-wire.integration.test.ts:290`, `pi-agent-engine-adapter.test.ts:544`). No test in the tree runs it against the live Codex adapter. Whether it was ever run outside the tree is not established here (OC-06 concerned the Section 8 premerge, not this suite). [code]
- The owner confirmed that the Section 8 pre-merge run against the Codex-hosted Runtime happened (OC-06). This is a different check from the conformance suite, and it does not answer this question. [owner testimony]
- Validation evidence in general exercises the legacy harness, not the shipped Codex path (`R3/CROSS_PACKAGE_FINDINGS.csv` XPF-036). [run finding]

## Affected rows
<!-- COUNTS -->
**24 rows are decided in this packet** (PRIMARY); 8 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-08`.

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Verification out of date (`STALE_VERIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 |  |  |  | 2 |  |  | 1 | 4 |
| PKG-01 |  |  | 1 |  |  |  |  |  | 1 |
| PKG-03 |  | 5 | 6 | 1 |  |  | 1 |  | 13 |
| PKG-04 |  | 1 |  |  | 1 |  |  |  | 2 |
| PKG-06 |  |  | 2 |  |  | 1 |  |  | 3 |
| PKG-09 |  | 1 |  |  |  |  |  |  | 1 |
| **Total** | **1** | **7** | **9** | **1** | **3** | **1** | **1** | **1** | **24** |

ALSO/CONTEXT members by Disposition: Partly built 6, Built differently 2.

<!-- /COUNTS -->
Every row states the conformance obligation, or its records and verification, and the only suite runs are on stub or legacy subjects. DEL-03-01 (the engine contract deliverable) holds 13 of the 24. Nine rows also carry R4-Q1, because their other evidence is legacy only. The 8 ALSO rows are decided in P-05 and P-09.

## Options
**A. Run the suite against the Codex adapter.** An engineering brief adds a conformance run with the live Codex adapter as subject. If needed, it extends the suite for Codex-shaped events once P-05 is ruled. *R5 would:* correct the stale text (the Claude-era evidence matrix, the fallback rows, TBDs). The "written, not built" and "partly built" rows wait on the brief, then R6 backchecks them.
**B. The D-GOV-43 acceptance set meets K-ENGINE-2 for Codex.** The ruling records that the S-1..S-8 spike checks, plus the retained request and session tests, are the Codex conformance evidence. *R5 would:* rewrite the rows to cite that evidence and record "difference already permitted". An App CONTRACT/SPEC amendment names the equivalence.
**C. Retire K-ENGINE-2 for the sole-engine release.** It applies again when a second engine arrives (local models, per your recorded sequence). *R5 would:* rewrite the rows as deferred, and a governed amendment of K-ENGINE-2 and SPEC §10.3 records it.
**D. Defer.** The rows stay held.

## HELP_HUMAN recommendation (draft)
Option A:
- The suite and the adapter port both exist, so one bounded test brief closes the gap without any governance change.
- The CONTRACT preamble already says historical qualification does not qualify Codex.
- B leans on checks that were never mapped to the suite's issue codes: persistence, terminals, pairing, interrupt and redaction.

Option C is a reasonable fallback if you see the suite as multi-engine machinery that D-GOV-43 item 11's simplification was meant to drop.

**Left open:** whether suite checks that assume translated events (P-05) are kept.

## Who decides
The owner decides the obligation. The suite's design and its Codex subject are an engineering call. Runtime test code belongs to the Runtime loop. Options B and C are governed App CONTRACT/SPEC amendments. Any reading of D-GOV-43 item 11 as having retired the suite is a Root question (Root / HELPS_HUMANS).

## On ruling
- **Where recorded.** The consolidated R4 ruling record (next free D-APP ID, committed by HELP_HUMAN) names the option and the key set (`PACKET_INDEX.csv` P-08 PRIMARY).
- **Option A.** A separate `software-bounded-implementation` brief (Runtime loop, with an App test slice if needed). R5 edits only the stale text now. The code-dependent rows are backchecked by R6 after the brief lands.
- **Options B and C.** An amendment tranche, then R5 text edits in each package and an R6 backcheck.
- No lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-03-01#REM-2`: "to-do list out of step". Its gate is satisfied, but it still cites R4-Q2.
- `SOW:SOW-037` is "matches" but cites R4-Q2, because the re-run is an explicit deferral.
- `DEL-01-02#CLM-006.13` may be "matches" (K-ENGINE-5 only asks that a governed path "remain available").
- `SOW:SOW-018.2` is "governing texts disagree" (the Root-runtime first adapter). It also turns on P-04 and P-09.
- **Dependencies.**
  - P-05: the suite rejects provider-named events under a translating reading.
  - P-09: 9 rows also cite R4-Q1.
