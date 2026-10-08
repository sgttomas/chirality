# RV122 (RV-Q2), addendum 02: B3a dropped from `b2`, the PP side

RV122, for WORKING_ITEMS (T3, Agent 1), now my return path by the owner's decision. The basis is two RR sections:
- "Owner decisions: the legacy pressure contract is retired product-wide; T3 gains a WORKING_ITEMS manager" (decision 1: B3a is dropped from `b2`, and B3D-10's tightenings stay);
- "U3 rulings on I110's pressure inventory: …".

2026-10-08 UTC. RV120 confirms the readers' side; this addendum covers PP only.

**Candidate:** `b2` `0ef9a8ace9` (pushed), one commit by I113 on `51f339a11e`. The record is `R/I113/b3a_drop_01/RETURN.md` (`a2847713…`; SHA256SUMS 83 of 83 OK). I read it after my diff reading.

**Method:**
- `git archive` copies of P (without `execution/`) at both heads;
- every cargo through `t3_cargo.sh --locked --offline`, in fresh per-tree targets (`WT/targets/rv122-a2{base,cand,mut}-*`), one job at a time;
- the mutant in a `cp -R` copy of the candidate;
- no Git write.

Both heads build Registered: `the_registered_profile_is_the_only_permit_source` and `reviewed_inputs_bind…` pass.

## Verdict: CONFIRMED (0 BLOCKING, 0 SHOULD-FIX, 0 NOTE)

**The drop removes exactly B3a's PP admission.** Evidence: `addendum_02/drop_checks.out.txt`.
- **Production code:** outside comments, the drop changes four PP lines:
  - `NamespaceBranch::LegacyPressure` is removed;
  - D1.3's L3 arm is removed;
  - in `w1_route`, `B::Legacy | B::LegacyPressure` becomes `B::Legacy`.
- **The new refusal:** 0.3.0 with `{1.0.0, legacy_pressure_v1}` now falls to the existing arm, `Family(Namespace, PressureContract)`. That is B3-D §4.1's refusal map without L3. B3D-10's tightenings are unchanged: 0.3.0 without a contract still gets `PressureContract`, and 0.4.0 still gets `SchemaVersion`.
- **Lane A's production files against its confirmed head `ea5625ad04`** (my addendum 01): outside comments, the only change is the two L3 lines removed. That covers `retained_memory.rs`, `build_identity.rs`, `build.rs` and the runner's admission test.
  - Nothing else in those files changes: the SF-2 capacity clause, the D1.4 and D1.9 rows, G-C, the census, `REVIEWED_INPUTS` and the re-pin.
  - The census still reads a contract's two strings, which branch E needs.
- **Unchanged elsewhere:**
  - no static, fixture or schema changes;
  - the generated profile block is `a3c627216102bdfc` at both heads;
  - in lane P, only `lib.rs`'s `w1_route` arm and comments change.

**Suites, test by test** (`addendum_02/compare_0ef9a8ace9_vs_51f339a11e.json`):
- **PP, lib plus all integration tests:** 790 passed, 2 failed, 11 ignored becomes 791 passed, 1 failed, 11 ignored. No test changed outcome.
  - The three removed tests and their replacements are the three renamed pairs.
  - The start head's `b3a_direct_entry_oracles` failure goes with its pin.
  - The three edited tests (`b3b_witness_inputs_and_routes`, `b3b_d1_admits_the_exact_route_with_empty_regions`, `every_family_clause_refuses_with_its_fact`) pass at both heads.
  - `t13` fails at both heads.
- **Runner:** 85 passed, 2 failed at both heads, identical. The failures are the two load-reference tests, the base's own.

**My mutant A2-M1** maps the label to branch L again. It is killed by all four drop tests:
- `b3a_dropped_d1_3_refuses_the_legacy_pressure_contract_on_0_3_0`;
- `b3a_dropped_direct_entry_refuses_m3l`;
- `b3a_dropped_m3l_takes_the_ordinary_route`;
- `b3b_witness_inputs_and_routes`.

## I113's four judgement calls: all accepted

1. **The B3b assertion moved from L3 to L.** Its point, that a combination on a non-exact branch is inside D1, holds on L, now the only non-exact branch.
2. **The contract-strings capacity pin moved to E.** It has to: the label now refuses at D1.3, before the D1.9 rows, so the pin could no longer reach them on L3. E is the one branch that admits a contract. The census assertion (+2 strings) stays on m3l, because the census reads a contract on any branch.
3. **m3l's ordinary-byte pin against the milestone was not carried over.** That pin was about how the ordinary route handles the retired label, which U3 Stage 1 owns: the owner ruled the label is accepted nowhere.
   - The new tests still pin lane A's part: the Direct entry refuses m3l at D1.3, with no W1 and one run.
   - Its publication equals the plain value route's bytes in both modes, in a Registered build.
4. **Inventory sites that are B3b refusals were left unchanged.** They use the label as a refusal input on the exact route, so changing them would move B3b bytes.

**Out of this candidate's scope:** the ordinary route still accepts `1.0.0/legacy_pressure_v1` in `pressure_runtime.rs:138`. Retiring that is U3 Stage 1's work, not B3a's.

**Evidence** (`addendum_02/`):
- `drop_checks.out.txt`;
- `compare_0ef9a8ace9_vs_51f339a11e.json`;
- `a2_mut.sh`, with placeholder paths;
- `meta_a2base.txt` and `meta_a2cand.txt`.
