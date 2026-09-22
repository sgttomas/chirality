# R4 decision book — RUN_D128 deliverable concordance

**Read this first.** It is the owner's decision gate for the RUN_D128 concordance (activated by
D-APP-128). Everything below was prepared by agents: packets propose, and **you rule**. Each
recommendation is a HELP_HUMAN draft, labelled as such. Nothing is repaired, and no lifecycle
changes, until your rulings are recorded.

## 1. Overview

**What the run did.** Agents compared every live App deliverable (54 deliverables, 11 packages)
with the code as it stood at the frozen commit `00115c719` (App 3.0.1), with the governing
documents and with the recorded v3 direction. They also audited five other surfaces: the ruled
D-APP-86..127 decisions, the release and validation docs, the decomposition scope ledger, the
packaged `AGENTS.md`, and the harness developer docs. Every one of the 1,746 deliverable units and
221 extension units has a verdict. Each package was checked by an independent verifier, and then
by a run-wide spot check (315 confirmed, 12 refuted, 11 undecided out of 338 items).

**Census (3,568 verdict rows, after your owner-check answers).**

| Verdict | Rows |
|---|---:|
| Matches, or nothing to check | 1,275 |
| Text out of date (deliverable text says something now false) | 1,089 |
| Partly built, built differently, or written but not built | 762 |
| Governing texts disagree (needs a ruling) | 169 |
| To-do list or register out of step | 116 |
| Already retired or permitted by a ruling | 87 |
| Unknown (22 off-code events nobody can confirm; 1 visual-evidence row) | 23 |
| Other (old verification or assessment, lifecycle, agent-instruction matter, undocumented) | 47 |

967 rows name a decision they wait on. Most of them wait on one of six framed questions, R4-Q1 to
R4-Q6.

**Your owner-check answers are applied.** Your answers (OC-01..OC-20) are testimony about events,
not rulings, and they are now in the concordance. Two rows moved: the arm64 and minimum-OS
inspections happened, but nothing records their results, so both rows are now "partly built".
The other 61 rows gained a note recording your testimony, and 5 statements that an event "did not happen" were corrected to "no record". The 22 rows you could not answer stay Unknown, with your belief
noted. The detail is in `R3/OWNER_CHECK_APPLIED.md` and packet P-02.

**What is being asked.** 25 packets: one per cause cluster, plus an exceptions list. About a third
of them turn on a real governance question. The rest ask you to authorize a class of text repairs
that follow from decisions you have already made, mainly D-GOV-43 (the Codex-hosted App) and its
App application D-APP-127.

**Terms used throughout.**
- *Legacy harness*: the old in-process Claude SDK / Pi engine code that is still in the repository
  but that the shipped App no longer runs.
- *Live Codex path*: the code the shipped App actually runs.
- *R5*: the repair stage that follows your ruling. It edits deliverable text only. Code changes
  always go through a separate, bounded implementation brief.
- *Codes in packets*: clause IDs such as K-PERM-6 (CONTRACT) and §2.8 (DIRECTIVE) are sections of the App governing documents. D-APP-nn and D-GOV-nn are App and Root decisions. R4-Q1..Q6 are the six framed questions. XPF-nnn is an R3 cross-package finding, and S1-/S2-/S3-nnn is a spot-check item. Rules marked MR-n or "rule 2b" are run rules from `CONVENTIONS.md`, and each packet explains the one it uses.
- *PRIMARY rows*: the rows a packet decides. A row can touch several packets, but it is decided in
  exactly one.

**Worth knowing before you read.**
- Several code options change **Runtime** code (`projects/chirality-runtime`). This App run cannot
  edit Runtime code, so those implementation briefs go to the Runtime project loop (P-08, P-12,
  P-13, P-15, P-16 and P-20).
- R4-Q6 reach (P-04) matters: 82 rows are in scope under the narrow reading and 146 under the
  broad one.
- R3 counted 428 rows with both live and legacy evidence. The final count is 410; P-09 holds 333
  of them.
- Amending Root documents, D-GOV rules, agent role files or workflows is outside your App
  authority in this run. Those items are routed to Root or HELPS_HUMANS.
- Your rulings go into one consolidated ruling record, the next free D-APP ID (currently D-APP-130).
  HELP_HUMAN commits it before any repair. Rows tied to D-APP-116..119 stay on hold until those are
  ruled.

## 2. The packets

Ordered by cause group, then by the authority the question turns on (GOVERNING before mixed before CONTEXT). "Rows" = rows decided in the packet (+ rows that touch it but are decided elsewhere). Recommendations are HELP_HUMAN drafts, not rulings.

