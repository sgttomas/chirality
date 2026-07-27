# OD-7 Fan-In Validation

Verdict: `ADMITTED_WITH_ONE_SCHEMA_WAIVER_AND_VISIBLE_UNKNOWNS`

## Return inventory

| Dispatch | SHA-256 | Basis | Coverage verdict |
|---|---|---|---|
| `A2-ROOT-RECORDS` | `175f475a46269a0d79a2ef1940f7c50b29bf9e08449254c077dd32e198259ef3` | `ef164c20c8a903a7ecff9450f677938a4111392f` | PASS — all assigned Root residues, closure protections, routing fields, and deterministic populations present |
| `A2-APP-RECORDS` | `be582f3228628f34d917d62a85db5a7f7913b1450e5e095048cc2b64d1cc521e` | same | PASS — all assigned App records, detector, boundary, and notice questions dispositioned |
| `A2-T0-PEC` | `73af1b3addc616ca7274f96462bd000a126ff6c428ced622bb49fbab8dbd3f2b` | same | PASS — all assigned Tier-0/PEC lineage, seam, profile, ownership, and notice questions dispositioned |
| `A2-PIPING` | `65612f9174c2ad87c491ce9039ba8842692486c2d1abfccd8ad40dd8b31ca8bb` | same | PASS — D-30, D-31, DEC-063, receiver notices, non-client status, and two directly related mechanical residues dispositioned |

Every return names files inspected, uses the frozen status/decision enums,
keeps missing behavior evidence `UNKNOWN`, records limitations, and identifies
actual engine/provider/model where exposed. No return was repaired before
fan-in.

One non-material schema omission is explicitly waived rather than silently
repairing a frozen return: `A2-PIPING` issue
`PIP-EXISTING-AGENT-NOTICE` has eleven cells because its `Unknowns` cell is
omitted. The row is `CLOSED`, its claim and rerun trigger are complete, and no
unknown is asserted or used by synthesis. Fan-in treats the omitted field as
`None` for this row only. All other horizontal issue rows have twelve cells;
all six vertical `A2-T0-PEC` issue tables contain the twelve required fields.

## Evidence and scope validation

- All four basis identities match the accepted commit.
- All 132 file-and-line references in the four returns and all 60 evidence
  references in `FINDINGS.csv` resolve within their cited files. Semantic
  support for the routed claims was checked during fan-in.
- Read-only Git ancestry reproduces the three proposed SHA identities:
  D-GOV-27 effective merge `bfb21d11…`, D-APP-75 effective merge
  `18e5dda5…`, and D-30 publication commit `712df448…`.
- Current bytes reproduce the D-30/D-APP-48 `source.commitSha` mismatch.
- Current Root decomposition/telemetry closes OI-011; current PRD/README close
  C-4. Neither is reopened.
- Current notices prove D-GOV-28 delivery to App and PEC. No current evidence
  supports retroactive D-GOV-26/27 notice debt to PEC.
- No child proposed implementation, method reform, semantic parity, new
  product scope, mandatory PEC, or mandatory resource governance.

## Non-averaged dispositions

1. `RB-PEC-ADAPTER`: the T0/PEC return called correction mechanical; the App
   return called retire-versus-pending semantics owner-gated. The App
   classification governs because the row is App-owned accepted consumer
   evidence and the two truthful successors differ materially. The finding is
   therefore `OWNER_DECISION`.
2. Piping notice posture: App correctly found no generic runtime-migration
   notice due merely because App/PEC migrated. Piping correctly found a
   narrower current-state notice due because Piping directly claims D-APP-48
   synchronized consumption. Both stand; the required notice is about the
   demonstrated D-30 mismatch and contract disposition, not Piping client
   migration.
3. D-APP-48/Piping: retained under OD-6 for App/Root evidence and under OD-7
   only for immediate coordination and Piping-owned successor routing. No
   repin or successor identity is inferred.
4. PEC-K-03/K-11: remains `UNKNOWN` until the owner classifies the language as
   interface requirements or external obligations. A PEC coordination note
   may surface the question, but accepted decomposition cannot be annotated
   outside SCOPE_CHANGE.

## Shared unknowns

- Current executable D-APP-49 conformance and cross-release compatibility.
- Governed live PEC daemon consumption and actual legacy profile invocation.
- Need and exact shape for a daemon global event feed.
- Final auth-reuse and event-contract placement decisions.
- Whether PEC-K-03/K-11 were intended to bind external consumers.
- Exact successor Root workplan.
- Any accepted successor for Piping's App-era contract mechanism.

These unknowns constrain claims; they are not converted into failures.

## Admission result

All mandatory returns are admitted. The one field-level waiver above does not
waive a return or factual issue, and no new dispatch is needed. Synthesis may
proceed from the four frozen returns plus current-basis deterministic
verification.
