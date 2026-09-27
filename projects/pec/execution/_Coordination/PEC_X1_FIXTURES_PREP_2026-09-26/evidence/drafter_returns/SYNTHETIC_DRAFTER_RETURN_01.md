## X1 synthetic grammar-edge fixtures: drafter report (TASK, brief B)

**Status: complete.** I wrote 27 synthetic fixture files and `MANIFEST.json` covering 24 cases: 8 for DEL-02-08, 8 for DEL-02-09 and 8 for DEL-02-03, including the 3 constructed at test time. They sit under the drafting stub in my mktemp copy of the candidate `parsers/` directory. The full candidate suite passed 10/10, including the three required tests.

**mktemp path:** `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1syn.Wsbloe`
- `parsers/`: the copy of `candidates/projects/pec/v2/tests/parsers/`. `fixtures/pinned/` has been replaced by `drafting_stub/pinned/`, and `fixtures/synthetic/` holds my files.
- `make_manifest.py` generates the manifest. `broad_copy_check.py` is my extra copy check. Neither is parser code.
- `TMPDIR` pointed at this directory for every command. `run_fixture_suite.sh` made and removed its own `x1pfix.*` directory inside it.

**Boundary compliance:**
- I wrote nothing in any Git worktree and did no checkout, branch switch or branch creation.
- `git status --short` in `pec-x1-fixtures-prep` was empty at the end. That worktree's HEAD is `3f41666bb1e59917a498d1622241540880adb726`.
- Repository reads used plain file reads and read-only plumbing only (`cat-file`, `ls-tree`, `rev-parse`, `hash-object` without `-w`, `log -1`).
- No network. No parser code.

**Basis read:**
- AGENT_TASK.md, root AGENTS.md, projects/pec/AGENTS.md and the brief.
- The three contracts in full, all byte-identical to HEAD:
- DEL-02-08 `ScopeOfWork.md`, blob `1a006f7d78510bbdd96c4949605873166f0e4856`
- DEL-02-09, blob `226e9ca150f3291b88b61cd4d663149f0e34b060`
- DEL-02-03, blob `3e0a48c6ac3e05c3bde475d0080c1f7a9e7533ab`
- Both templates. Their blobs `91f10bfb…` and `0aebc32f…` match the stub pins.
- The candidate test module.
- For shape only, not copied: the PEC ledger blob `ea6f32cc…` (marker line and nested cursor bullets), the FC-1 receipt blob `23623e2c…` and the FC-1 graph blob `ae942d99…`.

### Checks run

- **Hygiene** (every file, including the manifest): 28 files, 0 problems. Checked for ASCII only, LF only, no tabs, no trailing spaces, exactly one final newline, no `remaining` in any case, no canonical file names. Both marker lines' `prefix-bytes`/`prefix-sha256` values re-verified against the file bytes.
- **Broader copy check (my own, beyond the stub):** 8-word runs of every blob at `d61981ee2` and `6c6cc1b` named `WORK_GRAPH.md`, `MEMORY.md`, `RECEIPT.md`, `LOOP_RECEIPTS.md` or `EVIDENCE.md` (300 blobs, 453,266 runs), minus the template runs, compared against every synthetic file. Result: 0 overlaps. The fixtures should therefore survive a wider final pin set drawn from those file names.
- **First suite run failed 7 copy subtests.** They came from structural seams, not prose, and I fixed them:
- The run `| ## Current state and recovery - Checked` (a table immediately followed by the recovery heading) occurs in pinned graphs but not in the template.
- `| W1, V1, P1, C1, M1, F1 |` matched the App graph blob.
- My own words "is claimed." happened to match the Piping receipt next to `## Cursor and pointers`.
- Fixes: a one-line filler paragraph between tables and the next heading, "M1 and F1", and reworded prose. Other drafters will likely hit the same seam hazard.

Suite output tail (final run, verbatim; command `zsh run_fixture_suite.sh <worktree> 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240 <mktemp>/parsers -v`):
```
test_every_record_binds_a_requirement_criterion_and_verification (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_every_record_binds_a_requirement_criterion_and_verification) ... ok
test_git_access_is_read_only_and_allowlisted (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_git_access_is_read_only_and_allowlisted) ... ok
test_golden_source_values_are_grounded_in_their_pinned_blobs (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_golden_source_values_are_grounded_in_their_pinned_blobs) ... ok
test_goldens_are_content_minimal_and_hold_no_source_text_run (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_goldens_are_content_minimal_and_hold_no_source_text_run) ... ok
test_loaded_suite_has_exact_verification_mapping (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_loaded_suite_has_exact_verification_mapping) ... ok
test_manifests_and_goldens_are_well_formed (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_manifests_and_goldens_are_well_formed) ... ok
test_no_fixture_source_is_copied_into_the_tree (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_no_fixture_source_is_copied_into_the_tree) ... ok
test_pins_resolve_by_read_only_plumbing_on_integrated_history (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_pins_resolve_by_read_only_plumbing_on_integrated_history) ... ok
test_synthetic_cases_cover_the_contract_minimums (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_synthetic_cases_cover_the_contract_minimums) ... ok
test_tree_expectations_hold_at_their_pinned_commits (test_parser_fixture_integrity.ParserFixtureIntegrityTests.test_tree_expectations_hold_at_their_pinned_commits) ... ok

----------------------------------------------------------------------
Ran 10 tests in 1.000s

OK
```
The stub goldens also passed, so there were no stub-only failures to set aside.

### Case → contract-line bindings

Line numbers are for the contract blobs named above (worktree HEAD `3f41666bb`).

**DEL-02-08** (`.../DEL-02-08_Work_graph_parser/ScopeOfWork.md`):

| Case | Bound IDs (line) |
|---|---|
| SYN-WG-01 missing-run-identity | REQ-006 (L156), REQ-017 (L167), AC-006 (L177), AC-017 (L188), VER-006 (L217), VER-017 (L228) |
| SYN-WG-02 duplicated-run-identity | REQ-006 (L156), REQ-017 (L167), AC-006 (L177), AC-017 (L188), VER-006 (L217), VER-017 (L228) |
| SYN-WG-03 unrecognized-state-token | REQ-004 (L154), REQ-017, AC-004 (L175), AC-017, VER-004 (L215), VER-017 |
| SYN-WG-04 no-node-table | REQ-009 (L159), REQ-017, AC-009 (L180), AC-017, VER-009 (L220), VER-017 |
| SYN-WG-05 unresolved-pr-number | REQ-008 (L158), REQ-017, AC-008 (L179), AC-017, VER-008 (L219), VER-017 |
| SYN-WG-06 two-graphs-bind-one-deliverable | REQ-007 (L157), REQ-015 (L165), REQ-017, AC-007 (L178), AC-015 (L186), AC-017, VER-007 (L218), VER-015 (L226), VER-017 |
| SYN-WG-07 prose-in-every-position | REQ-010 (L160), AC-010 (L181), VER-010 (L221) |
| SYN-WG-08 links-and-bindings | REQ-007 (L157), AC-007 (L178), VER-007 (L218) |

**DEL-02-09** (`.../DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md`):

| Case | Bound IDs (line) |
|---|---|
| SYN-MEM-01 template-table-form | REQ-002 (L141), REQ-004 (L143), REQ-014 (L153), AC-002 (L158), AC-004 (L160), AC-014 (L170), VER-002 (L193), VER-004 (L195), VER-014 (L205) |
| SYN-MEM-02 entry-without-readable-run-token | REQ-004 (L143), REQ-014, AC-004 (L160), AC-014, VER-004 (L195), VER-014 |
| SYN-MEM-03 unreadable-date | REQ-005 (L144), REQ-014, AC-005 (L161), AC-014, VER-005 (L196), VER-014 |
| SYN-MEM-04 file-without-run-index-entry | REQ-001 (L140), REQ-014, AC-001 (L157), AC-014, VER-001 (L192), VER-014 |
| SYN-MEM-05 deliverable-without-memory-file | REQ-001 (L140), REQ-014, AC-001 (L157), AC-014, VER-001 (L192), VER-014 |
| SYN-MEM-06 runs-section-mixed-with-dated-sections | REQ-007 (L146), REQ-014, AC-007 (L163), AC-014, VER-007 (L198), VER-014, TBD-005 (L130) |
| SYN-MEM-07 prose-in-every-position | REQ-008 (L147), AC-008 (L164), VER-008 (L199) |
| SYN-MEM-08 links-in-each-form | REQ-003 (L142), AC-003 (L159), VER-003 (L194) |

**DEL-02-03** (`.../DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md`):

