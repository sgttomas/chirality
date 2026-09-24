# Return A4 — feed-model v2 design note (HELPS_HUMANS, general-purpose/opus, high effort requested)

Output: `projects/pec/execution/_Coordination/SCA-005_PREP_2026-09-23/FEED_MODEL_V2_DESIGN_NOTE.md`,
SHA-256 `4b9ccb9f3e96e66a9566479858deac42f5616315045542ba1b5663fef30d12da`. Labelled DESIGN PROPOSAL; asserts no scope status. Records 69 relied-on files with hashes at basis `d61981ee2`; consulted no other role file; A1/A2 outputs had not landed and were not relied on.

Recommendation: **O-B2 with P-β** — App/Piping's new surfaces (`WORK_GRAPH.md`, central `RECEIPT.md`, MEMORY `## Runs`) become first-class feeds; JSON run evidence, workplans and the App/Piping receipt ledgers become labelled historical formats; each loop's row in `loops.json` (schema v2) selects from a fixed set of versioned feed profiles; `adapter.yaml` ceases to be PEC's feed manifest (read only for harness parity); presence from Git worktree scanning plus hook-pushed sessions, `ACTIVE` graph nodes shown as declared activity never liveness; Runtime SSE bridge, client seam and live hierarchy deferred behind a stated trigger.

Trades away: automatic census parity with the harness; zero-configuration onboarding; a larger SCA-005 plus a later schema/port packet; session-level presence and live hierarchy indefinitely.

Findings shaping the design: all three 2026-09-23 trial graphs still show `F1 ACTIVE` though their final PRs are merged (method is deliberate; completion must be derived from Git); run IDs differ from folder names in two of three trials (join on declared run ID); two of three trials have no `RECEIPT.md`; the harness classifies `RECEIPT.md` as unclassified.

Owner questions Q1–Q10 (feed model; adapter.yaml disposition; presence under A2; graph-state reading incl. Git-derived completion; when external trials enter; restating §16.2/16.6/16.8/16.9 after A2; Git refs for in-flight graphs; PEC's own registry row before/after migration; Step-0 cost baseline loops; P1 harness parity coverage given the harness does not observe PEC).
