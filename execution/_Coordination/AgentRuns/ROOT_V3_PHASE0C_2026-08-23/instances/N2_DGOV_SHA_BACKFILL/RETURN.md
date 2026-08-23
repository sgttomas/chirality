# Return — N2 D-GOV-34 / D-GOV-35 SHA backfill

InstanceID: `N2_DGOV_SHA_BACKFILL`
Role: Agent 2 ephemeral generalist (`role not mechanically enforced`; evidence instruction-asserted)
Basis: `8635e40995b05f494ae35c6083dabdd50068bb52`
Verdict: `PASS — CONTENT COMPLETE; PARENT COMMIT AND POST-COMMIT CI-FORM G4 RERUN REQUIRED`

## Result

The two decision records now carry the Git-act identities authorized by the
Phase-0c N2 steer. D-GOV-35 also carries the prescribed effective status, and
its live register row no longer says that the three Git acts are pending.
D-GOV-34's register row was not changed because it carries no affected SHA or
publication-pending text.

The live tranche manifest records the N2 steer section byte-for-byte in
`m2_gate.authorization`, pins the current-main basis, keeps the PR human-gated
with `self_merge: false`, records M6 notice disposition `pending`, and defers
the `exports/chirality-app/**` derivative.

## Evidence-bounded SHA derivation

### D-GOV-34

| Slot | Value | Recorded basis |
| --- | --- | --- |
| `CandidateSHA` | `8e704f2b63302c8568c48f8fee7c4681e3ec4262` | Receipt 113 names this exact N3 D-GOV-34 commit at `execution/_Coordination/LOOP_RECEIPTS.md:3689-3695`; the originating run repeats it at `HANDOFF_STATE.md:9` and `VALIDATION.md:15-16`. |
| `PublicationSHA` | `d1a53697e6b7f54dcdb5862357bd0b395f51fff2` | Receipt 113 records PR #607 and that terminal results belong to the final head after the receipt commit at `execution/_Coordination/LOOP_RECEIPTS.md:3703-3708`; run publication evidence says the same at `VALIDATION.md:40-46`. The recorded Git merge object for PR #607, `9f95250e4091a789ca82fb207deec6471d7044d1`, has this commit as its second parent; the commit subject is `record receipt 113 and root handoff`. |
| `EffectiveSHA` | `9f95250e4091a789ca82fb207deec6471d7044d1` | The recorded Git object is `Merge pull request #607 from sgttomas/codex/root-del0206-acceptance-governance-20260821`, with parents `bc1228ca1519f0aad14c4c261c84a65f13a3fece` and the PublicationSHA above. Receipt 114 begins the next Root receipt on later `main` at `execution/_Coordination/LOOP_RECEIPTS.md:3715-3720`; Git ancestry proves that basis and current `main` contain the merge. |

All three objects resolve as `commit`. Candidate is an ancestor of
PublicationSHA; PublicationSHA is the PR-merge second parent and an ancestor
of EffectiveSHA. No semantic-content inference was used.

The steer does not authorize a replacement D-GOV-34 status string, so its
existing `Status: RULED — CANDIDATE IMPLEMENTATION PREPARED; PUBLICATION
PENDING` line remains unchanged even though the Git-act slots are now
backfilled. The record's historical convention/publication-posture prose also
remains untouched under the slot-only edit boundary. This is an explicit
non-inferred limitation, not a missing SHA blocker.

### D-GOV-35

| Slot | Value |
| --- | --- |
| `CandidateSHA` | `294e846bc762b96ac780d49f0137f61eb4dde779` |
| `PublicationSHA` | `ade6ecf33d4e10dab1441aeedb240061e140ff1b` |
| `EffectiveSHA` | `8deca1489a3e5921288f71d4960d555e183a6f3f` |
| `Status` | `RULED — APPLIED 2026-08-22; EFFECTIVE 8deca1489…` |

All three objects resolve as `commit`; CandidateSHA is an ancestor of
PublicationSHA, and the PR #622 merge object has PublicationSHA as its second
parent. The register's D-GOV-35 row now records the same three full SHAs and
effective state. Historical record-convention/publication-posture prose was
not rewritten because the N2 check surface authorizes only declared SHA/status
slots.

## Exact slot/status diffs

`D-GOV-34_change_clean_basis_lane_routine.md` changes three lines only:

