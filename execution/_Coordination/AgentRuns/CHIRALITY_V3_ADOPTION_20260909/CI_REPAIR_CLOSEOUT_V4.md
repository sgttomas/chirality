# PR 764 CI correction closeout

Base: `041011d8a081f85080dfac808db9657a3fd6455f`.

Root G4 declaration now includes the already-reviewed `.github/workflows/harness-premerge.yml` change. Only that declaration and the corresponding export size/hash row changed. Independent reviewer `/root/integration_custody_review` returned PASS for both exact postimages: tranche `7183995fafbaad150edfa6906d4e85dea02c309dce56ebd3718bccee1a52ad59`, export CSV `6164890f12d18c6fcf23507e632823d0c20088bbc9911ae62fbcb31f8eca56a6`. All M2/M6 fields remain unchanged. Full PR-range G4 and 48 validator tests passed.

The controlled App stub now accepts structured Runtime input and requires frozen context for v3 sessions. Unsupported legacy adapters still reject ordinary v3 work. The App maps legacy dontAsk to readOnly only when no explicit canonical permission choice exists; the existing SDK permission policy supports that conservative mapping. The stub performs deterministic simulation, without executing Runtime callbacks or claiming semantic instruction execution.

App validation: 21 focused tests, typecheck, and all eight Section 8 checks passed through an isolated Node Runtime daemon and real Next HTTP routes. Independent Astra review passed the four-file App repair. Exact source and evidence hashes are recorded in the selected manager and reviewer receipts. Test processes were stopped. Raw traces, patches, and full review captures remain preserved locally; this commit selects compact review and result records.

Fresh CI must pass before the authorized merge. This correction grants no supplier qualification, packaged trial acceptance, or publishing approval.
