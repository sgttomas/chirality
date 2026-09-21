# RUN_D128 — Conventions (adopted R2 rulebook)

> **Status: ADOPTED** by the owner's R0 gate ruling of 2026-09-21, recorded as
> **D-APP-129** (`execution/_Coordination/_DECISIONS/D-APP-129_RULING_R0_GATE_RUN_D128_2026-09-21.md`). Ruling items: **A** adopt every verdict in
> `R0_CALIBRATION/R0_CALIBRATION_REPORT.md` §7 as written; **B** the v3 done-declaration
> candidate is CONTEXT only; **C** the R2 operating plan; **D** the scope extension.
> This file is self-contained: R2 workers need no other convention text.
> `CONVENTIONS_CANDIDATE.md` is kept unchanged as the R0 record.
>
> **Origin marks.** Every rule carries its origin:
> - `(CAND §n)`: candidate rule carried unchanged (plan §6–§7 as amended by packet Δ1–Δ11);
> - `(<rule> ADOPT, R0 §7.n)` / `(<rule> REVISE, R0 §7.n)`: a §7 verdict under ruling A;
>   REVISE text is integrated verbatim or near-verbatim;
> - `(Ruling B|C|D)`: the other ruling items;
> - `[INTEG]`: an integration detail added by the R0 gate integration TASK so that a ruled
>   rule can be applied or checked the same way by every worker. It is not itself ruled;
>   HELP_HUMAN may strike it. See `R0_GATE_INTEGRATION_NOTES.md`.

## 1. What you are comparing (the four-way picture) (CAND §1)

For each audit unit, establish:

1. **What the deliverable says.** The claim text and its declared state.
2. **What the implementation does.** App `frontend/**` and
   `projects/chirality-runtime/{packages,tests}/**` at the frozen basis `00115c719`.
3. **What recorded direction says.**
   - Only CONTEXT sources from `RUN_BASIS.md` §5 may explain a divergence in CONTEXT terms;
     a GOVERNING ruling that itself explains it is cited with `GOV:` (§2.3,
     DirectionEvidence).
   - CONTEXT may explain a divergence. It never changes the Disposition.
   - The v3 done-declaration candidate (`R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md`)
     is **CONTEXT only** for R2. Its questions Q-01..Q-13 are carried to R4 and are not
     answered or cited as rulings by R2 rows. (Ruling B)
4. **Whether the divergence is unrecorded judgment.** When code diverges and neither the
   decision register nor a CONTEXT record explains it, say so:
   `CauseTag = UNRECORDED_JUDGMENT` (§4).

Code and tests are evidence, not authority. An agent disposition is never a ruling.

**Authority handling (MR-11 REVISE, R0 §7.1).** Deliverable text is judged against the
GOVERNING map.

- Apply MR-11 (a ruled decision stands over older, untranscribed corpus wording) **only
  when the ruling explicitly addresses the clause or the deliverable.** Cite the ruling in
  `LatestDecision` and classify the stale wording per MR-8.
- Where DIRECTIVE §0's authority order resolves a disagreement among GOVERNING sources,
  apply it, cite both sources, and do not use `AUTHORITY_CONFLICT`.
- Where a ruling undercuts an unamended GOVERNING clause without naming it, or two
  GOVERNING texts conflict and the authority order does not resolve it, the row is
  `AUTHORITY_CONFLICT` with `HumanDecisionNeeded = R4` (or the matching `R4-Qn`, §2.4).
  It is never resolved by the worker.

## 2. Ledger file `<DEL-ID>_claims.csv`

### 2.1 Format (25-column schema ADOPT, R0 §7.2)

- **Format.** UTF-8 CSV with a header row, then data rows, then a final record containing
  exactly `#END`. Fields may contain quoted newlines and commas: the validator parses CSV
  records, not lines (Validator REVISE, R0 §7.2).
- **Paths.** Never write an absolute path. Use repo-relative paths, e.g.
  `projects/chirality-runtime/packages/core/src/x.ts:120`.
- **Header**, exactly 25 columns:

`ClaimKey,ClaimID,PackageID,DeliverableID,ClaimType,NormativeSource,AuthorityTier,LatestDecision,DeclaredState,RecordedRemaining,RemainingSource,RemainingGate,MechanicallyUnblocked,ImplementationEvidence,VerificationEvidence,LifecycleState,AssessmentEvidence,DirectionEvidence,PostReleaseBasis,Disposition,CauseTag,Confidence,RemainingWork,HumanDecisionNeeded,Notes`

Extension ledgers (§8) use the same header and different key and file names.

### 2.2 ClaimKey, splitting and run-local keys

**`ClaimKey`** is `DEL-xx-yy#<local>`, where `<local>` is the `LocalID` from
`R1_INVENTORY/CLAIM_INDEX.csv`. `ClaimID` is the local part of the key. (CAND §2)

- **Coverage.** Every indexed unit for your deliverable appears at least once. (CAND §2)
- **Splitting.** (ClaimKey splitting REVISE, R0 §7.2) Split one unit into sub-rows
  `…#CLM-007.1`, `.2`, … **only when the unit holds separately numbered REQ-, AC- or VER-
  items, or a table of independently dispositionable rows.** Report your split rate in the
  notes. [A0] The claim index's `SubItems` column lists the REQ/AC/VER items defined inside
  each unit (120 units, 208 items; `RUN_BASIS.md` Addendum 1). A unit listing k ≥ 2 items
  needs at least k rows (validator `V-SUBITEMS`); give each listed item its own `.n` row and
  name the item in Notes.
