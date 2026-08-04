# Decision request — TM-ROOT-112 Root graceful-stop contract and repair gate

DecisionID: `ROOT-TM112-STOP-CONTRACT-01`
RequestedBy: `HELPS_HUMANS`
Question: Should the Root accountable human authorize a bounded TM-ROOT-112
semantic-contract and implementation/test tranche now, or explicitly route it
into the broader TM-ROOT-121 / DEL-02-06 owner-selection session?

## Options

1. **Authorize a separate bounded TM-ROOT-112 tranche (recommended).** Select
   exact graceful-stop semantics for active ordinary requests and SSE streams,
   including a finite drain/termination boundary and residual-connection
   handling; then authorize the Root runtime owner to implement and test the
   selected contract. This is the shortest route to the HIGH App D-APP-88
   blocker while preserving separate human semantic acceptance.
2. **Route the semantic selection into TM-ROOT-121 / DEL-02-06.** This unifies
   the decision with broader runtime stewardship but holds the App blocker
   behind that larger selection session and its still-unselected implementation
   authority.
3. **Defer without repair.** This retains an evidenced condition in which an
   active SSE connection keeps first-signal shutdown awaiting `server.close()`;
   this option must explicitly accept that consequence and does not satisfy the
   row's recorded closure target.

Recommendation: Option 1. The minimum candidate scope is one accepted shutdown
contract surface (currently absent from `docs/SPEC.md` §14.1/runtime docs),
`runtime/packages/daemon/src/runtime-daemon.ts`, and bounded cases in
`runtime/tests/daemon.test.ts`: idle, completed keep-alive, incomplete ordinary
request, live SSE, bounded termination, disconnect/interrupt, socket and owner
cleanup, and restart. Exact grace duration, stream cancellation obligations,
and forced residual-connection behavior remain human-selected semantics; this
inquiry does not choose them.

Evidence:
`instances/H1-TM112-INVESTIGATION/evidence/raw/CONTROLLED_RESULTS.json` and
`MANAGER_RETURN.md`.

DownstreamBlocked: Root source/test repair; App D-APP-88 auditable post-GUI
first-signal teardown rerun and acceptance.
