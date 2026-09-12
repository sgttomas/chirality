# APP docs return: D-GOV-43 (A2) application tranche, App-loop documentation

Bounded Type 2 (TASK) return, 2026-09-12. Basis: worktree branch
`claude/chirality-codex-replatform-3999f1` at `e83cb1f47`; publication SHA
of the ruling and supplement `d2878462be59a43b4afc175a8cce85abca9cf696`.
No Git write operations were run. Reviewed Git changes are the record.

## Files changed

Write scope (`docs/**`, `frontend/docs/**`):

- `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md`:
  Status table gains an amendment row; `RB-DAEMON`, `RB-CONTROL-SOCKET` and
  `RB-ROLE-MODEL` revised to the App-owned Runtime service, private socket
  API with per-launch token, and `developerInstructions` plus recorded policy;
  `RB-RESIDENCY` retired in place (item 13); the RB-PEC-ADAPTER disposition
  notes that D-GOV-43 supersedes the one-daemon boundary on the App path.
- `docs/RELEASE_QUALITY_GATES.md`: amendment note; harness-workflow gate now
  requires the event representation and the disconnection rule; packaging
  gate points to the short procedure and names the retired family 1 and 5
  gates; §13 "Desktop and CLI use one daemon" revised (App-owned child; CLI
  compatibility unverified); family 1/2/5 and residency bullets retired in
  place with one-line notes rather than deleted.
- `docs/PRD.md`: amendment note; Codex-basis paragraph; §2 runtime direction
  bullets; principle 13; journey 7.12; FR-017, FR-019, FR-027; §9.1 and §9.3
  (extensible upstream-preserving representation, keepalives, disconnect
  rule, every request answered); §9.4 read-with; NFR-030 (stock pinned
  Codex, signature and pin verification); §12.8; §13 ownership note; §16
  PKG-03 and PKG-04 rows; §17 re-expressed to A2 and the Pi/oMLX pilot
  retired; §18.
- `docs/SPEC.md`: amendment note; Codex-basis paragraph; §11 rewritten to the
  A2 transport and event rules; §17.1 and §17.9 route clauses; §19.4 release
  verification; §25.1, §25.2 and §25.5 re-expressed (child ownership,
  effective home, threads, socket API, CLI unverified); §25.6 and §25.7
  retired to history with their text preserved.
- `docs/CONTRACT.md`: amendment note; Codex-basis paragraph; K-ENGINE-3,
  K-EVENT-1, K-EVENT-3, K-EVENT-4, K-EVENT-6, K-UNTYPED-1, K-NET-1, K-KEY-1
  clause revisions; K-CONSENT-1 and K-RESIDENCY-1 retired in place and listed
  in §4; enforcement-map rows re-titled; §5.1 K-RUNTIME-1, K-CONTROL-1,
  K-STORE-2 re-expressed; a sentence after the SCA table records that
  D-GOV-43 supersedes the daemon, supervisor-socket, consent and residency
  parts of SCA-APP-003 and SCA-APP-008 (SCA-APP-008 marked not accepted,
  revision required).
- `docs/PLAN.md`: amendment note; §3 and §13 read-with sentences; §13.1 steps
  4 to 7 annotated as superseded or deferred.
- `docs/TYPES.md`: amendment note; §7.4 browser event terms revised; §13
  Runtime Daemon becomes Runtime Service, Runtime Client revised, residency
  terms retired in place, Required Delegation re-expressed; `PolicySelection`,
  `ApprovalRecord` and Thread Index Entry vocabulary added.
- `docs/VALIDATION_STRATEGY.md`: amendment note; §7 shared-runtime addendum
  rewritten to child-lifecycle, transport, interrupt-versus-retirement
  regression, request correctness and the S-1 to S-8 set; retired items
  named; one run per distinct condition.
- `docs/BUILD_AND_RELEASE.md`: amendment note; §3 baseline paragraph; new
  §8.1 short packaging procedure (build, sign, notarize, verify signature and
  Codex pin, then S-6, S-8 and signature/pin verification as the minimum,
  not a ceiling) and retirement of the Stage 9 to 13 spine's applicability;
  §11 addendum revised (no LaunchAgent, no `--runtime-daemon`, CLI
  unverified).
