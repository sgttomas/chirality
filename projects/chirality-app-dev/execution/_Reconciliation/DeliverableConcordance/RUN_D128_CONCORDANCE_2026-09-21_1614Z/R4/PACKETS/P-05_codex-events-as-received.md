<!-- PACKET
id: P-05
cluster: CL-05
title: Codex event payloads stored as received or translated
question: Now that D-GOV-43 and the amended event clauses say Codex events are kept as received, do the unamended translate-everything clauses (K-ENGINE-4, SPEC §10.3) still bind the live Codex path?
recommended: A — as received; amend K-ENGINE-4, SPEC §10.3
depends_on: P-04
decision_type: owner
tier: GOVERNING
-->
# P-05 — Codex event payloads stored as received or translated

Cluster CL-05 · named question R4-Q5 · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** Two sets of App rules now disagree:
- Amended CONTRACT K-EVENT-1 and K-EVENT-6 and SPEC §11 say Codex events cross into the App with their method names and payloads preserved.
- The unamended CONTRACT K-ENGINE-4 and SPEC §10.3 say provider messages must be translated into Chirality-owned shapes, with provider names allowed only as adapter metadata.

Which rule governs the live Codex path?

## What we found
- K-EVENT-1 (`docs/CONTRACT.md:78`) and K-EVENT-6 (:83) are marked "Under D-GOV-43". They require upstream method names, identifiers and payloads to be preserved, and unfamiliar notifications to stay inspectable. [GOVERNING]
- K-ENGINE-4 (:64) and SPEC §10.3 (`docs/SPEC.md:673-680`) are unamended. They say `HarnessEvent`, session storage and permission decisions must not become provider-shaped, and that the adapter "MUST translate" external names. [GOVERNING]
- D-GOV-43 item 2 forbids "projection to a closed generic event schema", and says an unfamiliar notification is "kept in the event log, never dropped" (`D-GOV-43.proposed.md:156-171`). It does not name K-ENGINE-4 or SPEC §10.3. [GOVERNING]
- The live code stores events as received. The Runtime's Codex adapter wraps each notification as `codex.notification` with the original `method` and `params` (`projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:282,289`). The session store appends it to `events.jsonl` (`packages/core/src/session-store.ts:813-822`). [code]
- The same tension is graded differently across packages: "governing texts disagree", "built differently", "partly built" or "text out of date" (`R3/CROSS_PACKAGE_FINDINGS.csv` XPF-013). The spot checker saw the same thing: K-ENGINE-4 restatements are dispositioned inconsistently (`R3/R3_SPOT_CHECK.md`, systematic observations). [run finding]

## Affected rows
<!-- COUNTS -->
**53 rows are decided in this packet** (PRIMARY); 12 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-05`.

| Package | Matches (`ALIGNED`) | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | Governing texts disagree (`AUTHORITY_CONFLICT`) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| EXT | 1 |  | 9 | 5 |  | 1 | 16 |
| PKG-01 |  |  | 2 |  |  | 1 | 3 |
| PKG-02 |  |  |  |  | 3 | 4 | 7 |
| PKG-03 |  |  | 3 |  |  | 8 | 11 |
| PKG-04 |  |  |  | 1 |  |  | 1 |
| PKG-05 |  | 3 | 1 | 5 | 2 |  | 11 |
| PKG-09 |  | 2 |  | 1 |  | 1 | 4 |
| **Total** | **1** | **5** | **15** | **12** | **5** | **15** | **53** |

ALSO/CONTEXT members by Disposition: Governing texts disagree 12.

<!-- /COUNTS -->
Every row restates K-ENGINE-4 or SPEC §10.3, or a deliverable principle derived from them ("public semantics stay Chirality-owned", "provider names only as metadata"). On the live path those rows meet Codex events kept as received. Many of the "partly built" and "written, not built" rows also carry R4-Q1 (their translation or redaction code is legacy only) or R4-Q2 (conformance). The 12 ALSO rows are decided in P-04; they also cite DIRECTIVE §2.10.

## Options
**A. As received governs.** K-ENGINE-4 and SPEC §10.3 give way to the amended event clauses and D-GOV-43 item 2 on the Codex path. They keep only their core rule: the browser contract and the stored-event contract stay separate, and the terminal events stay Chirality-owned. *R5 would:* rewrite the rows' text to the amended event clauses, recording "difference already permitted" where the only divergence is pass-through. A governed amendment tranche would amend K-ENGINE-4 and SPEC §10.3 (the D-APP-38 corpus-bump procedure). Rows that also carry R4-Q1 or R4-Q2 wait for those packets.
**B. Translate governs.** The code changes to translate Codex events into Chirality-owned types. That needs a separate implementation brief, and it would contradict D-GOV-43 item 2, a Root ruling. All rows wait on it.
**C. Both, split by sink.** Keep events as received in the store and the stream, and translate for named views only. This is a narrower amendment. The deliverable text for the translation views remains open work.
**D. Defer.** The rows stay held.

## HELP_HUMAN recommendation (draft)
Option A:
- The amended clauses and D-GOV-43 item 2 are the newer, specific direction, and the code already follows them.
- Option B would re-create the closed schema that D-GOV-43 retired, which is a Root question outside your App authority.
- A single ruling removes the inconsistent grading across packages.

Option A **leaves open** whether stored events are redacted as K-EVENT-6 requires. That question is P-12, and Option A does not answer it.

## Who decides
You decide, as the owner of the App CONTRACT and SPEC. Option B would conflict with D-GOV-43 item 2, a Root ruling: that part is external authority (Root / HELPS_HUMANS).

## On ruling
- **Where recorded.** The consolidated R4 ruling record (next free D-APP ID, committed by HELP_HUMAN before repair) names the R4-Q5 answer and the key set (`PACKET_INDEX.csv` P-05 PRIMARY).
- **R5.** Tranche managers per package edit the rows' deliverable text. R6 backchecks every listed row.
- **Governance amendment.** A separate governed tranche amends K-ENGINE-4 and SPEC §10.3, with independent review and a corpus version bump.
- **Held and dependent rows.**
  - Rows that also cite R4-Q1 or R4-Q2 stay open on those halves.
  - `DEL-02-02#REM-2` also names D-APP-117, so it stays held until D-APP-117 is ruled.
- No lifecycle transition.

## Risks, contested rows and dependencies
- **Spot-check refutations.** For `DEL-02-05#CLM-011.3` (S2-038) and `#CLM-003.2` (S2-052), the checker reads the rows as "matches" with no owner decision needed. They cite only the amended SPEC §11 and TYPES §7.4, not K-ENGINE-4. The rows `DEL-02-05#CLM-005.5` and `#CLM-010.7` point to CLM-003.2 and share that reading. Under Option A the four rows are simply "matches".
- **Spot-check refutation S1-055.** The checker proposes "governing texts disagree" for `DEL-04-05#CLM-009.14`, which is sealed as "built differently". Under Option A both readings lead to the same text repair.
- `DEL-02-05#CLM-025` (S1-035, undecided): "text out of date" or "nothing to check".
- **Depends on P-04.** The 12 ALSO rows, and any row citing DIRECTIVE §2.10, need P-04 as well.
- **Related packets.** P-12 (redaction) and P-08 (conformance, 8 rows here also cite R4-Q2).
