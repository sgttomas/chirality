# Manager fan-in validation — N1 blocked

Verdict: `BLOCK — N1 TOOL-CONTRACT BOOTSTRAP DEFECT; N2 HELD`

WORKING_ITEMS independently accepts the child's substantive evidence but
rejects N1 as a governed return.

## Independently reproduced substantive checks

- six owner-authorized salvage files exist and the Stage 5 ledger is exactly
  SHA-256
  `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`;
- manager F02 over the six explicit paths exited `1` with stdout `0` bytes;
- Stage 4 parses as exactly 80 unique rows, 80 `PASS` dispositions, and 183
  explicit provenance paths; all 183 are live files and zero names a closed
  D-APP-93 historical root;
- Stage 5 records the exact 13-column schema, 43+37=80 field-byte-equal fan-in,
  contiguous unique row identities, complete fields, permitted actors/classes,
  and exact approval/failure/cleanup fences;
- child output containment is exactly six stage files plus one return;
- read-only Git status over the five physical closed-lineage roots is empty;
  no packet, freeze, verifier, product/runtime, or other downstream file exists.

## Governing defect

The child invocation ledger openly records:

1. `/usr/bin/sed -n '1,260p'` to read the sealed N1 brief; and
2. a shell `for`/`echo` wrapper invoking `/usr/bin/sed -n '1,320p'` over
   fresh-root control-file requests.

Neither sed range form is F03 (`sed -n '1p'` only); `for` and `echo` were
explicitly prohibited. The operands were fresh-root files, so this is not a
historical-root breach, but the brief makes any unlisted form an immediate
BLOCK. The child also continued Stages 1–5 rather than stopping immediately.
Those later outputs remain preserved evidence only.

The manager owns the primary causal defect: the dispatch envelope required the
child to read the brief completely but froze no command form capable of doing
so, and the brief's permitted forms were discoverable only after that read.
This circular bootstrap made compliant intake impossible. The executable
preflight correctly repaired lineage four's host-path/BSD-syntax defect, but
it probed an insufficient F03 shape and therefore could not make N1 lawful.

## Disposition

- N1: `REJECTED / PRESERVED BLOCKED EVIDENCE`.
- N2, packet, index, author return, freeze, N3 verifier, and approval token:
  `HELD / ABSENT`.
- No remediation or replacement child is authorized within this lineage.
- Close the fifth lineage, append Receipt 153 through CHANGE, and return the
  blocker to the owner. Do not begin a sixth lineage.
