# TM-ROOT-112 implementation acceptance packet

DecisionID: `ROOT-TM112-IMPLEMENTATION-ACCEPTANCE-01`
Recommendation: `ACCEPT-FINAL-HASH-REPAIR`
Status: `DECISION-READY / NO DECISION TAKEN`

Authority basis: the implementation ran against pre-normalization sealed brief
SHA-256 `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`.
The current published brief is the semantically identical whitespace-normalized
blob SHA-256 `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`.
Acceptance of the candidate does not depend on treating those byte identities
as interchangeable; each is bound to its recorded phase.

## Candidate offered for acceptance

The candidate implements the already accepted `G2 + C1 + F1` / N-STOP-1..7
semantics at these exact product hashes:

| Product surface | SHA-256 |
|---|---|
| `docs/SPEC.md` | `647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f` |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2` |
| `runtime/tests/daemon.test.ts` | `c853f20726c8633207246a90e79ac89122b651a15e6e0f9976b15f1910acb352` |

Fresh backcheck found no material defect after two reproduced material defects
were repaired. Final Node 24 evidence is adversarial 2/2, canonical daemon
15/15, full runtime 74/74, strict checks PASS, and evidence build PASS.

## Residual and effect boundary

Acceptance would accept these exact Root contract/source/test bytes as the
TM-ROOT-112 graceful-stop repair. It would not claim Node 22.19 execution
coverage, prove App R2 causality, prove process/SIGTERM behavior, accept App
parity, or authorize merge by itself. Under the owner's prior routing
direction, acceptance of this repair would release the ordinary Root-to-App
notice naming D-APP-88 and TM-APP-036's mandatory non-blocking parity-rerun
rider. App owns that later parity evidence and its consequences.

## Exact recommended owner return

```text
ACCEPT ROOT-TM112-IMPLEMENTATION-ACCEPTANCE-01 FINAL-HASH-REPAIR — ACCEPT THE
TM-ROOT-112 G2+C1+F1 IMPLEMENTATION AT EXACT SHA-256
647eee2d8e68da9d6a4f7935b781b6b98c874ba696c824dd6d6a8f6c1b8d6a7f FOR
DOCS/SPEC.MD, 224403008e5ff072f1f614801afe4cedba6d3ade3c000c90ce1602ae8e27ddf2 FOR
RUNTIME/PACKAGES/DAEMON/SRC/RUNTIME-DAEMON.TS, AND
C853F20726C8633207246A90E79AC89122B651A15E6E0F9976B15F1910ACB352 FOR
RUNTIME/TESTS/DAEMON.TEST.TS AS THE ACCEPTED ROOT GRACEFUL-STOP REPAIR; ACCEPT
THE RECORDED NODE 24 STRICT, ADVERSARIAL 2/2, DAEMON 15/15, FULL-RUNTIME 74/74,
BUILD, AND FRESH-BACKCHECK EVIDENCE; CARRY NODE 22.19 EXECUTION AS AN EXPLICIT
UNEXECUTED COMPATIBILITY GAP; AUTHORIZE THE ORDINARY ROOT-TO-APP NOTICE NAMING
D-APP-88 AND TM-APP-036'S MANDATORY NON-BLOCKING PARITY-RERUN RIDER; DO NOT
CLAIM APP R2 CAUSALITY, PROCESS/SIGTERM PROOF, APP PARITY ACCEPTANCE, OR MERGE
AUTHORITY — <ACCOUNTABLE HUMAN> <YYYY-MM-DD>
```

Alternative: return `REJECT ROOT-TM112-IMPLEMENTATION-ACCEPTANCE-01` with exact
defects and required bounded remediation. No inferred partial acceptance.
