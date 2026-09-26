# D-PEC-96 — Loop-registry schema v2 with closed feed profiles (SCA-005 §B6 registry source packet) — proposal

Status: **PROPOSAL / AWAITING_RULING** (revision 2). Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node G1) for the PEC loop, 2026-09-25 (session date), from brief `G1_REGISTRY_SOURCE_PROPOSAL.md` (SHA-256 `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1`). No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. It asks for no lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `56a626c3b` the register has no D-PEC-96 row. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`.

**Revision 2.** Revision 1 (SHA-256 `f486111927dbd0b29ec7ec9ff653e51b5169d02dce53e4ab7357f544c1697d87`) was published unchanged as PR #928. The independent REVIEW required by D-PEC-78 §4.3, relayed by HELP_HUMAN, reproduced every hash and check and 13/13 mutations. It raised seven points. This revision addresses them:

| Point | Change in revision 2 |
|---|---|
| 1 Remaining sections invisible (medium) | New profile `remaining-items`: it reads the `## Remaining` sections as records only, not as a selection surface and not with the ledger. PEC's row declares it `live`. The choice is owner question 3 |
| 2 Overlapping or contradictory profiles accepted (medium) | Each profile now names the surfaces it covers. The adapter rejects a row whose profiles overlap on any surface, and a row with no live profile. There are 6 new located test cases and 6 new mutations (M14–M19) |
| 3 `agentruns-json` narrower than PRD v2.3 (low–medium) | Coverage is now JSON run evidence anywhere under `execution/`, as PRD §7.1 says. PEC's row declares it `historical`, which covers PEC's one `WORK_GRAPH.json` |
| 4 §B6 quoted in part (low) | §B6 is quoted in full. Owner question 2 states the departure from the letter of §B6 and Q8 (a), and why |
| 5 Containment "nothing else" (low) | HELP_HUMAN's records under `execution/_Coordination/**` may ride the act PR; the draft lists them |
| 6 HOLD citation (low) | Now cites DEL-01-06 `_REVIEW.md` L45–48 |
| 7 Test and schema nits (low) | Added tests for a non-string `state` and a `null` `profile`. A new test proves that no failure echoes a document value. The schema `$id` is now `…/loops.schema.v2.json` |

## Provenance

- **Owner acts relied on.**
  - SCA-005 checkpoint 1 (2026-09-24): "I accept checkpoint 1 and the Impact Assessment." It selected the resolution note's Section A, including Q1 O-B2, Q8 (a) and CP1-V "within D-PEC-78 O-A with no supersession" (`_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/DECISION.md`, `b9157b2b…40da`; note `CHECKPOINT1_RESOLUTION_NOTE.md`, `af4e46d0…0ad2`; `Decision_Log.md` rows SCA005-CP1-Q8 and SCA005-CP1-V).
  - Checkpoint 2 (2026-09-25, `D-PEC-92`): "CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred." It accepted `Propagation_Plan.md` (`50cd0b1d…1350`), whose §B6 is this packet's intent, and it opened no `v2/**` path.
  - Checkpoint 3 (2026-09-25): "CP3: accept; Q1 a". Revision 1.5 became `current_basis` with PRD v2.3.
  - `D-PEC-78` O-A (2026-08-02): "D-PEC-78: O-A". The packet it ruled (`D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md`, `426dba04…5d17`) §4.2 says: "Adding, removing, or changing a field's meaning requires a new schema version and a successor D-PEC migration packet. Version 1 is not silently widened. A dual-read transition, if needed, must be time-bounded and tested; unknown versions fail closed."
  - `D-PEC-94` (2026-09-25): "You can continue with all the open work you identified." Its record (`b6814e90…6a6b`) exercises `D-PEC-86` §3 I-7: PEC adopted the shared development-loop method and froze `loop/LOOP_RECEIPTS.md` after Receipt 197. It says later fenced writes still need their own packets, and it names no registry change.
- **Fence.** `projects/pec/AGENTS.md` (`c9d3b44d…197a`) §"Write Scopes And Fences" says every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. `F-PEC-1` (`D-T0-15`, `95c245b5…0b09`) fences source trees until such a packet opens them. No earlier ruling opens the paths below for this change:
  - `D-PEC-75` opened DEL-01-06's first slice, merged 2026-08-02 as `ccd9a2178`.
  - Later `v2/**` packets opened other deliverables' paths, for example `D-PEC-77` for DEL-01-05 and `D-PEC-85`, `-87`, `-89` and `-91` for DEL-01-03.
  - Since the D-PEC-75 slice, the registry files have changed only in the 2026-09-05 path migration (`ca49b846d`).
- **Intent of record.** `Propagation_Plan.md` §B6, in full: "`loops.schema.json` v2 carrying feed-profile declarations, `loops.json` rows declaring profiles (PEC's own `pec` row `remaining-loop`, Q8 (a)), and a `RegisteredLoop` port field; exact paths, VER-001/VER-003 re-run and rollback named by that packet. Since D-PEC-87 X-1, `software-workflow.json`'s `v2-store-guard` rule also covers `v2/src/pec_v2/**`, so the packet's verification list names both checks. D-PEC-86 I-7 (PEC's own migration) stays deferred; migration later is one owner-gated row change (Q8)."
  - Revision 1.5 states the obligation in SOW-077, SOW-094 and the DEL-01-06 description.
  - PRD v2.3 §16.3 says a strict schema version 2 "arrives only through a later D-PEC packet, within D-PEC-78 O-A".
