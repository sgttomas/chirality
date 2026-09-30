# Additive replay and process errata

This note preserves the hash-bound audit and historical T3 records unchanged.
It applies the independent V0 dispositions and the owner's current evidence
direction; it does not retrospectively qualify a historical gate.

## Replaying the historical audit — AUD-REV-N1

The old script's `BASE` label does not validate working-tree inputs. For an
actual replay of that audit, ROOT should supply a fresh, clean Git worktree at
`3bddc2b05f6106e969c7cf43373b230845c7cc66` (the #1064 merge). That tree contains
the audit script from `7fd632f60ee0d4eeb0429ff4dbd2193eaeeb5d6d` and the original
input snapshot from `74b3c7313491f27f71c4361d5e1657ee4a39e2f1`.

Before replay, verify the exact HEAD and clean working tree, the audit packet's
SHA256SUMS, the script's blob identity against its own revision, and every
principal input hash in `AUDIT/_run_records/basis.json`. Use a fresh worktree
without inherited build/cache output. Preserve Python/tool versions and results
in a new folder. If identities differ, refuse the historical replay label or
explicitly classify the result as a new analysis. Git materialization belongs to
ROOT, not TASK. No later current-main run acquires the old basis merely because
the script prints its constant. V0 independently reproduced the original data.

## Checksum bases — AUD-T3-02

Run each original SHA256SUMS from its containing folder except these five,
whose base is the named parent:

| Manifest beneath T3 | Working directory beneath T3 |
|---|---|
| `REVIEW/_run_records/SHA256SUMS` | `REVIEW` |
| `DESIGN_NUMERICS/_run_records/SHA256SUMS` | `DESIGN_NUMERICS` |
| `DESIGN_STANDING/_run_records/SHA256SUMS` | `DESIGN_STANDING` |
| `REFERENCES/_run_records/SHA256SUMS` | `REFERENCES` |
| `REFERENCES_ELOAD/_run_records/SHA256SUMS` | `REFERENCES_ELOAD` |

The audit and V0 independently verified all 90 original manifests/9,088 entries.
These results identify the checked snapshot, not a timeless pass for future edits.

## Historical Git exceptions — AUD-T3-03

Preserve the separate categories and their original return/ruling evidence:

- S11-K, K2b and K6 disclosed intent-to-add/reset pairs contrary to their normal
  TASK restrictions; their reported nil net effect is not evidence of no write.
- K6b disclosed a fetch, which changes remote-tracking state; it is distinct
  from a commit/index change.
- S11-K's later fast-forward was expressly permitted by its repair brief.

The current response assigns all Git/index mutations to ROOT, including fetch
and staging. Actual native parentage, supplied briefs and returns are recorded.
No assertion of an unseen complete historical command history is made.

## Historical raw evidence — AUD-T3-04

Use `instances/ENV-EVIDENCE/RECOVERY_LIST.md` for exact original identities and
the named missing files. The owner's current direction is in
`decisions/03_OWNER_EVIDENCE_AND_A0_PREPARATION.md`. Recovery is not a prerequisite
to the current numerical investigations. Missing M5 originals remain explicitly
unavailable-for-now; newly recreated inputs and reruns receive new evidence
identities. Preserve original hashes/summaries and do not fabricate old outputs.
