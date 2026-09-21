# EXT worker common rules (RUN_D128, R2 scope extension, wave 5)

You are a TASK (Type 2) worker dispatched by the EXT WORKING_ITEMS manager. You do not
delegate. Placeholders `<FROZEN_TREE>`, `<RUN>`, `<APP_WORK>` are given in your prompt; use
them to find files, but **never write their values (or any absolute path) into an output**.
Write repo-relative paths (e.g. `projects/chirality-app-dev/frontend/src/x.ts:120`).

## Read first

1. `<RUN>/CONVENTIONS.md`, in full. It is your rulebook. **§8 defines your units and the
   extension ledger schema.** §2 is the column rules; §2.4 and §2.6 carry the rules below.
2. `<RUN>/RUN_BASIS.md` §5 (authority map; the "GOVERNING, flagged" row) and Addenda 3–7.
3. Your own brief (the file that pointed you here).

## Evidence roots (read-only)

- Read only: `<FROZEN_TREE>/projects/chirality-app-dev/**`;
  `<FROZEN_TREE>/projects/chirality-runtime/packages/**` and `.../tests/**`; the run-folder
  inputs named in your brief; Root governance documents (`<FROZEN_TREE>/docs/{DIRECTIVE,CONTRACT,SPEC,TYPES}.md`)
  only where App docs defer to them.
- **Never read:** Root `<FROZEN_TREE>/execution/**`; `projects/chirality-runtime/execution/**`
  (exclude both explicitly in every grep/find, e.g. `--exclude-dir=execution` when searching
  the runtime project, and never search the frozen tree root without excluding `execution/`);
  the working repository's deliverable folders (anything outside `<FROZEN_TREE>` except the
  run-folder inputs below); any other R2 folder (`<RUN>/R2/PKG-*`, other `<RUN>/R2/EXT/*`
  worker folders); any R0 ledger (`<RUN>/R0_CALIBRATION/DEL-*`).
- Run-folder inputs you may read: `<RUN>/CONVENTIONS.md`, `<RUN>/RUN_BASIS.md`,
  `<RUN>/R1_INVENTORY/{EXTENSION_INDEX,DELIVERABLE_INVENTORY,DECISION_INDEX}.csv`,
  `<RUN>/R2/EXT/EVIDENCE_PACK/**`, `<RUN>/R2/EXT/_inputs/**`,
  `<RUN>/R2/SURFACES/*_capabilities.csv` and `*_notes.md`, `<RUN>/GATE_TRANSCRIPTS/*.md`,
  `<RUN>/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md` (CONTEXT only).
- Economize: grep before you read; read line ranges; prefer the evidence pack.

## Git, installs, tests

- **Git: read-only `git -C <FROZEN_TREE> log`, `git -C <FROZEN_TREE> show`, and
  `git -C <FROZEN_TREE> blame -L …` against `<FROZEN_TREE>` only.** No `merge-base`, no
  `ls-files`, no `grep`, no `diff`, no `rev-parse`, no other git subcommand, and no git at all
  against the working repository.
- No installs. No test runs (cite `<RUN>/GATE_TRANSCRIPTS/` instead). No network.

## Evidence pack (`<RUN>/R2/EXT/EVIDENCE_PACK/`)

`TOUCHED_PATHS.csv` (PostReleaseBasis: a cited file on this list → check whether the
relied-on lines fall inside a listed range, or `blame -L` them; `YES` if any line blames to
`da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a`), `REACHABILITY.csv` (REACH tags),
`REFERENCE_HASHES.csv` (`HASH-RECOMPUTE@00115c719`), `DECISION_HITS.csv` (which
deliverables cite which D-APP/D-GOV), `D-APP-127_APPLICATION_MAP.csv`. Read CSVs with
short scripts (python `csv`), not by dumping them.

## Rules given verbatim

**Addendum 5 tie-break (CONVENTIONS §2.6), between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`:**

1. Use `STALE_SPECIFICATION` when the text states a present fact that is now false (a hash
   recorded as `MATCH`, a path called "current", a dependency marked `SATISFIED`, a file said
   to exist). The rule is the same for SoW, `_STATUS`, register and references text.
2. Use `REMAINING_STATE_MISMATCH` only for (a) an item in `## Remaining`, or a `REMAINING_WORK`
   row, whose open or done status is contradicted by the evidence; or (b) register
   bookkeeping that is behind but says nothing false about the product or its references
   (a `Last Updated` date, a `TBD` placeholder, a lagging status field).
