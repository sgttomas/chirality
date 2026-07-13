# W-A1 Portability Inventory

Verdict: `PASS`.

Generated reconciliation evidence contains zero checkout-root and local-temp
prefixes. Repository and run references are relative. Reproduction scripts
derive the active repository root at runtime and emit portable records.

Accepted machine-specific strings are confined to exact copied source/control
bytes, marker-bound candidate/render text, and verifier fixtures copied from
those bytes. They are classified `PRESERVED_SOURCE_LITERAL` and were not
normalized. Package inventories and all source/hash/marker bindings are
carried through the 189 current package bindings.

PKG01 has 54 files containing classified preserved source literals after R2;
the exact file/hit ledger is `detailed/PKG01_PORTABILITY_HITS.tsv`. The two
formerly unclassified generated `workspace_root` fields are now portable `~`
and the exact R1-to-R2 reverse chain passes. Other package inventories remain
bound by their accepted current manifests.

No portability action changed candidate, source, status, control, map, parity,
checklist, render, check verdict, project, lifecycle, or authority semantics.
