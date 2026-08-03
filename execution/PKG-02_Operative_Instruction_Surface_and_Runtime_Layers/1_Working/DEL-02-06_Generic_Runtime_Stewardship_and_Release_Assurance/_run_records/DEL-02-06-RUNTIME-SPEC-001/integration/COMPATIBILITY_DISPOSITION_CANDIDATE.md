# Compatibility disposition candidate

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Status: `CANDIDATE_NOT_ADOPTED`
- Candidate disposition: `DELTA_REQUIRED_IF_RECOVERY_SPEC_IS_ADOPTED`

## Fact / candidate separation

Accepted fact: the exact Root compatibility identity value, grammar,
declaration point, comparison envelope, mismatch identifier, binding record,
and epoch-change criteria remain unresolved as TBD-001 through TBD-004 and
TBD-015. No current label may be inferred from route namespace, npm package
version, runtime fingerprint, source/release commit, or Tier-0 Flow-A.

Candidate judgment: adopting the recovery specification would change
consequential generic daemon/client semantics because it adds a
recovery-before-readiness gate, a durable accepted-turn classification,
machine-readable indeterminate/recovery behavior, and new no-admission
conditions visible to the affected Root CLI and App surfaces. Therefore the
N4 proposal is `DELTA`, not `NO_CHANGE`, subject to accountable-human review.
This candidate judgment does not choose a compatibility value or apply a
delta.

## Exact candidate disposition rules

1. If the recovery specification is not adopted, this N4 file has no
   compatibility effect and makes no `NO_CHANGE` ruling.
2. If it is adopted, the owner must accept an exact new compatibility identity
   and binding record before any implementation or affected-client work.
3. Exact equality remains the only permitted comparison. Range negotiation,
   downgrade, alternate daemon/runtime/model/transport, and inference from
   route success remain prohibited.
4. The binding record must connect the exact identity to exact contract bytes,
   source and release identities, affected-client accepted bases, conformance
   or migration evidence, proportionate regression evidence, and the later
   accountable-human release disposition.
5. Root owns the identity and generic semantics. Tier-0 may coordinate a
   Flow-A relationship but cannot amend Root semantics or supply the identity
   by implication.
6. Root CLI and App remain the only accepted `AFFECTED` clients in the current
   census. Piping and Tier-0 remain `NOT_AFFECTED`. PEC remains `UNRESOLVED`
   and gains no work, dependency, or closure veto.

## Held exact values

| Open item | Required exact later decision |
|---|---|
| TBD-001 / OD6-OPEN-001 | compatibility identity and grammar |
| TBD-002 / OD6-OPEN-002 | declaration/preflight locus and equality behavior |
| TBD-003 / OD6-OPEN-003 | mismatch identifier, envelope, and presentation mapping |
| TBD-004 / OD6-OPEN-004 | complete identity-to-bytes/evidence/release binding |
| TBD-015 / OD6-OPEN-015 | accepted epoch-change/no-change criteria |

Verdict on this document is only: present the `DELTA` candidate to the owner.
No semantic adoption, runtime/client write, repin, lifecycle, release, or
reliance act occurs here.
