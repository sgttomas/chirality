# D-PEC-96 — Loop-registry schema v2 with closed feed profiles (SCA-005 §B6 registry source packet) — proposal

Status: **PROPOSAL / AWAITING_RULING** (revision 4). Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node G1) for the PEC loop, 2026-09-26 (session date), from brief `G1_REGISTRY_SOURCE_PROPOSAL.md` (SHA-256 `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1`), as revised on HELP_HUMAN's relayed instructions. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. It asks for no lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row and the filed copy of this proposal. At `8f9bd314c` the register's D-PEC-96 row reads `PROPOSAL / AWAITING_RULING`, and the filed `D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md` is revision 3 (`2f7d9875…afc4`). This revision is meant to replace it.

**Revision 4 (owner direction).** Relayed by HELP_HUMAN, the owner's words on 2026-09-26, verbatim:

> "Why am I seeing `remaining-items` appearing?  There must not be any of those going forward, so no need to scan for them."

> "revision 4: drop remaining-items and remaining-loop"

This is recorded as evidence of the direction. The ruling on D-PEC-96 itself stays with the owner (K-AUTH-1).

| Change | Revision 4 |
|---|---|
| Vocabulary | `remaining-items` and `remaining-loop` are removed from the closed vocabulary, the schema options, `FEED_PROFILE_VERSIONS`, `FEED_PROFILE_SURFACES`, the surface table and the tests. The vocabulary is now `shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1 |
| Surfaces | `status-remaining` was declared only by the two dropped profiles. It is removed from the surface set: PEC's `## Remaining` sections are not a PEC surface and are not read. No other surface lost its only profile |
| Coherence rules | Both rules are kept: disjoint surfaces, and at least one live profile. The three shipped profiles are pairwise disjoint, so the overlap rule now guards future vocabulary changes. A test pins the disjointness. A second test adds two probe profiles through `unittest.mock.patch.dict` (the shipped files are untouched) and exercises three real overlaps: live and historical on one surface, two live readers, and two historical grammars. It also shows that a disjoint probe row loads and that the probes are removed afterwards |
| PEC's row | `shared-dev-loop` v1 live, `loop-receipts-ledger` v1 historical and `agentruns-json` v1 historical, with the revision-3 bases |
| Options | Option A-R, the `--pec-row` path of `apply_d96.py` and `mutate_d96.py`, the A-R postimage overrides and the A-R mutation variants are gone. `--pec-row` is now an unknown argument (exit 2) |
| Mutations | M11 is now "default declares the ledger live". M16 is now "`shared-dev-loop` also claims the receipt ledger". M19 is now "default drops `agentruns-json`". The runner stays fail-closed: a `NOT_APPLIED` mutation fails the run (probe run in the evidence). It now prints a total: **19/19 CAUGHT** |
| Owner questions | The Remaining question is settled by the owner's direction and recorded as settled: not read, no profile. Question 2 keeps its own-ruling framing. The rest are renumbered |
| Carried text | The stale "PEC's own row declares `remaining-loop` now" sentences in SOW-094's Notes and in the DEL-01-06 description and `_CONTEXT.md` are carried to graph node S2 as before. HELP_HUMAN relays that, in the same exchange, the owner directed that the `projects/pec/AGENTS.md` sentences keeping the Remaining sections as binding records be corrected separately, in the SCA-006 checkpoint-3 instruction tranche. At `8f9bd314c` the accepted checkpoint-2 candidate (`SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md`) still carries that paragraph. This packet writes neither surface |

**Earlier revisions** (history).

- **Revision 3** (`2f7d9875…afc4`, filed via PR #928 as `6721457be`) fixed the re-review's blocking finding: the mutation runner crashed under A-R. It also stated that a rollback never reverts ruling or register records, and noted in question 2 that A-R left PEC's one `WORK_GRAPH.json` unread. Re-review 03 found it reproducible.
- **Revision 2** (`4655e757…8da7`) addressed review 01's findings, numbered as review 01 numbers them:
  1. Remaining sections: a `remaining-items` profile. **Withdrawn in revision 4 by owner direction.**
  2. Overlapping profiles: surface disjointness and at least one live profile. **Kept.**
  3. `agentruns-json` coverage widened to `execution/**`. **Kept.**
  4. §B6 quoted in full. **Kept.**
  6. Containment allows HELP_HUMAN's records. **Kept.**
  7. The HOLD cited in `_REVIEW.md`. **Kept.**
  8. Test and schema nits. **Kept.**
- **Revision 1** (`f4861119…7d87`).

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
  - Earlier revisions were read at `abfd0897b`, `56a626c3b` and `7f33b4dd5`. Revision 4 was read at `origin/main` `8f9bd314c5f2499e6faf5bf4bdce917927e8185e`, from a fresh `git archive` export.
  - **Nothing under `projects/pec/v2/**` and nothing in `projects/pec/software-workflow.json` changed since `7f33b4dd5`, or since `abfd0897b`.** All 10 product preimages and all 6 must-remain hashes were re-verified at `8f9bd314c`.
  - PEC changes since revision 3 are HELP_HUMAN's records, which include the filed revision-3 proposal, the prep folder `execution/_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/`, the register row and the graph (G1 `BLOCKED` on the owner's ruling). They also include seven Root notices of 2026-09-26 and SCA-006 checkpoint 2. None touches the registry (see "SCA-006").
  - The checkout (now on branch `claude/pec-graph-cp2-d96`, moved by another actor) was not changed. This TASK switched no branch and ran only read-only Git commands and `git fetch`.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` at `8f9bd314c` with `--operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for all 13 targets: the 11 product paths and the two administrative paths below.

## What preparation found

### The registry today (unchanged since `abfd0897b`)

