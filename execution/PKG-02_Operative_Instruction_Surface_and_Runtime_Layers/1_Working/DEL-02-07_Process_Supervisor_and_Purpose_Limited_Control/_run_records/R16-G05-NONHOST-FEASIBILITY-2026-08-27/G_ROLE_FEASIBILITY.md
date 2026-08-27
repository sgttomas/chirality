# R16 N3.4 — G-ROLE bounded feasibility evidence

- Date: 2026-08-27
- Node: `N3.4`
- Primary carrier: `DEL-02-07`
- Calibrated state: `SUPPORTED_FOR_DESIGN`
- Gate status: feasibility evidence only; `G-ROLE` has not passed
- Exact App Server payload SHA-256:
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`

## Exact-pin bounded-entry readback

In a fresh mode-`0700` disposable root
`/private/tmp/chirality-r16-g-role.JFUs2I`, the exact accepted App Server ran
under the same fail-closed no-network/no-real-home/no-securityd outer profile
used by N3.1 and N3.3. A sealed disposable configuration set:

```toml
[features]
multi_agent = false
multi_agent_v2 = false

[agents]
enabled = false
```

`features.plugins=false` was supplied only as a session flag. The App Server
exited `0`; stdout was `23028` bytes and stderr was empty. `config/read`
reported all four values exactly as proposed. `experimentalFeature/list`
also reported `multi_agent.enabled=false` and
`multi_agent_v2.enabled=false`.

| Transient observation | SHA-256 |
|---|---|
| bounded-entry `config.toml` bytes | `7ecb4ce52c88547713520226f63f993e5aa1c9d2d0e84424ac4f9de20cd2df14` |
| App Server JSONL stdout | `f1a57ac50e5212de068681e8e6463abce482ab1a563acbceaf7da78c5e5d3801` |
| App Server stderr (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| denied-egress stderr | `b66318a4e27ea144257f9cf29ff0ab556f6b196cbe531a5a1ebed9c305b47f49` |

This changes no production configuration. It establishes only that exact pin
0.149.0 accepts and reads back the proposed optional bounded-entry overlay.

## Evidence calibration

| Claim | Calibration | Result |
|---|---|---|
| hard outer filesystem/network/account/policy envelope | mechanism-proven for these probes by Seatbelt denial and clean disposable environment | supported for design |
| exact-pin three-switch bounded-entry overlay | configuration-asserted by `config/read` and feature listing | supported for design |
| ordinary native descendant availability in the current primary harness | mechanism-observed: the parent launched four independent bounded descendants and received their returns; no foreign-loop work was created | supported as current harness evidence only |
| those descendants' sealed Agent-2 non-delegation | instruction-asserted; their briefs prohibited delegation and the returned work disclosed none | not mechanical proof |
| exact App Server bounded-entry behavioral refusal to delegate | unavailable: no authenticated model turn or generated behavioral probe surface was authorized |
| Agent 2/TASK non-delegation as a general platform property | `UNAVAILABLE_UNDER_BOUNDS`; no mechanism proof exists |

## Verdict, limitations, and implication

`SUPPORTED_FOR_DESIGN` means the role split is representable without globally
disabling native delegation: the current primary harness can use ordinary
native descendants, while a distinct exact-pin worker configuration can read
back the three bounded-entry switches as false. This is not a claim that the
false values mechanically prevent every descendant path, and it is not a
G-ROLE pass.

The actual bounded-entry behavioral probe, authenticated turn execution,
generated schema/type confirmation, packaged worker isolation, and mechanical
Agent-2/TASK non-delegation remain `UNAVAILABLE_UNDER_BOUNDS`. Future
implementation must key worker reuse to role posture plus effective-config
digest, keep ordinary Agent 0/1 native delegation available, expose the
bounded entry only after a behavioral no-delegation sentinel, and continue to
label instruction-only non-delegation evidence as instruction-asserted.

No concurrency default, child allowlist, topology, account endpoint, model
endpoint, or turn endpoint was invented.
