"""I101 B3 readers: the RS mutants, one per new check (B3a, B3b). Each replaces exactly one occurrence."""
RP = "core/reporting/result_export/src/retained_precision.rs"
SC = "core/reporting/result_export/src/semantic_contract.rs"
DV = "core/reporting/result_export/src/derivative.rs"
M = [
 # B3a: D1.3's preview namespace, type-strict
 ("A1", "B3a L branch admits any contract", RP, 'Some("0.1.0" | "0.2.0") => model["pressure_contract"].is_null(),', 'Some("0.1.0" | "0.2.0") => true,'),
 ("A2", "B3a L3 also admits 0.3.0 without a contract", RP, 'pressure_contract_is(&model["pressure_contract"], "1.0.0", "legacy_pressure_v1")', 'model["pressure_contract"].is_null() || pressure_contract_is(&model["pressure_contract"], "1.0.0", "legacy_pressure_v1")'),
 ("A3", "contract: extra keys admitted", RP, "        o.len() == 2\n            && o.get(\"version\")", "        true\n            && o.get(\"version\")"),
 ("A4", "contract: version unchecked", RP, '            && o.get("version").and_then(Value::as_str) == Some(version)\n', ''),
 ("A5", "contract: mode unchecked", RP, '            && o.get("mode").and_then(Value::as_str) == Some(mode)\n', ''),
 # B3b G0 exact, steps 1-9
 ("B01", "G0 step 1: profile unchecked", RP, '            && source["formulation_basis"]["profile_id"] == EXACT_PROFILE,', ''),
 ("B02", "G0 step 2: producer and envelope schema unchecked", RP, '    // 2. Producer component and version; envelope schema 0.2.0.\n    unsupported(', '    // 2. Producer component and version; envelope schema 0.2.0.\n    unsupported(true ||'),
 ("B03", "G0 step 3: table identity compared with the preview id", RP, 't["semantic_contract_id"] == EXACT_CONTRACT_ID && t["formulation_profile_id"] == EXACT_PROFILE,', 't["semantic_contract_id"] == CONTRACT_ID && t["formulation_profile_id"] == EXACT_PROFILE,'),
 ("B04", "G0 step 4: DEF-E's H compared with DEF-O's", RP, '        )? == EXACT_DEFINITION_HASH\n', '        )? == DEFINITION_HASH\n'),
 ("B05", "G0 step 5: inherited hash against preview-physics-1's bytes", RP, '&& t["inherited_semantic_contract_sha256"] == sha256_hex(PHYSICS_TABLE_BYTES),', '&& t["inherited_semantic_contract_sha256"] == sha256_hex(INHERITED_TABLE_BYTES),'),
 ("B06a", "G0 step 6: the cross-check always binds", RP, '    table["receipt_bindings"] == receipt_bindings()\n', '    true || table["receipt_bindings"] == receipt_bindings()\n'),
 ("B06b", "G0 step 6: the call dropped", RP, '    unsupported(table_binds_reader_constants(t))?;', ''),
 ("B07", "G0 step 7: receipt_version unchecked", RP, '    // 7. receipt_version 1 (D32: by value).\n    unsupported(uint(&b["receipt_version"]) == Some(1))?;', '    // 7. receipt_version 1 (D32: by value).'),
 ("B08", "G0 step 8: policies unchecked", RP, '        unsupported(want.is_string() && b[key] == *want)?;', '        let _ = (want, key);'),
 ("B09", "G0 step 8: limits unchecked", RP, '        unsupported(rb["work"][key].as_u64().is_some() && uint(&b["work"][key]) == rb["work"][key].as_u64())?;', '        let _ = key;'),
 ("B10", "G0 step 9: definition ids unchecked", RP, '            unsupported(a["definition_id"] == EXACT_DEFINITION_ID)?;', ''),
 # G1 S-1
 ("B11", "G1 S-1: DEF-O's H on the exact route", RP, '    definition_hash: EXACT_DEFINITION_HASH,', '    definition_hash: DEFINITION_HASH,'),
 # G5b evidence
 ("B12", "G5b evidence: the pass dropped", RP, '        g5b_exact_evidence(source, &cases)?;', ''),
 ("B13", "G5b evidence: a repeated case entry admitted", RP, '        section(entries.len() == 1)?;', '        section(!entries.is_empty())?;'),
 ("B14", "G5b evidence: a repeated pipe entry admitted", RP, '            section(matched.len() == 1)?;', '            section(!matched.is_empty())?;'),
 ("B15", "G5b evidence: As unchecked", RP, '                ("As_m2", &st["area"]),\n', ''),
 ("B16", "G5b evidence: Z unchecked", RP, '                ("Z_m3", &st["section_modulus"]),\n', ''),
 ("B17", "G5b evidence: OD unchecked", RP, '                ("outside_diameter_m", &g["normalized_od"]),\n', ''),
 ("B18", "G5b evidence: wall unchecked", RP, '                ("effective_wall_thickness_m", &g["effective_wall"]),\n', ''),
 ("B19", "G5b evidence: ro unchecked", RP, '                ("ro_m", &g["actual_radius"]),\n', ''),
 ("B20", "G5b evidence: I unchecked", RP, '                ("I_m4", &g["actual_second_moment"]),\n', ''),
 ("B21", "G5b evidence: J unchecked", RP, '                ("J_m4", &g["actual_polar_moment"]),\n', ''),
 # G7
 ("B22", "G7: the exact route projected onto preview-physics-1", RP, '    base_id: "openpipestress.result_semantics/0.3.0/physics-1",', '    base_id: "openpipestress.result_semantics/0.3.0/preview-physics-1",'),
 # G8
 ("B23", "G8 step 1: the exact route read with the legacy namespace", RP, 'if route.exact { exact_namespace(model) } else { legacy_namespace(model) }', 'legacy_namespace(model) || route.exact'),
 ("B24", "G8 step 1: the exact contract unchecked", RP, '        && pressure_contract_is(&model["pressure_contract"], "2.0.0", "exact_straight_pressure_v2")', ''),
 ("B25", "G8 step 3: base selection unchecked", RP, '        fail(!route.exact || value == json!({"kind":"base"}))?;', ''),
 ("B26", "G8 step 4: shear origin unchecked", RP, '                        && m["shear_origin"]\n                            == json!({"kind":"derived_e_nu","poisson_ratio":bits(nu),\n                                "constitutive_basis":"homogeneous_isotropic_E_nu_v1"})\n', ''),
 ("B27", "G8 step 4: selection unchecked", RP, '                        && m["selection"] == json!({"kind":"base"})\n', ''),
 ("B28", "G8 step 4: E bits unchecked", RP, '                        && m["elastic_modulus"] == bits(e)\n', ''),
 ("B29", "G8 step 4: G-hat bits unchecked", RP, '                        && m["shear_modulus"] == bits(g),', '                        ,'),
 ("B30", "G8 step 4: poisson unit unchecked", RP, '    fail(poisson["unit"] == "1")?;', ''),
 ("B31", "G8 step 5: S-C dropped", RP, '            crate::physics_source::actual_materials(inv, &cases[ci], entry).map_err(|detail| {', '            Ok::<(), String>(()).map_err(|detail: String| { let _ = (inv, ci, entry);'),
 ("B32", "G8 step 6: N-6 dropped", RP, '                fail(pm["G_pa"].as_f64().map(bits).as_ref() == Some(&mat["shear_modulus"]))?;', '                let _ = mat;'),
 ("B33", "G8 step 8: regions read as on the preview route", RP, '                case.get("pressure_regions").is_some_and(|r| r.as_array().is_some_and(Vec::is_empty))', '                list(&case["pressure_regions"]).is_empty()'),
 ("B34", "G8 step 9: geometry route unchecked", RP, '                    && geo["route"] == route.geometry', ''),
 ("B35", "transport: preview metadata on the exact route", RP, '        crate::physics_evidence::validate_transport_metadata(&projected).map_err(base_error)?;', '        preview_physics_transport_metadata(&projected).map_err(base_error)?;'),
 ("B36", "semantic_contract: is_retained without the exact id", SC, '        || source["producer"]["semantic_contract_id"] == PHYSICS_RETAINED_ID\n', '\n'),
 ("B37", "derivative: the exact successor's receipt not carried", DV, '        Some(PREVIEW_PHYSICS_RETAINED_ID | PHYSICS_RETAINED_ID)', '        Some(PREVIEW_PHYSICS_RETAINED_ID)'),
]