- `v2/config/loops.json` is schema version 1 with one row: `pec` → `projects/pec/loop/LOOP_INIT.md`. It carries no feed profile.
- `loops.schema.json` fixes `schema_version` to `1` and allows only `loop_id` and `loop_init_path` per row (`additionalProperties: false`).
- `RegisteredLoop` has two fields. The JSON adapter rejects every version other than 1 with a located error.
- `v2-loop-registry` runs 12 tests and passes. Nothing outside `projects/pec/v2` imports the registry; a repository grep finds only historical reconciliation manifests that name the files.

### PEC's own row

**Row: PEC's `pec` row declares the shape PEC writes after D-PEC-94.**

| Profile | Version | State | Basis |
|---|---|---|---|
| `shared-dev-loop` | 1 | live | the D-PEC-94 record |
| `loop-receipts-ledger` | 1 | historical | `projects/pec/AGENTS.md` |
| `agentruns-json` | 1 | historical | the D-PEC-94 record |

This is the migration row change the accepted records foresee. It departs from the letter of those records, so it needs its own ruling, asked as question 2. No scope change is needed.

1. **Why SCA-005 chose `remaining-loop`.** The checkpoint-1 resolution note gave Q8 (a) this reason: "D-PEC-86 I-7 defers PEC's own migration; PEC's `LOOP_INIT.md` still selects from `## Remaining`, so its registry row declares the shape it actually writes". Its sources were D-PEC-86 §3 I-7 and the then `loop/LOOP_INIT.md` §4. Both premises lapsed after checkpoint 3: D-PEC-94 exercised I-7 on 2026-09-25, and PEC's `LOOP_INIT.md` no longer selects from `## Remaining`.
2. **What the accepted texts say.**
   - The SOW-094 statement asks only for "each row's feed-profile selection". Its Notes cell adds: "PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7)".
   - Q8 (a) and §B6 (quoted in full above) say the same.
   - The design note (`FEED_MODEL_V2_DESIGN_NOTE.md`, `4b9ccb9f…12da`, §4 O-B2) describes that migration as "one owner-gated row change from `remaining-loop` to `shared-dev-loop`, with the ledger declared `historical`, and no parser rework".
   - SOW-077 asks each row to declare a profile with "live/historical" and a "basis citation to the loop's own record". PRD v2.3 names no profile.
3. **Why this needs its own ruling.** The accepted texts require the migration to happen "under its own ruling". The owner's revision-4 direction removes `remaining-loop` from the vocabulary, which implies the migrated row, since no other row is expressible. It is not itself a ruling on D-PEC-96. Question 2 therefore still asks for the row explicitly.
4. **What PEC writes now.**
   - One Git-tracked `WorkGraphs/<undertaking>/WORK_GRAPH.md` and one dated-heading `MEMORY.md` (DEL-01-03).
   - A central `RECEIPT.md`, planned at the undertaking's closeout; none exists yet.
   - `loop/LOOP_RECEIPTS.md`, closed at Receipt 197, which is "a historical ledger" per `projects/pec/AGENTS.md`.
   - One historical `WORK_GRAPH.json` (below).

Consequences, none blocking:

- **Stale Notes and description text.** The SOW-094 Notes cell and the DEL-01-06 description and `_CONTEXT.md` still say "PEC's own row declares `remaining-loop` now". After the act this records the SCA-005 intent, not the current row. It is Notes and description text, not a scope statement. It is carried to graph node S2 (the DEL-01-06 Scope of Work rebuild) as before, and the decomposition sentence can be refreshed by a later PEC scope change. This packet writes neither.
- **R-05 and FX-PEC-0.** SCA-005 risk R-05 and fixture FX-PEC-0 rest on the lapsed premise. The Impact Assessment §9.3 and design note §6 define FX-PEC-0 as "PEC `_STATUS.md` (57 with `## Remaining`), `LOOP_RECEIPTS.md`, 64 `Dependencies.csv`, the one historical `WORK_GRAPH.json`" under `remaining-loop`. Under this row, FX-PEC-0 reads `_STATUS.md` lifecycle, the historical ledger, the dependency registers, the historical `WORK_GRAPH.json`, the new work graph and MEMORY, and not the `## Remaining` sections. This is carried to graph node X1.

### PEC's `## Remaining` sections: settled, not read

The owner settled this on 2026-09-26 (above): "There must not be any of those going forward, so no need to scan for them"; "drop remaining-items and remaining-loop".

- **In the registry.** No profile in the vocabulary covers the `## Remaining` sections, and `status-remaining` is not a surface. PEC does not read the sections.
- **Against the PRD.** PRD v2.3 §7.1 makes "remaining items" "a per-loop optional field, read only where the loop's feed profile declares it". Since no profile declares it, not reading it conforms.
- **On disk.** The 57 sections at `8f9bd314c` are untouched by this packet.
- **In the instructions.** `projects/pec/AGENTS.md` still keeps them as records whose "gate markers still bind that item". HELP_HUMAN relays that the owner directed a separate correction of those sentences, in the SCA-006 checkpoint-3 instruction tranche. This packet neither relies on those sentences nor edits them.

### Profile coherence: disjoint surfaces, at least one live

**The rule is validated in the adapter, not left to the parsers.** The registry is the declaration, and REQ-003 requires an invalid configuration to fail explicitly, naming the offending entry. If the parsers resolved overlaps instead, each would need its own precedence rule: a hidden policy, applied late, and possibly different per parser.

Each profile names the surfaces it covers. The adapter holds these as `FEED_PROFILE_SURFACES`, and each schema option's description ends with the same list, which a test checks. Two rules apply to each row:

1. **The declared profiles cover pairwise-disjoint surfaces.** This one rule forbids:
   - two live readers of one surface;
   - a surface that is both live and historical;
   - two historical grammars for one surface.

   A violation fails at `$.loops[i].feed_profiles[j].profile`, naming the surface and the earlier entry.
