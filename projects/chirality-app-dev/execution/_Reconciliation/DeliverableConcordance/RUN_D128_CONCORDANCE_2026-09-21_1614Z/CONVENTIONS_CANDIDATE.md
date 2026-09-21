# RUN_D128 — Candidate conventions (R0 calibration edition)

> **Status: CANDIDATE.** These rules are used by the R0 calibration so they can be
> tested. None is adopted until the owner rules at the R0 gate (D-APP-128 ruling §5.5).
> Base method: plan §6–§7 as amended by packet Δ1–Δ11. Where this file extends the plan,
> the extension is marked **[EXT]**; where it restates July's MR-n, it says so.

## 1. What you are comparing (the four-way picture)

For each audit unit, establish:

1. **What the deliverable says.** The claim text and its declared state.
2. **What the implementation does.** App `frontend/**` and `projects/chirality-runtime/{packages,tests}/**`
   at the frozen basis `00115c719`.
3. **What recorded direction says.**
   - Only CONTEXT sources from `RUN_BASIS.md` §5 may be used here.
   - They may explain a divergence. They never change the Disposition.
4. **Whether the divergence is unrecorded judgment.** When code diverges and no direction
   record explains it, say so: `CauseTag = UNRECORDED_JUDGMENT`.

Code and tests are evidence, not authority. An agent disposition is never a ruling.

## 2. Ledger file `<DEL-ID>_claims.csv` [EXT schema]

- **Format.** UTF-8 CSV with a header row, then data rows, then a final line containing
  exactly `#END`.
- **Paths.** Never write an absolute path. Use repo-relative paths, e.g.
  `projects/chirality-runtime/packages/core/src/x.ts:120`.
- **Header**, exactly 25 columns:

`ClaimKey,ClaimID,PackageID,DeliverableID,ClaimType,NormativeSource,AuthorityTier,LatestDecision,DeclaredState,RecordedRemaining,RemainingSource,RemainingGate,MechanicallyUnblocked,ImplementationEvidence,VerificationEvidence,LifecycleState,AssessmentEvidence,DirectionEvidence,PostReleaseBasis,Disposition,CauseTag,Confidence,RemainingWork,HumanDecisionNeeded,Notes`

| Column | Rule |
|---|---|
| `ClaimKey` | See the ClaimKey rules below the table. |
| `ClaimID` | The local part of the key (`CLM-007`, `CLM-007.2`, `REM-1`, …). |
| `PackageID`, `DeliverableID` | e.g. `PKG-03`, `DEL-03-01`. |
| `ClaimType` | `REQUIREMENT` · `ACCEPTANCE` · `EXCLUSION` · `CONTEXT_CLAIM` **[EXT]** (references, provenance, conflict tables, method notes; non-normative) · `STATE_ASSERTION` **[EXT]** (dated reconciliation/carrier notes and Remaining prose asserting current state) · `REMAINING_WORK` · `REGISTER_DEFECT` (MR-5). |
| `NormativeSource` | Where the claim's authority comes from: SoW section plus the `Source` cell's references (PRD §, CONTRACT K-…, decision ID). |
| `AuthorityTier` [EXT] | `LOCAL_DESIGN` (deliverable-level design choice) · `PRD` (restates a PRD requirement) · `GOVERNANCE_INVARIANT` (restates DIRECTIVE/CONTRACT/SPEC/TYPES or a D-GOV rule) · `NOT_APPLICABLE` (CONTEXT_CLAIM). Pick the highest tier the claim restates. |
| `LatestDecision` | `D-APP-nn` when it governs; `D-APP-nn (context)` when it only touches (MR-7); `NONE_FOUND`. |
| `DeclaredState` | What the deliverable asserts is true now (short). |
| `RecordedRemaining`, `RemainingSource`, `RemainingGate` | For REM rows: verbatim item, its source, and verbatim gate suffixes concatenated (MR-6). Otherwise `NONE_RECORDED`. |
| `MechanicallyUnblocked` [EXT rename of `SelectableUnderCurrentLoop`] | See the MechanicallyUnblocked rules below the table. |
| `ImplementationEvidence` | Repo-relative path + symbol/line; or `documentary claim` + exact doc sections (MR-10); or `NONE_FOUND` after a stated search. |
| `VerificationEvidence` | `GATE-TRANSCRIPT(APP@00115c719)` or `GATE-TRANSCRIPT(RUNTIME@00115c719)` **plus** the named test file and case; or an MR-10 token: `DOC-BASIS(D-APP-nn)`, `RUN-INSPECTION@00115c719`, `RULING-RECORD(D-APP-nn)`, `SNAPSHOT+LIVE-REVERIFY(<snapshot>)`; or `NONE_FOUND`. Never run a test suite. |
| `LifecycleState` | From `_STATUS.md` (`IN_PROGRESS` / `OPEN`). |
| `AssessmentEvidence` | Exactly one token, `OVERTAKEN` · `STILL CURRENT` · `NOT APPLICABLE`, about the deliverable's `Assessment_INSP-03_*` conclusion for this claim (MR-1). Where the assessment predates the SoW, cite the old REQ-ID it discussed, or write "no direct conclusion" (MR-9). |
| `DirectionEvidence` [EXT] | For a divergence, the CONTEXT record (path + section/anchor) that explains it, or `NONE_FOUND`. For ALIGNED rows, `NOT_APPLICABLE`. |
| `PostReleaseBasis` [EXT] | `YES` if the evidence relied on comes from the post-v3.0.1 commits `da95ec194`, `cb08dbe2f`, `9ecbdecdf`, `ccb95e06a`; else `NO`. |
| `Disposition` | Plan §7 vocabulary (below). |
| `CauseTag` [EXT] | See §4. `NONE` only on ALIGNED rows. |
| `Confidence` | `HIGH` · `MEDIUM` · `LOW`. LOW rows must contain `LEAST-CONFIDENT:` in Notes, with the alternative reading. |
| `RemainingWork` | The evidence-based residual, `NONE_OBSERVED`, or `UNKNOWN`. |
| `HumanDecisionNeeded` | `NO`, an existing decision ID (e.g. `D-APP-117`), or `R4` (needs an owner ruling not yet framed). |
| `Notes` | Short. Self-flags, cross-deliverable observations, method friction. |

