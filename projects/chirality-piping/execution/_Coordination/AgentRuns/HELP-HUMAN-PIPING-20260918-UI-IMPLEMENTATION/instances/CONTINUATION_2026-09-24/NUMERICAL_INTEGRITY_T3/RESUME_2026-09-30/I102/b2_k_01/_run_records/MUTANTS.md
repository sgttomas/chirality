# I102 mutants (one per new check; each run on a scratch copy of the committed FK)

## Part 1 (B3-K), against 806424c6de; filter `product_certificate`

| Id | Check | Verdict | Killed by |
|---|---|---|---|
| p1m1 | K3-1: BaseENu maps to ExactENu { e, nu } (mutant: nu forced to 0) | KILLED | b3k_base_e_nu_maps_to_exact_operands_and_refuses_through_the_public_variant, b3k_base_e_nu_stress_and_maximum_rows_certify_in_both_lanes_nu_0_3125_control, b3k_restored_material_gate_fails_stress_and_maximum_rows_with_represented_z |
| p1m2 | K3-2: represented Z for ExactENu (mutant: the material gate restored) | KILLED | b3k_base_e_nu_stress_and_maximum_rows_certify_in_both_lanes_nu_0_3125_control, b3k_exact_e_nu_represented_z_axis_bits_and_restored_material_gate, b3k_nu_0_3125_control_and_exact_g_against_represented_g, b3k_restored_material_gate_fails_stress_and_maximum_rows_with_represented_z, product_certificate_fraction_geometry_material_and_coefficients |
| p1m3 | K3-2: Iy = Iz axis bits for ExactENu (mutant: skipped for ExactENu) | KILLED | b3k_exact_e_nu_represented_z_axis_bits_and_restored_material_gate |
| p1m4 | K3-2: the hull with I_K/c (mutant: Z-hat point for ExactENu) | KILLED | b3k_exact_e_nu_represented_z_axis_bits_and_restored_material_gate, b3k_nu_0_3125_control_and_exact_g_against_represented_g, product_certificate_fraction_geometry_material_and_coefficients |

## Part 2 (B2-K), against f7494326f1; filter `b2k` (plus `origins` or `source_residual` where noted in the runner)

| Id | Check | Verdict | Killed by |
|---|---|---|---|
| p2m01 | SF-1 run-capacity check | KILLED | b2k_k02_for_invocation_registration_and_the_run_capacity_check |
| p2m02 | registration capacity | KILLED | b2k_k02_for_invocation_registration_and_the_run_capacity_check |
| p2m03 | I7: a case-owned source | SURVIVED | - |
| p2m04 | I7: no combination ledger | SURVIVED | - |
| p2m05 | I7: full K4SRC bytes | KILLED | b2k_k03_an_unavailable_operand_is_rebuilt_identity_checked_and_custody_refuses_otherwise |
| p2m06 | NoSelectedOperand (recorded) | KILLED | b2k_k04_no_selected_operand_is_refused_after_the_native_checks |
| p2m07 | NoSelectedOperand (unrecorded) | KILLED | b2k_k04_unrecorded_all_prepared_is_no_selected_operand_after_the_native_checks |
| p2m08 | first selected group (recorded) | KILLED | b2k_k05_a_prepared_first_operand_keeps_authored_order_and_takes_the_group_of_operand_one |
| p2m09 | first selected group (unrecorded) | KILLED | b2k_k05_a_prepared_first_operand_keeps_authored_order_and_takes_the_group_of_operand_one |
| p2m10 | authored-order cache merge (recorded) | SURVIVED | - |
| p2m11 | requested operand source in range | KILLED | b2k_k03_an_unavailable_operand_is_rebuilt_identity_checked_and_custody_refuses_otherwise |
| p2m12 | for_invocation counts prepared ordinals | KILLED | b2k_c01_c04_mixed_operands_match_all_selected_bits_charge_nothing_and_change_no_operand, b2k_k02_for_invocation_registration_and_the_run_capacity_check, b2k_k04_no_selected_operand_is_refused_after_the_native_checks, b2k_k05_a_prepared_first_operand_keeps_authored_order_and_takes_the_group_of_operand_one, b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags, b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows, b2k_k10_mutation_controls_fail_containment, b2k_k12_the_i42_bridge_holds_for_a_p2_combination_owner |
| p2m13 | source reservation cases + combinations | KILLED | b2k_k02_for_invocation_registration_and_the_run_capacity_check |
| p2m14 | I9 owner kind | KILLED | b2k_k06_product_owner_is_the_recorded_kind_of_the_run |
| p2m15 | view: factor bits | KILLED | b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags |
| p2m16 | view: term count | KILLED | b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags |
| p2m17 | view: +0.0 by bits (N-3) | KILLED | b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags |
| p2m18 | view: visits before checks (N-8) | KILLED | b2k_k07_view_admits_p2_refuses_corruption_and_keeps_native_data_flags |
| p2m19 | residual: free rows read the ledger | KILLED | b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows, b2k_k10_mutation_controls_fail_containment |
| p2m20 | recovery: reaction offsets read the ledger (SF-2) | KILLED | b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows, b2k_k10_mutation_controls_fail_containment |
| p2m21 | net: outward, not nearest (SF-4) | KILLED | b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward |
| p2m22 | free rows add the net | KILLED | b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows, b2k_k10_mutation_controls_fail_containment, source_residual_combination_and_missing_uniqueness_are_explicit_refusals |
| p2m23 | reactions subtract the net | KILLED | b2k_k08_residual_and_recovery_contain_the_oracle_and_nets_are_exact_outward, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows, b2k_k10_mutation_controls_fail_containment |
| p2m24 | coverage: combination row families | KILLED | b2k_c05_the_combination_coverage_rule |
| p2m25 | coverage: slot 20 empty | KILLED | b2k_c05_the_combination_coverage_rule, b2k_c06_a_nonzero_prescription_in_a_later_operand_is_unsupported, b2k_k06_both_certificate_entries_accept_a_recorded_combination_owner_only, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows |
| p2m26 | coverage: no mode record | KILLED | b2k_c05_the_combination_coverage_rule, b2k_c06_a_nonzero_prescription_in_a_later_operand_is_unsupported, b2k_k06_both_certificate_entries_accept_a_recorded_combination_owner_only, b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows |
| p2m27 | (ii): magnitudes hull-projected instead | KILLED | b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows |
| p2m28 | (ii): mm components | KILLED | b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work |
| p2m29 | (ii): upper tie to even | SURVIVED (not equivalent: corrected in Repair 01 below) | - |
| p2m30 | (ii): lower tie to even | SURVIVED | - |
| p2m31 | (ii): SA4-1 (b) refusal at MAX | KILLED | b2k_rn64_norm3_agrees_with_the_oracle_vectors, b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work |
| p2m32 | (ii): SA4-1 (d) one step | SURVIVED | - |
| p2m33 | (ii): SA4-1 (c) overflowing estimate decided exactly | SURVIVED | - |
| p2m34 | (ii): SA4-1 (e) zero estimate | SURVIVED | - |
| p2m35 | certify_product_case owner check | KILLED | b2k_k06_both_certificate_entries_accept_a_recorded_combination_owner_only |

