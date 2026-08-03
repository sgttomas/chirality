# Agent 2 Brief — Packaging, Identity, and Coexistence Review

Parent: `HELPS_HUMANS`

Objective: independently test the candidate A/C schemas, B extraction map,
and two-artifact identity/resource/data-coexistence design examples against
the current App packaging and Electron topology.

Read scope:

- D-APP-90 packet and ruling;
- this run's `ACTIVATION.md` and `WORK_GRAPH.md`;
- current App `package.json`, Next/Electron config, Electron entry files,
  resources, and relevant packaging evidence;
- prior D-APP-87 re-plan and D-APP-88 blocked/rollback evidence.

Write scope: only
`reviews/A2_PACKAGING_IDENTITY_COEXISTENCE_RETURN.md`.

Required return:

- candidate non-authoritative A/C schema examples;
- B shared-core and target-shell boundary/extraction review;
- two design examples showing distinct artifact identity, display name,
  resources, update channel (design-only), and application-data/session roots;
- collision/failure modes, measurement suggestions, and elimination tests;
- explicit separation from the absent D-APP-88 helper and from release,
  signing, publication, and generic-runtime authority; and
- confirmation that no forbidden path was written.

Do not delegate. Do not build/package, alter source/config, or define actual
bundle identifiers or runtime contracts.
