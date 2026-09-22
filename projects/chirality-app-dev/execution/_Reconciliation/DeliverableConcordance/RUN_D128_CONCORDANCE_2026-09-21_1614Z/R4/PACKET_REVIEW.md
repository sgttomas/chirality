# R4 packet review — RUN_D128 (TASK RV, independent)

Reviewer: TASK RV (Type 2), dispatched by the R4 WORKING_ITEMS packet manager under
`R4/BRIEFS/RV_PACKET_REVIEW.md`. Blind to drafter notes, scripts and briefs (`R4/_work/D*`,
`R4/BRIEFS/D*.md` not read). Evidence: the frozen tree at `00115c719`, the run folder, the
concordance CSVs read through `R3/_scripts/r3lib.py` `read_csv` (helpers in
`R4/_work/RV_scripts/`). Frozen-tree paths below are repository-relative.

Basis note: the D-APP-128 ruling record is not in the frozen tree (it post-dates `00115c719`); its
"What this authorizes" section was read from the working App loop's `_DECISIONS/` folder.

Status: COMPLETE. 25 packets and the decision book reviewed.

**Result.** 75 statement checks: 73 CONFIRMED, 1 REFUTED (P-20 S3, a count), 1 UNVERIFIABLE (P-04
S3, half of the statement). One further side statement REFUTED (P-11, a count). Findings: 1
BLOCKING (RV-01), 20 MINOR (RV-02..RV-21). No CONTEXT source was found tagged GOVERNING. The owner's
R4-Q6 answer in P-04 matches `OWNER_DIRECTION.md` `r2_r4q6_answer` byte for byte. Every packet's
PRIMARY/ALSO counts and sub-question counts agree with `PACKET_INDEX.csv` and
`PACKET_SUBQUESTIONS.csv`. The book's census and table columns agree with the CSVs and packet
headers.

## Summary table

| Packet | S1 | S2 | S3 | Authority | Consistency |
|---|---|---|---|---|---|
| P-01 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-02 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK (RV-18 decision type) |
| P-03 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-03, RV-04 |
| P-04 | CONFIRMED | CONFIRMED | UNVERIFIABLE (half) | OK | RV-06, RV-15, RV-19 |
| P-05 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-06 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-02 (order), RV-17 |
| P-07 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-08 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-09 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-02 (order), RV-05, RV-07 |
| P-10 | CONFIRMED | CONFIRMED | CONFIRMED | RV-08 | RV-21 |
| P-11 | CONFIRMED | CONFIRMED | CONFIRMED (+1 side REFUTED) | OK | RV-09, RV-10 |
| P-12 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-13 | CONFIRMED | CONFIRMED | CONFIRMED | RV-20 (option A only) | RV-07 |
| P-14 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-02 (order), RV-11 |
| P-15 | CONFIRMED | CONFIRMED | CONFIRMED | **RV-01 BLOCKING** | OK |
| P-16 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-17 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-18 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-19 | CONFIRMED | CONFIRMED | CONFIRMED | RV-12 | OK |
| P-20 | CONFIRMED | CONFIRMED | REFUTED (count) | RV-20 (option B only) | RV-13 |
| P-21 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-14, RV-17 |
| P-22 | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| P-23 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-21 |
| P-24 | CONFIRMED | CONFIRMED | CONFIRMED | OK | RV-16 |
| P-EX | CONFIRMED | CONFIRMED | CONFIRMED | OK | OK |
| Book | census CONFIRMED | table = headers | order | n/a | RV-02, RV-15 |

## Findings

**RV-01 — BLOCKING — P-15, "Who decides" (line 76) and "On ruling" step 3 (line 81).** The
recommended option A composes a scaffold port "in the App-owned Runtime". The code that must change
is Runtime code: `RuntimeService.scaffold` and its optional `scaffoldPort`
(`projects/chirality-runtime/packages/core/src/runtime-service.ts:118,619-624`) and the App-owned
composition that passes `undefined` (`projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:226`).
The packet says "None of this is outside the App's authority" and routes the brief without naming
the Runtime loop. The run's rule is that Runtime code goes to the Runtime loop (P-08, P-12 and P-16
route it that way). *Fix:* state that the option-A brief is issued in the Runtime project loop (with
an App slice only if the App route or tests change), and strike "None of this is outside the App's
authority" or limit it to the text and scope-change parts.