| Case | Bound IDs (line) |
|---|---|
| SYN-RCP-01 marker-carrying-ledger-entry | REQ-003 (L174), REQ-017 (L188), AC-003 (L193), AC-018 (L208), VER-003 (L234), VER-017 (L248) |
| SYN-RCP-02 prose-structured-ledger-entry | REQ-004 (L175), REQ-017, AC-004 (L194), AC-018, VER-004 (L235), VER-017 |
| SYN-RCP-03 receipt-without-examined-through | REQ-004 (L175), REQ-017, AC-004 (L194), AC-018, VER-004 (L235), VER-017 |
| SYN-RCP-04 malformed-ledger | REQ-004, REQ-017, AC-004, AC-018, VER-004, VER-017 (AC-004 and VER-004 name malformed fixtures explicitly) |
| SYN-RCP-05 unreadable-file | REQ-004, REQ-017, AC-004, AC-018, VER-004, VER-017 (AC-004 and VER-004 name unreadable fixtures explicitly) |
| SYN-RCP-06 undeclared-loop | REQ-014 (L185), REQ-017, AC-015 (L205), AC-018, VER-014 (L245), VER-017 |
| SYN-RCP-07 receipt-folder-diverges-from-cursor | REQ-016 (L187), AC-017 (L207), VER-016 (L247); VER-016 names "a synthetic receipt whose folder name differs from its cursor Receipt-ID" |
| SYN-RCP-08 prose-in-every-position | REQ-007 (L178), AC-007 (L197), VER-007 (L238) |

### Judgment calls and open points for the manager

1. **ASCII rule versus the observed em dash.** DEL-02-09 CLM-016 says observed bullets open with "a date, an em dash and a backticked run token". Because the brief binds ASCII only, my bullet-form and dated-heading fixtures use ` -- ` instead. A grammar that requires an em dash will not read them as written; a test would have to substitute the character when copying into place, or the packet should rule on this.
2. **Labels are case-folded.** `expect` allows only lowercase-hyphen labels, so:
 - SYN-RCP-07 records the cursor token `SYN-RUN-RCP-CURSOR-0701` as `syn-run-rcp-cursor-0701` and the placement folder as `syn-run-rcp-folder-0702`.
 - State and field names are lowercased (`planned`…, `receipt-id`…).
 - Tests must compare case-insensitively. Placing the file in the lowercase folder still exercises folder ≠ cursor.
3. **Counts assume likely grammar choices.** TBD-002 in both DEL-02-08 and DEL-02-09 leaves the grammar open, so the integer expectations rest on these assumptions:
 - The template `## Work` table is the node table.
 - The `## Runs` first cell `token / date` is the declared token and date position.
 - Links are Markdown inline links or autolinks. No backticked bare paths are used in the links fixtures, to keep link counts unambiguous.
 - A grammar chosen differently would require a fixture-local expectation change, not a contract change.
4. **PR links use `https://example.invalid/synthetic/pull/N`,** so nothing points at a real host. A grammar keyed only to `github.com/.../pull/N` would not count them as PR links, which affects SYN-MEM-08 `pr_links_per_file`. Every PR link text also carries `PR #N` or `#N`.
5. **Open questions left open in the expectations:**
 - SYN-WG-04 sets `presented_as_complete: false` rather than fixing a parse outcome, because the contract does not choose between partial and unparseable.
 - SYN-MEM-06 requires only form attribution, no silent omission and no dated-heading token (DEL-02-09 CON-004). It does not fix how the file is read, because TBD-005 is open; I also bound TBD-005.
6. **SYN-MEM-03 uses shapes that no ISO date grammar reads** (`late-zebra-season`, `2026-09-XX`) rather than impossible calendar dates, so the expectation does not presume calendar validation.
7. **Marker prefix values are truthful.** In PEC's ledger blob `ea6f32cc`, `prefix-bytes=426714` equals the marker line's byte offset, and the SHA-256 of those bytes equals the recorded `prefix-sha256`. That is my reading of the semantics. I computed the same values over the synthetic ledgers (890/`936296a7…` and 396/`a979ba5b…`). Editing the bytes before a marker line invalidates them. The fake-SHA rule applies to commits, which all use repeated patterns.
8. **Decoys planted so a parser can be shown not to infer:**
 - `SYN-RUN-DECOY-0101` in prose (SYN-WG-01).
 - In SYN-MEM-02: decision identifier `D-SYN-9202`, parenthesized `(ZEBRA_PAREN_0202)`, and a path folder `SYN-RUN-DECOY-0203`.
 - A merge SHA in Result prose (SYN-RCP-03).
 - An "Examined through:" prose line with no marker (SYN-RCP-02).
 - Link-target file names avoid canonical names too (`SYN_RECEIPT.md`, `SYN_GRAPH.md`, `SYN_EVIDENCE.md`).
9. **Bindings needing review:**
 - SYN-WG-06 binds DEL-02-08 REQ-015/AC-015/VER-015 because overlap detection belongs to DEL-06-06. VER-015 is an inspection method, so the fixture supports it rather than executing it.
 - SYN-RCP-06 binds AC-015 (discovery) alongside AC-018.
 - SYN-WG-01 keeps the brief's example binding exactly.
10. **Construction cases reuse a file.** SYN-RCP-05 and SYN-RCP-06 both reuse `receipts/marker_carrying_ledger_entry.md`. SYN-MEM-05 names the folder `DEL-99-15` and no file.
11. **Packet-named paths are not established.** DEL-02-08 REQ-017, DEL-02-03 REQ-017 and DEL-02-03 AC-018 require synthetic fixtures "only at paths a ruled packet names". I cannot confirm that the provisional D-PEC-106 packet names `projects/pec/v2/tests/parsers/fixtures/synthetic/**`; that is for the packet and the owner.
12. **Other choices:**
 - The non-vocabulary token is `MARINATING`, on exactly one node.
 - State cells follow the template's `STATE; text` shape.
 - The duplicate identities use the plain template spelling with two different values.

### MANIFEST.json (verbatim; `fixtures/synthetic/MANIFEST.json`, git blob `807ebf09208127f2556c24c8b8856c6ac6563065`)

