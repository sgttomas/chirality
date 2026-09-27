## X1 synthetic fixtures — revision report (manager rulings 1–3 applied)

The revision is done and the suite passes 10/10 against the updated test module. My wider copy check still finds no copied text. I stayed inside my mktemp dir with TMPDIR set there: no worktree writes, no branch operations, no network, no parser code.

The same content, with the full MANIFEST.json and changed files verbatim, also went by SendMessage to aaaf7c7927994c396.

**Where things are**
- Mktemp dir: `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1syn.Wsbloe`
- Fixtures: `parsers/fixtures/synthetic/` inside it.
- I re-copied the current test module into `parsers/`: blob `6ca941442df697e4bd88a2716171a761b43b12d4`.

### 1. Em dash (U+2014, UTF-8)
- I replaced 24 ` -- ` with ` — `.
  - Five memory files, in bullet openings and dated headings:
    - `links_in_each_form_bullet.md`
    - `links_in_each_form_heading.md`
    - `prose_in_every_position_bullet.md`
    - `prose_in_every_position_heading.md`
    - `runs_section_mixed_with_dated_sections.md`
  - All nine work_graph files, in the title only (`# Work graph — …`). Every other byte of those files is as in my first report.
- None of my files uses the node-ID suffix position, so nothing changed there.
- `receipts/*.md` are byte-unchanged, and both marker prefix-bytes/prefix-sha256 values still verify.
- Hygiene recheck over 28 files found 0 problems:
  - U+2014 is the only non-ASCII character, and receipts are pure ASCII.
  - LF line endings, no tabs, no trailing spaces, one final newline.
  - No "remaining" in any casing.

### 2. Case restored in the manifest
- `recognized_states`: PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN, COMPLETE
- `governed_fields`: Receipt-ID, Examined-Through, Parent-Receipt, Gate-Outcome
- `cursor_receipt_id`: SYN-RUN-RCP-CURSOR-0701
- `placement_folder`: SYN-RUN-RCP-FOLDER-0702
- `prose_marker`: ZEBRA-PROSE

### 3. Removed expectations (case | key | old value)
- SYN-WG-01 | nodes_emitted | 3
- SYN-WG-02 | declared_identity_bullets | 2
- SYN-WG-02 | nodes_emitted | 2
- SYN-WG-03 | recognized_state_nodes | 6
- SYN-WG-03 | unrecognized_state_nodes | 1
- SYN-WG-04 | run_identity_available | true (how the identity bullet is recognized is left open by DEL-02-08 TBD-002)
- SYN-WG-06 | graphs_parsed | 2
- SYN-WG-06 | graphs_binding_shared_deliverable | 2
- SYN-WG-08 | distinct_del_bindings | 2
- SYN-WG-08 | relative_links | 2
- SYN-WG-08 | external_urls | 2
- SYN-MEM-01 | entries 3, run_tokens_read 3, dates_read 3, run_id_unavailable_entries 0
- SYN-MEM-02 | entries 3, run_tokens_read 1, run_id_unavailable_entries 2, dates_read 3
- SYN-MEM-03 | entries 3, run_tokens_read 3, dates_read 1, dates_unavailable 2
- SYN-MEM-06 | runs_bullet_entries 2, dated_sections 2
- SYN-MEM-08 | relative_links_per_file 1, pr_links_per_file 1, external_urls_per_file 1
- SYN-RCP-01 | governed_entries 2, ungoverned_entries 2, prose_valued_fields 1
- SYN-RCP-02 | entries | 2
- SYN-RCP-03 | receipt_id_available | true (how cursor fields are recognized is left open by DEL-02-03 TBD-002)

These counts stay, because the case fixes them whatever grammar is chosen:
- SYN-WG-04 `nodes_emitted` 0 (the file has no table).
- SYN-MEM-04 and SYN-MEM-05 `entries` 0 (a header-only table, and no file).
- SYN-RCP-05 and SYN-RCP-06 `receipts_emitted` 0.
- SYN-WG-05 `cited_pr` 99999999 (the brief defines the case by this citation).