- **Run-local keys.** Rows the index does not know get run-local keys, **numbered per
  deliverable**:
  - `REGISTER-n` for register defects (MR-5);
  - `STATE-n` for state assertions outside indexed units.
- **Repeated statements (MR-4 REVISE, R0 §7.1).** When the same normative statement recurs
  across SoW sections, disposition it once on the earliest indexed unit. Each later unit
  gets a row with the same Disposition and `SEE:<ClaimKey>` in Notes. The census counts
  SEE rows separately. [INTEG] The token is written exactly `SEE:<ClaimKey>` (for example
  `SEE:DEL-03-01#CLM-004`); the validator checks that the target row exists in the same
  ledger and carries the same Disposition. Plain prose "see …" is not a SEE row.

### 2.3 Column rules

| Column | Rule |
|---|---|
| `ClaimKey`, `ClaimID` | §2.2. (CAND §2) |
| `PackageID`, `DeliverableID` | e.g. `PKG-03`, `DEL-03-01`. Extension ledgers: §8. (CAND §2) |
| `ClaimType` | `REQUIREMENT` · `ACCEPTANCE` · `EXCLUSION` · `CONTEXT_CLAIM` (references, provenance, conflict tables, method notes; non-normative) · `STATE_ASSERTION` (dated reconciliation/carrier notes and Remaining prose asserting current state) · `REMAINING_WORK` · `REGISTER_DEFECT` (MR-5). (CAND §2; STATE_ASSERTION ADOPT, R0 §7.2) **`CONTEXT_CLAIM` rows that make a checkable, now-false factual assertion may take `STALE_SPECIFICATION`. Otherwise use `NOT_AUDITABLE`, with the reason in Notes.** (CONTEXT_CLAIM REVISE, R0 §7.2) |
| `NormativeSource` | Where the claim's authority comes from: SoW section plus the `Source` cell's references (PRD §, CONTRACT K-…, decision ID). (CAND §2) |
| `AuthorityTier` | (AuthorityTier REVISE, R0 §7.2) Use `GOVERNANCE_INVARIANT` when the claim restates App or Root DIRECTIVE, CONTRACT, SPEC or TYPES, or a D-GOV rule. Use `PRD` only when the highest source restated is `PRD.md`. Use `LOCAL_DESIGN` for a decomposition, SCA or deliverable-level choice. Use `NOT_APPLICABLE` for `CONTEXT_CLAIM`, and for `STATE_ASSERTION` or `REGISTER_DEFECT` rows that restate no normative source. **The validator errors on `CONTEXT_CLAIM` with any other tier.** [INTEG] The validator also errors on `NOT_APPLICABLE` for `REQUIREMENT`, `ACCEPTANCE` and `EXCLUSION` rows, which the revised rule gives no NOT_APPLICABLE case. |
| `LatestDecision` | (MR-7 REVISE, R0 §7.1) `D-APP-nn` or `D-GOV-nn`, or either with ` (context)`, or `NONE_FOUND`. Governing when the decision governs the claim; `(context)` when it only touches it. One value per row. |
| `DeclaredState` | What the deliverable asserts is true now (short). (CAND §2) |
| `RecordedRemaining`, `RemainingSource`, `RemainingGate` | For REM rows: verbatim item, its source, and verbatim gate suffixes concatenated (MR-6). Otherwise `NONE_RECORDED`. (CAND §2) |
| `MechanicallyUnblocked` | §2.5. (`MechanicallyUnblocked` rename ADOPT, R0 §7.2) |
| `ImplementationEvidence` | Repo-relative path + symbol/line; or `documentary claim` + exact doc sections (MR-10); or `NONE_FOUND` after a stated search. (CAND §2) **Reachability** (ImplementationEvidence reachability REVISE, R0 §7.2): for every row whose evidence is code, append `REACH=LIVE`, `REACH=LEGACY_ONLY` or `REACH=TEST_ONLY` to ImplementationEvidence, determined statically from a product entry point. A requirement met only on a `LEGACY_ONLY` path is judged on the live path: `PARTIALLY_IMPLEMENTED` if the live path covers part of it, `IMPLEMENTED_DIFFERENTLY` if the live path uses another mechanism, `DOCUMENTED_UNIMPLEMENTED` if the live path lacks it. A claim about the retained module itself is judged at module level and carries the REACH tag. [INTEG] Use the evidence pack's `REACHABILITY.csv` (§9) as the static map; when several code paths are cited with different reach, tag each (`… a.ts:10 REACH=LIVE; b.ts:4 REACH=LEGACY_ONLY`). A value that begins `NONE_FOUND` (a search statement) needs no tag. [A0] Code reached from no product entry takes `REACH=LEGACY_ONLY` with `UNREACHED` in Notes (`RUN_BASIS.md` Addendum 1). |
| `VerificationEvidence` | `GATE-TRANSCRIPT(APP@00115c719)` or `GATE-TRANSCRIPT(RUNTIME@00115c719)` **plus** the named test file and case; or an MR-10 token (§2.4); or `NONE_FOUND`. Never run a test suite. (CAND §2; MR-3 replacement ADOPT, R0 §7.1) |
| `LifecycleState` | From `_STATUS.md` (`IN_PROGRESS` / `OPEN`). (CAND §2) |
| `AssessmentEvidence` | (MR-1 REVISE, R0 §7.1) AssessmentEvidence carries exactly one of `OVERTAKEN` · `STILL CURRENT` · `NOT APPLICABLE`, and no other token's phrase anywhere in the cell. `NOT APPLICABLE` only when the INSP-03 assessment reached no conclusion on this claim. A recorded MATCH or PASS that no longer reproduces at the frozen basis is `OVERTAKEN`. `STALE_ASSESSMENT` is reserved for rows where the overtaken conclusion is the operative defect. Where the assessment predates the SoW, cite the old REQ-ID it discussed, or write "no direct conclusion" (MR-9 ADOPT, R0 §7.1). |
| `DirectionEvidence` | (DirectionEvidence REVISE, R0 §7.2) DirectionEvidence cites the explaining record with a class prefix: `CTX:<path §>` for a CONTEXT source, or `GOV:<ruling>` when a GOVERNING ruling itself explains the divergence. Before writing `NONE_FOUND`, the worker must search `_DECISIONS/_REGISTER.md` and the CONTEXT sources, and name the search in Notes. CONTEXT still never changes a Disposition. [INTEG] On `ALIGNED` and `NOT_AUDITABLE` rows (no divergence to explain) write `NOT_APPLICABLE` (CAND §2). Every other row starts `CTX:` or `GOV:`, or is exactly `NONE_FOUND`. Several records: `CTX:a; GOV:b` (the first must carry a prefix; give each one its own). |
| `PostReleaseBasis` | (PostReleaseBasis REVISE, R0 §7.2) The manager supplies, in each brief, the paths touched by `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a` (§9 `TOUCHED_PATHS.csv`). For a cited file on that list, the worker runs read-only `git -C <frozen> blame -L` on the relied-on lines, and sets `YES` if any line blames to one of the four commits. Otherwise `NO`. Line citations inside touched files are taken at the frozen basis. [A0] Git permitted to children is read-only `git -C <frozen> log`, `show` and `blame -L` against the frozen tree only (`RUN_BASIS.md` Addendum 1); nothing against the working repository. |
| `Disposition` | §2.6. |
| `CauseTag` | §4. `NONE` only on `ALIGNED` and `NOT_AUDITABLE` rows. (CAND §2) |
| `Confidence` | `HIGH` · `MEDIUM` · `LOW`. LOW rows must contain `LEAST-CONFIDENT:` in Notes, with the alternative reading. (CAND §2) |
| `RemainingWork` | The evidence-based residual, `NONE_OBSERVED`, or `UNKNOWN`. (CAND §2) |
| `HumanDecisionNeeded` | §2.4. |
| `Notes` | Short. Self-flags, cross-deliverable observations, method friction, and the tokens `SEE:`, `CAUSE2:`, `MOOT:`, `LEAST-CONFIDENT:`. (CAND §2) |

