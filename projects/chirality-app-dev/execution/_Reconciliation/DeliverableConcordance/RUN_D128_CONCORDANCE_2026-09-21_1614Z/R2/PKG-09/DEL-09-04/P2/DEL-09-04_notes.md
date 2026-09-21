# DEL-09-04 — part P2 notes (forward pass)

Worker: TASK (Type 2), split part P2 of DEL-09-04 (PKG-09, wave 5). Units owned: CLM-013..CLM-025
(SoW Praxeology and Axiology), REM-1, REM-2, plus run-local REGISTER-51..55 and STATE-51..56.
Basis: frozen tree `00115c719`. Deliverable-local file citations in the ledger (`ScopeOfWork.md:233`,
`_STATUS.md:105`, `_REFERENCES.md:12`, ...) are relative to
`projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/`.
`<frozen>` in the REM-2 row stands for the frozen reading tree.

## 1. Census

32 rows (sealed figures; no errata file yet).

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 8 |
| STATE_ASSERTION | 8 |
| CONTEXT_CLAIM | 7 |
| REGISTER_DEFECT | 5 |
| REMAINING_WORK | 2 |
| ACCEPTANCE | 1 |
| EXCLUSION | 1 |

| Disposition | Rows | of which SEE rows |
|---|---:|---:|
| STALE_SPECIFICATION | 12 | 3 (CLM-013→REGISTER-51, CLM-019→CLM-013, CLM-025.1→REGISTER-51) |
| ALIGNED | 7 | 0 |
| PARTIALLY_IMPLEMENTED | 4 | 1 (CLM-023.1→CLM-021) |
| NOT_AUDITABLE | 3 | 0 |
| REMAINING_STATE_MISMATCH | 3 | 0 |
| AUTHORITY_CONFLICT | 2 | 1 (CLM-023.3→CLM-022) |
| IMPLEMENTED_DIFFERENTLY | 1 | 0 |

- SEE rows: 5 (counted separately per MR-4). Without them, 27 distinct dispositions.
- Split rate: 2 of 15 indexed units split (13%). CLM-023 (trade-off table) → .1-.4 and CLM-025
  (conflict table CONF-001..004) → .1-.4, both as tables of independently dispositionable rows.
  CLM-018 lists one SubItem (VER-001) → one row. CLM-017 (verification table) kept as one row because
  its rows restate REQ items owned by P1's CLM-009/CLM-011.
- Run-local rows: REGISTER-51..55 (5), STATE-51..56 (6).
- Confidence: HIGH 10, MEDIUM 19, LOW 3.
- HumanDecisionNeeded: R4 on 4 rows (CLM-016, CLM-017, CLM-022, CLM-023.3), all on the signing-posture
  conflict. No R4-Qn rows: no claim here is met only by LEGACY_ONLY code on the product path.

## 2. Least-confident rows

- **CLM-024 (Examples TBD) — STALE_SPECIFICATION, LOW.** A2 build records with commands, stage exits and
  the Codex-pin probe output exist in AgentRuns, so "no example transcript available" reads false.
  Alternative: none is *accepted* and none sits in the deliverable's own corpus, so the TBD is still
  true (NOT_AUDITABLE).
- **CLM-025.4 (CONF-004) — STALE_SPECIFICATION, LOW.** The D-APP-127 packaging procedure names packaged
  S-6/S-8 as the post-build minimum, which overtakes the "SDK-backed turn start after R1" question.
  Alternative: no ruling names CONF-004, so the open question stands (NOT_AUDITABLE).
- **REM-2 (V3-02 icon) — REMAINING_STATE_MISMATCH, LOW.** `b2b32669c` (2026-09-10) replaced
  `build/icon.icns`/`icon-macos.svg`, with an independent review PASS recorded in TRIAL_FINDINGS, after
  the item was seeded; that reads as its removal condition ("merged with review PASS"). Alternative: the
  trial change sat outside the gated item and lacks the required reproducibility record, so V3-02 is
  legitimately open and there is no mismatch.
- Also worth a second look (MEDIUM): **CLM-022/CLM-023.3 AUTHORITY_CONFLICT.** Alternative reading:
  the D-GOV-43 amendments of CONTRACT's preamble and PRD 7/12.8/NFR-030 are the later governed change and
  should prevail over the unamended K-RELEASE-1/PRD 6.2 lines, which would make these rows
  STALE_SPECIFICATION with LatestDecision D-APP-127. I did not choose because the same documents carry
  both texts and no ruling names K-RELEASE-1 (brief: never resolve such a conflict).