2. **At least one profile is live.** A violation fails at `$.loops[i].feed_profiles`. A loop that PEC serves but that writes nothing live is better handled by removing its row, which is D-PEC-78's owner-gated act.

| Surface (design-note S#) | `shared-dev-loop` | `loop-receipts-ledger` | `agentruns-json` |
|---|:-:|:-:|:-:|
| `work-graphs` (S1) | ✓ | | |
| `central-receipts` (S3) | ✓ | | |
| `memory-run-index` (S5) | ✓ | | |
| `status-lifecycle` (S6) | ✓ | | |
| `dependency-registers` (S8) | ✓ | | |
| `decision-registers` (S9) | ✓ | | |
| `receipt-ledger` (S14) | | ✓ | |
| `json-run-evidence` (S15) | | | ✓ |

**Effect of the reduced vocabulary.** The three profiles are pairwise disjoint. Any combination of distinct profiles is therefore coherent, so long as one is live. Repeating a profile is rejected earlier, by the duplicate-profile check.

The overlap rule has no shipped case to fire on today. It stays for two reasons:

- It is the only guard against a later vocabulary change that introduces an overlap. That change is a code-plus-packet act under O-B2.
- It is exercised: a test adds two probe profiles, each copying one surface of a shipped profile, and proves all three overlap kinds are rejected with the right location. It then proves that a disjoint probe row loads and that the probes are removed afterwards. Mutations M14, M16 and M17 show the rule and the disjointness are observed.

`loop_init_path` is read for loop identity on every row, whatever its profiles, as PRD PEC-RCN-002 requires, so it is not a profile surface.

### `agentruns-json` coverage

- **The PRD's wording.** PRD v2.3 §7.1 on RunRecord: "`STATUS.json` / `RUNTIME_SUMMARY.json` under `execution/**` are read as declared historical grammar or current evidence per the loop's feed profile". On DependencyEdge: "`WORK_GRAPH.json` is read as a declared historical grammar where the loop's feed profile says so".
- **The profile's coverage.** The profile covers JSON run evidence anywhere under the loop's `execution/` tree, including `AgentRuns/` and deliverable `_run_records/`. The identifier keeps its SCA-005 name.
- **What PEC's row covers.** At `8f9bd314c`, PEC has exactly one such file: `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/WORK_GRAPH.json`. There is no `STATUS.json` or `RUNTIME_SUMMARY.json` under `projects/pec`. The design note's §3.1 count of 13 PEC `STATUS.json` files does not reproduce, and where it came from is UNKNOWN.
- **The basis.** PEC's row declares the profile `historical`, citing the D-PEC-94 record. That record adopts work graphs and central receipts as PEC's run records. No PEC record states in so many words that JSON run evidence is historical, so this basis rests on implication. Question 2 lets the owner name another.

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
- **Records.** DEL-01-06 has no `MEMORY.md`; in PEC only DEL-01-03 has one. Under `projects/pec/AGENTS.md`, a MEMORY row needs the governing packet to name the path, so the administrative grant names it (question 5).

### SCA-006 does not bear on the registry

**The owner's acceptances.**

- Checkpoint 1 was accepted on 2026-09-25: "SCA-006 CP1: accept; DQ a; ENV a; BUD a; GATE a; INS a; R-C excluded" (`checkpoint_snapshots/SCA-006_GROUP-1_2026-09-25/DECISION.md`, `0160dd88…50df`). It accepted the Impact Assessment `93253b7d…b691`, whose §7.1 classes DEL-01-06 `NOT_AFFECTED`.
- Checkpoint 2 was accepted: "SCA-006 CP2: accept; Q1 a; Q2 a" (`checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md`, `30aebd16…f989`).

**What it touches.** None of SCA-006's checkpoint-1 actions (`Amendment_Actions.csv`, `c5f90801…4891`), its checkpoint-2 actions (`Amendment_Actions_CP2.csv`, `d901b432…fc1de`) or its `Propagation_Plan.md` names SOW-077, SOW-094, DEL-01-06, the registry files, `RegisteredLoop` or a feed profile.

**The instruction tranche.** Its checkpoint-3 instruction tranche is where HELP_HUMAN relays that the owner wants the `projects/pec/AGENTS.md` Remaining sentences corrected. That change is independent of this packet.

### Findings beyond the brief (disclosed)

1. **"A feed profile" or a list.** SOW-077 and the DEL-01-06 description say each row declares "a closed, PEC-versioned feed profile". The migration they foresee already needs more than one entry on a row, and PRD v2.3 PEC-RCN-002 reads receipts as "live or declared historical per profile". Option A therefore makes `feed_profiles` a list with at least one live entry and disjoint surfaces (question 3).
2. **The vocabulary is fixed here for the first time.** The accepted vocabulary term lists `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger` and `agentruns-json` as examples ("e.g."). This packet makes three of them the closed set, each at version 1.
   - `remaining-loop` is dropped by owner direction.
   - The coverage lists are in the schema. Grammars stay in the parser deliverables (O-B2: "Path conventions and grammars live in PEC adapter code").
   - Adding a profile, version or surface later is a D-PEC code-plus-packet change within schema version 2 (question 3).
   - The vocabulary term in `SOFTWARE_DECOMP.md` §9 still names the dropped profile as an example. That is example text, left for a later scope change like the Notes sentence.
3. **Path-normalization residual (inherited).**
   - The version-1 check rejects absolute paths, `..` segments and backslashes.
   - It accepts `projects/./pec/x`, `projects//pec/x`, a trailing `/`, a leading space and `C:x`.
   - A keeps this rule unchanged and reuses it for `basis`; the schema description states exactly what is checked.
   - Tightening it is a small amendment, not prepared here.
4. **The version-1 tests had no unknown-field case,** although REQ-001 requires rejecting unknown fields. A adds one for rows and one for profile entries.
5. **Order under D-PEC-78 §4.3.** That section says: "The owner accepts the exact config/schema/test bytes only after deterministic schema and adapter contract tests and REVIEW."
   - Revisions 1–3 were reviewed on PR #928 (reviews 01–03).
   - Revision 4 changes the schema, default, adapter, test and runner bytes, and the prototype tests ran on them.
   - A reviewer follow-up on revision 4's bytes completes that order before the ruling.

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

### 2. The default instance — `v2/config/loops.json` (full postimage `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7`)

The one existing row keeps `loop_id` and `loop_init_path` and gains `feed_profiles`, and `schema_version` becomes 2. No row is added or removed.

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

The behaviour is summarized here; the exact bytes are in the act script and `optionA_vs_8f9bd314c.diff`.

- **Schema version.** Only `schema_version` 2 is accepted, as described under backward compatibility.
- **Row fields.** Each row needs exactly `loop_id`, `loop_init_path` and `feed_profiles`. A missing field fails at `$.loops[i].<field>` with "required field is missing". An unknown field fails with "field is not defined by schema v2".
- **Profile entries.** `feed_profiles` must be a non-empty list of objects with exactly `profile`, `version`, `state` and `basis`. Failures are located at `$.loops[i].feed_profiles[j].<field>`:
  - `profile` must come from the closed vocabulary `FEED_PROFILE_VERSIONS`: `agentruns-json`, `loop-receipts-ledger` and `shared-dev-loop`, each mapped to `{1}`.
  - A profile repeated in a row fails at the second occurrence, naming the first.
  - `version` must be an exact `int` in that profile's version set, so `True` and `"1"` are rejected.
  - `state` must be the string `live` or `historical`.
  - `basis` must pass the same repository-relative path rule as `loop_init_path`, now one shared helper.
- **Coherence.** The profiles on a row must cover pairwise-disjoint surfaces, per `FEED_PROFILE_SURFACES` and the table above; an overlap fails at the later entry's `.profile`. At least one profile must be `live`; otherwise the row fails at `$.loops[i].feed_profiles`.
- **Unchanged behaviour.** The error class, the file-level failures (absent, unreadable, malformed) and the no-partial-set rule are unchanged.
- **No value echo.** No failure message echoes a document value, except a profile identifier or surface name already validated against the closed vocabulary. Locations name keys, as before. A test proves this for every field.

### 5. Tests and fixtures

| Path | Act | Content |
|---|---|---|
| `v2/tests/config/test_json_loop_registry.py` | modify | The expected default is the three-profile row. The schema test checks the version-2 `$id`, every field description, and each vocabulary entry's description and surface list against `FEED_PROFILE_SURFACES`. It also checks that the schema's profile set, version and states equal the adapter's and the port's. New tests: `test_schema_version_1_is_rejected_with_location`; `test_invalid_feed_profiles_are_rejected_with_location` (21 located sub-cases, including unknown fields, non-string `state`, `null` `profile`, duplicate profile and no live profile); `test_shipped_vocabulary_surfaces_are_pairwise_disjoint`; `test_overlapping_profiles_are_rejected_with_location` (probe profiles via `mock.patch.dict`, three overlap kinds plus a disjoint control); `test_failures_do_not_echo_document_values` (6 fields); `test_additional_loops_need_entries_only`. `test_invalid_document_never_returns_partial_or_empty_set` also covers the version-1 fixture and a document whose second row alone is invalid |
| `v2/tests/config/test_loop_registry_contract.py` | modify (unchanged since revision 1) | Immutability now also covers `feed_profiles` and `FeedProfile`. New `test_registered_loop_carries_the_typed_feed_profile_field`. The three existing port, core-import and stdlib tests are unchanged |
| `v2/tests/config/fixtures/duplicate_loop_id.json`, `missing_loop_id.json` | modify (unchanged since revision 1) | Migrated to version 2, with one live `shared-dev-loop` entry per row |
| `v2/tests/config/fixtures/schema_version_1.json` | **create** | Byte-identical to today's `loops.json` (`4ce07ad0…d32e`) |
| `v2/tests/config/fixtures/malformed.json` | unchanged | Still fails as malformed JSON before any version check |

The suite goes from 12 to **19** tests. The mapping to DEL-01-06's verification methods:

| Method | Tests |
|---|---|
| **VER-001** format against the default and malformed fixtures | `test_schema_documents_every_field_and_the_exact_default`, `test_checked_in_default_has_exactly_the_pec_loop`, `test_schema_version_1_is_rejected_with_location`, `test_missing_loop_id_…`, `test_duplicate_loop_id_…`, `test_malformed_json_…`, `test_invalid_feed_profiles_are_rejected_with_location`, `test_shipped_vocabulary_surfaces_are_pairwise_disjoint`, `test_overlapping_profiles_are_rejected_with_location`, `test_failures_do_not_echo_document_values` |
| VER-002 one loop at P1; more loops by entries only | `test_checked_in_default_has_exactly_the_pec_loop`, `test_additional_loops_need_entries_only` |
| **VER-003** invalid, unreadable and absent fail explicitly, with no partial set | `test_absent_file_…`, `test_unreadable_path_…`, `test_invalid_document_never_returns_partial_or_empty_set`, `test_malformed_json_…` |
| VER-004 the consumer interface carries no path or serialization detail | `test_port_has_only_the_typed_capability_method`, `test_registered_loop_is_immutable`, `test_registered_loop_carries_the_typed_feed_profile_field` |
| VER-005 no third-party dependency or network call | `test_core_imports_no_adapter_or_outer_io_module`, `test_implementation_uses_only_stdlib_and_no_network_module`, plus `v2-core-posture` (the DEL-01-05 enforcement) and `v2/tests/enforcement` |
| VER-006 the suite runs and passes | `v2-loop-registry` |

## Options

- **A — schema version 2, a three-profile closed vocabulary with surface coherence, the port field, and the migrated PEC row (recommended).**
  - One act on **11 product paths**: 10 modified and 1 created (the version-1 fixture). Nothing is deleted.
  - PEC's row declares `shared-dev-loop` live, and `loop-receipts-ledger` and `agentruns-json` historical. This takes question 2 as "migrated".
  - `software-workflow.json` is unchanged; its rules already select all five checks for these paths.
- **Amend.** The owner changes the scope and the packet is re-prepared. For example:
  - a different vocabulary, surface table or coherence rule (question 3);
  - a time-bounded dual read of version 1 (question 4);
  - tightened path normalization (finding 3);
  - different `basis` citations.
- **Defer.** Nothing opens.
  - The registry stays version 1 with no profiles, and SOW-077 and SOW-094 stay unmet in source.
  - The DEL-01-06 Scope of Work rebuild (S2) waits, since SCA-005 gates it on this packet.
  - DEL-02-08's discovery "per the loop's declared feed profile" has no declaration to read.
  - No consumer exists yet, so deferring is not unsafe.

No narrower source-only option is offered. The parts depend on each other: a version-2 loader rejects the version-1 default, and the default cannot declare profiles without the schema and port.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** for PKG-01 / DEL-01-06. The script writes only these paths, relative to `projects/pec/`. The preimage SHA-256 values were read at `8f9bd314c`, and are equal at `7f33b4dd5`, `56a626c3b` and `abfd0897b`.

| # | Path | Act | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|---|
| 1 | `v2/config/loops.json` | modify | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` | `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7` |
| 2 | `v2/config/loops.schema.json` | modify | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | `104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143` |
| 3 | `v2/src/pec_v2/core/ports/loop_registry.py` | modify | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` | `a509bfb74920172a86ac21aff6a67245cd3248c5d73ef4e7427966069099c8a9` |
| 4 | `v2/src/pec_v2/core/ports/__init__.py` | modify | `669e1569216722509dcea0ae5ed42dc4a0ca856a196676568ee78d7a38a1edeb` | `e44bf7f00c8ef2cfa5f8006ef2834feb020063df63a3b4b8d8cbd8f359174ff7` |
| 5 | `v2/src/pec_v2/core/__init__.py` | modify | `33c54e244e8e19b66cb2c53c81fa747979f6d512f227f7a56e3f8d57cfb9ff4a` | `0e699a54d6bc202ff7a90c25fdb355da5ed2db185709c3a399870c1b0309c42d` |
| 6 | `v2/src/pec_v2/adapters/config/loop_registry.py` | modify | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` | `620a173d19d881ef396ebb339e4097f5ee4e3a0b6ada231718ca700926832f07` |
| 7 | `v2/tests/config/test_json_loop_registry.py` | modify | `d7efb486287d3703aa9ea007eb5376eba95689286bb322c887eeca8b193ac956` | `8b45495fdc78eb77c12a4ebefdb064d34d40d5602fde573be4b4e817ddbe0c9b` |
| 8 | `v2/tests/config/test_loop_registry_contract.py` | modify | `49b2f6a3b5088bceb82dc393cce050b8800af3a5ac5d34b3b6a3d7b71c01111b` | `b05ed8719c59258998b1c483456b66bd8d4a4d3bc4f68cdd6fb5c02541db7106` |
| 9 | `v2/tests/config/fixtures/duplicate_loop_id.json` | modify | `2e65c719af6c9eb7e170fb25d437b928847dc8d617c056093de213673b3e3396` | `6875f50023f1ad34a45c1af4b0a65316260c45aa05562ce45bb2d9bd8fd13c7e` |
| 10 | `v2/tests/config/fixtures/missing_loop_id.json` | modify | `2155849d9419f0239dca7a69d919ca9ee46a6434106d5326d85bc8c70afc5257` | `f4255b2483a014b542fb7f25c4314ff75dabb5cebbcfe751a2ad3df425f29598` |
| 11 | `v2/tests/config/fixtures/schema_version_1.json` | create | absent | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |

The path-list SHA-256 (the 11 paths, sorted, newline-terminated) is `b5db12e59bec0188b1798e8ccf7a3c09300c44e5dbcdf31c16a64aff5e84c73c`.

These paths stay unopened, and the script checks each is unchanged before writing:

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

The bytes come from one run of `apply_d96.py`, **SHA-256 `80725b4ff0180e858e6a0ecf0cf50fc8bcf19d861fcf53278f115567e6d6bbf3`**. It is stdlib-only Python, prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/apply_d96.py --repo "$(git rev-parse --show-toplevel)"
```

Before writing anything, the script checks:

- the six must-remain files;
- the 10 preimages, and that the fixture to be created does not exist;
- that every embedded postimage decodes to its pinned SHA-256;
- that the write set equals the grant.

It then writes, re-hashes every written file, and reports `READ`, `WRITE` and `UNCHANGED` lines. On any failure it exits 1 with nothing written, and a second run also exits 1. `--check-only` renders and checks without writing. There is no option flag; `--pec-row` exits 2 as an unknown argument. The product bytes contain no date, so there is no slot rule.

The preparation aids are not bound: `build_apply_d96.py` (`5f18ac1108b1507709a91f0849209470f3753818b55a248f63df975f5b66421e`), `apply_d96.template.py` (`671fb575b4f17b2b7164409134593c655cd1b3936081c2274b60b0f6b0b48033`) and `build_json_postimages.py` (`a5028f667c1f262464f6b4d0f4fdf3f3a2153510550f5192eaf726e4e897718d`).

## Finite verification

Run the registered checks from `projects/pec` (cwd `.`, as registered), and `harness-self-check` from the repository root.

- Use an explicit interpreter of Python 3.10 or later, record its path and version, and set `PYTHONDONTWRITEBYTECODE=1`.
- Record every command, exit code and output in the run root.
- The manager may use `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <ID> --output <run-root>/checks/<ID>.json` from the repository root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | the script's built-in checks; the ruling and its register row on fetched `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on each of the 13 targets before dispatch, and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere. Otherwise stop and route the discrepancy |
| Selection | `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json <the 11 paths>` | exactly `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` |
| **`v2-loop-registry` (VER-001, VER-003 rerun)** | `python3 -m unittest discover -s v2/tests/config -p test_*.py` (verbose run recorded, each test mapped to its VER method as tabled above) | exit 0; **Ran 19, OK** (12 before) |
| `v2-store-guard` (`v2/src/pec_v2/**` rule, D-PEC-87 X-1) | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | exit 0; Ran 13, OK |
| `v2-core-posture` (VER-005; DEL-01-05 enforcement; `always_checks`) | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | exit 0; `"verdict": "PASS"`, zero findings; `core_tree_sha256` changes from `88f590c0…c016` to `dd7e1dda…6e5a`; config and workflow hashes unchanged |
| DEL-01-05 enforcement tests | `python3 -m unittest discover -s v2/tests/enforcement -p test_*.py` | exit 0; Ran 28, OK |
| `v2-api-contract` (`always_checks`) | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | exit 0; Ran 6, OK |
| `harness-self-check` (`always_checks`; every PR) | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0; output identical to the pre-act run (on the prototype, `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` both times, stdout `e5f9ff70…d110`) |
| Receipts validator (every PR) | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0; output unchanged |
| Mutation evidence | `mutate_d96.py projects/pec` (copied into the run root) | baseline passes; M1–M19 each CAUGHT, none `NOT_APPLIED`; `TOTAL 19/19 CAUGHT`; `RESULT PASS` |
| Byte identity | recompute SHA-256 of the 11 paths | equal to the grant table |
| Basis citations | `test -f` on each `basis` and `loop_init_path` in the new `loops.json` | all present at the act commit |
| Containment | `git diff --name-status origin/main...HEAD` | the 11 paths, plus the run root and, if question 5 is answered yes, `MEMORY.md`. HELP_HUMAN's own records may ride the same PR or go separately: the D-PEC-96 register row, ruling and proposal under `execution/_Coordination/_DECISIONS/`, the work graph, the undertaking's `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/` briefs, returns and receipt, and the prep folder, all under the default-writable `execution/_Coordination/**`, plus `docs/STATUS.md` and `README.md` under D-PEC-88. Nothing else |
| Whitespace and encoding | `git diff --check origin/main...HEAD`; non-ASCII scan of the 11 postimages | clean; 0 non-ASCII bytes |

Decomposition and dependency validators do not apply: no register, decomposition or dependency file changes. The strict register validator was run on the prototype anyway, and its output was byte-identical before and after.

### Independent verifier

A fresh read-only TASK that authored nothing applies `.agents/skills/software-code-review/SKILL.md` and returns a verdict file. Defects go back to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`. The run-root script hashes to `80725b4f…bbf3`, and the recorded preimages match.
2. **Reproduction.** It reruns the script on a fresh `git archive` export of the pre-act `origin/main` and gets byte-identical files.
3. **The fixed checks.** It reruns the verification table and gets the same results, including the mutation run.
4. **Semantics.**
   - The schema documents every field, and the vocabulary is exactly the three profiles, with surface lists matching the adapter's.
   - Neither the schema nor the adapter names `## Remaining`, `remaining-items`, `remaining-loop` or `status-remaining`.
   - The adapter enforces exactly what the schema states, including disjoint surfaces and at least one live profile.
   - Every failure is located, none returns a partial set, and none echoes a document value.
   - Version 1 is rejected, not read.
   - The core imports stay stdlib-only, with no I/O module.
   - The PEC row matches the ruled answer to question 2, and its `basis` paths exist and say what they are cited for.
   - The tests assert no criterion beyond revision-1.5 SOW-077/094, the DEL-01-06 SOW's surviving clauses and this packet.
5. **Containment.** Nothing changed outside the containment row. In particular these are unchanged: `software-workflow.json`, `service_core_posture.json`, the storage and API files, `malformed.json`, DEL-01-06's `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv` and `_CONTEXT.md`, any decomposition file, and `docs/PRD.md`.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-06 only, for this act.
  - The manager runs the reliance preflights and the script. No author TASK is needed, because the bytes are bound. The manager may instead dispatch a bounded TASK to run the script, commissioned as an implementation node under `construct-local-work-graph` (`3e197c9d…9dc3`). Its brief carries the objective, basis, write fence, exclusions, acceptance criteria and authorized checks, as that workflow requires.
  - One fresh read-only TASK is the verifier.
- **Run root.** `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/**`, a new folder beside the D-PEC-75 and D-PEC-77 records. It holds:
  - `apply_d96.py` (exact bytes) and its report;
  - `mutate_d96.py` and its output;
  - the check outputs and preflight results;
  - `RUN.md`;
  - `VERIFIER_VERDICT_NN.md`.

  The earlier `_run_records/*` stay immutable.
- **`MEMORY.md` (question 5).** If the owner agrees, the act creates `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`). The path does not exist at `8f9bd314c`. At closeout, the undertaking's M1 node writes one run row: the run ID, the date, "schema version 2 source act under D-PEC-96", the PR and the central receipt.
- **Not opened.**
  - DEL-01-06 `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` and `Dependencies.csv`.
  - Every other deliverable.
  - `docs/STATUS.md` and `README.md`, which HELP_HUMAN maintains under D-PEC-88 and names in the graph.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for the manager and the verifier, as under D-PEC-91 and D-PEC-95, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, the graph and the central receipt are HELP_HUMAN's.

