# Independent first-run geometry / source-load diagnosis

The first frozen geometry suite passed four of six tests. Original test SHA-256 remains 6fff5e055fee05956b5f286c5859ffc4a2cc0d1cd064cd02bf65dbdb51c471ba. Source references, numeric values and 1e-9 comparisons remain unchanged.

Passed: ordinary source section and all responses; thin source section and pressure/bending/torsion/normal-stress responses; unpressurized thin member with no fake pressure region; and rejected collapsed/overflowed/underflowed final geometry. See _run_records/geometry_run1.log, GEOMETRY_RUN1_INPUTS.json and GEOMETRY_RUN1_RESULT.json. All 49 source hashes were unchanged after this run.

## Large-range input parsing, separate from geometry arithmetic

The large model reached MECHANICS_SOLVED in both modes and returned finite I/J. Its radius-bit predicate failed. An evidence-only diagnostic, linked to the exact already-built product and serde_json rlibs, proves why:

| Field | Original frozen source bits | Decoded input bits |
|---|---|---|
| OD=2e77 | 4ffba2bfd0d5ff5b | 4ffba2bfd0d5ff5b |
| wall=5e76 | 4fdba2bfd0d5ff5b | 4fdba2bfd0d5ff5c |

The old serde_json feature set decoded the wall as 5.0000000000000006e76. Product geometry faithfully retained that parsed wall and reported ri=4.999999999999999e76 (bits ending 5a), instead of the frozen source value 5e76 (bits ending 5b). It returned I=7.363107781851078e307 and J=1.4726215563702156e308. The mismatch begins before DTO construction in this golden-JSON path.

ROOT directed the actual M34 float_roundtrip feature repair rather than a test-input reconstruction workaround. The original frozen test is unchanged and will be rerun. SOURCE_INPUT_BITS.json was prepared as diagnostic custody only; it is not used to substitute inputs for a passing test or change the property targets.

## Near-incompressible cancellation, with source bits verified

The same diagnostic retained each exact original nu selection and original JSON fixture construction, then called both public solver modes for every near-limit case. The normalized OD/wall and reported nu bits match the source reference for these cases:

| nu | Relative extension error in both modes | Disposition |
|---|---:|---|
| .499999 | -1.8880587e-11 | Below unchanged 1e-9 |
| .4999999999 | +1.7902493e-8 | Fails |
| Last binary64 value below .5 | +.043037835047 | Fails |

For the last valid nu, actual extension is 1.5790972091241894e-20 m; independent source expectation is 1.51394048812521335e-20 m. The response-equivalent RHS is 1.8189894035458563e-12 N, versus independent source net load 1.74393424900431578e-12 N. The RHS figure is **inferred from the actual response and declared section**, not a directly captured assembly vector. The observed error is consistent with the separately rounded cap/eigen cancellation already identified in the source design; the raw source bits eliminate input parsing as its cause here.

Stable assembly must preserve the mathematical small source difference while retaining cap/eigen ledger identities. Do not enlarge the extension tolerance, substitute zero, move nu away from its legitimate value, or claim that an assembled-system residual proves the original load accurate.

## Diagnostic custody and limits

_run_records/geometry_bit_diagnostic.rs is a copy of the unchanged test helpers with include paths rebased and an appended printing main. It changes no physical inputs, expected values, production files or original test. Nu-from-bits is exactly the selection already present in the frozen near-limit test, not a new workaround. It ran outside the test harness as an approved narrow diagnostic, linked to the uniquely identified already-built rlibs in BIT_DIAGNOSTIC_INPUTS.json. Raw output is geometry_bit_trace.jsonl; the compile log is retained.

This diagnosis does not mark the six-test suite passed, does not reclassify the old radius-only reference as source-accurate, and does not qualify native transport or current repaired source before rerun. Parent owns the parser and stable source-load changes. The existing pressure14 test remains untouched.
