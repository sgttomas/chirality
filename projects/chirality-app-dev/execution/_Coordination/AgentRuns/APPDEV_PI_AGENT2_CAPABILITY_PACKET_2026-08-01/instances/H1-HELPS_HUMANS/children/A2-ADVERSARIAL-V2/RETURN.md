# Agent 2 Return V2 — Independent Revision 2 Refutation

Status: `COMPLETE / READ_ONLY`

Verdict: `COMMIT-SAFE / OWNER-PRESENTABLE`

Basis: live Revision 2 proposal, the single D-APP-84 register row, Revision 1,
and versioned v2 RunID records after manager repair

The fresh Agent 2 changed no file and did not rely on the Revision 1
adversarial verdict.

## Findings and repair cycle

Initial findings:

1. `BLOCKER` — P1 allowed a failed native primitive to fall back to a
   registered Chirality tool, contradicting fixed implementation selection and
   the no-fallback fence.
2. `MAJOR` — §3 described X1's all-agent worker placement as required while X2
   and X3 remained valid alternatives.
3. `MAJOR / RECORD-ONLY` — the v2 work graph and manager records were not yet
   closed and generic manager records still represented Revision 1.

Manager repair:

- P1 now fixes exactly one implementation family per public tool at accepted
  versioned profile/registration time. Unavailability, failure, or nonconforming
  wrapping rejects the operation. Runtime fallback/substitution is prohibited,
  and an implementation-family change requires renewed evidence and a newly
  constructed session.
- §3 is explicitly the recommended X1 architecture. It identifies common
  non-bypass invariants while leaving X2/X3 placement to their option text.
- Versioned v2 child/manager return, status, work-graph, and handoff records
  were materialized without overwriting Revision 1 evidence.

## Final verification

- No `BLOCKER`, `MAJOR`, or repair-requiring `MINOR` remains.
- Pi-native reuse stays behind Chirality identity/schema, exposure policy,
  pre-execution authorization, evidence, canonical-event, interruption, and
  audit contracts. Native delegation and ambient Pi resources remain disabled.
- X1 means a separate role/run-specific sandbox for every tool-executing Agent
  0/1/2 instance, never one shared sandbox. Pi remains Agent-2-only.
- H1 is Agent-2-only, grants no Bash now, and leaves current project-root
  read/write plus serialized-integration doctrine binding until a separate Root
  ruling and implementation.
- No present OS agent/tool sandbox is claimed; the Electron GUI renderer
  sandbox is correctly distinguished.
- Revision 1 is byte-preserved at SHA-256
  `0f4ddfb3c71b1862225ce35430fc18b275588b2dfafbca7d884aaef524a9830e`.
- B1 requires exactly one V/P/X/H/R token subject to compatibility; B2, B3,
  and D are standalone. The exact response interface is coherent.
- Exactly one D-APP-84 `AWAITING_RULING` register row points to Revision 2.
- `git diff --check` passed and scoped changes are contained to the two packet
  revisions, the one register row, and the existing RunID.