## Rollback

- **During execution.** The script writes nothing unless every check passes. If a later check fails, discard the branch or worktree; nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR of the act restores the 10 preimages tabled above. It removes the created fixture, the run root and, if created, `MEMORY.md`. History is preserved and no reset is made. The owner's ruling record and every register row are never reverted. Under the register header's convention a ruled row is not reopened or annotated, so the rollback is recorded as its own new register row and record, citing D-PEC-96 and the revert PR. HELP_HUMAN's other records that rode the act PR (graph, briefs, returns) stay as history and gain a dated note. If the revert PR touches them, it may only add to them.
- **Stores and consumers.**
  - No store holds registry data and no consumer reads the port, so there is no migration or consumer rollback to do.
  - The version-1 bytes also survive as `schema_version_1.json` until reverted.
  - If the revert happens after a consumer has been built against `feed_profiles`, that consumer's own packet must roll back first.

## Limits

This proposal, and any ruling selecting A or an amendment, grants none of the following:

- **No lifecycle change.** DEL-01-06 stays `INITIALIZED` and its Gate 5 HOLD stands. No `_STATUS.md` is touched.
- **No DEL-01-06 Gate 5 act and no SOW change.** Gate 5 is not re-entered, RF-001 and RF-002 are not reopened, and no `ScopeOfWork.md` byte changes. The rebuild remains graph node S2 under its own packet.
- **No PRD, decomposition or instruction change.**
  - Nothing is written to `docs/PRD.md`, `_Decomposition/**`, any register, any `_CONTEXT.md`, `_REFERENCES.md` or dependency file, or `projects/pec/AGENTS.md`.
  - The stale "declares `remaining-loop` now" sentences go to S2 and to a later scope change.
  - The AGENTS.md Remaining sentences go to the SCA-006 checkpoint-3 instruction tranche.
