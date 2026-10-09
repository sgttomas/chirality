# I116 RETURN: U5, the piping governance documents follow the pressure retirement

I116 is a TASK (Type 2) for T3's WORKING_ITEMS (Agent 1), which is the return path. I delegated nothing.
- **Brief:** `R/BRIEFS/U5_GOVERNANCE_DOCS.md`, sha256 `2bd0c63e0762b3bd42fb65201ec382988d55ef37b063635a54780ffc9a3d5d89`, at NUM `c8ce1bdf0f`, verified. Also read: `R/BRIEFS/B1_COMMON.md`, with WORKING_ITEMS in ROOT's place.
- **Instructions read:** Root `AGENTS.md`; Piping `AGENTS.md` and `loop/LOOP_INIT.md`, for the notice search.
- **RR sections read:** RR, NUM copy, lines 16379–16591. That covers "Owner decisions: the legacy pressure contract is retired product-wide; …", the U3 rulings, "Owner decisions: T4 starts now; the governance-documents PR is authorized", and the T2 and #1168 rulings.
- **Product read:** U3's `T/IMPLEMENTATION/U3/CHANGE_RECORD.md`, and the product at #1168's head `37724dea27`.

Paths use `WT`, `NUM`, `P`, `T`, `R` and `RR` as in the brief.

## 1. Branch head

`WT/u5-docs`, branch `codex/piping-t3-u5-governance-docs-20261009`, head **`f995add7c6d5eb30f2a274a4da7bff7ad75577d5`**. It has three commits on main `7b2715cb0e`:
- `3b1d870227`: the three documents and the tranche manifest;
- `ca415e282d` and `f995add7c6`: two additions to the manifest's M6 rationale (the validation-planning inventory's pin, and the 2026-09-05 physics audit's authority bindings).

Neither is pushed and no PR is open. `git merge-tree` against #1168's head `37724dea27` merges cleanly. #1168 changes none of these four paths, and main's three documents have the same blobs as #1168's.

## 2. Statements found and their corrections

The full inventory is in `_run_records/STATEMENTS.md`: every pressure line in the five documents, with its kind, its disposition and the grounding for each correction. It also lists the other places found in `P/docs/`. The diff is `_run_records/branch_diff.patch`.

**The test I applied.** I corrected a statement only if it says an implemented slice, module or suite *has* a pressure capability that it no longer has at #1168. A requirement or intent statement ("shall", "Must", "should") says what the product is to do. The retirement does not make it false, so I left it unchanged. Q1 asks WORKING_ITEMS to confirm this.

**Corrected: five statements in three documents.** Each cites the owner decision by its RR heading.

| # | Where (main) | Was | Now |
|---|---|---|---|
| S1 | `P/docs/TYPES.md:172` `StressRecovery` | "recovers axial, bending, torsional, and pressure membrane stress components from explicit resultants and section/pressure inputs" | "recovers axial, bending, and torsional stress components from explicit resultants and section inputs. It has no pressure components: its legacy thin-wall pressure membrane was removed when the owner retired the legacy pressure contract product-wide (owner decision "…", path). Pressure is solved only through the exact straight-pressure contract `2.0.0/exact_straight_pressure_v2`, within that contract's own qualifications." |
| S2 | `P/docs/TYPES.md:178` `StressRecoveryBenchmark` | "… torsional shear stress, pressure membrane stress, and mechanics-only stress range" | "pressure membrane stress," is dropped, and this is added: "Its pressure membrane fixture was an oracle of the retired legacy pressure computation and was removed with it (owner decision …)." |
| S3 | `P/docs/SPEC.md:587-597` (RV127: `:591`) | "… resultants, section properties, and optional pressure basis inputs: … and thin-wall pressure membrane components. Missing resultants, missing section or pressure inputs, …" | "… resultants and section properties: axial normal stress, bending normal stress components, and torsional shear stress." Then the S1 sentences with the full citation, then "Missing resultants, missing section inputs, …" |
| S4 | `P/docs/SPEC.md:601-608` | "contains … hand-calculation notes for … pressure membrane stress, …" | The item is dropped, and this is added: "Its pressure membrane fixture, `STRESS-PRESSURE-MEMBRANE-ORIGINAL`, was an oracle of the retired legacy pressure computation and was removed with it (owner decision …)." |
| S5 | `P/docs/VALIDATION_STRATEGY.md:71-77` (RV127: `:74`) | "Its required fixture families are … pressure membrane stress, …" | The family list is unchanged, so the requirement stands. This is added: "The pressure membrane family has no fixture since the owner retired the legacy pressure contract product-wide: `STRESS-PRESSURE-MEMBRANE-ORIGINAL` was an oracle of the retired legacy pressure computation and was removed with it (owner decision …, full heading and path)." It is followed by the exact-contract sentence |

**Unchanged: requirement, intent and plan statements.** Each is listed with its reason in `STATEMENTS.md` §1.
- From RV127's list:
  - `SPEC.md:599`, "shall calculate … pressure membrane stresses";
  - `VALIDATION_STRATEGY.md:50` and `:51`, the benchmark-family strategy table. Row 50 is already conditional: "pressure thrust where modeled";
  - `INTENT.md:175` and `:182`, "should calculate";
  - `PRD.md:662`, "Expansion joints shall support … pressure thrust".