### Owner-reserved and owner-check items

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-01](PACKETS/P-01_deferred-del-06-02-keys.md) — Two DEL-06-02 rows where the two workers disagreed | For DEL-06-02#CLM-005 and #CLM-032, which of the two workers' verdicts stands, or a third reading? | 2 (+0) | GOVERNING | C — both "built differently", follow P-09 | P-09 |
| [P-03](PACKETS/P-03_release-signing-and-g6a.md) — Release signing posture and the exact-candidate gate | Did the amended CONTRACT preamble, SPEC §19.4 and PRD §12.8 replace the "unsigned" release target, the F-APP-2 signing fence and the G6a gate? | 22 (+5) | GOVERNING | C with b2 — amend K-RELEASE-1, PRD §6.2; G6a met by OC-01 | none |
| [P-02](PACKETS/P-02_owner-check-what-remains.md) — What is still unknown after your owner check | How should R5 treat rows your testimony confirmed, and the 22 rows still unknown? | 63 (+0) | mixed | a: look in Root records; b, c: repair text | P-03, P-24 |

### Named governance questions (R4-Q1..Q6)

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-04](PACKETS/P-04_directive-superseded-by-dgov43.md) — Old App DIRECTIVE permission and provider clauses versus D-GOV-43 | Do you confirm your recorded answer that D-GOV-43 superseded the unamended App DIRECTIVE §2.8, §2.10, §4.1, §4.2 and CONTRACT K-PERM-1/K-PERM-6, and if so, for which rows and in which repair direction? | 86 (+0) | GOVERNING | A — confirm; narrow reach; text follows code | none |
| [P-05](PACKETS/P-05_codex-events-as-received.md) — Codex event payloads stored as received or translated | Now that D-GOV-43 and the amended event clauses say Codex events are kept as received, do the unamended translate-everything clauses (K-ENGINE-4, SPEC §10.3) still bind the live Codex path? | 53 (+12) | GOVERNING | A — as received; amend K-ENGINE-4, SPEC §10.3 | P-04 |
| [P-06](PACKETS/P-06_four-role-adoption.md) — Does the App adopt the 2026-09-09 four-role model? | Should the App loop adopt the 2026-09-09 four-role model that the code already ships, by amending its own governing texts, or do the unamended App texts still bind? | 102 (+0) | GOVERNING | A — adopt for the App; amend texts | P-09, P-22, P-23 |
| [P-07](PACKETS/P-07_status-tool-actor-check.md) — Who is the actor on status transitions | Is a caller-supplied actor string enough to authorize human-gated lifecycle transitions, or must the human gate be carried by something the agent cannot assert? | 13 (+0) | GOVERNING | B: text states the limit; P-14 decides mechanism | P-09, P-14 |
| [P-08](PACKETS/P-08_codex-engine-conformance-obligation.md) — Codex engine never run through conformance suite | The shipped Codex engine was never run through the K-ENGINE-2 engine conformance suite; must it be, or does the D-GOV-43 acceptance set replace that obligation for the Codex path? | 24 (+8) | GOVERNING | A — run suite against Codex adapter | P-05 |
| [P-09](PACKETS/P-09_legacy-harness-history-or-obligation.md) — Retained legacy harness: history, compatibility or obligation | For claims that only the retained legacy harness meets, are they history, a documented compatibility surface, or obligations the live Codex path must meet? | 630 (+97) | GOVERNING | D — a: compatibility (B); b: re-express guarantees; c: per part | P-04, P-13, P-14, P-10 |

### Rows held on existing or unframed decisions

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-10](PACKETS/P-10_rows-held-on-decisions.md) — Rows waiting on existing or pending decisions | For rows that name an existing decision, do you agree that rows on unruled D-APP-116..119 stay held, and that rows on already-ruled decisions are repaired to what those decisions settle? | 18 (+23) | GOVERNING | A — hold a; repair b and c | none |
| [P-11](PACKETS/P-11_unframed-owner-questions.md) — Five smaller owner questions no named question covers | For each of five themes, which governing text or later direction stands, and so which side changes? | 26 (+22) | GOVERNING | a amend SPEC; b-c amend text; d-e case by case | P-04, P-09, P-21, P-23 |

