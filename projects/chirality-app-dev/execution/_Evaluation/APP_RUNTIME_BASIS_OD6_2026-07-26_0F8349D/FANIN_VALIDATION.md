# Fan-in validation

## Admission result

`PASS_WITH_WARNINGS`

All four required terminal returns are present, basis-bound to
`0f8349d90f58c1e6b3339263f5aafaf36e783a7e`, evidence-linked, and separated
from repository writes. Each required scope in `EVALUATION_PROTOCOL.md` is
covered.

| Return | Coverage | Evidence anchors | Unknowns separated | Admission |
|---|---|---|---|---|
| `A2-BASIS-53` | 53-contract census; 51+2 distinction; invariant register; SOW-064 | PASS | PASS | ADMIT |
| `A2-HOLD` | held set; ruling/register/tool/test concordance; operation checks | PASS | PASS | ADMIT |
| `A2-DAPP48-49` | source conflict; pins/consumers; D-APP-49 continuity/audit; versions | PASS | PASS | ADMIT |
| `A2-RUNTIME-CONSUMERS` | App/PEC/Piping topology; governed evidence; degraded/version behavior | PASS | PASS | ADMIT |

The runtime-consumer child initially returned an unrelated status answer. That
return was rejected before fan-in and the same child was rerun against its
original sealed scope. Only the completed runtime-consumer return preserved in
this package is admitted.

## Manager reproduction

EVALUATION independently reproduced:

- 53 ScopeOfWork contracts: 51 decomposition-derived and two PKG-00 controls;
- 47 resolvable basis commits/paths and six unresolvable basis commits;
- exact agreement between the six unresolvable contracts and APP-HOLD-1;
- the live APP-HOLD scan and 12/12 tests;
- four historical decomposition pins containing identical historical bytes;
- current decomposition bytes differing from those historical bytes;
- absence of `contract_invariant_coverage_register.csv`;
- absence of `SOW-064` from all 53 ScopeOfWork frontmatter blocks;
- D-APP-48's ruling/JSON commit mismatch;
- pull-only validation passing and combined Piping consumption validation
  failing on source commit;
- byte-identical D-APP-49 migration into Root;
- App and PEC as production runtime clients, with Piping not a client;
- absence of client-side runtime API-version negotiation.

## Fan-in agreements

The returns agree that:

1. Root owns the generic runtime; App packages it and acts as a governed
   client; PEC is a bounded client; Piping is not a runtime client.
2. APP-HOLD-1 is active and correctly contains the six unverifiable
   ScopeOfWork bases without repinning them.
3. The corpus lacks one consolidated current-byte App ScopeOfWork acceptance
   binding and lacks the required invariant register or deferral.
4. D-APP-48 is a historical App-era contract with unresolved ruling/live
   identity conflict and a stale Piping consumption record.
5. D-APP-49 source bytes migrated intact, but no first current-location
   executable audit has been admitted.
6. Version compatibility, complete degraded-mode behavior, and live PEC
   daemon consumption remain incomplete or UNKNOWN.

## Preserved distinctions

- Historical decomposition pins are resolvable evidence, not proof of
  current-byte alignment and not automatically nonconforming.
- The six unresolvable pins BLOCK only named reliance/dispatch/promotion/
  accepted-dependency claims under OD-3, not the whole App.
- Piping's stale record blocks reliance on that synchronized metadata claim;
  it does not prove a broken Piping runtime.
- Byte continuity for D-APP-49 is established; executable current-location
  conformance is not.
- Fail-closed daemon-unavailable behavior is established in bounded paths;
  a complete degraded-mode contract is not.

## Warnings

- D-APP-75 retains a stale `PENDING_PR_MERGE` effective label.
- The hold's direct/API/fan-in coverage is governed and testable but not a
  universal runtime interceptor.
- Current behavioral tests were not installed or rerun in this clean
  evaluation worktree.
- No new repin or version target is inferred.
