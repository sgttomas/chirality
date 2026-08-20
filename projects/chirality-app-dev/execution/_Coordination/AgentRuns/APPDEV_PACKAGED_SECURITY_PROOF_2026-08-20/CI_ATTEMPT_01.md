# CI attempt 01

- Pull request: `#586`.
- Node revision: `605a0b7bc85e054d32221083e1f15a57b2d85dee`.
- Candidate base: `357a58b56726feba49507534159c3fbc4656b818`.
- Governance run/job: `32345362720 / 96352866416`.
- Result: `FAIL`, G4 instruction-tranche manifest coverage only.
- Exact block: `.github/workflows/desktop-release-template.yml` changed in the
  candidate range but no newly added schema-readable tranche manifest covered
  the workflow.
- Disposition: bounded remediation 03 adds the D-APP-97-authorized manifest;
  it changes no product byte and grants no authority. Other proof/check claims
  are not inferred from this failed run.
