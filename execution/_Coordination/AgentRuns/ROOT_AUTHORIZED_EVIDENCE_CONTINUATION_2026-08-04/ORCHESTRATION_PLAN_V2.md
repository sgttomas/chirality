# Root authorized evidence continuation — orchestration plan v2

RunID: `ROOT_AUTHORIZED_EVIDENCE_CONTINUATION_2026-08-04`

Plan version: `2`

Selection authority: `HUMAN`

Descriptive posture: `MIXED`

## Version basis

Plan v1 remains immutable and is not rewritten. Its two terminal manager
returns passed HELP_HUMAN fan-in:

- H1 G1-B refresh/re-ingest: manifest SHA-256
  `ec8a7209376dc7b3587b69a5753c213802443d25ffbb3eaf8b50549954f49ddc`;
- H2 TM105 AB-01/AB-09: package-manifest SHA-256
  `4f9241adaa58235359a8c9b328dd536a23f5e51c278d217bc54f729a4954829f`.

H1 closes its bounded objective with `TM-ROOT-106` and PIA-U30 still held.
H2 closes AB-01/AB-09 evidence acquisition while all thirteen targeted TBDs
remain open. H2's accepted return identifies AB-02 as the next bounded
backend/rights/topology candidate-evidence node and AB-07 as a lawful parallel
store/privacy evidence node. The standing TM105-A preparation-only authority
and no-byte-gate fence remain unchanged.

## Added node

| Node | Manager | Objective | Writes | Depends on | Expected return |
|---|---|---|---|---|---|
| H3 | HELPS_HUMANS | Execute AB-02 backend/rights/topology evidence and AB-07 evidence-store/privacy evidence using governed disjoint Agent-2 children. | `instances/H3-TM105-AB02-AB07/` only | H2 terminal accepted fan-in | validated evidence carrier, candidate/unknown matrices, child fan-in, blockers and reruns |

H1 and H2 are terminal. H3 may run its two evidence children concurrently
after sealing disjoint read sets and instance-local write targets. Failure in
one child does not license inference or block recording the other's valid
evidence.

## Preserved gates

H3 may inventory and test bounded candidates but may not qualify or select a
backend, decide a rights grammar or topology, infer owner/vendor/platform/legal
facts, set retention or deletion policy, draft no-TBD contract bytes, present
a byte gate, or authorize implementation. AB-03 remains dependent on an
AB-02 candidate posture; AB-06 remains held on AB-02 and AB-07 plus later
accepted prerequisites. Timing, budgets, conformance, semantic acceptance,
implementation, lifecycle, release, reliance, publication, and merge remain
outside H3.

HELP_HUMAN will validate H3 terminal fan-in and version the plan again before
any further node or closeout act.
