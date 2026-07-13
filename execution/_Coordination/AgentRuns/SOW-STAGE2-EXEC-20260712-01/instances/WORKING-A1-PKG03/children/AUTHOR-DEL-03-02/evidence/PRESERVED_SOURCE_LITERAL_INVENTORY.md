# DEL-03-02 Preserved Source Literal Inventory

Classification verdict: `PASS`.

One machine-specific checkout string occurs in the accepted source/control
kit copied byte-for-byte into the isolated workspace:

| Artifact | Line | Count | Classification | Binding |
|---|---:|---:|---|---|
| `workspace/_REFERENCES.md` | 13 | 1 | `PRESERVED_SOURCE_LITERAL` | Exact copied source/control bytes; SHA-256 `c711cf5c2401089b192c2b9d5724ea91b68ef6ba3ec4d2859e788e28d10ce92f` matches the frozen manifest row and live source. |

The literal is outside the four production documents, so it is not present in
the candidate or rendered derivative. Candidate, map, parity, checklist,
render, validation, negative-test, return-preparation, and repaired TASK-run
metadata contain zero machine-specific checkout or temporary-directory
prefixes.

The TASK run-record portability repair is separately authorized and proved by
`amendments/A1-PKG03-GENERATED-EVIDENCE-PORT-001.md` and the package-local
`GENERATED_EVIDENCE_PORT_REPAIR.tsv` / `GENERATED_EVIDENCE_PORT_REPAIR_CHECKS.md`.
It changed generated metadata only and did not change the preserved literal,
source/control bytes, candidate bytes, or semantic evidence.
