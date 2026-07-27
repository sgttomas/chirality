# Handoff State — G2-DELIVERABLE-OWNERSHIP-20260726

- Accepted upstream basis:
  `2db2c712825af13d6b5425c34d31ff9daf470c89`
- Candidate branch: `codex/g2-deliverable-ownership-validation`
- Candidate status: implementation and focused validation complete
- Authority status: owner-authorized M2 candidate; not integrated by this
  return
- Derivative/evidence status: run records current for the candidate bytes
- Public-export derivative status: regeneration explicitly deferred; the
  accepted post-merge validator and test bytes must be consumed before the
  next export release
- Audit status: focused tool, G4, diff-containment, live-basis, candidate
  Project Setup, and independent adversarial checks pass
- Closure verdict: `READY_FOR_CHANGE_CLOSEOUT`
- Blockers: none within the authorized G2 correction

## Rerun requirements

At Git closeout:

1. verify only the two G2 files, the one tranche manifest, and this run-record
   directory are staged;
2. rerun the focused 60-test suite;
3. rerun G4 CI mode and `git diff --check`;
4. verify the manifest covers the actual instruction-surface diff; and
5. land the correction as its own commit/PR before resuming Project Setup.

After integration, Project Setup remains the next lawful owner. It must rerun
G0–G4 against its own candidate state, then run the requested 46/46
`AUDIT_DECOMP` and present its separate Git closeout. This handoff authorizes
no Project Setup, decomposition, product, runtime, or export write.
