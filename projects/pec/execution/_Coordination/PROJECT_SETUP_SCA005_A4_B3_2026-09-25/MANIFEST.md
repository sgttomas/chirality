# PROJECT_SETUP — SCA-005 A4 + B3 (D-PEC-93 option A) Manifest

**Status:** EXECUTED / VALIDATED (independent verification recorded separately; see `HANDOFF_STATE.md`)
**Owning instrument:** PROJECT_SETUP under `D-PEC-93` option A
**Act date `{D}`:** 2026-09-25 (local date at the generator run; America/Denver, MDT; no clock or time-zone manipulation)
**Branch:** `claude/pec-d93-project-setup-act`
**Branch basis:** `origin/main` `04e04da00f620a1a5786ee744b167490cc90531c` (PR #913 merge)
**Act commit (product writes and checks):** `995af4f368d0d8cc0b3134eef484b4b9618aa8ac`

This package is derivative coordination evidence. It cites accepted upstream
truth and does not replace decomposition, scope-change or decision authority.

## Authority

| Instrument | SHA-256 |
|---|---|
| `_DECISIONS/D-PEC-93_RULING_2026-09-25.md` (owner: "D-PEC-93: A."; clarifications N1, N2, N5, N6) | `ffb0b58293d868e1d7ddf61d2958a6b18ca73fa0c36da077f5309a8782153709` |
| `_DECISIONS/D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md` (the specification) | `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422` |
| `_DECISIONS/_REGISTER.md` row D-PEC-93 (`RULED A / EFFECTIVE ON MERGE`), observed on fetched `origin/main` `04e04da00` | — |
| `gen_d93.py` (this run root; byte-identical to `PROJECT_SETUP_SCA005_A4_B3_PREP_2026-09-25/gen_d93.py`) | `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2` |

## Binding command (run once, from the repository root)

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/gen_d93.py --repo /Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-adb8a84864c6fa862 --act-date 2026-09-25
```

No `--mirror-set`, no `--optional-edge`, default `--actor` (`TASK+preparation`).
The proposal writes `--repo "$(git rev-parse --show-toplevel)"`; the host's
worktree-isolation guard refused command substitution, so the literal value
was passed. `git rev-parse --show-toplevel` printed exactly that path
immediately before the run. Exit 0, empty stderr (`gen_d93_stderr.txt`),
report `gen_d93_report.tsv` (27 READ, 31 WRITE, 2 CHECK lines).

## Exact live-effect manifest (31 product paths + 1 pointer)

Every written path is on the proposal's 31-path list, and every postimage
equals the proposal table at `{D}` = 2026-09-25 (`checks/01_postimage_hashes.out`,
31/31). The act date equals the table date, so no slot substitution applies.

| Path (relative to `projects/pec/execution/`) | Act | Postimage SHA-256 |
|---|---|---|
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/_STATUS.md` | CREATE (`OPEN`, `TASK+preparation`) | `d80800a48b45a43d641916bd5ee67c4b478e21538281b833e34dbc7cfe5f0eef` |
| `…/DEL-02-08_Work_graph_parser/_CONTEXT.md` | CREATE | `721a9807211b1330b0cd124139d37fdb9b2f9167b9edc461f218bb4570f34d20` |
| `…/DEL-02-08_Work_graph_parser/_REFERENCES.md` | CREATE | `87f95d423851a800651c6e01c4b04a7434b5f56f3476b5512075da556563840b` |
| `…/DEL-02-08_Work_graph_parser/_DEPENDENCIES.md` | CREATE | `0ee572b955cedf628958305e049b0f776bec3fad39dada73bca88b1421959a3d` |
| `…/DEL-02-08_Work_graph_parser/_SEMANTIC.md` (empty) | CREATE | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `…/DEL-02-08_Work_graph_parser/Dependencies.csv` | CREATE | `c23cd711fc8762dbd4a8629ba277753544f9f9e91368f789140b040f94cf701e` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/_STATUS.md` | CREATE (`OPEN`, `TASK+preparation`) | `3e14313c78e2500cabbd3f4897f9095daabc75c6468169074cb4400f4667d768` |
| `…/DEL-02-09_MEMORY_run_index_parser/_CONTEXT.md` | CREATE | `2413b5c0b241eb44c9e53401499729ca3b84e23860692b63f09104af56640502` |
| `…/DEL-02-09_MEMORY_run_index_parser/_REFERENCES.md` | CREATE | `211cb59ce46a7399ba56775fa57024f018322ebf2f50ecaf0887eb419d06073f` |
| `…/DEL-02-09_MEMORY_run_index_parser/_DEPENDENCIES.md` | CREATE | `41c841a4cac76634bd5f1aae664152f9488c073b5ef5c254f2fe2cdaaebadf3a` |
| `…/DEL-02-09_MEMORY_run_index_parser/_SEMANTIC.md` (empty) | CREATE | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `…/DEL-02-09_MEMORY_run_index_parser/Dependencies.csv` | CREATE | `41afd6dc44f21200f6b2a1c480e9175d98b64d49b12e638bca67edcd15168e4b` |
| `PKG-03_…/DEL-03-01_Full_rebuild_reconciler_one_command/Dependencies.csv` | MODIFY | `833fbfe0c2a09ab8b564866dff8e55327fb005d5c4993973ef93408d2e2a436b` |
| `PKG-06_…/DEL-06-04_Live_hierarchy_edges/Dependencies.csv` | MODIFY | `ac55576e8bb4b17ba57d7e1d92e96415ce4f9da40c2c742e8be769df4d49b8fc` |
| `PKG-07_…/DEL-07-02_Daemon_SSE_subscriber_bridge/Dependencies.csv` | MODIFY | `77230bbbc0e809c4e9e0c3a8353ad5bf4f42ee7ad7849b7199a33c84f0b1d8dd` |
| `PKG-07_…/DEL-07-04_cmux_socket_adapter_optional/Dependencies.csv` | MODIFY | `cbb2175b28c4a1ba8e7ec58777d8831d20053b14363f63647ff727f7a5392b12` |
| `PKG-07_…/DEL-07-05_Shared_runtime_client_seam_v2/Dependencies.csv` | MODIFY | `aa1dbe679b23450fed5eb603d687ae91cfa3fa9550f33d057094f9366ec6d41c` |
| `PKG-09_…/DEL-09-05_Presence_board/Dependencies.csv` | MODIFY | `9811343ccb1f9e6820a03ebdac5aa53f163d355049508815438befb35db032d5` |
| `PKG-00_…/DEL-00-02_Event_contract_schema_v1/_DEPENDENCIES.md` | MODIFY | `818a06a33952651ce70c415b33bfc7c381898eda4891cd33cb21472bc4b62c3c` |
| `PKG-01_…/DEL-01-01_Record_tier_schema_entity_model/_DEPENDENCIES.md` | MODIFY | `1c39420c392e09b7e37edb48680bf203018ddad64a1cfbdae98808bbab5172f0` |
| `PKG-01_…/DEL-01-02_Presence_tier_schema_entity_model/_DEPENDENCIES.md` | MODIFY | `625bb400c65ff866369bfb1789244e651570555f2ac7054cd9ceac505455052e` |
| `PKG-03_…/DEL-03-01_Full_rebuild_reconciler_one_command/_DEPENDENCIES.md` | MODIFY | `e039ded3a08b3951540d960c3c626ebccde1f24df7584416326325dcd8d261ec` |
| `PKG-06_…/DEL-06-01_Session_presence_records/_DEPENDENCIES.md` | MODIFY | `9fd90c726544d06550f730c383a38df4aedcfb8dc0d5582432af0a80a5d1afad` |
| `PKG-07_…/DEL-07-01_Idempotent_event_ingest_durable_message_store/_DEPENDENCIES.md` | MODIFY | `2ea6519dec0866dc38881d0074d2893cb7b635c53ea703516b21014ff10a5360` |
| `PKG-07_…/DEL-07-03_Hooks_CLI_bridge/_DEPENDENCIES.md` | MODIFY | `a9536c7a9a7caf419a941f204f9cd4d71b328b5047e142fb04d96017655d7b8b` |
| `PKG-09_…/DEL-09-05_Presence_board/_DEPENDENCIES.md` | MODIFY | `faa212e0c6f667c291177f6a2859799302fe84d0fdea20f83c91e35e45965251` |
| `PKG-02_…/DEL-02-07_adapter_yaml_feed_manifest_consumer/_DEPENDENCIES.md` | MODIFY | `2e53136f4580ae902b732c0ae657913d02e380b2a30350be39935347f88c8cdb` |
| `PKG-06_…/DEL-06-04_Live_hierarchy_edges/_DEPENDENCIES.md` | MODIFY | `d6a1ad590fddacf18132411661a11fa613436573fc3b480f7cad61f90e4d034d` |
| `PKG-07_…/DEL-07-02_Daemon_SSE_subscriber_bridge/_DEPENDENCIES.md` | MODIFY | `f315d8a8bd7bb34ecabc0d32fd6a6c92ceaf6e070ae26c346d87cc3f3d06da89` |
| `PKG-07_…/DEL-07-04_cmux_socket_adapter_optional/_DEPENDENCIES.md` | MODIFY | `b1dc2ed3c6d78e3412907d72fbc2ea4b229861717b985a7f16852808b9df3ac6` |
| `PKG-07_…/DEL-07-05_Shared_runtime_client_seam_v2/_DEPENDENCIES.md` | MODIFY | `fc43eb3d3873cce8f9e488a039bcf8379ea7ecbc83436d2817e925ca3b863617` |
| `_Evaluation/DecompCoverage/_LATEST.md` (conditional; moved after 0 BLOCKERs) | MODIFY | preimage `0084d218b6106482dbf3f73933d44de5ed43c15b8515b48c70b098c985df7432` → `2b43dc3bb34163ae51067f6176ebf235430b59aa668890c1e65d7cc9d3cf1450` |

The 19 MODIFY preimages equal the proposal table at `04e04da00` (the same
bytes as at `6dac281c6`): the generator's fail-closed guard and READ lines,
and `checks/00b_preimages_at_04e04da00.out` (31/31). Aggregate over the 31 product paths in bytewise-sorted path
order: `c4525add6b621d16523ad7567410b96f1864683cf93fd0d03c3f43954a79727a`;
newline-terminated path-list hash
`1133e1ab0867f71f01346ed566cd8ede7fa2cff73ef79e4dbf87bc3bc8dcb9f1` — both
equal the proposal (`checks/09_aggregate.out`).

The pointer postimage is exactly the tool's two lines:
`Latest: COV_SCA005_POSTSETUP_2026-09-25_1606` and `Updated: 2026-09-25`.
The hand-added paragraph of the preimage is not carried, as the proposal states.

## Row effects

Across the 66 registers: 255 → 263 rows (ANCHOR 136 → 140; EXECUTION
119 → 123). 20 rows retired, 1 refreshed (`DEP-03-01-007`), 8 added
(`DEP-02-08-001..003`, `DEP-02-09-001..003`, `DEP-03-01-015`, `-016`), 0
deleted (`checks/06_row_conservation_and_quotes.out`).

## Re-audit

`_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/` (TASK
`audit-decomp`, SOFTWARE, ALL, revision 1.5, compared with
`COV_SCA005_POSTCHANGE_2026-09-25_1344`): 0 BLOCKER, 3 WARNING (all
PRE-EXISTING), 70 INFO; `overall_status` `WARNINGS`, `closure_readiness`
`WARN`. File hashes are in `HANDOFF_STATE.md`.

## Run-root contents

`gen_d93.py`, `gen_d93_report.tsv`, `gen_d93_stderr.txt`, `closure/` (the
analyzer's output directory), `checks/` (every command, exit code and output;
`COMMANDS.txt` is the index), `probes/` (the manager's check scripts and the
31-path table extracted from the proposal), this file, `VALIDATION.md`,
`HANDOFF_STATE.md` and `VERIFIER_VERDICT_NN.md`. No `_run_records/` entry was
written in any deliverable.
