# Evidence recovery list — 2026-09-30

This is a recovery inventory, not a reconstruction of missing originals. No
original evidence was downloaded, copied from another host or regenerated.
Existing canonical records remain in place. Full paths, sizes and hashes are
in `evidence_inventory.json`. `T3` and `Run` follow the sealed brief.

`<M5_T3>` means the historical `<repo>/.claude/worktrees/swbpipe-control-layer-8a41be/.claude/t3`;
`<M5_VENV>` means the corresponding historical Piping `.venv`. Their absence
at the mapped paths in this checkout does not say whether the M5 machine or a
backup still holds them. The owner supplied that they are not available here.

## Six audited final Mac merge suites

All six canonical merge manifests verify: 85 entries total. Their retained
final `suites.log` files are count summaries, not the original per-manifest
logs. There are **zero raw `dec025/suites/*.log` files** in these six folders.
The summaries, comparisons, sanitized SWEEP JSON, metadata, sweep output and
Python/desktop surface logs remain available. This verifies preserved bytes;
it does not re-witness the historical tests.

| Slice | Final candidate | Retained Cargo suite-manifest count | Original recovery directory | Original unsanitized SWEEP JSON SHA256 |
|---|---|---:|---|---|
| K4 | `5a46a6278af3c857a52ecb9be6880990493190f8` | 39 | `<M5_T3>/scratch/sweep_k4/` | `9aabdee58f688eed9f0afd11f848b7761072fd75da85943c8dbf9526620daa12` |
| KF1 | `66adfede42de817efb5e0090342c02e3e4382f21` | 39 | `<M5_T3>/scratch/sweep_kf1/` | `99d5e121222a2b0f253db6cd2fa88e51343b61f1c55e58395c70c5ab50b6b44a` |
| VK | `5f0d394262516e4053322730506cb88dfb36a2f0` | 40 | `<M5_T3>/scratch/sweep_vk/` | `8a02119f9bccae13ebd59f18c43f6dc0c4302e23dd7fec7ac238d6899d3ac869` |
| K6B | `597c81ba4b3dcf9a1154ef438a3c827054a57ad9` | 40 | `<M5_T3>/scratch/sweep_k6b/` | `4cafcf7ace2d1c58a21a4ff64ebe7e83ba5b3a000a74069f69ecaf2b6ce8b04a` |
| KF3 | `aa83f67969c2f618034b856ba6e1fc13ae10762e` | 40 | `<M5_T3>/scratch/sweep_kf3/` | `b28a88cc58623c82d036950f0ba4c52c60348e425e650c94db92c461c3723904` |
| KF2 | `522167ac62f27ad999a4416d10b95f922ff8c665` | 40 | `<M5_T3>/scratch/sweep_kf2/` | `9b4d80026c9b3e0aede1a3f14ca910dac396a21cf975a75677e5c0f541c3e20b` |

For each row recover the complete original `suites/` directory, `suites.log`,
`meta.txt`, SWEEP JSON and any adjacent driver/control record from that M5
scratch directory or its backup. Match the head and timestamps to the retained
metadata. The recorded SHA above authenticates the **unsanitized SWEEP JSON**,
not any raw suite log. No original per-log hash is supplied by the inspected
merge manifests. Record those hashes only when originals are obtained; provenance
and metadata must distinguish recovered originals from later reruns. Preserve
raw bytes in a scoped evidence store, then create sanitized copies with separate
hashes and a transformation map. Do not change original manifests.

The M5 sweep directories are known locations from their merge records and the
handoff. `<M5_T3>/scratch/sweep_kf2/` was the preserved current M5 baseline under
the later handoff; it is not an M3 baseline and is not a pruning authorization.
If originals cannot be recovered, ROOT should disposition that exact loss
and limit replay claims. A new M3 rerun is new evidence and cannot replace an
original-hash recovery. The old three platform failures require same-M3
base/candidate re-establishment, not adoption as expected failures.

## KF2 raw gate evidence

Source: `T3/IMPLEMENTATION/KF2/_run_records/b/gate/uncommitted_sha256.txt`.
Original part-1 raw files are absent from the checked local record/runtime
locations. Their recorded identities are:

| Original location under `<M5_T3>/scratch/i20/b/gate/` | Bytes / records | Recorded SHA256 |
|---|---|---|
| `part1_base/runs.jsonl` | 605,711,611 bytes / 884 | `c42981e541650578a60efe48cbf346360fedbb4507b3d02365b5f5abb78e9f68` |
| `part1_cand/runs.jsonl` | 605,711,700 bytes / 884 | `11dfe8296681280e0fd4163ee3195cc16ff0f78f3ce81dff82516a520bf2ef3f` |

