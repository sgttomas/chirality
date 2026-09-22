<!-- PACKET
id: P-03
cluster: CL-03
title: Release signing posture and the exact-candidate gate
question: Did the amended CONTRACT preamble, SPEC §19.4 and PRD §12.8 replace the "unsigned" release target, the F-APP-2 signing fence and the G6a gate?
recommended: C with b2 — amend K-RELEASE-1, PRD §6.2; G6a met by OC-01
depends_on: none
decision_type: owner (App governance amendment executed by a governed tranche)
tier: GOVERNING
-->
# P-03 — Release signing posture and the exact-candidate gate

Cluster CL-03 · run-wide call (f) · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** v3.0.0 and v3.0.1 were shipped signed and notarized. Some App governing texts still say the release target is an unsigned, unnotarized DMG. Did the amended texts replace that target, and the related fences?

- **P-03.a** — the signing posture. CONTRACT K-RELEASE-1 (the release-target invariant) and PRD §6.2 still say "unsigned/unnotarized", and D-APP-97 keeps the F-APP-2 fence on signing, notarization and distribution (19 rows).
- **P-03.b** — the G6a gate: release acts only after you name and rule the exact candidate (3 rows).

## What we found
- The amended CONTRACT preamble lists "bundle signing and notarization" as ordinary software integrity, and says K-RELEASE-1 is "read with D-GOV-43 items 1 and 4" (`docs/CONTRACT.md:17`). [GOVERNING]
- The K-RELEASE-1 row itself is unchanged: "Current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG unless amended" (`docs/CONTRACT.md:138`). [GOVERNING]
- PRD §6.2 still lists an "Unsigned, unnotarized local-builder DMG" (`docs/PRD.md:339-346`). [GOVERNING]
- SPEC §19.4 and PRD §12.8 now state a two-tier posture: ordinary local output is unsigned or ad hoc signed, while the D-GOV-43 consolidated candidate is signed and notarized, with the signature and the Codex pin verified (`docs/SPEC.md:1197-1211`; `docs/PRD.md:1389-1400`; NFR-030 at `docs/PRD.md:1202`). [GOVERNING]
- DIRECTIVE §0 puts CONTRACT and SPEC above PRD, and all three above accepted execution scope (`docs/DIRECTIVE.md:13-25`). [GOVERNING]
- D-APP-97 authorized release *preparation* only: "F-APP-2 continues to fence signing, notarization, and distribution" (ruling record line 20). No ruling in the register names F-APP-2 as lifted. [GOVERNING]
- The decomposition v3_2 row for DEL-09-05 lets WP-11 execute release acts only after the owner names and rules the exact candidate at G6a. D-APP-127 does not mention G6a (`Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:382`). [GOVERNING]
- The code signs only when a signing identity is supplied; otherwise the build is unsigned (`frontend/scripts/pack-electron.mjs:86-95`). A signing hook applies Developer ID with hardened runtime and verifies the signature (`frontend/scripts/sign-electron-runtime-v2.mjs`). [code]
- You testified that you named and authorized the exact v3.0.0 and v3.0.1 candidates (OC-01), that v3.0.1 was built and Developer ID signed (OC-02), notarized and stapled (OC-03), and published (OC-04). [owner testimony]
- The App loop's execution protocol says historical releases "are not undone by F-APP-2" and forbids inferring another release from a prior one (`loop/LOOP_INIT.md` §3). It constrains how work runs; it creates no scope. [run finding]
- The two readings R3 framed but did not resolve (`R3/RUNWIDE_CALLS.md` call f): [run finding]
  - **Reading 1** (text out of date): the preamble and §0 settle it, and K-RELEASE-1 says "unless amended". The DEL-09-04 verifier took this view.
  - **Reading 2** (governing texts disagree): the K-RELEASE-1 row, PRD §6.2 and F-APP-2 are unamended, and "read with" states no outcome. The DEL-09-05 verifier graded `CLM-026` contested.
- The done-declaration candidate asks the same question as Q-02 (see P-24). [CONTEXT]

## Affected rows
<!-- COUNTS -->
**22 rows are decided in this packet** (PRIMARY); 5 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-03`.

| Package | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|
| EXT |  | 1 |  |  | 1 |
| PKG-09 | 1 | 16 | 1 | 3 | 21 |
| **Total** | **1** | **17** | **1** | **3** | **22** |

By sub-question (`R4/PACKET_SUBQUESTIONS.csv`):

- P-03.a: 19 rows — Text out of date 15, Governing texts disagree 3, Built differently 1
- P-03.b: 3 rows — Text out of date 2, To-do list out of step 1

ALSO/CONTEXT members by Disposition: Partly built 2, Text out of date 2, Governing texts disagree 1.

<!-- /COUNTS -->
Most rows are DEL-09-04 and DEL-09-05 text that still describes the "unsigned" target. They are already graded text out of date under reading 1. Three rows are graded "governing texts disagree". Sub-question split: `R4/_work/SUBQ/P-03_subq.csv`. The rule is: (b) rows whose declared state names G6a, WP-11 or the owner-directed signed build; (a) all others. `DEL-09-05#CLM-016.3` and `#CLM-016.6` (G6a) are decided in P-02, where they are PRIMARY; their repair follows your P-03.b answer.

