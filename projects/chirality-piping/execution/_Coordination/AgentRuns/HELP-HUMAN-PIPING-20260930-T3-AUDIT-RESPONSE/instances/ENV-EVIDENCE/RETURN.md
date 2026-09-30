# RETURN — ENV-EVIDENCE read-only checkpoint

**Result: bounded investigation complete; full E0 runtime qualification remains
open. No heavy run is admitted.** Native TASK `/root/delivery_manager/env_evidence`
returns to DELIVERY `/root/delivery_manager`, under ROOT `/root`.

Basis: audit/source `3bddc2b05f6106e969c7cf43373b230845c7cc66`, planning
`5506e1f48db66f0119667c52058efa992ed14a5d`, activation/observed HEAD
`86bb36d6fb88e7699df595bce1d6a31f5fbd6be5` (tree
`616bee52ce7504e3a0c154d5f75efa82d46fcb3a`). The sealed brief hash matches
`8f3fa504c19e56f5b791c71ac86cfebbc6bce7935225af43b6dc49aeee6ee947`.
Instructions, read scopes and native addenda are recorded in CONTEXT.json.
The per-agent scope is prompt-only on the shared filesystem; host sandbox
permissions are the actual enforced boundary. No model diversity is claimed.

## Concrete returns

- **Runtime/guard:** `RUNTIME_GUARD_PROPOSAL.md` specifies an isolated response
  runtime, exact Rust 1.97.1 provisioning under response RUSTUP_HOME/CARGO_HOME,
  one target per slice/candidate, one global heavy workload, cargo `-j 1`,
  `RUST_TEST_THREADS=1`, one pytest worker, at-most-2-GiB initial observation
  ceilings and at-least-35% memory-reserve policy. The proposed guard uses an
  explicit PID/start-identity registry and dedicated process groups/sessions;
  it never chooses victims by command substrings. It requires live footprint,
  RSS, pressure and swap monitoring, calibrated stop latency, failure handling
  and later controlled validation. It preserves the binary heap backstop.
- **Actual environment:** `observations.json` and `runtime_inventory.json`.
  Rust 1.97.1 is absent; installed default is 1.92.0. No auto-install occurred.
  Python 3.13.7, Node 24.5.0, npm 11.5.2 and Apple Clang 21 are visible.
  Checked project venv/node_modules/target paths are absent. Coverage 7.15.0
  differs from the pinned 7.15.3. Dependencies are not yet qualified.
- **Snapshots and permissions:** local memory_pressure reported 16 GiB total
  and 68% system-wide free; disk had about 104.07 GiB available. vm_stat works;
  own-PID/relevant-job ps and sysctl memory/CPU/swap/pressure queries were
  denied in this TASK's default sandbox. ROOT separately supplied an approved
  host check: 8 CPUs, swap used 3118.19M of 4096.00M, own-shell process fields
  visible and time-l peaks available. ROOT_HOST_OBSERVATION.json is referenced
  and hashed. Those are ROOT's observations; a live guard remains unverified.
  Existing swap does not establish when pressure occurred or its cause.
- **Recovery:** `RECOVERY_LIST.md` and `evidence_inventory.json` name all six
  final Mac suite candidates and original locations/hashes. Their six manifests
  verify (85 entries); all six lack original per-manifest suite logs. Retained
  suite summaries describe 39 or 40 Cargo manifests each. The unsanitized
  SWEEP JSON hashes do not authenticate missing suite logs.
- **KF2:** original part-1 base/candidate JSONL files remain unavailable here,
  with full recorded hashes and sizes in the recovery list. Part 2's raw JSONL
  is present (four records) with four full output envelopes. All 54 checkpoint-B
  manifest entries verify. Reviewer instrumented JSONL is retained separately
  and does not replace the missing originals.
- **K4:** all seven pinned generator inputs exist and match their hardcoded
  hashes. Three inputs live under the dated execution tree omitted by the
  numerical CI sparse checkout. Generator execution was not attempted.

## Missing inputs and next safe action

DELIVERY should return the following to ROOT without granting a heavy slot:

1. Seal the response runtime location and an exact-1.97.1 provisioning scope,
   including package/locked-dependency verification. The default 1.92.0 is not
   proposed as a substitute. ROOT reports the official pinned manifest is
   available (HTTP HEAD 200); no download or installation has happened here.
2. Authorize a separate lightweight guard implementation/qualification slice
   and approved monitoring boundary. Validate process ownership/containment,
   live footprint and pressure/swap sampling, then controlled owned-process
   stops before a build or observation slot. No synthetic kill test occurred
   in this assignment.
3. Coordinate recovery of six original suite-log directories and KF2 part-1
   raw files from the M5 or backup. Verify original hashes before sanitizing;
   otherwise explicitly disposition missing evidence. No absent M5 directory
   is an M3 calibration, lost-evidence closure or project-readiness verdict.
4. After guard/runtime qualification, establish same-M3 base/candidate behavior
   and ascend through tiny/10/100-member cases. Required larger/full gates remain
   outstanding until separately admitted; the old failures, caps and timings
   are not adopted. K0/A1 source/proof work can proceed independently.

This checkpoint wrote only `Run/instances/ENV-EVIDENCE/**`. No source, historical
ruling, old manifest, Git/index state or other agent output was changed by this
TASK. No install/download/build, guard activation, process kill or delegation
was performed. Context and command provenance, evidence inventories and
SHA256SUMS make the return recoverable. The full graph E0 completion condition
is not met: runtime provisioning, live guard validation, memory admission and
same-host calibration remain required. No engineering acceptance, release,
dependency-satisfaction or deliverable-readiness claim is made.
