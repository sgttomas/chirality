# Phase-B record-only EOF repair validation activation

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ChildInstanceID: `A2-PKG09-R20-PHASEB-REPAIR-VALIDATE-04`.
- Role: delegated-harness-native ephemeral-generalist Agent 2; role and non-delegation are instruction-asserted and not mechanically enforced. No delegation occurred.
- Authority: exact owner approval in `CHAT_TRANSCRIPTION.md`, `AMENDMENT_05_RECORD_ONLY_EOF_REPAIR.md`, `ORCHESTRATION_PLAN_V7.md`, `WORK_GRAPH_V7.json`, and the sealed brief.
- Objective: verify the exact three VALIDATE-02 preimages and tails, remove exactly one final LF from each, prove reversible one-byte lineage, and run only VALIDATE-03's still-unreached gates.
- Write scope: the three named VALIDATE-02 files and this instance directory only.
- Hard fences: no prior or one-shot command rerun; no shared R20/status/TM, source, test, package, raw evidence, runtime telemetry, manager, proof, Git, Receipt, network, GUI, operator, owner R19 Desktop evidence, or private-root-content action.
- Accepted source basis: branch `codex/app-login-proof-r20-repair`; HEAD/PROOF_REVISION `cb008dc5d6aa9b249639c91f3453a18609530d0f`; parent `a702dd6ec5005b361c8c023b12b599a425e5e2b8`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- Preimage checks passed: ACTIVATION 1,668 bytes / `3c50905cd730925da6ccf9374b8880a09c48b893b2ac2effb5795f2789ec2cb2`; RETURN 5,937 bytes / `9620af4620e4cbaae32ce22e06b2cc214b81149fc67542a2d340278ce322caaf`; VALIDATION 8,126 bytes / `ef06190377bbba777089b70635575ff3e67642fadbf62eb40f3b161d6cd76440`. Every preimage ended in exact bytes `0a0a`.
- Prospective postimage prefix hashes: ACTIVATION `0eee8bf6ceb539797c418fc55411c8fbda2f6ee1c981bb7950bdf14e4c59e9bb`; RETURN `6257fccadf4062d7549b512abea5eebb0abcc5a4edfb69ee9021ecee564c80d3`; VALIDATION `d1a4f7788ed1a4b5fd865be4abc992ff1625134b38ae73327ce75f5c52c04d34`. Before mutation, each prospective postimage plus one LF compared byte-for-byte equal to its preimage.
- Immutable prechecks passed: historical executor RETURN 16,439 bytes / `7d3b2ad4f49c2316dce7e1878ca4426ab5cb367e64a385ea2ee3137b37a5d399`; raw pack log 15,852 bytes / `d462b1efa4ab63a400b8e2efc96bd3b59a8eb9a0e173a6ff887aa9cb6f9fbdd2`; all 15 accepted raw-log path/byte/hash identities; R20/status/TM `bc9d39ba804c59a4a1cc7b1b5de39785288e2fe6a8539ca2e3936c99c118303c` / `6c864ceebd8769c47519a3fba338dc2932667efa6ad590bc1fd25b62851feb48` / `45f164a70a54d6333f8c0be63deabef2d24b1739b4d3d48a380bdd2594726ab8`.