**RV-02 — MINOR — Decision book §3 (lines 118-139).** The suggested order conflicts with three
packets' `depends_on`: P-09 (step 2) depends on P-10 (step 5); P-14 (step 2) depends on P-06 (step
3); P-06 (step 3) depends on P-23 (step 6). The "Cycles to note" paragraph also omits P-02↔P-24 and
P-23↔P-24 (step 6) and P-06↔P-22 (step 3). *Fix:* move P-10 ahead of the P-09 group (it depends on
nothing), note that P-14's P-06 dependency and P-06's P-23 dependency are soft or reorder, and list
the other cycles.

**RV-03 — MINOR — P-03 header `recommended` (line 6).** The header reads "C — record retrospectively;
amend K-RELEASE-1, PRD §6.2", but the body recommends "C with b2". The book table repeats the header,
so an owner answering `REC` from the table has no G6a answer. *Fix:* header "C with b2 — ...".

**RV-04 — MINOR — P-03 "Affected rows" note (line 54).** "`DEL-09-05#CLM-016.3` and `#CLM-016.6`
(G6a) are decided here but sit PRIMARY in P-02" contradicts the book's rule that a row is decided in
exactly one packet (its PRIMARY one). P-02 line 97 says their repair "follows P-03". *Fix:* say they
are decided in P-02 and their repair follows the P-03.b answer.