### 2.4 Token vocabularies

**HumanDecisionNeeded** (CAND §2; Ruling C):

- `NO`;
- an existing decision ID, `D-APP-nn` or `D-GOV-nn` [INTEG: D-GOV per MR-7];
- `R4`: needs an owner ruling not yet framed;
- one of the **named R4 questions** (Ruling C; R4-Q4, R4-Q5 and R4-Q6 added by Addenda 4, 7 and 9). Cite the named question instead of
  plain `R4` whenever the row turns on it:
  - `R4-Q1`: the legacy in-process harness versus the live Codex path, i.e. whether retained
    harness code is history, compatibility or obligation (K-PATH, K-ROOT, K-HOOK, SPEC
    §15.2 unamended for D-GOV-43);
  - `R4-Q2`: the Codex engine never run through the K-ENGINE-2 conformance suite;
  - `R4-Q3`: the actor check on the legacy `status_transition` tool, which the agent
    supplies itself.
  - `R4-Q4` [A0: owner direction `r2_tiebreak_q4`, RUN_BASIS Addendum 4]: whether the
    2026-09-09 v3 four-role adoption (`9b005c23a`; alias map, default role, retired agent
    matrix and Pipeline surface, new agent-file header format) is a governing amendment of
    SPEC §7 and §13 and the persona and matrix contracts, which were not amended.
  - `R4-Q5` [A0: owner direction `r2_r4q5`, RUN_BASIS Addendum 7]: Codex event payloads,
    stored as received (amended CONTRACT K-EVENT-1/K-EVENT-6, SPEC §11) or translated
    (unamended K-ENGINE-4, SPEC §10.3)?
  - `R4-Q6` [A0: owner direction `r2_r4q6_answer`, RUN_BASIS Addendum 9]: do the unamended App
    DIRECTIVE clauses (§2.8, §2.10, §4.1, §4.2) and CONTRACT K-PERM-1/K-PERM-6 still bind the
    Codex-hosted App, or did D-GOV-43 supersede them? Covers the Anthropic API-key UI, the live
    "Full access" option and the unfiltered `~/.codex` link. The owner has answered it
    (Addendum 9), but the answer becomes GOVERNING only when the R4 ruling records it. Until then,
    dispositions follow §1 and §2.6 unchanged.