- **No `CHECKING`, `ISSUED`, artifact acceptance, or any readiness or reliance claim.** CHECKING is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it.
- **No other registry row.** No loop is added or removed.
- **No consumer, parser, fixture suite or grammar.** DEL-02-0x and X1 remain their own packets.
- **No change to other surfaces.** `software-workflow.json`, CI, Root, tier-0, sister-project and frozen-corpus surfaces are untouched.
- **No duty on any other loop.** A profile is PEC's reading hypothesis, never the loop's truth. Listing a loop creates no duty, cadence or authority (D-PEC-78 O-A).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Settled by the owner's direction (not a question)

- **PEC's `## Remaining` sections.** They are not read, and no profile covers them. Owner, 2026-09-26: "There must not be any of those going forward, so no need to scan for them"; "revision 4: drop remaining-items and remaining-loop".

## Questions only the owner can answer

1. **A, amend or defer.** Recommendation: **A**.
2. **PEC's own row: the migration row change, ruled here as its own item.**
   - **The departure.** Option A departs from the letter of the CP2-accepted §B6 ("PEC's own `pec` row `remaining-loop`, Q8 (a)"; "D-PEC-86 I-7 … stays deferred") and of SCA005-CP1-Q8 (a).
   - **Why.** Their premise was that PEC still selected from `## Remaining`, with I-7 deferred. That premise ended when D-PEC-94 exercised I-7 after checkpoint 3.
   - **What the question asks.** The migration they foresee as "one owner-gated row change".
   - **The direction's implication.** The owner's revision-4 direction removes `remaining-loop`, so only the migrated row remains expressible. This question records the ruling itself.
   - **Migrated (recommended):** `shared-dev-loop` v1 `live` (basis: the D-PEC-94 record), `loop-receipts-ledger` v1 `historical` (basis: `projects/pec/AGENTS.md`), and `agentruns-json` v1 `historical` (basis: the D-PEC-94 record, by implication). The last reads PEC's one `WORK_GRAPH.json`.
   - **Other:** state other profile states or basis citations within the three-profile vocabulary.
   - **Scope.** This is within the accepted scope and needs no scope change.