- Also unchanged:
  - `INTENT.md:154`;
  - `PRD.md:487`, `:731-732` and `:1384-1385`, plus the metadata lines;
  - `SPEC.md:538`, `:540-545` and `TYPES.md:169`, on pressure primitive loads (Q2). These remain true of the schema and of the `primitive_loads` crate, while the product refuses such loads at solve.

**What grounds the corrections.** The details are in `STATEMENTS.md` §3:
- the owner decision itself, which retires the legacy contract and removes the oracles that depend on it;
- `stress_recovery` at `37724dea27`: no `PressureBasis`, membrane, pressure components or `MissingPressureInput`;
- the U3 change record §4, and RV127 ADDENDUM_01's confirmation of the `STRESS-PRESSURE-MEMBRANE-ORIGINAL` removal;
- `pressure_runtime.rs` `validate_profile` at `37724dea27`, for "pressure is solved only through `2.0.0/exact_straight_pressure_v2`".

**The exact contract's standing.** The corrected text says only that pressure is solved through that contract, within its own qualifications. Those qualifications are the published limitations of `exact_straight_pressure_v2` and, for model 0.4.0, of `resolved_straight_load_state_v1`.
- I wrote "contract" where U3's T2 says "profile", because both of those profiles solve exact-contract pressure (`is_exact` covers 0.3.0 and 0.4.0).
- I did not describe what the contract computes. The accepted records I found each disclaim engineering acceptance:
  - the 2026-09-15 private-kernel acceptance;
  - the #905 runtime-join return.
- T4 is not anticipated.

**Other places in `P/docs/` (not edited):**
- `developer_guide/index.md:165-166` and `theory/centerline_analysis.md:117-118`: expectations, and true through exact-contract regions;
- `_Registers/Deliverables.csv:33`, `:35`, `:56` and `ScopeLedger.csv:14`, `:16`: scope, which changes only by scope change;
- `validation_manual/headless_runner_reproduction.md:201`: a dated 2026-07-20 note;
- `_ScopeChange/…` and `_history/PRD_v0.1.md`: history.

U3 already corrects the validation-manual and benchmark pages.

## 3. The tranche manifest and its validation

**The manifest:** `docs/governance_harness/tranche_manifests/PIPING-PRESSURE-RETIREMENT-DOCS-20261009.yaml`.
- It follows the shape of `PIPING-LOOP-INIT-20261005` and `ROOT-DOCS-CI-ROUTING-20261008`, checked against the validator `tools/validation/validate_instruction_tranche_manifest.py`.
- `basis`: `7b2715cb0e5efaa69239778b5b3d09582d6c3e91`.
- `instruction_surface_paths`: the three documents and the manifest. The piping documents fall outside root's G4 surface, so G4 reports them as INFO over-declaration. `ROOT-DEVELOPMENT-LOOP-MEMORY-20260922` declared piping `TYPES.md` the same way.
- `m2_gate`: the two owner decisions, by RR heading and path, with the owner's recorded words. Integration owner: T3's WORKING_ITEMS. `owner-authorized-pr`, `self_merge: true`.
- `m6_notice`: `none-required`, with the search in the rationale (§4).
- `scope_limits`: what changes, what is unchanged and why, no restatement of the exact contract, and nothing else.

**Validation** (`_run_records/`):
All of the following were rerun at the head `f995add7c6`.
- G4 CI mode: PASS, 160 manifests schema-valid, exit 0 (`g4_ci_mode.txt`).
- G4 diff mode, `--base 7b2715cb0e --head HEAD --added-manifests-only`, as CI runs it: PASS, exit 0 (`g4_diff_mode.txt`). It reports only INFO lines for this manifest.
- The rest of the governance harness, run locally at the head (`harness_light.txt`): four-role and workflow contracts, conflict markers, the run-record leak check, and G0 to G3. All PASS, exit 0.
- The tools test estate was not run separately. It is CI's routed `run_affected_tests.py`, and its live gate is GEN-8 (§5).
- The piping claims lint `validate_claims_language.py`: VALID, 385 files (`screens_and_claims_lint.txt`).

**Not done, following the precedent.** I did not regenerate `exports/chirality-app/export-manifest.csv`. `PIPING-LOOP-INIT-20261005` did not declare it either. Main's export manifest already lacks three recent manifests' rows, and its 1,881 data rows disagree with its report's 1,879. WORKING_ITEMS can run the exporter at PR time if it wants the row.

## 4. Notices

**None.** No project loop pins or mirrors the changed texts. I searched at main `7b2715cb0e`, which equals #1168 for these files. The commands and every hit are in `_run_records/notice_search.txt`:
1. **Paths:** every path outside `P` that names any of the five documents.
2. **Other loops:** any `chirality-piping/docs` reference in the App, App v4, Runtime and PEC loops and in Root's instruction surfaces.
3. **Hashes:** the five files' SHA-256 and blob ids across the whole tree.
4. **Wording:** the changed sentences' own wording.
5. **Identities:** the documents' `doc_id`s (OPS-TYPES, OPS-SPEC, OPS-VALIDATION-STRATEGY).
6. **Inside Piping:**
   - its `AGENTS.md` and `LOOP_INIT.md`. The loop's basis is `docs/PRD.md`, which is unchanged;
   - its coordination and decomposition pointers;
   - T3's records;
   - T4's `PRESSURE_STRESS_T4/` on the T4 branch.