```diff
-CandidateSHA: TBD
-PublicationSHA: TBD
-EffectiveSHA: TBD
+CandidateSHA: 8e704f2b63302c8568c48f8fee7c4681e3ec4262
+PublicationSHA: d1a53697e6b7f54dcdb5862357bd0b395f51fff2
+EffectiveSHA: 9f95250e4091a789ca82fb207deec6471d7044d1
```

`D-GOV-35_delegated_harness_native_class.md` changes four lines only:

```diff
-Status: RULED — APPLICATION TRANCHE PREPARED; PUBLICATION PENDING
+Status: RULED — APPLIED 2026-08-22; EFFECTIVE 8deca1489…
-CandidateSHA: TBD
-PublicationSHA: TBD
-EffectiveSHA: TBD
+CandidateSHA: 294e846bc762b96ac780d49f0137f61eb4dde779
+PublicationSHA: ade6ecf33d4e10dab1441aeedb240061e140ff1b
+EffectiveSHA: 8deca1489a3e5921288f71d4960d555e183a6f3f
```

`_REGISTER.md` changes exactly the D-GOV-35 row: its affected status/SHA text
now records APPLIED/EFFECTIVE and the three full SHAs. The D-GOV-34 row is
byte-identical to basis.

## Output identities

| Path | SHA-256 |
| --- | --- |
| `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md` | `e300923a42a233619c9425b324ad309d79d8441e0613e4408e29ca17a294d3f2` |
| `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md` | `e7c1e532a9d46cdc27957c85003515c46b5193e21438c905cf1cfb4e56433efa` |
| `docs/governance_harness/_DECISIONS/_REGISTER.md` | `a9ffd0e3c07300bd22080ddc65bb1f10c834f8c7220092afd9a457b0349f1882` |
| `docs/governance_harness/tranche_manifests/ROOT-DGOV34-DGOV35-SHA-BACKFILL-2026-08-23.yaml` | `91841b2ec68a8522129902ab90068e19d2008cc41e13b0863351ee2c49dd1609` |

## Validation

- Basis identities: `HEAD == origin/main == 8635e40995b05f494ae35c6083dabdd50068bb52`; basis `AGENTS.md` SHA-256 is `377a93c13dc8e727c2fb38b6ace5c0dd62833fff3ec50753ebe58d57937a9fc3`; both decision-record pre-hashes matched the steer.
- Manifest authorization exact comparison against the N2 steer section: `PASS` (`1789` bytes on both sides).
- Direct `validate_manifest` on the new manifest: `failures=[]`; only the expected pending-M6 informational note.
- `validate_instruction_tranche_manifest.py` CI mode: `PASS`, 45 schema-valid manifests.
- Required CI-form G4 command before a node commit: exit `0`, 45 schema-valid manifests, but correctly reports `0 changed path(s)` and `0 manifest(s)` because `HEAD` is still the basis and this sealed node is forbidden to commit. The parent must rerun the exact command after the N2 commit; only that post-commit run can prove candidate-range coverage.
- `validate_agent_instructions.py`: `34 files, 0 errors, 0 warnings`.
- `validate_instruction_entrypoints.py`: `PASS`.
- `validate_candidate_whitespace.py --base-ref origin/main`: `PASS`.
- `git diff --check`: `PASS`.
- Object/type/ancestry checks for all six Git-act SHAs: `PASS`.
- Record diff shape: D-GOV-34 `3/3`, D-GOV-35 `4/4`, register `1/1`; no other tracked N2 content path differs.
- `git diff origin/main -- AGENTS.md agents`: empty.

## Write set

Content writes:

1. `docs/governance_harness/_DECISIONS/D-GOV-34_change_clean_basis_lane_routine.md`
2. `docs/governance_harness/_DECISIONS/D-GOV-35_delegated_harness_native_class.md`
3. `docs/governance_harness/_DECISIONS/_REGISTER.md` — D-GOV-35 row only
4. `docs/governance_harness/tranche_manifests/ROOT-DGOV34-DGOV35-SHA-BACKFILL-2026-08-23.yaml`

Control-plane writes are limited to this instance folder (`RETURN.md` and
terminal `STATUS.json`, in addition to the parent-created launch brief).

## Derivative disposition, blockers, and next owner

- `exports/chirality-app/**`: `deferred`; no export bytes changed.
- M6 notice: `pending`, `routed_to: []`; HELP_HUMAN owns the fan-in disposition.
- Content blocker: none.
- Required parent actions: fresh review, N2 commit after N1, post-commit CI-form
  G4 rerun, integrated closeout/Receipt 116, push, and human-gated PR. This
  return authorizes none of those acts and no merge.
