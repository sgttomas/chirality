# Manager fan-in — PR761 daemon project reference repair

Verdict: `VALIDATED_PASS__ONE_FILE_POSTIMAGE_READY_FOR_CHANGE__PR_CI_REQUIRED`.

The isolated publication tree `/private/tmp/chirality-graceful-source-closure-20260908` changes exactly `projects/chirality-runtime/packages/daemon/tsconfig.json`. Preimage: 345 bytes, SHA-256 `3b14197e0ee6cc749515c27953f5f20138404f98323be386655a7c3a58122833`. Reviewed postimage: 394 bytes, SHA-256 `0bc20ec8bdb3348def4739751609e173745e12d8b4e6e346e78d692c173c2c9b`. The sole delta inserts the project reference `../native-admission` after `../core` and before `../engine-pi-omlx`.

Author manifest `06d3c306c4b808a7dfdd5ebaaab0433dd991d57cb319d117069c3223ad28c08a` and distinct reviewer manifest `15f50f48b827cf479d4ac0ea32fbe43c17681b85e00a523df0687a685a6d4f13` rehash. Static checks establish that daemon already declares `@chirality/native-admission`, native-admission references core and not daemon, both projects appear in the root solution, and the added edge is acyclic. All accepted Runtime R V3 members remain byte-identical, 29/29. The publication selection is therefore the accepted 29 paths plus this one reviewed integration postimage: 30 paths and 605,978 bytes.

This repair addresses PR761's sole reported terminal blocker, TS2307 at `packages/daemon/src/codex-worker.ts(143,51)`, on head `5bd5a63ef673d5fb5691a302020d16135534f516`. No build, test, dependency setup, native compilation, supplier read, account action, feature activation, or release occurred. The postimage is approved for CHANGE to commit and push; required PR CI must establish the clean-build result. This evidence extends publication integration only and does not accept new account functionality.

After handoff, Runtime identity work returns to safe pause. New instruction/workflow conformance remains unassessed and no product wave resumes.