- [INTEG] Several values are `;`-separated (e.g. `D-APP-117; R4-Q1`); `NO` stands alone.
  Done-declaration questions Q-01..Q-13 are not HumanDecisionNeeded tokens (Ruling B:
  CONTEXT only); mention them in Notes if relevant.

**Legacy-versus-live subject test (R4-Q1)** [A0: owner direction `r2_r4q1_subject_test`,
RUN_BASIS Addendum 6]. It makes precise the §2.3 ImplementationEvidence rule on module-level
claims:

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

**VerificationEvidence tokens** (MR-10 REVISE, R0 §7.1). Non-behavioural claims use:

- `DOC-BASIS(D-APP-nn)`; `RUN-INSPECTION@00115c719`; `RULING-RECORD(D-APP-nn)`;
  `SNAPSHOT+LIVE-REVERIFY(<snapshot>)` (CAND §2);
- **new:** `HASH-RECOMPUTE@<sha>` (a recomputed file hash) and `REACHABILITY(static)@<sha>`
  (entry point → module import chain).
- [INTEG] `DOC-BASIS` and `RULING-RECORD` also accept `D-GOV-nn` (MR-7). Every non-empty
  VerificationEvidence carries at least one recognised token or `NONE_FOUND`.

### 2.5 MechanicallyUnblocked (CAND §2; MR-2 ADOPT and MR-6 REVISE, R0 §7.1)

Meaningful only on `REMAINING_WORK` rows:

- `YES`: every written gate is verified satisfied at the source the gate itself names, and
  no ACTIVE PREREQUISITE dependency named in the item's `Depends` is pending.
- `NO`: at least one gate or dependency is unsatisfied.
- `UNKNOWN`: cross-project gate status is not stated on an App surface.
- **MR-6 additions:** For a gate phrased as code landing on the App production path, App
  code at the frozen basis is an App surface. Runtime lifecycle or gate status still needs
  an App carrier, else `UNKNOWN`. A gate whose premise a GOVERNING ruling retired is `NO`,
  with `MOOT:<ruling>` in Notes (e.g. `MOOT:D-APP-127`).
- On every other row: `NO` (MR-2). `YES` is never permission to execute.
- Gates are copied verbatim; cross-project status comes only from App surfaces (MR-6).

### 2.6 Disposition vocabulary (CAND §2 plan §7; MR-8 REVISE, R0 §7.1)

- `ALIGNED`
- `IMPLEMENTED_UNDOCUMENTED`
- `DOCUMENTED_UNIMPLEMENTED`
- `PARTIALLY_IMPLEMENTED`
- `IMPLEMENTED_DIFFERENTLY`
- `STALE_SPECIFICATION`: (i) text flatly asserting a now-false state; repair-shaped.
- `STALE_ASSESSMENT`: only where the overtaken conclusion is the operative defect
  (`AssessmentEvidence = OVERTAKEN`; MR-1).
- `STALE_VERIFICATION`
- `ACCEPTED_DIVERGENCE`: (ii) text acknowledging the gate where a GOVERNING ruling permits
  the difference. CONTEXT alone never makes a row ACCEPTED_DIVERGENCE.
- **`RETIRED_BY_RULING`** (iii, new): a GOVERNING ruling names the deliverable or item
  retired and preserves its text as history. It applies to every file in the preserved set,
  and one whole-section row per ruling is allowed. Text outside the preserved set stays
  under MR-11. `LatestDecision` names that ruling (governing, not `(context)`).
- `LIFECYCLE_REASSESSMENT_REQUIRED`
- `REMAINING_STATE_MISMATCH`
- `DEFERRED_AGENT_WORKFLOW`: agent-instruction or workflow matter; evidence only (Δ10).
- `AUTHORITY_CONFLICT`: never choose between conflicting sources (MR-11, §1).
- `UNKNOWN`
- `NOT_AUDITABLE`: `CONTEXT_CLAIM` rows with nothing to check; say why in Notes.
  (NOT_AUDITABLE ADOPT, R0 §7.2)

**Absence is not evidence of absence** [A0: owner direction `r2_absence_not_evidence`, RUN_BASIS
Addendum 10]. A claim may be about whether an action or event happened outside the code:
notarization, signing, publication, a release or CI job run, an attestation, a manual or human
step, or a credentialed operation. If the only evidence is that no record exists within the
evidence roots:
- the Disposition is `UNKNOWN`, never `DOCUMENTED_UNIMPLEMENTED`, and never wording such as
  "never ran";
- Notes carry `OWNER_CHECK: <one-line question for the owner>`.

Positive evidence either way counts as usual, for example a failed job log or a script that
hard-fails. Code-presence findings are unaffected: whether code exists and is reached is judged
from the code.

MR-8 (iv): a claim true only of a recorded snapshot (for example "REF-006 MATCH at v23") is
a REGISTER row (MR-5), not `STALE_SPECIFICATION`.

**Tie-break between `STALE_SPECIFICATION` and `REMAINING_STATE_MISMATCH`** [A0: owner direction
`r2_tiebreak_adopt`, RUN_BASIS Addendum 5]:

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

### 2.7 Register defects (MR-5 REVISE, R0 §7.1)

