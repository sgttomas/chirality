# D-GOV-16 Inactive Proposal Package

Status: `PROPOSAL_ONLY`

Nothing in this directory is live canon, an accepted migration profile, or
Stage-2 authority. The files exist so the owner can rule on exact bytes rather
than an open-ended implementation promise.

| File | Role | SHA-256 |
|---|---|---|
| `DELIVERABLE_SCOPE_OF_WORK_STANDARD.proposed.md` | Exact proposed successor standard | `7f74290167e3f410242bafe8bca153828a2a93e82099b8498ea6fd90eec85a6f` |
| `TYPES.proposed.patch` | Exact inactive zero-context patch to current `docs/TYPES.md` | `9614166c7db8340532d838768be2de52567862757fe0d5add3d3a90edea9d4b4` |
| `SPEC.proposed.patch` | Exact inactive zero-context patch to current `docs/SPEC.md` | `543200af8a617e2f5673db110eef2b0a5cf742c54e70ccda8bce0cad870d4b2e` |
| `STAGE2_EVIDENCE_PACKAGE_INDEX.md` | Commit/hash-bound Stage-1 evidence and reservation coverage | `8a6e48ac8247fe5147afb4208d3e7c0b4f48cb1071b1e086b4f24a2ceeded806` |

The decision interface is
`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`.
If the owner approves exact successor text, a later controlled implementation
copies/applies the ruled bytes and regenerates derivatives. Proposal files are
not themselves renamed into authority by a tool or agent.

The two patch files intentionally use zero context so their artifact bytes do
not contain whitespace-only unified-diff context markers. Validate or apply
them with `git apply --unidiff-zero --check` (or the equivalent controlled
application command).
