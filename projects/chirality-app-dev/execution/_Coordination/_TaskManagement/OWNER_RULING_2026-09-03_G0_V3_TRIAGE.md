# Owner Ruling — G0 v3 Release Task Management Triage Dispositions

Date: `2026-09-03`

Status: OWNER RULING OF RECORD

Provenance: the owner (Ryan Tufts) ruled in the HELP_HUMAN session chat on
2026-09-03 by selecting one option per question; "[click]" marks the
selection. HELP_HUMAN relayed the ruling to this App-loop TASK_MANAGEMENT
instance for application. K-AUTH-1 is satisfied by the owner's own selection
act; this record transcribes the three-question ruling verbatim, including the
unselected option text. It authorizes only the effects the owner selected; it
creates no unstated promotion, priority, disposition, notice route, foreign-loop
write, lifecycle effect, or release claim.

The ruling answers the triage packet prepared under A10 at
`TRIAGE_2026-08-24_G0_V3_RELEASE/` (packet basis
`8884b143f3d8dbca49756e981e4e20299d55875d`, published by PR #670). A "Step 1"
question in the same session concerned the PR #678 merge and is already
executed; it is context only and is not a register act. The companion ruling
record is
`plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md`
(repo-root path).

## Owner ruling — verbatim

```text
Question "Step 2a: TM-APP-025 (dual-target product-delivery direction). G0 B1 ruled macOS arm64 only with the second target deferred, and said this row closes RESOLVED_BY_DECISION once SCA-APP-008 applies. SCA-APP-008 is applied. Disposition?"
  [click] "RESOLVED_BY_DECISION (Recommended)" — Close with G0 B1 plus the applied SCA-APP-008 Impact Assessment line 105 as closure evidence. Executes the conditional closure you already recorded.
  "Retain OPEN" — not selected.
  "SUPERSEDED_BY_SCOPE_CHANGE" — not selected.

Question "Step 2b: the four remaining G0 rows. TM-APP-027/028/032 are DEFERRED on the same DEL-02-06 gate (all ten bindings still held, expected to fire at G6a-G7). TM-APP-030 (helper bundle identity) is OPEN and G0 B2 said let it resolve at G-HELPER. Ruling?"
  [click] "Retain all as classified (Recommended)" — 027/028/032 stay DEFERRED as STILL_BLOCKED with Triggers byte-identical; 030 stays OPEN for G-HELPER. Also apply the mechanical LastReviewed refresh on the 12 reviewed rows and record the compatibility notice as current reciprocal provenance.
  "Retain, but sharpen Triggers" — not selected.
  "Rule TM-APP-030 now" — not selected.

Question "Step 2c: Electron authority drift answering Root's TM-ROOT-122 notice (a named G1 blocker). D-APP-98 already rules 43.2.0 as App authority and the manifest, lockfile, and frozen supply all agree; nine governed App docs still say 43.1.1. Which disposition?"
  "E1: echo D-APP-98 to Root (Recommended)" — not selected.
  [click] "E2: fix the docs first, then echo" — Run the App contract/doc amendment and corpus bump before echoing. Root closure waits on that tranche; one combined identity goes to Root.
  "E3/E4: re-pin Electron" — not selected.
```

## Application basis

- Git basis: `13d845ef822a935296b25aa5e574eda0373b4729` (`origin/main`, PR #678
  merge). Branch `codex/app-tm-g0-rulings-2026-09-03`.
- Live register pre-image: `REGISTER.csv` SHA-256
  `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`
  (13 rows: 9 OPEN, 3 DEFERRED, 1 CLOSED — TM-APP-044, closed 2026-08-21 and
  not yet relocated). Archive pre-image: `REGISTER_CLOSED.csv` SHA-256
  `8e75d44ab11b20877f86a3b57e7d27a47f60f0188d71181db120144cab51d1e6`
  (31 rows).
- Mandatory federation preflight (D-GOV-33) ran read-only before any write:
  `COMPLETE`, four canonical registers validated, zero register writes;
  APP pre-state `OPEN=9 DEFERRED=3 ELEVATED=0 CLOSED=0+1; archived=31`.
- Every pre-image row identity below was verified equal to the packet's
  `REGISTER_ROW_DIFF_CANDIDATE.md` value before editing. Each identity is the
  SHA-256 of the complete newline-terminated CSV record. The review date
  applied is `2026-09-03` (the owner reviewed and ruled today), not the
  packet's hypothetical `2026-08-24`.
- Evidence bytes recomputed at the basis:
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`
  `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`;
  `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Impact_Assessment.md`
  `068c7b29734ea7ca4a0af9bc63d6355beb23f2083b668725d93c951bf53f4cf0`;
  Root `DEL-02-06-COMPATIBILITY-ACCEPTANCE-005/ACCEPTED_COMPATIBILITY_SNAPSHOT.md`
  `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`
  (ten `HELD_UNAVAILABLE` bindings, including `release_act`);
  `NOTICE_2026-08-19_ROOT_TM-APP-027_TM-APP-028_COMPATIBILITY_COMPLETION.md`
  `17f269567c3a5795799e5be92a9ac75281dc8ff553afa11376a055d3e78924ed`;
  `NOTICE_2026-08-21_ROOT_DEL0206_COMPATIBILITY_ACCEPTANCE.md`
  `5930ad2c1395918950aa02fd76635c2209966f02665ad2cd1e5f81e148e535ec`.

## Applied register meaning

### Step 2a — TM-APP-025 (`RESOLVED_BY_DECISION`)

Status `OPEN` → `CLOSED`; Disposition `RESOLVED_BY_DECISION`; `Closed` and
`LastReviewed` `2026-09-03`. `EvidenceRef` lists G0 B1
(`plans/steers/chirality_app_v3_g0_record_2026-08-22.md` lines 80-82) and the
applied SCA-APP-008 `Impact_Assessment.md` line 105; `EvidenceSha` carries the
two recomputed file hashes above in the same order; `EvidenceQuote` carries a
short exact quote from each. One dated Notes entry cites A11 and this file.
No other field changed.

| Identity | SHA-256 |
|---|---|
| Pre-image row | `326816615419aa76c61af973b739d509338b5f5372c7c9da7a2787ac6062fd57` |
| Post-image row | `c46d0949e364c69f997682323044659da45741afcaa3a294be1d79df5892a7ec` |

The post-image row was then relocated byte-identically to
`REGISTER_CLOSED.csv` by the mechanical `taskmgmt archive` pass (K-TM-3:
closure is the owner's act above; archiving is storage layout only).

### Step 2b — TM-APP-027, TM-APP-028, TM-APP-032 (retain `DEFERRED`, `STILL_BLOCKED`)

Status stays `DEFERRED`; `Trigger` byte-identical (asserted before write);
`LastReviewed` `2026-09-03`; one dated Notes entry per row records the
`STILL_BLOCKED` classification, the ten held DEL-02-06 bindings per
acceptance-005, the expected G6a–G7 firing when `release_act` completes the
manifest (G0 B3), and the A11 citation. TM-APP-027 and TM-APP-028 additionally
record the owner's adoption of the 2026-08-19 compatibility notice as current
reciprocal provenance paired with the 2026-08-21 Root acceptance notice. No
notice ledger is created; TM-APP-040 remains `OPEN` on that question.

| Row | Pre-image row SHA-256 | Post-image row SHA-256 |
|---|---|---|
| TM-APP-027 | `5bc5966ea43648d02ed83c2858bf675d7c002a296e665a0f4041e38ef945e48a` | `d61b4bfbb17cb7096096b20893417f55de4261c224c7e653fed2cf5c145252ef` |
| TM-APP-028 | `bf292765033d18fed549b67a4b8b8588c6a029ac5f29bdf8caa8d037128909da` | `81508f65465fc27e512e818af5a519ff9e487b01a44f9ae5c39ac8511d9ac1fc` |
| TM-APP-032 | `3456bc79c6255d84036aa34e7a69cc27cbab73e235920edfcc76e9d9c3d6e696` | `1082feab8bc10063581ffa8231d6839a930d0a58cec98b20b6013be873122b86` |

### Step 2b — TM-APP-030 (retain `OPEN` for G-HELPER)

Status stays `OPEN`; `LastReviewed` `2026-09-03`; one dated Notes entry
records retention for G-HELPER per G0 B2 and this ruling, with the A11
citation. No bundle-identity choice is inferred.

| Identity | SHA-256 |
|---|---|
| Pre-image row | `7359b18b66a1a8974ced33c11c9a6aaf5ddd9a95efe71805f9692819ca88d1d5` |
| Post-image row | `ce0c09418dbd8b909b43382fff44a95f37aa9dd350f1fa8932bccb26b7458cd8` |

### Step 2b — mechanical `LastReviewed` refresh (remaining reviewed rows)

Only `LastReviewed` → `2026-09-03`. Nothing else on these rows changed.

| Row | Pre-image row SHA-256 | Post-image row SHA-256 |
|---|---|---|
| TM-APP-029 | `b8644019cf7d129cc27ae9e7565f38a08aefb1072592ea0e717a2695821cd1ed` | `002217f31cab9fa21d092d9eddc9972a8b655e3f07aaf0f41881a7ead11baac2` |
| TM-APP-033 | `1cad4d43e7e93f4b255c542a95d102dd10476367bd6905b076d337aeb4d6b693` | `5a8fb90c09b4a61e6e4486ff155f41d8a286db291e6ea18052ea102ed6a5ea3d` |
| TM-APP-034 | `9d50b7a32b6e1b036ca2e1b59130a9f83f8ffa9c16a77b713ebc3e27aa81566c` | `d1458d6f343d0e7cb3435ade7b0e580beddddeac08277c3b7b48d69df2966bde` |
| TM-APP-036 | `a9bd2a78c5770c6d04203d962c5c7df9d75b33c93c1fbebac9950ca369447ce8` | `d34f130de08b3ceef2a1786bb46913ae1c71824a618724566e55c83ead9e8783` |
| TM-APP-038 | `3728e221c72b859d64effe9d84e89500b8e63d75873618007608c6e597952773` | `6c3160e3e3e8d5dd4c09fe5bb106f486a599449cb282a2211f09e9995c7bb901` |
| TM-APP-040 | `8049f1d2b00f655608258d555402256d028aff7424ac2204bdd459cb48a329f9` | `f843a1763d49f6fdd885c088b1bfa20acee4526890d09790a04e0f6a447533cb` |
| TM-APP-042 | `41577c4a95fef7a25c0de40d9bcc93f5b1c167eec41c40ac6714596e08a43e21` | `ba50c166b898e133b1a5bb3490504707f5e70115cdbbb244a774d90fac685ddc` |

Field-level proof over the whole file: exactly 12 `LastReviewed` cells, 5
`Notes` cells, and the six closure cells of TM-APP-025 (`Status`,
`Disposition`, `EvidenceRef`, `EvidenceSha`, `EvidenceQuote`, `Closed`)
differ; header, row order, and every other cell are byte-identical.
TM-APP-044 row identity
`20facb6978ecef9f8fa5b4a9023d6535fa92cff6aedef825554c16f0043d42d7` is
unchanged before and after relocation.

### Archive pass and post-state

`taskmgmt archive` relocated both CLOSED rows (TM-APP-025 from this ruling
and TM-APP-044, closed 2026-08-21) to `REGISTER_CLOSED.csv`. Post-state:
live `REGISTER.csv` 11 rows (`OPEN=8 DEFERRED=3 ELEVATED=0 CLOSED=0`),
SHA-256 `bae90ca564f45d51bbb94722cf64b3cda6bc0d614365a2c177b2b79c55844931`;
`REGISTER_CLOSED.csv` 33 rows, SHA-256
`7b0489dce6ae11de6453e59738006a81854912ef191d24627bd1de9094ccd19b`. Both
validate `PASS`. Final federation pass `COMPLETE`, zero register writes, APP
`OPEN=8 DEFERRED=3 ELEVATED=0 CLOSED=0; archived=33`.

## Step 2c — Electron authority drift: E2 authorization

The owner selected E2 of `ELECTRON_DRIFT_DISPOSITION_CANDIDATE.md`: propagate
D-APP-98 through the App governed documents first, then echo. This is not a
register-row act; no App register row carries it. The owner's E2 selection
authorizes, as a **separate App tranche** not executed here:

1. an App authority-document concordance amendment replacing or qualifying the
   nine live `43.1.1` references enumerated in the candidate's drift table
   (`docs/CONTRACT.md:57,199`; `docs/DIRECTIVE.md:119`;
   `docs/PLAN.md:66,479,502`; `docs/SPEC.md:710`; `docs/PRD.md:64,177,1392`;
   `docs/TYPES.md:510`; `docs/VALIDATION_STRATEGY.md:98`;
   `docs/harness/reliance_boundary_register.md:41`) with the D-APP-98
   successor fact (Electron `43.2.0`), D-APP-72 preserved as immutable
   history, executed through the App's ordinary amendment instrument with a
   D-APP-38 authority-corpus version bump and its registered checks; and
2. after that tranche lands, one combined echo — the D-APP-98 identity
   (`71dfc1ae6369acea1e49f71d68e45aaf9da8f14c5f6a77733845c43f3ee7c020`) plus
   the applied concordance identity — routed to Root for TM-ROOT-122 through
   the App loop's ordinary notice flow.

Notice adoption: the Electron notice
(`NOTICE_2026-08-03_ROOT_TM-ROOT-122_ELECTRON_AUTHORITY_DRIFT.md`, SHA-256
`f806474b4500b2b081a49d759a0c0793fe65bce860d7efd146147abc38d5951e`) is
adopted under option 2 of `NOTICE_ADOPTION_ASSESSMENTS.md` ("Amend the
receiving assessment"): the notice's missing-successor premise is recorded as
later superseded by D-APP-98; the App completes the G1 concordance act first;
both identities are echoed together. Root closure of TM-ROOT-122 therefore
waits on that tranche.

Effect boundary of Step 2c in this tranche: no docs write, no corpus bump, no
notice routing, no Root write, no register row, no Electron pin change. E3/E4
re-pinning is expressly not selected.

## Effect boundary

This ruling record and the register edits it describes are App Task
Management coordination artifacts. They do not amend a deliverable, contract,
or corpus member; execute validation beyond the registered register checks;
route a notice; write a Root or other foreign surface; lift TM-ROOT-106/122
or any of the ten held DEL-02-06 bindings; pass G1 or any later gate; or
authorize implementation, supply, release, publication, or reliance. Closing
TM-APP-025 records the owner's product-delivery decision as ruled at G0 B1;
it grants no second-target, packaging, or lifecycle authority.
