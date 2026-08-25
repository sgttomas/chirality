# Return — N4 Supply-Unit Candidate Assembly and Review

- **Status:** `PASS_WITH_DOCUMENTED_GAPS`
- **Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`
- **Basis:** `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
- **Dependency:** corrected N3 return SHA-256
  `181d594ad3b973bd5ac0defe6f6c91c59bf62c2fce4366f233247c77ca682743`
- **Review:** fresh claim/hash/scope review; zero actionable findings.

## Assembled subject

The candidate binds the exact three official 0.149.0 macOS arm64 asset
identities, the 3/3 byte-identical App Server payload, package ancillary
identities, the R13-admitted vendor-signature defect, Apache-2.0 license and
notice obligations, exact-pin readback and `multi_agent_v2` precedence, all
118 feature entries, the exact `features.plugins` baseline/default/override,
all three sandbox-denied destinations, OUT-002 policy handoff, current-doc
drift, and every N3 evidence gap.

The N2b `.zst` inventory row now carries the official archive digest
`c4c31ecd562a834b01f9e1466da090279a9c4774b4d7f5ee1ee9fb0d31e73677`
rather than the decompressed payload digest. All dependent evidence and review
hashes were regenerated without download, vendor execution, or network probe.

Generated JSON schema, generated TypeScript types, schema-derived exhaustive
method inventories, and the version-run per-run gate record remain
`UNAVAILABLE_UNDER_BOUNDS`. Nine other runs have complete attributable gate
records; no vendor code was rerun during correction. The named
R13-B finding remains: the plan fails G5 on an invalid nested signature;
0.149.0 App Server's vendor signature is invalid as published per issue 37725
and R13; G5 requires a corrected artifact or later owner ruling.

No G2 acceptance, pin amendment, G5 disposition, implementation, cutover,
release, publication, reliance, App adoption, or blocker/hold lift is claimed.
TM-ROOT-106/122 and all ten existing DEL-02-06 held bindings remain unchanged.

## Stable output hashes

| Output | SHA-256 |
| --- | --- |
| `README.md` | `ff4ed9502b2b4ac843107cf14a9f5ff35983f6e9f70469f80610b960582bd897` |
| `SUPPLY_MANIFEST.json` | `18a1fa0741b9d6d9466e2c5e4903aa9b87baab1b5259d6a1c2a36664d11ecc39` |
| `SUPPLY_UNIT_CANDIDATE.md` | `238769718d71d62be8465d5d758c4fdacaf26a62da0aa60e471ce6e56de6890a` |
| `CONFIG_METHOD_FEATURE_MATRIX.md` | `c44656398ca7d1b5bdf84dbd0be65b32d9f33cba1fc241e05e5ceeab76bfd58d` |
| `SCHEMA_TYPES_METHOD_INDEX.md` | `d5620ffde7ff42ee824648dfee8c2e02d5f92d370786cf97a692d1bab75ec1cf` |
| `OUT-002_ENDPOINT_INVENTORY.md` | `fd6bd4e4dd7c2a0dc477e567becd5d2d092514db36dfedaf2fa2a529798d9f47` |
| `G2_ACCEPTANCE_SHEET.md` | `cec83abc2fc39358037600c883dd7b55ad09b154140d68a4d86346c309cda5ae` |
| `EVIDENCE_HASH_MANIFEST.csv` | `0808752ae60270e483daa86774f896006da35f4d950804b1a3982e90c6ccdbe6` |
| `04_REVIEW/HASH_VERIFICATION.csv` | `ab69a0e6054026425a0115ae039fe881cea03d7ae39c3d153620c080814bcf47` |
| `04_REVIEW/REVIEW.md` | `80538b87008cb36db1664384f519fdeb22864bca6a1f2f56b4bc4c047ade1a67` |

## Validation

- governing-instrument and N1–N3 return hash chain: `PASS`
- every `EVIDENCE_HASH_MANIFEST.csv` row: `PASS`
- every N3 `ARTIFACT_HASHES.csv` row: `PASS`
- candidate JSON and CSV parse: `PASS`
- 118 unique feature entries; stage counts `38/2/41/3/34`; enabled/default
  counts `42/42`: `PASS`
- exactly three denied attempts; committed traces record zero completed
  connections, credential prompts, and external writes: `PASS`
- nine complete attributable per-run gates plus one explicit version-run
  evidence gap: `PASS_WITH_DOCUMENTED_GAP`
- exact plugin/config/precedence assertions: `PASS`
- candidate top-level hashes: `PASS`
- `git diff --check`: `PASS`

N4 returns the packet for owner G2 disposition. It does not select an option
on the decision sheet.