- **REM-1 — REMAINING_STATE_MISMATCH, MEDIUM.** It relies on agent-recorded build/publication records
  (CONTEXT) to read the removal condition as met. Alternative: "the package lands" may mean a deliverable-local
  recording that has not happened, which makes the item still open (no mismatch).

## 3. Register-defect summary

- **REGISTER-51** `_REFERENCES.md`: REF-002 CONTRACT, REF-003 SPEC and REF-006 PRD record MATCH with
  Actual = Expected. None reproduces at `00115c719` (REFERENCE_HASHES.csv, Match NO). REF-001, REF-004,
  REF-005 (App `docs/PLAN.md`) and REF-007/009/010 (Root `workflows/software-decomp/**`) still reproduce.
  CLM-013, CLM-019 (via CLM-013) and CLM-025.1 point to it. CLM-015, CLM-018, CLM-021 and REGISTER-54
  restate REF-006 MATCH inside larger units (noted as "cf. REGISTER-51").
- **REGISTER-52** `_CONTEXT.md`: the SCA-APP-001 paragraph still names Claude Agent SDK / Anthropic as
  the current path and cites four-document files (Guidance/Specification/Procedure/Datasheet.md) that no
  longer exist. Not revised under D-APP-127 (application map NO).
- **REGISTER-53** `Dependencies.csv`: DEP-009 targets "current shipped Anthropic packaged network
  guardrails"; DEP-005 says Node >=20 (enforced >=22.19.0); EvidenceFile cites absent files; the V3-01 and
  V3-02 Depends edges are not in the register.
- **REGISTER-54** `_DEPENDENCIES.md`: "no accepted dependency edges have been extracted yet" contradicts
  its own 9-row register section; the D-APP-56 annotation restates REF-006 MATCH.
- **REGISTER-55** `_STATUS.md` header: Last Updated 2026-09-12 predates the 2026-09-13 3.0.0 builds and
  publication and the 2026-09-19 3.0.1 version bump (bookkeeping lag, rule 2b).
- Other hygiene noticed, no separate row: `_STATUS.md:62` embeds a machine-specific user-home absolute
  path (inside preserved history; not reproduced); V3-01 cites decomposition "L367" (pinned `d6f6cadb2`)
  while V3-02 cites "L381" (current), which is the same row at two revisions.

## 4. Direction and cause

- Main CauseTags: DOC_HYGIENE (7; hash drift and register placeholders), A2_TOPOLOGY (5; the D-GOV-43
  packaging procedure and LaunchAgent retirement), CODEX_SOLE_ENGINE (4; Anthropic-era network
  wording and tooling), PRE_V3_DRIFT (3; asset-set completeness and the Node floor), CARRIER_PROPAGATION
  (2), SHELL_REDESIGN (1; the V3-02 icon from the SCA-APP-010 seating).
- CAUSE2 secondaries: CARRIER_PROPAGATION on most A2/Codex rows (ScopeOfWork.md, `_CONTEXT.md`,
  `Dependencies.csv` and `_REFERENCES.md` are all `NO` in D-APP-127_APPLICATION_MAP; only `_STATUS.md` was
  revised); A2_TOPOLOGY on REM-1; `OTHER:V3_ROLE_ADOPTION` on CLM-021 and CLM-025.3 (the v3 bundle manifest
  in `prepare-packaged-instruction-root.mjs` fixed the bundled list; it omits SPEC 1.1's `docs/PLAN.md`,
  `docs/WHAT-IS-AN-AGENT.md` and `PROFESSIONAL_ENGINEERING.md`).
- GOVERNING records used: D-APP-127 (application record, incl. the D-APP-100 replacement text and the
  boundary "no release, publishing ... authorized"); App CONTRACT line 17 and K-RELEASE-1/K-VALIDATE-1;
  PRD 6.2, 7 acceptance, 12.8, NFR-030; SPEC 1.1; App DIRECTIVE §0.
- CONTEXT records used (never changing a Disposition): `AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/{PACKAGING_PROCEDURE.md, BUILD_EVIDENCE_20260912.md}`,
  `AgentRuns/APP_V3_USER_JOURNEYS_20260912/{BUILD_EVIDENCE_RELEASE_20260913.md, PUBLIC_RELEASE_20260913.md}`,
  `AgentRuns/APP_V3_DIRECT_TRIAL_20260910/TRIAL_FINDINGS.md:73`. These are agent records, not rulings.
