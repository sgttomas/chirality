# Independent Review — SCA-APP-008 Phase 2 Candidates

**Verdict:** `RETURN_FOR_REPAIR`
**Review instance:** `N3-REVIEW-01`
**Basis:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Review scope:** resolved K-EVENT-4 transaction plus complete companion-register candidate
**Lifecycle effect:** none
**Findings:** `1 MAJOR / 1 OPEN`

## Candidate boundary

| Artifact | SHA-256 | Review result |
| --- | --- | --- |
| `Phase2/K_EVENT_4_RESOLVED_CONTRACT_ROW_CANDIDATE.md` | `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0` | `PASS` |
| Resolved full App-contract candidate reconstructed in memory | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` | `PASS` |
| `Phase2/CONTRACT_INVARIANT_COVERAGE_REGISTER_RESOLVED_CANDIDATE.csv` | `26ffe13b3c53130e44e4acaf6ab0aecadf0be853757c8a9678a54b80426b67c2` | `RETURN_FOR_REPAIR` |

## Gate 1 — basis, rulings, and Root source identity: PASS

- Phase-2 steer, A4, A5, and decision input independently re-hash to
  `5cd8e4ac…`, `14db6877…`, `1896d892…`, and `4d16cefa…`.
- Gate-3, Gate-4, and the concordance workplan remain exact at `1a8048f4…`,
  `47daaedf…`, and `c747a81b…`.
- The five A4-A Root source files independently match their pinned SHA-256
  identities: Root contract `ed87eaff…`, CLI config `40cec2df…`, session store
  `fe81bc9a…`, event contract `d20fd7dc…`, and session contract `22e49ccf…`.
- The literal selected identity is supported at the cited bytes: Root
  K-RUNTIME-1/K-STORE-2 retain daemon-exclusive ownership and lazy
  non-destructive import; CLI config resolves `{userData}` and
  `{userData}/runtime`; session-store paths resolve
  `runtime/projects/<projectId>/sessions/<sessionId>/{events.jsonl,session.json}`;
  and the two contract sources fix `chirality.event/v1` and
  `chirality.session/v2`.

## Gate 2 — independent resolved-contract reconstruction: PASS

The reviewer extracted every exact Gate-3 C-01 through C-11 pre-image,
post-image, and insertion anchor, required one match in the live App contract,
and replayed the transaction order while substituting only the Phase-2
resolved C-06 post-image.

| Check | Independent result |
| --- | --- |
| Live App-contract pre-image | `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7` |
| Resolved full-file bytes | `34317` |
| Resolved full-file SHA-256 | `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` |
| Old K-EVENT-4 open-question occurrence | `0` |
| Resolved K-EVENT-4 occurrence | `1` |
| Live K-EVENT-4 row SHA-256 with LF | `f172b56078f83dcc48019ff0fea3c867f96c3d79ab5143fa9bb668d6937fab2a` |
| Resolved K-EVENT-4 row SHA-256 with LF | `92c9d359f70a934fad07b399e18b93df07dc9573f0bf04ab4dd4d40d18eebf93` |

The exact resolved row names the selected path and both schemas, preserves the
Root daemon as the sole active writer, makes the App-local JSONL path a lazy
non-destructive legacy source rather than authority, and limits App streaming
and replay to projections. N1 is therefore accepted by this review without a
repair finding.

## Gate 3 — CSV structure, census, anchors, and sequencing: PASS

- The candidate parses as 18 columns and 83 data rows; all 83 invariant IDs
  are unique and span 50 unique families.
- The live register independently parses as 81 unique IDs across 48 families.
  The exact delta is only K-CONSENT-1/K-CONSENT and
  K-UNTYPED-1/K-UNTYPED; no live ID is removed or duplicated.
- Every one of the 83 `ContractSourceSHA256` cells equals independently
  reconstructed contract identity `a7928297…`; every
  `AppDecompositionBasis` cell names exact approved candidate `932b890e…`.
- All 83 source anchors resolve to the same invariant ID at the cited line in
  the independently reconstructed 214-line contract candidate.
- K-CONTROL-1 has both `OpenIssueIDs` and `CoverageStatus` exactly
  `PENDING_ROOT_AMENDMENT`; it is the only row in that state. Its authority
  references include A4-B/A5-B. No current Root-amendment or Gate-5
  eligibility is claimed.
- A5-C's single Gate-5 grouping remains stated in the transaction record; no
  decomposition-only early act or partial contract application is inferred.

## Gate 4 — six consequential enforcement relationships: PASS

All six exact Gate-3 enforcement-point names occur on every referenced
candidate row:

1. process-supervisor/control sockets on K-CONTROL-1, K-ROOT-1, K-PATH-2,
   and K-KEY-1;
2. `HostedEngineConsentPort`/account-root continuity on K-CONSENT-1,
   K-NET-1, K-KEY-1, and K-ROLE-2;
3. role/native-descendant classification on K-ROLE-2, K-UNTYPED-1, and
   K-SUBAGENT-1/2/3;
4. event codec/coordinator/persistence/SSE/replay/diagnostic/support sinks on
   K-EVENT-3/4/6 and K-KEY-1;
5. renderer credential IPC on K-KEY-1, K-CONSENT-1, and K-AUTH-1; and
6. exact-candidate release validation on K-PACKAGE-1, K-RELEASE-1,
   K-VALIDATE-1, K-NET-1, K-SDK-1, K-CONTROL-1, and K-KEY-1.

The union is exactly 19 affected/new invariant rows. Their enforcement and
rationale additions are present, and the new K-CONSENT-1 and K-UNTYPED-1 rows
have source anchors, provenance, owner classification, carrier coverage, open
issues, and validation surfaces consistent with the approved Gate-3 and
Carrier Map candidate context.

## Gate 5 — changed/new row integrity: RETURN_FOR_REPAIR

`RF-001` is blocking. Relative to the live register, K-EVENT-3 changes:

```text
AppDeliverableIDs:
- DEL-03-04;DEL-05-02;DEL-09-03
+ DEL-03-01;DEL-03-03;DEL-05-02;DEL-09-02;DEL-09-03