Re-run against ef51a2d295 after the follow-up tests:

| Id | Check | Verdict | Killed by |
|---|---|---|---|
| p2m03 (re-run) | I7: a case-owned source | KILLED | b2k_k03_each_i7_check_refuses_on_its_own |
| p2m04 (re-run) | I7: no combination ledger | KILLED | b2k_k03_each_i7_check_refuses_on_its_own |
| p2m10 (re-run) | authored-order cache merge (recorded) | KILLED | b2k_k05_a_prepared_first_operand_keeps_authored_order_and_takes_the_group_of_operand_one |

## Repair 01 (RV121's RK-1 to RK-4), against e22fd799bc; filter `b2k`

**Correction (RK-1).** p2m29 is not equivalent. RETURN.md said that y0 is never
odd at a tie. That holds only for estimates that do not overflow. At an exact
overflow tie, S = (MAX + 2^970)^2, the 1024-bit square root is MAX + 2^970,
which overflows to y0 = MAX. MAX is odd, and only the upper tie clause refuses.
Under p2m29 the kernel publishes MAX where SA4-1 (b) refuses. Three binary64
components reach this, for example (7fefffffffffffe5, 7e7443426b800000,
7e4d4ef94a000000). The reasons for p2m30, p2m32, p2m33 and p2m34 stand:
RV121 confirms them.

| Id | Check | Verdict | Killed by |
|---|---|---|---|
| p2m29 (re-run) | (ii): upper tie to even | KILLED | b2k_rn64_norm3_vectors_signed_zeros_refusal_and_work, b2k_rn64_norm3_agrees_with_the_oracle_vectors (the overflow tie) |
| m36 (RV121's) | a case owner's displacement magnitude formed as (ii) (`let combination=true;` in `project`) | KILLED | b2k_k13_a_case_owner_keeps_its_hull_projected_displacement_magnitude |
| m18 (RV121's) | slot 20 exempted for every owner (`!(j % 21 == 20)`) | KILLED | b2k_c05_the_combination_coverage_rule (the maximum alone missing) |
| mrk4 | relative rows judged only on the two decimal predicates (`tests.into_iter().skip(2)`) | KILLED | b2k_k09_full_prepared_proof_certifies_combinations_and_prints_the_diagnose_rows (the pinned pattern) |

At ef51a2d295, mrk4 survives FK's whole lib: 508 passed, 0 failed. The net-case
parity in K-09 cannot detect it, because the same gate decides both owners.
RV121 shows that p2m29 (with its probe), m36 and m18 survive at ef51a2d295.