3. MR-8(iv) clarified: a claim tied to a named snapshot ("MATCH at v23") stays a REGISTER row.
   Text that restates it as current ("is MATCH") without naming the snapshot takes
   `STALE_SPECIFICATION` and points to the REGISTER row (`SEE:`).
4. If both still fit, choose the verdict whose repair is a change to deliverable text, and
   record the other in Notes as `ALSO:<verdict>`.

**Addendum 6 legacy-versus-live subject test for R4-Q1 (CONVENTIONS §2.4):**

1. **Decide the subject from the claim text, not from where the code lives.** The subject is
   *product behaviour* if the claim names the App, the system, the user, a session, a turn or
   an agent run; states an observable outcome (something allowed, blocked, recorded, shown or
   sent); or states a guarantee or control (permission, path containment, hooks, redaction,
   approval), even when the text also names the component meant to provide it. The subject
   is *the module* only if the claim names a specific code unit (class, function, file, tool
   or API) and describes only that unit's own contract (inputs, outputs, structure), with no
   outcome the product can observe.
2. **If the text supports both readings, treat it as product behaviour** and judge it on the
   live path (§2.3).
3. **R4-Q1 is cited by evidence, not by opinion.** Cite `R4-Q1` in HumanDecisionNeeded on every
   row where the only code meeting the claim is tagged `REACH=LEGACY_ONLY`, whether the row is
   judged on the live path or at module level. Rows met by `LIVE` code, and rows with no code
   evidence, do not cite R4-Q1 for this reason.
4. **Record the other reading.** On a product-behaviour row met only by legacy code, add
   `ALSO_MODULE:<verdict>` to Notes, giving the verdict a module-level reading would have
   produced.

**Rule 3 reading for mixed rows (manager direction):** for any row met partly by LEGACY_ONLY
code and partly by LIVE or TEST_ONLY code, cite R4-Q1 only when LEGACY_ONLY code is the only
code meeting the claim on the product path; TEST_ONLY code does not meet a product claim.

## Other rules to apply

- **Named R4 questions** (HumanDecisionNeeded; cite instead of plain `R4` when the row turns
  on one): `R4-Q1` legacy in-process harness vs live Codex path; `R4-Q2` Codex engine never
  run through K-ENGINE-2 conformance; `R4-Q3` actor check on the legacy `status_transition`
  tool; `R4-Q4` whether the 2026-09-09 v3 four-role adoption (`9b005c23a`) is a governing
  amendment of SPEC §7/§13 and the persona and matrix contracts; `R4-Q5` Codex event payloads
  stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or translated
  (unamended K-ENGINE-4, SPEC §10.3). Several values are `;`-separated; `NO` stands alone.
- **CauseTag:** where the cause is the v3 four-role adoption, use exactly
  `OTHER:V3_ROLE_ADOPTION`. Report every other `OTHER:` token you use in your notes.
- **Done-declaration questions Q-01..Q-13** are CONTEXT: mention them in Notes only, never as
  HumanDecisionNeeded.
- **CONTEXT never changes a Disposition.** Agent dispositions are never rulings. Code and
  tests are evidence, not authority. Governing documents (App/Root DIRECTIVE, CONTRACT, SPEC,
  PRD, TYPES) and the invariant coverage register are **not audit targets**; they are
  GOVERNING only.
- **No reverse pass.** Extension units do not answer CLAIMED_BY / PARTIAL / NOT_MINE.
  If you find a defect in your own ledger *after* sealing, do not edit it: file
  `<STEM>_errata.csv` (CONVENTIONS §5.1 format) in your folder and validate it with
  `validate_ledger.py errata --ledger <STEM>_claims.csv <STEM>_errata.csv`.

## Output, validation and seal

- Write only inside your assigned folder under `<RUN>/R2/EXT/`.
- For each ledger stem: `<STEM>_claims.csv` (25-column header, rows, final `#END` record) and
  `<STEM>_notes.md` (CONVENTIONS §3 sections: census incl. split rate and SEE rows;
  least-confident rows with alternative readings; register-defect summary; direction and
  cause incl. every NONE_FOUND search; method friction; effort).
- Validate from `<APP_WORK>`:
  `python3 <RUN>/_scripts/validate_ledger.py ledger <your folder>/<STEM>_claims.csv`
  (your brief may add `--extension-index`). **Errors must be zero**; report warnings.
- Then compute `shasum -a 256` of each claims file. The ledger is now **sealed**; do not
  edit it afterwards.
- Last, write `<your folder>/RETURN.md` (this is the manager's completion signal) holding:
  per ledger the row count, top dispositions, validator RESULT line, SHA-256; anything the
  manager must resolve. Your final chat reply: at most 10 lines, same content.