ValidationSurfaces:
- DEL-03-04;DEL-05-02;DEL-09-03
+ DEL-03-01;DEL-03-03;DEL-05-02;DEL-09-02;DEL-09-03
```

The additions are supportable, but the removal is not. The unchanged live
decomposition at line 306 assigns DEL-03-04 to interrupt, cancel, cleanup, and
terminal-event compatibility. Gate-3 C-05 strengthens exactly-one durable
terminal outcomes, terminal mapping, recovery, and replay; neither C-05 nor
any carrier transaction removes DEL-03-04. The candidate row's own
`RationaleEvidenceAnchor` still cites `#DEL-03-04`, making the omission also
internally inconsistent.

### Exact repair requirement

Repair only the two K-EVENT-3 cells in the raw CSV so the still-live carrier is
retained alongside the justified additions:

```text
AppDeliverableIDs=DEL-03-01;DEL-03-03;DEL-03-04;DEL-05-02;DEL-09-02;DEL-09-03
ValidationSurfaces=DEL-03-01;DEL-03-03;DEL-03-04;DEL-05-02;DEL-09-02;DEL-09-03
```

Then run candidate whitespace before regenerating every artifact that pins the
CSV identity; recompute the full candidate SHA/byte count; update the companion
transaction record and N2 return/status/validation evidence consistently; and
submit the repaired exact bytes to a fresh independent reviewer. N1 and the
resolved full-contract identity require no change.

## Gate 6 — frozen/protected surfaces and containment: PASS

- All eleven A2-frozen assessment identities match: Brief `4bf54dc3…`, Impact
  `068c7b29…`, Carrier Map `72a1b55b…`, contract proposal `8a6a7999…`, DAG
  `0b721c2e…`, work graph `273c14cc…`, handoff `7fa51832…`, draft notice
  `8ebc728b…`, audit return `7ddc86e0…`, closure summary `30dd016f…`, and issue
  log `deca04cd…`.
- `_LATEST.md` remains `a0298fdc…`; the App Task Management register remains
  `eb37fba1…`; the live App contract and companion register remain
  `6d3a082c…` and `84d6fe00…`; the frontend tree remains `74e3dbe8…`.
- Tracked worktree and index diffs are empty. All current candidate and run
  artifacts are untracked additions inside the steer-authorized SCA and run
  roots. No authoritative or prohibited surface changed.
- Candidate whitespace against exact basis `4c9fdb4c…` passed with zero skipped
  binary/symlink paths; `git diff --check` passed.

## Verdict and state

`RETURN_FOR_REPAIR` with one open MAJOR mechanical finding. No Phase-2
`Handoff_State.md` was created. The candidate state remains incomplete for
owner return; authority and authoritative truth remain unchanged; and a fresh
independent review is required after the exact repair and hash propagation.