7. **Piping consumers** that name the files.

The hits are history or identity only:
- earlier tranche manifests;
- agent run records;
- the 2026-09-21 reconciliation snapshot;
- `_Evaluation/PHYSICS_AUDIT_2026-09-05`;
- a 2026-07-28 evaluation script;
- two dated surveys;
- the manual-v7 source record, which inspected `TYPES.md` for checking candidacy;
- Piping's DAG and dependency rows, which name the documents by identity;
- `capability_inventory.json`, which binds `VALIDATION_STRATEGY.md`'s old hash to revision `eec2855d82` and checks it only at that revision.

T4 cites none of the documents. ROOT may still want to tell T4's row as a courtesy, since T4 will later extend these statements. That would not be a D-11 notice.

## 5. Gates

- **Both screens, before each commit:**
  - `t3_host_screen.py --staged`: 0 hits on 4 files at `3b1d870227`, and on 1 file at each of `ca415e282d` and `f995add7c6`.
  - `validate_private_terms.py --from-host --staged`: PASS, 0 findings, at all three commits.
  - The range screen `--base 7b2715cb0e --head HEAD`: PASS (`screens_and_claims_lint.txt`).
- **GEN-8** (`pytest tools/practitioner_harness/test_live_baseline.py -k gen8`, through `WT/tools/t3_slot.sh`):
  - **Pending at the time of writing.** It has been queued since 03:10Z behind the exclusive DEC-025 of U3's exact head. I did not signal any job.
  - The result is added to `_run_records/gen8.txt`, and to this section in my final report, when it completes.
  - The four changed files hold no machine-absolute path, and every check above that scans for one passes.

## 6. Questions for WORKING_ITEMS

- **Q1: the two documents named in the authorization but left unchanged.** The owner's authorization names five documents, following RV127 A1-N-2. The correction changes three.
  - `INTENT.md` (`:175`, `:182`) and `PRD.md:662` state intent and requirements, not current capability. RV127 also cited `SPEC.md:599` and `VALIDATION_STRATEGY.md:50-51`, which are a requirement and a plan.
  - The retirement does not make any of them false, and the exact contract does publish pressure membrane stresses on straight members.
  - `PRD.md` is the piping loop's basis. It is amended through D, DEC and SCA instruments (`LOOP_INIT.md` "Decisions"; earlier PRD edits went through D-71, DEC-101 and SCA-010).
  - **Recommendation:** confirm that these stay unchanged. The PR body should then say plainly why INTENT and PRD do not change.
  - **If ROOT or the owner rules otherwise,** the smallest grounded addition, with no requirement removed, is one dated sentence after `INTENT.md:183`, and likewise after `PRD.md:665`'s list: "The legacy pressure contract is retired product-wide (owner decision "Owner decisions: the legacy pressure contract is retired product-wide; …"); pressure is solved only through the exact straight-pressure contract `2.0.0/exact_straight_pressure_v2`, within that contract's own qualifications." For PRD this would need its own D, DEC and SCA record.
- **Q2: pressure primitive loads.** `SPEC.md:538` ("Primitive loads include … pressure …"), `SPEC.md:540-545` and `TYPES.md:169` remain true of the schema and of the `primitive_loads` crate. The product, however, refuses every pressure primitive at solve, and new ones cannot be authored.
  - **Recommendation:** no change. They do not state a pressure stress or thrust capability.
  - **The alternative:** one added clause after `SPEC.md:538`: "A pressure primitive is refused on every solve route and cannot be newly authored (owner decision …); pressure is supplied only through the exact contract's pressure regions."
- **Q3: the RR citations do not yet resolve on main.**
  - The cited RR headings are at lines 16379 and 16521 of NUM's RR. Main's RR copy ends at line 15,660 and lacks them, and #1168 does not carry RR.
  - After #1168 merges, main has U3's change record, which quotes both headings (§2). RR itself reaches main only with a records PR.
  - **Recommendation:** land the records PR carrying RR before this PR merges, or note in the PR body that the headings resolve in NUM's RR until then.

## 7. Notes

- **Basis.** When WORKING_ITEMS merges main after #1168, the manifest's `basis` (`7b2715cb0e…`) stays truthful as the commit the tranche was cut from. Precedents keep the cut basis.
- **The independent review is pending.** WORKING_ITEMS dispatches it. The manifest has no `review:` entry yet, and one can be added as `PIPING-LOOP-INIT-20261005` did.
- **A wording note on U3's T2, not a defect.** Its "solved only on the exact straight-pressure profile" reads "profile" loosely: model 0.4.0's `resolved_straight_load_state_v1` also solves exact-contract pressure. The documents say "contract".
- **Scratch** is in `WT/scratch/i116_u5/`.
