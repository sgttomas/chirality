# P3_MANIFEST Caller Closure

Verdict: `PASS — CANDIDATE AWAITING RECON-B1`

## P2 bindings and current rows

The P2 manifest itself hashes to
`def458aad0c829b9bb000b02b2813b326d101408fab4402f7c39f89822ef0dff`.
All 15 paths bound by that manifest reproduce their exact SHA-256 values.

All 64 root caller rows and nine App caller rows have a current disposition.
Sixty root rows reproduce their recorded post hash directly. The four root
rows marked `OUT_OF_LANE_UNCHANGED` were lawfully overlaid by the App lane and
reproduce the accepted App final state:

| Surface | Current SHA-256 |
|---|---|
| `frontend/src/__tests__/api/project/deliverables-route.test.ts` | `64523601a2a5b4cef3a178992f59c5ff81249454397f4a37e57a82e6689f4ce7` |
| `frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts` | `295fbb0369b448534de6c1bb56fbecd35df6fc2f595b96677ed2e96ed1b0ebaf` |
| `frontend/src/components/shell/document-view.tsx` | `9dfe17e734a6f76d5470792ef4d62daeea51d8005dfaa5e6fe7341b8cd0120b1` |
| `frontend/src/lib/workspace/filesystem.ts` | `3f3a45c6dd09c35e51f22f651399f70fbae33a17021ebdf531e192ee11b2dc3f` |

Seven App rows reproduce the initial C2A final hash directly. The scanner and
scanner regression rows reproduce the later accepted C2A-R1 repair hashes;
their dispositions remain `ACTIVATED` and `ACTIVATED_TEST` respectively.
No row is missing, unowned, or ambiguously disposed.

## Search refresh

The accepted original-vocabulary query at the synchronized tip returns 5,389
tracked paths, digest
`65170dfe26de49ffe1b0cc3f45ab4377523590bfb725c09da2fbb64b97773efa`.
Relative to P0 it adds 24 paths (23 root execution evidence, one project
evidence path) and removes five vocabulary hits whose accepted activation
changed their wording; none is removed from the caller manifests.

The targeted transition-vocabulary query returns 196 paths, digest
`902d81220c8a5e64fe16c9b9942c25c0627baaaddea4603a7ca5dada93e56af4`.
The union has 5,496 paths, digest
`a7f244e9ccf677a662a19763abf536e7e537218e2d189d7943d81a1b7ba99ca9`.
Within active roots, the original query has 76 hits: 49 exact manifest rows
and 27 P0-classified governance-history, thesis, or independent-schema paths.
The targeted query has 57 hits: 51 exact manifest rows and six P0-classified
governance decision/proposal/history paths. Zero newly active or unclassified
caller is present.

## Containment

The C2 consumer-to-final range changes 236 tracked paths and zero path under
either governed project `1_Working/DEL-*` population. It changes no production
source, `_STATUS.md`, lifecycle, membership, H1/H2, release, or retirement
truth. The fresh census is byte-identical to P0, independently proving this
containment at the row/field level.