- NONE_FOUND searches: `_DECISIONS/_REGISTER.md` grep for `REF-006|_REFERENCES|DEL-09-04` (no REF-006
  re-baseline after D-APP-38), `Developer ID|notari|F-APP-2` (only D-APP-97, which fences signing),
  `CONF-003|instruction-root manifest` (none); AgentRuns APP_V3_* grep for REF-006 (none).
- Done-declaration: Q-02 (whether the session publishing approval is the release act / F-APP-2 lift) bears
  on CLM-014, CLM-016, CLM-022, CLM-023.3, REM-1, REGISTER-55 and STATE-51. It is noted only.

## 5. Method friction

- **Disabled-by-default branches and REACH.** The brief says a disabled-by-default branch (signing without
  an identity) "is judged as not live", but the REACH vocabulary has no tag for it. Tagging
  `sign-electron-runtime-v2.mjs` LEGACY_ONLY would wrongly trigger R4-Q1 logic for current A2 code, so I
  tagged it `REACH=LIVE` and wrote `DISABLED_BY_DEFAULT` in Notes. Proposal: add `REACH=DISABLED` (or
  allow `REACH=LIVE;STATE=DISABLED`, as capability files already do).
- **Manual tools.** `generate-macos-icon.mjs` is reached from no entry, so per A0 it takes
  `REACH=LEGACY_ONLY` + UNREACHED, although it is not legacy. The tag misdescribes it; same proposal.
- **Governing texts in conflict inside one document** (CONTRACT preamble vs K-RELEASE-1; PRD 6.2 vs PRD
  7/12.8). DIRECTIVE §0 orders documents, not clauses within one document, so AUTHORITY_CONFLICT was the only fit.
  A named question (for example R4-Q6, the release signing/notarization posture) would let R3 cluster
  these rows across PKG-09.
- **SEE across parts.** P2 rows restating P1 content (CLM-017 vs P1's CLM-009/011) cannot use `SEE:`
  because the target is in the other part's ledger. I disposed them independently. The manager should
  check agreement after the merge.
- **Proof versus capability.** Most pass criteria here are proof records. A2-era proofs exist only as
  agent-recorded AgentRuns files (CONTEXT). I cited them as documentary claims and never as rulings.

## 6. Effort

About 35 files or ranges read: the brief, CONVENTIONS, RUN_BASIS §3/§5/addenda, the PREGATHER P2
section, the evidence-pack rows, the deliverable's SoW (L200-400), `_STATUS.md` (in ranges),
`_REFERENCES.md`, `_CONTEXT.md`, `Dependencies.csv`, `_DEPENDENCIES.md`, the INSP-03 assessment,
`package.json`, eight packaging scripts (in ranges), `main.ts`/`runtime-service-host.ts`/
`runtime-control-ipc.ts`/`codex-executable.ts` excerpts, `codex-supervisor.ts` L98-112, the D-APP-127
record excerpts, the PACKAGING_PROCEDURE, three AgentRuns build/publication records, CONTRACT/PRD/SPEC
excerpts, and the test-case names of six script test files. Git use was limited to read-only `blame -L`
on codex-supervisor L104-108 and L261 (untouched; all PostReleaseBasis NO, since no App path is in
TOUCHED_PATHS), `log` on the icon files, and `show --stat b2b32669c`. The context budget was adequate
and not tight.

## Coverage gaps

- `MEMORY.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `Evidence/**` and `_run_records/**` carry state
  assertions (for example LaunchAgent-era proofs and a pointer to DEL-09-06 packaged-security evidence),
  but my prompt did not assign them to P2. The manager should confirm that P1 or the merged ledger owns them.
- Work delivered but not documented in the deliverable: the A2 consolidated builds (3.0.0-rc.1, 3.0.0),
  the Developer ID signing hook, the notarization and the 3.0.0 publication are recorded only under
  AgentRuns. No SoW unit describes signing/notarization as deliverable scope (see CLM-022). The 3.0.1
  version (`package.json:3`) has no build record anywhere in root.
- Possible packaged instruction-root inconsistency (P1 or DEL-level owner): in packaged mode `main.ts:808`
  sets the App process's `CHIRALITY_INSTRUCTION_ROOT` to `Resources/` while the service receives
  `Resources/instruction-root` (`main.ts:441-445`). The LIVE `src/lib/harness/instruction-root.ts` requires
  `docs/PLAN.md` and `agents/` at that root, and the v3 bundle does not ship `docs/PLAN.md`. I noted this
  at STATE-54 without changing a disposition. It was not probed further.
- The LIVE renderer egress allowlist (`main.ts:133`) still names `api.anthropic.com`. This is a
  DEL-09-06/P1 network matter, noted at CLM-021.