### Live Codex path findings

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-12](PACKETS/P-12_live-event-store-redaction.md) — Live event store keeps Codex payloads without redaction | The live Runtime stores and streams Codex notification payloads without the structural secret redaction that amended K-EVENT-6 requires; should the code be fixed, the requirement narrowed, or the gap recorded and deferred? | 25 (+32) | GOVERNING | A — fix code in Runtime; text names owner | P-05 |
| [P-13](PACKETS/P-13_live-protected-paths-hooks.md) — Protected paths, instruction root and hooks on Codex | On the live Codex path, which surface carries the protected-path, instruction-root and hook guarantees: the Codex sandbox (documented), new code, or none (retired)? | 25 (+51) | GOVERNING | B: document sandbox; keep domain rows accepted | P-09, P-04 |
| [P-14](PACKETS/P-14_live-human-gate-transitions.md) — Human gate on the live status-transition route | On the live path, is the human gate for lifecycle transitions documented as a procedural limit, or built so an agent cannot perform it? | 13 (+44) | GOVERNING | D — text now; mechanism C when a transition UI returns | P-07, P-09, P-06 |
| [P-15](PACKETS/P-15_live-scaffold-returns-501.md) — Execution-root scaffolding returns 501 on the live path | Should the live App scaffold execution roots from a decomposition again, or is scaffolding no longer an App operation? | 28 (+8) | GOVERNING | A: compose the scaffold port; fix text | P-04, P-13, P-09 |
| [P-16](PACKETS/P-16_legacy-session-migration-inert.md) — Old chat history not picked up for new projects | The Runtime can read old project-local chat sessions, but projects the App sets up never declare where those are, so the reader never runs; should the deliverable text say so, or should the code declare the old location? | 8 (+6) | GOVERNING | A — correct the text; code stands | none |

### Repair classes by cause (no new direction expected)

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-17](PACKETS/P-17_carrier-propagation.md) — Carry D-APP-127 and D-GOV-43 into deliverable text | Does the owner authorize R5 to bring the carriers' ScopeOfWork, _CONTEXT, _REFERENCES, Dependencies and _STATUS text to the state D-APP-127 and D-GOV-43 already ruled, and route the one unseated SOW-079 row to scope-change? | 118 (+43) | GOVERNING | A — authorize the text-repair class | P-18 |
| [P-18](PACKETS/P-18_document-hygiene.md) — Fix stale reference hashes, registers and metadata | Does the owner authorize R5 to repair the 513 register, reference-hash and metadata rows, including a D-APP-38 corpus version bump, and does the rule 2b reading behind 9 tie-break moves stand? | 513 (+29) | GOVERNING | A — authorize the hygiene class, bump corpus | none |
| [P-20](PACKETS/P-20_codex-sole-engine.md) — Codex as the only engine, and Codex-held credentials | For rows where the deliverable text still assumes the Claude SDK, the Anthropic key or Pi, while D-GOV-43 and D-APP-127 made Codex the only engine and credential custodian, does the text follow the ruled Codex design, with any still-missing parts recorded as open work? | 117 (+517) | GOVERNING | A — text follows ruled Codex design | P-04, P-05, P-09 |
| [P-21](PACKETS/P-21_a2-topology-runtime-extraction.md) — App-owned Runtime service, Runtime extraction, contracts facade | For rows still describing the per-user daemon, LaunchAgent, in-App runtime code or the harness-contract package where D-GOV-43 topology A2 and the Runtime extraction now apply, does the text follow the ruled design, with any still-missing parts recorded as open work? | 139 (+172) | GOVERNING | B — A, but hold 3 rows for P-12 and P-04 | P-04, P-09, P-12 |
| [P-22](PACKETS/P-22_shell-redesign-roles.md) — Woven dialogue shell redesign, text catch-up | For shell-redesign rows under SCA-APP-010, D-APP-74 and D-APP-108 (and four role-adoption rows), does the text follow the woven dialogue shell as built, with still-missing parts recorded as open work? | 75 (+73) | GOVERNING | A — text follows the built shell | P-06 |
| [P-19](PACKETS/P-19_pre-v3-drift.md) — Differences that predate v3 | For divergences already present before 2026-08-22, does the text follow the code (text-shaped rows), and are the unbuilt or partly built parts recorded as open work rather than built now? | 260 (+118) | mixed | A — text follows code; gaps recorded as open | P-18 |

### Lifecycle, done-declaration and exceptions