Register defects become `REGISTER-n` rows (`ClaimType = REGISTER_DEFECT`).
REGISTER_DEFECT rows take `REMAINING_STATE_MISMATCH` for metadata lag, or
`STALE_SPECIFICATION` when the register asserts a now-false fact. Each `_REFERENCES.md`
MATCH hash that does not reproduce at the frozen basis is one REGISTER row per deliverable,
and SoW rows restating it cite that key. [INTEG] Use `HASH-RECOMPUTE@00115c719` with the
§9 `REFERENCE_HASHES.csv` row as VerificationEvidence.

## 3. Notes file `<DEL-ID>_notes.md` (CAND §3)

Sections:

1. **Census:** rows by ClaimType and Disposition; split rate; **SEE rows counted
   separately** (MR-4); **sealed and errata-applied figures side by side** when an errata
   file exists (Reverse pass REVISE, R0 §7.2).
2. **Least-confident rows,** each with the alternative reading (mandatory).
3. **Register-defect summary.**
4. **Direction and cause:** the main CauseTags, any `CAUSE2:` secondaries, the CONTEXT
   records used, and the register/CONTEXT searches behind each `NONE_FOUND`.
5. **Method friction:** any rule here that did not fit, with a proposed revision.
6. **Effort:** approximate files read, and whether the context budget was tight.

## 4. CauseTag vocabulary (CAND §4; CauseTag REVISE, R0 §7.2; OTHER ADOPT, R0 §7.2)

`NONE` · `CODEX_SOLE_ENGINE` (Codex is the only engine; Claude/Anthropic/Pi paths retired
or demoted) · `A2_TOPOLOGY` (D-GOV-43: App-owned Runtime service; daemon/LaunchAgent/per-root
homes retired) · `RUNTIME_EXTRACTION` (behavior moved to `projects/chirality-runtime`) ·
`SHELL_REDESIGN` (SCA-APP-010 dialogue-centred shell / woven workspace) ·
`CREDENTIAL_CUSTODY` (Codex owns login and credentials; D-APP-126/127) ·
`FACADE_DEPRECATION` (`harness-contract` → `runtime-contracts`) · `NATIVE_DELEGATION`
(Codex-native descendants versus the Type 2 bridge) · `V3_RELEASE_SCOPE` (explicitly in or
out of scope for v3 per CONTEXT direction) · `CARRIER_PROPAGATION` (an agent-propagated
note that is stale or partial) · `PRE_V3_DRIFT` (divergence already present before
2026-08-22) · `DOC_HYGIENE` (metadata/register/reference defects) · **`LIFECYCLE_GATE_PENDING`**
(new: a normal open human gate) · `UNRECORDED_JUDGMENT` · `OTHER:<TOKEN>` (new cause; the
manager reports every OTHER token).

Precedence (REVISE text):

- CauseTag names the mechanism.
- A divergence that predates 2026-08-22 is `PRE_V3_DRIFT` unless a named v3 mechanism
  applies.
- `UNRECORDED_JUDGMENT` is used only when no vocabulary mechanism fits **and** neither the
  decision register nor CONTEXT records the direction. [INTEG] Such a row therefore has
  `DirectionEvidence = NONE_FOUND`.
- With mixed causes, put the primary in CauseTag and the secondary as `CAUSE2:<tag>` in
  Notes. [INTEG] The secondary is a vocabulary tag other than `NONE` and differs from the
  primary.

## 5. Reverse pass, errata and capability files

### 5.1 Two sealed passes (Reverse pass REVISE, R0 §7.2; CAND §5)

1. **Forward pass.**
   - Write `<DEL-ID>_claims.csv` (with `#END`) and `<DEL-ID>_notes.md`.
   - Run the validator (§6).
   - Record `sha256sum` of the claims file in your return. The forward ledger is then
     **sealed**: do not edit it afterwards.
2. **Reverse pass.**
   - Only after sealing, open the capability file you are given.
   - Write `<DEL-ID>_reverse.csv`, then `#END`. Header:
     `CapabilityID,Response,ClaimKey,Rationale`. Answer every row:
     - `CLAIMED_BY` + the key of one of your claims that owns it;
     - `PARTIAL` + the key that covers part of it;
     - `NOT_MINE` with empty `ClaimKey`.
   - If the reverse pass shows a forward row was wrong, **do not edit the sealed ledger.**
     Forward-row corrections found in pass 2 are written to `<DEL-ID>_errata.csv`
     (`ClaimKey,Field,SealedValue,ProposedValue,Evidence`, ending `#END`). The verifier
     rechecks every errata row, and the census reports sealed and errata-applied figures
     side by side. Explanations stay in `<DEL-ID>_reverse_notes.md`.
   - [INTEG] One errata row per (ClaimKey, Field). `Field` is any ledger column except
     `ClaimKey` and `ClaimID`. `SealedValue` is copied exactly from the sealed ledger.
     A **missing** forward row (a coverage gap) cannot be expressed as an erratum; describe
     it in reverse_notes for the manager (see integration notes).
   - Validate with `validate_ledger.py errata <DEL-ID>_errata.csv`; the sealed ledger in the
     same folder is found automatically.

Resuming the same worker for pass 2 is the default mechanism (R0 §7.2 evidence).

### 5.2 Capability file `<AREA>_capabilities.csv` (Capability file REVISE, R0 §7.2; CAND §5)

