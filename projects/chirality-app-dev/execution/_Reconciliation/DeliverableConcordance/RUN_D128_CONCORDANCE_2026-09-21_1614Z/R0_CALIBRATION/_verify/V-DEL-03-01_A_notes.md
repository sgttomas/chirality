# V-DEL-03-01_A — verifier shard notes (R0 calibration, unit V)

Ledger: `R0_CALIBRATION/DEL-03-01_A/` (worker A). The paired `DEL-03-01_B/` was not read.
Evidence was read at the frozen tree `00115c719`. The only git use was read-only
`log`/`show` (pickaxe on SPEC, the port and types; `show` of `95364569a^` and the four
post-v3.0.1 commits).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 47 | 36 | 7 | 4 |
| b | 3 | 3 | 0 | 0 |
| c | 1 | 1 | 0 | 0 |
| **Total** | **51** | **40** | **7** | **4** |

- **REFUTED:** 6 on DirectionEvidence (CLM-003.4, 011, 013.2, 018, 019, 022) and 1 on
  CauseTag (CLM-025). No Disposition was refuted.
- **CONTESTED:**
  - Disposition: CLM-009.8 and CLM-010.
  - CauseTag: CLM-009.10.
  - MechanicallyUnblocked: REM-2.
- **PostReleaseBasis:** `NO` holds on every selected row.
  - I checked `git show --stat` for `da95ec194`, `cb08dbe2f`, `9ecbdecdf` and `ccb95e06a`.
  - The only cited file any of them touched is `app-owned-composition.ts`, in
    `da95ec194`.
  - That diff has no `engines.register` line on either side.
  - This agrees with the reverse-notes revisit.

## (ii) Systematic patterns

1. **Misattributed CONTEXT DirectionEvidence for the Codex conformance gap.** This caused
   6 REFUTED rows and part of the CLM-009.8 finding.
   - Affected keys: CLM-003.4, 009.8, 011, 013.2, 018, 019, 022.
   - They cite A2 `HANDOFF.md` L126-128 ("runtime-conformance-v2.ts removed
     deliberately") to explain why the Codex adapter is not an engine-conformance subject.
   - The removed file (`git show 95364569a^:…/runtime-conformance-v2.ts`) contains payload
     manifest, native-profile and supply conformance code. It has no
     `runEngineConformance` or `AgentEnginePort` content.
   - So the correct DirectionEvidence is `NONE_FOUND`. The GOVERNING replacement is
     CONTRACT K-ENGINE-3 plus VALIDATION_STRATEGY L125 (the S-1..S-8 functional checks on
     the production path).
   - CauseTag `CODEX_SOLE_ENGINE` and the PARTIALLY_IMPLEMENTED dispositions still hold.
   - The S-1..S-8 basis also makes CLM-009.8's LOW self-flag genuinely two-sided:
     DOCUMENTED_UNIMPLEMENTED or PARTIALLY_IMPLEMENTED.
2. **GOVERNING records placed in DirectionEvidence.** This is a convention ambiguity, not
   refuted.
   - Affected keys: CLM-002, 003.3, 004.3, 008, 009.11, 012.2, 017, 021, 023, REGISTER-3
     and REGISTER-4.
   - They cite D-APP-127 or the decomposition in DirectionEvidence. The rulebook defines
     that field as the CONTEXT record.
   - D-APP-127 does explain the divergence, and MR-8 was applied correctly: the SoW text
     never acknowledges the gate, so the rows are STALE_SPECIFICATION, not
     ACCEPTED_DIVERGENCE.
   - Proposal: allow a GOVERNING citation in DirectionEvidence, or add a
     `GoverningExplanation` column.
3. **Several causes collapsed into one CauseTag, and inconsistent handling of stale
   CONTEXT_CLAIMs.**
   - Keys with mixed causes: CLM-009.10 (resume gap is PRE_V3_DRIFT; Codex subject gap is
     CODEX_SOLE_ENGINE), CLM-017 and CLM-025.
   - CLM-025 is refuted: its stale content (optional `interrupt?`, adapter-side
     `turn.accepted`) is pre-v3 drift from 2026-07-22 (`4412157d1`), not A2_TOPOLOGY.
   - Stale CONTEXT_CLAIMs are handled inconsistently. CLM-023 and CLM-025 are
     STALE_SPECIFICATION, but CLM-010 (which embeds the false "REF-006 is reconciled"
     assertion) and CLM-024 (obsolete probe-TBD preference) are NOT_AUDITABLE.
   - This repeats the worker's own method-friction item: the rulebook should state
     whether STALE_SPECIFICATION is allowed on a CONTEXT_CLAIM.

Minor:

- **Line citations.**
  - Decomposition "L303" (CLM-002, CLM-008) is the numbering at pin `d6f6cadb2`; at the
    frozen tree the row is L317.
  - CLM-012.1 cites `runtime_engine_contract.md` L359; the line is L354.
- **MR-2/MR-6 on REM-2** is CONTESTED. The worker self-flagged it:
  - YES if App code counts as the gate's source;
  - UNKNOWN if only App status surfaces count.
- **Reverse-notes revisits** (CLM-012.2, CLM-019, REGISTER-1, CLM-009.9, CLM-021/003.4)
  were checked and accepted. The Section 9 linkage exists by ID only: its `evidenceFiles`
  entry is legacy `agent-runtime-contract.ts`, imported only by the legacy
  `sdk-message-mapper` and its test. CLM-019's note overstates the linkage.
- **Evidence the worker did not cite:**
  - For CLM-004.1 and 009.7: `event-schema.ts:44` makes `codex.notification` a canonical
    HarnessEvent type. This strengthens PARTIALLY_IMPLEMENTED and resolves CLM-009.7's LOW
    self-flag.
  - For CLM-004.2 (the worker did not diff the route shape): `V3TurnRequest` is additive
    over `TurnRequest`, which supports ALIGNED.
- **AssessmentEvidence.** Parentheticals appended to the token (for example
  "NOT APPLICABLE (no direct conclusion)") appear throughout. This is consistent with MR-9
  and is not counted as an issue.

## (iii) Effort

- **Files read:** about 30 files or ranges:
  - the SoW (in full), `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `Dependencies.csv`,
    and `_DEPENDENCIES.md` (grep);
  - the INSP-03 assessment;
  - SPEC §10-11 and header;
  - CONTRACT K-ENGINE;
  - VALIDATION_STRATEGY and PLAN excerpts;
  - D-APP-127 excerpts and a `_REGISTER.md` grep;
  - HANDOFF L120-130;
  - the port, conformance, types and event-schema excerpts;
  - the composition and delegated-adapter greps, the turn-coordinator range, and the turn
    route;
  - the `daemon-harness-port` excerpt, the Section 9 manifest, and
    `runtime_engine_contract.md` greps;
  - test-name greps;
  - hash computation for 7 reference files.
- **Git:** about 8 read-only log/show calls.
- **Context:** moderate, not tight. Shared evidence (port, SPEC 10-11, D-APP-127, HANDOFF)
  covered most rows.
