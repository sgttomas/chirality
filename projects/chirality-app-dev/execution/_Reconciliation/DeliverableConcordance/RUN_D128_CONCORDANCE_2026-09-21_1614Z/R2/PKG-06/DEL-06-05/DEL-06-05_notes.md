# DEL-06-05 Bash Governance and Timeout Policy: forward-pass notes

Frozen basis `00115c719`. The forward ledger is `DEL-06-05_claims.csv`. It is sealed after validation, and its SHA-256 is reported in the return.

## 1. Census

- **Rows:** 54 in total.
  - 49 rows cover the 31 indexed units (`CLM-001`..`CLM-031`). Every unit appears at least once.
  - 5 are run-local rows, `REGISTER-1`..`REGISTER-5`.
  - There are no `STATE-n` rows.
- **Split rate:** 4 of the 31 units were split (13%), producing 22 sub-rows:
  - `CLM-004`: 2 rows (the conditions table);
  - `CLM-009`: 16 rows, one per `DEL-06-05-REQ-001..016`;
  - `CLM-019`: 2 rows, the records list and `VER-001`;
  - `CLM-031`: 2 rows, `AC-002` and `VER-002`.
  - `V-SUBITEMS` is satisfied: `CLM-013` has `AC-001` on 1 row, `CLM-019` has `VER-001` in `.2`, and `CLM-031` has `AC-002` and `VER-002` in `.1` and `.2`.
- **SEE rows (counted separately):** 3. `CLM-007`, `CLM-014` and `CLM-020` repeat `CLM-001` verbatim and are all `STALE_SPECIFICATION`.

**By Disposition (sealed)**

| Disposition | Rows |
|---|---:|
| STALE_SPECIFICATION | 15 (3 of them are SEE rows) |
| AUTHORITY_CONFLICT | 15 |
| PARTIALLY_IMPLEMENTED | 8 |
| NOT_AUDITABLE | 5 |
| DOCUMENTED_UNIMPLEMENTED | 4 |
| IMPLEMENTED_DIFFERENTLY | 3 |
| ALIGNED | 2 |
| STALE_ASSESSMENT | 1 |
| REMAINING_STATE_MISMATCH | 1 |

**By ClaimType**

| ClaimType | Rows |
|---|---:|
| REQUIREMENT | 27 |
| STATE_ASSERTION | 8 |
| CONTEXT_CLAIM | 7 |
| ACCEPTANCE | 7 |
| REGISTER_DEFECT | 5 |

**HumanDecisionNeeded:** `R4-Q1` on 32 rows and `NO` on 22. No row cites `R4-Q2` or `R4-Q3`.

**PostReleaseBasis:** `NO` on every row.
- None of the cited App harness files, nor `delegated.ts`, `delegated-engine-adapter.ts` or `request-card.tsx`, is in `TOUCHED_PATHS.csv`.
- For `codex-supervisor.ts`, the relied-on lines were blamed with `git blame -L`:
  - lines 40, 104-112 and 718-735 blame to `95364569a`, `1cb09c09d`, `0ed1a1a7f`, `2f825f180` and `5c43b3a20`;
  - none of these is one of the four post-release commits.

## 2. Least-confident rows

- **`CLM-027` (LOW), recorded as `STALE_SPECIFICATION`.**
  - Alternative reading: `ALIGNED`. The sentence says only that the PRD "is listed as MATCH" in `_REFERENCES.md`, and that is literally true.
  - Why it was taken as stale: the sentence relies on the listing as the current source state, and that listing is stale (see REGISTER-1).
- **Timeout, capture, storage and preflight rows (MEDIUM): `CLM-009.6`/`.7`/`.8`/`.16`, `CLM-025` and `CLM-031.1`.**
  - These were judged on the live path, where they are `DOCUMENTED_UNIMPLEMENTED` or `PARTIALLY_IMPLEMENTED`.
  - Alternative reading: `AUTHORITY_CONFLICT`. D-GOV-43 forbids patching or vetoing Codex, which arguably undercuts K-BASH-1 as a whole.
  - Where the line was drawn:
    - rows whose posture D-GOV-43 item 4 contradicts directly got `AUTHORITY_CONFLICT`. These are default deny, the mode denials, hook fail-closed, and path containment.
    - rows describing mechanisms that are simply absent on the live path were judged under the reachability rule.
- **`CLM-009.10` interrupt, `ALIGNED` (MEDIUM).**
  - Alternative reading: `PARTIALLY_IMPLEMENTED`. Live interruption works at turn level (`turn/interrupt`), not per command.
  - The requirement is conditional on what the runner exposes, so turn-level interruption was accepted.
- **`CLM-009.14` product-owned events, `ALIGNED` (MEDIUM).**
  - Alternative reading: `PARTIALLY_IMPLEMENTED`. The Codex item type `commandExecution` is carried verbatim as `toolName`.
- **`CLM-021` Purpose, `NOT_AUDITABLE`.**
  - Alternative reading: `STALE_SPECIFICATION`. The claim "Chirality treats it as denied by default" can be checked and is false on the live path.
  - It was left `NOT_AUDITABLE` so that the worker does not resolve the conflict that is already recorded at `CLM-003`.

## 3. Register-defect summary

