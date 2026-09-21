# DEL-10-05: reverse-pass notes

The reverse pass answered all 270 capability rows, taken in this order: BUILD 41, ELECTRON 35,
HARNESS 60, RTCONTRACT 53, SETTINGS 42, WORKSPACE 39.

- **Response counts:** CLAIMED_BY 0, PARTIAL 4, NOT_MINE 266.
  - `CAP-HARNESS-053` → PARTIAL `CLM-004.3`: fixture posture.
  - `CAP-HARNESS-055` → PARTIAL `CLM-004.1`: the staged-live partition and the non-acceptance result semantics.
  - `CAP-RTCONTRACT-040` → PARTIAL `CLM-009.5`: the protected / agent-writable split.
  - `CAP-RTCONTRACT-041` → PARTIAL `CLM-029`: the operation-proposal notice copy for the `boundary_notice` field.
- **Why nothing is CLAIMED_BY:** DEL-10-05 is a DOC_UPDATE deliverable that produces copy and review
  material. It owns none of these behaviours outright. The domain code belongs to the other PKG-10
  deliverables (profile contract, protected paths, operation proposals, and the D-APP-50..52 tools).
- **Coverage gaps:** none. Every capability that touches domain boundary copy maps to an existing
  forward row.
- **Errata:** none. The sealed ledger is unchanged; its SHA-256 still matches
  `9d0903bd7a0441e7813d348689bf2a446c91572009c1227f598ca6ac87a22a6e`. So the sealed and
  errata-applied census are identical.

## REACH discrepancy (no erratum)

The two capability rows and the forward ledger tag the same files differently:

- The forward ledger tags `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts`
  and `operation-proposal.ts` as `REACH=LIVE`. That follows `EVIDENCE_PACK/REACHABILITY.csv`, which
  reaches them through the contracts barrel.
- `CAP-RTCONTRACT-040` and `CAP-RTCONTRACT-041` tag them `REACH=TEST_ONLY`, with the note
  "no non-test consumer".

I wrote no erratum because CONVENTIONS §2.3 [INTEG] makes the evidence-pack map the static
reachability source.

The discrepancy does not change any Disposition. The rows that cite these files are CLM-009.4,
CLM-009.5, CLM-029, CLM-030 and CLM-004.1. The copy rows among them are judged on the deliverable
text. CLM-004.1 already rests on the legacy-only tool handlers.

R3 may want to reconcile the barrel-reach rule (pack) with the consumer-reach rule (capability
files). If the capability reading is adopted, those rows' code citations become TEST_ONLY
corroboration and not live evidence.