- **Precedents.** `D-PEC-95` (proposal format; a bound, preimage-checked act script; revert-PR rollback). `D-PEC-91` (v2 source grant, registered-check table, mutation evidence). `D-PEC-87` X-1 (the store-guard path rule). `D-PEC-75` (DEL-01-06 run records under `_run_records/`).
- **Source state.**
  - Revision 1 was read at `origin/main` `abfd0897b`. Revision 2 was read at `origin/main` `56a626c3b5515fea790b0d40549e7729669b7dff` (PR #927), from a fresh `git archive` export.
  - That commit descends from `4d5f7b911`, the basis HELP_HUMAN named, and changes nothing under `projects/pec` since it. No `v2/**` path changed since `abfd0897b`, and every product preimage and must-remain hash was re-verified.
  - Cited files that changed since revision 1:
    - `_REGISTER.md` (`d94bfeab…b59e`), which still has no D-PEC-96 row;
    - the work graph (`ac0db3b4…0be7`), where G1 is `ACTIVE`;
    - SCA-006 checkpoint 1, now accepted (see below);
    - the verifier skill `.agents/skills/software-code-review/SKILL.md` (`ee085d58…8bca`).
  - The checkout (now on branch `claude/pec-d96-registry-proposal`, moved by another actor) was not changed. This TASK switched no branch and ran only read-only Git commands and `git fetch`.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` at `56a626c3b` with `--operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for all 13 targets: the 11 product paths and the two administrative paths below.

## What preparation found

### The registry today (unchanged since `abfd0897b`)

- `v2/config/loops.json` is schema version 1 with one row: `pec` → `projects/pec/loop/LOOP_INIT.md`. It carries no feed profile.
- `loops.schema.json` fixes `schema_version` to `1` and allows only `loop_id` and `loop_init_path` per row (`additionalProperties: false`).
- `RegisteredLoop` has two fields. The JSON adapter rejects every version other than 1 with a located error.
- `v2-loop-registry` runs 12 tests and passes. Nothing outside `projects/pec/v2` imports the registry; a repository grep finds only historical reconciliation manifests that name the files.

### The PEC-row premise

**Resolution: PEC's `pec` row should now declare the shape PEC writes after D-PEC-94:**

| Profile | Version | State | Basis |
|---|---|---|---|
| `shared-dev-loop` | 1 | live | the D-PEC-94 record |
| `remaining-items` | 1 | live | `projects/pec/AGENTS.md` |
| `loop-receipts-ledger` | 1 | historical | `projects/pec/AGENTS.md` |
| `agentruns-json` | 1 | historical | the D-PEC-94 record |

This is the migration row change the accepted records foresee, plus the two surfaces the review showed must stay visible. It needs its own ruling, which this packet asks for as a separate question (question 2). No scope change is needed.

1. **Why Q8 chose `remaining-loop`.** The resolution note gave Q8 (a) this reason: "D-PEC-86 I-7 defers PEC's own migration; PEC's `LOOP_INIT.md` still selects from `## Remaining`, so its registry row declares the shape it actually writes". Its sources were D-PEC-86 §3 I-7 and the then `loop/LOOP_INIT.md` §4. Both premises lapsed after checkpoint 3:
   - D-PEC-94 exercised I-7 on 2026-09-25.
   - The current `projects/pec/AGENTS.md` says the `## Remaining` sections are "no longer a work-selection surface", and that `loop/LOOP_RECEIPTS.md` is "a historical ledger, closed by Receipt 197".
2. **What the profiles mean.** The design note (`FEED_MODEL_V2_DESIGN_NOTE.md`, `4b9ccb9f…12da`, §4 O-B2) defines them:
   - `remaining-loop` is a live `## Remaining` field, the live ledger, dependency registers and decision registers ("PEC's own current loop").
   - `shared-dev-loop` is work graphs, central receipts, the MEMORY run index, `_STATUS.md`, dependency registers and decision registers.

   The note describes PEC's later migration as "one owner-gated row change from `remaining-loop` to `shared-dev-loop`, with the ledger declared `historical`, and no parser rework". PEC now writes that shape: one Git-tracked `WorkGraphs/<undertaking>/WORK_GRAPH.md` and one dated-heading `MEMORY.md` (DEL-01-03). A central `RECEIPT.md` is planned at the undertaking's closeout; none exists yet.
3. **What the accepted texts require.**
   - The SOW-094 statement asks only for "each row's feed-profile selection". Its Notes cell adds: "PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7)".
   - Q8 (a) reads "declare `remaining-loop` now; migration later as one row change under its own ruling".
   - §B6 (above) repeats both.
   - SOW-077 asks each row to declare a profile with "live/historical" and a "basis citation to the loop's own record".
   - PRD v2.3 names no profile.
4. **Inside this packet or separate.** The accepted texts foresee the migration, and no scope statement changes, so it needs no scope change. They do require that it happen "under its own ruling", so this packet asks it as a separate question. The source bytes are the same either way, except `loops.json` and one test expectation (option A versus A-R). The owner may also rule it in a later packet.
5. **Why not the literal `remaining-loop`.**
   - It would record a reading hypothesis that PEC's own instructions contradict.
   - Its `basis` could cite only a lapsed record.
   - PEC would read a closed ledger as live, so under PEC-ORI-006 the ledger's silence would look like staleness.
   - A later packet would still be needed for a one-row change.

   Nothing consumes the registry yet, so A-R is harmless now, but it is knowingly stale.

Consequences of A, none blocking:

- **Stale "now" sentences.** The SOW-094 Notes cell and the DEL-01-06 description and `_CONTEXT.md` still say "PEC's own row declares `remaining-loop` now". After A that sentence records the SCA-005 intent, not the current row. It is Notes and description text, not a scope statement. The DEL-01-06 Scope of Work rebuild (graph node S2) states the current row, and the next PEC scope change can refresh the decomposition sentence. This packet writes neither.
- **R-05 and FX-PEC-0.** SCA-005 risk R-05 ("PEC's own P1 self-ingest corpus stays old-shape") and fixture FX-PEC-0 rest on the lapsed premise. Impact Assessment §9.3 and design note §6 define FX-PEC-0 as "PEC `_STATUS.md` (57 with `## Remaining`), `LOOP_RECEIPTS.md`, 64 `Dependencies.csv`, the one historical `WORK_GRAPH.json`" under `remaining-loop`. Under A the same corpus is covered by `remaining-items`, `loop-receipts-ledger` (historical), `shared-dev-loop` and `agentruns-json` (historical), plus the new work graph and MEMORY surfaces. FX-PEC-0 becomes a real dual-generation self-ingest. This is carried to graph node X1.

### Remaining sections: read as records (review point 1)

**Observed.** `projects/pec/AGENTS.md` §"Deliverable records and loop ownership" says the `## Remaining` sections "stay in place as deliverable-local records of open scope under their owning decisions". It also says they are "no longer a work-selection surface" and that "A Remaining item's own gate markers still bind that item". There are 57 such sections at `56a626c3b`. Revision 1's row declared no profile that reads them. `remaining-loop` cannot sit beside `shared-dev-loop`, because it also claims the lifecycle, dependency and decision surfaces and the ledger as live.

**Options considered.**

- **(a) A records-only add-on profile, `remaining-items` (recommended).** It covers exactly one surface, the `## Remaining` sections, read as records of open scope with their gate markers. It is never a selection signal and brings no ledger with it.
  - It fits PRD v2.3 §7.1, which makes "remaining items" "a per-loop optional field, read only where the loop's feed profile declares it". An optional field declared by an add-on profile is that text taken literally.
  - It keeps O-B2's closed bundles (owner-selected at checkpoint 1) for everything else.
  - It keeps `remaining-loop` meaningful for a loop that still selects from Remaining.
- **(b) Split every profile into single-surface profiles.** Every row would then list its surfaces one by one. That moves toward O-B1 ("free declarations"), which checkpoint 1 did not select, and the design note's reason for preferring O-B2 applies: configuration should stay "small and strictly validatable". Not recommended.
- **(c) Leave them unread** (revision 1). That makes the maintained records, with their gate markers, invisible to PEC's orientation, which the review found unacceptable without the owner's say. Available by answering question 3 (c).

**State.** `live`. PEC still updates the sections "under the packet that opens that `_STATUS.md`" when an undertaking completes or changes an item, so the generation is not frozen. If the owner later retires the sections, as App and Piping did, that is a one-row change to `historical` or removal.

### Profile coherence: disjoint surfaces, at least one live (review point 2)

**Observed in revision 1.** Uniqueness was checked per profile identifier only. The adapter accepted:

- `remaining-loop` live with `loop-receipts-ledger` historical, which puts the ledger in both states;
- two live profiles covering the same lifecycle, dependency and decision surfaces;
- a row with no live profile.

**Chosen rule: validate in the adapter, not in the parsers.** The registry is the declaration, and REQ-003 requires an invalid configuration to fail explicitly, naming the offending entry. If parsers had to resolve overlaps, each would need a precedence rule: a hidden policy, applied late, and different per parser. So each profile now names the surfaces it covers. The adapter holds this as `FEED_PROFILE_SURFACES`, and each schema option's description ends with the same list, which a test checks. Two rules apply per row:

1. **The declared profiles cover pairwise-disjoint surfaces.** This one rule forbids:
   - two live readers of one surface;
   - one surface both live and historical;
   - two historical grammars for one surface, which is as ambiguous as two live ones.

   A violation fails at `$.loops[i].feed_profiles[j].profile`, naming the surface and the earlier entry. Surface names come from the closed set.
2. **At least one profile is live.** A violation fails at `$.loops[i].feed_profiles`. A loop PEC serves but that writes nothing live is better handled by removing its row, which is D-PEC-78's owner-gated act. The owner may amend this if archived loops should stay listed.

| Surface (design-note S#) | `shared-dev-loop` | `remaining-loop` | `remaining-items` | `loop-receipts-ledger` | `agentruns-json` |
|---|:-:|:-:|:-:|:-:|:-:|
| `work-graphs` (S1) | ✓ | | | | |
| `central-receipts` (S3) | ✓ | | | | |
| `memory-run-index` (S5) | ✓ | | | | |
| `status-lifecycle` (S6) | ✓ | ✓ | | | |
| `status-remaining` (S6, `## Remaining`) | | ✓ | ✓ | | |
| `dependency-registers` (S8) | ✓ | ✓ | | | |
| `decision-registers` (S9) | ✓ | ✓ | | | |
| `receipt-ledger` (S14) | | ✓ | | ✓ | |
| `json-run-evidence` (S15) | | | | | ✓ |

Under this table, PEC's row A (`shared-dev-loop` + `remaining-items` + `loop-receipts-ledger` + `agentruns-json`) and row A-R (`remaining-loop` alone) are both valid. A loop still on the old shape can declare `remaining-loop` with `agentruns-json`. `remaining-loop` cannot be combined with `shared-dev-loop`, `remaining-items` or `loop-receipts-ledger`. Every `loop_init_path` is read for loop identity regardless of profile, as PRD PEC-RCN-002 says, so it is not a profile surface.

### `agentruns-json` coverage (review point 3)

- **The PRD's scope.** PRD v2.3 §7.1 reads: RunRecord: "`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` are read as declared historical grammar or current evidence per the loop's feed profile". DependencyEdge: "`WORK_GRAPH.json` is read as a declared historical grammar where the loop's feed profile says so".
- **The fix.** Revision 1 pinned the profile to `execution/_Coordination/AgentRuns/`. Revision 2 describes it as "JSON run evidence anywhere under the loop's execution/ tree (WORK_GRAPH.json, STATUS.json, RUNTIME_SUMMARY.json), including AgentRuns/ and deliverable _run_records/". The identifier keeps its SCA-005 name for traceability to the accepted vocabulary term. The schema says so.
- **What PEC's row covers.** At `56a626c3b`, PEC has exactly one such file: `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/WORK_GRAPH.json` (D-PEC-85's working-items graph). There is no `STATUS.json` or `RUNTIME_SUMMARY.json` anywhere under `projects/pec`. The design note's §3.1 count of 13 PEC `STATUS.json` files does not reproduce at `56a626c3b`, and where it came from is UNKNOWN. PEC's row declares `agentruns-json` `historical`, so this file is read, as FX-PEC-0 expects.
- **Its basis.** It cites the D-PEC-94 record, which adopts work graphs and central receipts as PEC's run records. No PEC record states in so many words that JSON run evidence is historical; the citation supports it by implication. Question 2 lets the owner name another basis.

### Backward compatibility: version-1 files are rejected; the one checked-in file is migrated

- **A version-1 row cannot meet revision 1.5.** SOW-077 requires "each row declaring a closed, PEC-versioned feed profile". Accepting version 1 would mean one of two things:
  - inventing a profile, which is silent substitution, forbidden by the DEL-01-06 REQ-003/AC-003 contract;
  - returning loops with no profile, which SOW-077 forbids.
- **D-PEC-78 permits dual reading only "if needed", time-bounded and tested.** It is not needed. The only version-1 document is the checked-in default, which this act migrates. PEC runs nowhere, and no store or consumer holds registry data.
- **So the loader accepts exactly `schema_version: 2`.** Any other value, including 1, fails at `$.schema_version` with "expected integer constant 2; no other schema version is accepted".
- **The version-1 bytes are kept as a test fixture.** `schema_version_1.json` is byte-identical to today's `loops.json`, so the rejection is tested.
- **Version 1 stays strict and is not widened** (PRD v2.3 §16.3; CP1-V). Its bytes remain in Git history and in that fixture. The version-2 schema has its own `$id` (`https://chirality.local/pec/v2/config/loops.schema.v2.json`), so the two versions are not confused.

### Relation to DEL-01-06 (Gate 5 HOLD, SOW currency, records)

- **Lifecycle.** DEL-01-06 is `INITIALIZED` (`_STATUS.md` `20e6db02…e90d`).
  - The owner's Gate 5 ruling is in DEL-01-06 `_REVIEW.md` (`570506a6…cdac`) L45–48: "DEL-01-06 REVIEW Gate 5 — HOLD. Retain DEL-01-06 at INITIALIZED. This does not accept the produced artifacts, …". The D-PEC-75 source bytes were produced but never accepted.
  - This packet changes those unaccepted bytes and asks for no lifecycle change. It does not touch `_STATUS.md`, `_REVIEW.md` or `Review_Findings.csv`.
  - The SELF_CHECK evidence (RF-001, RF-002; registry 12/12) becomes historical evidence about the superseded bytes.
  - Any later Gate 5 re-entry is the owner's own act, and would review the version-2 bytes against the rebuilt Scope of Work.
- **Scope of Work currency.**
  - The accepted contract (`5fdcfd96…a2fa8`, revision-1.4 basis) still says "strict version-1" in CLM-003, TBD-002, REQ-001, REQ-005, CON-001 and AX-003. SCA-005 §B4 classes it `STALE_REBUILD_REQUIRED … gated on B6`, and the graph orders its rebuild after G1 (node S2).
  - REQ-005 says "a path, schema, or field-meaning change requires a separately governed migration without amending DEL-02-07, DEL-03-01, or DEL-09-02 merely for adapter details". This packet is that migration.
  - Until S2 lands, the new tests go beyond the revision-1.4 text. They check behaviour that revision 1.5 requires but the old contract does not declare, so the contract's wording (REQ-007) lags until S2 absorbs them.
  - This packet writes no SOW byte. AC-002 ("adding entries only, with no format change") stays true under version 2.
- **Records.** DEL-01-06 has no `MEMORY.md`; in PEC only DEL-01-03 has one. Under `projects/pec/AGENTS.md`, a MEMORY row needs the governing packet to name the path, so the administrative grant names it (question 6).

### SCA-006 does not bear on the registry

The owner accepted SCA-006 checkpoint 1 on 2026-09-25: "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded" (`checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md`, `0160dd88…50df`). It accepted the Impact Assessment at `93253b7d…b691`.

- That assessment's §7.1 classes DEL-01-06 `NOT_AFFECTED` ("no K-03, verify-before-rely, §8, access-class, auth, size or parity text").
- None of its 54 actions (`Amendment_Actions.csv`, `c5f90801…4891`) names SOW-077, SOW-094, DEL-01-06, DEL-02-08, DEL-02-09, the registry files or a feed profile.
- Its reliance envelope ("per-feed coverage and limitations") will consume the feeds the profiles declare, but it does not change how they are declared.

### Findings beyond the brief (disclosed)

1. **"A feed profile" or a list.** SOW-077 and the DEL-01-06 description say each row declares "a closed, PEC-versioned feed profile". The migration they foresee already needs two entries on one row, and PRD v2.3 PEC-RCN-002 reads receipts as "live or declared historical per profile". Option A therefore makes `feed_profiles` a list with at least one live entry and disjoint surfaces. Question 4 asks the owner to confirm this.
2. **The vocabulary is fixed here for the first time.** The accepted vocabulary term lists `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger` and `agentruns-json` as examples ("e.g."), and the design note calls its table "Example profiles". This packet makes those four and the new `remaining-items` the closed set, each at version 1.
   - `remaining-items` is not among the accepted examples.
   - The coverage of each profile is in the schema. Grammars stay in the parser deliverables (O-B2: "Path conventions and grammars live in PEC adapter code").
   - Adding a profile, version or surface later changes the schema bytes and the adapter. A treats that as a D-PEC code-plus-packet change within schema version 2, because no field is added and no field's meaning changes. Question 4.
3. **Path-normalization residual (inherited).**
   - The version-1 check rejects absolute paths, `..` segments and backslashes. It accepts `projects/./pec/x`, `projects//pec/x`, a trailing `/`, a leading space and `C:x`.
   - A keeps this rule unchanged and reuses it for `basis`, and the schema description states exactly what is checked.
   - Tightening it, for example by requiring `PurePosixPath(value).as_posix() == value` and no `.` segment, is a small amendment. It is not prepared.
4. **The version-1 tests had no unknown-field case,** although REQ-001 requires rejecting unknown fields. A adds one for rows and one for profile entries.
5. **Order under D-PEC-78 §4.3.** That section says: "The owner accepts the exact config/schema/test bytes only after deterministic schema and adapter contract tests and REVIEW." The prototype ran the tests, and the independent REVIEW of revision 1 ran on PR #928. Revision 2 changes bytes, so the reviewer's follow-up on this revision's bytes completes that order before the ruling.

## Exact change

All paths are relative to `projects/pec/`. The bytes are exact; the bound act script (below) carries every postimage.

### 1. Schema version 2 — `v2/config/loops.schema.json` (full postimage)

It is serialized as the version-1 file is: `json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True)` plus one final newline, with LF line endings. The preimage round-trips through the same rule byte for byte.

```json
{
  "$id": "https://chirality.local/pec/v2/config/loops.schema.v2.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "additionalProperties": false,
  "description": "Local configuration format naming the loops PEC serves and the closed, PEC-versioned feed profiles PEC reads each loop with. Schema version 1 is not accepted by the version-2 loader.",
  "properties": {
    "loops": {
      "description": "The configured loops PEC may read as non-authoritative file-truth locations.",
      "items": {
        "additionalProperties": false,
        "properties": {
          "feed_profiles": {
            "description": "The feed profiles PEC applies to this loop: PEC's reading hypothesis, never the loop's truth. At least one entry and at least one live entry; a profile identifier appears at most once per loop, and the profiles on one loop cover pairwise-disjoint surfaces, so no surface is read under two grammars or declared both live and historical.",
            "items": {
              "additionalProperties": false,
              "properties": {
                "basis": {
                  "description": "Citation to the loop's own record that supports this declaration. Normalized repository-relative path (no leading '/', no '..' segment, no backslash).",
                  "minLength": 1,
                  "type": "string"
                },
                "profile": {
                  "description": "Identifier from PEC's closed feed-profile vocabulary. Each option ends with the surfaces it covers. Path conventions and grammars for each profile live in PEC's adapters.",
                  "oneOf": [
                    {
                      "const": "agentruns-json",
                      "description": "JSON run evidence anywhere under the loop's execution/ tree (WORK_GRAPH.json, STATUS.json, RUNTIME_SUMMARY.json), including AgentRuns/ and deliverable _run_records/; the identifier keeps its SCA-005 name. Surfaces: json-run-evidence."
                    },
                    {
                      "const": "loop-receipts-ledger",
                      "description": "The loop's loop/LOOP_RECEIPTS.md receipt ledger, under that loop's grammar. Surfaces: receipt-ledger."
                    },
                    {
                      "const": "remaining-items",
                      "description": "The '## Remaining' sections of the loop's _STATUS.md files, read as deliverable-local records of open scope with their gate markers, never as a work-selection signal. Surfaces: status-remaining."
                    },
                    {
                      "const": "remaining-loop",
                      "description": "Loops that select work from _STATUS.md '## Remaining' items: lifecycle with those items, the loop/LOOP_RECEIPTS.md ledger as the receipt feed, dependency registers and decision registers. Surfaces: decision-registers, dependency-registers, receipt-ledger, status-lifecycle, status-remaining."
                    },
                    {
                      "const": "shared-dev-loop",
                      "description": "The shared development-loop method: undertaking work graphs (execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md), central receipts (execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md), the deliverable MEMORY.md run index, _STATUS.md lifecycle, dependency registers and decision registers. Surfaces: central-receipts, decision-registers, dependency-registers, memory-run-index, status-lifecycle, work-graphs."
                    }
                  ],
                  "type": "string"
                },
                "state": {
                  "description": "live: the loop currently writes this generation. historical: the generation is frozen, and its silence is never reported as staleness.",
                  "enum": [
                    "historical",
                    "live"
                  ],
                  "type": "string"
                },
                "version": {
                  "const": 1,
                  "description": "Version of the selected profile; every profile in this vocabulary is at version 1.",
                  "type": "integer"
                }
              },
              "required": [
                "basis",
                "profile",
                "state",
                "version"
              ],
              "type": "object"
            },
            "minItems": 1,
            "type": "array"
          },
          "loop_id": {
            "description": "Stable lower-case identifier for one configured loop.",
            "minLength": 1,
            "pattern": "^[a-z][a-z0-9-]*$",
            "type": "string"
          },
          "loop_init_path": {
            "description": "Repository-relative path to the loop's governed LOOP_INIT.md surface.",
            "minLength": 1,
            "type": "string"
          }
        },
        "required": [
          "feed_profiles",
          "loop_id",
          "loop_init_path"
        ],
        "type": "object"
      },
      "minItems": 1,
      "type": "array"
    },
    "schema_version": {
      "const": 2,
      "description": "Version of this local loop-registry configuration format.",
      "type": "integer"
    }
  },
  "required": [
    "schema_version",
    "loops"
  ],
  "title": "PEC local loop registry configuration v2",
  "type": "object"
}
```

### 2. The default instance — `v2/config/loops.json`

The one existing row keeps `loop_id` and `loop_init_path` and gains `feed_profiles`, and `schema_version` becomes 2. No row is added or removed.

**Option A** (question 2 answered "migrated"; postimage `aad704700748055e8f5cc1ec0c4f3a29c000c775994e1280dcf651952094678e`):

```json
{
  "loops": [
    {
      "feed_profiles": [
        {
          "basis": "projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md",
          "profile": "shared-dev-loop",
          "state": "live",
          "version": 1
        },
        {
          "basis": "projects/pec/AGENTS.md",
          "profile": "remaining-items",
          "state": "live",
          "version": 1
        },
        {
          "basis": "projects/pec/AGENTS.md",
          "profile": "loop-receipts-ledger",
          "state": "historical",
          "version": 1
        },
        {
          "basis": "projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md",
          "profile": "agentruns-json",
          "state": "historical",
          "version": 1
        }
      ],
      "loop_id": "pec",
      "loop_init_path": "projects/pec/loop/LOOP_INIT.md"
    }
  ],
  "schema_version": 2
}
```

**Option A-R** (question 2 answered "as accepted": `remaining-loop`; postimage `6e1321e32f72b0fc9f9d987a3175266550a23fa40230df0a61418cfccd4c7961`). The basis cites the record whose I-7 deferral kept PEC on that shape. D-PEC-94 has since exercised that deferral, so the citation is historical.

```json
{
  "loops": [
    {
      "feed_profiles": [
        {
          "basis": "projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md",
          "profile": "remaining-loop",
          "state": "live",
          "version": 1
        }
      ],
      "loop_id": "pec",
      "loop_init_path": "projects/pec/loop/LOOP_INIT.md"
    }
  ],
  "schema_version": 2
}
```

### 3. The port field — `v2/src/pec_v2/core/ports/loop_registry.py` (full postimage, unchanged from revision 1)

`RegisteredLoop` gains one field, `feed_profiles: tuple[FeedProfile, ...]`. It is required and has no default. Two core-owned types support it. The port method and its signature are unchanged, and the core still imports no JSON, filesystem or adapter module (only `dataclasses`, `enum` and `typing`).

```python
"""Typed core contract for discovering the loops PEC is configured to serve."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol


class FeedProfileState(Enum):
    """Whether a declared feed-profile generation is live or historical for its loop."""

    LIVE = "live"
    HISTORICAL = "historical"


@dataclass(frozen=True, slots=True)
class FeedProfile:
    """One closed, PEC-versioned feed profile declared for a registered loop.

    A profile is PEC's reading hypothesis about the loop's file truth, never the
    loop's truth. ``basis`` is the repository-relative locator of the loop's own
    record that supports the declaration.
    """

    profile: str
    version: int
    state: FeedProfileState
    basis: str


@dataclass(frozen=True, slots=True)
class RegisteredLoop:
    """One configured loop, the locator of its file truth, and its feed profiles."""

    loop_id: str
    loop_init_path: str
    feed_profiles: tuple[FeedProfile, ...]


class LoopRegistry(Protocol):
    """Core-owned capability port for the configured registered-loop set."""

    def registered_loops(self) -> tuple[RegisteredLoop, ...]:
        """Return the complete validated registered-loop set."""
        ...
```

`v2/src/pec_v2/core/ports/__init__.py` and `v2/src/pec_v2/core/__init__.py` each add `FeedProfile` and `FeedProfileState` to their existing re-export line and `__all__`. Nothing else in those files changes.

### 4. The adapter — `v2/src/pec_v2/adapters/config/loop_registry.py`

The behaviour is listed here; the exact bytes are in the act script and `optionA_vs_56a626c3b.diff`.

- It accepts only `schema_version` 2, as described under backward compatibility.
- Each row needs exactly `loop_id`, `loop_init_path` and `feed_profiles`.
  - A missing field fails at `$.loops[i].<field>` with "required field is missing".
  - An unknown field fails with "field is not defined by schema v2".
- `feed_profiles` must be a non-empty list of objects with exactly `profile`, `version`, `state` and `basis`. Each failure is located at `$.loops[i].feed_profiles[j].<field>`:
  - `profile` must come from the closed vocabulary `FEED_PROFILE_VERSIONS`. This module constant maps each of the five identifiers to `{1}`.
  - A profile repeated in a row fails at the second occurrence, naming the first.
  - `version` must be an exact `int` in that profile's version set, so `True` and `"1"` are rejected.
  - `state` must be the string `live` or `historical`.
  - `basis` must pass the same repository-relative path rule as `loop_init_path`, now one shared helper.
  - **New in revision 2:** the profiles on a row must cover pairwise-disjoint surfaces, per `FEED_PROFILE_SURFACES` and the table above. An overlap fails at the later entry's `.profile`, naming the surface and the earlier entry.
  - **New in revision 2:** at least one profile must be `live`; otherwise the row fails at `$.loops[i].feed_profiles`.
- The error class is unchanged, as are the file-level failures (absent, unreadable, malformed) and the no-partial-set rule.
- No failure message echoes a document value, except a profile identifier or surface name already validated against the closed vocabulary. Locations name keys, as before. A test now proves this for every field.

### 5. Tests and fixtures

| Path | Act | Content |
|---|---|---|
| `v2/tests/config/test_json_loop_registry.py` | modify | The expected default is updated. The schema test checks: the version-2 `$id`; every field description; each vocabulary entry's description; that the surfaces listed in each description equal `FEED_PROFILE_SURFACES`; and that the schema's profile set, version and states equal the adapter's and the port's. New tests: `test_schema_version_1_is_rejected_with_location`; `test_invalid_feed_profiles_are_rejected_with_location` (24 located sub-cases, including unknown fields, non-string `state`, `null` `profile`, the ledger both live and historical, two live lifecycle readers, Remaining read twice, and no live profile); `test_failures_do_not_echo_document_values` (6 fields); `test_additional_loops_need_entries_only` (a second row loads with entries only). `test_invalid_document_never_returns_partial_or_empty_set` also covers the version-1 fixture and a document whose second row alone is invalid |
| `v2/tests/config/test_loop_registry_contract.py` | modify (unchanged from revision 1) | Immutability now also covers `feed_profiles` and `FeedProfile`. New `test_registered_loop_carries_the_typed_feed_profile_field` pins the field names and order of both dataclasses and the two state values. The three existing port, core-import and stdlib tests are unchanged |
| `v2/tests/config/fixtures/duplicate_loop_id.json`, `missing_loop_id.json` | modify | Migrated to version 2 with one live `shared-dev-loop` entry per row, so each still fails at its intended location |
| `v2/tests/config/fixtures/schema_version_1.json` | **create** | Byte-identical to today's `loops.json` (`4ce07ad0…d32e`) |
| `v2/tests/config/fixtures/malformed.json` | unchanged | Still fails as malformed JSON before any version check |

The suite goes from 12 to 17 tests. The mapping to DEL-01-06's verification methods is:

| Method | Tests |
|---|---|
| **VER-001** format against the default and malformed fixtures | `test_schema_documents_every_field_and_the_exact_default`, `test_checked_in_default_has_exactly_the_pec_loop`, `test_schema_version_1_is_rejected_with_location`, `test_missing_loop_id_…`, `test_duplicate_loop_id_…`, `test_malformed_json_…`, `test_invalid_feed_profiles_are_rejected_with_location`, `test_failures_do_not_echo_document_values` |
| VER-002 one loop at P1; more loops by entries only | `test_checked_in_default_has_exactly_the_pec_loop`, `test_additional_loops_need_entries_only` |
| **VER-003** invalid, unreadable and absent fail explicitly, with no partial set | `test_absent_file_…`, `test_unreadable_path_…`, `test_invalid_document_never_returns_partial_or_empty_set`, `test_malformed_json_…` |
| VER-004 consumer interface carries no path or serialization detail | `test_port_has_only_the_typed_capability_method`, `test_registered_loop_is_immutable`, `test_registered_loop_carries_the_typed_feed_profile_field` |
| VER-005 no third-party dependency or network call | `test_core_imports_no_adapter_or_outer_io_module` and `test_implementation_uses_only_stdlib_and_no_network_module`, plus `v2-core-posture` (the DEL-01-05 enforcement) and `v2/tests/enforcement` |
| VER-006 the suite runs and passes | `v2-loop-registry` |

## Options

- **A — schema version 2, closed vocabulary with surface coherence, port field, migrated PEC row (recommended).**
  - One act on **11 product paths**: 10 modified and 1 created (the version-1 fixture). Nothing is deleted.
  - PEC's row declares `shared-dev-loop` and `remaining-items` live, and `loop-receipts-ledger` and `agentruns-json` historical. This takes question 2 as "migrated" and question 3 as (a).
  - `software-workflow.json` is unchanged; its rules already select all five checks for these paths.
- **A-R — as A, but PEC's row declares `remaining-loop` alone, as the accepted Notes text says.** Same 11 paths; only `loops.json` and `test_json_loop_registry.py` differ (postimages below). The migration row change then needs a later packet of its own. Choose A-R if the owner wants the migration ruled separately from the schema act, or wants the accepted text followed literally until then.
- **Amend.** The owner changes the scope and the packet is re-prepared. Examples:
  - a different vocabulary, surface table or coherence rule (question 4);
  - the Remaining sections historical or unread (question 3 (b), (c));
  - a time-bounded dual read of version 1 (question 5);
  - tightened path normalization (finding 3);
  - different `basis` citations.
- **Defer.** Nothing opens.
  - The registry stays version 1 with no profiles, and SOW-077 and SOW-094 stay unmet in source.
  - The DEL-01-06 SOW rebuild (S2) waits, since SCA-005 gates it on this packet, or it proceeds against unimplemented text ("SOW first").
  - DEL-02-08 discovery "per the loop's declared feed profile" has no declaration to read.
  - No consumer exists yet, so deferring is not unsafe.

A narrower source-only option is not offered. Every part of A is needed for the others to pass: a version-2 loader rejects the version-1 default, and the default cannot declare profiles without the schema and port. Splitting off the PEC-row decision is what A-R does.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** for PKG-01 / DEL-01-06. The script writes only the paths below, relative to `projects/pec/`. Preimage SHA-256 values were read at `56a626c3b` and are equal at `abfd0897b`.

| # | Path | Act | Preimage SHA-256 | Postimage SHA-256 (A) |
|---|---|---|---|---|
| 1 | `v2/config/loops.json` | modify | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` | `aad704700748055e8f5cc1ec0c4f3a29c000c775994e1280dcf651952094678e` |
| 2 | `v2/config/loops.schema.json` | modify | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | `27b8ff110c07bbba67b17ce98955db9e665f67b55cff92cbe3a34011800f04ce` |
| 3 | `v2/src/pec_v2/core/ports/loop_registry.py` | modify | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` | `a509bfb74920172a86ac21aff6a67245cd3248c5d73ef4e7427966069099c8a9` |
| 4 | `v2/src/pec_v2/core/ports/__init__.py` | modify | `669e1569216722509dcea0ae5ed42dc4a0ca856a196676568ee78d7a38a1edeb` | `e44bf7f00c8ef2cfa5f8006ef2834feb020063df63a3b4b8d8cbd8f359174ff7` |
| 5 | `v2/src/pec_v2/core/__init__.py` | modify | `33c54e244e8e19b66cb2c53c81fa747979f6d512f227f7a56e3f8d57cfb9ff4a` | `0e699a54d6bc202ff7a90c25fdb355da5ed2db185709c3a399870c1b0309c42d` |
| 6 | `v2/src/pec_v2/adapters/config/loop_registry.py` | modify | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` | `4fc4bbf72e2b0cc7507a020fe4cce93c793ab2d5b65f2cc6dbbc2db2c6328ad4` |
| 7 | `v2/tests/config/test_json_loop_registry.py` | modify | `d7efb486287d3703aa9ea007eb5376eba95689286bb322c887eeca8b193ac956` | `d410afa5a32d4fd11384a4960b1ea28352f3f930f8902488e28b46d392dc3fae` |
| 8 | `v2/tests/config/test_loop_registry_contract.py` | modify | `49b2f6a3b5088bceb82dc393cce050b8800af3a5ac5d34b3b6a3d7b71c01111b` | `b05ed8719c59258998b1c483456b66bd8d4a4d3bc4f68cdd6fb5c02541db7106` |
| 9 | `v2/tests/config/fixtures/duplicate_loop_id.json` | modify | `2e65c719af6c9eb7e170fb25d437b928847dc8d617c056093de213673b3e3396` | `6875f50023f1ad34a45c1af4b0a65316260c45aa05562ce45bb2d9bd8fd13c7e` |
| 10 | `v2/tests/config/fixtures/missing_loop_id.json` | modify | `2155849d9419f0239dca7a69d919ca9ee46a6434106d5326d85bc8c70afc5257` | `f4255b2483a014b542fb7f25c4314ff75dabb5cebbcfe751a2ad3df425f29598` |
| 11 | `v2/tests/config/fixtures/schema_version_1.json` | create | absent | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |

Under A-R, two postimages differ: `v2/config/loops.json` `6e1321e32f72b0fc9f9d987a3175266550a23fa40230df0a61418cfccd4c7961` and `v2/tests/config/test_json_loop_registry.py` `586fcd5ead4bbb19e76a125da972910ea1e93a610b2d74758fcfd7fb89a6ee01`. The path-list SHA-256 (the 11 paths, sorted, newline-terminated) is `b5db12e59bec0188b1798e8ccf7a3c09300c44e5dbcdf31c16a64aff5e84c73c`.

These paths stay unopened. The script checks each is unchanged before writing:

| Path | SHA-256 |
|---|---|
| `v2/tests/config/fixtures/malformed.json` | `f37303491c50fa74756f547929f09c99900abfad5a9310cc2b46beb5027425b0` |
| `v2/src/pec_v2/adapters/config/__init__.py` | `7a9bdbc59b96d3c9f306af483d18d6c0b23b7071481fd6ab79204ba398513cba` |
| `v2/src/pec_v2/adapters/__init__.py` | `8c80e607671eef1a35dca0334503deb151418c03b618af0c4577514d0184ef22` |
| `v2/src/pec_v2/__init__.py` | `ae46d431c13413d5bcbb6ab60a97f6db09510dd97903c1f2a8586a3567b17c1e` |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |
| `v2/config/service_core_posture.json` | `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed` |

The grant opens no other source, test, contract, configuration, documentation, workflow, decomposition, SOW, `_STATUS.md`, Root, CI, sister-project, tier-0 or frozen-corpus path.

### Generation method (binding)

The bytes come from one run of `apply_d96.py`, **SHA-256 `b314213a7b4e615fd97c6c1b7f0fdac170c8c7c493354e2f54c390cc35a36dd4`**. It is stdlib-only Python, prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/apply_d96.py --repo "$(git rev-parse --show-toplevel)" [--pec-row remaining]
```

Option A is the default; A-R adds `--pec-row remaining`.

- **Checks before any write:**
  - the six must-remain files;
  - the 10 preimages, and that the fixture to be created does not exist;
  - that every embedded postimage decodes to its pinned SHA-256;
  - that the write set equals the grant.
- **The act.** It writes, re-hashes every written file, and reports `READ`, `WRITE` and `UNCHANGED` lines.
- **Failure behaviour.** It exits 1 with nothing written on any failure, and exits 1 if run a second time. `--check-only` renders and checks without writing.
- **No slot rule.** The product bytes contain no date.
- **Preparation aids (not bound):** `build_apply_d96.py` (`a0a71e6fd3519d40a773d2d62c341a2c089f7e8e21dd8f22d68fa11d3ac1831d`), `apply_d96.template.py` (`4fe61dc1b900e5dfa4c8ed9bec3dc8308537feee9adb59db6172c04fb4258290`, unchanged from revision 1) and `build_json_postimages.py` (`f3dfb9c8b587e7a562178302bb0c43f825953ad705a9b110143117a602b8998b`).

## Finite verification

Run the registered checks from `projects/pec` (cwd `.`, as registered), and `harness-self-check` from the repository root.

- Use an explicit interpreter of Python 3.10 or later (the registry requires 3.10+), record its path and version, and set `PYTHONDONTWRITEBYTECODE=1`.
- Record every command, exit code and output in the run root.
- The manager may run `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <ID> --output <run-root>/checks/<ID>.json` from the repository root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | the script's built-in checks; the ruling and its register row on fetched `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on each of the 13 targets before dispatch, and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere. Otherwise stop and route the discrepancy |
| Selection | `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json <the 11 paths>` | exactly `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` |
| **`v2-loop-registry` (VER-001, VER-003 rerun)** | `python3 -m unittest discover -s v2/tests/config -p test_*.py` (verbose run recorded, each test mapped to its VER method as tabled above) | exit 0; **Ran 17, OK** (12 before) |
| `v2-store-guard` (`v2/src/pec_v2/**` rule, D-PEC-87 X-1) | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | exit 0; Ran 13, OK. The store still imports the changed `core/ports` package |
| `v2-core-posture` (VER-005; DEL-01-05 enforcement; `always_checks`) | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | exit 0; `"verdict": "PASS"`, zero findings; `core_tree_sha256` changes from `88f590c0…c016` to `dd7e1dda…6e5a`; config and workflow hashes unchanged |
| DEL-01-05 enforcement tests | `python3 -m unittest discover -s v2/tests/enforcement -p test_*.py` | exit 0; Ran 28, OK |
| `v2-api-contract` (`always_checks`) | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | exit 0; Ran 6, OK |
| `harness-self-check` (`always_checks`; every PR) | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0; output identical to the pre-act run. On the prototype it was `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` both times, stdout `e5f9ff70…d110` |
| Receipts validator (every PR) | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0; output unchanged |
| Mutation evidence | `mutate_d96.py projects/pec` (copied into the run root) | baseline passes; M1–M19 each CAUGHT; `RESULT PASS` |
| Byte identity | recompute SHA-256 of the 11 paths | equal to the grant table for the chosen option |
| Basis citations | `test -f` on each `basis` and `loop_init_path` in the new `loops.json` | all present at the act commit |
| Containment | `git diff --name-status origin/main...HEAD` | the 11 paths, plus the run root and, if question 6 is answered yes, `MEMORY.md`. HELP_HUMAN's own records may ride the same PR: the D-PEC-96 register row, ruling and proposal files under `execution/_Coordination/_DECISIONS/`, the work graph, and the undertaking's `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/` briefs, returns and receipt, all under the default-writable `execution/_Coordination/**`, plus `docs/STATUS.md` and `README.md` under D-PEC-88. Any of them may instead go in a separate PR. Nothing else |
| Whitespace and encoding | `git diff --check origin/main...HEAD`; non-ASCII scan of the 11 postimages | clean; 0 non-ASCII bytes |

Decomposition and dependency validators do not apply, because no register, decomposition or dependency file changes. The strict register validator was run on the prototype anyway; its output was byte-identical before and after.

### Independent verifier

A fresh read-only TASK that authored nothing applies `.agents/skills/software-code-review/SKILL.md` and returns a verdict file. Defects return to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`. The run-root script hashes to `b314213a…6dd4`, and the recorded preimages match.
2. **Reproduction.** It reruns the script with the ruled option on a fresh `git archive` export of the pre-act `origin/main` and gets byte-identical files.
3. **The fixed checks.** It reruns the verification table and gets the same results, including the mutation run.
4. **Semantics.**
   - The schema documents every field, and each profile's surface list matches the adapter's.
   - The adapter enforces exactly what the schema states, including disjoint surfaces and at least one live profile.
   - The vocabulary, versions and states agree across schema, adapter and port.
   - Every failure is located, none returns a partial set, and none echoes a document value.
   - Version 1 is rejected, not read.
   - Core imports stay stdlib-only, with no I/O module.
   - The PEC row matches the ruled answers to questions 2 and 3, and its `basis` paths exist and say what they are cited for.
   - The tests assert no criterion beyond revision-1.5 SOW-077/094, the DEL-01-06 SOW's surviving clauses and this packet (see the SOW-currency note).
5. **Containment.** Nothing changed outside the containment row above. In particular these are unchanged: `software-workflow.json`, `service_core_posture.json`, the storage and API files, `malformed.json`, DEL-01-06 `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` and `_CONTEXT.md`, any decomposition file, and `docs/PRD.md`.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-06 only, for this act.
  - The manager runs the reliance preflights and the script. No author TASK is needed, because the bytes are bound. The manager may instead dispatch a bounded TASK to run the script under `workflows/software-bounded-implementation/WORKFLOW.md`.
  - One fresh read-only TASK is the verifier.
- **Run root.** `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/**`, a new folder beside the D-PEC-75 and D-PEC-77 records. It holds:
  - `apply_d96.py` (exact bytes) and its report;
  - `mutate_d96.py` and its output;
  - the check outputs and preflight results;
  - `RUN.md`;
  - `VERIFIER_VERDICT_NN.md`.

  The earlier `_run_records/*` stay immutable.
- **`MEMORY.md` (question 6).** If the owner agrees, the act creates `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`). The path does not exist at `56a626c3b`. At closeout, the undertaking's M1 node writes one run row: the run ID, the date, "schema version 2 source act under D-PEC-96", the PR and the central receipt.
- **Not opened.**
  - DEL-01-06 `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` and `Dependencies.csv`.
  - Every other deliverable.
  - `docs/STATUS.md` and `README.md`, which HELP_HUMAN maintains under D-PEC-88 and names in the graph.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for the manager and the verifier, as under D-PEC-91 and D-PEC-95, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, the graph and the central receipt are HELP_HUMAN's.

## Rollback

- **During execution.** The script writes nothing unless every check passes. If a later check fails, discard the branch or worktree; nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR of the act restores the 10 preimages tabled above. It removes the created fixture, the run root and, if created, `MEMORY.md`. History is preserved and no reset is made. HELP_HUMAN's records that rode the PR are reverted with it, or kept by a partial revert; that is HELP_HUMAN's choice.
- **Stores and consumers.**
  - No store holds registry data and no consumer reads the port, so there is no migration or consumer rollback to do.
  - The version-1 bytes also survive as `schema_version_1.json` until reverted.
  - If the revert happens after a consumer has been built against `feed_profiles`, that consumer's own packet must roll back first.

## Limits

This proposal, and any ruling selecting A, A-R or an amendment, grants none of the following:

- **No lifecycle change.** DEL-01-06 stays `INITIALIZED` and its Gate 5 HOLD stands. No `_STATUS.md` is touched and no `## Remaining` entry is written or changed; `remaining-items` only reads them.
- **No DEL-01-06 Gate 5 act and no SOW change.** Gate 5 is not re-entered, RF-001 and RF-002 are not reopened, and no `ScopeOfWork.md` byte changes. The rebuild remains graph node S2 under its own packet.
- **No PRD or decomposition change.** No write to `docs/PRD.md`, `_Decomposition/**`, any register, any `_CONTEXT.md`, any `_REFERENCES.md` or any dependency file. The stale "declares `remaining-loop` now" sentences stay until their own currency acts.
- **No `CHECKING`, `ISSUED`, artifact acceptance, or any readiness or reliance claim.** CHECKING is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it.
- **No other registry row.** No loop is added or removed.
- **No consumer, parser, fixture suite or grammar.** DEL-02-0x and X1 remain their own packets.
- **No change to other surfaces.** `software-workflow.json`, CI, Root, tier-0, sister-project, instruction and frozen-corpus surfaces are untouched.
- **No duty on any other loop.** A profile is PEC's reading hypothesis, never the loop's truth. Listing a loop creates no duty, cadence or authority (D-PEC-78 O-A).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, A-R, amend or defer.** Recommendation: **A**.
2. **PEC's own row: the migration row change, ruled here as its own item.**
   - **The departure.** Option A departs from the letter of the CP2-accepted §B6 ("PEC's own `pec` row `remaining-loop`, Q8 (a)"; "D-PEC-86 I-7 … stays deferred") and of SCA005-CP1-Q8 (a). Their premise, that PEC still selected from `## Remaining` with I-7 deferred, ended when D-PEC-94 exercised I-7 after checkpoint 3. The migration they foresee as "one owner-gated row change" is what this question asks.
   - **Migrated (recommended):** `shared-dev-loop` v1 `live` (basis: the D-PEC-94 record), `loop-receipts-ledger` v1 `historical` (basis: `projects/pec/AGENTS.md`) and `agentruns-json` v1 `historical` (basis: the D-PEC-94 record, by implication; see review point 3). The Remaining sections are question 3.
   - **As accepted:** `remaining-loop` v1 `live` alone (option A-R). The migration then needs a later ruling.
   - **Other:** state the profiles and basis citations.

   Either answer is within the accepted scope. Neither needs a scope change.
3. **PEC's `## Remaining` sections** (57, kept as records whose gate markers still bind their items).
   - **(a) Read them through the new records-only profile `remaining-items`, `live`, basis `projects/pec/AGENTS.md` (recommended).**
   - (b) The same profile, but `historical`: read, and never flagged stale.
   - (c) Leave them unread. PEC's orientation would then not show them.

   Under A-R the question is moot, because `remaining-loop` reads them.
4. **Vocabulary, surfaces and row shape.** Confirm:
   - the closed vocabulary of five profiles, each at version 1, with the coverage and surface lists in the schema; `remaining-items` is new, and `agentruns-json` now covers JSON run evidence anywhere under `execution/`;
   - `feed_profiles` as a non-empty list, each profile at most once per row;
   - the coherence rules: disjoint surfaces and at least one live profile, enforced at load;
   - that adding a profile, version or surface later is a D-PEC code-plus-packet change within schema version 2.

   Recommendation: **confirm**. Alternatives by amendment: a smaller vocabulary; exactly one profile per row; leaving coherence to the parsers; allowing all-historical rows; or a new schema version for every vocabulary change.
5. **Version-1 files.** Recommended: reject them with a located error, with the one checked-in default migrated by this act. The alternative is a time-bounded, tested dual read (amend); D-PEC-78 §4.2 allows one "if needed". It is not needed, and it would need a defaulting rule that REQ-003 forbids.
6. **Records.** Recommended: create DEL-01-06 `MEMORY.md` from the template so the undertaking's closeout can write the run row. The alternative is to record this run only in the graph and central receipt and complete without the row; `projects/pec/AGENTS.md` allows either on your decision. The run root under DEL-01-06 `_run_records/` is part of the grant either way.
7. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in fresh `mktemp -d` directories under the host's temporary area, outside the session scratchpad and the checkout.

- `base` is a `git archive` export of the whole tree at `56a626c3b`.
- Each prototype is an APFS clone (`cp -Rc`) of `base` with a variant applied.
- For `harness-self-check` and `git diff`, the base clone and the option-A prototype were made throwaway repositories: `git init`; an `objects/info/alternates` entry pointing read-only at the source object store; `git read-tree 56a626c3b`; `update-ref HEAD` inside the export only.

Nothing was written to the checkout or its repository. The interpreter was Python 3.13.7 (CPython), and the local date was 2026-09-25.

| Command (scratch) | Exit | Result |
|---|---|---|
| five registered checks on `base` via `run_registered_checks.py` | 0 ×5 | api 6 OK; registry 12 OK; store 13 OK; posture PASS, 0 findings, core tree `88f590c0…c016`; harness `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` |
| the same on the option-A prototype | 0 ×5 | api 6 OK; **registry 17 OK**; store 13 OK; posture PASS, 0 findings, core tree `dd7e1dda…6e5a`; harness output byte-identical to `base` (`e5f9ff70…d110`) |
| `v2/tests/enforcement` on `base` / prototype | 0 / 0 | Ran 28, OK / Ran 28, OK |
| `select_affected_checks.py` over the 11 paths | 0 | all five checks |
| `apply_d96.py --check-only` on a fresh clone | 0 | 11 RENDER; `diff -rq` shows the tree unchanged |
| `apply_d96.py` (A) on a fresh clone | 0 | 6 UNCHANGED, 11 READ (10 preimages, 1 absent), 11 WRITE; `v2/` byte-identical to the hand-applied prototype; `diff -rq` against `base` shows exactly the 11 paths |
| `apply_d96.py` rerun on the applied clone | 1 | "preimage mismatch v2/config/loops.json …; nothing written" |
| `apply_d96.py` on a clone with `software-workflow.json` altered | 1 | "must-remain file differs: software-workflow.json; nothing written"; no file created |
| `apply_d96.py --pec-row remaining` (A-R) on a fresh clone | 0 | 11 WRITE; differs from A in exactly `loops.json` and the test file; registry suite Ran 17, OK |
| `mutate_d96.py` on the applied A clone | 0 | baseline OK; **M1–M19 all CAUGHT**. M1–M13 as in revision 1. M14 drop the surface-disjointness check; M15 drop the at-least-one-live rule; M16 `remaining-loop` stops claiming the ledger; M17 allow overlap between live and historical; M18 echo an invalid `state` value; M19 default drops `remaining-items` |
| `validate_pec_loop_receipts.py --repo-root .` on `base` / prototype | 0 / 0 | VALID; identical apart from the absolute path prefix |
| `validate_decomposition_registers.py --strict projects/pec/execution` on `base` / prototype | 0 / 0 | 0 errors / 0 warnings; output byte-identical |
| prototype `git diff --check`; non-ASCII scan of the 11 postimages | 0 | clean; 0 non-ASCII bytes |
| path-rule probe (revision 1, same rule) | 0 | `projects/./pec/AGENTS.md`, `projects//pec/AGENTS.md`, `projects/pec/`, `C:x` and a leading-space path are accepted (finding 3, inherited) |
| `pec_reliance_hold.py … --operation exact-correction-preparation` from `base/projects/pec` | 0 ×13 | `ALLOW` |

Scratch artifacts are in the preparer's `g1/` folder, with hashes in `g1/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `apply_d96.py` (the bound act script) | `b314213a7b4e615fd97c6c1b7f0fdac170c8c7c493354e2f54c390cc35a36dd4` |
| `mutate_d96.py` (mutation runner) | `c438e7acd67e1138ee8b816d752780ffad52a7bf6a64231ea4c31c75ad146ad7` |
| `build_apply_d96.py`, `apply_d96.template.py`, `build_json_postimages.py` (preparation aids) | `a0a71e6f…831d`, `4fe61dc1…8290`, `f3dfb9c8…998b` |
| `evidence/optionA_vs_56a626c3b.diff` (A; includes the created fixture) | `b8d7d9ab6ab24cf5d382842dcf7d2bb75de5940224ca2e9b864457f9aa986169` |
| `evidence/optionAR_vs_optionA.diff` | `ca122d953fec5d53af3e25939f132ef0abb66ab6c39e2f3478ae5386d331a928` |
| `evidence/CHECKS_SUMMARY.txt`, `evidence/mutate_d96.out`, `evidence/optionA_v2-loop-registry_verbose.txt`, `evidence/preflight.txt`, `evidence/actA.report.txt`, `evidence/actAR.report.txt`, `evidence/preimages.txt` | in `SHA256SUMS` |
| `postimages/optionA_v2/**`, `postimages/optionAR_overrides/*` (postimage copies for review) | in `SHA256SUMS` |

The basis read for preparation, at `56a626c3b`:

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `projects/pec/docs/PRD.md` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `projects/pec/execution/_Decomposition/_LATEST.md` | `626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd` |
| `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Impact_Assessment.md` | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| `projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| `projects/pec/execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md` | `4b9ccb9f3e96e66a9566479858deac42f5616315045542ba1b5663fef30d12da` |
| `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/CHECKPOINT1_RESOLUTION_NOTE.md` | `af4e46d0dba2fb71c8f4aceca69098d81806b9add1ac960f074aa8fe949b0ad2` |
| `projects/pec/execution/_Coordination/D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md` | `426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-78_oi_003_loop_registry_home.md` | `3f91ea6a18360d950f3cecce755ee929cdc78c53651d0b2774a3c93aa290a565` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` | `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md` | `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-95_RULING_2026-09-25.md` | `51dceb7136c24c1dea2f68c2338f66781de17fb2b63a8caf8bc719dd5a4e2beb` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md` | `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` | `bf0046cb455e9ac335b620c0ba4d77bdd76f3f5b9dd85465a7258cff749e347f` |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | `d94bfeabf370bd8749376d17fe3f57d5ee96afe424e70b0b4899d769fdb2b59e` |
| `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` | `ac0db3b444e41e2e94cdbbf7bb4625de56c236f944ba8ef78a1efc5ac3560be7` |
| `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Impact_Assessment.md` | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` |
| `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/Amendment_Actions.csv` | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` |
| `_DomainEngines/_DECISIONS/D-T0-15_pec_loop_goal_fences.md` | `95c245b5b78d102e4531a132aab7d010b320c5c4e1065875c3f08d6c1ff70b09` |
| `_DomainEngines/_DECISIONS/D-T0-19_pec_appdev_bridge_lane.md` | `46a9a9d281e4eb1891c6a9215df65069154b838aaaf1ab8eb751065d5511f1c4` |
| `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |
| `projects/pec/execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `projects/pec/software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `5fdcfd96834509e32a4df1fc001932fe7a0c5d4c5d96becb9acca0be3c4a2fa8` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_STATUS.md` | `20e6db0216943cf93d734cf97a18c50ece47706e6a012e47580aea9745e5e90d` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md` | `1362ed668436b5af79fe54dd5f7ab660dac9ddd29dad2a0d1b0adebb01ad5919` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REFERENCES.md` | `6e640cf84b3beb619c7503c7702017d786b80da237ae1be8ea01275c6d9c63b1` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_REVIEW.md` | `570506a614df62e10f3e5c122614e525a5e563f972835b8a845ec2bdf244cdac` |
| `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/Review_Findings.csv` | `f114d52b264109d9c89b9f519b6c532a3dc4cf4f1e38a1b1297055dbd647fd8c` |
| `projects/pec/loop/LOOP_INIT.md` | `c97d49fff5c2fabca1c9c05b44bcde958e46fccb067d512ce93779d4cfad821b` |
| `projects/pec/loop/LOOP_RECEIPTS.md` | `7569bd6055f44ae4d55a58a0c34aa8e5eb59f2fdceb8fa31a7cde942555bc922` |
| `docs/templates/MEMORY_TEMPLATE.md` | `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a` |
| `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md` | `0160dd881c0501e95c7245b71ffccffc332240573bb96a31196ed492c67250df` |
| `.agents/skills/software-code-review/SKILL.md` | `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca` |
| `workflows/software-bounded-implementation/WORKFLOW.md` | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| Brief G1 (scratch) | `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node G1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