**`ClaimKey`** is `DEL-xx-yy#<local>`, where `<local>` is the `LocalID` from `R1_INVENTORY/CLAIM_INDEX.csv`.

- **Coverage.** Every indexed unit for your deliverable must appear at least once.
- **Splitting.** You **may split** one unit into sub-rows `…#CLM-007.1`, `.2`, … when it
  holds independently dispositionable statements (e.g. a table of several
  requirements). Report your split rate in the notes.
- **Extra keys.** Rows the index does not know get run-local keys:
  - `REGISTER-n` for register defects (MR-5);
  - `STATE-n` for state assertions outside indexed units.

**`MechanicallyUnblocked`** is meaningful only on `REMAINING_WORK` rows:

- `YES`: every written gate is verified satisfied at the source the gate itself names, and
  no ACTIVE PREREQUISITE dependency named in the item's `Depends` is pending.
- `NO`: at least one gate or dependency is unsatisfied.
- `UNKNOWN`: cross-project gate status is not stated on an App surface (MR-6).
- On every other row: `NO` (MR-2). `YES` is never permission to execute.

**Disposition vocabulary** (plan §7):

- `ALIGNED`
- `IMPLEMENTED_UNDOCUMENTED`
- `DOCUMENTED_UNIMPLEMENTED`
- `PARTIALLY_IMPLEMENTED`
- `IMPLEMENTED_DIFFERENTLY`
- `STALE_SPECIFICATION`: the text flatly asserts a now-false state; repair-shaped (MR-8).
- `STALE_ASSESSMENT`
- `STALE_VERIFICATION`
- `ACCEPTED_DIVERGENCE`: the text acknowledges the gate, **and** a GOVERNING ruling permits the difference (MR-8). CONTEXT alone never makes a row ACCEPTED_DIVERGENCE.
- `LIFECYCLE_REASSESSMENT_REQUIRED`
- `REMAINING_STATE_MISMATCH`
- `DEFERRED_AGENT_WORKFLOW`: agent-instruction or workflow matter; evidence only (Δ10).
- `AUTHORITY_CONFLICT`: never choose between conflicting sources.
- `UNKNOWN`
- `NOT_AUDITABLE` **[EXT]**: `CONTEXT_CLAIM` rows with nothing to check; say why in Notes.