3. **Vocabulary, surfaces and row shape.** Confirm:
   - the closed vocabulary of three profiles (`shared-dev-loop`, `loop-receipts-ledger`, `agentruns-json`), each at version 1, with the coverage and surface lists in the schema;
   - `feed_profiles` as a non-empty list, with each profile at most once per row;
   - the coherence rules: disjoint surfaces and at least one live profile, enforced at load, and kept as a guard although the shipped profiles are disjoint;
   - that adding a profile, version or surface later is a D-PEC code-plus-packet change within schema version 2.

   Recommendation: **confirm**. Alternatives, by amendment: exactly one profile per row; leaving coherence to the parsers; allowing rows with only historical profiles; or a new schema version for every vocabulary change.
4. **Version-1 files.**
   - **Recommended:** reject them with a located error; this act migrates the one checked-in default.
   - **Alternative (amend):** a time-bounded, tested dual read. D-PEC-78 §4.2 allows one "if needed". It is not needed, and it would need a defaulting rule that REQ-003 forbids.
5. **Records.**
   - **Recommended:** create DEL-01-06's `MEMORY.md` from the template, so the undertaking's closeout can write the run row.
   - **Alternative:** record this run only in the graph and central receipt, and complete without the row.

   The run root under DEL-01-06 `_run_records/` is part of the grant either way.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in fresh `mktemp -d` directories under the host's temporary area, outside the session scratchpad and outside the checkout.