```json
{
"schema": "pec-v2-parser-fixtures-synthetic/v1",
"cases": [
  {
    "id": "SYN-WG-01",
    "case": "missing-run-identity",
    "files": [
      "work_graph/missing_run_identity.md"
    ],
    "expect": {
      "run_identity_available": false,
      "fabricated_identity": false,
      "limitation": "missing-run-identity",
      "nodes_emitted": 3
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-006",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-006",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-02",
    "case": "duplicated-run-identity",
    "files": [
      "work_graph/duplicated_run_identity.md"
    ],
    "expect": {
      "declared_identity_bullets": 2,
      "run_identity_available": false,
      "fabricated_identity": false,
      "limitation": "duplicated-run-identity",
      "nodes_emitted": 2
    },
    "binds": [
      "DEL-02-08/REQ-006",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-006",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-006",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-03",
    "case": "unrecognized-state-token",
    "files": [
      "work_graph/unrecognized_state_token.md"
    ],
    "expect": {
      "recognized_states": [
        "planned",
        "ready",
        "active",
        "blocked",
        "uncertain",
        "complete"
      ],
      "recognized_state_nodes": 6,
      "unrecognized_state_nodes": 1,
      "limitation": "unrecognized-state",
      "coerced_state": false,
      "unrecognized_token_carried": false
    },
    "binds": [
      "DEL-02-08/REQ-004",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-004",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-004",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-04",
    "case": "no-node-table",
    "files": [
      "work_graph/no_node_table.md"
    ],
    "expect": {
      "run_identity_available": true,
      "nodes_emitted": 0,
      "limitation": "no-node-table",
      "presented_as_complete": false
    },
    "binds": [
      "DEL-02-08/REQ-009",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-009",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-009",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-05",
    "case": "unresolved-pr-number",
    "files": [
      "work_graph/unresolved_pr_number.md"
    ],
    "expect": {
      "cited_pr": 99999999,
      "pr_resolution": "unresolved-locally",
      "guessed_commit": false,
      "network_access": false
    },
    "binds": [
      "DEL-02-08/REQ-008",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-008",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-008",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-06",
    "case": "two-graphs-bind-one-deliverable",
    "files": [
      "work_graph/two_graphs_bind_one_deliverable_a.md",
      "work_graph/two_graphs_bind_one_deliverable_b.md"
    ],
    "expect": {
      "graphs_parsed": 2,
      "graphs_binding_shared_deliverable": 2,
      "bindings_emitted_per_graph": true,
      "overlap_verdict_emitted": false
    },
    "binds": [
      "DEL-02-08/REQ-007",
      "DEL-02-08/REQ-015",
      "DEL-02-08/REQ-017",
      "DEL-02-08/AC-007",
      "DEL-02-08/AC-015",
      "DEL-02-08/AC-017",
      "DEL-02-08/VER-007",
      "DEL-02-08/VER-015",
      "DEL-02-08/VER-017"
    ]
  },
  {
    "id": "SYN-WG-07",
    "case": "prose-in-every-position",
    "files": [
      "work_graph/prose_in_every_position.md"
    ],
    "expect": {
      "prose_marker": "zebra-prose",
      "prose_in_output": false,
      "prose_capable_field_types": 0
    },
    "binds": [
      "DEL-02-08/REQ-010",
      "DEL-02-08/AC-010",
      "DEL-02-08/VER-010"
    ]
  },
  {
    "id": "SYN-WG-08",
    "case": "links-and-bindings",
    "files": [
      "work_graph/links_and_bindings.md"
    ],
    "expect": {
      "distinct_del_bindings": 2,
      "relative_links": 2,
      "external_urls": 2,
      "link_text_emitted": false,
      "external_url_followed": false,
      "external_url_emitted_as_path": false
    },
    "binds": [
      "DEL-02-08/REQ-007",
      "DEL-02-08/AC-007",
      "DEL-02-08/VER-007"
    ]
  },
  {
    "id": "SYN-MEM-01",
    "case": "template-table-form",
    "files": [
      "memory/template_table_form.md"
    ],
    "expect": {
      "form": "table",
      "entries": 3,
      "run_tokens_read": 3,
      "dates_read": 3,
      "run_id_unavailable_entries": 0
    },
    "binds": [
      "DEL-02-09/REQ-002",
      "DEL-02-09/REQ-004",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-002",
      "DEL-02-09/AC-004",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-002",
      "DEL-02-09/VER-004",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "SYN-MEM-02",
    "case": "entry-without-readable-run-token",
    "files": [
      "memory/entry_without_readable_run_token.md"
    ],
    "expect": {
      "form": "table",
      "entries": 3,
      "run_tokens_read": 1,
      "run_id_unavailable_entries": 2,
      "dates_read": 3,
      "inferred_run_id": false
    },
    "binds": [
      "DEL-02-09/REQ-004",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-004",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-004",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "SYN-MEM-03",
    "case": "unreadable-date",
    "files": [
      "memory/unreadable_date.md"
    ],
    "expect": {
      "form": "table",
      "entries": 3,
      "run_tokens_read": 3,
      "dates_read": 1,
      "dates_unavailable": 2,
      "inferred_date": false
    },
    "binds": [
      "DEL-02-09/REQ-005",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-005",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-005",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "SYN-MEM-04",
    "case": "file-without-run-index-entry",
    "files": [
      "memory/file_without_run_index_entry.md"
    ],
    "expect": {
      "entries": 0,
      "coverage_limit": true,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-001",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-001",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "SYN-MEM-05",
    "case": "deliverable-without-memory-file",
    "files": [],
    "construction": "At test time, create a deliverable folder DEL-99-15 inside a loop whose registry declaration covers the run index, and put no MEMORY file in it.",
    "expect": {
      "entries": 0,
      "coverage_limit": true,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-09/REQ-001",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-001",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-001",
      "DEL-02-09/VER-014"
    ]
  },
  {
    "id": "SYN-MEM-06",
    "case": "runs-section-mixed-with-dated-sections",
    "files": [
      "memory/runs_section_mixed_with_dated_sections.md"
    ],
    "expect": {
      "runs_bullet_entries": 2,
      "dated_sections": 2,
      "every_entry_names_form": true,
      "silent_omission": false,
      "dated_heading_run_token_emitted": false
    },
    "binds": [
      "DEL-02-09/REQ-007",
      "DEL-02-09/REQ-014",
      "DEL-02-09/AC-007",
      "DEL-02-09/AC-014",
      "DEL-02-09/VER-007",
      "DEL-02-09/VER-014",
      "DEL-02-09/TBD-005"
    ]
  },
  {
    "id": "SYN-MEM-07",
    "case": "prose-in-every-position",
    "files": [
      "memory/prose_in_every_position_table.md",
      "memory/prose_in_every_position_bullet.md",
      "memory/prose_in_every_position_heading.md"
    ],
    "expect": {
      "forms": [
        "table",
        "bullet",
        "dated-heading"
      ],
      "prose_marker": "zebra-prose",
      "prose_in_output": false,
      "prose_capable_field_types": 0
    },
    "binds": [
      "DEL-02-09/REQ-008",
      "DEL-02-09/AC-008",
      "DEL-02-09/VER-008"
    ]
  },
  {
    "id": "SYN-MEM-08",
    "case": "links-in-each-form",
    "files": [
      "memory/links_in_each_form_table.md",
      "memory/links_in_each_form_bullet.md",
      "memory/links_in_each_form_heading.md"
    ],
    "expect": {
      "forms": [
        "table",
        "bullet",
        "dated-heading"
      ],
      "relative_links_per_file": 1,
      "pr_links_per_file": 1,
      "external_urls_per_file": 1,
      "link_text_emitted": false,
      "external_url_followed": false,
      "external_url_emitted": false
    },
    "binds": [
      "DEL-02-09/REQ-003",
      "DEL-02-09/AC-003",
      "DEL-02-09/VER-003"
    ]
  },
  {
    "id": "SYN-RCP-01",
    "case": "marker-carrying-ledger-entry",
    "files": [
      "receipts/marker_carrying_ledger_entry.md"
    ],
    "expect": {
      "marker_present": true,
      "governed_entries": 2,
      "ungoverned_entries": 2,
      "governed_fields": [
        "receipt-id",
        "examined-through",
        "parent-receipt",
        "gate-outcome"
      ],
      "prose_valued_fields": 1,
      "prose_value_presence_only": true,
      "ungoverned_fields_unavailable": true,
      "fabricated_value": false,
      "fifth_contract_field": false
    },
    "binds": [
      "DEL-02-03/REQ-003",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-003",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-003",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-02",
    "case": "prose-structured-ledger-entry",
    "files": [
      "receipts/prose_structured_ledger_entry.md"
    ],
    "expect": {
      "marker_present": false,
      "entries": 2,
      "contract_fields_marked_unavailable": true,
      "inferred_field": false,
      "prose_in_output": false
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-004",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-004",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-03",
    "case": "receipt-without-examined-through",
    "files": [
      "receipts/receipt_without_examined_through.md"
    ],
    "expect": {
      "generation": "central-receipt",
      "receipt_id_available": true,
      "examined_through_available": false,
      "examined_through_marked_unavailable": true,
      "inferred_examined_through": false
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-004",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-004",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-04",
    "case": "malformed-ledger",
    "files": [
      "receipts/malformed_ledger.md"
    ],
    "expect": {
      "limitation": "malformed-ledger",
      "presented_as_complete": false,
      "fabricated_value": false,
      "conflicting_value_chosen": false
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-004",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-004",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-05",
    "case": "unreadable-file",
    "files": [],
    "construction": "At test time, copy receipts/marker_carrying_ledger_entry.md to the ledger path of a loop that declares the receipt-ledger surface, then remove read permission from the copy.",
    "expect": {
      "limitation": "unreadable-file",
      "receipts_emitted": 0,
      "presented_as_complete": false
    },
    "binds": [
      "DEL-02-03/REQ-004",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-004",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-004",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-06",
    "case": "undeclared-loop",
    "files": [],
    "construction": "At test time, copy receipts/marker_carrying_ledger_entry.md to the ledger path of a loop that has no registry declaration at all.",
    "expect": {
      "no_declaration_reported": true,
      "receipts_emitted": 0,
      "declaration_inferred_from_files": false
    },
    "binds": [
      "DEL-02-03/REQ-014",
      "DEL-02-03/REQ-017",
      "DEL-02-03/AC-015",
      "DEL-02-03/AC-018",
      "DEL-02-03/VER-014",
      "DEL-02-03/VER-017"
    ]
  },
  {
    "id": "SYN-RCP-07",
    "case": "receipt-folder-diverges-from-cursor",
    "files": [
      "receipts/receipt_folder_diverges_from_cursor.md"
    ],
    "expect": {
      "cursor_receipt_id": "syn-run-rcp-cursor-0701",
      "placement_folder": "syn-run-rcp-folder-0702",
      "receipt_id_source": "cursor-field",
      "folder_derived_identity": false,
      "nonconformance": false
    },
    "binds": [
      "DEL-02-03/REQ-016",
      "DEL-02-03/AC-017",
      "DEL-02-03/VER-016"
    ]
  },
  {
    "id": "SYN-RCP-08",
    "case": "prose-in-every-position",
    "files": [
      "receipts/prose_in_every_position_ledger.md",
      "receipts/prose_in_every_position_central.md"
    ],
    "expect": {
      "prose_marker": "zebra-prose",
      "prose_in_output": false,
      "prose_capable_field_types": 0,
      "prose_value_presence_only": true
    },
    "binds": [
      "DEL-02-03/REQ-007",
      "DEL-02-03/AC-007",
      "DEL-02-03/VER-007"
    ]
  }
]
}
```

### Fixture files (verbatim)

All paths are relative to `fixtures/synthetic/`. The Git blob id is given for each file.

