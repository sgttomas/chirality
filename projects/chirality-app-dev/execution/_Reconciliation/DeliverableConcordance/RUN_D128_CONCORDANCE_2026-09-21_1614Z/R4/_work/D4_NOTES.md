# D4 notes — P-06, P-17..P-22 (RUN_D128, R4)

TASK D4 (Type 2). Drafts only; no rulings. I was interrupted once by a server overload and resumed; the only thing on disk from before was `D4_scripts/dump.py`.

## Method
- I read the common brief, the D4 brief, CONVENTIONS §1/§2.4/§2.6/§4, RUN_BASIS §5 and Addenda 4-13, OWNER_DIRECTION.md, R3_SUMMARY §8, CLUSTERS.md (CL-06, CL-17..22), R3_SPOT_CHECK.md, the fact sheets, and CROSS_PACKAGE_FINDINGS (XPF-015/016/020/022/027/029/030/034/035/048/050).
- Helpers, all read-only apart from the SUBQ output:
  - `D4_scripts/dump.py`: dumps a packet's rows;
  - `held.py`: D-APP-116..119 check (no hits in any D4 packet);
  - `xref.py`: cross-packet membership;
  - `subq.py`: writes the SUBQ CSVs.
- Frozen-tree checks:
  - `9b005c23a --stat`: no `projects/chirality-app-dev/docs/` file was changed;
  - App SPEC §7 and §13.1;
  - TYPES §3.4 and PRD FR-026;
  - `persona-resolution.ts:3-9` and `harness/session-manager.ts:9`;
  - the role file header;
  - DIRECTIVE §0 rank 7;
  - K-WRITE-1;
  - the D-APP-108 Q3 wording;
  - the D-GOV-42 Root register row;
  - `AUTHORITY_CORPUS.json` (current v23, last written by `23b3879b3`) and the post-v23 doc edits (`9eaddb596`, `95b342519`, `7f1e9f387`);
  - the D-APP-38 ruling text;
  - the D-APP-127 consequential-applications list;
  - the R2 application map counts (11 `_STATUS` YES, 54/54/54/52 NO);
  - `frontend/package.json` runtime-contracts dependency and Node engine;
  - the harness-contract `deprecated` field;
  - the App-local premerge workflow (Node 20, `ANTHROPIC_API_KEY`);
  - `not-found.tsx` rendering `AppShell`;
  - the `shell-frame.tsx` working-root guard.

## Sub-question rule (`subq.py`)
- P-17: b = `SOW:SOW-079.1`; a = the rest (117/1).
- P-19: b = Disposition in {PARTIALLY_IMPLEMENTED, DOCUMENTED_UNIMPLEMENTED, IMPLEMENTED_DIFFERENTLY} (208/52). P-19 includes IMPLEMENTED_DIFFERENTLY in b because no ruling covers pre-v3 differences.
- P-20: b = {PARTIALLY_IMPLEMENTED, DOCUMENTED_UNIMPLEMENTED} (100/17).
- P-21: same rule as P-20 (125/14).
- P-22: same rule as P-20 (61/14).
- P-06 and P-18 are not split.

## Things the manager must know
- **Tagging of D-GOV-42.** It is a Root register row that is on neither the GOVERNING nor the CONTEXT list in RUN_BASIS §5, so I tagged it `[run finding]`. The P-06 recommendation relies on its wording ("candidate implementation", "no receiving-loop adoption"), which I verified in the frozen Root register.
- **Clause list in P-06.** FR-001, FR-007, FR-023 and DIRECTIVE §4.1 come from XPF-015 and were not re-verified clause by clause; the packet says so. SPEC §7 and §13.1, TYPES §3.4, PRD FR-026 and K-WRITE-1 were verified.
- **Next free D-APP ID.** The working-repo register currently ends at D-APP-129. The packets say "next free D-APP ID" and give no number.
- **Rule 2b moves.** The 9 moves are split: 4 in P-18, 4 in P-19 and 1 in P-17 (DEL-07-01#REGISTER-3). P-18 carries the confirm-or-reverse ask, and P-17 and P-19 point to it.
- **Hidden cross-packet dependencies** among rows that are PRIMARY in D4 packets:
  - P-20: DEL-06-06#CLM-004.2, #CLM-010.1 and #CLM-025.1 are the R4-Q5 matter (P-05). DEL-02-05#CLM-013.2 is the R4-Q6 key-UI matter (P-04).
  - P-21: DEL-03-04#CLM-009.10 and DEL-05-03#CLM-010.5 are live redaction gaps (P-12). SOW:SOW-064.2 is the shared `~/.codex` question (P-04).
  - P-22: the four OTHER:V3_ROLE_ADOPTION rows depend on P-06.
- **P-20 and P-04/P-09 overlap.** No P-20 PRIMARY row is PRIMARY or ALSO in P-04 or P-09. The overlap runs the other way: 517 P-20 ALSO rows are PRIMARY elsewhere (P-09 342, P-04 75, P-05 39). The packet says so and sequences tranches.
- **Word count.** P-06 is slightly above the target of about 900 words, even after trimming.