- `base` is a `git archive` export of the whole tree at `8f9bd314c`.
- Each prototype is an APFS clone (`cp -Rc`) of `base` with the act applied.
- For `harness-self-check` and `git diff`, the base clone and the applied clone were made throwaway repositories: `git init`; an `objects/info/alternates` entry pointing read-only at the source object store; `git read-tree 8f9bd314c`; and `update-ref HEAD` inside the export only.

Nothing was written to the checkout or its repository. The interpreter was Python 3.13.7 (CPython), and the local date was 2026-09-26.

| Command (scratch) | Exit | Result |
|---|---|---|
| five registered checks on `base` via `run_registered_checks.py` | 0 ×5 | api 6 OK; registry 12 OK; store 13 OK; posture PASS, 0 findings, core tree `88f590c0…c016`; harness `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` |
| the same on the applied clone | 0 ×5 | api 6 OK; **registry 19 OK**; store 13 OK; posture PASS, 0 findings, core tree `dd7e1dda…6e5a`; harness output byte-identical to `base` (`e5f9ff70…d110`) |
| `v2/tests/enforcement` on `base` / applied | 0 / 0 | Ran 28, OK / Ran 28, OK |
| `select_affected_checks.py` over the 11 paths | 0 | all five checks |
| `apply_d96.py --check-only` on a fresh clone | 0 | 11 RENDER; `diff -rq` shows the tree unchanged |
| `apply_d96.py` on a fresh clone | 0 | 6 UNCHANGED, 11 READ (10 preimages, 1 absent), 11 WRITE; `v2/` byte-identical to the hand-applied prototype; `diff -rq` against `base` shows exactly the 11 paths |
| `apply_d96.py` rerun on the applied clone | 1 | "preimage mismatch v2/config/loops.json …; nothing written" |
| `apply_d96.py` on a clone with `software-workflow.json` altered | 1 | "must-remain file differs: software-workflow.json; nothing written"; no file created |
| `apply_d96.py --pec-row remaining` | 2 | unknown argument; the A-R path no longer exists |
| `mutate_d96.py` on the applied clone | 0 | baseline OK; **TOTAL 19/19 CAUGHT**; `RESULT PASS`. The mutations: M1 accept version 1; M2 drop the duplicate-profile check; M3 skip the basis path check; M4 widen the vocabulary; M5 admit a `bool` version; M6 admit empty profiles; M7 make profiles optional; M8 unlocated state failure; M9 admit version 2; M10 schema constant back to 1; **M11 default declares the ledger live**; M12 swap the `RegisteredLoop` field order; M13 allow a traversing `loop_init_path`; M14 drop the surface-disjointness check; M15 drop the at-least-one-live rule; **M16 `shared-dev-loop` also claims the receipt ledger**; M17 overlap allowed when states differ; M18 echo an invalid `state` value; **M19 default drops `agentruns-json`** |
| fail-closed probe: the runner with M1's anchor made invalid | 1 | `M1 … NOT_APPLIED (RuntimeError …)`; `TOTAL 18/19 CAUGHT`; `RESULT FAIL` |
| `validate_pec_loop_receipts.py --repo-root .` on `base` / applied | 0 / 0 | VALID; identical apart from the absolute path prefix |
| `validate_decomposition_registers.py --strict projects/pec/execution` on `base` / applied | 0 / 0 | 0 errors / 0 warnings; output byte-identical |
| applied `git diff --check`; non-ASCII scan of the 11 postimages | 0 | clean; 0 non-ASCII bytes |
| `grep -ri remaining` over the applied `v2/` tree | 1 | no match |
| `pec_reliance_hold.py … --operation exact-correction-preparation` from `base/projects/pec` | 0 ×13 | `ALLOW` |

