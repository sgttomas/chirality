# W04–06 independent semantic review

**Verdict: FAIL — one blocking derivative finding remains (F1b).** Production semantic repairs pass this bounded review; this is not an overall R5 closeout, product qualification, lifecycle acceptance or code-check waiver.

Reviewer: `/root/app_record_repair_manager/review_04_06`, fresh TASK via delegated harness, no descendants. Basis: HEAD `1b5adbf50142a4c01c454c62a31dfcdc60da1894`. Scope: all 16 DELs in PKG04–06, complete changed-block diff and per-key derivative; 486 changed units across 83 manifest source paths, 682 original residual keys plus two SOW-079 extension rows. Read-only production review; this report is the only reviewer write.

Own APP-HOLD-1 reliance preflight: all 16 ALLOW, exit 0, before reliance; hold register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`, scan fingerprint `68b88e611cd7b0ebfa61dc15aa1e3910a01da286ea7e0d9212ef46ea2b1ac675`. This is distinct from the manager dispatch check.

## Blocking finding

**F1b — P1, blocking: completed record-only keys still inherit package-wide delivery work.** In `W04_06_ROWS.csv`, the following original RECORD_REPAIR keys remain DELIVERY_TASK without a precise account of the completed record edit or a distinct surviving atomic obligation:

- DEL-04-01#CLM-025
- DEL-04-02#CLM-031; DEL-04-02#STATE-1
- DEL-04-04#CLM-028
- DEL-05-01#CLM-010.4; DEL-05-01#CLM-013
- DEL-05-03#CLM-005; DEL-05-03#CLM-009; DEL-05-03#CLM-013
- DEL-06-06#STATE-2

The clearest cases are DEL-04-02#CLM-031 and DEL-04-04#CLM-028: their original work is closing/restating a conflict entry with an obsolete MATCH premise; the derivative substitutes max-turn/configuration work or organisation-layer implementation for that key. DEL-04-02#STATE-1 and DEL-06-06#STATE-2 similarly concern writing current records already changed by this tranche. This prevents exact completion accounting and appears to defer authorized record repair into product delivery. Mark purely documentary obligations repaired and cross-reference separate live keys. For genuinely mixed keys, explicitly state the completed record repair and the specific surviving duty; DEL-05-03#CLM-013, for example, may retain the external-transcript guarantee question without inheriting the entire sink implementation package. Do not alter the frozen original columns. Exact findings were routed to author and manager; no further production edit is requested for F1b.

## Completed repair backcheck

| Finding | Initial severity | Final status |
|---|---|---|
| F1: register duties mislabeled as D-APP-38 hash work; broad replay duties and omitted local prerequisites | P1 | Repaired: exact formal boundaries, narrowed replay rows and surviving local gates restored; F1b above remains separately open |
| F2: DEL-05-05 distinct medium-band deferral erased | P1 | Repaired across output, requirements/checks, context/memory, Remaining and derivative; D-APP-56 R4-P08 remains deferred and current thresholds stay actionable |
| F3: DEL-06-06 exactly-one/noncontradictory terminal criterion lost | P1 | Repaired, including completion/Stop race and named live-store fixture |
| F4: stale OUT-001 contracts contradicted current requirements | P1 | All 16 outputs/current matrices repaired, including DEL-04-01 SOW-079 trace |
| F5: untouched metadata/formal edits falsely called repaired | P1 | Routed truthfully to owning manager; P45 history label and DEP-05-01-006 snapshot repaired; DEL-05-05 conditional repin explicitly not triggered by unchanged scope |

## Coverage and limits

Full semantic coverage includes changed claim blocks, atomic requirements, named checks, outputs, AC/VER and trace matrices, contexts, Remaining, memory additions, dependency indices and all derivative keys. Identical repeated boilerplate was compared once per distinct form, with each block bound by its independently recomputed hash. No changed CLM block is missing from the manifest. Every original key occurs exactly once and every original field matches frozen R5 bytes; no original key was erased. Current counts at review: 338 REPAIRED, 342 DELIVERY_TASK, 1 ALREADY_RESOLVED, 1 DEFERRED_OPTIONAL.

All 486 old/new unit hashes independently match HEAD/current bytes; whitespace check passes. All 16 MEMORY historical prefixes and all _STATUS bytes outside Remaining are intact. The 193 descriptive dependency rows preserve the unchanged formal CSV status/satisfaction; formal CSVs are not changed by this author. Accepted basis pins, lifecycle and approval identity remain preserved. Protected tests and product implementation were not modified by this slice. No product test, native/off-code outcome or verification completion is asserted by this review.

D-GOV-43/A2 and D-APP-127 lift current obligations without treating existing code as authority to retire them. D-APP-132's scoped P01 release is respected; no new hidden tool access or domain-stage waiver appears. SOW-079/CLM-032 is seated inside the already accepted DEL-04-01 owner. Live source limitations, max-turn, structural redaction/artifacts, current-threshold metadata, native scope/timeout evidence, migration/replay and exact terminal checks remain concrete. Distinct medium-band adoption and optional D-APP-116 inventory/cleanup are not silently activated.

Manager integration remains necessary: **19 formal dependency duties** in `W04_06_FORMAL_BOUNDARIES.csv` and **6 status metadata duties** in `W04_06_STATUS_METADATA_BOUNDARIES.csv` are record work, not product-code gaps. Apply and independently backcheck these before overall record-repair closeout. This review does not establish their completion or dependency satisfaction. The separate manager D-APP-38 v24 pass is not reopened merely for expected reference metadata changes; the authorized path-based REF-ID collision fix preserves source identity/accepted hashes.

## Hash binding

Hashes are SHA-256. Production aggregate is UTF-8, sorted unique manifest SourcePath, each encoded as `path + NUL + full-file SHA256 + LF`:

`c7471f09dbd4dcf22b89b99f2390aaa0e57494b9a50b52427101eabe292efda3`

| Evidence | SHA-256 |
|---|---|
| W04_06_CHANGES.csv | `7b6530d260d74e59eab070a8bf70a6f0b3da21d6fb467b69e5af63db387b8035` |
| W04_06_ROWS.csv | `8371d948a4404e139f4fa447427753f66dbcab18bcaf3f963cacd2e12130f996` |
| W04_06_EXTENSION_ROWS.csv | `8fbfd1679e59afb8794480dbfadb5b70c59990f96c8ec604ceb2e8c2e8f3128f` |
| W04_06_FORMAL_BOUNDARIES.csv | `ca3294b360b2c41a792e14c47a1bf8c76d7c7c4184103d778cef84490dfcfe29` |
| W04_06_STATUS_METADATA_BOUNDARIES.csv | `e570e8f5a2af23a4cf31c5590950dc3d35ac55ee275040f4b6684ef5af32c09b` |
| W04_06_REFID_MAP.csv | `794995bb3498b6a82849ab164a4e5c19a510dfad80fda702b0e69e88e06325e8` |

Instruction/method origins actually consulted (source-qualified workflow: `bundled:chirality-root/reconciliation`, R5/R6):

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/chirality-app-dev/AGENTS.md` | `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f` |
| `workflows/reconciliation/WORKFLOW.md` | `75948a77e7ee3ebd9cd9d8a2089c9aff75ca76b49d87260793e6fbdd152fa380` |
| `workflows/reconciliation/resources/contract.md` | `36eb3a4454e384fae7ea3e5d60dda2f9d63e9b7c2e7758c40048f00cb422b2fb` |
| `workflows/reconciliation/resources/method.md` | `f1c8f54909c0ae4341d53391cb4a96fe377dfc1f167c00b1159d15eab079ea16` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-131_APPLICATION_R5_R6_AGENT0_2026-09-22.md` | `37a3dd3798af7c8d8ce5ea21b2b5d9dac22b452c8473c260fbafbb5a219de097` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-132_RULING_P01_AND_AGENT0_DISPOSITIONS_2026-09-22.md` | `d52dd0f59913961312572ff41dadc37cb203efc8838b408277b2b4a61048c8a3` |
