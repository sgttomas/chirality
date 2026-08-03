# Packaged UI Smoke — D-APP-86 Option A

Verdict: `PASS`

## Lawful inspection seam

Native Computer Use was attempted first, after reading its skill instructions
in full. The Mac was locked and automatic unlock was unavailable, so no native
UI claim was made from that attempt. Brief Amendment 02 authorized equivalent
persistent-state inspection through the identical packaged Electron
renderer's standard loopback CDP endpoint.

Retry 02 used packaged GUI PID `54094`, CDP `127.0.0.1:52778`, page target
`13817769A0731F8CDAC91A7A510B2D57`, and packaged internal renderer URL
`http://127.0.0.1:52812/`. The endpoint was loopback-only, existed only for the
isolated run, and was absent after cleanup. No development server or product
source change supplied the observed state.

Every observation below has a DOM snapshot, full accessibility tree, and
2560×1580 PNG in
`instances/A2-PARITY-EXECUTOR-01/evidence/ui/`.

## Observation 1 — Workbench governed boundary

`retry02-workbench.*` records `data-woven-surface="workbench"`, the focused
surface heading `Workbench`, and the governed deliverable-contract boundary.
It rendered the live 53-deliverable inventory and stated the Documents,
evidence, contracts, lifecycle/dependency, and reconciliation roles. The
primary dialogue component remained mounted. Returning to Dialogue succeeded.

DOM SHA-256:
`28c18f6968db1697117f77d48d95fcff4776429ed829a7e13c65623636af7d30`.
Accessibility SHA-256:
`7915f58b30f9a5afe47ee7c860a05b20a25e33be6da4b3dae0e9a6c1b99ffd3d`.
PNG SHA-256:
`83c1210034ecf6a8db4fcecb7f53b8ccb559dd668202bd12b53b6da5fdab6024`.

## Observation 2 — Pipeline governed boundary

`retry02-pipeline.*` records `data-woven-surface="pipeline"` and exact
DECOMP, PREP, TASK, and AUDIT intent. It rendered the dynamic 53-deliverable
scope and the supported/coming-soon lane boundaries. The primary dialogue
component remained mounted. Returning to Dialogue succeeded.

DOM SHA-256:
`f822349f0b75817743a2daadf343579f72930959a6709d0f07d534deba157fa6`.
Accessibility SHA-256:
`6527a2727bc3afed09d42d5268afadd3e222bf34a17b7ac64ff38be9c8ee156e`.
PNG SHA-256:
`7d461fa16bff2aeb98acb2798682692352feaa61d79291b9ea071fda272da93d`.

## Observation 3 — Guarded recorded-session selection

A deterministic stub turn was started in the packaged primary Dialogue.
`retry02-dialogue-inflight.*` and
`retry02-dialogue-guarded-selection.*` show:

- `primaryDialogueMounted=true`;
- primary chat input disabled while the turn ran;
- both visible recorded-session rows disabled;
- explicit UI text `Session selection is paused while the primary dialogue is running.`;
- the attempted selection of session
  `e2c32024-fa62-48d5-b27a-d8637080d2c3` did not change
  `selectedSessionId` from `null`; and
- the running primary turn continued to completion.

Guarded-selection DOM SHA-256:
`0e9ce6bf6806bdc0d2955a5427860e50d7781ef6d02de9de354765d5156be50f`.
Accessibility SHA-256:
`f144515d5b06981dd172bcc4f6aa4ef0b7832bbb10f1a9140d639a863cc97a8b`.
PNG SHA-256:
`1c50bedf51168fe560f917534577a58b0a6867e019058c4d8604a91e953798a4`.

## Observation 4 — Read-only real-daemon replay

After the primary turn completed, the packaged navigator selected exact
recorded session `e2c32024-fa62-48d5-b27a-d8637080d2c3`.
`retry02-recorded-session-replay.*` records:

- `REPLAY — READ-ONLY`;
- the exact selected session ID and events source;
- `Events 2`;
- `Transcript items shown 1`;
- `Malformed records skipped 0`;
- runtime status `completed`, adapter/provider `stub`;
- terminal event
  `a26a661d-721e-491d-ab9f-66b2aa3b2dd0 / turn.completed`; and
- the primary dialogue remained mounted as session
  `67fcb7dd-521d-4ad6-b784-30cf6b4f329d`.

DOM SHA-256:
`f3fa7e1ed48bc440ac8d0a261b61c3335ba63ae0486c25533e41845dbe095d1e`.
Accessibility SHA-256:
`d43881e1a98522a9bd93141c018f9e9a3bd85c1cdd2de3a01947f97da31875b2`.
PNG SHA-256:
`a11f9082304c08f03d91771745e9f7eec23f89548eb1ed77c13a52bc88884a68`.

## Attribution limit

The real replay session is exactly attributed to admitted persona
`WORKING_ITEMS`, role `agent1`, with no parent/child identity. The unavailable
`A2-PARITY-FIXTURE` persona was not manufactured or inferred. This limits only
manager/child attribution; it does not limit the required parity observation.
