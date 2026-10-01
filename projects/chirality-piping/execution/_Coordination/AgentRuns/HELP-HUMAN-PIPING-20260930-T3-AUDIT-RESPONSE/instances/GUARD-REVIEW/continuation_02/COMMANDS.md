# Commands and outcomes

All commands ran from the repository root; Run is the response AgentRuns path.
All reviewer writes are in this continuation. Python scripts importing local
modules used PYTHONDONTWRITEBYTECODE=1. No actual provider, guard, signal,
compiler, model, network, install or Git/index write ran in this review.

1. Read complete v2-to-v3 source diff, modified provider code, diagnostic,
   return, live proposal, reproducer/harness and all meaningful tests with
   cat/sed/nl/diff. Diff exit 1 denotes the expected source differences.
   Initial combined output truncation was replaced by bounded complete reads.
   AST comparison in SOURCE_SCOPE.json checks all prior named top-level
   definitions/provider methods; compile grammar and read_job are unchanged.
2. Run GUARD-IMPLEMENTATION/continuation_02/run_preserved_tests.py and
   test_exit_races.py after inspecting their capability fences. Raw logs:
   preserved-tests.log (111 pass), author-exit-tests.log (39 pass).
3. Run independent_native_checks.py: independent-native-results.json, 21
   separately implemented fake-native cases pass. Import/operation capability
   fences prohibit real process/native/signal operations. No author Scenario
   class supplies these fixtures.
4. Inspect local CLT MacOSX26.5 SDK libproc.h and sys/proc_info.h declarations.
   Read ROOT's native PID-list witness, recompute array/count facts and run
   check_native_witness.py through fake bindings: NATIVE_WITNESS_CHECKS.json,
   all six arrays accepted. An initial attempt hit FileNotFoundError while ROOT
   moved the draft witness into its provider_01 packet. rg --files located the
   new path; the corrected file-only replay passed. No failed read is a pass.
5. Read ROOT-B02-INCIDENT, A0 continuation_02/03, ROOT-A0-BUILD, DESIGN returns,
   grants, graph changes and conditional continuation_05 design records.
   Independently parse event chronology, result/sample counts and stored
   comparisons; hash 33 exact raw runtime files, binary and feature fingerprints.
   BUILD_AND_B_EVIDENCE_CHECKS.json retains results. No comparator/model/build
   or old audit execution occurred. Historical failed-call PID remains unknown.
6. Parse PORTABLE_EXPORT_REISSUE_01 and both complete private archived packets;
   verify original/current manifests and changed-file hashes. Recursively compare
   parsed JSON and require every changed leaf to match the documented canonical
   ancestor/root/Python path substitution. PORTABLE_REISSUE_CHECKS.json:
   24 original manifest entries intact; three files / 31 path-string leaves;
   no numerical/result transformation. Personal path strings are not copied
   into this new packet. All operations are file reads.
7. Read-only Git commands: git diff --stat/--name-status/--binary and git show
   <sha>:<path> for 888e3888→84843dbf and 84843dbf→325516a7. Exact full identities,
   path/blob inventories and binary-diff hashes are in the two scope JSONs.
   No full source diff copy is committed. No fetch/stage/ref/index change ran.
8. Standard-library checks parse all new JSON/JSONL and Python, and verify each
   manifest from its declared base. Historical delta: seven manifests /100
   entries, 67 JSON/JSONL, eight Python. Final delta: four manifests /27 entries,
   ten JSON, six Python; all final worktree bytes match candidate blobs.
   Rehash the 47 aliased source/runtime inputs in the additive fresh preservation
   record; all match. Current preservation is not backdated to the original run.
9. Seal REVIEW.md, CONTEXT.json, scripts/results/logs with a new SHA256SUMS.
   Prior review/author/live/incident packets are unchanged.

ROOT's staged/clean GEN-8 results and post-freeze quiet-swap refusal were relayed
by ROOT and are not re-witnessed here. The review authorizes no subsequent live
operation; its suitability assessment and open operational gate are in REVIEW.md.