- `frontend/docs/harness/README.md`, `TRACEABILITY.md`,
  `runtime_engine_contract.md`, `adding_a_tool.md`: D-GOV-43 notes; the
  `AgentEnginePort` required behaviour and the conformance gate list revised
  to the pass-through representation; SDK-named scripts and the first-adapter
  path marked as compatibility history.

Written by the corpus mechanism (outside the docs scope, see below):
`execution/_Reconciliation/References/AUTHORITY_CORPUS.json` (v23) and 52
deliverable `_REFERENCES.md` files.

Not changed: `frontend/docs/harness/tool_catalog.md` (generated from
`HARNESS_TOOL_DESCRIPTORS`, gated by `tool-catalog.test.ts`; hand edits would
fail the test and the descriptor source is owned by the code session).

## Corpus-hash mechanism finding and action

`docs/MANIFEST.json` is an index only and records no hash. The corpus
mechanism is D-APP-38:
`execution/_Reconciliation/References/reconcile_authority_corpus.py` with
`AUTHORITY_CORPUS.json`. It has consumers: every deliverable `_REFERENCES.md`
pins the six authority documents by SHA-256, `audit` gates the
`CHECKING -> ISSUED` profile (`docs/ISSUE_READINESS_PROFILES.md` §6), and
`docs/RELEASE_QUALITY_GATES.md` §2 requires `status`, `bump`, `apply` after
authority-document edits. It is therefore not the consumer-less README
self-hash machinery that D-GOV-43 item 11 retires, and it was run once as
the mechanism requires:

```
status  -> DRIFT: CONTRACT, SPEC, TYPES, PLAN, PRD (DIRECTIVE and workflows MATCH)
bump    -> corpus v23 (2026-09-12), binding_commit e83cb1f47 (HEAD at bump)
apply   -> 52 deliverable files reconciled to v23
audit   -> all rows reconciled; status -> no drift
```

The bump was minted once. An intermediate v23 entry created before a
trailing-whitespace fix to the PRD header was removed by script before the
final `bump`, so the corpus history carries exactly one new version.

## Validator results

- `python3 tools/validation/validate_path_anchors.py --text .`: PASS, 4331
  live surfaces, no home-directory absolute paths.
- `python3 tools/validation/validate_claims_language.py --repo-root .`: VALID
  (302 files; the tool scans the chirality-piping surfaces and does not accept
  per-file paths, so it was run whole-repository).
- `git diff --check` over `projects/chirality-app-dev`: clean.
- New prose contains no em-dashes (one pre-existing em-dash remains inside
  the K-KEY-1 row text that was otherwise edited).

## Judgment calls

1. Retire-in-place everywhere: family 1, 2 and 5 gate members, residency
   rows and invariants keep their identifiers with a one-line retirement
   note and preserved historical text; nothing is deleted or renamed.
2. K-RELEASE-1 is not edited (outside the listed clause families). Release
   and packaging clauses say ordinary local output stays unsigned while the
   D-GOV-43 consolidated candidate is signed and notarized, and the Codex
   basis paragraphs read K-NET-1 and K-RELEASE-1 with D-GOV-43 items 1 and 4.
3. K-NET-1 keeps its deny-by-default spine; the per-root consent postures are
   re-expressed as the user's Codex network configuration and chosen sandbox
   mode (item 4). K-UNTYPED-1's hard envelope is re-expressed as the chosen
   policy (item 10). K-CONSENT-1 is retired with family 1.
4. `AUTHORITY_CORPUS.json` and the 52 `_REFERENCES.md` files lie outside the
   docs write scope but are written only by the corpus's own script, which
   the brief directed me to run.
5. TYPES gains three vocabulary rows (`PolicySelection`, `ApprovalRecord`,
   Thread Index Entry) mirroring the Root TYPES §12 direction in IMPACT.md;
   these are vocabulary, not a new register.
6. `projects/chirality-app-dev/AGENTS.md` "Shared Runtime Boundary" still
   describes the per-user daemon; it is outside this write scope and is left
   for the tranche owner.
7. `tool_catalog.md` left unchanged (generated, test-gated).