**work_graph/missing_run_identity.md** (`049286e679476f78d0a0379cb79a36d7de26a75f`)
```
# Work graph -- ZEBRA-PROSE-WG01-TITLE kettle without a declared identity

ZEBRA-PROSE-WG01-INTRO This invented graph has no stable run identity bullet on
purpose; every word of prose here is fixture filler.

## Intent and selected route

- Intended result and completion conditions: ZEBRA-PROSE-WG01-RESULT a purple
kettle learns to whistle in three keys.
- Steering basis: ZEBRA-PROSE-WG01-STEERING the decoy word SYN-RUN-DECOY-0101
sits in this prose and is not an identity field.
- Priorities and approach: ZEBRA-PROSE-WG01-PRIORITIES tune the lowest key first.
- Included / left for later: ZEBRA-PROSE-WG01-SCOPE the fourth key waits.
- Route through the project DAG: ZEBRA-PROSE-WG01-ROUTE no prerequisite applies.
- Open questions: ZEBRA-PROSE-WG01-QUESTIONS none worth asking.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes or resolves | Work nodes |
|---|---|---|---|
| DEL-99-01 synthetic kettle slice | ZEBRA-PROSE-WG01-EXISTS a silent kettle | ZEBRA-PROSE-WG01-CHANGES a whistling kettle | W1, V1, P1 |

ZEBRA-PROSE-WG01-AFTER-SCOPE Invented filler between two tables.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG01-W1 tune the kettle | DEL-99-01; ZEBRA-PROSE-WG01-W1-SCOPE spout only | ZEBRA-PROSE-WG01-W1-NEEDS nothing earlier | ZEBRA-PROSE-WG01-W1-CHECK the kettle hums | COMPLETE; ZEBRA-PROSE-WG01-W1-RESULT it hummed |
| V1 ZEBRA-PROSE-WG01-V1 listen to the kettle | DEL-99-01; ZEBRA-PROSE-WG01-V1-SCOPE one ear | ZEBRA-PROSE-WG01-V1-NEEDS W1 hummed | ZEBRA-PROSE-WG01-V1-CHECK a second ear agrees | ACTIVE; ZEBRA-PROSE-WG01-V1-RESULT listening |
| P1 ZEBRA-PROSE-WG01-P1 publish the tune | DEL-99-01; ZEBRA-PROSE-WG01-P1-SCOPE sheet music | ZEBRA-PROSE-WG01-P1-NEEDS V1 agrees | ZEBRA-PROSE-WG01-P1-CHECK PR #9001 merged | PLANNED |

ZEBRA-PROSE-WG01-AFTER-WORK Invented filler after the node table.

## Current state and recovery

- Checked basis: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`.
- Next work: ZEBRA-PROSE-WG01-NEXT V1 keeps listening.
- Graph maintainer: ZEBRA-PROSE-WG01-MAINTAINER an invented orchestra.
```

**work_graph/duplicated_run_identity.md** (`d84b63eeed42304dd90c09b0d7653422690ecf68`)
```
# Work graph -- ZEBRA-PROSE-WG02-TITLE kettle with two declared identities

ZEBRA-PROSE-WG02-INTRO This invented graph declares its stable run identity
twice, with different values, on purpose.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0201`.
- Intended result and completion conditions: ZEBRA-PROSE-WG02-RESULT a teal
kettle whistles in two keys.
- Stable run identity: `SYN-RUN-WG-0202`.
- Steering basis: ZEBRA-PROSE-WG02-STEERING invented direction only.
- Open questions: ZEBRA-PROSE-WG02-QUESTIONS which identity is real, if any.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes or resolves | Work nodes |
|---|---|---|---|
| DEL-99-02 synthetic teal slice | ZEBRA-PROSE-WG02-EXISTS a quiet kettle | ZEBRA-PROSE-WG02-CHANGES two whistles | W1, P1 |

ZEBRA-PROSE-WG02-AFTER-SCOPE Invented filler between two tables.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG02-W1 carve a second spout | DEL-99-02; ZEBRA-PROSE-WG02-W1-SCOPE spout two | ZEBRA-PROSE-WG02-W1-NEEDS nothing earlier | ZEBRA-PROSE-WG02-W1-CHECK both spouts whistle | READY; ZEBRA-PROSE-WG02-W1-RESULT tools laid out |
| P1 ZEBRA-PROSE-WG02-P1 publish both tunes | DEL-99-02; ZEBRA-PROSE-WG02-P1-SCOPE two sheets | ZEBRA-PROSE-WG02-P1-NEEDS W1 whistles | ZEBRA-PROSE-WG02-P1-CHECK PR #9002 merged | PLANNED |

ZEBRA-PROSE-WG02-AFTER-WORK Invented filler after the node table.

## Current state and recovery

- Checked basis: `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`.
- Next work: ZEBRA-PROSE-WG02-NEXT start W1.
```

**work_graph/unrecognized_state_token.md** (`56be61a180a823a861e31a1559eb4fe2b005ccd7`)
```
# Work graph -- ZEBRA-PROSE-WG03-TITLE every state and one stranger

ZEBRA-PROSE-WG03-INTRO Six invented nodes each declare one vocabulary state and
a seventh declares a state word the vocabulary does not hold.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0301`.
- Intended result and completion conditions: ZEBRA-PROSE-WG03-RESULT an
invented choir sings seven notes.
- Open questions: ZEBRA-PROSE-WG03-QUESTIONS none.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG03-W1 first note | DEL-99-03; ZEBRA-PROSE-WG03-W1-SCOPE | ZEBRA-PROSE-WG03-W1-NEEDS | ZEBRA-PROSE-WG03-W1-CHECK | PLANNED |
| W2 ZEBRA-PROSE-WG03-W2 second note | DEL-99-03; ZEBRA-PROSE-WG03-W2-SCOPE | ZEBRA-PROSE-WG03-W2-NEEDS | ZEBRA-PROSE-WG03-W2-CHECK | READY; ZEBRA-PROSE-WG03-W2-RESULT tuned |
| W3 ZEBRA-PROSE-WG03-W3 third note | DEL-99-03; ZEBRA-PROSE-WG03-W3-SCOPE | ZEBRA-PROSE-WG03-W3-NEEDS | ZEBRA-PROSE-WG03-W3-CHECK | ACTIVE; ZEBRA-PROSE-WG03-W3-RESULT singing |
| W4 ZEBRA-PROSE-WG03-W4 fourth note | DEL-99-03; ZEBRA-PROSE-WG03-W4-SCOPE | ZEBRA-PROSE-WG03-W4-NEEDS | ZEBRA-PROSE-WG03-W4-CHECK | BLOCKED; awaiting invented decision D-SYN-9003 |
| W5 ZEBRA-PROSE-WG03-W5 fifth note | DEL-99-03; ZEBRA-PROSE-WG03-W5-SCOPE | ZEBRA-PROSE-WG03-W5-NEEDS | ZEBRA-PROSE-WG03-W5-CHECK | UNCERTAIN; ZEBRA-PROSE-WG03-W5-RESULT pitch unclear |
| W6 ZEBRA-PROSE-WG03-W6 sixth note | DEL-99-03; ZEBRA-PROSE-WG03-W6-SCOPE | ZEBRA-PROSE-WG03-W6-NEEDS | ZEBRA-PROSE-WG03-W6-CHECK | COMPLETE; ZEBRA-PROSE-WG03-W6-RESULT sung |
| W7 ZEBRA-PROSE-WG03-W7 seventh note | DEL-99-03; ZEBRA-PROSE-WG03-W7-SCOPE | ZEBRA-PROSE-WG03-W7-NEEDS | ZEBRA-PROSE-WG03-W7-CHECK | MARINATING; ZEBRA-PROSE-WG03-W7-RESULT not a vocabulary word |

ZEBRA-PROSE-WG03-AFTER-WORK Invented filler after the node table.

## Current state and recovery

- Checked basis: `cccccccccccccccccccccccccccccccccccccccc`.
- Next work: ZEBRA-PROSE-WG03-NEXT decide D-SYN-9003.
```

**work_graph/no_node_table.md** (`0986608e6ab00dfbb5e9b03f114bf25aead30863`)
```
# Work graph -- ZEBRA-PROSE-WG04-TITLE graph without any node table

ZEBRA-PROSE-WG04-INTRO This invented graph declares an identity but holds no
node table anywhere; its work is described only in prose.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0401`.
- Intended result and completion conditions: ZEBRA-PROSE-WG04-RESULT an
invented lighthouse blinks twice.
- Open questions: ZEBRA-PROSE-WG04-QUESTIONS none.

## Work

ZEBRA-PROSE-WG04-WORK The lighthouse keeper intends to polish the lens, then
wind the clockwork, then watch one night; none of this is written as a table.

## Current state and recovery

- Checked basis: `dddddddddddddddddddddddddddddddddddddddd`.
- Next work: ZEBRA-PROSE-WG04-NEXT polish the lens.
```