**RV-05 — MINOR — P-09 header `recommended` (line 6).** It gives the split ("a: compatibility; b:
re-express guarantees; c: per part") without naming option D, which is the body's recommendation.
*Fix:* "D — a: compatibility (B); b: re-express guarantees; c: per part".

**RV-06 — MINOR — P-04 table and Risks (lines 62-66, 90).** "The 4 Full-access rows" are three
Full-access rows (`DEL-07-01#CLM-011.4`, `#CLM-011.6`, `DEL-06-05#CLM-024`) plus one DIRECTIVE §2.8
row (`DEL-04-05#CLM-024`), as P-09 line 108 states. The broad-reading row also says "Of the 59
adjacent rows ... 3 are Full-access rows; 56 are PRIMARY in P-09 and 3 in P-20", which reads as 62.
*Fix:* "4 rows (3 Full access, 1 DIRECTIVE §2.8)"; state the 59 as 56 in P-09 + 3 in P-20, of which 3
are Full-access rows.

**RV-07 — MINOR — P-09 line 27 and P-13 line 35.** The cited evidence that "the live Runtime starts
Codex threads with no Chirality tool servers" is `runtime-service.ts:580` `mcpServers: []`, which is
a field of the `runtimeFingerprint` record (lines 559-581), not the thread-start configuration. The
conclusion holds on other evidence: the Codex adapter starts the turn with an empty tool list
(`delegated-engine-adapter.ts:231`) and has no MCP wiring. *Fix:* cite the adapter line (as P-01
does), or describe line 580 as the fingerprint.

**RV-08 — MINOR — P-10 option B (lines 65-68).** "Rule D-APP-116..119 now, in this R4 record" folds
four pending decisions into the R4 record, although D-APP-128 §5.5.4 holds their rows from R5 and
each has its own packet and gate. The packet flags the widening, but the mechanism would bypass the
decisions' own records. *Fix:* reword B so that any such ruling is recorded on each decision's own
packet and register row, and the P-10.a rows are released only when those rows read RULED.

**RV-09 — MINOR — P-11 line 74.** "The 23 marked 'Text out of date' are in P-20 (7) and P-09 (5)" is
wrong (and sums to 12). The 34 rows carrying the R3 call (d) "cluster ED" note split as 11
AUTHORITY_CONFLICT in P-04, 18 STALE_SPECIFICATION in P-20 and 5 in P-09, as P-04 line 68 states.
*Fix:* "P-20 (18) and P-09 (5)".

**RV-10 — MINOR — P-11 line 72.** "Three rows the brief asked about" exposes the drafter's brief to
the owner, who has not seen it. *Fix:* "Three rows you might expect here".

**RV-11 — MINOR — P-14 header and recommendation (lines 6, 54).** "A: fix text now; C deferred" /
"Option A now, with C recorded as the direction if a transition UI returns" is what option D ("Defer
the mechanism. Repair the text now and reopen when a transition UI returns") describes. *Fix:*
recommend "D (text now; mechanism C when a transition UI returns)", or merge A and D.

**RV-12 — MINOR — P-19 option A for P-19.b (line 59) and "On ruling" step 2.** "R5 rewrites each row
to state what is built, and records the unbuilt part as a Remaining item ..., so the deliverable no
longer claims it" can be read as narrowing ScopeOfWork requirements, which is a scope change. The
method (R5) updates Remaining only through its owning contract. *Fix:* say the requirement text stays
and only false "built" or "done" assertions are corrected; the Remaining item is added under the
`_STATUS` contract; any narrowing of a requirement goes to WORKING_ITEMS (scope-change).

**RV-13 — MINOR — P-20 line 24.** "36 PRIMARY rows carry both LIVE and LEGACY_ONLY evidence" is
refuted: 40 rows do (32 in P-20.a, 8 in P-20.b). None of them cites R4-Q1, so the conclusion stands.
The 36 appears to be copied from P-21, where it is correct. *Fix:* "40".

**RV-14 — MINOR — P-21 header `recommended` (line 6) and book table.** The header and the book say
"A — text follows A2 and extraction", but the body recommends option B (A plus holds on
`DEL-03-04#CLM-009.10`, `DEL-05-03#CLM-010.5`, `SOW:SOW-064.2`). An owner answering `A` or `REC` from
the table would release three rows the body means to hold. *Fix:* header "B — A, holding 3 rows for
P-12/P-04".

**RV-15 — MINOR — P-04 line 32 and decision book lines 27, 37.** (i) P-04: "the Anthropic key UI is
not on the live path. See spot-check items S2-013 and S2-043": those items concern Full access only.
`ApiKeySettings` is still mounted in `components/shell/shell-frame.tsx:302` and in the non-hosted
branch of `settings-view.tsx:35`; whether either is reached in the hosted App was not established
here (UNVERIFIABLE). *Fix:* cite the evidence for the key-UI half or drop it. (ii) Book: the census
labels all 23 UNKNOWN rows "an off-code event nobody can confirm", but one (`DEL-02-04#CLM-010.14`,
P-23.c) is a sealed UNKNOWN about visual-evidence recency, not an owner-check event (the other 22 are
P-02's). "61 rows had their notes corrected": 63 rows gained testimony notes; only 4 Notes and 1
VerificationEvidence values were corrections of absence wording (`REMAP_LOG.csv` Source
`OWNER_CHECK`: 71 Notes, 2 Disposition, 1 VerificationEvidence, 1 RemainingWork lines). *Fix:*
"Unknown (22 off-code events; 1 visual-evidence row)"; "the other 61 rows gained a testimony note (5
absence statements corrected)".

**RV-16 — MINOR — P-24 lines 18, 20.** "Rows name them only in their notes" and "34 CONTEXT members,
all in PKG-09" understate reach: 40 rows name Q-01..Q-13 in Notes (all PKG-09) and 60 in Notes or
DirectionEvidence. P-24 itself counts Q-07 on 24 rows (mostly DEL-07-01, via DirectionEvidence),
none of which is a CONTEXT member. *Fix:* state the membership rule and the wider count, or add the
DirectionEvidence rows as CONTEXT members.

**RV-17 — MINOR — plain language (several packets).** Undefined codes the owner must decode: "Δ10"
(P-06 line 54), "MR-6" (P-21 line 79), "the undecided ED split in call d" (P-04 line 68), "rule 2b"
(P-18, P-19; defined only by reference), "REF-006" (P-14 line 24, P-23 line 25), and bare XPF-/S1-/S2-
item IDs without a gloss. *Fix:* a one-clause gloss at first use, or a short glossary in the book's
"Terms used throughout".

**RV-18 — MINOR — decision_type vocabulary (P-02, P-03, P-07, P-09, P-11, P-13).** Method R4 names
owner, engineering, WORKING_ITEMS (review), WORKING_ITEMS (scope-change), HELPS_HUMANS and external
authority. Headers also use "HELP_HUMAN (run basis)" (P-02) and "governance amendment (App)" /
"owner (App governance amendment)" (P-03, P-07, P-09, P-11, P-13). These are owner decisions executed
by a governed tranche. *Fix:* use "owner" and name the governed amendment tranche in "On ruling";
record the P-02.a root widening as an owner decision executed by HELP_HUMAN.

**RV-19 — MINOR — P-04 sub-question labels (lines 19-22 vs line 21, CSV).** The packet frames
P-04.1..P-04.4 (answer, reach, rows, direction) while `PACKET_SUBQUESTIONS.csv` and the counts use
P-04.a/b (row sets). The book's ruling form asks for `P-xx.a` answers. *Fix:* rename the confirmation
items (e.g. P-04.i..iv) or state that a/b are row sets answered under P-04.2.

**RV-20 — MINOR — P-13 option A (lines 61-65) and P-20 option B (line 62).** Neither non-recommended
code option says where the brief runs. P-13 A's "Runtime-side check on Codex file-change approvals"
is Runtime code; P-20 B's failure taxonomy and timeout distinction sit on the live Runtime path.
*Fix:* route each to the Runtime loop, as P-08, P-12 and P-16 do.

**RV-21 — MINOR — P-10 held-row list (line 85) vs P-23 (lines 34, 84, 97).** P-23 holds
`DEC:D-APP-101` from R5 until D-APP-118 is ruled (D-APP-128 §5.5.4), but P-10's consolidated list of
rows held on D-APP-116..119 (8 + 10 keys) omits it, because its HumanDecisionNeeded is `NO`. The
ruling record would then list holds in two places. *Fix:* add `DEC:D-APP-101` to P-10's held list
(or note it there as held via P-23).

## Decision book checks

- Census: 3,217 + 351 = 3,568 rows; the eight verdict groups (1,275 / 1,089 / 762 / 169 / 116 / 87 /
  23 / 47) and "967 rows name a decision" reproduce exactly from the two concordance CSVs. Spot-check
  totals (315/12/11 of 338) and unit counts (1,746 + 221) match `R3/R3_SPOT_CHECK.md` and
  `R3/R3_SUMMARY.md`. Label issues: RV-15.
- Table: every packet's title, question, tier, recommendation and depends-on in the book equals its
  header (scripted). Header/body mismatches carried into the table: RV-03, RV-05, RV-14.
- Ruling order: RV-02.

## Per-packet notes

- P-01: S1 tool-pool keeps request order, no sort (`frontend/src/lib/harness/tool-pool.ts:36-111`)
  CONFIRMED [code]; S2 Codex adapter starts turn with empty tool list
  (`chirality-runtime/packages/core/src/delegated-engine-adapter.ts:231`) CONFIRMED [code]; S3 both
  rows carry R4-Q1, worker B CLM-032 reading preserved in AltReading CONFIRMED [run finding]
  (D-APP-56 P27 domain ownership also CONFIRMED, RULED). Authority OK. Consistency OK.
- P-02: S1 2 Disposition moves UNKNOWN→PARTIALLY_IMPLEMENTED on DEL-09-04#CLM-011.4/.5 via
  OWNER_CHECK CONFIRMED (REMAP_LOG); S2 hosted release job fails at first step before build
  (`.github/workflows/desktop-release-template.yml:39-43`) CONFIRMED; S3 22 UNKNOWN rows in P-02 (16
  a / 6 b) CONFIRMED. Authority OK. Consistency OK.
- P-03: S1 CONTRACT:17 preamble "K-RELEASE-1 ... read with D-GOV-43 items 1 and 4" CONFIRMED; S2
  K-RELEASE-1 row unchanged (CONTRACT:138) and PRD §6.2 unsigned (PRD:339-346) CONFIRMED; S3 D-APP-97
  ruling line 20 keeps F-APP-2 fence CONFIRMED (also decomp v3_2:382 G6a, pack-electron.mjs:86-95).
  Authority OK. Consistency: header omits b2 (RV-03); "decided here but sit PRIMARY in P-02" (RV-04).
- P-04: S1 DIRECTIVE §2.8/§2.10/§4.1/§4.2 at :115/:144/:227/:250, K-PERM-1/6 at CONTRACT:90/:95
  unamended CONFIRMED; S2 D-GOV-43 item 3 "no effective-configuration veto", item 4 "Full access is
  available by explicit user choice" (proposed.md:186,192) CONFIRMED; S3 "composer offers Full
  access; Anthropic key UI not on the live path" — Full access CONFIRMED (`chat-panel.tsx:133`), key-UI
  half UNVERIFIABLE (cited S2-013/S2-043 cover Full access only; `ApiKeySettings` still mounted in
  `shell-frame.tsx:302`). Owner quote verbatim vs OWNER_DIRECTION CONFIRMED. Authority OK.
  Consistency: 4 "Full access" rows are 3 + 1 DIRECTIVE §2.8 row (RV-06); ED split 18/5 CONFIRMED.
- P-05: S1 K-EVENT-1/6 (CONTRACT:78/:83) "Under D-GOV-43" preserved names CONFIRMED; S2 K-ENGINE-4
  (:64) and SPEC §10.3 (:673-680) "MUST translate" unamended CONFIRMED; S3 adapter yields
  `codex.notification` with method/params (`delegated-engine-adapter.ts:282,289`) and store appends
  (`session-store.ts:813-822`) CONFIRMED. Authority OK (B correctly flagged as Root-conflicting).
  Consistency OK.
- P-06: S1 `9b005c23a` touched no `projects/chirality-app-dev/docs/` file CONFIRMED (git show
  --stat); S2 `DEFAULT_PERSONA='HELP_HUMAN'`, aliases HELP/AGENTS only (persona-resolution.ts:3-9),
  legacy `WORKING_ITEMS` (session-manager.ts:9) CONFIRMED; S3 SPEC §13.1 "hardcoded WORKING_ITEMS
  default" (SPEC:778) and Root role files open with `## PROTOCOL` CONFIRMED. Authority OK (role files
  routed to Root). Consistency OK; ordering finding RV-02.
- P-07: S1 K-GATE-1/K-STATUS-2 (CONTRACT:44,109) CONFIRMED; S2 D-APP-13 ruling :24-26 "required and
  sufficient" CONFIRMED; S3 actor is caller string in legacy tool (read-tools.ts:1125-1136) and live
  route (route.ts:52-62) CONFIRMED. D-APP-56 P19 quote CONFIRMED (ruling :60). Authority OK.
  Consistency OK.
- P-08: S1 K-ENGINE-2 (CONTRACT:62) unamended CONFIRMED; S2 preamble "historical qualification does
  not establish Codex qualification" CONFIRMED; S3 suite callers are `stub` and Claude SDK fixtures
  only (engine-conformance.test.ts:208,270), no Runtime test imports the suite CONFIRMED. Authority OK
  (Runtime test brief routed to Runtime loop). Consistency OK.
- P-09: S1 CONTRACT K-ROOT-2/K-HOOK-1/K-PATH-2 and hooks row (:52,:99,:100,:173), SPEC §15.2 (:847)
  CONFIRMED; S2 285 legacy-only / 333 both / 12 neither PRIMARY rows, 410 run-wide, 9 rows on
  D-APP-116..119 CONFIRMED (script); S3 "live Runtime starts Codex threads with no Chirality tool
  servers (`runtime-service.ts:580`)" CONFIRMED in substance, citation weak (RV-07). Authority OK.
  Consistency: header `recommended` gives the D split without naming option D (RV-05 class).
- P-10: S1 D-APP-116..119 AWAITING_RULING (register :132-137) CONFIRMED; S2 D-APP-121 RULED with gates
  pending, `inlinePdfPreview: false` (preload.ts:77) CONFIRMED; S3 ten other held rows (9 in P-09, 1
  `DEL-02-02#REM-2` in P-05) CONFIRMED. Authority: option B (RV-08). Consistency OK.
- P-11: S1 SPEC §17.6 (:1026-1032) and PRD FR-008 (:603) forbid resume CONFIRMED; S2 `0ed1a1a7f`
  2026-09-11 "Repair trial plans, history, ..." CONFIRMED; S3 decomp v3_2:336 "App-client
  compatibility for daemon-centralized sessions" CONFIRMED. Side statement "23 ... in P-20 (7) and P-09
  (5)" REFUTED (RV-09). Authority OK. Consistency: RV-09; drafter-brief wording (RV-10).
- P-12: S1 K-EVENT-6 (CONTRACT:83) "before every sink ... preserved after redaction" CONFIRMED; S2 raw
  params persisted with no redaction step (adapter :282,289; session-store :813-822) CONFIRMED; S3
  only Runtime redaction is `redactAccountText` e-mail scrub of stderr (codex-app-server-client.ts)
  CONFIRMED (other hits are type fields). Authority OK (Runtime loop). Consistency OK.
- P-13: S1 workspace-write → `writableRoots: [cwd]` (codex-supervisor.ts:107), bypass →
  danger-full-access (delegated.ts:318-330) CONFIRMED; S2 K-DOMAIN-2 "Specializes framework ...
  MUST NOT weaken" (CONTRACT:150), only domain clauses specialize Root CONFIRMED; S3 25 PRIMARY rows
  all HDN NO, PKG-10 14 / PKG-07 10 / PKG-06 1, 9 ACCEPTED_DIVERGENCE CONFIRMED. Authority OK.
  Consistency OK.
- P-14: S1 route takes actor/approvalSha from body (route.ts:52-62) CONFIRMED; S2 only non-legacy UI
  callers are workbench/pipeline surfaces via `deliverable-api.ts:226` CONFIRMED; S3 every route
  renders the woven shell, `void legacy` (woven-dialogue-route.tsx:18) CONFIRMED. Authority OK.
  Consistency: RV-11.
- P-15: S1 `scaffold` throws ENGINE_UNAVAILABLE 501 without a port (runtime-service.ts:118,619-624)
  and composition passes `undefined` (app-owned-composition.ts:226) CONFIRMED; S2 credential
  `set: offline` (:225) CONFIRMED; S3 `39c0bb6ab` is the D-GOV-43 A2 App-owned service commit
  CONFIRMED (nit: the live `/api/harness/scaffold` route still imports `CoordinationMode` from
  `lib/harness/scaffold.ts`, so "only tests use it" is loose). Authority: RV-01 (BLOCKING).
  Consistency OK.
- P-16: S1 `bootstrapProject` manifest has no `legacySessionRoots` (bootstrap-project.ts:43-53)
  CONFIRMED; S2 store iterates `project.legacySessionRoots` only (session-store.ts:112,170) CONFIRMED;
  S3 D-GOV-43 item 5 "No history-import feature is a release prerequisite" (proposed.md:196-207)
  CONFIRMED. Authority OK (B routed to Runtime loop). Consistency OK.
- P-17: S1 D-APP-127 "Consequential applications" list (ruling record §, line 178ff) CONFIRMED; S2
  application map 270 rows, `_STATUS.md` YES in 11 only, SoW/_CONTEXT/_REFERENCES NO in 54,
  Dependencies.csv NO in 52 CONFIRMED; S3 118/118 PRIMARY HDN NO CONFIRMED (also
  runtime-service-host.ts and codex-login.ts exist). Authority OK. Consistency OK.
- P-18: S1 AUTHORITY_CORPUS.json `current_version: v23`, last written by `23b3879b3` (2026-09-12)
  CONFIRMED; S2 later unbumped edits `9eaddb596`, `95b342519`, `7f1e9f387` to PRD/SPEC/CONTRACT
  CONFIRMED; S3 kit deleted in `8cb9cdaf0` CONFIRMED. Authority OK. Consistency OK.
- P-19: S1 94 PRIMARY rows LatestDecision NONE_FOUND CONFIRMED ("most of the rest cite D-APP-56" is
  loose: 54 of 166); S2 App-local `harness-premerge.yml` Node 20 + ANTHROPIC_API_KEY, unchanged since
  `7bee9ae41`, vs `node >=22.19.0` (package.json:96) CONFIRMED; S3 `bb8ae7424` 2026-07-13 CONFIRMED.
  Authority: RV-12. Consistency OK.
- P-20: S1 CONTRACT:17 preamble (Codex sign-in, App-owned Runtime service) CONFIRMED; S2 D-APP-127
  supersedes D-APP-126 and D-APP-125 item 3 (register row) CONFIRMED; S3 "36 PRIMARY rows carry both
  LIVE and LEGACY_ONLY evidence ... none cites R4-Q1" REFUTED on the count (40: 32 in a, 8 in b; the
  "none cites R4-Q1" part holds) (RV-13). Authority: RV-20. Consistency OK.
