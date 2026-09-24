# Unbound Pipe effective-wall gap — route to ROOT

**Confirmed in the existing WASM operation artifact; source trace identifies the same unchecked branch.** The bounded10-case probe exited1 for two unsafe accepted cases, not an environmental failure. No engine or product source was changed by this diagnostic. ROOT granted only the existing-WASM lane; it has been released.

The fixture is the existing invented precision-origin model. Its first Pipe has explicit OD0.06m and wall0.004m, with initially absent mill tolerance. For unbound cases only, the existing section_ref was removed while the inline known geometry stayed identical. Each operation has beforeTBD, explicit value/unit JSON and dimensionlength. Both validate_only and apply were called through the actual WASM export. All full inputs, operation outcomes and applied documents are retained under `_run_records/optional-wall-probe/`; command/status and manifest are adjacent.

| Tolerance entry | Bound Pipe | Unbound Pipe |
|---|---|---|
| 0m | Applied, expected | Applied, expected |
| 0.001m | Applied, expected | Applied, expected |
| 0.004m (equal wall) | Rejected OP-SECTION-BINDING-INVALID, expected | Applied without diagnostics, defect |
| 0.005m (greater than wall) | Rejected OP-SECTION-BINDING-INVALID, expected | Applied without diagnostics, defect |
| -0.001m | Rejected OP-VALUE-NEGATIVE, expected | Rejected OP-VALUE-NEGATIVE, expected |

The unbound equal-wall validation result reports schema/unit/before-state passed and a generated diff with no diagnostic; Apply publishes mill_tolerance0.004m against wall0.004m. The input documents remain unchanged as reported by the operation outcome. These are invalid **known** effective walls, not absent or incomplete physical inputs. The probe makes no claim about how missing geometry should be authored or diagnosed.

Causal source: `core/model_operations/operation_applier/src/lib.rs` routes Element field candidates to `section_bindings::validate_local`. That function in `section_bindings.rs`214ff validates geometry/cache only inside a present section_ref. The existing geometry helper76ff checks nonnegative mill reduction and strictly positive remaining wall. The OptionalQuantity field rule correctly rejects negatives and accepts zero but cannot enforce the coupled wall relation alone.

Proposed owning repair: enforce the known-geometry/effective-wall relation independently of shared binding on relevant local quantity changes, while preserving the accepted policy for missing/incomplete authored data. Do not blindly invoke the strict full shared-section geometry helper for every unrelated Element text/reference edit, which could block legitimate incomplete authoring. ROOT/solver should select the exact bounded backend change, add bound/unbound and missing/incomplete controls, rebuild the operation artifact and repeat these unchanged cases. This manager has no engine write authority.

The Pipe frontend will preserve backend outcomes and include the bound rejection plus valid controls. It must not mask this defect with an independent TypeScript engineering validator or count unsafe unbound Apply as a passing requirement. Unbound effective-wall rejection remains a connected acceptance dependency until the owning repair and actual route backcheck complete.

Exact artifact/source identity is `_run_records/optional-wall-probe/identity.json`; its current-source hashes and existing WASM bytes are recorded separately. No rebuild bound the binary anew, so this is an observed existing-artifact defect with source-supported causality, not a fresh source build claim.
