# QA report

Registered analyzer completed both invocations with exit 0. This is an observation status; the ALL subject is FAIL because two deliberately registerless controls appear in its inventory. The explicit CURRENT51 subject is PASS.

CURRENT51: 51 units, 51 readable registers, 51 schema-valid registers, 648 logical rows; denominator_complete=True. Zero invalid source rows, unresolved targets, outside-scope endpoints, SCCs, malformed IDs, misplaced fields, and missing IMPLEMENTS_NODE anchors. Evidence-file population is 648/648 cells. Cell presence does not validate the cited file or its claim.

ALL: 54 units, 52 registers, 2 schema-invalid/missing units. The two missing registers are exactly DEL-00-01 and DEL-00-02, governed control exceptions. DEL-09-07 is a retired historical carrier, with its existing register retained. ALL has 6 isolates, including those three excluded current-scope units. See Evidence/ALL/coverage.csv and Evidence/ALL/closure_summary.json.

Input_Manifest.csv pins every unit, context, and present register. Source_Basis.json pins instructions, selected workflow, analyzer, helpers, policy script, prior accepted summary and scope sources. Register and source hashes matched before and after both runs. The APP-HOLD reliance check was ALLOW for all 54 IDs.

Analyzer limits: a strict graph says nothing by itself about satisfaction, delivery readiness, implementation quality, or governed acceptance. Zero cycles applies to the stated filter and scope.