**work_graph/unresolved_pr_number.md** (`2002d4477afe12823f08f58975382352e993cc57`)
```
# Work graph -- ZEBRA-PROSE-WG05-TITLE graph citing a PR that never merged

ZEBRA-PROSE-WG05-INTRO This invented graph cites one PR number that no fixture
repository contains, in two citation syntaxes.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0501`.
- Intended result and completion conditions: ZEBRA-PROSE-WG05-RESULT an
invented bridge gains a railing.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG05-W1 bolt the railing | DEL-99-05; ZEBRA-PROSE-WG05-W1-SCOPE | ZEBRA-PROSE-WG05-W1-NEEDS | ZEBRA-PROSE-WG05-W1-CHECK | COMPLETE; railing change in #99999999 |
| P1 ZEBRA-PROSE-WG05-P1 integrate the railing | DEL-99-05; ZEBRA-PROSE-WG05-P1-SCOPE | ZEBRA-PROSE-WG05-P1-NEEDS W1 | ZEBRA-PROSE-WG05-P1-CHECK PR #99999999 merged | ACTIVE; awaiting PR #99999999 |

ZEBRA-PROSE-WG05-AFTER-WORK Invented filler after the node table.

## Current state and recovery

- Checked basis: `eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`.
- Next work: ZEBRA-PROSE-WG05-NEXT look for #99999999 locally.
```

**work_graph/two_graphs_bind_one_deliverable_a.md** (`37aba2b7dc878e29583a822ac58980ccad4fc7be`)
```
# Work graph -- ZEBRA-PROSE-WG06A-TITLE first graph binding DEL-99-01

ZEBRA-PROSE-WG06A-INTRO One of two invented graphs whose nodes bind the same
deliverable identifier.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0601`.
- Intended result and completion conditions: ZEBRA-PROSE-WG06A-RESULT paint
the invented kettle red.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG06A-W1 paint red | DEL-99-01; ZEBRA-PROSE-WG06A-W1-SCOPE lid only | ZEBRA-PROSE-WG06A-W1-NEEDS | ZEBRA-PROSE-WG06A-W1-CHECK lid is red | ACTIVE; ZEBRA-PROSE-WG06A-W1-RESULT first coat |
| P1 ZEBRA-PROSE-WG06A-P1 integrate red | DEL-99-01; ZEBRA-PROSE-WG06A-P1-SCOPE | ZEBRA-PROSE-WG06A-P1-NEEDS W1 | ZEBRA-PROSE-WG06A-P1-CHECK PR #9061 merged | PLANNED |
```

**work_graph/two_graphs_bind_one_deliverable_b.md** (`65264dd471f7454063108de998ce779fc8598af3`)
```
# Work graph -- ZEBRA-PROSE-WG06B-TITLE second graph binding DEL-99-01

ZEBRA-PROSE-WG06B-INTRO The other of two invented graphs whose nodes bind the
same deliverable identifier.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0602`.
- Intended result and completion conditions: ZEBRA-PROSE-WG06B-RESULT paint
the invented kettle blue.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG06B-W1 paint blue | DEL-99-01; ZEBRA-PROSE-WG06B-W1-SCOPE lid only | ZEBRA-PROSE-WG06B-W1-NEEDS | ZEBRA-PROSE-WG06B-W1-CHECK lid is blue | ACTIVE; ZEBRA-PROSE-WG06B-W1-RESULT primer on |
| P1 ZEBRA-PROSE-WG06B-P1 integrate blue | DEL-99-01; ZEBRA-PROSE-WG06B-P1-SCOPE | ZEBRA-PROSE-WG06B-P1-NEEDS W1 | ZEBRA-PROSE-WG06B-P1-CHECK PR #9062 merged | PLANNED |
```

**work_graph/prose_in_every_position.md** (`a5d82d07580acba778de7735cfe54079eb7cd6a1`)
```
# Work graph -- ZEBRA-PROSE-WG07-TITLE an orchard of invented sentences

ZEBRA-PROSE-WG07-INTRO Every prose-bearing position of this invented graph
carries a marker word beginning ZEBRA-PROSE so that tests can show none of it
reaches parser output.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0701`.
- Intended result and completion conditions: ZEBRA-PROSE-WG07-INTENT the
orchard grows plums that hum at dusk.
- Steering basis: ZEBRA-PROSE-WG07-STEERING an invented gardener asked for it.
- Priorities and approach: ZEBRA-PROSE-WG07-PRIORITIES water before pruning.
- Included / left for later: ZEBRA-PROSE-WG07-INCLUDED pears wait a season.
- Route through the project DAG: ZEBRA-PROSE-WG07-ROUTE the well comes first.
- Open questions: ZEBRA-PROSE-WG07-QUESTIONS do plums prefer lullabies.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes or resolves | Work nodes |
|---|---|---|---|
| DEL-99-07 ZEBRA-PROSE-WG07-BASIS humming orchard | ZEBRA-PROSE-WG07-EXISTS silent trees | ZEBRA-PROSE-WG07-CHANGES trees that hum | W1, V1, P1, C1, M1 and F1 |

ZEBRA-PROSE-WG07-AFTER-SCOPE Invented filler between two tables.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG07-OUTCOME-W1 teach the plums | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-W1 branches only | ZEBRA-PROSE-WG07-NEEDS-W1 a quiet evening | ZEBRA-PROSE-WG07-CHECK-W1 one plum hums | COMPLETE; ZEBRA-PROSE-WG07-RESULT-W1 a plum hummed in `aaaaaaa` |
| V1 ZEBRA-PROSE-WG07-OUTCOME-V1 listen at dusk | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-V1 two listeners | ZEBRA-PROSE-WG07-NEEDS-V1 W1 hummed | ZEBRA-PROSE-WG07-CHECK-V1 both listeners agree | COMPLETE; ZEBRA-PROSE-WG07-RESULT-V1 they agreed |
| P1 ZEBRA-PROSE-WG07-OUTCOME-P1 integrate the hum | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-P1 orchard notes | ZEBRA-PROSE-WG07-NEEDS-P1 V1 agreed | ZEBRA-PROSE-WG07-CHECK-P1 PR #9071 merged | COMPLETE; ZEBRA-PROSE-WG07-RESULT-P1 merged |
| C1 ZEBRA-PROSE-WG07-OUTCOME-C1 tidy the shed | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-C1 shed shelves | ZEBRA-PROSE-WG07-NEEDS-C1 P1 merged | ZEBRA-PROSE-WG07-CHECK-C1 shelves labelled | ACTIVE; ZEBRA-PROSE-WG07-RESULT-C1 half the shelves |
| M1 ZEBRA-PROSE-WG07-OUTCOME-M1 note the season | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-M1 one index row | ZEBRA-PROSE-WG07-NEEDS-M1 C1 tidy | ZEBRA-PROSE-WG07-CHECK-M1 row written | READY; ZEBRA-PROSE-WG07-RESULT-M1 pen uncapped |
| F1 ZEBRA-PROSE-WG07-OUTCOME-F1 close the gate | DEL-99-07; ZEBRA-PROSE-WG07-SCOPE-F1 the whole orchard | ZEBRA-PROSE-WG07-NEEDS-F1 M1 written | ZEBRA-PROSE-WG07-CHECK-F1 PR #9072 merged | PLANNED; ZEBRA-PROSE-WG07-RESULT-F1 gate still open |

ZEBRA-PROSE-WG07-WORK-NOTE The gardener hums while pruning, which is invented.

## Current state and recovery

- Checked basis: ZEBRA-PROSE-WG07-BASIS-BULLET the invented tip
`ffffffffffffffffffffffffffffffffffffffff`.
- Next work: ZEBRA-PROSE-WG07-NEXT finish the shelves.
- Local/unmerged work: ZEBRA-PROSE-WG07-LOCAL a basket of labels.
- Active operations and ownership: ZEBRA-PROSE-WG07-OPERATIONS the kettle boils.
- Graph maintainer: ZEBRA-PROSE-WG07-MAINTAINER an invented gardener.
- Open deferrals and follow-ups: ZEBRA-PROSE-WG07-DEFERRALS pears next spring.
- Current graph ref: ZEBRA-PROSE-WG07-REF the orchard branch of fancy.

| Completed work / node | What changed and was checked | Unresolved consequence |
|---|---|---|
| W1 | ZEBRA-PROSE-WG07-CHANGED-W1 a plum hums | ZEBRA-PROSE-WG07-CONSEQUENCE-W1 teach the rest |
| P1 | ZEBRA-PROSE-WG07-CHANGED-P1 merged notes | ZEBRA-PROSE-WG07-CONSEQUENCE-P1 tidy the shed |

ZEBRA-PROSE-WG07-CLOSING The orchard hums on, and nothing here is real.
```

