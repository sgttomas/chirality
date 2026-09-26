#!/usr/bin/env python3
"""gen_d99.py — bound generator for the PEC Remaining retirement act, D-PEC-99 (provisional number).

Stdlib only; prepared with CPython 3.13.7. Run from any directory:

  PYTHONDONTWRITEBYTECODE=1 python3 gen_d99.py --repo <REPO_ROOT> --act-date YYYY-MM-DD \
      --ruling-date YYYY-MM-DD [--decision D-PEC-NN] [--q1 s1|park|decline] \
      [--check-only] [--reproduction] [--render-to DIR]

Before any write it checks: the pinned census and decision account; every pinned preimage
(57 `_STATUS.md`, `projects/pec/AGENTS.md` at its post-SCA-006-checkpoint-3 bytes); that each
Remaining section is the file's last section and holds exactly the account's keys in order;
that every account row has a resolvable disposition; that the write set equals the grant; that
no `## Remaining` heading survives in any written `_STATUS.md`; and that the local date equals
--act-date (lifted only by --reproduction). It exits 1 with nothing written on any failure, and
exits 1 on a second run (preimages no longer match; new files already exist). --check-only
renders and checks without writing. --render-to writes the rendered postimages under DIR
instead of the repository.

Slots: --act-date {D}, --ruling-date {R}, --decision {N} (default D-PEC-99; the final number is
fixed at publication with its register row) and --q1 (the owner's answer to question 1 on
DEL-03-06-REM-004: s1 = carry-forward for S1, recommended and default; park = exhibit Part A,
unselected; decline = closed by the ruling). The exhibit folder name carries the fixed preparation
date 2026-09-26, not a slot. No other byte varies.
"""
import argparse, csv, datetime, hashlib, io, os, re, sys

