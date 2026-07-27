# A2-BASIS-53 terminal return

- **Basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
- **Mode:** read-only ephemeral Agent 2
- **Repository writes:** none

## Result

The complete census contains 53 `ScopeOfWork.md` contracts: 51 are
decomposition-derived and two are PKG-00 control contracts. All 53 associated
status files report `IN_PROGRESS`.

Six decomposition-derived contracts declare the unresolvable commit
`416b29033bbacb0bc3648d84033272b7ab4e6e11`. They are exactly the six targets
held by APP-HOLD-1: `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-05-04`,
`DEL-08-02`, and `DEL-08-03`. Their historical authoring basis is UNKNOWN.
The similar-looking reachable commit must not be substituted as provenance.

The other 47 declared commits and paths resolve. The two PKG-00 controls pin
their package-control README and match its current bytes. The 45 remaining
decomposition-derived contracts use four historical commits which all contain
the same decomposition bytes. Those historical bytes have SHA-256
`a907cda33835ebf06187331c1c5937a9ae9949923c5465b17519cbd8fcaba6d4`;
the current decomposition has SHA-256
`952d3cbf81b0cea014a1c3f1bd3f62fbc0b23b96bfa1fd1913961731c925b08b`.
Accordingly none of the 51 decomposition-derived contract headers proves
alignment to the current decomposition bytes.

The conversion closed at `92725eace3ef50306bf0c09032bc59492e636c01`.
Twenty-four current SOW files changed after conversion and 29 remain at their
conversion-closure bytes. Git history supplies partial provenance, but no
single current-byte acceptance register binds all 53 current SOW hashes.

## Invariant register

`contract_invariant_coverage_register.csv` does not exist and no ruled bounded
deferral was found. The accepted decomposition requires creation or explicit
deferral before REVIEW closure. Current `CONTRACT.md` contains 48 invariant
families while decomposition section 10A names 41. The missing families are
`K-CONTROL`, `K-EXPORT`, `K-PROJECT`, `K-RESIDENCY`, `K-ROLE`, `K-RUNTIME`,
and `K-STORE`.

All deliverables remain `IN_PROGRESS`; therefore this is not a present
lifecycle failure. It becomes a closure blocker for any REVIEW transition
unless the register is created or a bounded deferral is ruled.

## SOW-064 and PRD sections 8 and 9

The accepted decomposition maps `SOW-064` to both `DEL-06-02` and
`DEL-06-03`, but neither contract frontmatter declares it and no App
ScopeOfWork frontmatter contains `SOW-064`.

The substantive behavior is partly present: `DEL-06-02` covers
catalog/descriptor collision control and `DEL-06-03` covers in-process
composition. This corresponds to PRD FR-104/105 and the `ChiralityMcpTools`
interface. Semantic coverage does not close the missing trace identity.
Repairing the two contracts' traceability is not new scope.

## Owner alternatives returned

1. After a corrected App decomposition is accepted, bind the complete current
   population prospectively. Do not invent historical provenance for the six
   held contracts.
2. Alternatively, preserve current contract bytes and create a governed
   provenance register binding each current SOW hash to its source class,
   migration evidence, amendment authorities, lifecycle state, and accepted
   decomposition.
3. Create the invariant register against all 48 current families, or adopt a
   bounded deferral naming reason, owner, affected claims, trigger/expiry, and
   the seven currently uncovered families.
4. Repair the `SOW-064` trace identity in both `DEL-06-02` and `DEL-06-03`
   without selecting a repin target.

## Reproduced deterministic counts

```text
contracts=53
decomposition-derived=51
PKG-00 controls=2
declared commit resolves=47
declared commit unresolvable=6
current declared-basis bytes match=2
current declared-basis bytes differ=45
current declared-basis bytes unknown=6
held=6
CONTRACT invariant families=48
decomposition invariant families=41
missing invariant families=7
post-conversion SOW changes=24
SOW frontmatter rows containing SOW-064=0
```

## Limits

- No exact historical basis for the held six was inferred.
- Exact owner acceptance for every post-conversion byte was not established.
- Runtime behavior and D-APP-48/49 were outside this return.
- No repin target is recommended.
