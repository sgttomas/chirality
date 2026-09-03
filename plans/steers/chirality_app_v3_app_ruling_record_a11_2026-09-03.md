# APP RULING RECORD A11 — G0 Task-Management triage dispositions and Electron-drift E2 authorization — owner ruling of 2026-09-03

> **Plans-folder status:** ACTIVE owner-ruling record — non-governing transcription source. Owner: Ryan Tufts. Scope: the G0 Task-Management triage dispositions for TM-APP-025/027/028/030/032, the mechanical `LastReviewed` refresh on the twelve reviewed rows, and the authorization of a separate App Electron-drift concordance tranche (option E2). Target workspace: App-dev loop. Supersedes nothing; executes the conditional closure recorded at G0 B1. Companion instruments: A10 (`chirality_app_v3_app_ruling_record_a10_2026-08-24.md`, SHA-256 `0908fee812919291979dd486dd9748fda21b9fb4b20afb13604a1a3e02bd8aa2`); the applied owner-ruling file `projects/chirality-app-dev/execution/_Coordination/_TaskManagement/OWNER_RULING_2026-09-03_G0_V3_TRIAGE.md`. Governing role instruction: `agents/AGENT_TASK_MANAGEMENT.md` (D-GOV-32; K-TM-1..6 — every disposition remains a human act).