I added these single-token or boolean expectations; the contracts fix each one:
- SYN-WG-01 `decoy_token` SYN-RUN-DECOY-0101 (DEL-02-08 REQ-006).
- SYN-WG-03 `unrecognized_token` MARINATING (REQ-004).
- SYN-WG-06 `shared_deliverable` DEL-99-01 (REQ-017).
- SYN-WG-08 and SYN-MEM-08 `link_text_marker` ZEBRA-LINKTEXT.
- SYN-MEM-01 `inferred_run_id` false.
- SYN-MEM-02 `run_id_unavailable_marked` true and `decoy_tokens` [D-SYN-9202, ZEBRA_PAREN_0202, SYN-RUN-DECOY-0203] (DEL-02-09 REQ-004).
- SYN-MEM-03 `date_unavailable_marked` true (REQ-005).

The manager can drop these if preferred. Binds are unchanged.

### Final expect blocks, by case
The file on disk is standard `json.dumps(indent=2, ensure_ascii=True)`, blob `b191bd8d…`. The full JSON went verbatim in the SendMessage.
- WG-01: run_identity_available false, fabricated_identity false, limitation missing-run-identity, decoy_token SYN-RUN-DECOY-0101
- WG-02: run_identity_available false, fabricated_identity false, limitation duplicated-run-identity
- WG-03: recognized_states [the six, uppercase], limitation unrecognized-state, coerced_state false, unrecognized_token_carried false, unrecognized_token MARINATING
- WG-04: nodes_emitted 0, limitation no-node-table, presented_as_complete false
- WG-05: cited_pr 99999999, pr_resolution unresolved-locally, guessed_commit false, network_access false
- WG-06: bindings_emitted_per_graph true, overlap_verdict_emitted false, shared_deliverable DEL-99-01
- WG-07: prose_marker ZEBRA-PROSE, prose_in_output false, prose_capable_field_types 0
- WG-08: link_text_emitted false, external_url_followed false, external_url_emitted_as_path false, link_text_marker ZEBRA-LINKTEXT
- MEM-01: form table, inferred_run_id false
- MEM-02: form table, inferred_run_id false, run_id_unavailable_marked true, decoy_tokens [three tokens]
- MEM-03: form table, inferred_date false, date_unavailable_marked true
- MEM-04: entries 0, coverage_limit true, nonconformance false
- MEM-05: entries 0, coverage_limit true, nonconformance false
- MEM-06: every_entry_names_form true, silent_omission false, dated_heading_run_token_emitted false
- MEM-07: forms [table, bullet, dated-heading], prose_marker ZEBRA-PROSE, prose_in_output false, prose_capable_field_types 0
- MEM-08: forms [table, bullet, dated-heading], link_text_emitted false, external_url_followed false, external_url_emitted false, link_text_marker ZEBRA-LINKTEXT
- RCP-01: marker_present true, governed_fields [the four], prose_value_presence_only true, ungoverned_fields_unavailable true, fabricated_value false, fifth_contract_field false
- RCP-02: marker_present false, contract_fields_marked_unavailable true, inferred_field false, prose_in_output false
- RCP-03: generation central-receipt, examined_through_available false, examined_through_marked_unavailable true, inferred_examined_through false
- RCP-04: limitation malformed-ledger, presented_as_complete false, fabricated_value false, conflicting_value_chosen false
- RCP-05: limitation unreadable-file, receipts_emitted 0, presented_as_complete false
- RCP-06: no_declaration_reported true, receipts_emitted 0, declaration_inferred_from_files false
- RCP-07: cursor_receipt_id SYN-RUN-RCP-CURSOR-0701, placement_folder SYN-RUN-RCP-FOLDER-0702, receipt_id_source cursor-field, folder_derived_identity false, nonconformance false
- RCP-08: prose_marker ZEBRA-PROSE, prose_in_output false, prose_capable_field_types 0, prose_value_presence_only true

### Suite tail
Command: `run_fixture_suite.sh <worktree> 6c6cc1b00dd5cc2bf77a5a262d0ac593fc96e240 <mktemp>/parsers -v`, with `drafting_stub/pinned` in place. All 10 tests reported `... ok`:
- test_every_record_binds_a_requirement_criterion_and_verification
- test_git_access_is_read_only_and_allowlisted
- test_golden_source_values_are_grounded_in_their_pinned_blobs
- test_goldens_are_content_minimal_and_hold_no_source_text_run
- test_loaded_suite_has_exact_verification_mapping
- test_manifests_and_goldens_are_well_formed
- test_no_fixture_source_is_copied_into_the_tree
- test_pins_resolve_by_read_only_plumbing_on_integrated_history
- test_synthetic_cases_cover_the_contract_minimums
- test_tree_expectations_hold_at_their_pinned_commits