Written by the reverse-pass worker. Header:

`CapabilityID,Area,Capability,Paths,EntryPoints,CoveringTests,PostReleaseBasis,Notes`

- `CapabilityID`: `CAP-<AREA>-nnn`.
- **Granularity:** one row per user- or system-observable behavior, or contract surface,
  that a deliverable could plausibly own. Not per file or per function. Target 20–60 rows
  per area. **Per-function rows fold into their behaviour.**
- **Each capability states its live/legacy/test-only reach and its enabled or disabled
  state at the frozen basis, verified from code, not inferred from names.** [INTEG] Written
  in `Notes` as `REACH=LIVE|LEGACY_ONLY|TEST_ONLY` and `STATE=ENABLED|DISABLED` (header
  unchanged).
- The file has **no owner column**.
- End with `#END`.

## 6. Validator (Validator REVISE, R0 §7.2; CAND §6)

`_scripts/validate_ledger.py` v2 parses CSV records rather than lines, so quoted newlines
are safe. It enforces the mechanical rules of §2–§5 and §8, prints each message with a rule
ID, and ends with a `RULES` count line and `RESULT PASS|FAIL`. Run it from
`projects/chirality-app-dev`:

```
python3 <RUN>/_scripts/validate_ledger.py ledger  <files…>_claims.csv
python3 <RUN>/_scripts/validate_ledger.py errata  <files…>_errata.csv
python3 <RUN>/_scripts/validate_ledger.py reverse --capabilities <cap.csv> <files…>_reverse.csv
python3 <RUN>/_scripts/validate_ledger.py capabilities <files…>_capabilities.csv
```

`--index` and `--extension-index` default to `<RUN>/R1_INVENTORY/CLAIM_INDEX.csv` and
`EXTENSION_INDEX.csv`. **Errors must be zero before return; warnings are reported.**
`_scripts/test_validate_ledger.py` is its fixture suite.

## 7. Reading discipline (CAND §7; PostReleaseBasis REVISE, R0 §7.2)

- **Read from the frozen tree only**, i.e. the path given in your brief. Never read the
  working repository's deliverables: they carry run edits.
- **Economize.** Grep before you read, read line ranges, and prefer deliverable files and
  the evidence pack (§9) over broad code sweeps.
- **Out of bounds:** do not read `projects/chirality-runtime/execution/**`, or any other
  project's execution tree.
- **Write only your assigned output paths.** No edits anywhere else, no test runs, no
  installs. Git only as read-only `git -C <frozen> log`, `show` and `blame -L` against the
  frozen tree (§2.3; `RUN_BASIS.md` Addendum 1).

## 8. Scope-extension units (Ruling D)

Governing documents (CONTRACT, SPEC, PRD, TYPES, DIRECTIVE) and the invariant coverage
register are **not** audit targets. They remain GOVERNING only.

| Item | Unit key | Audit question | Source |
|---|---|---|---|
| 3 | `DEC:D-APP-nnn` for each register row D-APP-86..D-APP-127 in state `RULED` | Did the ruling's stated effect land in code or corpus at the frozen basis? | Register row + ruling record |
| 4 | `DOC:<DOCID>#<n>` for each `##`/`###` section of `docs/BUILD_AND_RELEASE.md` (`BUILDREL`), `docs/RELEASE_QUALITY_GATES.md` (`RQGATES`), `docs/VALIDATION_STRATEGY.md` (`VALSTRAT`), `docs/RELEASE_QUALITY_RUNBOOK.md` (`RQRUN`), `docs/harness/reliance_boundary_register.md` (`RELIANCE`) | Does the section match what shipped? `.github/workflows/{harness-premerge,desktop-release-template}.yml` and release AgentRuns records are evidence only | Section text |
| 5 | `SOW:SOW-nnn` for each scope-ledger row in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Does the row map to at least one live deliverable, and to code or an explicit deferral? | Ledger row |
| 6 | `DOC:PRODAGENTS#<n>` for sections of `instructions/AGENTS.md` | Is it accurate about product behavior? **Audit-only.** Repairs route to Root per packet Δ10 | Section text |
| 7 | `DOC:<DOCID>#<n>` for sections of `frontend/docs/harness/*.md` (DOCID = uppercase file stem, e.g. `RUNTIME_ENGINE_CONTRACT`) | Is the developer documentation accurate? **Audit-only** | Section text |

**Index.** `R1_INVENTORY/EXTENSION_INDEX.csv` (built by `_scripts/extension_index.py` from
the frozen tree; header `UnitKey,Item,SourcePath,SourceLine,Label`, then `#END`) is the
coverage checklist. [INTEG] Unit definitions used by the index:

- Item 3: a register row counts as `RULED` when its State cell begins `RULED` (including
  `RULED / CONCLUDED`, `RULED / DISPOSED`, `RULED (…)`). D-APP-116..119
  (`AWAITING_RULING`) are not units. 38 units.
- Items 4, 6, 7: `<n>` is the 1-based ordinal of the `##`/`###` heading in file order,
  ignoring headings inside fenced code blocks. `#0` is the preamble between the `#` title
  and the first `##`/`###` heading, indexed when it holds text (so no text is unaudited).
  Items 4/6/7: 58, 9 and 32 units.