Ruled by Ryan Tufts (K-AUTH-1) in the HELP_HUMAN session chat on 2026-09-03
by selecting one option per question. "[click]" marks the option the owner
selected. HELP_HUMAN relayed the ruling to the App loop's TASK_MANAGEMENT
instance, which applied it on branch `codex/app-tm-g0-rulings-2026-09-03`
from basis `13d845ef822a935296b25aa5e574eda0373b4729` (PR #678 merge).

## Context

A10 authorized preparation only. The resulting triage packet,
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/TRIAGE_2026-08-24_G0_V3_RELEASE/`,
was prepared at basis `8884b143f3d8dbca49756e981e4e20299d55875d` and
published by PR #670 (merge `f8db18addfee2e808bdfd8d06f34b1168503277e`,
Receipt-201). It presented five row decisions unselected — TM-APP-025
(closure echo ready), TM-APP-027/028/032 (`STILL_BLOCKED`, retain
`DEFERRED`), TM-APP-030 (retain `OPEN` for G-HELPER) — plus the Electron
authority-drift disposition candidate answering Root TM-ROOT-122, the
notice-adoption assessments for both unadopted Root notices, the
staleness/closure echo over the remaining OPEN rows, and an unapplied
`LastReviewed` candidate.

The live App register at the ruling basis was SHA-256
`eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`
(13 rows; TM-APP-025/029/030/033/034/036/038/040/042 OPEN,
TM-APP-027/028/032 DEFERRED, TM-APP-044 CLOSED and not yet relocated).
SCA-APP-008 is applied (`_ScopeChange/_LATEST.md` SHA-256
`12c7758b4ec15c50379fcae1bf26670e26e281518687db4dc9200ff9dd23cc9b`). A
"Step 1" question in the same session concerned the PR #678 merge and is
already executed; it is context only.

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

## Applied effect (summary; exact pre/post row identities are in the owner-ruling file)

- TM-APP-025: `CLOSED` / `RESOLVED_BY_DECISION`, closed `2026-09-03`;
  evidence G0 B1 (`chirality_app_v3_g0_record_2026-08-22.md` lines 80-82,
  SHA-256 `86b9877c6bea08a9f79c2af2378d5d38722a09c1a10deb37f87211c76d2c290b`)
  and applied SCA-APP-008 `Impact_Assessment.md` line 105 (SHA-256
  `068c7b29734ea7ca4a0af9bc63d6355beb23f2083b668725d93c951bf53f4cf0`);
  relocated to `REGISTER_CLOSED.csv` by the mechanical archive pass together
  with the previously closed TM-APP-044.
- TM-APP-027/028/032: `DEFERRED` retained, Triggers byte-identical,
  classified `STILL_BLOCKED`; all ten DEL-02-06 bindings remain
  `HELD_UNAVAILABLE` per acceptance-005 (SHA-256
  `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`);
  expected firing at G6a–G7. For 027/028 the 2026-08-19 compatibility notice
  (SHA-256 `17f269567c3a5795799e5be92a9ac75281dc8ff553afa11376a055d3e78924ed`)
  is adopted as current reciprocal provenance paired with the 2026-08-21 Root
  acceptance notice (SHA-256
  `5930ad2c1395918950aa02fd76635c2209966f02665ad2cd1e5f81e148e535ec`). No
  notice ledger is created; TM-APP-040 stays `OPEN` on that question.
- TM-APP-030: `OPEN` retained for G-HELPER per G0 B2.
- `LastReviewed` = `2026-09-03` on all twelve reviewed non-closed rows
  (the packet's hypothetical `2026-08-24` is not used; the owner reviewed and
  ruled today).
- Post-state: live register `OPEN=8 DEFERRED=3 ELEVATED=0 CLOSED=0` (11
  rows), SHA-256
  `bae90ca564f45d51bbb94722cf64b3cda6bc0d614365a2c177b2b79c55844931`;
  archive 33 rows, SHA-256
  `7b0489dce6ae11de6453e59738006a81854912ef191d24627bd1de9094ccd19b`.
- Electron drift (E2): the owner authorizes, as a separate App tranche, an
  App authority-document concordance amendment of the nine `43.1.1`
  references enumerated in `ELECTRON_DRIFT_DISPOSITION_CANDIDATE.md`
  (`docs/CONTRACT.md`, `docs/DIRECTIVE.md`, `docs/PLAN.md`, `docs/SPEC.md`,
  `docs/PRD.md`, `docs/TYPES.md`, `docs/VALIDATION_STRATEGY.md`,
  `docs/harness/reliance_boundary_register.md`) to the D-APP-98 successor
  fact with a D-APP-38 authority-corpus bump, after which one combined echo
  (D-APP-98 identity plus the applied concordance identity) is routed to Root
  for TM-ROOT-122. The Electron notice is adopted under option 2 of
  `NOTICE_ADOPTION_ASSESSMENTS.md` ("Amend the receiving assessment").

## Boundary of this authorization

Authorized: the register dispositions exactly as applied above and recorded
with pre/post row identities in the owner-ruling file; the mechanical archive
relocation of CLOSED rows; and the E2 docs-concordance tranche as a separate,
later App tranche executed through the App's ordinary amendment instrument
with its registered checks and corpus bump.

Not authorized: any lifecycle, implementation, supply, release, publication,
reliance, signing, notarization, or foreign-loop act; any Root surface or
Root register write; any notice routing in this tranche (the combined echo
follows the concordance tranche); any Electron pin change (E3/E4 not
selected); any notice-ledger creation (TM-APP-040 unchanged); any Trigger
change on TM-APP-027/028/032; any bundle-identity decision for TM-APP-030.
TM-ROOT-106/122 are not lifted. G1 is not passed. The ten held DEL-02-06
bindings, D-APP-97/F-APP-2, G6a, and every later gate remain exactly as they
are. Closure of TM-APP-025 records a decision already ruled at G0 B1; it
grants no second-target or packaging authority.

## Not ruled here

- The content, wording, and validation of the E2 concordance amendment
  itself (a later App tranche under its owning instrument).
- The text and timing of the combined echo to Root and Root's disposition of
  TM-ROOT-122 (Root authority).
- TM-APP-030's bundle-identity decision (G-HELPER).
- Any sharpening of the TM-APP-027/028/032 Triggers (option not selected).
- TM-APP-040's notice-ledger / scanner-scoping / standing-noise choice.
- Dispositions for TM-APP-029/033/034/036/038/040/042 (reviewed only;
  `LastReviewed` refreshed).
- The App Server supply authorization, G1, G6a, G-HELPER, and every later
  gate; any implementation, activation, release, publication, or reliance act.
