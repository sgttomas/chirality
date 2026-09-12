PASS — the prior P2 is repaired, and no actionable finding remains.

Reviewed **all 104 changed files** in `85f19f019589b798331c804c4b206e34849eeab5..3ad6fac0d75ad95f176269e4558f46617194e1f1`, including every source, test, instruction, documentation, and evidence change. This combines this reviewer’s earlier complete coverage with all 20 subsequent changed paths and connecting code; no exclusions. HEAD matches the candidate.

- Product defaults now resolve correctly for ordinary development, source overrides, staged overrides, and packaged launches. Distinct-content fixtures exercise initialization and restoration.
- Instruction refresh requires verified idle cold resume, then acknowledged developer-history injection before `turn/start`. Failed or uncertain acknowledgment leaves the user turn unstarted and forces safe reassessment on retry. Captured injection text/hash accompanies acceptance evidence. The stock implementation flushes injected history before acknowledgment. [Supplier source](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/core/src/codex_thread.rs).
- Native role files retain captured common guidance and the intended full role. Prior bytes, native project discovery, user configuration, and conversation history remain preserved.
- Earlier submission correlation, atomic attachment matching, replay isolation, pre-POST plan persistence, cancellation, shutdown classification, and panel-width repairs remain intact.
- Public updates retain exact source/destination validation, downgrade prevention, bounded failures, and explicit browser handoff. Report issue uses the existing external-browser policy without attaching conversation or account data.

Verification: scope validator **PASS, 104 paths, zero violations**. Incremental whitespace check passes; the full range retains only the disclosed historical Markdown hard break. Read filtered final logs: **342 Runtime tests passed; 2185 frontend tests passed, four skipped**. Typecheck log contains no diagnostics; parent reports successful frontend/Electron and Runtime typechecks. No suites or live actions repeated.

The parent’s recorded native checks now demonstrate edited guidance in the existing chat after restart and without restart, plus delivery to a fresh TASK child. Those observations are distinct from controlled tests; prior failures remain preserved.

Residual limits remain: raw-daemon cancellation and earlier timing observations are not independently repaired; service-loss evidence covers graceful SIGTERM. Replacement packaging, owner install-over acceptance, notarization, and publishing remain separate.

Independent read-only TASK, software-code-review, gpt-6-astra/high. No authorship, writes, Git mutations, private-state access, App actions, signals, or delegation. Suitable for manager fan-in; not owner or release approval.
