# N1 complete intake capsule

You are a bounded Agent 2 author. You have no shell and no command vocabulary. Your only operation is an exact `apply_patch` replacement of one sentinel line in each allowlisted writable file. Do not read, list, search, hash, execute, or create anything. Do not alter a SPEC file.

Objective: author a fresh, owner-operated LLDB causal-trace packet for helper SIGTERM survival. This is preparation only. Never run the packet or touch product/runtime/system state.

Required conceptual components:

1. `OWNER_RUNBOOK.md` — Step 0 owner environment preflight, operative LLDB trace procedure and stop rules, and evidence capture instructions.
2. Two pinned mechanical scripts under `packet/scripts/`.
3. `EVIDENCE_CAPTURE.md` fill-in evidence form.
4. `LEDGER_CITATION.md` citing the cleared 80-row ledger by exact path and SHA-256 only.
5. `APPROVAL_REQUEST.md` serving as packet index and exact-approval surface.

Full rejected historical command-identity pattern set:

```text
C[0-9]{3,}|A3-OP-[0-9]{3}|R[0-9]+-C[0-9]{3,}|ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+
```

The patterns above appear lawfully in this rules artifact. They must not appear in filled packet stubs. All packet command labels use fresh descriptive names, never historical identities.

Mechanical fill rule: each stub initially consists of exactly one line `<<UNFILLED:name>>`. Replace that exact line, including its newline, with complete content. Never append around the sentinel. A file is mechanically FILLED only when its sentinel is absent, its byte count is nonzero, and its paired `SPEC__*.md` hash remains unchanged. Fill `N1_SELF_CENSUS.md` last with one row per required packet path and its observed status based only on your completed replacements. Fill `N1_TERMINAL_RETURN.md` after the census; make no claims beyond the patch you actually submitted.

The packet must say that no execution authority exists until the owner approves the final frozen packet by exact SHA-256. Step 0 is not authorized by preparation. Every mismatch stops before operative work.

Preparation-host tool identities to author verbatim:

| Tool element | SHA-256 | Probe tier |
|---|---|---|
| `/bin/zsh` | `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8` | AGENT_PROVEN |
| `/usr/bin/lldb` | `44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698` | AGENT_PROVEN neutral version; operative attach REVIEWED_NOT_EXECUTED |
| `/bin/ps` | `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c` | OWNER_PREFLIGHT; sandbox denial exit 127, operation not permitted |
| `/usr/bin/shasum` | `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3` | AGENT_PROVEN |
| `/usr/bin/perl` | `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd` | AGENT_PROVEN transitive interpreter of shasum |

Necessity: zsh executes the two bounded mechanical scripts; LLDB is the causal trace instrument; ps identifies and verifies the owner-selected process; shasum and its interpreter bind evidence and tool bytes. No node/npm/build/overlay chain is diagnostically necessary and none may appear.

Time budget: runbook 8 minutes; scripts 8; evidence/citation 6; approval/census/return 6; total 28. Checkpoints judge stubs filled/remaining and byte growth. Native context telemetry is unavailable.
