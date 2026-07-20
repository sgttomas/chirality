# QA

## Verdict

`PASS_FOR_FRESH_V1_RECHECK` — derivative evidence only. This verdict does not
accept the candidate mappings or release the recheck.

## Checks

| Check | Result |
|---|---|
| Fresh D-APP-69 activation/basis preflight | PASS |
| Manifest count / uniqueness / existence | PASS — 22 / 22 / 22 |
| Ordered path-list hash | PASS — `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36` |
| Remaining-container reproduction | PASS — 14 + 1 + 1 + 4 + 2 = 22 |
| Predecessor child returns | PASS — immutable 5 / 5 bindings preserved |
| Sealed R1-REPAIR child reuse gate | PASS — exact brief/return hashes, basis, 14 / 14 rows, schema, source bindings, terminal containment, zero writes |
| Replacement child dispatch | PASS — none required and none dispatched |
| Sealed-child source blob and SHA bindings | PASS — 14 / 14 recomputed |
| Complete child-to-package fidelity matrix | PASS — 14 / 14 rows; 5 exact, 5 faithful compression, 4 repaired material loss, 0 unexplained |
| Complete package population | PASS — exact 22-path set; zero duplicates or omissions |
| Ledger schema / rows / order | PASS — 22 / 22 in manifest order |
| Proposed mapping schema / rows / order | PASS — 22 / 22 in manifest order |
| Classification reproduction | PASS — 22 `OWNER_CLASS`; all other classes zero |
| Candidate slate population | PASS — nine groups, `5+4+6+1+1+1+1+1+2=22` |
| V1-001 stylesheet boundaries | PASS — DEL-02-02 and DEL-02-05 plus all other evidenced boundaries retained |
| V1-002 ChatMarkdown graph | PASS — ChatPanel + DocumentView only; no DEL-05-04 edge |
| V1-003 ANSI graph | PASS — ChatMarkdown sole importer; DEL-02-01 primary / DEL-02-03 consumer proposal |
| V1-004 exact EOF repair | PASS — exactly ten named files now end in one LF, not two |
| V1R-001 FilePicker boundary fidelity | PASS — DEL-02-04 UI state plus DEL-09-06/server security restored; DEL-06-04 substitution removed |
| V1R-002 physical-owner alternatives | PASS — stylesheet, provider, and event-view shared/split alternatives explicit |
| V1R-003 v8 erratum | PASS — sustained nonconsequential; only exact manifest paths used for current evidence |
| V1-005 | PASS — nonblocking observation preserved; no source repair |
| Activated package file population | PASS — 14 files including the fidelity matrix |
| Subject source and five `_STATUS.md` paths unchanged from basis | PASS |
| Historical root-level blocked package unchanged | PASS |
| Historical R1, R1-RETRY, V1/V1-RETRY, evaluation, and child returns unchanged | PASS |
| Authorized write-root containment | PASS |
| JSON parse and required sealed-child row fields | PASS |
| Fidelity CSV schema / path order / source bindings / locations | PASS — 14 / 14 |
| Markdown/CSV terminal LF and horizontal-whitespace checks | PASS |
| Tracked and per-file no-index diff hygiene | PASS |
| Downstream release | PASS — false; fresh V1 recheck and W1 remain blocked |

## Accepted child return bindings

| Slice | Rows | RETURN.json SHA-256 |
|---|---:|---|
| DEL-02-01 | 14 | `6ba2cecb1bb4a99ce2c93dca3f40edaee39517f50161dd8a36b53eae0778b45b` |
| DEL-03-03 | 1 | `83387f67e826d38002b79dbe572a70b5952f42646b11432bbc92c2909c5ad3b1` |
| DEL-06-02 | 1 | `2d7082404b1b64434752e80df34959a32d408789413e3de0068b004c926cd50e` |
| DEL-09-04 | 4 | `4b5bd6862567fc657edb7893323abd461f98bae6d0687c9cfc8aa36995848faa` |
| DEL-10-04 | 2 | `70e4aa4a9db478e6adcbf56596fe37f35246fc5eff69763ff24edd23ee08aba2` |

Those five are immutable R1-RETRY inputs. The one fresh R1-REPAIR child is:

| Slice | Rows | RETURN.json SHA-256 |
|---|---:|---|
| DEL-02-01 fresh evidence | 14 | `b9bfb2923ec3853c4373923a61bca7e340963251e40fab94f3dbf5bdc56480c0` |

R1-REPAIR2 reused this exact sealed return only after validating its brief
SHA-256 `7ee27d1f464460bc8e9fb39c87aebdc044e1440eddb8ddd735c3bb0667b5b3fa`,
return hash, frozen basis, exact filtered-manifest order, all required fields,
all 14 live blobs and SHA-256 values, relied-on corpus/authority state,
terminal containment, and zero subject writes.

## Historical preservation bindings

The root-level blocked package retained its pre-run SHA-256 values, including
`CQF1_PATH_LEDGER.csv` `8905fc0d...`, `HANDOFF.md` `96b22f70...`, and
`RUN_BASIS.md` `add2073c...`. The original R1 launch, return, and status
retained `c8810c00...`, `b682a43a...`, and `197a83a7...` respectively.
R1-RETRY return/ledger/mapping/slate retained their amendment-v3 predecessor
bindings before authorized mutation of the activated package. V1-RETRY
return/status/report/findings and both evaluation-child returns remained at
their sealed hashes throughout repair.
R1-REPAIR return/status and V1-RECHECK return/status/protocol/report/findings/
handoff plus both V1-RECHECK child launch/return pairs remained at the exact
amendment-v4 bindings throughout R1-REPAIR2.

## Test posture

No runtime, frontend, generator, browser, or service test was run. This was an
authorized read-only concordance pass. Static implementation and existing-test
inspection were used as evidence and were freshly reproduced for all 14
DEL-02-01 rows. This is sufficient for candidate discovery and derivative
repair, not for subject repair or release.

## Rerun triggers

Rerun from the earliest stale node if any scoped source blob changes, any of
the five Remaining entries changes, governing authority is superseded, a V1
refutation invalidates a material claim, a child provenance defect is found,
or the owner selects a materially different boundary that requires fresh
evidence. A fresh V1 refutation remains an expected gate, not a waiver.
