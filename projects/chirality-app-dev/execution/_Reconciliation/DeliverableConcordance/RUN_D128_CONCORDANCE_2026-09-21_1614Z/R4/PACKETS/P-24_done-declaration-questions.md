<!-- PACKET
id: P-24
cluster: CL-24
title: The thirteen questions about what "done" meant for v3
question: How do you want to address Q-01..Q-13 of the v3 done-declaration candidate?
recommended: D — fold six into packets; rest when ready
depends_on: P-02, P-03, P-04, P-23
decision_type: owner
tier: CONTEXT
-->
# P-24 — The thirteen questions about what "done" meant for v3

Cluster CL-24 · no named question · draft by TASK D1 for HELP_HUMAN review; not a ruling.

**Question.** At R0 the run assembled a *candidate* statement of what "done" meant for v3, from the records. It left 13 questions it could not settle from the records alone. How do you want to address them? You may answer any, all or none. No row's verdict changes because of this packet.

## What we found
- The candidate is CONTEXT until you confirm it. Its 13 questions were carried here unanswered, and rows name them only in their Notes or DirectionEvidence (`R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` §4; CONVENTIONS §1). [CONTEXT]
- D-APP-129 ruling B amended D-APP-128 §5.5.3. R2 went ahead without your confirmation, and the questions were carried to R4 "for ruling". [GOVERNING]
- This packet owns no rows. It has 34 CONTEXT members, all in PKG-09 (R3's rule: rows naming a Q-nn in Notes); each is decided in its own packet (fact sheet P-24). Counting DirectionEvidence too, about 60 rows name a question, for example Q-07 on 24 rows, mostly DEL-07-01. [run finding]
- **Q-01, release identity.** The plans named `3.0.0-rc.1` as a prerelease, but stable `3.0.0` shipped. Does done mean stable 3.0.0, with rc.1 skipped on purpose? Four DEL-09-05 rows note that rc.1 was not the shipped identity (`#CLM-010.13`, `#CLM-016.2`, `#CLM-016.3`, `#CLM-016.4`). [run finding]
- On Q-01: you testified that you named and authorized the exact 3.0.0 and 3.0.1 candidates (OC-01). [owner testimony]
- **Q-02, release act and signing fence.** Does your publishing approval count as the release act and lift F-APP-2 for the published DMG, or should a retrospective ruling record it? 26 rows name Q-02, and 13 are PRIMARY in P-03. It is the same question as P-03. [run finding]
- **Q-03, retained human acts.** Were the native trial and the system-prompt discussion completed, waived, or left open? No row names Q-03. `DOC:BUILDREL#13` notes that the packaged Runtime child spawn is evidenced only by native trials. [run finding]
- **Q-04, packaged S-6 and S-8 checks.** Were quit-relaunch continuation and Chirality-scoped sign-in and sign-out repeated on the signed build, and did later rebuilds invalidate them? Four DEL-09-05 rows name Q-04 (`#SEC-1`, `#CLM-005`, `#CLM-010.6`, `#CLM-012`). `DOC:BUILDREL#9.5` stays Unknown (P-02.b). [run finding]
- On Q-04: OC-14 (packaged S-6/S-8) and OC-16 (manual DMG checklist) were "don't know". OC-12 (a packaged run with secret and network checks) was "yes". [owner testimony]
- **Q-05, loop record gap.** The App loop receipts skip from 2026-09-07 to 2026-09-19. Are the AgentRuns records enough, or should a loop record be added? No row names Q-05. Loop receipts are execution protocol, not the audited surface. [run finding]
- **Q-06, sole-engine decision.** Where was "Codex is the only engine" first decided? Three rows name Q-06 (`DEL-09-02#CLM-010.2`, `#STATE-1`; `DEL-09-06#SEC-1`). This is the cause of 117 PRIMARY rows in P-20. [run finding]
- On Q-06: your recorded R4-Q6 answer (Codex-hosted first, local models later, API no sooner), which awaits confirmation in P-04. [CONTEXT]
- **Q-07, containment.** Does done mean the user's own Codex policy, replacing the hard envelope and the per-root network postures? 24 rows name Q-07. 20 are DEL-07-01 rows that carry R4-Q1 (P-09); `DEL-09-02#CLM-010.6` is in P-04 (R4-Q6, the live "Full access" option). [run finding]
- **Q-08, SBOM and notices.** Were these dropped on purpose, or are they still owed? No row names Q-08. `DEL-09-05#REM-1` (an optional SBOM, waiting on the Syft tool) is graded "matches". `frontend/package.json` has an `sbom:generate` script that no release step calls. Four release-document rows carry your OC-08 "don't know" (P-02). [run finding]
- **Q-09, v2 upgrade path.** Is opening v2 data without a destructive rewrite part of done, and was it checked on the published build? No row names Q-09. `DEL-05-01#REM-1` finds the migration mechanism present but the App's v2 store unmapped, and P-16 covers the inert legacy-session migration. [run finding]
- **Q-10, held bindings and deferred rows.** Are the nine held bindings and TM-ROOT-106 and TM-APP-027/028/032 retired or still open? No row names Q-10 or those IDs. [run finding]
- **Q-11, managed multi-child delegation.** Is it still part of done? `DEL-09-02#CLM-010.11` and `#REM-1` name Q-11, and the twelve rows of P-23.d depend on it. [run finding]
- **Q-12, accessibility.** Is keyboard and VoiceOver support for consent, login, approval, interrupt and logout in or out of done? No row names Q-12 or AT-034. [run finding]
- **Q-13, who performed the Apple step.** An agent notarized under your direction. Is that the accepted procedure? Three DEL-09-05 rows name Q-13 (`#CLM-010.7`, `#CLM-016.3`, `#CLM-016.6`). OC-03 confirms that v3.0.1 was notarized and stapled. The owner check did not ask who performed it. [run finding]

## Affected rows
<!-- COUNTS -->
**0 rows are decided in this packet** (PRIMARY); 34 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-24`.

ALSO/CONTEXT members by Disposition: Text out of date 16, Governing texts disagree 6, To-do list out of step 3, Partly built 3, Written, not built 2, Built differently 2, Unknown 1, Retired by a ruling 1.

<!-- /COUNTS -->
No row is decided here. The table counts the CONTEXT members, whose verdicts are set in P-03 (14), P-02 (5) and others.

## Options
**A. Confirm the candidate as written, with your answers.** *R5 would:* change nothing directly. The confirmed statement becomes a governing reference only through the ruling record.

**B. Amend it, then confirm.** You answer chosen questions and HELP_HUMAN revises the candidate. *R5 would:* do the same as A.

**C. Leave it as CONTEXT.** The candidate stays an explanatory record and is never confirmed. *R5 would:* make no change. The rows follow their own packets.

**D. Fold questions into the packets that already ask them, and answer the rest when you choose.**
- Q-02 and Q-13 take P-03's answer.
- Q-04 takes P-02.b's.
- Q-06 and Q-07 take P-04's.
- Q-11 is answered for P-23.d.
- Q-01 can be answered now from your OC-01 testimony.
- Q-03, Q-05, Q-08, Q-09, Q-10 and Q-12 stay open as questions for you.

*R5 would:* act only through those packets' rulings.

## HELP_HUMAN recommendation (draft)
**D**, optionally followed by B once the folded answers exist. It avoids answering the same question twice. It lets R5 proceed on the packets that carry rows, and it leaves the six questions without rows (Q-03, Q-05, Q-08, Q-09, Q-10, Q-12) to your timing. None of those six blocks any repair. Q-08 and Q-09 would create new work only if you say the items are still owed.

## Who decides
The owner, entirely. Q-05 (loop records) touches the App loop's execution protocol, which is also yours. Nothing here is outside your App authority, but D-GOV-43's own text (Q-06, Q-07) is Root and is not amended here.

## On ruling
- **Ruling record.** The consolidated R4 ruling record (the next free D-APP ID, committed by HELP_HUMAN before any repair) states, per question, whether it is folded, answered or left open.
- **Confirmation.** If you confirm the candidate (A or B), the same record says so, and HELP_HUMAN saves the confirmed text beside the candidate. The candidate stays unchanged as history.
- **R5.** It edits no row on the strength of this packet. Checks come through the packets that carry the rows.
- No lifecycle transition.

## Risks, contested rows and dependencies
- CONTEXT members include `DEL-09-04#CLM-022` and `#CLM-023.3`. These are the restored-flag rows contested in P-03, and are decided there.
- Depends on P-02 (Q-04), P-03 (Q-02, Q-13), P-04 (Q-06, Q-07) and P-23 (Q-11).
- Risk: confirming the candidate before those packets are ruled could fix an answer that a later packet contradicts.
