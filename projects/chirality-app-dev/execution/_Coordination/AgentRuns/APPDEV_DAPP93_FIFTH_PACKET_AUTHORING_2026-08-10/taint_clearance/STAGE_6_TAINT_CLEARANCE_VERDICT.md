# Stage 6 — taint-clearance verdict

Verdict: `BLOCK — CHILD TOOL-FENCE BREACH; NO N1 ACCEPTANCE`

## Substantive results retained as evidence

- Stage 1: PASS — six exact salvage hashes match; the ledger is
  `dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.
- Stage 2: PASS — the full four-pattern scan exited `1` with stdout `0`
  bytes.
- Stage 3: PASS — 41/41 declared source identities resolve to live
  allowlisted repository files and every declared digest matches.
- Stage 4: PASS — 80/80 ledger rows resolve to live-source provenance.
- Stage 5: PASS — exact schema, 80 contiguous unique rows, field-complete,
  allowed actors/classes, exact approval fence, and Stage 3+4 fan-in equality.
- Historical-root content fence: no excluded historical root was listed,
  globbed, searched, walked, or read except the six direct authorized salvage
  files. No salvage file was copied.

## Blocking invocation-scope defect

At intake, after reading the sealed brief but before loading the frozen-form
table, the child used `/usr/bin/sed -n '1,260p'` to read the brief and then
a shell `for` loop with `echo` and `/usr/bin/sed -n '1,320p'` to request
fresh-root control files. Those are not frozen forms F01–F11; the loop and
`echo` are prohibited shell built-ins. Two requested fresh-root filenames
were absent. All operands were within the fresh run root, and the command did
not access an excluded historical root, but the sealed brief makes any tool
fence breach an immediate BLOCK.

The child also failed to stop immediately on recognizing that intake defect
and completed Stages 1–5. Those later outputs are evidence only and cannot
cure the violated invocation contract. No repair, substitution, packet
authoring, N2 release, Git/network/runtime/product action, or execution
authority follows.

Final disposition:
`BLOCK — SUBSTANTIVE TAINT CRITERIA PASS, BUT SEALED TOOL-FORM CONTAINMENT FAILED; PRESERVE EVIDENCE AND HOLD N2`.

Native context telemetry: unavailable.
