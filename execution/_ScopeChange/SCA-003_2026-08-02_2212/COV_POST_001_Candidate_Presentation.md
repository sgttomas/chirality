# SCA-003 COV-POST-001 exact candidate presentation

Status: `CANDIDATE_ONLY — AWAITING_OWNER_ACCEPTANCE_AND_APPLICATION`

## Exact identities

| Item | SHA-256 |
|---|---|
| Live source decomposition | `69bdb9ca682a80adab6c23e0a615bd4f9c5ed64f281f11a4e558a1f0e991278c` |
| Exact three-passage candidate | `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d` |
| Exact unified diff | `205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e` |
| Deterministic validation | `feccaf181660b6bf06f4a92066108ff3678553e1bbca5d28c794bfda81b174af` |
| Owner route ruling | `0349897a313f1a41973d3134be3dd1addffc4e9d20ed73bb60b337143de6022b` |
| Owner acceptance/application evidence cited by each correction | `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129` |
| Applied-file evidence cited by each correction | `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8` |

## Exact correction

The candidate changes only the three COV-POST-001 passages formerly located
at live lines 11, 565, and 622–623:

1. the amendment header states that exact SCA-003 acceptance and application
   are completed acts and cites both exact evidence hashes;
2. DEC-024 removes the current-facing candidate/pending-effect posture and
   records the same completed acts and evidence;
3. the current Change Log entry replaces its pending-effect sentence with the
   same completed acts and evidence.

Each corrected passage refers human confirmation status only to
`execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md`. None contains
the current-facing tokens `pending` or `confirmed`, so the text remains true
before and after a later human decision.

Validation reports 20/20 PASS. It proves all frozen inputs, exact
three-replacement construction, protected PRD/companion/pointer/evidence
hashes, 89 unchanged identifiers, DEC-023 byte preservation, unchanged
decision-row count, and future-truth wording compliance.

## Effect boundary

The candidate has no effect until separately accepted and applied. It changes
no scope, topology, mapping, identifier, count, status row, substantive
requirement, companion register, PRD, `_LATEST.md`, DEL packet, runtime,
client/project surface, lifecycle/release/reliance, Task Management, or Git
state. It does not confirm or close SCA-003.

## Exact owner-token grammar

Candidate acceptance:

```text
ACCEPT SCA-003 COV-POST-001 CORRECTION 23f6ae0f: approve exact candidate
SHA-256 23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d
and exact diff SHA-256
205edf58e8a461e049bccdd76100cb3921254b122db2d3957461dc58b5d5e92e as
the metadata-only three-passage correction; preserve every other applied byte
and all stated no-effect boundaries.
```

Separate application authorization after acceptance:

```text
APPLY SCA-003 COV-POST-001 CORRECTION 23f6ae0f: authorize SCOPE_CHANGE to
apply exact candidate SHA-256
23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d to
execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md only, validate
exact containment and protected hashes, rerun the COV-POST-001 AUDIT_DECOMP
backcheck, and return for human confirmation; do not change
_ScopeChange/_LATEST.md, companion registers, scope, topology, mappings,
counts, substantive requirements, DEL packet/N0, runtime/client/project state,
lifecycle/release/reliance, Task Management, or Git, and do not confirm or
close SCA-003.
```