- P-21: S1 `@chirality/runtime-contracts` `file:../../chirality-runtime/packages/contracts`
  (frontend/package.json:51) CONFIRMED; S2 harness-contract facade `deprecated` message CONFIRMED;
  S3 20 RETIRED_BY_RULING rows = 15 DEL-09-07 + DEC:D-APP-88/100/104/107 CONFIRMED (the 20th,
  `DOC:RELIANCE#11.5` under D-GOV-43, is unmentioned); 36 both-tag rows CONFIRMED. Authority OK.
  Consistency: header recommends A, body recommends B (RV-14).
- P-22: S1 D-APP-108 Q3 "Retired routes stay reachable by URL and unlisted; no 404" CONFIRMED; S2
  `app/not-found.tsx` renders `AppShell` CONFIRMED; S3 22 retired rows all DEL-02-02, 15 permitted
  rows 8/6/1 CONFIRMED. Authority OK. Consistency OK.
- P-23: S1 all 38 PRIMARY HDN NO, CauseTag LIFECYCLE_GATE_PENDING 29 / V3_RELEASE_SCOPE 9 CONFIRMED;
  S2 native descent role text at `delegated-runtime.ts:321` CONFIRMED; S3 `inlinePdfPreview: false`
  (preload.ts:77) CONFIRMED. Authority OK. Consistency: RV-21.