**work_graph/links_and_bindings.md** (`f3b7ebb7fbadaccb13806ce1ef8eac0cf55c7640`)
```
# Work graph -- ZEBRA-PROSE-WG08-TITLE bindings, links and external pages

ZEBRA-PROSE-WG08-INTRO Invented nodes carry deliverable identifiers, relative
links with link text, and external URLs that must never be followed.

## Intent and selected route

- Stable run identity: `SYN-RUN-WG-0801`.
- Intended result and completion conditions: ZEBRA-PROSE-WG08-RESULT two
invented slices gain signposts.

## Deliverable scope

| Deliverable / basis | What exists | What this undertaking changes or resolves | Work nodes |
|---|---|---|---|
| DEL-99-04 ZEBRA-PROSE-WG08-ALPHA signpost slice | ZEBRA-PROSE-WG08-ALPHA-EXISTS | ZEBRA-PROSE-WG08-ALPHA-CHANGES | W1, P1 |
| DEL-99-05 ZEBRA-PROSE-WG08-BETA signpost slice | ZEBRA-PROSE-WG08-BETA-EXISTS | ZEBRA-PROSE-WG08-BETA-CHANGES | V1, P1 |

ZEBRA-PROSE-WG08-AFTER-SCOPE Invented filler between two tables.

## Work

| ID / outcome | Deliverables and work scope | Needs / why | Completion check | State / result |
|---|---|---|---|---|
| W1 ZEBRA-PROSE-WG08-W1 plant the alpha sign | DEL-99-04; scope in [ZEBRA-LINKTEXT-WG08-ALPHA-SCOPE](../../../PKG-99_Synthetic_Parsers/1_Working/DEL-99-04_Synthetic_alpha/ScopeOfWork.md) | ZEBRA-PROSE-WG08-W1-NEEDS | ZEBRA-PROSE-WG08-W1-CHECK see <https://example.invalid/zebra-autolink> | COMPLETE; ZEBRA-PROSE-WG08-W1-RESULT planted |
| V1 ZEBRA-PROSE-WG08-V1 plant the beta sign | DEL-99-05; evidence in [ZEBRA-LINKTEXT-WG08-BETA-EVIDENCE](./../SYN-RUN-WG-0801-evidence/SYN_EVIDENCE.md) | ZEBRA-PROSE-WG08-V1-NEEDS | ZEBRA-PROSE-WG08-V1-CHECK compare [ZEBRA-LINKTEXT-WG08-EXTERNAL](https://example.invalid/zebra/external-page) | ACTIVE; ZEBRA-PROSE-WG08-V1-RESULT half planted |
| P1 ZEBRA-PROSE-WG08-P1 integrate both signs | DEL-99-04, DEL-99-05; ZEBRA-PROSE-WG08-P1-SCOPE | ZEBRA-PROSE-WG08-P1-NEEDS W1 and V1 | ZEBRA-PROSE-WG08-P1-CHECK PR #9081 merged | PLANNED |

ZEBRA-PROSE-WG08-AFTER-WORK Invented filler after the node table.

## Current state and recovery

- Checked basis: `abababababababababababababababababababab`.
- Next work: ZEBRA-PROSE-WG08-NEXT finish V1.
```

**memory/template_table_form.md** (`a4f0fd79f3c451478acb3f3dad58b4c74f55c6e4`)
```
# MEMORY - DEL-99-11

> ZEBRA-PROSE-MEM01-NOTE Invented deliverable-local run index for a parser
> fixture; no real deliverable, run or decision is described here.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|
| `SYN-RUN-MEM-0101` / 2026-09-01 | ZEBRA-PROSE-MEM01-R1-WORK tuned the invented kettle | ZEBRA-PROSE-MEM01-R1-RESULT merged in [PR #9101](https://example.invalid/synthetic/pull/9101); [ZEBRA-LINKTEXT-MEM01-R1](../../../_Coordination/AgentRuns/SYN-RUN-MEM-0101/SYN_RECEIPT.md) |
| `SYN-RUN-MEM-0102` / 2026-09-02 | ZEBRA-PROSE-MEM01-R2-WORK painted the invented lid | ZEBRA-PROSE-MEM01-R2-RESULT merged in [PR #9102](https://example.invalid/synthetic/pull/9102) |
| `SYN-RUN-MEM-0103` / 2026-09-03 | ZEBRA-PROSE-MEM01-R3-WORK listened at dusk | ZEBRA-PROSE-MEM01-R3-RESULT graph at [ZEBRA-LINKTEXT-MEM01-R3](../../../_Coordination/WorkGraphs/SYN-RUN-MEM-0103/SYN_GRAPH.md) |
```

**memory/entry_without_readable_run_token.md** (`e8a7e528684c07cbb52776fe63ba9c6c2bec88b2`)
```
# MEMORY - DEL-99-12

> ZEBRA-PROSE-MEM02-NOTE Invented run index in the table form; two rows carry
> no readable run token in the declared token position.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|
| `SYN-RUN-MEM-0201` / 2026-09-04 | ZEBRA-PROSE-MEM02-R1-WORK a readable row | ZEBRA-PROSE-MEM02-R1-RESULT [PR #9201](https://example.invalid/synthetic/pull/9201) |
| 2026-09-05 | ZEBRA-PROSE-MEM02-R2-WORK cites invented decision D-SYN-9202 and the parenthesized word (ZEBRA_PAREN_0202) | ZEBRA-PROSE-MEM02-R2-RESULT [ZEBRA-LINKTEXT-MEM02-R2](../../../_Coordination/AgentRuns/SYN-RUN-DECOY-0203/SYN_EVIDENCE.md) |
| `ZEBRA PROSE WORDS` / 2026-09-06 | ZEBRA-PROSE-MEM02-R3-WORK a phrase sits where a token belongs | ZEBRA-PROSE-MEM02-R3-RESULT [PR #9203](https://example.invalid/synthetic/pull/9203) |
```

**memory/unreadable_date.md** (`f306bc93af94050d2ffe382f46159fbea2a11fe4`)
```
# MEMORY - DEL-99-13

> ZEBRA-PROSE-MEM03-NOTE Invented run index in the table form; two rows carry a
> date the declared date form cannot read.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|
| `SYN-RUN-MEM-0301` / 2026-09-07 | ZEBRA-PROSE-MEM03-R1-WORK a readable date | ZEBRA-PROSE-MEM03-R1-RESULT [PR #9301](https://example.invalid/synthetic/pull/9301) |
| `SYN-RUN-MEM-0302` / late-zebra-season | ZEBRA-PROSE-MEM03-R2-WORK a word instead of a date | ZEBRA-PROSE-MEM03-R2-RESULT [PR #9302](https://example.invalid/synthetic/pull/9302) |
| `SYN-RUN-MEM-0303` / 2026-09-XX | ZEBRA-PROSE-MEM03-R3-WORK a date with letters for its day | ZEBRA-PROSE-MEM03-R3-RESULT [PR #9303](https://example.invalid/synthetic/pull/9303) |
```

**memory/file_without_run_index_entry.md** (`a0c1121f0e54a828ab5037a0a188e02cb12d63a2`)
```
# MEMORY - DEL-99-14

> ZEBRA-PROSE-MEM04-NOTE Invented run index whose table has a header and no
> rows; the file holds no run-index entry at all.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|

## ZEBRA-PROSE-MEM04-SECTION background notes

ZEBRA-PROSE-MEM04-BODY The invented deliverable has not yet been worked on by
any run, and this undated section is not an index entry.
```

**memory/runs_section_mixed_with_dated_sections.md** (`445e4eb5a62896323585ddee0253b77593a33ae4`)
```
# MEMORY - DEL-99-16

> ZEBRA-PROSE-MEM06-NOTE Invented run index with a bullet-form Runs section
> followed by earlier dated sections kept from before the index existed.

## Runs

- 2026-09-10 -- `SYN-RUN-MEM-0601` -- ZEBRA-PROSE-MEM06-B1-BODY tuned the invented bell; [PR #9601](https://example.invalid/synthetic/pull/9601).
- 2026-09-11 -- `SYN-RUN-MEM-0602` -- ZEBRA-PROSE-MEM06-B2-BODY polished the invented bell; graph at [ZEBRA-LINKTEXT-MEM06-B2](../../../_Coordination/WorkGraphs/SYN-RUN-MEM-0602/SYN_GRAPH.md).

## 2026-08-20 -- ZEBRA-PROSE-MEM06-H1-HEADING an earlier dated record

ZEBRA-PROSE-MEM06-H1-BODY The bell was cast from invented bronze; see
[ZEBRA-LINKTEXT-MEM06-H1](../../../_Coordination/SYN_CASTING_NOTE.md).

## 2026-08-12 -- ZEBRA-PROSE-MEM06-H2-HEADING D-SYN-9601 (ZEBRA_PAREN_0603)

ZEBRA-PROSE-MEM06-H2-BODY The mould was drawn on invented paper in [PR #9602](https://example.invalid/synthetic/pull/9602).
```