# ---------------------------------------------------------------- pinned block
PINS = {'basis': {'projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/REMAINING_CENSUS.csv': 'b0e25361b4955b1a2689fa729b9727a2caa0efe8d3770cb0fd006af4ab445eb4',
           'projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/SEMANTIC_DECISION_ACCOUNT.csv': 'b240b38d940448a66b37752a1f2509ea4c6783f388c0a8d6cb0d3d21a465f7e2'},
 'status': {'projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_STATUS.md': '90412b8561835d76d697054cd30049760ff95a686dbc175c4e1fd216c6eb0d84',
            'projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_STATUS.md': '37d11e4937651bfb29108db79031b2b73902f40a06d0b928ccc5340941843eb3',
            'projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-02_Presence_tier_schema_entity_model/_STATUS.md': '8f0e880702d0fd09595d2f41cd70031645254847c604dae85633d7387f5f66db',
            'projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_STATUS.md': 'd9429b4e14f60343dbd9827a0e0a93c99359d8fb64b96c0a612cc7d5dd56555b',
            'projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/_STATUS.md': '9600471873fbef6cd0b82db765e68ab801f42ee5c52ab29e7a27e791e3531564',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/_STATUS.md': '9a14fb751451f9c062846ce0f1dd74fa9f09bb36181e466f4c6db3484d301e66',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/_STATUS.md': '513a003912f8fa98955ae3043330256f643835284686fa9cc152dd337d8ee066',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_STATUS.md': '001b4d3951e041ba36a3a56e6748d0f422fad36e1f70d0b4c2e41c781bbfdbfd',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_STATUS.md': '8ccba8f2854d6f190dda068bef04042ec1ec7382a8bd44970051c7fb3d334919',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_STATUS.md': '1f05a08832b222e229eb51ad3833d3fc5affdf52d32c84c0cc0ac75807c66af6',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_STATUS.md': '627993d6fae59c0276ba7bbe01c750797f4c3be4aa2c2c56a2f778efbeff22c4',
            'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_STATUS.md': '4cea9b1c000db8a9248356412960f33d13b271530eb80f38ebd28d98d7ec42bd',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/_STATUS.md': '46a49e2444c22c5c622943def0ed069345f6b0e8b639e54d6684b00abf1cf80d',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/_STATUS.md': 'ff69a831e9dcd2ea38f8aae10e8cbeae76467c0213eb714bdb427ab9a4874b07',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_STATUS.md': '3757edd7955f681a71713f64d30146522fb80bb363e8c68a468f1d4a0b669612',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-04_Practitioner_harness_parity_diff/_STATUS.md': 'e76d6d6f3c45dfb688955f8f63c43881e1df167f5f0fe085730c9a7e2ebcff1a',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_STATUS.md': '38f0190b841865e1841ef84e13bcda339c989fc1eb14aab46a218eedb49c85b5',
            'projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/_STATUS.md': '4bb6e2fa272830c99f92c53942496b0be81465c9579d6936975a1cdc7d66dea1',
            'projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_STATUS.md': 'c08a317519a7dea41fdc852b9a43dce38f3fb8b669fd1cc276431e87c97e1ca6',
            'projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/_STATUS.md': '25a5ab54d49a1aaf7a26ffbbf51812d1c14bd935856d2c35674f571ad9e443f1',
            'projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_STATUS.md': '6b8653f06c399b9eeef0b378b6ee899772150008f0eac4b1ad9b828ba57278bf',
            'projects/pec/execution/PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/_STATUS.md': 'b9b4160fe2870703aa84a61466da7259003cddc7b120d94a8dd04e810f91d826',
            'projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_STATUS.md': 'c2ff52d3f946fbcb7fdd8ea7eebb814ba13775b0c0538d35657229aa0b80a95b',
            'projects/pec/execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-02_Cross_loop_decision_slate/_STATUS.md': '97204fa6ec6e67b58ba70322e6f250e2c6597a019f2c33fea9c46f4abe1b8c52',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_STATUS.md': '62e7050ea75b36e340ea14618d031d9fb00b40dfdb76532406f1c26a012a6e53',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-02_Git_worktree_scanner/_STATUS.md': 'e352e6f4627487ed4e71370ec1005eac2c0bd29aeb513df587efee32ee79d906',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-03_Session_worktree_scope_correlation/_STATUS.md': 'd3862a7371289a677350fee7d5d910c431a4facada2b81780d07a6325a12505e',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_STATUS.md': 'eeae22fbd49a8f4105139480e45db6c9c1147d343cfa2b8a83bd8bad039724bc',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-05_TTL_heartbeat_discipline_citation_exclusion/_STATUS.md': 'cf41c05e567f13bf1d7fc772150d110507e1b3d9779f064216d4484991b7e31a',
            'projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-06_Advisory_overlap_detection/_STATUS.md': '31239d73ac547cc8d954bb7208a18038e09c60b2e43d24707706a56239f92c42',
            'projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-01_Idempotent_event_ingest_durable_message_store/_STATUS.md': '4c29577a180f11091cd2d494082881ee94efc25f6e27d0aea72ba4a4c8894317',
            'projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_STATUS.md': '8eda30e178b6164c3caa4a5afd97271e49cbec2f1232a0ffc4c4fe4ccbc93b8a',
            'projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_STATUS.md': 'd64fbe49770c82daa0d4524364bf12b7702ec3853187ec7465bbdc4753877332',
            'projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_STATUS.md': '2aaec8fd5ba027c5a7cc34d1a94a972ca8ddb2c7a1a59db52e53be8d12f2de5e',
            'projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_STATUS.md': '19123cf8a3ca8e19a60bac8849c9008d33a025e245dabffb4bd82f4cc8383ded',
            'projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_STATUS.md': 'db1e606dc164359b12649bc6d9e3fc91a22d952f989380ecfe4be1a0f04f2cf0',
            'projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_STATUS.md': '871866000a44ad7d3fb261079163f31315bb7da2b339b091b97900f0cd24eb53',
            'projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/_STATUS.md': 'cd5577e642d4f1ea9b3c578ba4781880fdcd263c4e38ed67ceac2c07e47685a5',
            'projects/pec/execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_STATUS.md': '954f7f6406f11037236d963567610826cff7b912de4158b7213e81dd7ff74d7e',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-01_Overview_dashboard/_STATUS.md': '3daebf75f6316004b283c4a319146298d514ce266b578cde78b61edbcf9e0b90',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-02_Lifecycle_census_dashboard/_STATUS.md': '3bfe3105ee545054ebc7fe5b55aee0752040be5487b08a2349d5cf78491f2533',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-03_Register_views/_STATUS.md': '8f4d0b179587cb89a9d68f55cea28edb1e8bdc7a1d0f6825ccef832728be4f6f',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-04_Decision_slate_view_waiting_on_you/_STATUS.md': 'd4e10dc94d4b3bf21e839639ca2db1a2df68e5582921f569c493305aba8360a1',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_STATUS.md': '930c3aca6ad9cd8e5ec332a9b3c1867b939e47ed78331f87eac7b2592b146f24',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-06_Universal_drill_down_to_cited_source/_STATUS.md': 'ae2c4efd9e27bb01a7d2657ac17848aeb429612cbd6098f4547e232076993054',
            'projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules/_STATUS.md': 'dd95c428edb7c9a56b5ab9946c20c136843a75972dc77c478c723ce274bc2629',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/_STATUS.md': 'e04aef7be9a67c1616d56757bdb7387c643b795fae1980178c9176fb04479415',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-03_No_ruling_write_verification/_STATUS.md': 'cfdf2a3e9a8736dddcab4c1367c8da5be8cf722c19769bc5dca8091c54f74d0b',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-04_Orientation_defect_rate_spot_check/_STATUS.md': 'c7a2e6c374271160c4b78de56386a8c7a0b7e6968b48f1f97f3bb2acc012259b',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-05_Owner_consultation_logging/_STATUS.md': 'c71ed9aa993819ba6de56f54833531900b169764f5984e7a1f0d86455f84c878',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-06_Seeded_conflict_overlap_test/_STATUS.md': '8fa911b4143585e0429298d6a384587306f0d5078b686f9f5f26182fee1b8757',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-07_Presence_TTL_honesty_tests/_STATUS.md': '766424853d9617e57e92f0083f9e4d957e1f9ce43f96afa537a3fa407b158b3d',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_STATUS.md': 'da1baf19f80fcf36bdf897c9b82ee82a7562f02858d794c802a806519095e0b2',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-09_Collision_incident_measurement/_STATUS.md': 'cd7e5e96f5f526f698a253b295f92cb63308081a041e8f3b421cf09a78c8a628',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/_STATUS.md': '802d6a9c0fd2c96fbeb86dc2ec04101f2758953dfa887f070e82cae005419a63',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/_STATUS.md': '1d22b5814c80ad9b786e1e21b9f58eab32e0f6b98a2d09a43f8197a73fc98f9f',
            'projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-12_Poll_adoption_measurement/_STATUS.md': 'a09c05334d22eb788fa8aacfbb066e69c2b547af20c982e6efc6166d49c0c9de'},
 'agents_pre': '4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c',
 'agents_replacements': [('amended: 2026-09-26 (SCA-006 operational-reliance instruction tranche; earlier, '
                          'shared development-loop adoption under D-PEC-94)',
                          'amended: {D} (Remaining retirement under {N}; earlier, SCA-006 '
                          'operational-reliance instruction tranche and shared development-loop adoption '
                          'under D-PEC-94)'),
                         ('PEC adds no new deliverable `_STATUS.md` `## Remaining` sections or entries\n'
                          '(owner direction of 2026-09-26, recorded as SCA-006 checkpoint group 2\n'
                          'amendment 1). No PEC feed profile reads them, so the coordination plane does\n'
                          'not scan them, and they are not a work-selection surface. Steering selects the\n'
                          'undertaking; record new open scope in its work graph and governing records.\n'
                          'Until any retirement ruling, the existing sections stay in place as\n'
                          'deliverable-local records of open scope under their owning decisions (for\n'
                          "example `D-PEC-83`). A Remaining item's own gate markers still bind that item.\n"
                          'Update an item only under the packet that opens that `_STATUS.md`. If an\n'
                          'undertaking completes or affects an item without such a grant, record the\n'
                          'consequence in the graph and bring it to the owner. Retiring the sections, as\n'
                          'App and Piping did, is a separate owner-directed undertaking.\n',
                          "PEC's deliverable `_STATUS.md` files carry lifecycle and history only. Their\n"
                          'former `## Remaining` sections were retired under `{N}` (owner\n'
                          'directions of 2026-09-26; the first is recorded as SCA-006 checkpoint group 2\n'
                          'amendment 1). The finite account is\n'
                          '`execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`.\n'
                          'Each item was closed on its cited record or moved verbatim, with its gate,\n'
                          'into the exhibit of `{N}`: the unselected `D-PEC-83` E evidence\n'
                          'inquiries stay there until steering selects one, and each Scope of Work\n'
                          'carry-forward is absorbed by the currency packet the exhibit names. A moved\n'
                          "item's gate markers still bind it at its destination. When selected work\n"
                          'completes or changes an exhibit item, record that in the selecting graph and\n'
                          'its central receipt; the exhibit is not edited. Add no `## Remaining` section\n'
                          'or entry. No PEC feed profile reads such sections, so the coordination plane\n'
                          'does not scan them, and they are not a work-selection surface. Steering\n'
                          'selects the undertaking; record new open scope in its work graph and\n'
                          'governing records.\n')],
 'exhibit_path': 'projects/pec/execution/_Coordination/_DECISIONS/{N}_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md',
 'new_files': {'docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-{DC}.yaml': 'schema: '
                                                                                               'instruction-tranche-manifest/v1\n'
                                                                                               'tranche_id: '
                                                                                               'PEC-REMAINING-RETIREMENT-{DC}\n'
                                                                                               'title: PEC '
                                                                                               'retires its '
                                                                                               'deliverable '
                                                                                               'Remaining '
                                                                                               'sections '
                                                                                               'after a '
                                                                                               'finite '
                                                                                               'governed '
                                                                                               'transfer\n'
                                                                                               'date: {D}\n'
                                                                                               'instruction_surface_paths:\n'
                                                                                               '  - '
                                                                                               'projects/pec/AGENTS.md\n'
                                                                                               '  - '
                                                                                               'execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md\n'
                                                                                               '  - '
                                                                                               'projects/chirality-runtime/execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md\n'
                                                                                               '  - '
                                                                                               'docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-{DC}.yaml\n'
                                                                                               'm2_gate:\n'
                                                                                               '  '
                                                                                               'authorization: '
                                                                                               '>-\n'
                                                                                               '    Ryan '
                                                                                               'Tufts, '
                                                                                               '2026-09-26: '
                                                                                               '"Why am I '
                                                                                               'seeing '
                                                                                               '`remaining-items` '
                                                                                               'appearing?\n'
                                                                                               '    There '
                                                                                               'must not be '
                                                                                               'any of those '
                                                                                               'going '
                                                                                               'forward, so '
                                                                                               'no need to '
                                                                                               'scan for\n'
                                                                                               '    them." '
                                                                                               'and, '
                                                                                               'answering '
                                                                                               "HELP_HUMAN's "
                                                                                               'question '
                                                                                               'whether to '
                                                                                               'open a '
                                                                                               'retirement\n'
                                                                                               '    '
                                                                                               'undertaking '
                                                                                               'as App and '
                                                                                               'Piping did, '
                                                                                               '"open RS1". '
                                                                                               'The '
                                                                                               "retirement's "
                                                                                               'exact\n'
                                                                                               '    edits, '
                                                                                               'including '
                                                                                               'this '
                                                                                               'instruction '
                                                                                               'change, are '
                                                                                               'ruled by the '
                                                                                               'owner in\n'
                                                                                               '    {N} (PEC '
                                                                                               'decision '
                                                                                               'register). '
                                                                                               'projects/pec/AGENTS.md '
                                                                                               'made '
                                                                                               'retiring '
                                                                                               'the\n'
                                                                                               '    sections '
                                                                                               'a separate '
                                                                                               'owner-directed '
                                                                                               'undertaking. '
                                                                                               'This '
                                                                                               'manifest '
                                                                                               'records\n'
                                                                                               '    those '
                                                                                               'acts and '
                                                                                               'grants '
                                                                                               'none.\n'
                                                                                               '  '
                                                                                               'authorized_by: '
                                                                                               'Ryan Tufts\n'
                                                                                               '  '
                                                                                               'authorization_date: '
                                                                                               '{R}\n'
                                                                                               '  '
                                                                                               'integration_owner: '
                                                                                               '>-\n'
                                                                                               '    PEC '
                                                                                               'WORKING_ITEMS '
                                                                                               'manager '
                                                                                               'under '
                                                                                               'HELP_HUMAN '
                                                                                               'undertaking\n'
                                                                                               '    '
                                                                                               'HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT; '
                                                                                               'roles '
                                                                                               'instruction-asserted,\n'
                                                                                               '    not '
                                                                                               'mechanically '
                                                                                               'enforced. '
                                                                                               'HELP_HUMAN '
                                                                                               'owns the '
                                                                                               'merge.\n'
                                                                                               '  '
                                                                                               'merge_gate: '
                                                                                               'owner-authorized-pr\n'
                                                                                               '  '
                                                                                               'self_merge: '
                                                                                               'true\n'
                                                                                               'm6_notice:\n'
                                                                                               '  '
                                                                                               'disposition: '
                                                                                               'routed\n'
                                                                                               '  '
                                                                                               'routed_to:\n'
                                                                                               '    - '
                                                                                               'execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md\n'
                                                                                               '    - '
                                                                                               'projects/chirality-runtime/execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md\n'
                                                                                               '  rationale: '
                                                                                               '>-\n'
                                                                                               '    Root: '
                                                                                               'its '
                                                                                               'alignment '
                                                                                               'manual\n'
                                                                                               '    '
                                                                                               '(docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.md\n'
                                                                                               '    line 60) '
                                                                                               'still '
                                                                                               'describes '
                                                                                               "PEC's "
                                                                                               'selection as '
                                                                                               '"Deliverable '
                                                                                               '`Remaining`".\n'
                                                                                               '    Runtime: '
                                                                                               'DEL-02-06 '
                                                                                               'pins '
                                                                                               'projects/pec/AGENTS.md '
                                                                                               '(SOURCE_PINS.json '
                                                                                               'S4). App\n'
                                                                                               '    and '
                                                                                               'Piping '
                                                                                               'receive '
                                                                                               'none: each '
                                                                                               'retired its '
                                                                                               'own sections '
                                                                                               'on '
                                                                                               '2026-09-23 '
                                                                                               'and\n'
                                                                                               '    neither '
                                                                                               'pins '
                                                                                               'projects/pec/AGENTS.md. '
                                                                                               'Each notice '
                                                                                               'is '
                                                                                               'non-binding '
                                                                                               'and asks\n'
                                                                                               '    for no '
                                                                                               'write.\n'
                                                                                               'checks:\n'
                                                                                               '  - python3 '
                                                                                               'tools/validation/validate_instruction_entrypoints.py '
                                                                                               '.\n'
                                                                                               '  - python3 '
                                                                                               'tools/validation/validate_instruction_tranche_manifest.py\n'
                                                                                               '  - python3 '
                                                                                               'tools/validation/validate_instruction_tranche_manifest.py '
                                                                                               '--base '
                                                                                               'origin/main '
                                                                                               '--head HEAD '
                                                                                               '--added-manifests-only\n'
                                                                                               '  - python3 '
                                                                                               'tools/validation/validate_pec_loop_receipts.py '
                                                                                               '--repo-root '
                                                                                               '.\n'
                                                                                               '  - python3 '
                                                                                               '-m pytest -q '
                                                                                               'tools/validation/test_validate_instruction_entrypoints.py '
                                                                                               'tools/validation/test_validate_pec_loop_receipts.py\n'
                                                                                               '  - '
                                                                                               'PYTHONDONTWRITEBYTECODE=1 '
                                                                                               'python3 '
                                                                                               'tools/practitioner_harness/harness.py '
                                                                                               'self-check\n'
                                                                                               'rollback: '
                                                                                               '>-\n'
                                                                                               '  Revert the '
                                                                                               'retirement '
                                                                                               "act's "
                                                                                               'commit. '
                                                                                               'projects/pec/AGENTS.md '
                                                                                               'returns to '
                                                                                               'its\n'
                                                                                               '  '
                                                                                               'post-SCA-006 '
                                                                                               'preimage; '
                                                                                               'the notices, '
                                                                                               'this '
                                                                                               'manifest and '
                                                                                               'the exhibit '
                                                                                               'are\n'
                                                                                               '  deleted; '
                                                                                               'every '
                                                                                               '_STATUS.md '
                                                                                               'regains its '
                                                                                               'Remaining '
                                                                                               'section byte '
                                                                                               'for byte '
                                                                                               'and\n'
                                                                                               '  every '
                                                                                               'other '
                                                                                               'touched file '
                                                                                               'returns to '
                                                                                               'its '
                                                                                               'preimage.\n'
                                                                                               'scope_limits:\n'
                                                                                               '  - PEC '
                                                                                               'fences '
                                                                                               'F-PEC-1..4, '
                                                                                               'the '
                                                                                               'owner-ruled '
                                                                                               'D-PEC packet '
                                                                                               'rule, '
                                                                                               'K-AUTH-1 and '
                                                                                               'the '
                                                                                               'reliance-hold '
                                                                                               'control are '
                                                                                               'unchanged.\n'
                                                                                               '  - '
                                                                                               'projects/pec/loop/LOOP_INIT.md '
                                                                                               'names no '
                                                                                               'Remaining '
                                                                                               'surface and '
                                                                                               'is '
                                                                                               'unchanged; '
                                                                                               'projects/pec/init/ '
                                                                                               'is '
                                                                                               'unchanged.\n'
                                                                                               '  - No '
                                                                                               'CHECKING, '
                                                                                               'ISSUED, '
                                                                                               'acceptance, '
                                                                                               'release or '
                                                                                               'reliance '
                                                                                               'act; no '
                                                                                               'lifecycle '
                                                                                               'state '
                                                                                               'changes.\n',
               'execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md': '# Coordination Notice — '
                                                                                 'PEC retires its '
                                                                                 'deliverable Remaining '
                                                                                 'sections\n'
                                                                                 '\n'
                                                                                 '**Status:** NON-BINDING '
                                                                                 'NOTICE\n'
                                                                                 '**Receiving loop:** '
                                                                                 'Chirality Root\n'
                                                                                 '**Sending loop:** PEC '
                                                                                 '(`projects/pec`), '
                                                                                 'HELP_HUMAN undertaking '
                                                                                 '`HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`\n'
                                                                                 '\n'
                                                                                 'PEC has retired the `## '
                                                                                 'Remaining` sections of its '
                                                                                 'deliverable `_STATUS.md`\n'
                                                                                 'files under `{N}`, as App '
                                                                                 'and Piping did on '
                                                                                 '2026-09-23. Every item '
                                                                                 'was\n'
                                                                                 'accounted for in a finite '
                                                                                 'account at\n'
                                                                                 '`projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`\n'
                                                                                 'and was either closed on '
                                                                                 'its record or moved '
                                                                                 'verbatim, with its gate, '
                                                                                 'into\n'
                                                                                 "`{N}`'s decision-owned "
                                                                                 'exhibit. Evidence '
                                                                                 'inquiries stay there '
                                                                                 'unselected;\n'
                                                                                 'Scope of Work '
                                                                                 'carry-forwards are '
                                                                                 'absorbed later by the '
                                                                                 'currency packets the\n'
                                                                                 'exhibit names. '
                                                                                 '`projects/pec/AGENTS.md` '
                                                                                 "now says PEC's\n"
                                                                                 '`_STATUS.md` files carry '
                                                                                 'lifecycle and history only '
                                                                                 'and that no Remaining\n'
                                                                                 "entry is added. PEC's "
                                                                                 'fences, `D-PEC` packet '
                                                                                 'rule, K-AUTH-1 and '
                                                                                 'reliance-hold\n'
                                                                                 'control are unchanged.\n'
                                                                                 '\n'
                                                                                 'The alignment manual\n'
                                                                                 '`docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.md`\n'
                                                                                 '(line 60) still lists '
                                                                                 '"Deliverable `Remaining`" '
                                                                                 "among PEC's governing\n"
                                                                                 'surfaces. PEC reads no '
                                                                                 'Root text as changed by '
                                                                                 'this retirement. Root may\n'
                                                                                 'update that row, keep it, '
                                                                                 'or decline. This notice '
                                                                                 'asks for no write.\n'
                                                                                 '\n'
                                                                                 'Tranche manifest: '
                                                                                 '`docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-{DC}.yaml`.\n',
               'projects/chirality-runtime/execution/_Coordination/NOTICE_{D}_PEC_REMAINING_RETIREMENT.md': '# '
                                                                                                            'Coordination '
                                                                                                            'Notice '
                                                                                                            '— '
                                                                                                            'PEC '
                                                                                                            '`AGENTS.md` '
                                                                                                            'changed: '
                                                                                                            'Remaining '
                                                                                                            'sections '
                                                                                                            'retired\n'
                                                                                                            '\n'
                                                                                                            '**Status:** '
                                                                                                            'NON-BINDING '
                                                                                                            'NOTICE\n'
                                                                                                            '**Receiving '
                                                                                                            'loop:** '
                                                                                                            'Chirality '
                                                                                                            'Runtime\n'
                                                                                                            '**Sending '
                                                                                                            'loop:** '
                                                                                                            'PEC '
                                                                                                            '(`projects/pec`), '
                                                                                                            'HELP_HUMAN '
                                                                                                            'undertaking '
                                                                                                            '`HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`\n'
                                                                                                            '\n'
                                                                                                            'Runtime '
                                                                                                            'DEL-02-06 '
                                                                                                            'pins '
                                                                                                            '`projects/pec/AGENTS.md`\n'
                                                                                                            '(`execution/PKG-02_Runtime_Product/1_Working/DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance/_run_records/DEL-02-06-RUNTIME-SPEC-001/clients/SOURCE_PINS.json`).\n'
                                                                                                            'Under '
                                                                                                            '`{N}`, '
                                                                                                            'PEC '
                                                                                                            'replaced '
                                                                                                            'one '
                                                                                                            'paragraph '
                                                                                                            'of '
                                                                                                            'that '
                                                                                                            'file '
                                                                                                            '(section '
                                                                                                            '"Deliverable\n'
                                                                                                            'records '
                                                                                                            'and '
                                                                                                            'loop '
                                                                                                            'ownership") '
                                                                                                            'and '
                                                                                                            'its '
                                                                                                            'front-matter '
                                                                                                            '`amended:` '
                                                                                                            'line. '
                                                                                                            "PEC's\n"
                                                                                                            'deliverable '
                                                                                                            '`_STATUS.md` '
                                                                                                            '`## '
                                                                                                            'Remaining` '
                                                                                                            'sections '
                                                                                                            'are '
                                                                                                            'retired; '
                                                                                                            'every '
                                                                                                            'item '
                                                                                                            'was\n'
                                                                                                            'accounted '
                                                                                                            'for '
                                                                                                            'and '
                                                                                                            'moved '
                                                                                                            'to '
                                                                                                            'a '
                                                                                                            'governing '
                                                                                                            'home '
                                                                                                            'or '
                                                                                                            'closed '
                                                                                                            'on '
                                                                                                            'its '
                                                                                                            'record, '
                                                                                                            'and '
                                                                                                            'no\n'
                                                                                                            'new '
                                                                                                            'Remaining '
                                                                                                            'entry '
                                                                                                            'is '
                                                                                                            'added. '
                                                                                                            'No '
                                                                                                            'other '
                                                                                                            'instruction, '
                                                                                                            'fence '
                                                                                                            'or '
                                                                                                            'boundary '
                                                                                                            'in '
                                                                                                            'the\n'
                                                                                                            'file '
                                                                                                            'changed, '
                                                                                                            'and '
                                                                                                            'the '
                                                                                                            'Shared '
                                                                                                            'Runtime '
                                                                                                            'Boundary '
                                                                                                            'section '
                                                                                                            'is '
                                                                                                            'untouched.\n'
                                                                                                            '\n'
                                                                                                            'Runtime '
                                                                                                            'decides '
                                                                                                            'whether '
                                                                                                            'and '
                                                                                                            'when '
                                                                                                            'to '
                                                                                                            're-pin. '
                                                                                                            'This '
                                                                                                            'notice '
                                                                                                            'asks '
                                                                                                            'for '
                                                                                                            'no '
                                                                                                            'write.\n'
                                                                                                            '\n'
                                                                                                            'Tranche '
                                                                                                            'manifest: '
                                                                                                            '`docs/governance_harness/tranche_manifests/PEC-REMAINING-RETIREMENT-{DC}.yaml`.\n'}}