- P-24: S1 34 CONTEXT members, all PKG-09 CONFIRMED; S2 Q-02 named on 26 rows, 13 PRIMARY in P-03
  CONFIRMED; S3 Q-07 named on 24 rows, 21 of them PRIMARY in P-09 CONFIRMED. Authority OK.
  Consistency: RV-16.
- P-EX: S1 D-APP-99 ruling :18 "over ~2,000 lines needs a stated reason" CONFIRMED; S2 four DEL-09-06
  `secret-scan-summary.json` files at 9,922 / 7,547 / 7,515 / 7,578 lines CONFIRMED; S3
  `validate:release-quality` runs `harness:validate:contract-deps` first (package.json:29), Section 9
  in-process reusing full_test (validate-release-quality-evidence.mjs:430-446), `718b0d47a`
  2026-09-09 CONFIRMED. Authority OK (EX-2 routed to HELPS_HUMANS). Consistency OK.

## Manager disposition of findings (R4 WORKING_ITEMS manager, appended after review)

All 21 findings were confirmed against the cited evidence and fixed. The packets were then re-injected and QA re-run (C1–C5 PASS), and the book was rebuilt.

| Finding | Fix |
|---|---|
| RV-01 BLOCKING | P-15 "Who decides" and "On ruling": the port brief is issued in the Runtime project loop. That code change is outside this App run's write authority; the text and scope-change parts stay within App authority. |
| RV-02 | Book §3 reordered: P-10 before the P-09 group; soft P-06/P-14/P-23 links noted; all cycles listed. |
| RV-03, RV-05, RV-11, RV-14 | Header `recommended` aligned with the body: P-03 "C with b2", P-09 "D — …", P-14 "D — text now; mechanism C …" (body reworded to Option D), P-21 "B — A, but hold 3 rows". |
| RV-04 | P-03: G6a rows are decided in P-02, and their repair follows P-03.b. |
| RV-06 | P-04: the "4 rows" are 3 Full-access rows and 1 DIRECTIVE §2.8 row; the 59 adjacent rows are split 56 in P-09 and 3 in P-20. |
| RV-07 | P-09 and P-13 now cite `delegated-engine-adapter.ts:231` (the empty tool list) instead of the fingerprint field. |
| RV-08 | P-10 option B: any D-APP-116..119 ruling goes on that decision's own record and register row. |
| RV-09, RV-10 | P-11: "P-20 (18) and P-09 (5)"; the drafter-brief wording is removed. |
| RV-12 | P-19: the requirement text stays; only false built/done assertions are corrected; Remaining items are added under the `_STATUS` contract; any narrowing goes to scope change. |
| RV-13 | P-20: 40 rows (32 in a, 8 in b). |
| RV-15 | P-04: the key-UI half now states that `ApiKeySettings` is still mounted and that its hosted reach was not established. Book census labels corrected (22 off-code events + 1 visual-evidence row; 61 testimony notes, 5 absence statements corrected). |
| RV-16 | P-24: the membership rule is stated, plus the wider DirectionEvidence count. |
| RV-17 | Glossary line added to the book; Δ10, MR-6, REF-006 and the "ED split" / "T1 rows" wording glossed or removed in P-04, P-06, P-14 and P-21. REF-006 is glossed as the recorded PRD hash: the manager checked `_REFERENCES.md` and recomputed `docs/PRD.md` at the frozen tree (`17ca3f3c…`, recorded `8649ccba…`). |
| RV-18 | decision_type headers use "owner (incl. App governance amendment)"; P-02.a is an owner decision executed by HELP_HUMAN. |
| RV-19 | P-04: a/b are row sets decided by the P-04.2 reach answer, not separate questions. |
| RV-20 | P-13 option A and P-20 option B route their briefs to the Runtime project loop. |
| RV-21 | P-10 held list now includes `DEC:D-APP-101` (held via P-23.c until D-APP-118 is ruled). |