- **REGISTER-1:** the `_REFERENCES.md` MATCH hashes for CONTRACT, SPEC and PRD fail to reproduce (`HASH-RECOMPUTE@00115c719`).
  - My own recompute shows that REF-001 DIRECTIVE, REF-004 TYPES and REF-005 PLAN still reproduce.
  - The same MATCH claim is restated in:
    - SoW `CLM-001`/`007`/`014`/`020`, `CLM-004.1`, `CLM-006`, `CLM-027` and `CLM-030`;
    - `_DEPENDENCIES.md`, `_SEMANTIC_LENSING.md`, `Dependencies.csv` DEP-06-05-008, `MEMORY.md`, and the INSP-03 caveat.
- **REGISTER-2:** `_STATUS.md` says "Last Updated 2026-07-12", but its history has a 2026-07-19 D-APP-68 entry.
- **REGISTER-3:** `_DEPENDENCIES.md` says under "Declared Upstream" that no edges have been extracted, yet 8 extracted rows are ACTIVE. The evidence files named in `Dependencies.csv` (`Specification.md`, `Procedure.md`, `Datasheet.md`) no longer exist in the folder: the kit was consolidated into `ScopeOfWork.md`.
- **REGISTER-4:** `_CONTEXT.md` still describes the pre-D-GOV-43 topology ("daemon-owned" Bash, daemon conformance). The D-APP-127 application map shows `Revised=NO`.
- **REGISTER-5:** `_CONTEXT.md` (SCA-APP-001 alignment) still says "Claude Agent SDK / Anthropic remains the first concrete/current path".
- **Also noted, not given separate rows:**
  - The stale conflict table is recorded at `CLM-030`.
  - `_SEMANTIC.md` source lines embed machine-specific absolute paths.
  - The citation of a "root `AGENTS.md` managed-Bash rule" in SoW `CLM-031` points at a rule removed by `d5df483d7` (2026-08-02). This is recorded in the `CLM-031.1` Notes.

## 4. Direction and cause

- **CauseTags:**
  - `CODEX_SOLE_ENGINE` is the primary tag on 30 rows, with `CAUSE2:A2_TOPOLOGY` on the conflict rows;
  - `DOC_HYGIENE` 10;
  - `PRE_V3_DRIFT` 5;
  - `NATIVE_DELEGATION` 1;
  - `A2_TOPOLOGY` 1;
  - `NONE` 7.
- **Core finding:** the live path (`contracts/src/delegated.ts:322-330`) maps the App modes to Codex policies:
  - default/`ask` maps to on-request + workspace-write;
  - `readOnly` maps to read-only;
  - `workspaceWrite` maps to never + workspace-write;
  - `bypass` maps to danger-full-access.

  As a result, Codex's native shell is available by default and is governed only by the Codex sandbox and approval policy the user selects. Chirality adds no preflight, timeout, stream split or artifact store.
- **The conflict:** Root DIRECTIVE §7 (D-GOV-43 item 4) makes this the user's choice. App CONTRACT K-BASH-1, K-PERM-3/4/5/6, K-HOOK-1 and K-PATH-2/3 are unamended and are not named by D-GOV-43. These rows are therefore `AUTHORITY_CONFLICT` with `R4-Q1`, never `MR-11`.
- **CONTEXT consulted:** the v3 done-declaration candidate, DONE-05, which is marked "SUPERSEDED BY D-GOV-43 items 4 and 10". It is noted only, as CONTEXT, and cited on no row.
- **`NONE_FOUND` searches:**
  - `_REGISTER.md` was searched for Bash, shell and sandbox. The rows found were D-APP-04, D-APP-05, D-APP-43, D-APP-68, D-APP-84 (H1 grants no Bash; Bash doctrine separately gated), D-APP-86 and D-APP-127.
  - The CONTEXT sources searched were the done declaration and the list of v3 steers.
  - No record explains:
    - `CLM-017` step 3 left unrevised against REQ-016 (`CLM-017`);
    - the missing 600000 ms test (`CLM-031.2`);
    - the header-date lag (`REGISTER-2`);
    - the dependency prose and evidence-file drift (`REGISTER-3`).

## 5. Method friction

- **MR-4 against tables.**
  - `CLM-003` (Attributes), `CLM-008` (Scope), `CLM-018`/`CLM-022`/`CLM-024`/`CLM-029` and the REQ rows all restate the same default-deny posture.
  - Using `SEE` everywhere would force every REQ into the disposition of a mixed table.
  - I used `SEE` only for verbatim repeats (the D-APP-56 note) and gave each REQ its own evidence.
  - Proposed revision: allow MR-4 to anchor on the first REQ-numbered statement rather than the first unit.
- **The line between AUTHORITY_CONFLICT and live-path judgment** is not crisp when a ruling, rather than a code choice, removes the mechanism. See §2. Proposed revision: add guidance for "mechanism detail under a posture-level conflict".
- **Reference-hash drift:** `REFERENCE_HASHES.csv` covers only CONTRACT, SPEC and PRD. I recomputed DIRECTIVE, TYPES and PLAN myself to judge `CLM-006`.

## 6. Effort

- **Files read:** about 25, including:
  - the SoW and the deliverable carriers in full;
  - the INSP-03 assessment;
  - line ranges of `tool-shell-policy.ts`, `permission-overlay.ts` and its tests, `chirality-hooks.test.ts`, `tool-evidence.ts`, `codex-supervisor.ts`, `delegated.ts` and `delegated-engine-adapter.ts`;
  - the Root/App CONTRACT and DIRECTIVE excerpts, the register rows, and the done-declaration excerpt.
- **Context budget:** moderate, not tight.
