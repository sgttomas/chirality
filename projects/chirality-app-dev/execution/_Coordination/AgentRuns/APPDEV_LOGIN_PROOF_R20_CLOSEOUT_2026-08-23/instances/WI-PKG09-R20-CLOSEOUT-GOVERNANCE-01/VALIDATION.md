# Validation — closeout governance fan-in

Every listed gate exited `0` and changed no reviewed product or proof byte.

| Gate | Result |
| --- | --- |
| `python3 tools/run_affected_tests.py --base origin/main` | PASS; routed `practitioner_harness` and `validation`; 670 passed |
| `python3 tools/practitioner_harness/harness.py self-check` | PASS; no BLOCK; retained 4 REVIEW and 43 WARN findings |
| Root G0 materialization | PASS; registered G1-G4 all passing |
| Root G1 harness adapter | PASS; schema/pins valid; 53 status files |
| Root G2 surface ownership | PASS; all materialized children registered |
| Root G3 work graph | PASS; no active root node |
| Root G4 instruction tranche | PASS; 46 manifests valid; candidate has no instruction-surface path |
| App receipt validator, prior ledger | PASS; unchanged ledger frozen through Receipt-52 |
| App authority corpus | PASS; v18, eight MATCH rows, no drift |
| APP-HOLD dispatch | PASS; `ALLOW`, `CLEAR`, `NOT_HELD`; register `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan `e923a0edab48824195a903c664c9645f9fb9320127e5f04ef04589cc97510bb5` |
| App change scope | PASS; candidate App-only, zero violations |
| Instruction-root current-byte comparison | PASS; exact build revision `2ee96958daf997b7a156f020739bde43ca78ebf9`; 43 source/bundle comparisons; no mismatch; accepted `needs_remediation` row retained |
| Frontend identity | PASS; HEAD and build revision tree `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`; revision-to-HEAD stat and scoped porcelain empty |
| Fresh evidence review | `VALIDATED_PASS`; REVIEW SHA-256 `47cd3143bfff259b449701ca2360654f855e4485c7b057da9e4528f628015c5a` |

Final `git diff --check`, empty index, App containment, JSON syntax, and exact candidate whitespace run only after the manager return, handoff state, and manifest are frozen. No frontend/product/package/build/test/proof/preflight/LaunchAgent/operator/private-root/Desktop/network/signing/release command ran.
