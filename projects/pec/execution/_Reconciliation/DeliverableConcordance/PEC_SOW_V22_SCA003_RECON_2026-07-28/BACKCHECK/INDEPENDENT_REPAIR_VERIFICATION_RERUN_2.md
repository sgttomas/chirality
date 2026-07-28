---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
phase: R4_REPAIR_INDEPENDENT_VERIFICATION_RERUN_2
role: independent_agent_2_verifier
result: FAIL
status_policy: NO_STATUS_TOUCH
rebase_basis: 21e8e54e1f5648b7d3db29228271aaa8c7d8904f
effective_claim_repairs: 57
contracts_examined: 11
unknowns_preserved: 22
authority_conflicts: 0
---

# Independent repair verification — rerun 2

## Verdict

**FAIL.**

The effective 57-claim repair set passes, `DEL-10-11/AX-001` is restored,
the stale `DEL-10-11` lifecycle narrative is corrected, and all eleven
contracts accurately record PR #402 reference parity. One part of the first
post-repair verifier's DEL-10-10 finding remains uncorrected:

> The ordered source chain in `DEL-10-10/ScopeOfWork.md` still omits
> `D-PEC-68`.

The opening `SOW-064` attribution is now correct, but amendment 2 accepted the
prior finding exactly, including the ordered-chain omission. The hold must
therefore remain active pending this final bounded narrative correction and
another independent rerun.

## Verification basis

- Git basis:
  `21e8e54e1f5648b7d3db29228271aaa8c7d8904f`.
- SCA-003 decomposition merge:
  `11a494e9ae0cca795aa460deec19b9eac4d922a8`.
- PR #402 reference-parity merge:
  `af62343d3af95fcd3af0742615cb92a7c813f44a`.
- Effective repair authority: the original 56 W1 repair rows plus
  `W1_DISPOSITION_AMENDMENT_1.md` / `R4_AMENDMENT_1.md` adding
  `DEL-10-11/CLM-002`, for 57 total.
- Rerun correction authority:
  `W1_DISPOSITION_AMENDMENT_2.md`, `R4_AMENDMENT_2.md`, and
  `SOURCE_DRIFT_AMENDMENT_1.md`.
- Current source authority: PRD v2.2, `SOFTWARE_DECOMP.md` revision 1.3,
  current ledgers, local `_STATUS.md`, `_REFERENCES.md`, and dependency
  surfaces.

## Check results

| Check | Result | Evidence |
|---|---|---|
| Effective approved claim population | PASS | 57/57 IDs present across the same 11 contracts |
| Local-definition structure | PASS | 794 current definitions match the original ledger IDs, classes, source order, and per-contract counts |
| Approved repair containment | PASS | 54 approved first definition lines changed; the remaining three approved repairs are continuation-text changes (`DEL-08-04/CLM-002`, `DEL-08-04/CLM-008`, `DEL-10-10/CLM-001`); no unapproved first definition line changed |
| Approved repair semantics | PASS | Current PRD v2.2/SCA-003 consumer ownership, zero-contact, optional-injection, current lifecycle, directed-bootstrap, and ADR-014 historical-only meanings are retained |
| `DEL-10-11/CLM-002` amendment-1 repair | PASS | Exact “measured in observable system and use behavior” heading; parity population, per-reconcile denominator, silences, and unknowns preserved |
| `DEL-10-11/AX-001` restoration | PASS | Current definition is byte-identical to the pre-repair `HEAD` definition |
| DEL-10-11 narrative lifecycle | PASS | Production-method prose now says `INITIALIZED`; `_STATUS.md` independently records `INITIALIZED` |
| DEL-10-10 opening SourceRef | PASS | Lines 83–84 now state `PRD v2.2 §12, D-PEC-61, D-PEC-68` |
| DEL-10-10 ordered source chain | **FAIL** | Lines 89–105 contain PRD v2.2 and D-PEC-61 but no D-PEC-68 entry |
| PR #402 reference parity | PASS | All 11 `_REFERENCES.md` files name revision 1.3/current basis and PRD v2.2; all 11 contract basis notes accurately cite integration `af62343d3`; all 11 frontmatter pins are `11a494e9a` |
| Unknown preservation | PASS | All 22 W1 `UNKNOWN` definition lines remain byte-identical to their immutable W1 ledger text |
| Consumer-duty boundary | PASS | No approved repair creates PEC self-polling, scheduling, unsolicited injection, mandatory contact, receiving-loop conformance, or PEC ownership of consumer mode/cadence |
| Topology and lifecycle mutation | PASS | No selected `Dependencies.csv`, `_DEPENDENCIES.md`, or `_STATUS.md` differs from the rebased Git basis; scope/objective frontmatter mappings remain stable |
| Hold and reliance mutation | PASS | `ACTIVE_RELIANCE_HOLDS.csv` is unchanged and `PEC-HOLD-001` remains `ACTIVE` |
| Implementation/release mutation | PASS | The working diff outside reconciliation evidence is confined to the 11 selected `ScopeOfWork.md` files; no implementation, release, schedule, or estimate surface changed |
| Whitespace | PASS | `git diff --check` is clean for all 11 contracts |

## Exact remaining blocker

The repaired DEL-10-10 introductory attribution is now current:

`DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md:81-87`

> `SOW-064`'s current `SourceRef` is
> "PRD v2.2 §12, D-PEC-61, D-PEC-68"

Its quoted `SOW-064` row and `CLM-004` C16 source field also include all three
references. However, the immediately following ordered source chain reads:

`DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md:89-105`

1. `ScopeLedger.csv`, row `SOW-064`;
2. PRD v2.2 §12;
3. `D-PEC-61`;
4. `SOFTWARE_DECOMP.md`;
5. `Deliverables.csv`;
6. local control files and the accepted gate exhibit; and
7. the two upstream accepted contracts.

There is no entry for
`execution/_Coordination/_DECISIONS/D-PEC-68_prd_v2_2_consumer_interface_concordance.md`.
That omission is the same ordered-chain defect recorded in the preserved first
post-repair report. `W1_DISPOSITION_AMENDMENT_2.md` describes the prior
DEL-10-10 finding as retaining the pre-v2.2 SourceRef **and omitting
`D-PEC-68`**, then accepts correction of that narrative fact. Adding the
current `D-PEC-68` decision to this ordered chain is therefore authorized and
required; it is not a new repair ID or semantic expansion.

## Effective 57-ID set reverified

| Deliverable | Approved repaired local IDs |
|---|---|
| `DEL-00-01` | `OUT-002`, `CLM-002`, `REQ-005`, `AC-003`, `VER-002`, `AX-002`, `AX-004`, `AX-006` |
| `DEL-03-06` | `CLM-016`, `CLM-020`, `AX-012` |
| `DEL-04-01` | `CLM-016`, `CLM-018`, `REQ-010`, `AX-007`, `AX-012`, `AX-013` |
| `DEL-04-02` | `CLM-016`, `CLM-017`, `REQ-013`, `AX-013` |
| `DEL-04-03` | `CLM-016`, `CLM-017`, `AX-011` |
| `DEL-08-01` | `CLM-003`, `CLM-004`, `AX-004`, `AX-006` |
| `DEL-08-03` | `CLM-011`, `REQ-005`, `CON-001`, `CON-003`, `AX-006`, `AX-010` |
| `DEL-08-04` | `CLM-002`, `CLM-008`, `CLM-010`, `CLM-014`, `CON-005`, `AX-012` |
| `DEL-10-01` | `CLM-004`, `CLM-007`, `AX-005`, `AX-007` |
| `DEL-10-10` | `CLM-001`, `CLM-002`, `CLM-004`, `CLM-005`, `CLM-020`, `AX-011` |
| `DEL-10-11` | `CLM-002`, `CLM-003`, `CLM-015`, `CLM-017`, `CON-003`, `AC-015`, `AX-009` |

The only changed definition blocks outside this set are previously accepted
whole-contract bookkeeping adjacent to unchanged definition lines:
`DEL-00-01/CLM-008`, `DEL-00-01/AC-007`, `DEL-00-01/AX-007`,
`DEL-08-03/CLM-005`, and `DEL-10-01/CLM-012`. No new out-of-set definition
change remains; specifically, `DEL-10-11/AX-001` no longer differs.

## Required bounded correction

Add `D-PEC-68` to DEL-10-10's ordered source chain, preserving:

- the current `SOW-064` statement and exact SourceRef;
- the existing order and identity of all other source entries;
- all six approved DEL-10-10 claim repairs;
- every stable ID, mapping, dependency, lifecycle, unknown, hold, and
  no-authority boundary; and
- the PR #402 basis/reference-parity note.

Then run a fresh independent verification. No new repair-set amendment is
needed because amendment 2 already accepts this exact correction.

## Evidence identity and preservation

The contract SHA-256 values examined were:

| Deliverable | SHA-256 |
|---|---|
| `DEL-00-01` | `4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740` |
| `DEL-03-06` | `90de9c2d93d8350805410753a21f19c5cf141e48c3e94ffc8096621b3a42c97e` |
| `DEL-04-01` | `0c38bee95ca99d8a3f1da8155055f84e3c704865f23dc05be44338570d38e53f` |
| `DEL-04-02` | `a2b50f870aa30fb45e06b1f4cf1b300ff522a19490066c1e2d898b9022c0e65a` |
| `DEL-04-03` | `6ec7432bf8cfe86cc973c50b8c2a24a0305c55c7a64522d0c47778050e59ec6d` |
| `DEL-08-01` | `8ac1dc050efbd22530700d140a57944d0f82f48bcb2f9994bee4cddd588a3d76` |
| `DEL-08-03` | `013c615a0c91d7d2545d7dfc0faecfe509b0c7409f450fdefd01125d2aef3138` |
| `DEL-08-04` | `6d1ec1ad9796973656d6d0d60739b4dbf8cd134a2b17c8c878ee2ff4c098222b` |
| `DEL-10-01` | `40d47fb636ca72e52213929b2337dbbc3a02f0f7c073758c996f5d651e1a5a7e` |
| `DEL-10-10` | `dc718f9d7304c3b386c2838bf3553ff6f21bb4f4a5da58756b35e599cf6cc23a` |
| `DEL-10-11` | `9b90f33ba03a07ab829e7743176df48e6b88ca96d0de18d98c16332a7624cdf9` |

The two prior failed reports remain preserved:

- `WAVES/W1/W1_LEDGER_VERIFICATION.md`
  (`b94cca6542ef10d0a43ec8c0c25e14a2b12b2c97243f8f63f230ed6f6fe40317`);
- `BACKCHECK/INDEPENDENT_REPAIR_VERIFICATION.md`
  (`bd68d62b4566eb7db0bc18ce7795734062cdd6fa39d18e9bb95ee5124dff5ba8`).

This report is the sole file written by rerun 2.