| Packet | Question | Rows | Authority | Recommended (draft) | Depends on |
|---|---|---:|---|---|---|
| [P-23](PACKETS/P-23_open-gates-release-scope.md) — Open human gates and v3 release-scope wording | For rows describing open gates or v3 scope limits, which should R5 restate, leave open, or route elsewhere? | 38 (+72) | mixed | a fix text; b none; c keep open; d after Q-11 | P-03, P-24, P-10 |
| [P-EX](PACKETS/P-EX_exceptions.md) — Three rows that fit no other packet | For each of three unrelated rows, what should R5 do? | 3 (+0) | mixed | EX-1 record; EX-2 route; EX-3 fix text | none |
| [P-24](PACKETS/P-24_done-declaration-questions.md) — The thirteen questions about what "done" meant for v3 | How do you want to address Q-01..Q-13 of the v3 done-declaration candidate? | 0 (+34) | CONTEXT | D — fold six into packets; rest when ready | P-02, P-03, P-04, P-23 |

## 3. Suggested ruling order

The packets that unblock others come first. You can rule everything in one pass. This order just
means each answer is already in hand when a later packet depends on it.

1. **P-04: R4-Q6, did D-GOV-43 supersede the unamended DIRECTIVE and K-PERM clauses?** You have
   already answered this in session, so here you confirm the answer, its reach and the repair
   direction. It feeds P-05, P-09, P-11, P-13, P-15, P-20 and P-21. It is placed ahead of R4-Q1
   because the P-09 draft depends on it (the "Full access" and DIRECTIVE §2.8 rows).
2. **P-10** (rows held on existing decisions). It depends on nothing, and P-09 relies on its hold list.
3. **P-09: R4-Q1, the legacy harness: history, compatibility or obligation?** Rule it together
   with **P-13** (protected paths and hooks), **P-14** (human gate) and **P-07** (status-tool actor
   check). Their drafts depend on one another. The group feeds P-01, P-06, P-11, P-15, P-20 and
   P-21. It is also the largest packet: 630 rows.
4. **P-06: R4-Q4, the four-role adoption.** Rule it together with **P-22** (shell redesign and
   roles). P-14's link to P-06 and P-06's link to P-23 are soft: they affect wording, not direction.
5. **P-05: R4-Q5, Codex events stored as received or translated?** Then **P-12** (event
   redaction) and **P-08** (conformance suite), which both depend on it.
6. **P-03** (release signing and G6a). It depends on no other packet.
7. **P-02, P-23 and P-24.** These cover the owner check, open gates and the done-declaration
   questions, which are CONTEXT. They depend on P-03 and P-10.
8. **Repair classes that need no new direction:** P-16, P-17, P-18, P-19, P-20 and P-21, then
   P-11, P-15, P-01 and P-EX. Most ask you to authorize text repair that follows decisions already
   made. Rule P-18 before P-17 and P-19, because the corpus bump comes first.

Cycles to note, each resolved by ruling the group in one sitting: P-07 and P-14 (mechanism), P-09 with P-13 and P-14, P-06 and P-22, and P-02, P-23 and P-24.

## 4. Ruling form

Answer in shorthand, one line per packet: an option letter (for example `A`), `A with <change>`, `REC` (adopt the draft recommendation), `DEFER`, or `ASK` (send back with a question). Sub-questions take one answer each (`P-09.a A; P-09.b B`).

```text
P-01  Two DEL-06-02 rows where the two workers disagre : 
P-02  What is still unknown after your owner check     : 
P-03  Release signing posture and the exact-candidate  : 
P-04  Old App DIRECTIVE permission and provider clause : 
P-05  Codex event payloads stored as received or trans : 
P-06  Does the App adopt the 2026-09-09 four-role mode : 
P-07  Who is the actor on status transitions           : 
P-08  Codex engine never run through conformance suite : 
P-09  Retained legacy harness: history, compatibility  : 
P-10  Rows waiting on existing or pending decisions    : 
P-11  Five smaller owner questions no named question c : 
P-12  Live event store keeps Codex payloads without re : 
P-13  Protected paths, instruction root and hooks on C : 
P-14  Human gate on the live status-transition route   : 
P-15  Execution-root scaffolding returns 501 on the li : 
P-16  Old chat history not picked up for new projects  : 
P-17  Carry D-APP-127 and D-GOV-43 into deliverable te : 
P-18  Fix stale reference hashes, registers and metada : 
P-19  Differences that predate v3                      : 
P-20  Codex as the only engine, and Codex-held credent : 
P-21  App-owned Runtime service, Runtime extraction, c : 
P-22  Woven dialogue shell redesign, text catch-up     : 
P-23  Open human gates and v3 release-scope wording    : 
P-24  The thirteen questions about what "done" meant f : 
P-EX  Three rows that fit no other packet              : 
```

Riders or general directions (optional):

```text

```