## Options
**A. Reading 1: already superseded.** The preamble, SPEC §19.4 and PRD §12.8 control, so the old wording is simply out of date. *R5 would:* revise the DEL-09-04 and DEL-09-05 text to the two-tier posture. The three "governing texts disagree" rows become text out of date. K-RELEASE-1 and PRD §6.2 stay as they are, which leaves the internal inconsistency in place.

**B. Reading 2: the unsigned target still binds.** Then the signed releases went beyond what the text authorizes. *R5 would:* change nothing until a later ruling. The 17 "text out of date" rows would become "built differently".

**C. Record it retrospectively and amend (a).** The ruling states that the signed and notarized candidates, and the lifting of F-APP-2 for 3.0.0 and 3.0.1, were your acts (OC-01 to OC-04). It then directs a governed amendment of the K-RELEASE-1 row and PRD §6.2 to the two-tier text that SPEC §19.4 already carries. *R5 would:* do what option A does, citing the ruling. A separate governance tranche would amend CONTRACT and PRD.

**For (b), the G6a gate:**
- **b1. Retired.** The D-GOV-43 short procedure ("explicit publishing approval") replaced G6a. *R5 would:* retire DEP-09-05-015 and restate the phase-boundary text.
- **b2. Satisfied for 3.0.0 and 3.0.1; publishing approval governs later releases.** Your authorization of the exact candidates (OC-01) is recorded as the G6a act. *R5 would:* do as b1, and name the candidates as satisfied.
- **b3. Kept open** for future candidates, with the text updated to the current procedure.

**D. Defer.** Every row stays held.

## HELP_HUMAN recommendation (draft)
**C with b2.** C is the only option that removes the conflict rather than reading past it. The releases happened with your authorization, and SPEC and PRD §12.8 already describe the posture, so the amendment only aligns K-RELEASE-1 and PRD §6.2. b2 uses your testimony as evidence of the act. It does not invent a new gate, and it leaves later releases under the D-GOV-43 publishing-approval act. Left open: whether the hosted release job (blocked at its first step) and attestation are still wanted, which is P-02 and P-24 Q-08.

## Who decides
Owner: the signing posture, the F-APP-2 fence and the G6a gate are all App matters. Amending CONTRACT and PRD is an App governance amendment. You rule it, and a separate governed tranche executes it, using the register's established corpus-bump procedure (D-APP-38, as used under D-APP-56). D-GOV-43 itself is Root and is not changed here.

## On ruling
- **Ruling record.** The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN before any repair) carries a P-03 clause. It covers (a) the posture and the F-APP-2 lift for the named candidates, and (b) the G6a answer. It lists the rows by `PACKET_INDEX.csv` P-03 and `R4/PACKET_SUBQUESTIONS.csv`.
- **R5.** The PKG-09 tranche manager, and EXT for `DOC:BUILDREL`, revise DEL-09-04 and DEL-09-05 `ScopeOfWork.md`, `_DEPENDENCIES.md` (DEP-09-05-015) and `docs/BUILD_AND_RELEASE.md` text. The two G6a rows in P-02 are included.
- **Governance tranche.** A separate tranche amends the K-RELEASE-1 row and PRD §6.2, with a validator run.
- **Checks.** R6 backchecks every listed row. No code change and no lifecycle transition.

## Risks, contested rows and dependencies
- **`DEL-09-04#CLM-022` and `#CLM-023.3`.** The verifiers read these as needing no owner decision. R3 kept "governing texts disagree" and restored the owner flag, for consistency. For `#CLM-022` the spot check (S2-031) left both readings open: reading A is text out of date, settled by the preamble; reading B is "governing texts disagree", because "read with" states no outcome. Your ruling settles both rows.
- **`SOW:SOW-072`.** It is graded "matches" because it reads the unsigned target as unamended, which is a third reading. It is not in this packet, but under C it becomes stale and needs a follow-up.
- **Overlaps.** 16 rows are also in P-17 (D-APP-127 carried into the text) and 14 are CONTEXT members of P-24 (Q-02, Q-13). Q-02 in P-24 is the same question and should take this ruling's answer.
