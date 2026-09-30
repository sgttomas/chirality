# Read/command provenance

All commands were run from the Git-derived repository root. `CONTEXT.json`
records 68 input origins, hashes and read scopes; mechanical evidence inventory
hashes are in `evidence_inventory.json`. No toolchain probe preceded DELIVERY's
`RUSTUP_AUTO_INSTALL=0` addendum. Native `collaboration.list_agents` for
`/root/delivery_manager/env_evidence` returned that exact agent name, running.
No child was spawned. Parent communications used native collaboration only.

## Executed inventory commands and durable outputs

- `git rev-parse --show-toplevel`: success; establishes `<REPO_ROOT>`.
- `python3 -B Run/instances/ENV-EVIDENCE/collect_readonly.py`: success.
  The exact underlying argv, timestamps, environment overrides, return codes,
  stdout/stderr and raw-output hashes are in `observations.json`; supplementary
  Python package metadata and exact runtime-path checks are in
  `runtime_inventory.json`. Package metadata was read via importlib.metadata;
  numpy/scipy or other heavy packages were not imported. No pytest was run.
- `python3 -B Run/instances/ENV-EVIDENCE/inventory_evidence.py`: success.
  Script retains the exact bounded traversal, static AST pin parsing and
  streaming hash method. Output is `evidence_inventory.json`. All six merge
  manifests and KF2 B's manifest matched, and all seven K4 pins matched.
  This is integrity/existence checking, not execution of a generator or gate.
- `python3 -B Run/instances/ENV-EVIDENCE/write_provenance.py`: success;
  sealed brief hash equalled supplied `8f3fa504...947`, 68 context entries.
- Supplemental `python3 -B` with importlib.metadata.version for coverage and
  pyyaml printed `coverage 7.15.0` and `pyyaml 6.0.3`. Those results are appended
  under `supplemental_package_metadata` in runtime_inventory.json.

Host-install paths in the durable command outputs were normalized to the
aliases described in runtime_inventory.json. Raw stdout/stderr hashes remain
hashes of the unsanitized returned text. The collector source subsequently
received the same alias normalization for repeatability; its final checksum is
in SHA256SUMS. Its initial execution predates that formatting-only change.
No raw local path is necessary to recover the missing M5 evidence. Standard
OS executable paths and the collector's generic alias replacement literals
remain in script source; they are not user-specific path disclosures.

## Source reads and bounded search

The initial source-read commands were `cat` of Root/project/TASK instructions
and the sealed brief; then `cat` of ACTIVATION, PLANNING_BASIS, graph and the
three T3 handoff/operating records. One combined source read exceeded the tool
output budget. Necessary graph, audit environment/replay, handoff §§0/5/6/9
and operating-note §§4/8 passages were then explicitly retrieved with `sed`.
Read scopes in CONTEXT do not claim that truncated text was fully inspected.

Subsequent successful `cat`/`sed` reads covered requirements-dev, project and
desktop package.json, K4 generator lines 1-160, numerical CI lines 155-205,
KF2 merge record, KF2 B INDEX/part-1 SUMMARY/uncommitted hashes, archived
DEC-025 driver, H allocator lines 1-145 and observer main lines 480-550.
ROOT_HOST_OBSERVATION.json was read in full and hashed as supplied evidence.
ROOT's HTTP HEAD observation is retained verbatim in CONTEXT as a native
message from DELIVERY; ENV-EVIDENCE did not repeat that network request.

`rg --files` and bounded `rg -n` were used for the T3 merge/gate files,
project runtime/configuration names, generator/environment terms and relevant
allocator/backstop source. A filesystem inventory prints file names/sizes,
then inventory_evidence.py reads the precisely named files. No home-directory,
other-worktree or whole-disk search was performed.

Visible non-success/truncated discovery attempts (all corrected by narrower
reads where needed):

- `command -v` over the requested tools returned 1 because python, cmake,
  ninja and pkg-config were not found; found tools were printed. Per-tool
  final results are retained in runtime_inventory.json.
- `rg --files ... projects/chirality-piping .codex .claude` returned 2 because
  `.codex` and `.claude` do not exist here. It still listed project manifests.
- A large `rg --files T3 | rg '(K4_MERGE|...|KF2)'` listing was truncated.
  Narrow subsequent pathlib inventories replaced reliance on that output.
- `rg -n` for gate/hash terms across KF2 B accidentally encountered long JSON
  lines and was truncated; only subsequent named text files and mechanical
  inventories support recovery conclusions. No full large JSON content was
  claimed inspected from that output.
- A search naming KF2 B README.md returned 2 (no such file); B uses INDEX.txt,
  which was read successfully.
- A shell glob `numerical_robustness/*.py` had no matches; the following rg did
  not run in that attempt. A subsequent search named a nonexistent VR tools/
  directory and returned 2 while producing valid H hits. `rg --files` then
  located VR runner/ scripts; no VR runtime check was performed.
- A guessed PLATFORM_CALIBRATION_MAC/run_suites_nff.sh.txt path was absent;
  `sed` returned 1. The archived DEC-025 driver actually references the old
  scratch `run_suites_nff.sh`; no substituted driver was executed. The retained
  calibration suite-script/excerpt names were discovered but not used as fresh
  evidence of final candidate suite identities.
- A selected metadata-term `rg` returned 1 (no matches); a small Python reader
  then printed the exact six meta.txt, sweep hash and summary headers and the
  absence of suites/ directories.
- `rg --files` for toolchain/requirements/lock filenames at repository level
  also returned names from other projects; those contents were not loaded.

None of these unavailable queries or absent paths is treated as a passing
check. Default-sandbox ps/sysctl denials are in observations.json. No escalation
was requested by this TASK. ROOT's separately approved query demonstrates a
possible future host boundary, not a guard already running under this one.

## Writes and verification

Explicit writes are confined to this ENV-EVIDENCE folder. They consist of
three read-only inventory/provenance scripts, JSON records, this read log,
RETURN, runtime/guard proposal, recovery list and a new SHA256SUMS.
There was no install, download, build, product/source edit, guard activation,
process termination, synthetic kill test, Git/index mutation or delegation.
No broader host write audit is claimed. Other agents share the filesystem;
changes elsewhere belong to their separate scopes and were not altered.

Final local checks parse every output JSON and Python source (AST only),
check the sealed brief hash, summarize the independently recomputed evidence
checks, and verify the packet manifest. These checks do not satisfy any
product, native-host or heavy-run gate. The packet needs ROOT's normal
independent review before integration.
