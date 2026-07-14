# App Stage-2 Agentic Runtime and Failure Analysis

> Deterministic derivative report. The cited run evidence governs. Rates are descriptive;
> Wilson intervals do not make packages, agents, or deliverables independent random samples.

## Population and outcomes

- Packages / waves / members: 10 / 3 / 47.
- Author/verifier baseline roles: 94; documented child-attempt directories: 99.
- Mappings / source lines: 1,428 / 15,386.
- Eventual accepted candidates: 47/47; substantive candidate failures in the catalog: 0.
- RECON apply/rollback simulations: 47/47 across 47 members; project writes: 0.
- Manager-evidence-closeout statuses: 14; retry-suffixed attempt directories: 5.

## Command-level project checks

- Recorded invocations: 67 (60 PASS, 7 FAIL).
- Recorded command time: 951.714 seconds across 60 timed invocations; 7 invocations lack durations.
- Timed failed-attempt time: 0.995 seconds.
- Packages with a failed first frontend-premerge attempt: 7/10.

| Check | Runs | Failures | Total s | Median s | P95 s |
|---|---:|---:|---:|---:|---:|
| frontend-build | 10 | 0 | 89.459 | 9.714 | 11.456 |
| frontend-premerge | 17 | 7 | 101.721 | 10.694 | 11.680 |
| frontend-test | 10 | 0 | 42.182 | 4.624 | 5.093 |
| frontend-typecheck | 10 | 0 | 24.748 | 2.758 | 2.847 |
| harness-pytest | 10 | 0 | 620.446 | 68.273 | 73.975 |
| harness-self-check | 10 | 0 | 73.158 | 8.399 | 9.089 |

Hypothetical one-successful-run-per-wave/check cache:

- Invocations retained/avoided: 18/49 (73.1% avoided).
- Measured time avoidable lower bound: 620.653 seconds; untimed records make the true value larger.
- This is a counterfactual estimate, not an executed optimization.

## Curated abnormal episodes

| Category | Episodes | Affected units | Packages | Deliverables |
|---|---:|---:|---:|---:|
| BRIEF_OR_INPUT | 5 | 5 | 4 | 5 |
| EVIDENCE_PORTABILITY | 11 | 46 | 9 | 3 |
| EVIDENCE_TERMINALIZATION | 16 | 27 | 6 | 9 |
| NEGATIVE_FIXTURE_SETUP | 1 | 1 | 1 | 1 |
| PROJECT_CHECK_SUBSTRATE | 7 | 7 | 7 | 0 |
| SUSPECTED_NOT_REPRODUCED | 1 | 1 | 1 | 1 |
| TOOL_INVOCATION | 2 | 2 | 1 | 1 |

Detection layers: child_self_check=3, evidence_remediation=3, manager_fan_in=22, manager_supervision=4, reconciliation=1, registered_check=7, runtime_normalization=1, tool_guard=2.

## Git-bounded wall-clock envelopes

These are activation-commit to merge-commit envelopes, not CPU time or summed agent time.

| Wave | Members | Preparation h | Merge lag min | Envelope h | Members/h | Source lines/min preparation |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 15 | 3.479 | 15.700 | 3.741 | 4.010 | 23.075 |
| A2 | 16 | 4.355 | 12.267 | 4.559 | 3.509 | 21.370 |
| A3 | 16 | 4.361 | 13.983 | 4.594 | 3.483 | 19.051 |

## Statistical bounds

- Eventual-pass rate: 100.0%; 95% Wilson interval 92.4%–100.0%.
- Observed substantive-failure rate: 0.0%; 95% Wilson interval 0.0%–7.6%.
- Project-check invocation failure rate: 10.4%; 95% Wilson interval 5.2%–20.0%.

## Measurement limits

- No native model-token, context-occupancy, CPU, or per-agent start/stop telemetry is present.
- Event classification is curated and evidence-bound because historical prose/status schemas are heterogeneous.
- Event episodes are not equal-cost or statistically independent; counts must not be read as a defect probability without their denominator.
- Git envelopes include orchestration, evidence work, integration, CI, and queue latency.
