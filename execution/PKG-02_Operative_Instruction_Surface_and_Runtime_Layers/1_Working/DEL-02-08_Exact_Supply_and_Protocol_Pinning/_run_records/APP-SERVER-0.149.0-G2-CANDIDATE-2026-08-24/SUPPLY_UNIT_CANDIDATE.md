# App Server 0.149.0 Supply-Unit Candidate

**State:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

**Assembly verdict:** `PASS_WITH_DOCUMENTED_GAPS`

## Exact unit offered for decision

The official `openai/codex` release `rust-v0.149.0` remains published and
offers the three ruled macOS arm64 assets. Their exact archive identities are:

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `codex-app-server-aarch64-apple-darwin.tar.gz` | `71843308` | `35892a576ec29edbbb766cfba002c57c7beea479c6c21715a134cab4a7352032` |
| `codex-app-server-aarch64-apple-darwin.zst` | `50359498` | `c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677` |
| `codex-app-server-package-aarch64-apple-darwin.tar.gz` | `93775517` | `aaa3751edfab80b887dbd1ca709c87a16495238e1f1a86cbcbbbb5a34e2b31a2` |

All three contain the same `179721344`-byte arm64 App Server payload,
SHA-256 `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`.
Both alternate payload comparisons returned `cmp` exit `0` against the
independently reverified primary, and the alternates compare equal to each
other.

The package variant additionally contains three frozen ancillary executables:
`codex-code-mode-host` (`8f9f6969…`), `rg` (`b4a0ff40…`), and `zsh`
(`4707e28b…`). Only the code-mode host was executed, solely for help/entrypoint
inventory; it exposed only `--listen`. The generic search and shell members
were not run because they cannot produce the evidence R14-B names.

## Supply, signature, and redistribution findings

The payload is Mach-O arm64 for macOS, minimum macOS 11.0, SDK 15.5, and
identifies at runtime as `codex-app-server 0.149.0`.

Its embedded signature has Team Identifier `2DC432GLL2` and hardened runtime,
but `codesign --verify --deep --strict` returns `invalid signature (code or
signature have been modified)`, the binary carries an invalid entitlements
blob, and `spctl` returns exit `1`. The same exact R13-admitted class occurs
across all three byte-identical App Server copies. This is recorded supply
inventory under R13; it is not a valid-signature or reliance claim.

The exact-tag license is Apache-2.0, 10,926 bytes, SHA-256
`d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc`.
The exact-tag `NOTICE` is 242 bytes, SHA-256
`9d71575ecfd9a843fc1677b0efb08053c6ba9fd686a0de1a6f5382fd3c220915`.
Neither is included in the release archives. A future redistribution package
must add the license and carry applicable notice/attribution obligations; this
packet authorizes no redistribution.

## Exact-pin empirical result

Every vendor invocation passed a binary-identity gate, the network-deny
profile gate (`17a57916…`), and a sandboxed network-denial preflight. Ten
bounded runs produced version/help, configuration readback, precedence,
feature inventory, negative schema/type probes, and ancillary help evidence.

The unmanaged disposable host returned `configRequirements/read = null`.
The user layer made command networking off and the project fixture was
disabled as untrusted. Session flags overrode user configuration. In
particular, the user layer read `features.multi_agent=true`,
`features.multi_agent_v2=false`, and `agents.enabled=false`; the session layer
read `false`, `true`, and `true` respectively, each with `sessionFlags` origin.
Thus exact-pin `multi_agent_v2` existence and session-over-user precedence are
observed. No trusted-project precedence claim is made from the untrusted
fixture.

The complete two-page inventory contains 118 features: 38 `stable`, 2 `beta`,
41 `underDevelopment`, 3 `deprecated`, and 34 `removed`. The baseline run had
42 enabled entries and 42 default-enabled entries. The authoritative full
entry list is `03_EMPIRICAL_EVIDENCE/FEATURE_INVENTORY.json` at SHA-256
`21a1aa2825fdcadf3f87379a4d456cd338c9af2dc8bee4defeb1e27e5997003d`.

## Plugin synchronization and egress

Exact 0.149.0 exposes `features.plugins`, a stable whole-plugin feature with
baseline `enabled=true` and `defaultEnabled=true`. `config/read` omits the
literal field at default. The explicit session override
`-c features.plugins=false` reads back `false` and suppresses every observed
plugin-startup attempt. This is not a curated-only sub-switch. Current official
configuration documentation names no dedicated curated-sync switch.

With the baseline enabled, the sandbox denied three attempts:

1. `https://chatgpt.com/backend-api/plugins/featured?platform=codex` — warming
   the featured-plugin ID cache;
2. `https://api.github.com/repos/openai/plugins` — curated GitHub HTTP sync
   after local `git` was unavailable; and
3. `https://chatgpt.com/backend-api/plugins/export/curated` — curated export
   archive fallback.

All returned `SANDBOX_DENIED_NO_COMPLETED_CONNECTION`. The configured remote
control base `https://chatgpt.com/backend-api/` was logged but not attempted;
the process waited for authentication without prompting. Across the runs there
were zero completed connections, credential prompts, login/device flows,
approval grants, `auth.json` files, or writes outside the disposable tree.

## Documented evidence gaps

Generated JSON schema, generated TypeScript types, and the resulting
schema-derived exhaustive method inventory are each
`UNAVAILABLE_UNDER_BOUNDS`. Current documentation describes wrapper commands,
but the pinned dedicated server rejects `generate-json-schema` and
`generate-ts`, and the only relevant package ancillary executable exposes no
such command. R14-B prohibits obtaining or executing a different binary. The
observed bounded method inventory remains in
`03_EMPIRICAL_EVIDENCE/METHOD_CONFIG_FEATURE_MATRIX.md`; it is not promoted to
an exhaustive schema-derived inventory.

## Named G5 open finding — R13-B

The plan fails G5 on an invalid nested signature; 0.149.0 App Server's vendor
signature is invalid as published per `openai/codex#37725` and R13. G5 requires
a corrected artifact or later owner ruling. G2 acceptance of this candidate
would not dispose that G5 finding.

## Candidate boundary

This packet does not record G2 acceptance or a pin amendment. It grants no G5
disposition, implementation, cutover, release, publication, reliance, App
adoption, or blocker/hold lift. TM-ROOT-106 and TM-ROOT-122 remain G1 blockers;
all ten existing DEL-02-06 bindings remain held and unchanged.
