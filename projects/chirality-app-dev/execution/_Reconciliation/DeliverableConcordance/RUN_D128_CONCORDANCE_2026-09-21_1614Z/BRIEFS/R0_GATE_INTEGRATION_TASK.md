# Brief — R0 gate integration TASK: adopted conventions, validator v2, extension index

**Role.** TASK (Type 2). You do not delegate.

**Run.** `RUN_D128_CONCORDANCE_2026-09-21_1614Z`.

**Placeholders**, supplied at dispatch:

- `<FROZEN_TREE>`: read-only checkout at `00115c719`.
- `<RUN>`: the run folder in the working repository.
- `<APP_WORK>`: the working repository's `projects/chirality-app-dev`.

## Authority

The owner ruled the R0 gate on 2026-09-21. It is being transcribed as D-APP-129.

- **A.** Adopt every convention verdict in `<RUN>/R0_CALIBRATION/R0_CALIBRATION_REPORT.md`
  §7 (tables 7.1 and 7.2) exactly as written. `ADOPT` keeps the candidate rule;
  `REVISE: <text>` replaces or adds that text. This brings in the new disposition
  `RETIRED_BY_RULING`, the `REACH=` tag, the `_errata.csv` file, `CAUSE2:`,
  `LIFECYCLE_GATE_PENDING`, the `CTX:`/`GOV:` prefixes, `SEE:` rows, and the new MR-10
  tokens.
- **B.** R2 proceeds with the v3 done-declaration candidate as CONTEXT only. Its 13
  questions (Q-01..Q-13) go to R4.
- **C.** R2 follows the proposal:
  - one WORKING_ITEMS manager per package, at most 3 concurrent managers, each with at
    most 4 concurrent children;
  - a per-manager evidence pack;
  - the report §9 wave order and double-blind rule;
  - three named R4 questions that rows cite in `HumanDecisionNeeded`:
    - `R4-Q1`: the legacy in-process harness versus the live Codex path, i.e. whether
      retained harness code is history, compatibility or obligation (K-PATH, K-ROOT,
      K-HOOK, SPEC §15.2 unamended for D-GOV-43);
    - `R4-Q2`: the Codex engine never run through the K-ENGINE-2 conformance suite;
    - `R4-Q3`: the actor check on the legacy `status_transition` tool, which the agent
      supplies itself.
- **D. Scope extension.** Items 3–7 below. Governing documents (CONTRACT, SPEC, PRD,
  TYPES, DIRECTIVE) and the invariant coverage register are **not** audit targets. They
  remain GOVERNING only.

## Deliverables

All deliverables go under `<RUN>/`. Do not modify `CONVENTIONS_CANDIDATE.md`, the R0
outputs, or `_scripts/claim_index.py`.

### 1. `CONVENTIONS.md`: the adopted, self-contained R2 rulebook

- It is the candidate text with every §7 verdict integrated verbatim or near-verbatim.
- Mark each rule's origin, e.g. `(MR-8 REVISE, R0 §7.1)`.
- Integrate the B and C items, including the R4-Qn tokens.
- Add **§8 Scope-extension units** (item D):

  | Item | Unit key | Audit question | Source |
  |---|---|---|---|
  | 3 | `DEC:D-APP-nnn` for each register row D-APP-86..D-APP-127 in state `RULED` | Did the ruling's stated effect land in code or corpus at the frozen basis? | Register row + ruling record |
  | 4 | `DOC:<DOCID>#<n>` for each `##`/`###` section of `docs/BUILD_AND_RELEASE.md` (`BUILDREL`), `docs/RELEASE_QUALITY_GATES.md` (`RQGATES`), `docs/VALIDATION_STRATEGY.md` (`VALSTRAT`), `docs/RELEASE_QUALITY_RUNBOOK.md` (`RQRUN`), `docs/harness/reliance_boundary_register.md` (`RELIANCE`) | Does the section match what shipped? `.github/workflows/{harness-premerge,desktop-release-template}.yml` and release AgentRuns records are evidence only | Section text |
  | 5 | `SOW:SOW-nnn` for each scope-ledger row in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Does the row map to at least one live deliverable, and to code or an explicit deferral? | Ledger row |
  | 6 | `DOC:PRODAGENTS#<n>` for sections of `instructions/AGENTS.md` | Is it accurate about product behavior? **Audit-only.** Repairs route to Root per packet Δ10 | Section text |
  | 7 | `DOC:<DOCID>#<n>` for sections of `frontend/docs/harness/*.md` (DOCID = uppercase file stem, e.g. `RUNTIME_ENGINE_CONTRACT`) | Is the developer documentation accurate? **Audit-only** | Section text |

  Use the same ledger schema. `PackageID` is `EXT`. `DeliverableID` is the owning
  deliverable when one is evident, else `NONE`. Ledger file names:
  - `DEC_claims.csv`
  - `SOW_claims.csv`
  - `DOC-<DOCID>_claims.csv`

- Add **§9 Evidence pack.** Contents per report §9:
  - the post-release touched-path list with line ranges;
  - the static reachability map;
  - hash recomputes of CONTRACT, SPEC and PRD versus each deliverable's `_REFERENCES.md`;
  - per-deliverable decision-register and D-GOV hits;
  - the D-APP-127 application map.

  Specify each item's file name and format so managers build it identically.

### 2. `_scripts/validate_ledger.py` v2

Edit it in place, keeping the v1 behavior that still applies. It must:

- parse CSV records, not lines;
- enforce all §7 mechanical rules:
  - `RETIRED_BY_RULING` in the vocabulary;
  - `LatestDecision` pattern allowing `D-GOV-nn`;
  - `CTX:`/`GOV:` prefix on `DirectionEvidence` for non-ALIGNED rows, unless the value is
    `NONE_FOUND`;
  - an error on a `CONTEXT_CLAIM` row whose tier is not `NOT_APPLICABLE`;
  - a `REACH=LIVE|LEGACY_ONLY|TEST_ONLY` tag whenever `ImplementationEvidence` cites a
    code path;
  - `LIFECYCLE_GATE_PENDING` as a cause;
  - `HumanDecisionNeeded` accepting `R4-Q1..R4-Q3`;
- add an `errata` mode validating `_errata.csv`;
- accept the extension keys and ledger file names;
- check coverage for extension ledgers against `R1_INVENTORY/EXTENSION_INDEX.csv`.

Add `_scripts/test_validate_ledger.py`: a pytest with passing and failing fixtures for
every rule. Run it; it must pass.

### 3. `_scripts/extension_index.py` → `R1_INVENTORY/EXTENSION_INDEX.csv`

- Deterministic, reading `<FROZEN_TREE>`.
- Header: `UnitKey,Item,SourcePath,SourceLine,Label`, then `#END`.
- Covers every item 3–7 unit.
- Report counts per item.

### 4. `R0_GATE_INTEGRATION_NOTES.md`

- A mapping table: §7 row → where it landed in `CONVENTIONS.md` → validator rule, or
  "prose only".
- Any §7 text you could not integrate mechanically, with the reason.
- The pytest result.
- The result of running validator v2 over the R0 calibration ledgers. They are expected to
  fail some new rules: summarize the counts only. **Do not edit R0 outputs.**

## Rules

- Write only the four items above.
- No git, installs or network. Pytest via `python3 -m pytest` is allowed.
- No absolute machine paths in outputs.
- Read deliverables only from `<FROZEN_TREE>`.

## Return

At most 12 lines:

- file paths and SHA-256 of each output;
- extension unit counts per item;
- pytest result;
- the count of R0-ledger failures under v2, by rule;
- anything not integrated.