Scratch artifacts are in the preparer's `g1/` folder, with hashes in `g1/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `apply_d96.py` (the bound act script) | `80725b4ff0180e858e6a0ecf0cf50fc8bcf19d861fcf53278f115567e6d6bbf3` |
| `mutate_d96.py` (mutation runner) | `57c2f03107aec5056f03847c43b9443a6986fbfd522017971c3cab72c3c826f0` |
| `build_apply_d96.py`, `apply_d96.template.py`, `build_json_postimages.py` (preparation aids) | `5f18ac11…421e`, `671fb575…8033`, `a5028f66…718d` |
| `evidence/optionA_vs_8f9bd314c.diff` (includes the created fixture) | `fc4745e16c796e42a2b5513c6926b00847821d1a7468d817b80b367f5c633faf` |
| `evidence/CHECKS_SUMMARY.txt`, `evidence/mutate_optionA.out`, `evidence/mutate_notapplied_probe.out`, `evidence/optionA_v2-loop-registry_verbose.txt`, `evidence/preflight.txt`, `evidence/actA.report.txt`, `evidence/preimages.txt` | in `SHA256SUMS` |
| `postimages/optionA_v2/**` (postimage copies for review) | in `SHA256SUMS` |

Basis read for preparation, at `8f9bd314c`:

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
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | `cdfc47193542dc36da36af93fd1ef400e61646aee57bcfb54ab3f331f89cd519` |
| `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` | `24901c3a80f7a49ae4de3c35e94a5e2f9521c397c57dacb83371068f008f41be` |
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
| `workflows/construct-local-work-graph/WORKFLOW.md` | `3e197c9ddc75d40daa02929dc3df653a66f7d76ab6996239e823bba647dd9dc3` |
| `projects/pec/execution/_Coordination/NOTICE_2026-09-26_WORKFLOW_WAVE2A_EXECUTION.md` | `d194b1b5ae55b07a10a14d059334f6047dc1044069ae603138a2638faf3d4383` |
| `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md` | `30aebd162e98cdc91923468852af6833feda84c3a3d9d3efe252dc8a87abf989` |
| `projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/CP2_CANDIDATE/AGENTS.candidate.md` | `49ce993a7e21c76561bcb781b6fc317f51cdd0b7b76e6cbc8e38859aceeb070d` |
| Brief G1 (scratch) | `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node G1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