**Deliverable text is judged against the GOVERNING map.** A ruled decision stands over
older corpus wording that has not been transcribed (MR-11, generalized). Cite the ruling
in `LatestDecision` and classify the stale wording per MR-8.

## 3. Notes file `<DEL-ID>_notes.md`

Sections:

1. **Census:** rows by ClaimType and Disposition; split rate.
2. **Least-confident rows,** each with the alternative reading (mandatory).
3. **Register-defect summary.**
4. **Direction and cause:** the main CauseTags and the CONTEXT records used.
5. **Method friction:** any rule here that did not fit, with a proposed revision (R0 calibration input).
6. **Effort:** approximate files read, and whether the context budget was tight (this sets the oversize threshold).

## 4. CauseTag vocabulary [EXT]

`NONE` · `CODEX_SOLE_ENGINE` (Codex is the only engine; Claude/Anthropic/Pi paths retired or
demoted) · `A2_TOPOLOGY` (D-GOV-43: App-owned Runtime service; daemon/LaunchAgent/per-root
homes retired) · `RUNTIME_EXTRACTION` (behavior moved to `projects/chirality-runtime`) ·
`SHELL_REDESIGN` (SCA-APP-010 dialogue-centred shell / woven workspace) ·
`CREDENTIAL_CUSTODY` (Codex owns login and credentials; D-APP-126/127) ·
`FACADE_DEPRECATION` (`harness-contract` → `runtime-contracts`) · `NATIVE_DELEGATION`
(Codex-native descendants versus the Type 2 bridge) · `V3_RELEASE_SCOPE` (explicitly in or
out of scope for v3 per CONTEXT direction) · `CARRIER_PROPAGATION` (an agent-propagated
note that is stale or partial) · `PRE_V3_DRIFT` (divergence already present before about
2026-08-22) · `DOC_HYGIENE` (metadata/register/reference defects) · `UNRECORDED_JUDGMENT`
(divergence with no recorded direction found) · `OTHER:<TOKEN>` (new cause; the manager
reports every OTHER token).

## 5. Reverse pass [EXT] (two sealed passes)

1. **Forward pass.**
   - Write `<DEL-ID>_claims.csv` (with `#END`) and `<DEL-ID>_notes.md`.
   - Run the validator.
   - Record `sha256sum` of the claims file in your return. The forward ledger is then **sealed**: do not edit it afterwards.
2. **Reverse pass.**
   - Only after sealing, open the capability file you are given.
   - Write `<DEL-ID>_reverse.csv`, then `#END`. Header: `CapabilityID,Response,ClaimKey,Rationale`. Answer every row:
     - `CLAIMED_BY` + the key of one of your claims that owns it;
     - `PARTIAL` + the key that covers part of it;
     - `NOT_MINE` with empty `ClaimKey`.
   - If the reverse pass shows a forward row was wrong, **do not edit the sealed ledger.**
     Describe it in `<DEL-ID>_reverse_notes.md`; the verifier and manager handle it.

**Capability file** `<AREA>_capabilities.csv` is written by the reverse-pass worker. Header:

`CapabilityID,Area,Capability,Paths,EntryPoints,CoveringTests,PostReleaseBasis,Notes`

- `CapabilityID`: `CAP-<AREA>-nnn`.
- **Granularity:** one row per user- or system-observable behavior, or contract surface,
  that a deliverable could plausibly own. Not per file or per function. Target 20–60 rows
  per area.
- The file has **no owner column**.
- End with `#END`.

## 6. Validator

`python3 <RUN>/_scripts/validate_ledger.py ledger --index <RUN>/R1_INVENTORY/CLAIM_INDEX.csv <files…>`
(also `reverse --capabilities <cap.csv> <files…>` and `capabilities <files…>`). Run it from
`projects/chirality-app-dev`. Errors must be zero before return; warnings are reported.

## 7. Reading discipline

- **Read from the frozen tree only**, i.e. the path given in your brief. Never read the
  working repository's deliverables: they carry run edits.
- **Economize.** Grep before you read, read line ranges, and prefer deliverable files
  over broad code sweeps.
- **Out of bounds:** do not read `projects/chirality-runtime/execution/**`, or any other
  project's execution tree.
- **Write only your assigned output paths.** No edits anywhere else, no git operations, no
  test runs, no installs.
