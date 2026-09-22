<!-- PACKET
id: P-12
cluster: CL-12
title: Live event store keeps Codex payloads without redaction
question: The live Runtime stores and streams Codex notification payloads without the structural secret redaction that amended K-EVENT-6 requires; should the code be fixed, the requirement narrowed, or the gap recorded and deferred?
recommended: A — fix code in Runtime; text names owner
depends_on: P-05
decision_type: owner; engineering
tier: GOVERNING
-->
# P-12 — Live event store keeps Codex payloads without redaction

Cluster CL-12 · no named question (a live-path finding; RUN_BASIS Addendum 9 keeps it separate from R4-Q6) · draft by TASK D2 for HELP_HUMAN review; not a ruling.

**Question.** Amended CONTRACT K-EVENT-6 requires secrets to be removed before every sink. The live Runtime writes and streams Codex notification payloads as received, with no such redaction. Which of these do you want?
- Fix the code, so the payloads are redacted.
- Narrow the requirement.
- Record the gap and defer it.

## What we found
- Amended K-EVENT-6 requires structural redaction "before every sink": the coordinator, persistence, the browser stream, status and replay views, logs, App Server diagnostics and support bundles. It says upstream payloads are preserved "after redaction", and lists secrets, tokens, device-login values, cookies and credentials as excluded (`docs/CONTRACT.md:83`). [GOVERNING]
- D-GOV-43 item 2 requires the complete notification stream to reach the renderer, and item 6 says the App never reads or relays credential material. D-GOV-43 does not relax redaction (`D-GOV-43.proposed.md:156-213`). [GOVERNING]
- On the live path, the Runtime's Codex adapter yields `codex.notification` with the raw `params` (`projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts:282,289`). `persistEvent` appends it to `events.jsonl` with no redaction step (`packages/core/src/session-store.ts:813-822`). [code]
- The only redaction in the Runtime packages removes e-mail-like tokens from App Server stderr lines (`packages/daemon/src/codex-app-server-client.ts:44-70`). [code]
- Structural redaction exists only in the legacy harness, which the live Codex path does not reach: `redactJsonLike` in `frontend/src/lib/harness/run-logger.ts:95`, and the legacy event writer. [code]
- Four packages found this independently (PKG-03, 04, 05, 06). No App carrier names who owns redaction in the Runtime (`R3/CROSS_PACKAGE_FINDINGS.csv` XPF-041). [run finding]
- On the live path the App holds no API key; Codex custodies sign-in. So the exposure is secret-like content inside tool output and notification payloads, not a Chirality-held key. Several rows note an alternative "matches" reading on that ground (for example `DEL-02-05#CLM-004.4`). [run finding]

## Affected rows
<!-- COUNTS -->
**25 rows are decided in this packet** (PRIMARY); 32 more rows touch it but are decided in their own packet (ALSO/CONTEXT). Full key list: `R4/PACKET_INDEX.csv`, PacketID `P-12`.

| Package | Written, not built (`DOCUMENTED_UNIMPLEMENTED`) | Partly built (`PARTIALLY_IMPLEMENTED`) | Built differently (`IMPLEMENTED_DIFFERENTLY`) | Text out of date (`STALE_SPECIFICATION`) | To-do list out of step (`REMAINING_STATE_MISMATCH`) | Total |
|---|---:|---:|---:|---:|---:|---:|
| PKG-01 |  | 2 |  |  |  | 2 |
| PKG-02 |  | 3 |  |  |  | 3 |
| PKG-03 |  | 4 |  |  |  | 4 |
| PKG-04 |  | 1 |  |  |  | 1 |
| PKG-05 |  | 6 |  | 5 | 1 | 12 |
| PKG-06 | 2 |  | 1 |  |  | 3 |
| **Total** | **2** | **16** | **1** | **5** | **1** | **25** |

ALSO/CONTEXT members by Disposition: Partly built 13, Text out of date 7, Written, not built 6, Built differently 3, Governing texts disagree 2, Verification out of date 1.

<!-- /COUNTS -->
All 25 PRIMARY rows are redaction, secret-handling or event-store rows that need no ruling on authority: the governing text is amended and clear, and the code does not meet it. Most are PKG-05 (DEL-05-03 is the redaction deliverable). The 32 ALSO rows are decided in their own packets (mostly P-09 and P-05); the answer here gives them their redaction half.

## Options
**A. Fix the code; the text names the Runtime owner.**
- A separate implementation brief adds structural redaction before persistence and streaming on the Runtime path. The Runtime code sits outside this App run's write scope (RUN_BASIS §4), so the brief is issued in the owning Runtime loop; the App side covers App sinks (views, logs, support bundles).
- *R5 would:* correct the text that names legacy modules (DEL-05-03 slots, verification approaches and principles) so it names the live sinks and the Runtime owner. The "partly built" and "written, not built" rows wait on the brief. R6 then backchecks them against the new code.

**B. Narrow the requirement.** Amend K-EVENT-6 so that events kept as received are redacted only for credentials that Chirality holds (none on the Codex path). *R5 would:* rewrite the rows to the narrowed text. This is a governed CONTRACT amendment, and it weakens a security control.

**C. Accept the gap for now.** The ruling permits the difference until a named trigger, such as the next release. *R5 would:* record "difference already permitted" on the rows and add a Remaining item naming the owner.

**D. Defer.** The rows stay as found.

## HELP_HUMAN recommendation (draft)
Option A:
- K-EVENT-6 was amended for D-GOV-43, so it is current direction, not old wording.
- Storing raw tool output can capture secrets that the user's tools print.
- The fix is bounded to one write path and one stream path.

Option A leaves the timing open, and which loop owns the Runtime change: the Runtime loop, or the App through D-APP-127's App-owned Runtime service.

## Who decides
The owner decides the direction. The redaction design is an engineering call under a bounded implementation brief. Runtime package edits belong to the Runtime project loop, outside this run's write authority. Option B is a governed App CONTRACT amendment.

## On ruling
- **Where recorded.** The consolidated R4 ruling record (next free D-APP ID, committed by HELP_HUMAN) names the option and the key set (`PACKET_INDEX.csv` P-12 PRIMARY).
- **Option A.**
  - HELP_HUMAN issues a `software-bounded-implementation` brief. It is routed to the Runtime loop for the Runtime sinks, with an App slice if needed.
  - R5 edits only the carrier text that names the owner and the live sinks.
  - Rows whose verdict depends on the code wait for the brief to land, then R6 backchecks them.
- **Option B.** A governed amendment tranche for K-EVENT-6, then R5 text edits and R6.
- No lifecycle transition.

## Risks, contested rows and dependencies
- `DEL-02-05#CLM-004.4`, `#CLM-010.9`, `#CLM-011.4` and `DEL-03-01#CLM-018.7` are least-confident. They may read as "matches" if K-EVENT-6 is read as covering only credentials that Chirality holds, which is close to Option B.
- `DEL-04-05#CLM-009.14` (ALSO; spot-check item S1-055) is contested between "built differently" and "governing texts disagree" (P-05).
- Depends on P-05: under P-05 Option A, redaction applies to payloads that are kept as received. Under P-05 Option B, the translation step could carry the redaction instead.
- Some rows also carry legacy-module text (R4-Q1, P-09). Retiring that text does not close the live gap.
