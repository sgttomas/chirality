# Consumer-local boundary

Status: `CANDIDATE SUPPORT ARTIFACT — NOT AUTHORITY`

| Concern | Generic candidate may carry/enforce | Must remain consumer-local | Root must not claim |
|---|---|---|---|
| operation identity | opaque operation/tool ID, version, schema/hash | operation taxonomy, preconditions, mutation meaning | that two consumers' operations are equivalent |
| domain subject | opaque subject IDs/hashes/versions | models, components, results, rule-pack and analysis meanings | engineering validity or model correctness |
| units/tolerances/mapping | opaque governed references | unit taxonomy, conversions, tolerance values/suitability, mapping admissibility, normalization | cross-consumer equality or compatibility |
| privacy/redaction | opaque policy labels, decision/evidence references | classification, protected-content rules, redaction action, telemetry/export policy | privacy clearance from generic success |
| professional boundary | opaque notices and review-reference fields | professional judgment, review obligations, decision-support limits | certification, sealing, professional acceptance |
| human gate | required-gate ID and accepted evidence reference | who may accept, decision content, acceptance criteria | that a runtime/tool receipt is human acceptance |
| UI/API equivalence | transport-neutral IDs, hashes, structured outcomes | product route semantics and no-bypass obligations | that transport conformance proves domain equivalence |
| failure/diagnostics | generic outcome and opaque consumer diagnostics | consumer failure taxonomy and remediation meaning | that generic `SUCCEEDED` means consumer success |
| artifacts/evidence | hashes, inventory, provenance references | retention, visibility, privacy, admissibility, reliance | that captured evidence is sufficient for external reliance |
| fixtures/previews | explicit test-profile/non-authoritative marker if later allowed | product preview semantics and test-fixture meaning | fixture/synthetic output as authoritative runtime success |

Basis: E-001, E-002 §B, E-003, and E-006 §§4-8. This table deliberately
preserves Piping's solver, engineering, privacy, protected-content, mapping,
tolerance, professional, and human-review meanings locally and applies the same
generic/local division to every future consumer.
