# D-PEC-96 — Loop-registry schema v2 with closed feed profiles (SCA-005 §B6 registry source packet) — proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN (undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node G1) for the PEC loop, 2026-09-25 (session date), from brief `G1_REGISTRY_SOURCE_PROPOSAL.md` (SHA-256 `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1`). No earlier direction approves this file. It performs no production act: no tracked file was edited, and every prototype ran on scratch copies only. It asks for no lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row; this file does not add it. At `abfd0897b` the register has no D-PEC-96 row and no file under `projects/pec` carries the number; this packet uses the number its brief assigned. Suggested filing name: `execution/_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`.

## Provenance

- **Owner acts relied on.**
  - SCA-005 checkpoint 1 (2026-09-24): "I accept checkpoint 1 and the Impact Assessment." It selected the resolution note's Section A, including Q1 O-B2, Q8 (a) and CP1-V "within D-PEC-78 O-A with no supersession" (`_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-1_2026-09-24/DECISION.md`, `b9157b2b…40da`; note `CHECKPOINT1_RESOLUTION_NOTE.md`, `af4e46d0…0ad2`; `Decision_Log.md` rows SCA005-CP1-Q8 and SCA005-CP1-V).
  - Checkpoint 2 (2026-09-25, `D-PEC-92`): "CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred." It accepted `Propagation_Plan.md` (`50cd0b1d…1350`), whose §B6 is this packet's intent, and it opened no `v2/**` path.
  - Checkpoint 3 (2026-09-25): "CP3: accept; Q1 a". Revision 1.5 became `current_basis` with PRD v2.3.
  - `D-PEC-78` O-A (2026-08-02): "D-PEC-78: O-A". The packet it ruled (`D-PEC-78_OI-003_LOOP_REGISTRY_HOME_2026-08-02/PACKET.md`, `426dba04…5d17`) §4.2 says: "Adding, removing, or changing a field's meaning requires a new schema version and a successor D-PEC migration packet. Version 1 is not silently widened. A dual-read transition, if needed, must be time-bounded and tested; unknown versions fail closed."
  - `D-PEC-94` (2026-09-25): "You can continue with all the open work you identified." Its record (`b6814e90…6a6b`) exercises `D-PEC-86` §3 I-7: PEC adopted the shared development-loop method and froze `loop/LOOP_RECEIPTS.md` after Receipt 197. It says later fenced writes still need their own packets, and it names no registry change.
