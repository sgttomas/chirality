# Authority and effect map — TM-ROOT-112 implementation acceptance

RunID: `ROOT_TM112_IMPLEMENTATION_ACCEPTANCE_2026-08-04`
DecisionID: `ROOT-TM112-IMPLEMENTATION-ACCEPTANCE-01`
Selection: `FINAL-HASH-REPAIR`
Accountable human: Ryan Tufts
Decision date: 2026-08-04

## Ruling identity

The ruling of record is the complete signed content of
`OWNER_RETURN_TRANSCRIPT_2026-08-04.txt`:

- length: 913 bytes;
- SHA-256: `a10bda1c05fe1e1249a7efa266401ddf71752e4d9a8ab0448ec96251d5973046`;
- Git blob identity: `cf6ab819969d4f2e1fe2008e306ad1a49c86defa`.

The transcript is preserved verbatim, including capitalization, punctuation,
line wrapping, signature, and one terminal newline used by the carrier.

## Exact accepted product bytes

| Surface | Accepted SHA-256 | Current working byte match | `HEAD` byte match |
|---|---|---|---|
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` | yes | yes |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` | yes | yes |
| `runtime/tests/daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` | yes | yes |

Verification commit and current branch/remote tip at capture:
`fa60348f93fb74079d352cac93c5ff440ac71226`. The commit identity is evidence
of the checked byte state, not merge authority.

## Accepted effects

1. The exact three product blobs above are accepted as the Root
   TM-ROOT-112 `G2 + C1 + F1` graceful-stop repair.
2. The recorded Node 24 strict checks, adversarial 2/2, daemon 15/15,
   full-runtime 74/74, build, and fresh-backcheck evidence are accepted.
3. Node 22.19 execution remains an explicit unexecuted compatibility gap.
4. The ordinary Root-to-App notice is now authorized. It must name D-APP-88
   and TM-APP-036's mandatory non-blocking parity-rerun rider.

## Explicit non-effects

The ruling does not prove App R2 causality, prove process/SIGTERM behavior,
accept App parity, authorize a merge, or itself perform the downstream notice,
register, receipt, lifecycle, publication, or Git actions. Those effects remain
with their lawful downstream owners and gates.

## Basis packet

The source decision packet is
`execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/OWNER_IMPLEMENTATION_ACCEPTANCE_PACKET.md`,
SHA-256 `9db1c0341d82fe3146564a0ddbe64564ff0fc59c13dd80de991889a1324cd0e7`.
Its offered hashes, accepted evidence summary, residual gap, App-routing
condition, and excluded claims match the signed return exactly.
