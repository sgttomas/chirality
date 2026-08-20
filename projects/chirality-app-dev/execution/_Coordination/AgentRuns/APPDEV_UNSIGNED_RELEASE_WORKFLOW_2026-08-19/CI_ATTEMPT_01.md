# PR CI attempt 01 — G4 manifest remediation

- PR / product head: `#583` / `ea1d6fd322d4cac794ad3f0ca817d09ef872ac54`.
- Failed proof: governance `harness`, run `32327128948`, job `96300527118`, step `G4 instruction-surface tranche manifest`.
- Exact observation: base `57803893d1eb161f395e0574c256dd27920bf1d4`; 21 changed paths, two instruction-surface paths, zero added schema-readable manifests. Both `.github/workflows/desktop-release-template.yml` and its deleted `.disabled` predecessor were uncovered.
- Classification: intrinsic governance coverage defect in the existing DEL-09-05 workflow node; product workflow behavior was not implicated.
- Remediation: added `docs/governance_harness/tranche_manifests/APP-DEL0905-UNSIGNED-CI-20260819.yaml`, covering both workflow paths and itself while recording D-APP-97 C1, human-gated PR posture, serialized integration ownership, and pending M6 fan-in disposition.
- Local proof: G4 corpus schema validation PASS (34 manifests); named-tranche diff coverage PASS for the two product-head workflow paths; candidate-range simulation using the live validator's `--added-manifests-only` selection PASS for all three instruction-surface paths (both workflows plus the manifest); G4 validator tests 44 PASS; self-check exit 0; whitespace PASS.
- Product hashes: unchanged from review 03; no new product review required.
- Rerun: governance `harness` must execute the real committed candidate range after CHANGE commits/pushes the new manifest. The local candidate-range simulation is deterministic preflight evidence, not a CI pass.