- Item 5: the rows of `## 9. Scope Ledger` (84 units, SOW-001..SOW-084).

**Ledger schema.** The §2 header and rules apply, with:

- `PackageID` is `EXT`.
- `DeliverableID` is the owning deliverable when one is evident, else `NONE`.
- `ClaimKey` is the unit key; `ClaimID` is the key after the class prefix (`D-APP-86`,
  `SOW-001`, `BUILDREL#3`). [INTEG] Split sub-rows add `.n` (`DOC:BUILDREL#3.1`);
  run-local rows are `DEC:STATE-n`, `SOW:REGISTER-n`, `DOC:<DOCID>#STATE-n`, and so on.
- **Ledger file names:** `DEC_claims.csv`, `SOW_claims.csv`, `DOC-<DOCID>_claims.csv`
  (one per DOCID); notes, reverse and errata files follow the same stem
  (`DEC_notes.md`, `DOC-BUILDREL_errata.csv`).
- [INTEG] Column guidance for extension units:
  - Item 3 (`DEC`): `ClaimType = REQUIREMENT` for the ruling's stated effect;
    `LatestDecision` is the ruling itself; `ALIGNED` when the effect landed,
    `DOCUMENTED_UNIMPLEMENTED`/`PARTIALLY_IMPLEMENTED` when it did not, `RETIRED_BY_RULING`
    or `ACCEPTED_DIVERGENCE` when a later ruling superseded it. Rows flagged in `RUN_BASIS.md`
    §5 as "GOVERNING, flagged" (effect pending, held or unapplied) are judged against their
    recorded flag, not treated as landed.
  - Item 5 (`SOW`): the audit question has two parts; split `.1` (live-deliverable mapping)
    and `.2` (code or explicit deferral) when they disposition differently. An `OUT` row is
    a boundary trace: `ALIGNED` when no live deliverable implements it.
  - Items 4, 6, 7 (`DOC`): tier by the source the section restates; process sections that
    restate nothing normative are `STATE_ASSERTION` with `NOT_APPLICABLE`.
  - Items 6 and 7 are **audit-only**: record the accuracy finding with the normal
    Disposition, and begin `RemainingWork` with `AUDIT-ONLY` on every non-ALIGNED row;
    item 6 adds `ROUTE:ROOT (Δ10)`. Nothing in these files is repaired by this run
    (validator warning `W-AUDIT-ONLY`).
