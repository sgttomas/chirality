# Sealed brief — common production closeout

Validate the final WORKING_ITEMS return against D-PEC-85, the immutable V2
proposal, and this run basis. Reproduce its manifest, exact path inventory,
pre/post hashes, hold results, status semantics, five selected checks,
author→fresh-verifier chain, correction/backcheck chain if any, and explicit
limits. Use manager evidence directly; do not rerun a full product assessment.

After validated fan-in, freshly confirm the loop receipt head. Append exactly
one D85 production-closeout receipt: Receipt 177 only if Receipt 176 remains
the head and 177 remains next; otherwise use the then-next available number.
Preserve the complete prefix byte-for-byte and run the receipt validator before
and after. The receipt records source production and finite evidence while
leaving fitness acceptance and promotion unopened.

Seal every common output in this sibling root. The root manifest excludes only
itself and explicitly names the future `CHANGE_PUBLICATION/**` subtree owned by
CHANGE. Include every nested manifest. Run default candidate whitespace with
untracked files, `git diff --check`, receipt checks, scoped containment, and
harness self-check. Freeze this common root except for the named CHANGE subtree
and stop the writer.
