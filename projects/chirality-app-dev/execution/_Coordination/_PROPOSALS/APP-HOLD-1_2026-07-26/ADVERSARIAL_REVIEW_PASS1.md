# APP-HOLD-1 Adversarial Review — Pass 1

Verdict: `RETURN_FOR_CORRECTION`  
Reviewer: read-only ephemeral Agent 2 generalist  
Engine/provider/model: `Codex` / `OpenAI` / `UNKNOWN`  
Brief: `APP-HOLD-1-A2-REVIEW-2026-07-26`  
Brief SHA-256:
`ed4a36ed3aa040c7c74cde0b5fb5ee5d4e0216743b98cb92e19bdb7e8e833b58`  
Review basis: Git `918bb48b8fcee66c031d0d6d4040a46089f96067`

The reviewer wrote no file. This record was persisted by the HELPS_HUMANS
parent after receipt of the terminal return.

## Findings

### AHR-001 — BLOCK — Exception verifier permitted unrelated owner prose

The verifier accepted any declared substring found in an App decision. It did
not bind the cited ruling text to the exception ID, deliverable, operation,
entry path, and expiry. The reviewer demonstrated an `ALLOW_BY_OWNER_EXCEPTION`
for `DEL-02-01` by citing an unrelated D-APP-74 sentence approving an SCA-APP-004
propagation plan.

Required correction: derive one canonical owner-exception block from all
exception fields, require that exact block in the committed ruling bytes, and
validate every exception row globally before evaluating a target.

### AHR-002 — BLOCK — Proposed live test placement broke path resolution

The candidate-layout test resolved the tool and registers relative to the
proposal structure. After the proposed live copy, it would look for
`execution/_Scripts/tools/app_hold.py` and registers under
`execution/_Scripts/`, which do not exist.

Required correction: make path resolution explicitly support both candidate
and proposed live layouts, add a live-layout path test, and complete the
promised invalid-exception tests.

### AHR-003 — REVIEW — Tool read/output containment was not enforced

Explicit repository, SOW, register, exception, and output paths could escape
the intended checkout or App subtree.

Required correction: require the canonical Git top level; constrain SOW,
register, exception, fixture, and output paths; remove or contain generic
output writes.

### AHR-004 — REVIEW — Application inventory omitted tool catalogs

The proposed deterministic tool lacked the required root `tools/REGISTRY.md`
entry and project-local `execution/_Scripts/README.md` catalog entry.

Required correction: add exact proposed registry/catalog rows and tool
contract details to the application inventory.

### AHR-005 — REVIEW — Fail-closed parsing claim exceeded implementation

Duplicate front-matter keys could be overwritten, malformed lines ignored,
and invalid exception rows outside the current target silently bypassed.

Required correction: fail on duplicate/malformed top-level front matter;
validate every exception row, including unique IDs, enums, paths, targets,
dates, commits, and ruling bytes, before any `ALLOW`.

### AHR-006 — WARN — Universal binding exceeds universal interception

The candidate creates a universal normative prohibition, but only
WORKING_ITEMS receives a pre-act target gate. Direct/API entry is
instruction-bound and retrospectively fan-in checked rather than universally
intercepted in product code.

Required correction: state this observed enforcement limitation without
weakening the entry-path-independent prohibition.

## Reproduction

- Hash manifest: 11/11 verified.
- Corpus: 53 contracts.
- Held set: exact six expected contracts.
- Register parity: `PASS`.
- Scan fingerprint:
  `dd8657773edc7ac57107a3741d19e8f348cf08382645a6c96a3347dd5e16ca4a`.
- Missing object `416b29033bbacb0bc3648d84033272b7ab4e6e11`:
  unresolvable.
- All 12 held operation/entry-path combinations: `BLOCK_APP_HOLD`.
- `DEL-03-01`: `ALLOW`.
- Mixed dependency set: aggregate `BLOCK_APP_HOLD`, unaffected row remained
  individually `ALLOW`.
- Unrelated D-APP-74 ruling exploit: `ALLOW_BY_OWNER_EXCEPTION`.

The reviewer did not run write-bearing temporary-fixture tests because the
sealed brief prohibited all writes. No live surface was modified.

## Question dispositions

| Question | Pass-1 disposition |
|---|---|
| Universal entry-path binding | Partial: normatively yes; universal pre-act mechanical interception no |
| WORKING_ITEMS enforcement vs authority | Yes |
| No repin | Yes |
| Exact prior owner exception | No — AHR-001 |
| Checkout containment | No — AHR-003 |
| Registered-check compatibility | Yes |
| Complete/minimal application inventory | No — AHR-004 |
| Fail-closed scanner and authoritative scan | Partial — AHR-005 |
| Fan-in isolation | Yes |
| No hidden expansion | No product/lifecycle/repin expansion; hidden exception-authority path present |