# ------------------------------------------------------------ end pinned block

TM_REL = 'execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/'
TM = 'projects/pec/' + TM_REL
ACCOUNT = TM + 'SEMANTIC_DECISION_ACCOUNT.csv'
CENSUS = TM + 'REMAINING_CENSUS.csv'
AGENTS = 'projects/pec/AGENTS.md'
NODE_NAMES = {'S1': 'S1 (SOW currency, review and housekeeping class)',
              'S2': 'S2 (SOW currency, rebuild class)',
              'S4': 'S4 (SOWs whose quoted PRD text SCA-006 changes)'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fail(msg):
    print('FAIL ' + msg)
    sys.exit(1)


def read(repo, rel):
    p = os.path.join(repo, rel)
    if not os.path.isfile(p):
        fail('missing ' + rel)
    return open(p, 'rb').read()


def rows_of(b):
    return list(csv.DictReader(io.StringIO(b.decode('utf-8'), newline='')))


def slot(s, a):
    return (s.replace('{DC}', a.act_date.replace('-', '')).replace('{D}', a.act_date)
             .replace('{R}', a.ruling_date).replace('{N}', a.decision))


def resolved(r, a):
    """Return the applied destination class for a row, after the owner's question answers."""
    if r['Disposition'] == 'e':
        if r['Key'] != 'DEL-03-06-REM-004':
            fail('unexpected owner-decision row ' + r['Key'])
        return {'s1': 'EXHIBIT_B_CARRY_S1', 'park': 'EXHIBIT_A_D83E', 'decline': 'CLOSED_BY_RULING'}[a.q1]
    return r['DestinationClass']


def label(cls, a):
    if cls == 'EXHIBIT_A_D83E':
        return 'the `D-PEC-83` E evidence-inquiry set in the %s exhibit (still unselected)' % a.decision
    if cls.startswith('EXHIBIT_B_CARRY_'):
        n = cls[-2:]
        return ('the %s exhibit, for exact carry-forward into this deliverable\'s `ScopeOfWork.md` by '
                'work-graph node %s' % (a.decision, n))
    if cls == 'CLOSED_BY_RULING':
        return 'closed by the %s ruling (the owner declined the correction)' % a.decision
    if cls == 'CLOSED_ON_RECORD':
        return 'closed on the record cited in the account'
    fail('label ' + cls)


def status_post(pre, keys, rs, a, exhibit_rel):
    t = pre.decode('utf-8')
    marker = '\n\n## Remaining\n'
    if t.count(marker) != 1 or t.count('## Remaining') != 1:
        fail('Remaining anchor not unique')
    head, section = t.split(marker, 1)
    if re.search(r'^## ', section, re.M):
        fail('Remaining is not the last section')
    found = re.findall(r'^- \[.\] (DEL-\d\d-\d\d-REM-\d{3}) — ', section, re.M)
    if found != keys:
        fail('section keys %s != account keys %s' % (found, keys))
    lu = re.findall(r'^\*\*Last Updated:\*\* \S+$', head, re.M)
    if len(lu) != 1 or head.count('\n## History\n') != 1:
        fail('Last Updated / History anchor')
    head = head.replace(lu[0], '**Last Updated:** ' + a.act_date, 1)
    groups = []
    for cls in ('EXHIBIT_A_D83E', 'EXHIBIT_B_CARRY_S1', 'EXHIBIT_B_CARRY_S2', 'EXHIBIT_B_CARRY_S4', 'CLOSED_ON_RECORD', 'CLOSED_BY_RULING'):
        ks = [r['Key'] for r in rs if resolved(r, a) == cls]
        if ks:
            groups.append('%s → %s' % (', '.join(ks), label(cls, a)))
    moved = any(resolved(r, a).startswith('EXHIBIT_') for r in rs)
    ex_note = (' Exhibit: `%s`.' % exhibit_rel.split('projects/pec/', 1)[1]) if moved else ''
    line = ('- %s — `## Remaining` section retired under %s by WORKING_ITEMS (PEC Remaining retirement). '
            'Its items, with their original text, are accounted for in `%s`; each was moved verbatim, with its '
            'gate, or closed: %s.%s No lifecycle change: no CHECKING, ISSUED or artifact acceptance is implied.'
            % (a.act_date, a.decision, TM_REL, '; '.join(groups), ex_note))
    return (head.rstrip('\n') + '\n' + line + '\n').encode('utf-8')


def exhibit(rows, a):
    A = [r for r in rows if resolved(r, a) == 'EXHIBIT_A_D83E']
    B = {n: [r for r in rows if resolved(r, a) == 'EXHIBIT_B_CARRY_' + n] for n in ('S1', 'S2', 'S4')}
    L = ['# %s exhibit — PEC Remaining items moved on retirement' % a.decision, '',
         'Created by the %s retirement act on %s (ruling of %s). Each item below was a deliverable `_STATUS.md` '
         '`## Remaining` item applied under `D-PEC-83` A-A (Receipt 174), except `DEL-01-05-REM-003`, which comes '
         'from the frozen carrier that `D-PEC-83` F never applied. The finite account is '
         '`projects/pec/%sSEMANTIC_DECISION_ACCOUNT.csv`. Every item keeps its exact text, `Depends:` value and '
         'gate, and **its gate still binds it here**. Being listed performs no inquiry or production, opens no '
         'path, selects no work and implies no completion, CHECKING, ISSUED or acceptance.'
         % (a.decision, a.act_date, a.ruling_date, TM_REL), '',
         '## Part A — the `D-PEC-83` E evidence-inquiry set (%d items)' % len(A), '',
         '`D-PEC-83` E selected no individual evidence-only inquiry. These items stay **unselected**. One may run '
         'only when owner steering selects it into a work graph and its own gate is met. At selection, re-derive '
         'its linked claims against the deliverable\'s `ScopeOfWork.md` current at that time; the currency notes '
         'below are the retirement assessment\'s observations, not authority.', '']
    for r in A:
        L += ['### %s (%s, %s)' % (r['Key'], r['DeliverableID'], r['Lifecycle']), '', r['ItemText'], '',
              'Depends: ' + r['Depends'], '', 'Gate: ' + r['GateMarkers'], '']
        if r['ClaimCurrency'].strip():
            L += ['Currency note (2026-09-26 assessment): ' + ' '.join(r['ClaimCurrency'].split()), '']
        if r['Population'] != 'LIVE_REMAINING':
            L += ['Provenance (frozen `D-PEC-83` F carrier, never applied; its application gate is superseded by '
                  'this ruling\'s closure of F): ' + r['Annotations'], '']
        if r['Disposition'] == 'e':
            L += ['Correction input (parked by the owner\'s answer to question 1; not applied, not selected): '
                  + ' '.join(r['DestinationExactText'].split()), '']
    L += ['## Part B — Scope of Work carry-forwards (%d items)' % sum(len(v) for v in B.values()), '',
          'Each of these items belongs in its deliverable\'s `ScopeOfWork.md`, which a pending currency node of '
          'work graph `HELP-HUMAN-PEC-20260925-POST-SCA005` will rewrite. To avoid editing the same Scope of Work '
          'twice, the retirement does not write it. The named node\'s owner-ruled packet absorbs the carry-forward '
          'input below as an exact carry-forward, re-verified at that packet\'s basis, and its ruling discharges '
          'the item\'s gate only for the text it applies. Until then the item stays here.', '']
    for n in ('S1', 'S2', 'S4'):
        if not B[n]:
            continue
        L += ['### Node %s — %d item%s' % (NODE_NAMES[n], len(B[n]), '' if len(B[n]) == 1 else 's'), '']
        for r in B[n]:
            L += ['#### %s (%s, %s)' % (r['Key'], r['DeliverableID'], r['Lifecycle']), '',
                  'Original item: ' + r['ItemText'], '', 'Depends: ' + r['Depends'], '',
                  'Gate: ' + r['GateMarkers'], '', 'Carry-forward input for %s:' % n, '',
                  r['DestinationExactText'].strip(), '']
    return ('\n'.join(L).rstrip('\n') + '\n').encode('utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--act-date', required=True)
    ap.add_argument('--ruling-date', required=True)
    ap.add_argument('--decision', default='D-PEC-99')
    ap.add_argument('--q1', choices=('s1', 'park', 'decline'), default='s1')
    ap.add_argument('--check-only', action='store_true')
    ap.add_argument('--reproduction', action='store_true')
    ap.add_argument('--render-to')
    a = ap.parse_args()
    for d in (a.act_date, a.ruling_date):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', d):
            fail('date ' + d)
    if not re.fullmatch(r'D-PEC-\d{2,3}', a.decision):
        fail('decision id')
    if not a.reproduction and datetime.date.today().isoformat() != a.act_date:
        fail('local date %s != act date %s' % (datetime.date.today().isoformat(), a.act_date))
    repo = a.repo

    for rel, h in PINS['basis'].items():
        if sha(read(repo, rel)) != h:
            fail('basis hash ' + rel)
    rows = rows_of(read(repo, ACCOUNT))
    census = rows_of(read(repo, CENSUS))
    if [r['Key'] for r in rows] != [r['Key'] for r in census] or len({r['Key'] for r in rows}) != 92:
        fail('account keys != census keys (92)')
    for r in rows:
        if r['Disposition'] not in ('c', 'd', 'e'):
            fail('disposition outside the prepared set: %s %s' % (r['Key'], r['Disposition']))
        for f in ('ItemText', 'Depends', 'GateMarkers'):
            if not r[f].strip():
                fail('empty %s for %s' % (f, r['Key']))

    exhibit_rel = slot(PINS['exhibit_path'], a)
    out = {}
    by_path = {}
    for r in rows:
        if r['Population'] == 'LIVE_REMAINING':
            by_path.setdefault(r['SourcePath'], []).append(r)
    if sorted(by_path) != sorted(PINS['status']):
        fail('status population != grant')
    for rel, rs in by_path.items():
        pre = read(repo, rel)
        if sha(pre) != PINS['status'][rel]:
            fail('preimage ' + rel)
        out[rel] = status_post(pre, [x['Key'] for x in rs], rs, a, exhibit_rel)

    if os.path.exists(os.path.join(repo, exhibit_rel)):
        fail('exhibit exists')
    out[exhibit_rel] = exhibit(rows, a)

    pre = read(repo, AGENTS)
    if sha(pre) != PINS['agents_pre']:
        fail('AGENTS.md preimage: SCA-006 checkpoint 3 (PR #943) must be merged first')
    t = pre.decode('utf-8')
    for old, new in PINS['agents_replacements']:
        if t.count(old) != 1:
            fail('AGENTS.md anchor count')
        t = t.replace(old, slot(new, a), 1)
    out[AGENTS] = t.encode('utf-8')

    for rel, body in PINS['new_files'].items():
        rel2 = slot(rel, a)
        if os.path.exists(os.path.join(repo, rel2)):
            fail('exists ' + rel2)
        out[rel2] = slot(body, a).encode('utf-8')

    grant = set(PINS['status']) | {exhibit_rel, AGENTS} | {slot(k, a) for k in PINS['new_files']}
    if set(out) != grant:
        fail('write set != grant: %s' % sorted(set(out) ^ grant))
    for rel, b in out.items():
        if rel.endswith('/_STATUS.md') and re.search(r'^## Remaining', b.decode('utf-8'), re.M):
            fail('Remaining survives ' + rel)
    ex = out[exhibit_rel].decode('utf-8')
    for r in rows:
        cls = resolved(r, a)
        if cls.startswith('EXHIBIT_') and not all(x in ex for x in (r['Key'], r['ItemText'], 'Depends: ' + r['Depends'], 'Gate: ' + r['GateMarkers'])):
            fail('exhibit misses ' + r['Key'])
    for rel in sorted(out):
        print('POST %s %s' % (sha(out[rel]), rel))
    from collections import Counter
    c = Counter(resolved(r, a) for r in rows)
    print('CHECK write_set %d' % len(out))
    print('CHECK status_sections_removed %d' % len(by_path))
    print('CHECK account_keys %d %s' % (len(rows), dict(sorted(c.items()))))
    if a.check_only:
        print('CHECK-ONLY: nothing written')
        return
    target = a.render_to or repo
    for rel, b in out.items():
        p = os.path.join(target, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'wb') as fh:
            fh.write(b)
    print(('RENDERED to ' + target) if a.render_to else ('WROTE %d files' % len(out)))


if __name__ == '__main__':
    main()