- Validator: the same `ledger` mode; coverage is checked against `EXTENSION_INDEX.csv`
  (`DEC` ← item 3, `SOW` ← item 5, `DOC-<DOCID>` ← that DOCID's units).
- [A0] Wave placement (D-APP-129 item D and §10): item 4 is audited **with the PKG-09 wave
  (wave 5)**. All extension ledgers (items 3, 4, 5, 6 and 7) are written under one extension
  manager (`EXT`, brief `BRIEFS/R2_EXT_MANAGER.md`) that HELP_HUMAN dispatches alongside the
  PKG-09 manager in wave 5.

## 9. Evidence pack (Ruling C; R0 report §9)

Each R2 WORKING_ITEMS manager builds **one evidence pack** for its package before
dispatching workers, and puts its path into every worker brief. It contains the five items
of report §9. [INTEG] `[A0]` marks HELP_HUMAN post-review corrections. File names and formats, so every manager builds it identically:

- **Location:** `<RUN>/R2/<PKG-ID>/EVIDENCE_PACK/` (extension managers:
  `<RUN>/R2/EXT/EVIDENCE_PACK/`). Items 1, 2 and 5 are corpus-wide: [A0] the R1b manager builds them once at
  `<RUN>/R2/_shared/EVIDENCE_PACK/`, and each package manager copies them byte-for-byte; their SHA-256 must then match.
- **All CSVs:** UTF-8, header row, data rows, final `#END` record, repo-relative paths,
  rows sorted by the listed key columns, built from the frozen tree at `00115c719`.

| # | File | Header | Content and method |
|---|---|---|---|
| 1 | `TOUCHED_PATHS.csv` | `Path,Commit,StartLine,EndLine` | The post-release touched-path list with line ranges. For each path changed by `da95ec194`, `cb08dbe2f`, `9ecbdecdf` or `ccb95e06a` (`git -C <frozen> show --name-only --format= <commit>`) that exists at the frozen basis, one row per maximal run of consecutive lines that `git -C <frozen> blame --line-porcelain 00115c719 -- <path>` attributes to that commit. Line numbers are at the frozen basis. Deleted paths get one row with `StartLine = EndLine = 0`. Sort: Path, StartLine. |
| 2 | `REACHABILITY.csv` | `Path,Reach,EntryPoint,ImportChain,Basis` | The static reachability map. One row per module under `frontend/src/**` and `frontend/electron/**`, plus `projects/chirality-runtime/packages/*/src/**` (runtime modules are `LIVE` when reached from LIVE App code via `@chirality/runtime-*` imports or from the runtime-service entry the App packages) [A0]. `Reach` ∈ `LIVE` (reached by static imports from a product entry point: `frontend/src/app/api/**` routes, `frontend/src/app/**` pages, `frontend/electron/main.ts`), `LEGACY_ONLY` (reached only through the retained Claude SDK / Pi path, seeded from the `LEGACY-IN-PROCESS:` notes in `R0_CALIBRATION/SURFACES/HARNESS_capabilities.csv` and re-verified from imports), `TEST_ONLY` (reached only from tests) or `UNREACHED`. `ImportChain` is the shortest chain `entry>…>path`. `Basis` = `REACHABILITY(static)@00115c719`. Sort: Path. |
| 3 | `REFERENCE_HASHES.csv` | `DeliverableID,Document,RecordedSha256,RecordedVerdict,RecomputedSha256,Match` | Hash recomputes of CONTRACT, SPEC and PRD versus each deliverable's `_REFERENCES.md`. `Document` ∈ `CONTRACT`, `SPEC`, `PRD`. `RecordedVerdict` is the `_REFERENCES.md` verdict (e.g. `MATCH`) or `NOT_RECORDED`. `RecomputedSha256` is `shasum -a 256` of `projects/chirality-app-dev/docs/<Document>.md` at the frozen basis. `Match` ∈ `YES`, `NO`, `NOT_RECORDED`. Workers cite it as `HASH-RECOMPUTE@00115c719`. Sort: DeliverableID, Document. |
| 4 | `DECISION_HITS.csv` | `DeliverableID,DecisionID,Kind,Source,Path,Line,RegisterState` | Per-deliverable decision-register and D-GOV hits. Every `D-APP-nn` and `D-GOV-nn` string in the deliverable's folder (`Source = DELIVERABLE`), plus every register row or ruling record naming the deliverable ID (`Source = REGISTER` or `RULING`). `Kind` ∈ `D-APP`, `D-GOV`. `RegisterState` is the App register State cell for D-APP IDs (first word, e.g. `RULED`, `AWAITING_RULING`) and `ROOT` for D-GOV. Sort: DeliverableID, DecisionID, Path, Line. |
| 5 | `D-APP-127_APPLICATION_MAP.csv` | `DeliverableID,Carrier,Revised,Evidence` | The D-APP-127 application map. For each deliverable and each carrier `_STATUS.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `Dependencies.csv`, `_REFERENCES.md`: `Revised` ∈ `YES` (the carrier cites D-APP-127 or D-GOV-43 and states the applied effect), `PARTIAL`, `NO`, `ABSENT` (no such file). `Evidence` is `path:line` of the citation, or `NONE_FOUND`. Sort: DeliverableID, Carrier. |
| — | `PACK_MANIFEST.md` | — | For each file: the exact commands or script used, the row count, and SHA-256. Scripts live in `<RUN>/R2/_scripts/`. |

## 10. R2 operating rules (Ruling C; R0 report §6 and §9)

- **Managers.** One WORKING_ITEMS manager per package; **at most 3 managers run
  concurrently**; each manager runs **at most 4 concurrent children**. (Ruling C; this
  replaces the report's "10 forward workers per manager".)
- **Evidence pack.** One per manager, per §9, before its first dispatch.
- **Worker sizing** (report §6, §9): one deliverable per worker. Pre-gather when
  SoW + `_STATUS` ≥ 48 KB or indexed units ≥ 38 (13 deliverables: DEL-01-02, 02-01, 02-02,
  02-05, 04-01, 05-04, 06-03, 08-03, 08-04, 08-05, 09-04, 09-05, 09-06). Split across two
  workers by SoW section range when ≥ 55 KB or ≥ 50 units (DEL-01-02, 02-01, 09-04, 09-05);
  the manager merges the two ledgers. Retired deliverables such as DEL-09-07 get a light
  worker using `RETIRED_BY_RULING`.
- **Wave order** (report §9), clustered by shared evidence:
  1. legacy-harness cluster (PKG-04, 06, 08, 10), reusing the HARNESS reverse pass;
  2. engine, runtime and session (PKG-03, 05);
  3. shell and UI (PKG-02, 07);
  4. governance and docs (PKG-00, 01);
  5. release and installer (PKG-09), which carries the retired-deliverable handling, with the
     extension ledgers (§8).
  - [A0, D-APP-129 ruling C] **The remaining 10 reverse-pass areas run first, under their
    own manager (R1b), before any wave**: ELECTRON, BUILD, ROUTES, SHELL, WOVEN, WORKSPACE,
    SETTINGS, RTCORE, RTCONTRACT, INSTRUCTIONS (HARNESS was done in R0). This supersedes the
    report's placement of new areas within waves. At most 3 managers run concurrently;
    HELP_HUMAN schedules packages in the order above as manager slots free.
- **Double-blind rule** (Double-blind ADOPT, R0 §7.2; report §9): one double-blind
  deliverable per wave — two independent workers, compared by
  `R0_CALIBRATION/_scripts/double_blind.py`.
- **Verifier** (report §9): shards of at most 50 items; one shared grading key across
  shards; selection class (a) = all LOW, self-flagged, `AUTHORITY_CONFLICT`, `UNKNOWN`,
  `REMAINING_WORK` and errata rows, plus 30% of other non-ALIGNED rows.
- **R4 citations** (Ruling C): rows turning on the framed questions cite `R4-Q1`,
  `R4-Q2`, `R4-Q3`, `R4-Q4`, `R4-Q5` or `R4-Q6` (§2.4) instead of plain `R4`. The done-declaration's Q-01..Q-13 go to
  R4 separately (Ruling B).