- **Fence.** `projects/pec/AGENTS.md` (`c9d3b44d…197a`) §"Write Scopes And Fences": every write under `projects/pec` outside `execution/_Coordination/**`, `AGENTS.md` and the one-time STATUS pointer needs an owner-ruled D-PEC packet naming exact paths, acts, verification and rollback. `F-PEC-1` (`D-T0-15`, `95c245b5…0b09`) fences source trees until such a packet opens them. No earlier ruling opens the paths below for this change. `D-PEC-75` opened DEL-01-06's first slice (merged 2026-08-02 as `ccd9a2178`). Later `v2/**` packets opened other deliverables' paths, for example `D-PEC-77` for DEL-01-05 and `D-PEC-85`, `-87`, `-89` and `-91` for DEL-01-03. Since the D-PEC-75 slice, the registry files have changed only in the 2026-09-05 path migration (`ca49b846d`).
- **Intent of record.** `Propagation_Plan.md` §B6: "`loops.schema.json` v2 carrying feed-profile declarations, `loops.json` rows declaring profiles (PEC's own `pec` row `remaining-loop`, Q8 (a)), and a `RegisteredLoop` port field; exact paths, VER-001/VER-003 re-run and rollback named by that packet. Since D-PEC-87 X-1, `software-workflow.json`'s `v2-store-guard` rule also covers `v2/src/pec_v2/**`, so the packet's verification list names both checks." Revision 1.5 states the obligation in SOW-077, SOW-094 and the DEL-01-06 description; PRD v2.3 §16.3 says a strict schema version 2 "arrives only through a later D-PEC packet, within D-PEC-78 O-A".
- **Precedents.** `D-PEC-95` (proposal format; a bound, preimage-checked act script; revert-PR rollback). `D-PEC-91` (v2 source grant, registered-check table, mutation evidence). `D-PEC-87` X-1 (the store-guard path rule). `D-PEC-75` (DEL-01-06 run records under `_run_records/`).
- **Source state.** Every hash below was read at `origin/main` `abfd0897bedc59df23772f1a8b6382a3c67c89b1` (PR #924), from a `git archive` export, and each registry preimage was compared with `git show origin/main:<path>`. The last commits touching the registry files are `d4f53a70e` (2026-08-02, the D-PEC-75 slice) and `ca49b846d` (2026-09-05, path migration). The checkout (branch `claude/pec-graph-u1-complete`) was not changed. Its HEAD moved from `0401c6bc1` to `1f37702e1` during preparation by another actor; that commit adds one review transcription under `AgentRuns/` and touches no registry path. The work graph at `abfd0897b` (`f32ab9d2…3802`) lists G1 as `PLANNED`. **Re-fetched at the end of preparation:** `origin/main` had advanced to `3245f9acd42d447238033e926ccace6c9aa5176d` (PR #925). Among the files this packet cites, only `_REGISTER.md` (now `fb650799…326a`, still no D-PEC-96 row) and the work graph (now `9e8dd065…3052`, G1 `READY`) changed. Every product preimage, must-remain hash and other basis hash is unchanged. By then another actor had also switched the checkout to branch `claude/pec-sca006-cp1-accept` (`4398370947`). This TASK switched no branch and ran only read-only Git commands plus `git fetch`.
- **Holds.** `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (`f877d931…41cbc`) has a header and no rows. `execution/_Scripts/pec_reliance_hold.py` (`b1712e4b…cd0e`), run from `projects/pec` with `--operation exact-correction-preparation`, returned `{"operation": "exact-correction-preparation", "status": "ALLOW"}` with exit 0 for all 13 targets: the 11 product paths and the two administrative paths below.

## What preparation found

### The registry today (observed at `abfd0897b`)

- `v2/config/loops.json` is schema version 1 with one row: `pec` → `projects/pec/loop/LOOP_INIT.md`. It carries no feed profile.
- `loops.schema.json` fixes `schema_version` to `1` and allows only `loop_id` and `loop_init_path` per row (`additionalProperties: false`).
- `RegisteredLoop` has two fields; the JSON adapter rejects every version other than 1 with a located error.
- `v2-loop-registry` runs 12 tests and passes. Nothing outside `projects/pec/v2` imports the registry: a repository grep finds only historical reconciliation manifests that name the files.

### The PEC-row premise

**Resolution: PEC's `pec` row should now declare `shared-dev-loop` version 1 as `live` and `loop-receipts-ledger` version 1 as `historical`. That is the migration row change the accepted records foresee. It needs its own ruling, which this packet asks for as a separate question (question 2). No scope change is needed.**

The basis:

1. **Why Q8 chose `remaining-loop`.** The resolution note gave Q8 (a) this reason: "D-PEC-86 I-7 defers PEC's own migration; PEC's `LOOP_INIT.md` still selects from `## Remaining`, so its registry row declares the shape it actually writes" (sources: D-PEC-86 §3 I-7 and the then `loop/LOOP_INIT.md` §4). Both premises have lapsed. D-PEC-94 exercised I-7 on 2026-09-25. The current `projects/pec/AGENTS.md` says the `## Remaining` sections are "no longer a work-selection surface" and that `loop/LOOP_RECEIPTS.md` is "a historical ledger, closed by Receipt 197".
2. **What the profiles mean.** The design note (`FEED_MODEL_V2_DESIGN_NOTE.md`, `4b9ccb9f…12da`, §4 O-B2) defines `remaining-loop` as a live `## Remaining` field plus the live ledger, dependency and decision registers ("PEC's own current loop"). It defines `shared-dev-loop` as work graphs, central receipts, the MEMORY run index, `_STATUS.md`, dependency and decision registers. It also describes PEC's later migration as "one owner-gated row change from `remaining-loop` to `shared-dev-loop`, with the ledger declared `historical`, and no parser rework". PEC now writes that shape: one Git-tracked `WorkGraphs/<undertaking>/WORK_GRAPH.md`, one dated-heading `MEMORY.md` (DEL-01-03), and a central `RECEIPT.md` planned at the undertaking's closeout (none exists yet).
3. **What the accepted texts require.** The SOW-094 statement asks only for "each row's feed-profile selection". Its Notes cell adds: "PEC's own `pec` row declares the `remaining-loop` profile now; its later migration is one owner-gated row change under its own ruling (D-PEC-86 I-7)". Q8 (a) reads "declare `remaining-loop` now; migration later as one row change under its own ruling". SOW-077 asks that each row declare a profile with "live/historical" and "basis citation to the loop's own record". PRD v2.3 does not name any profile.
4. **Inside this packet or separate.** The migration is foreseen by the accepted texts, and no scope statement changes, so it needs no scope change. The texts do require that it happen "under its own ruling". This packet therefore asks for it as a separate question. The source bytes are the same either way except `loops.json` and one test expectation (option A versus A-R). The owner may also rule it in a later packet.
5. **Why not the literal `remaining-loop`.** Declaring it today would record a reading hypothesis PEC's own instructions contradict. Its `basis` citation would have to point at a lapsed record, since no current PEC record says PEC writes that shape. PEC would also read a closed ledger as live, so under PEC-ORI-006 its silence would look like staleness. It would cost a second packet for a one-row change. Nothing consumes the registry yet, so A-R is harmless now, but it is knowingly stale.

Consequences of A, none blocking:

- The SOW-094 Notes cell and the DEL-01-06 description and `_CONTEXT.md` still say "PEC's own row declares `remaining-loop` now". After A that sentence describes the SCA-005 intent, not the current row. It is Notes and description text, not a scope statement. The DEL-01-06 Scope of Work rebuild (graph node S2) states the current row, and the next PEC scope change can refresh the decomposition sentence. This packet writes neither.
- Under `shared-dev-loop` PEC's 57 retained `## Remaining` sections are not read. PRD v2.3 §7.1 makes "remaining items" a per-loop optional field "read only where the loop's feed profile declares it", and D-PEC-94 removed their selection role. If the owner wants them read, that is an amendment: for example, add a profile.
- SCA-005 risk R-05 ("PEC's own P1 self-ingest corpus stays old-shape") and fixture FX-PEC-0 ("PEC self-ingest (`remaining-loop`)", Impact Assessment §9.3) rest on the lapsed premise. PEC's corpus now holds both generations, so FX-PEC-0 becomes a dual-generation self-ingest under A. This is carried to graph node X1.

### Other registry rows

There are none. `loops.json` has one row, which matches OI-010 (one loop at P1) and Q5 (a) (App and Piping enter P1 only as pinned fixtures). The P2 loops (Root, App, Piping, Runtime, Bridge) each need their own owner-gated row packet under D-PEC-78 §4.3. At that point Root, Runtime and Bridge, whose ledgers are live prose ledgers, may need a profile the vocabulary below lacks. That is a later code-plus-packet change, as O-B2 foresees.

### Backward compatibility: version-1 files are rejected; the one checked-in file is migrated

- **A version-1 row cannot meet revision 1.5.** SOW-077 requires "each row declaring a closed, PEC-versioned feed profile". Accepting version 1 would mean either inventing a profile, which is silent substitution that the DEL-01-06 REQ-003/AC-003 contract forbids, or returning loops with no profile, which SOW-077 forbids.
- **D-PEC-78 permits dual reading only "if needed", time-bounded and tested.** It is not needed. The only version-1 document is the checked-in default, which this act migrates. PEC runs nowhere, and no store or consumer holds registry data.
- **So the loader accepts exactly `schema_version: 2`.** Any other value, including 1, fails at `$.schema_version` with "expected integer constant 2; no other schema version is accepted". The exact version-1 bytes are kept as a test fixture (`schema_version_1.json`, byte-identical to today's `loops.json`), so the rejection is tested.
- **Version 1 stays strict and is not widened** (PRD v2.3 §16.3; CP1-V). Its bytes remain in Git history and in that fixture.

### Relation to DEL-01-06 (Gate 5 HOLD, SOW currency, records)

- **Lifecycle.** DEL-01-06 is `INITIALIZED` (`_STATUS.md` `20e6db02…e90d`) under the owner's Gate 5 HOLD. The D-PEC-75 source bytes were produced but never accepted: the HOLD "does not accept the produced artifacts". This packet changes those unaccepted bytes and asks for no lifecycle change. It does not touch `_STATUS.md`, `_REVIEW.md` or `Review_Findings.csv`. The SELF_CHECK evidence (RF-001, RF-002; registry 12/12) becomes historical evidence about the superseded bytes. Any later Gate 5 re-entry is the owner's own act and would review the version-2 bytes against the rebuilt Scope of Work.
- **Scope of Work currency.** The accepted contract (`5fdcfd96…a2fa8`, revision-1.4 basis) still says "strict version-1" in CLM-003, TBD-002, REQ-001, REQ-005, CON-001 and AX-003. SCA-005 §B4 classes it `STALE_REBUILD_REQUIRED … gated on B6`, and the graph orders its rebuild after G1 (node S2). REQ-005 itself says "a path, schema, or field-meaning change requires a separately governed migration without amending DEL-02-07, DEL-03-01, or DEL-09-02 merely for adapter details"; this packet is that migration. Until S2 lands, the new tests go beyond the revision-1.4 text: they check behaviour that revision 1.5 requires but the old contract does not declare, so REQ-007 wording lags. The S2 rebuild absorbs them. This packet writes no SOW byte. AC-002 ("adding entries only, with no format change") stays true under version 2.
- **Records.** DEL-01-06 has no `MEMORY.md`. Only DEL-01-03 has one in PEC. Under `projects/pec/AGENTS.md`, a MEMORY row needs the governing packet to name the path, so the administrative grant names it (question 5).

### SCA-006 does not bear on the registry

SCA-006's checkpoint-1 Impact Assessment (`93253b7d…b691`, §7.1) classes DEL-01-06 `NOT_AFFECTED` ("no K-03, verify-before-rely, §8, access-class, auth, size or parity text"). None of its 54 proposed actions (`Amendment_Actions.csv`, `c5f90801…4891`) names SOW-077, SOW-094, DEL-01-06, DEL-02-08, DEL-02-09, the registry files or a feed profile. Its proposed reliance envelope ("per-feed coverage and limitations") would consume the feeds the profiles declare, but it does not change how they are declared. Its checkpoint 1 is not yet accepted.

### Findings beyond the brief (disclosed)

1. **"A feed profile" or a list.** SOW-077 and the DEL-01-06 description say each row declares "a closed, PEC-versioned feed profile". The migration they foresee needs two entries on one row: `shared-dev-loop` live with the ledger historical. PRD v2.3 PEC-RCN-002 reads receipts as "live or declared historical per profile". Option A therefore makes `feed_profiles` a list with at least one entry and no repeated profile. One-profile-per-row would need a combined profile for every mix of generations. Question 3 asks the owner to confirm the list.
2. **The vocabulary is fixed here for the first time.** The accepted vocabulary term lists `shared-dev-loop`, `remaining-loop`, `loop-receipts-ledger` and `agentruns-json` as examples ("e.g."). The design note calls its table "Example profiles". This packet makes those four, each at version 1, the closed set. Their one-line coverage is documented in the schema, and grammars stay in the parser deliverables (O-B2: "Path conventions and grammars live in PEC adapter code"). Adding a profile or version later changes the schema bytes and the adapter; A treats that as a D-PEC code-plus-packet change within schema version 2, not a new schema version, because no field is added and no field's meaning changes. Question 3.
3. **Path normalization residual (inherited).** The version-1 check rejects absolute paths, `..` segments and backslashes. It accepts `projects/./pec/x`, `projects//pec/x`, a trailing `/`, a leading space and `C:x`. A keeps this rule unchanged and reuses it for `basis`. The schema description states exactly what is checked. Tightening it, for example by requiring `PurePosixPath(value).as_posix() == value` and no `.` segment, is a small amendment, not prepared.
4. **The version-1 tests had no unknown-field case,** although REQ-001 requires rejecting unknown fields. A adds one for rows and one for profile entries.
5. **Order under D-PEC-78 §4.3.** "The owner accepts the exact config/schema/test bytes only after deterministic schema and adapter contract tests and REVIEW." The prototype ran the tests. HELP_HUMAN should have this draft independently reviewed before presenting it, as PR #921 was for D-PEC-95. The ruling on the exact bytes then follows tests and review, and the act verifier re-confirms them.

## Exact change

All paths are relative to `projects/pec/`. The bytes are exact; the bound act script (below) carries every postimage.

### 1. Schema version 2 — `v2/config/loops.schema.json` (full postimage)

Serialized as the version-1 file is: `json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=True)` plus one final newline, LF line endings. The preimage round-trips through the same rule byte for byte.

```json
{
  "$id": "https://chirality.local/pec/v2/config/loops.schema.json",
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
            "description": "The feed profiles PEC applies to this loop: PEC's reading hypothesis, never the loop's truth. At least one entry; a profile identifier appears at most once per loop.",
            "items": {
              "additionalProperties": false,
              "properties": {
                "basis": {
                  "description": "Citation to the loop's own record that supports this declaration. Normalized repository-relative path (no leading '/', no '..' segment, no backslash).",
                  "minLength": 1,
                  "type": "string"
                },
                "profile": {
                  "description": "Identifier from PEC's closed feed-profile vocabulary. Path conventions and grammars for each profile live in PEC's adapters.",
                  "oneOf": [
                    {
                      "const": "agentruns-json",
                      "description": "JSON run evidence under execution/_Coordination/AgentRuns/ (WORK_GRAPH.json, STATUS.json, RUNTIME_SUMMARY.json)."
                    },
                    {
                      "const": "loop-receipts-ledger",
                      "description": "The loop's loop/LOOP_RECEIPTS.md receipt ledger, under that loop's grammar."
                    },
                    {
                      "const": "remaining-loop",
                      "description": "Loops that select work from _STATUS.md '## Remaining' items: lifecycle with those items, the loop/LOOP_RECEIPTS.md ledger as the receipt feed, dependency registers and decision registers."
                    },
                    {
                      "const": "shared-dev-loop",
                      "description": "The shared development-loop method: undertaking work graphs (execution/_Coordination/WorkGraphs/<undertaking>/WORK_GRAPH.md), central receipts (execution/_Coordination/AgentRuns/<RunID>/RECEIPT.md), the deliverable MEMORY.md run index, _STATUS.md lifecycle, dependency registers and decision registers."
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

The one existing row keeps `loop_id` and `loop_init_path`, gains `feed_profiles`, and `schema_version` becomes 2. No row is added or removed.

**Option A** (question 2 answered "migrated"; postimage `dc789031afd0bc949baf5aafe0a6221a8c5f72c6810188b84e2d5d2170a694a6`):

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
        }
      ],
      "loop_id": "pec",
      "loop_init_path": "projects/pec/loop/LOOP_INIT.md"
    }
  ],
  "schema_version": 2
}
```

**Option A-R** (question 2 answered "as accepted": `remaining-loop`; postimage `6e1321e32f72b0fc9f9d987a3175266550a23fa40230df0a61418cfccd4c7961`). The basis cites the record whose I-7 deferral kept PEC on that shape. D-PEC-94 has since exercised that deferral, so the citation is historical:

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

### 3. The port field — `v2/src/pec_v2/core/ports/loop_registry.py` (full postimage)

`RegisteredLoop` gains one field, `feed_profiles: tuple[FeedProfile, ...]`, which is required and has no default. Two core-owned types support it. The port method and its signature are unchanged, and the core still imports no JSON, filesystem or adapter module (only `dataclasses`, `enum`, `typing`).

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

The behaviour changes are listed below; the exact bytes are in the act script and `optionA_vs_abfd0897b.diff`.

- It accepts only `schema_version` 2, as described under backward compatibility.
- Each row needs exactly `loop_id`, `loop_init_path` and `feed_profiles`. A missing field fails at `$.loops[i].<field>` with "required field is missing". An unknown field fails with "field is not defined by schema v2".
- `feed_profiles` must be a non-empty list of objects with exactly `profile`, `version`, `state` and `basis`. Each failure is located at `$.loops[i].feed_profiles[j].<field>`:
  - `profile` must come from the closed vocabulary `FEED_PROFILE_VERSIONS`, a module constant mapping each of the four identifiers to `{1}`;
  - a profile repeated in a row fails at the second occurrence, naming the first;
  - `version` must be an exact `int` in that profile's version set, so `True` and `"1"` are rejected;
  - `state` must be `live` or `historical`;
  - `basis` must pass the same repository-relative path rule as `loop_init_path`, now one shared helper.
- The error class, the file-level failures (absent, unreadable, malformed) and the no-partial-set rule are unchanged. No failure message echoes a document value, except a profile identifier already validated against the closed vocabulary; locations name keys, as before.

### 5. Tests and fixtures

| Path | Act | Content |
|---|---|---|
| `v2/tests/config/test_json_loop_registry.py` | modify | Expected default updated. The schema test checks every field description, each vocabulary entry's description, and that the schema's profile set, version and states equal the adapter's and the port's. New tests: `test_schema_version_1_is_rejected_with_location`; `test_invalid_feed_profiles_are_rejected_with_location` (18 located sub-cases, including the unknown-field ones); `test_additional_loops_need_entries_only` (a second row loads with entries only). `test_invalid_document_never_returns_partial_or_empty_set` also covers the version-1 fixture and a document whose second row alone is invalid |
| `v2/tests/config/test_loop_registry_contract.py` | modify | Immutability now also covers `feed_profiles` and `FeedProfile`. New `test_registered_loop_carries_the_typed_feed_profile_field` pins the field names and order of both dataclasses and the two state values. The three existing port, core-import and stdlib tests are unchanged |
| `v2/tests/config/fixtures/duplicate_loop_id.json`, `missing_loop_id.json` | modify | Migrated to version 2 with one `shared-dev-loop` entry per row, so each still fails at its intended location |
| `v2/tests/config/fixtures/schema_version_1.json` | **create** | Byte-identical to today's `loops.json` (`4ce07ad0…d32e`) |
| `v2/tests/config/fixtures/malformed.json` | unchanged | Still fails as malformed JSON before any version check |

The suite goes from 12 to 16 tests. The mapping to DEL-01-06's verification methods:

| Method | Tests |
|---|---|
| **VER-001** format against the default and malformed fixtures | `test_schema_documents_every_field_and_the_exact_default`, `test_checked_in_default_has_exactly_the_pec_loop`, `test_schema_version_1_is_rejected_with_location`, `test_missing_loop_id_…`, `test_duplicate_loop_id_…`, `test_malformed_json_…`, `test_invalid_feed_profiles_are_rejected_with_location` |
| VER-002 one loop at P1; more loops by entries only | `test_checked_in_default_has_exactly_the_pec_loop`, `test_additional_loops_need_entries_only` |
| **VER-003** invalid, unreadable and absent fail explicitly, with no partial set | `test_absent_file_…`, `test_unreadable_path_…`, `test_invalid_document_never_returns_partial_or_empty_set`, `test_malformed_json_…` |
| VER-004 consumer interface carries no path or serialization detail | `test_port_has_only_the_typed_capability_method`, `test_registered_loop_is_immutable`, `test_registered_loop_carries_the_typed_feed_profile_field` |
| VER-005 no third-party dependency or network call | `test_core_imports_no_adapter_or_outer_io_module`, `test_implementation_uses_only_stdlib_and_no_network_module`, plus `v2-core-posture` (the DEL-01-05 enforcement) and `v2/tests/enforcement` |
| VER-006 the suite runs and passes | `v2-loop-registry` |

## Options

- **A — schema version 2, closed vocabulary, port field, migrated PEC row (recommended).**
  - One act on **11 product paths**: 10 modified and 1 created (the version-1 fixture). Nothing is deleted.
  - The PEC row declares `shared-dev-loop` live and `loop-receipts-ledger` historical. This takes question 2 as "migrated".
  - `software-workflow.json` is unchanged: its rules already select all five checks for these paths.
- **A-R — as A, but the PEC row declares `remaining-loop` as the accepted Notes text says.** Same 11 paths; only `loops.json` and `test_json_loop_registry.py` differ (postimages below). The migration row change then needs a later packet of its own. Choose A-R if the owner wants the migration ruled separately from the schema act, or wants the accepted text followed literally until then.
- **Amend.** The owner changes the scope and the packet is re-prepared. Examples:
  - a different vocabulary or single-profile rows (question 3);
  - a time-bounded dual read of version 1 (question 4);
  - tightened path normalization (finding 3);
  - different `basis` citations;
  - reading PEC's `## Remaining` sections through an added profile.
- **Defer.** Nothing opens.
  - The registry stays version 1 with no profiles. SOW-077 and SOW-094 stay unmet in source.
  - The DEL-01-06 SOW rebuild (S2) waits, since SCA-005 gates it on this packet. Or it proceeds against unimplemented text, which is the "SOW first" ordering.
  - DEL-02-08 discovery "per the loop's declared feed profile" has no declaration to read.
  - No consumer exists yet, so deferring is not unsafe.

A narrower source-only option is not offered. Every part of A is needed for the others to pass: a version-2 loader rejects the version-1 default, and the default cannot declare profiles without the schema and port. Splitting the PEC-row decision is what A-R does.

## Exact product grant (A)

After this ruling and its register row are merged and observed on fetched `origin/main`, one WORKING_ITEMS instance may run the bound act script **once** for PKG-01 / DEL-01-06. The script writes only these paths, relative to `projects/pec/`. The preimage SHA-256 values were read at `abfd0897b`.

| # | Path | Act | Preimage SHA-256 | Postimage SHA-256 (A) |
|---|---|---|---|---|
| 1 | `v2/config/loops.json` | modify | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` | `dc789031afd0bc949baf5aafe0a6221a8c5f72c6810188b84e2d5d2170a694a6` |
| 2 | `v2/config/loops.schema.json` | modify | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | `cb88365c2fba7bdc599348d2b089f8905353062cc0db518e9adfd743bbfe72c8` |
| 3 | `v2/src/pec_v2/core/ports/loop_registry.py` | modify | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` | `a509bfb74920172a86ac21aff6a67245cd3248c5d73ef4e7427966069099c8a9` |
| 4 | `v2/src/pec_v2/core/ports/__init__.py` | modify | `669e1569216722509dcea0ae5ed42dc4a0ca856a196676568ee78d7a38a1edeb` | `e44bf7f00c8ef2cfa5f8006ef2834feb020063df63a3b4b8d8cbd8f359174ff7` |
| 5 | `v2/src/pec_v2/core/__init__.py` | modify | `33c54e244e8e19b66cb2c53c81fa747979f6d512f227f7a56e3f8d57cfb9ff4a` | `0e699a54d6bc202ff7a90c25fdb355da5ed2db185709c3a399870c1b0309c42d` |
| 6 | `v2/src/pec_v2/adapters/config/loop_registry.py` | modify | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` | `c7a2363eb7d7ffaecc4dde8448a9d78572a3ca6e3d18fcfd60fff29d0f5b9c67` |
| 7 | `v2/tests/config/test_json_loop_registry.py` | modify | `d7efb486287d3703aa9ea007eb5376eba95689286bb322c887eeca8b193ac956` | `495c57444061dfb8d95182f14efb8489e0e8c14da9adb29b80f9d44587de39f0` |
| 8 | `v2/tests/config/test_loop_registry_contract.py` | modify | `49b2f6a3b5088bceb82dc393cce050b8800af3a5ac5d34b3b6a3d7b71c01111b` | `b05ed8719c59258998b1c483456b66bd8d4a4d3bc4f68cdd6fb5c02541db7106` |
| 9 | `v2/tests/config/fixtures/duplicate_loop_id.json` | modify | `2e65c719af6c9eb7e170fb25d437b928847dc8d617c056093de213673b3e3396` | `6875f50023f1ad34a45c1af4b0a65316260c45aa05562ce45bb2d9bd8fd13c7e` |
| 10 | `v2/tests/config/fixtures/missing_loop_id.json` | modify | `2155849d9419f0239dca7a69d919ca9ee46a6434106d5326d85bc8c70afc5257` | `f4255b2483a014b542fb7f25c4314ff75dabb5cebbcfe751a2ad3df425f29598` |
| 11 | `v2/tests/config/fixtures/schema_version_1.json` | create | absent | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |

Under A-R, two postimages differ: `v2/config/loops.json` `6e1321e32f72b0fc9f9d987a3175266550a23fa40230df0a61418cfccd4c7961` and `v2/tests/config/test_json_loop_registry.py` `84d695f7b64cbf98539777c17888e516d2141056b658ea5c2b7b6c3730cf5c40`. Path list SHA-256 (the 11 paths, sorted, newline-terminated): `b5db12e59bec0188b1798e8ccf7a3c09300c44e5dbcdf31c16a64aff5e84c73c`.

These paths stay unopened, and the script checks that each is unchanged before writing:

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

The bytes come from one run of `apply_d96.py`, **SHA-256 `08c75241e39e5d00bcecdda3ccf5ae9a869c8689128cf7aca66d54c25fb63664`**. It is stdlib-only Python, prepared with CPython 3.13.7. It is copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/apply_d96.py --repo "$(git rev-parse --show-toplevel)" [--pec-row remaining]
```

Option A is the default; A-R adds `--pec-row remaining`. Before any write, the script:

- checks the six must-remain files;
- checks the 10 preimages, and that the fixture to be created does not exist;
- checks that every embedded postimage decodes to its pinned SHA-256;
- checks that the write set equals the grant.

It then writes, re-hashes every written file, and reports `READ`, `WRITE` and `UNCHANGED` lines. It exits 1 with nothing written on any failure, and exits 1 if run a second time. `--check-only` renders and checks without writing. The product bytes contain no date, so there is no slot rule. `build_apply_d96.py` (`a0a71e6fd3519d40a773d2d62c341a2c089f7e8e21dd8f22d68fa11d3ac1831d`), `apply_d96.template.py` (`4fe61dc1b900e5dfa4c8ed9bec3dc8308537feee9adb59db6172c04fb4258290`) and `build_json_postimages.py` (`51dd6c0774202a828f004e1608ddd0d59cd746ebf0a2ed26efb5f5a7d1feb28b`) are preparation aids, not bound.

## Finite verification

Run the registered checks from `projects/pec` (cwd `.`, as registered) and `harness-self-check` from the repository root. Use an explicit interpreter of Python 3.10 or later (the registry requires 3.10+), record its path and version, and set `PYTHONDONTWRITEBYTECODE=1`. Record every command, exit code and output in the run root. The manager may use `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <ID> --output <run-root>/checks/<ID>.json` from the repository root.

| Check | Command | Required result |
|---|---|---|
| Preconditions | the script's built-in checks; the ruling and its register row on fetched `origin/main`; `pec_reliance_hold.py --operation dispatch-for-production` on each of the 13 targets before dispatch, and `rely-for-production` before fan-in | preimages as tabled; `ALLOW` everywhere; otherwise stop and route the discrepancy |
| Selection | `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json <the 11 paths>` | exactly `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` |
| **`v2-loop-registry` (VER-001, VER-003 rerun)** | `python3 -m unittest discover -s v2/tests/config -p test_*.py` (verbose run recorded, each test mapped to its VER method as tabled above) | exit 0; **Ran 16, OK** (12 before) |
| `v2-store-guard` (`v2/src/pec_v2/**` rule, D-PEC-87 X-1) | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | exit 0; Ran 13, OK; the store still imports the changed `core/ports` package |
| `v2-core-posture` (VER-005; DEL-01-05 enforcement; `always_checks`) | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | exit 0; `"verdict": "PASS"`, zero findings; `core_tree_sha256` changes from `88f590c0…c016` to `dd7e1dda…6e5a`; config and workflow hashes unchanged |
| DEL-01-05 enforcement tests | `python3 -m unittest discover -s v2/tests/enforcement -p test_*.py` | exit 0; Ran 28, OK |
| `v2-api-contract` (`always_checks`) | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | exit 0; Ran 6, OK |
| `harness-self-check` (`always_checks`; every PR) | `PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check` | exit 0; output identical to the pre-act run (on the prototype, `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` both times, stdout `e5f9ff70…d110`) |
| Receipts validator (every PR) | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | exit 0; output unchanged |
| Mutation evidence | `mutate_d96.py projects/pec` (copied into the run root) | baseline passes; M1–M13 each CAUGHT; `RESULT PASS` |
| Byte identity | recompute SHA-256 of the 11 paths | equal to the grant table for the chosen option |
| Basis citations | `test -f` on each `basis` and `loop_init_path` in the new `loops.json` | all present at the act commit |
| Containment | `git diff --name-status origin/main...HEAD` | exactly the 11 paths, plus the run root and, if question 5 is answered yes, `MEMORY.md`; nothing else |
| Whitespace and encoding | `git diff --check origin/main...HEAD`; non-ASCII scan of the 11 postimages | clean; 0 non-ASCII bytes |

Decomposition and dependency validators do not apply: no register, decomposition or dependency file changes. The strict register validator was run on the prototype anyway, and its output was byte-identical before and after.

### Independent verifier

A fresh read-only TASK that authored nothing applies `.agents/skills/software-code-review/SKILL.md` and returns a verdict file. Defects return to the author; the verifier does not repair. It checks:

1. **Basis.** The ruling and its register row are on `origin/main`. The run-root script hashes to `08c75241…3664`, and the recorded preimages match `abfd0897b`.
2. **Reproduction.** It reruns the script on a fresh `git archive` export of `abfd0897b` with the ruled option and gets byte-identical files.
3. **The fixed checks.** It reruns the verification table and gets the same results, including the mutation run.
4. **Semantics.**
   - The schema documents every field.
   - The adapter enforces exactly what the schema states, and no more or less.
   - The vocabulary, versions and states agree across schema, adapter and port.
   - Every failure is located and none returns a partial set.
   - Version 1 is rejected, not read.
   - The core imports stay stdlib-only with no I/O module.
   - The PEC row matches the ruled answer to question 2, and its `basis` paths exist and say what they are cited for.
   - The tests assert no criterion beyond revision-1.5 SOW-077/094, the DEL-01-06 SOW's surviving clauses and this packet (see the SOW-currency note).
5. **Containment.** Nothing else changed: `software-workflow.json`, `service_core_posture.json`, the storage and API files, `malformed.json`, DEL-01-06 `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `_CONTEXT.md`, any decomposition file and `docs/PRD.md`.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-06 only, for this act. The manager runs the reliance preflights and the script. One fresh read-only TASK is the verifier. No author TASK is needed, because the bytes are bound; the manager may instead dispatch a bounded TASK to run the script under `workflows/software-bounded-implementation/WORKFLOW.md`.
- **Run root.** `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/**`, a new folder beside the D-PEC-75 and D-PEC-77 records. It holds:
  - `apply_d96.py` (exact bytes) and its report;
  - `mutate_d96.py` and its output;
  - the check outputs and preflight results;
  - `RUN.md`;
  - `VERIFIER_VERDICT_NN.md`.

  The earlier `_run_records/*` stay immutable.
- **`MEMORY.md` (question 5).** If the owner agrees, the act creates `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/MEMORY.md` from `docs/templates/MEMORY_TEMPLATE.md` (`5a9564f4…6a5a`). At closeout, the undertaking's M1 node writes one run row: run ID, date, "schema version 2 source act under D-PEC-96", the PR and the central receipt. The path does not exist at `abfd0897b`.
- **Not opened.** DEL-01-06 `ScopeOfWork.md`, `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` and `Dependencies.csv`; every other deliverable; `docs/STATUS.md` and `README.md`, which HELP_HUMAN maintains under D-PEC-88 and names in the graph.
- **Models.** Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for the manager and the verifier, as under D-PEC-91 and D-PEC-95, unless the owner states otherwise. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** Branch, commit, push, PR and merge follow the standing Git authorization of 2026-09-12 (Root `AGENTS.md`), with required CI and independent review on the actual candidate. The register row, the graph and the central receipt are HELP_HUMAN's.

## Rollback

- **During execution.** The script writes nothing unless every check passes. If a later check fails, discard the branch or worktree; nothing reaches `origin/main`.
- **Before merge.** Close the PR and discard the branch.
- **After merge, at owner direction.** A revert PR of the act restores the 10 preimages tabled above and removes the created fixture, the run root and, if created, `MEMORY.md`. History is preserved and no reset is made.
- **Stores and consumers.** No store holds registry data and no consumer reads the port, so no migration or consumer rollback exists. The version-1 bytes also survive as `schema_version_1.json` until reverted. If the revert happens after a consumer has been built against `feed_profiles`, that consumer's own packet must roll back first.

## Limits

This proposal, and any ruling selecting A, A-R or an amendment, grants none of the following:

- **No lifecycle change.** DEL-01-06 stays `INITIALIZED` and its Gate 5 HOLD stands. No `_STATUS.md` is touched and no `## Remaining` entry is written.
- **No DEL-01-06 Gate 5 act, and no SOW change.** Gate 5 is not re-entered, RF-001/RF-002 are not reopened, and no `ScopeOfWork.md` byte changes. The rebuild remains graph node S2 under its own packet.
- **No PRD or decomposition change.** Nothing is written in `docs/PRD.md`, `_Decomposition/**`, any register, `_CONTEXT.md`, `_REFERENCES.md` or dependency file. The stale "declares `remaining-loop` now" sentences stay until their own currency acts.
- **No `CHECKING`, `ISSUED`, artifact acceptance, or any readiness or reliance claim.** CHECKING is not an owner gate of this packet, and this packet creates no prompt, gate or reminder about it.
- No other registry row, and no loop added or removed.
- No consumer, parser, fixture suite or grammar. DEL-02-0x and X1 remain their own packets.
- No change to `software-workflow.json`, CI, Root, tier-0, sister-project, instruction or frozen-corpus surfaces.
- No duty on any other loop. A profile is PEC's reading hypothesis, never the loop's truth. Listing a loop creates no duty, cadence or authority (D-PEC-78 O-A).

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.

## Questions only the owner can answer

1. **A, A-R, amend or defer.** Recommendation: **A**.
2. **PEC's own row: the migration row change, ruled here as its own item.** The Q8 (a) premise, "PEC's `LOOP_INIT.md` still selects from `## Remaining`", lapsed with D-PEC-94.
   - **Migrated (recommended):** `shared-dev-loop` v1 `live` (basis: the D-PEC-94 record) and `loop-receipts-ledger` v1 `historical` (basis: `projects/pec/AGENTS.md`). This is the row change SOW-094's Notes and Q8 (a) foresee.
   - **As accepted:** `remaining-loop` v1 `live` (option A-R). Migration then needs a later ruling.
   - **Other:** state the profiles and basis citations.

   Either answer is within the accepted scope, and neither needs a scope change.
3. **Vocabulary and row shape.** Confirm:
   - the closed vocabulary of the four named profiles, each at version 1, with the one-line coverage in the schema;
   - `feed_profiles` as a non-empty list, each profile at most once per row;
   - that adding a profile or version later is a D-PEC code-plus-packet change within schema version 2.

   Recommendation: **confirm**. Alternatives by amendment: a smaller vocabulary (only the two profiles A uses); exactly one profile per row; or a new schema version for every vocabulary change.
4. **Version-1 files.** Rejected with a located error, with the one checked-in default migrated by this act (recommended). Or a time-bounded, tested dual read (amend; D-PEC-78 §4.2 allows it "if needed"). It is not needed, and it would need a defaulting rule that REQ-003 forbids.
5. **Records.** Create DEL-01-06 `MEMORY.md` from the template so the undertaking's closeout can write the run row (recommended), or record this run only in the graph and central receipt and complete without the row (`projects/pec/AGENTS.md` allows either on your decision). The run root under DEL-01-06 `_run_records/` is part of the grant either way.
6. **Model steer.** Keep the defaults above, or state others.

## Preparation evidence

Everything ran in fresh `mktemp -d` directories under the host's temporary area, outside the session scratchpad and outside the checkout:

- `base` is a `git archive` export of the whole tree at `abfd0897b`.
- Each prototype is an APFS clone (`cp -Rc`) of `base` with a variant applied.
- For `harness-self-check` and `git diff`, the base clone and the option-A prototype were made throwaway repositories: `git init`; an `objects/info/alternates` entry pointing read-only at the source object store; `git read-tree abfd0897b`; `update-ref HEAD` inside the export only.

Nothing was written to the checkout or its repository. The interpreter was Python 3.13.7 (CPython), and the local date was 2026-09-25.

| Command (scratch) | Exit | Result |
|---|---|---|
| five registered checks on `base` via `run_registered_checks.py` | 0 ×5 | api 6 OK; registry 12 OK; store 13 OK; posture PASS, 0 findings, core tree `88f590c0…c016`; harness `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124` |
| the same on the option-A prototype | 0 ×5 | api 6 OK; **registry 16 OK**; store 13 OK; posture PASS, 0 findings, core tree `dd7e1dda…6e5a`; harness output byte-identical to `base` (`e5f9ff70…d110`) |
| `v2/tests/enforcement` on `base` / prototype | 0 / 0 | Ran 28, OK / Ran 28, OK |
| `select_affected_checks.py` over the 11 paths | 0 | all five checks |
| `apply_d96.py --check-only` on a fresh clone | 0 | 11 RENDER; tree unchanged |
| `apply_d96.py` (A) on a fresh clone | 0 | 6 UNCHANGED, 11 READ (10 preimages, 1 absent), 11 WRITE; `v2/` byte-identical to the hand-applied prototype; `diff -rq` against `base` shows exactly the 11 paths |
| `apply_d96.py` rerun on the applied clone | 1 | "preimage mismatch v2/config/loops.json …; nothing written" |
| `apply_d96.py` on a clone with `software-workflow.json` altered | 1 | "must-remain file differs: software-workflow.json; nothing written"; no file created |
| `apply_d96.py --pec-row remaining` (A-R) on a fresh clone | 0 | 11 WRITE; differs from A in exactly `loops.json` and the test file; registry suite Ran 16, OK |
| `mutate_d96.py` on the applied A clone | 0 | baseline OK; M1–M13 all CAUGHT: accept version 1; drop the duplicate-profile check; skip the basis path check; widen the vocabulary; admit a `bool` version; admit empty profiles; make profiles optional; unlocated state failure; admit version 2; schema constant back to 1; default declares `remaining-loop`; swap `RegisteredLoop` field order; allow a traversing `loop_init_path` |
| `validate_pec_loop_receipts.py --repo-root .` on `base` / prototype | 0 / 0 | VALID; identical apart from the absolute path prefix |
| `validate_decomposition_registers.py --strict projects/pec/execution` on `base` / prototype | 0 / 0 | 0 errors / 0 warnings; output byte-identical |
| prototype `git diff --check`; non-ASCII scan of the 11 postimages | 0 | clean; 0 non-ASCII bytes |
| path-rule probe on the prototype | 0 | `projects/./pec/AGENTS.md`, `projects//pec/AGENTS.md`, `projects/pec/`, `C:x` and a leading-space path are accepted (finding 3, inherited) |
| `pec_reliance_hold.py … --operation exact-correction-preparation` from `base/projects/pec` | 0 ×13 | `ALLOW` |

Scratch artifacts in the preparer's `g1/` folder, listed with hashes in `g1/SHA256SUMS`:

| Artifact | SHA-256 |
|---|---|
| `apply_d96.py` (the bound act script) | `08c75241e39e5d00bcecdda3ccf5ae9a869c8689128cf7aca66d54c25fb63664` |
| `mutate_d96.py` (mutation runner) | `47b12a59a1f90749ff364f70ab58f1900472e38f113556064deeafc6555834cc` |
| `build_apply_d96.py`, `apply_d96.template.py`, `build_json_postimages.py` (preparation aids) | `a0a71e6f…831d`, `4fe61dc1…8290`, `51dd6c07…b28b` |
| `evidence/optionA_vs_abfd0897b.diff` (A; includes the created fixture) | `7fc3417849f2f4a1ecc0029b1b5804d59fb4492bad77c177e858f352d65c3f95` |
| `evidence/optionAR_vs_optionA.diff` | `c140f51ef084976bdc363795d9a815ac5ef3fa2cb1cb75b61d1b1bae8cb1223e` |
| `evidence/CHECKS_SUMMARY.txt`, `evidence/mutate_d96.out`, `evidence/optionA_v2-loop-registry_verbose.txt`, `evidence/preflight.txt`, `evidence/actA.report.txt`, `evidence/actAR.report.txt`, `evidence/preimages.txt` | in `SHA256SUMS` |
| `postimages/optionA_v2/**`, `postimages/optionAR_overrides/*` (postimage copies for review) | in `SHA256SUMS` |

Basis read for preparation, at `abfd0897b` unless stated:

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
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` | `50e9ea65b904cc6a6154173af092018db232b4584eaa7791704a3bb59c847211` |
| `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md` | `f32ab9d2545e1b3fad40a5445db2de93b3a88f5bae9695924fc807e156133802` |
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
| Brief G1 (scratch) | `084eadd8eeb77a3c2fa31e0c51646e69bbb18c8bd2a30da750c69222c2b0fca1` |

Attribution: prepared by a TASK (Type 2) under HELP_HUMAN, node G1 of `HELP-HUMAN-PEC-20260925-POST-SCA005`, with no delegation. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are instruction-asserted.