For each side the original `full/` directory contains 818 files and its sorted
per-file SHA-list digest is `a8fb70b932978b729d5897d41ef64e8d5c2b15eba2d2dbedfb5a65fed8dceb5b`.
Each `envelopes/` directory contains 818 files and has list digest
`32005949474219ce93cedae5020d4953bbfeba483ef33461fac15d9a44b6874f`.
These are hashes of lists, not hashes of directory archives. The lists require
their exact path/order/line-ending convention to validate; recover that convention
with the originals. The preserved `part1/index_base.tsv` and `index_cand.tsv`
retain per-run hashes, and the side-specific result JSON, schedules, host
samples, driver logs and gate/comparison summaries are present.

Recovery: obtain the two JSONL originals plus `full/`, `envelopes/` and `stderr/`
from M5 scratch/backup under a separately scoped transfer. Verify JSONL hash,
byte count and record count before sanitization; compare envelope indexes and
list hashes where their serialization convention is known. Preserve originals
and distinct sanitized hashes. No fabricated byte stream or regenerated request
counts as recovery. Missing items stay explicitly unavailable if no source exists.

The part-1 lack does **not** extend to all KF2 raw evidence:
`T3/IMPLEMENTATION/KF2/_run_records/b/gate/part2/runs.jsonl` is present, with four
records (592,845 bytes), alongside four full envelopes. All 54 checkpoint-B
manifest entries verify. The reviewer also retained `instr_part1_candidate.jsonl`
and `instr_n10_chain_rot.jsonl`; they are independent instrumented observations,
not the missing original base/candidate JSONL files. Their hashes are inventoried.

## K4 pinned generator dependencies

Static AST inspection of `FK/tests/retained_k4/gen_k4_vectors.py` identified
seven pins; all seven current file hashes equal the hardcoded expected values.
No import, generation or `--check` run was performed.

| Input | Current SHA256 (= expected pin) | Requires dated execution tree |
|---|---|---|
| `projects/chirality-piping/core/solver/frame_kernel/tests/retained_wide_k3/gen_wide_k3_vectors.py` | `ca48d1bd65540eb3da7f30acbbdd4fa553fe03fed432f2b18afd960e2ba4da29` | no |
| `projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/REFERENCES/references.py` | `80d473a7351e92a2a903d233b9e633aac794aeff07f3ac41e40d25a0d94fc8a8` | yes |
| `projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/REFERENCES/references.json` | `7b176dbbf2296be02d8bca19c698ee56d0d5753751150a9175e0d3ad4cf89cc9` | yes |
| `projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3/DESIGN_NUMERICS/_run_records/floor_kinds.json` | `8326561530598e1f6b69d9f174b70946e52800373b5ecab48864ae174087ae78` | yes |
| `projects/chirality-piping/core/solver/nonlinear_integration/src/structural_adapter/kd5_models.rs` | `17a4680c83ff3e940a7dcfd908ef334c8b5a53427b6ff388dafb5888477dca23` | no |
| `projects/chirality-piping/core/solver/nonlinear_integration/src/structural_adapter/k2b_models.rs` | `c23eedd273ebacd4d3d324bb24e72cbe766b33d2768c8808e5f9d51674c63090` | no |
| `projects/chirality-piping/validation/benchmarks/numerical_integrity/fixtures.json` | `c061d73481d2ad137f7cef988475721681131789ec222e3e93c5ed3836b2910e` | no |

The numerical CI sparse checkout in `.github/workflows/piping-desktop-e2e.yml`
excludes `projects/*/execution/`, which removes R1 Python/JSON and floor-kinds
inputs from that checkout. The full local checkout has them. A green cargo job
does not establish that this generator ran or can rerun from the sparse tree.

Next action: include these pinned bytes and their provenance in any sealed
offline K4 rerun packet. Keep the current canonical copies; any move to maintained
tooling copies or CI checkout amendment belongs to a separately authorized
tooling slice with parity/hash checks. No change is necessary merely to inventory
them, and none is made here.

## Limits and return path

The search covered the six named merge folders, KF2 checkpoint B and reviewer
gate records, the seven K4 pins, and exact plausible project-owned runtime paths.
It did not search unrelated personal directories or every checkout on the disk.
No absent directory establishes project readiness, lost-evidence closure or a
satisfied production dependency. DELIVERY/ROOT own recovery coordination and
any acceptance/disposition of unavailable originals.