**memory/prose_in_every_position_table.md** (`49636128eeead20e18581066d47dadc4e9d3969b`)
```
# MEMORY - DEL-99-17 ZEBRA-PROSE-MEM07T-TITLE

> ZEBRA-PROSE-MEM07T-NOTE Every prose-bearing position of this invented table
> index carries a marker word beginning ZEBRA-PROSE.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|
| `SYN-RUN-MEM-0711` / 2026-09-12 | ZEBRA-PROSE-MEM07T-R1-WORK the invented lantern was trimmed | ZEBRA-PROSE-MEM07T-R1-RESULT it glowed; [ZEBRA-PROSE-MEM07T-R1-LINKTEXT](../../../_Coordination/AgentRuns/SYN-RUN-MEM-0711/SYN_RECEIPT.md) |
| `SYN-RUN-MEM-0712` / 2026-09-13 | ZEBRA-PROSE-MEM07T-R2-WORK the invented wick was replaced | ZEBRA-PROSE-MEM07T-R2-RESULT it flickered in [ZEBRA-PROSE-MEM07T-R2-LINKTEXT](https://example.invalid/synthetic/pull/9712) |

## ZEBRA-PROSE-MEM07T-SECTION-HEADING lamplighter notes

ZEBRA-PROSE-MEM07T-SECTION-BODY The lamplighter keeps a second notebook that is
not part of the index.
```

**memory/prose_in_every_position_bullet.md** (`05066a0a6052fd7e7fc8d7781b40f49eb135afcd`)
```
# MEMORY - DEL-99-17 ZEBRA-PROSE-MEM07B-TITLE

> ZEBRA-PROSE-MEM07B-NOTE Every prose-bearing position of this invented bullet
> index carries a marker word beginning ZEBRA-PROSE.

## Runs

- 2026-09-14 -- `SYN-RUN-MEM-0721` -- ZEBRA-PROSE-MEM07B-B1-BODY the invented
lantern was carried uphill; [ZEBRA-PROSE-MEM07B-B1-LINKTEXT](../../../_Coordination/AgentRuns/SYN-RUN-MEM-0721/SYN_RECEIPT.md).
- 2026-09-15 -- `SYN-RUN-MEM-0722` -- ZEBRA-PROSE-MEM07B-B2-BODY the invented
lantern was carried down again; [ZEBRA-PROSE-MEM07B-B2-LINKTEXT](https://example.invalid/synthetic/pull/9722).

ZEBRA-PROSE-MEM07B-TRAILER A closing sentence under the bullets, still invented.
```

**memory/prose_in_every_position_heading.md** (`2f2f0176beb55ecbf6a9b7c9e2f0e51bb5f54739`)
```
# MEMORY - DEL-99-17 ZEBRA-PROSE-MEM07H-TITLE

> ZEBRA-PROSE-MEM07H-NOTE Every prose-bearing position of this invented
> dated-heading index carries a marker word beginning ZEBRA-PROSE.

## 2026-09-16 -- ZEBRA-PROSE-MEM07H-H1-HEADING the lantern festival

ZEBRA-PROSE-MEM07H-H1-BODY Invented townsfolk lit invented lanterns; see
[ZEBRA-PROSE-MEM07H-H1-LINKTEXT](../../../_Coordination/SYN_FESTIVAL_NOTE.md).

- ZEBRA-PROSE-MEM07H-H1-BULLET a bullet inside the section body.

## 2026-09-17 -- ZEBRA-PROSE-MEM07H-H2-HEADING D-SYN-9731 (ZEBRA_PAREN_0732)

ZEBRA-PROSE-MEM07H-H2-BODY The lanterns were counted twice, in
[ZEBRA-PROSE-MEM07H-H2-LINKTEXT](https://example.invalid/synthetic/pull/9732).
```

**memory/links_in_each_form_table.md** (`149ad0788fd7805a216831d8593179a2bea2389e`)
```
# MEMORY - DEL-99-18

> ZEBRA-PROSE-MEM08T-NOTE Invented table index carrying one relative link with
> link text, one PR link and one external URL.

## Runs

| Run ID / date | Work in this deliverable | Result and source links |
|---|---|---|
| `SYN-RUN-MEM-0811` / 2026-09-18 | ZEBRA-PROSE-MEM08T-R1-WORK a signpost was painted | [ZEBRA-LINKTEXT-MEM08T-RELATIVE](../../../_Coordination/AgentRuns/SYN-RUN-MEM-0811/SYN_RECEIPT.md); [PR #9811](https://example.invalid/synthetic/pull/9811); [ZEBRA-LINKTEXT-MEM08T-EXTERNAL](https://example.invalid/zebra/elsewhere) |
```

**memory/links_in_each_form_bullet.md** (`3caa1d0cf61f5b78ede5e0b5522293a84172f322`)
```
# MEMORY - DEL-99-18

> ZEBRA-PROSE-MEM08B-NOTE Invented bullet index carrying one relative link with
> link text, one PR link and one external URL.

## Runs

- 2026-09-19 -- `SYN-RUN-MEM-0821` -- ZEBRA-PROSE-MEM08B-B1-BODY a signpost was
planted; [ZEBRA-LINKTEXT-MEM08B-RELATIVE](../../../_Coordination/WorkGraphs/SYN-RUN-MEM-0821/SYN_GRAPH.md); [PR #9821](https://example.invalid/synthetic/pull/9821); [ZEBRA-LINKTEXT-MEM08B-EXTERNAL](https://example.invalid/zebra/elsewhere).
```

**memory/links_in_each_form_heading.md** (`f4461942ba1729333d0528c89b5f898fc6e5d51f`)
```
# MEMORY - DEL-99-18

> ZEBRA-PROSE-MEM08H-NOTE Invented dated-heading index carrying one relative
> link with link text, one PR link and one external URL.

## 2026-09-20 -- ZEBRA-PROSE-MEM08H-H1-HEADING the signpost survey

ZEBRA-PROSE-MEM08H-H1-BODY Invented surveyors counted signposts; see
[ZEBRA-LINKTEXT-MEM08H-RELATIVE](../../../_Coordination/SYN_SURVEY_NOTE.md),
[PR #9831](https://example.invalid/synthetic/pull/9831) and
[ZEBRA-LINKTEXT-MEM08H-EXTERNAL](https://example.invalid/zebra/elsewhere).
```

**receipts/marker_carrying_ledger_entry.md** (`697804d68e0994102a42e491dd9cb611c58f9957`)
```
# SYN Loop Receipts -- ZEBRA-PROSE-RCP01-TITLE invented ledger

> ZEBRA-PROSE-RCP01-HEADER Invented ledger for parser fixtures only; nothing
> here describes a real loop, decision, run or merge.

## Rules

1. ZEBRA-PROSE-RCP01-RULE-ONE pointers over narrative, in invented form.
2. ZEBRA-PROSE-RCP01-RULE-TWO entries after the marker comment carry cursor fields.

- **2026-08-01 -- Receipt 1** (ZEBRA-PROSE-RCP01-E1-TITLE first invented entry).
- Pointers: `projects/syn/execution/_Coordination/SYN_NOTE_0001.md`; PR #9901.
- Checks: ZEBRA-PROSE-RCP01-E1-CHECKS the kettle test passed.
- Gate outcome: ZEBRA-PROSE-RCP01-E1-GATE stopped after the first key.

- **2026-08-02 -- Receipt 2** (ZEBRA-PROSE-RCP01-E2-TITLE second invented entry).
- Pointers: PR #9902 at `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`.
- Gate outcome: ZEBRA-PROSE-RCP01-E2-GATE parked for an invented owner.
<!-- receipt-contract-v2 frozen-through=Receipt-2 prefix-bytes=890 prefix-sha256=936296a7d4b8fbe0b359b88e1e4540de5d0294a3e2c7d72749a540b8fd94525d -->

- **2026-08-03 -- Receipt 3** (ZEBRA-PROSE-RCP01-E3-TITLE first governed entry).
- Receipt-ID: `Receipt-3`
- Examined-Through: `cccccccccccccccccccccccccccccccccccccccc`
- Parent-Receipt: `Receipt-2`
- Pointers: PR #9903.
- Gate-Outcome: `SYN-EXECUTED`

- **2026-08-04 -- Receipt 4** (ZEBRA-PROSE-RCP01-E4-TITLE second governed entry).
- Receipt-ID: `Receipt-4`
- Examined-Through: `dddddddddddddddddddddddddddddddddddddddd`
- Parent-Receipt: `Receipt-3`
- Gate-Outcome: ZEBRA-PROSE-RCP01-E4-GATE the invented gate closed after a
  long sentence about kettles, which is prose and not a token.
```