```
Ran 10 tests in 0.853s

OK
```

Broader copy check (feed-named blobs at d61981ee2 and 6c6cc1b, minus template runs): source blobs 300, runs 453266, files with overlap: 0.

### Git blob ids (git hash-object, no -w), fixtures/synthetic
```
b191bd8d5fc18e6507d793638adaf91b9f130100 MANIFEST.json
e8a7e528684c07cbb52776fe63ba9c6c2bec88b2 memory/entry_without_readable_run_token.md
a0c1121f0e54a828ab5037a0a188e02cb12d63a2 memory/file_without_run_index_entry.md
c4dac84889521c09ad4bc5fc4af19aeb3cb7d096 memory/links_in_each_form_bullet.md
a685e9a9e305e8db38e763bd86e9214a4e0489a3 memory/links_in_each_form_heading.md
149ad0788fd7805a216831d8593179a2bea2389e memory/links_in_each_form_table.md
3b8848bca4a91372c6fd96fcbbc448e76a1f96f5 memory/prose_in_every_position_bullet.md
5730d1012a8535942ab953e0923310f56fa1a655 memory/prose_in_every_position_heading.md
49636128eeead20e18581066d47dadc4e9d3969b memory/prose_in_every_position_table.md
5525ad8015d44e0df2eeb4858929d537cf34a2ed memory/runs_section_mixed_with_dated_sections.md
a4f0fd79f3c451478acb3f3dad58b4c74f55c6e4 memory/template_table_form.md
f306bc93af94050d2ffe382f46159fbea2a11fe4 memory/unreadable_date.md
c7a0ddb16bad8c57d6562831ddc58b74baf759ce receipts/malformed_ledger.md
697804d68e0994102a42e491dd9cb611c58f9957 receipts/marker_carrying_ledger_entry.md
10e239079a9a6a7959fd342a060141a6088dd198 receipts/prose_in_every_position_central.md
64bece52d0ae196ed35ee7ea6ec9b27df223c6de receipts/prose_in_every_position_ledger.md
a808494d04e0bf0ab8864b1a875d195531e336ae receipts/prose_structured_ledger_entry.md
dfe4b3bb441a7e3eb7d1d0ef7e36da151d94395b receipts/receipt_folder_diverges_from_cursor.md
7432930198265ee91372c65ab7e23803d9081acf receipts/receipt_without_examined_through.md
e86eae263b889a9d7b777e17d107fd3bc9aecf26 work_graph/duplicated_run_identity.md
825636297e34222e431bb6ed3e4c2be28516a49a work_graph/links_and_bindings.md
129225138556fc9f482f7d7bc42850b1eab420d5 work_graph/missing_run_identity.md
5452a3bb5f5a9a25c253ac0741312ac991b9f485 work_graph/no_node_table.md
e4985d99886d7448757fe9a54e553e7db0746a7e work_graph/prose_in_every_position.md
e86fd99bb7a16d19718604a4cd0e5a1d00ed812e work_graph/two_graphs_bind_one_deliverable_a.md
1f68e76129d8724e76fc93b0d0a4395841a5d23d work_graph/two_graphs_bind_one_deliverable_b.md
f19f3601f746b4d49d0d507dd21e5840c4968fb0 work_graph/unrecognized_state_token.md
b69c4ba2582fe0d1cbee126dda854e1e00f54570 work_graph/unresolved_pr_number.md
```

### Worktree status
`pec-x1-fixtures-prep` now shows 7 status entries. None came from this session, which only read that worktree:
- modified: `candidates/.../test_parser_fixture_integrity.py`
- untracked: `apply_x1p.py`, `apply_x1p.template.py`, `build_apply_x1p.py`, `test_apply_x1p.py`, `candidates/projects/pec/software-workflow.json`, `candidates/.../parsers/fixtures/`

### Files the manager needs next
- Changed memory files: their full text is in the SendMessage.
- Work-graph files: only line 1 changed, from `# Work graph -- …` to `# Work graph — …`, with the rest of each title unchanged. The body text is in my first report.
