# D85 P-A publication and production graph

Base: fetched `origin/main` / branch base
`55df51ac3201456e0f181823e3aefefef47a73bb`. Native roles are
instruction-asserted. All manager and specialist launches use
`gpt-5.6-sol` / `medium`.

```text
HELP_HUMAN (read-only supervision and validated fan-in)
├── RECONCILIATION common coordination
│   ├── publish exact D85 P-A ruling, one register row, Receipt 176
│   └── seal D85_EXECUTION_2026-09-08 and hand off; then writer stops
├── CHANGE
│   ├── publish/merge ruling tranche under standing session Git authority
│   └── fetch and prove exact ruling/register observability on origin/main
└── WORKING_ITEMS PKG-01 / DEL-01-03 (released only after merged observation)
    ├── N0: mechanical check registration/review and ordinary production start
    ├── TASK author: software-bounded-implementation
    ├── TASK verifier: fresh, read-only, software-code-review
    └── integration/closeout in sibling D85_PRODUCTION_CLOSEOUT_2026-09-08
```

Edges are sequential gates, not hidden delegation: RECONCILIATION ruling
publication → CHANGE merge/observation → WORKING_ITEMS fresh preflight and N0
→ author → verifier → manager fan-in. Affected-check selection runs from
`projects/pec` with project-relative paths and is expected to select five
checks after registration. Product writes before merged observation
are prohibited. Verifier defects return to the author. CHECKING, ISSUED,
artifact acceptance, full P1, issuance, release, and system kill/parity claims
remain outside this graph.

The common authority manifest excludes by name only the future
`D85_EXECUTION_2026-09-08/CHANGE_PUBLICATION/**` subtree. CHANGE owns that
publication evidence after the common seal. Later production preserves this
authority root and uses its separate sibling closeout root.
