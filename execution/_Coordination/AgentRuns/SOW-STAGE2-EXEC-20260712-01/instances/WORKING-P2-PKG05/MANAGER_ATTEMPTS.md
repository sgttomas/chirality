# WORKING-P2-PKG05 Manager Attempts

The first manager fan-in attempt required byte-identical author and verifier
forward/inverse TSV files. Both contained the same 25 governed operations and
hashes, but the author placed `ADD ScopeOfWork.md` after each member's deletes
while the verifier placed it first; the author also spelled inverse legacy
adds as `RESTORE`, while the verifier used `ADD`.

This was a safe evidence-representation defect, not a project, candidate,
semantic, authority, lifecycle, or scope conflict. The failed assertion was
retained. Fan-in was rebound to canonicalize only `RESTORE` to `ADD`, ignore
row order, and require exact set equality over deliverable, operation, path,
and SHA-256. No child or candidate file was changed; all downstream manager
bindings and checks were regenerated.