**receipts/prose_structured_ledger_entry.md** (`a808494d04e0bf0ab8864b1a875d195531e336ae`)
```
# SYN Loop Receipts -- ZEBRA-PROSE-RCP02-TITLE invented prose ledger

> ZEBRA-PROSE-RCP02-HEADER Invented ledger with no receipt-contract marker; its
> entries are prose-structured and carry no validated cursor fields.

- **2026-08-21 -- Receipt 1** (ZEBRA-PROSE-RCP02-E1-TITLE first invented entry).
- Owner direction (2026-08-21, verbatim): "ZEBRA-PROSE-RCP02-E1-OWNER please
  teach the invented kettle a fourth key."
- Executed: ZEBRA-PROSE-RCP02-E1-EXECUTED the key was taught in PR #9911 at
  `aaaaaaa`.
- Examined through: ZEBRA-PROSE-RCP02-E1-EXAMINED an invented tip `bbbbbbb`,
  written as prose rather than as a cursor field.
- Checks: ZEBRA-PROSE-RCP02-E1-CHECKS the kettle hummed.
- Gate outcome: ZEBRA-PROSE-RCP02-E1-GATE executed, with reasons in prose.

- **2026-08-22 -- Receipt 2** (ZEBRA-PROSE-RCP02-E2-TITLE second invented entry).
- Follows Receipt 1. ZEBRA-PROSE-RCP02-E2-BODY the kettle rested; pointer
  `projects/syn/execution/_Coordination/SYN_NOTE_0002.md`.
- Gate outcome: ZEBRA-PROSE-RCP02-E2-GATE stopped because nothing was asked.
```

**receipts/receipt_without_examined_through.md** (`7432930198265ee91372c65ab7e23803d9081acf`)
```
# Loop receipt -- SYN-RUN-RCP-0301

> ZEBRA-PROSE-RCP03-NOTE Invented derivative run account for a parser fixture;
> its cursor section has no Examined-Through field.

## Result

ZEBRA-PROSE-RCP03-RESULT [PR #9921](https://example.invalid/synthetic/pull/9921)
merged an invented change as `eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`; this
commit sits in prose and is not a cursor value.

## Checks and limits

ZEBRA-PROSE-RCP03-CHECKS Invented checks passed on an invented head; nothing
real was reviewed.

## Cursor and pointers

- **Receipt-ID:** `SYN-RUN-RCP-0301`.
- **Parent-Receipt:** none.
- **Gate-Outcome:** ZEBRA-PROSE-RCP03-GATE the invented run finished quietly.
- **Work graph:** [ZEBRA-LINKTEXT-RCP03-GRAPH](../../WorkGraphs/SYN-RUN-RCP-0301/SYN_GRAPH.md).
```

**receipts/malformed_ledger.md** (`c7a0ddb16bad8c57d6562831ddc58b74baf759ce`)
```
# SYN Loop Receipts -- ZEBRA-PROSE-RCP04-TITLE invented malformed ledger

> ZEBRA-PROSE-RCP04-HEADER Invented ledger whose structure is broken on purpose:
> orphaned cursor bullets, an empty Receipt-ID, a doubled Examined-Through with
> conflicting values, an unclosed entry heading and a field without its colon.

<!-- receipt-contract-v2 frozen-through=Receipt-0 -->

- Receipt-ID: `Receipt-1`
- Examined-Through: `ffffffffffffffffffffffffffffffffffffffff`

- **2026-08-12 -- Receipt 2** (ZEBRA-PROSE-RCP04-E2-TITLE doubled field).
- Receipt-ID:
- Examined-Through: `abababababababababababababababababababab`
- Examined-Through: `cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd`
- Parent-Receipt: `Receipt-1`
- Gate-Outcome: `SYN-EXECUTED`

- **2026-08-13 -- Receipt 3 (ZEBRA-PROSE-RCP04-E3-TITLE unclosed heading
- Receipt-ID: `Receipt-3`
- Parent-Receipt `Receipt-2`
- Gate-Outcome: `SYN-EXECUTED`
```

**receipts/receipt_folder_diverges_from_cursor.md** (`dfe4b3bb441a7e3eb7d1d0ef7e36da151d94395b`)
```
# Loop receipt -- ZEBRA-PROSE-RCP07-TITLE invented folder-divergent receipt

> ZEBRA-PROSE-RCP07-NOTE Invented derivative run account whose cursor
> Receipt-ID differs from the AgentRuns folder it is placed in at test time.

## Result

ZEBRA-PROSE-RCP07-RESULT An invented bell was cast in
[PR #9971](https://example.invalid/synthetic/pull/9971).

## Checks and limits

ZEBRA-PROSE-RCP07-CHECKS Invented checks only.

## Cursor and pointers

- **Receipt-ID:** `SYN-RUN-RCP-CURSOR-0701`.
- **Examined-Through:** `abcdabcdabcdabcdabcdabcdabcdabcdabcdabcd`.
- **Parent-Receipt:** none.
- **Gate-Outcome:** `SYN-EXECUTED`.
```

**receipts/prose_in_every_position_ledger.md** (`64bece52d0ae196ed35ee7ea6ec9b27df223c6de`)
```
# SYN Loop Receipts -- ZEBRA-PROSE-RCP08L-TITLE invented prose-heavy ledger

> ZEBRA-PROSE-RCP08L-HEADER Every prose-bearing position of this invented
> ledger carries a marker word beginning ZEBRA-PROSE.

- **2026-08-30 -- Receipt 1** (ZEBRA-PROSE-RCP08L-E1-TITLE a frozen entry).
- ZEBRA-PROSE-RCP08L-E1-BODY An ungoverned narrative bullet about invented
  geese crossing an invented road.
<!-- receipt-contract-v2 frozen-through=Receipt-1 prefix-bytes=396 prefix-sha256=a979ba5b5fad74525717db4f8c4eb0ff982bcd679d34a08966f32f4a45bbdd5b -->

- **2026-08-31 -- Receipt 2** (ZEBRA-PROSE-RCP08L-E2-TITLE a governed entry).
- Receipt-ID: `Receipt-2`
- Examined-Through: `efefefefefefefefefefefefefefefefefefefef`
- Parent-Receipt: `Receipt-1`
- Owner direction (2026-08-31, verbatim): "ZEBRA-PROSE-RCP08L-E2-OWNER let
  the invented geese cross twice."
- Result: ZEBRA-PROSE-RCP08L-E2-RESULT the geese crossed and honked.
- Checks: ZEBRA-PROSE-RCP08L-E2-CHECKS an invented goose counter agreed.
- Limits: ZEBRA-PROSE-RCP08L-E2-LIMITS the far bank was not examined.
- Rationale: ZEBRA-PROSE-RCP08L-E2-RATIONALE geese prefer mornings.
- Gate-Outcome: ZEBRA-PROSE-RCP08L-E2-GATE the crossing is complete, the
  road is quiet, and the invented farmer is content.

ZEBRA-PROSE-RCP08L-E2-NARRATIVE A trailing narrative paragraph inside the
entry, describing invented weather in some detail.
```

**receipts/prose_in_every_position_central.md** (`10e239079a9a6a7959fd342a060141a6088dd198`)
```
# Loop receipt -- ZEBRA-PROSE-RCP08C-TITLE invented prose-heavy receipt

> ZEBRA-PROSE-RCP08C-NOTE Every prose-bearing position of this invented central
> receipt carries a marker word beginning ZEBRA-PROSE.

## Result

ZEBRA-PROSE-RCP08C-RESULT The invented geese were counted in
[PR #9981](https://example.invalid/synthetic/pull/9981); the count was odd.

## Checks and limits

ZEBRA-PROSE-RCP08C-CHECKS An invented reviewer recounted; ZEBRA-PROSE-RCP08C-LIMITS
the far bank stayed out of scope.

## Owner direction

"ZEBRA-PROSE-RCP08C-OWNER count the invented geese before breakfast."

## Cursor and pointers

- **Receipt-ID:** `SYN-RUN-RCP-0801`.
- **Examined-Through:** `fefefefefefefefefefefefefefefefefefefefe`.
- **Parent-Receipt:** none.
- **Gate-Outcome:** ZEBRA-PROSE-RCP08C-GATE the geese are counted and the
invented farmer sleeps.
- **Work graph:** [ZEBRA-PROSE-RCP08C-LINKTEXT](../../WorkGraphs/SYN-RUN-RCP-0801/SYN_GRAPH.md).
```

**Not claimed:** no parser exists and none was run. These fixtures and expectations have not been checked against any grammar declaration. No human ruling occurred or is recorded. The packet has not named these fixture paths (open point 11). Nothing was committed or placed in any worktree.

Files are in `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1syn.Wsbloe/`:
- `parsers/fixtures/synthetic/`: MANIFEST.json plus work_graph/, memory/ and receipts/
- `make_manifest.py`
- `broad_copy_check.py`