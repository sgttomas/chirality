# SCA-004 Gate-5 application-append slot inventory

Status: `DRAFT — AWAITING OWNER APPROVAL OF APPEND BYTES`

Basis: the seven exact Gate-3 candidate files approved by owner ruling R3-A.
This inventory is exhaustive for current SCA-004 candidate-status assertions.
A slot is text-status metadata only. No row identity, mapping, count, ID,
parent binding, scope/objective allocation, or trace datum is a slot.

## Inventoried slots

| Slot | File | Exact candidate locator | Before | After |
|---|---|---|---|---|
| WS-001 | `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` | line 1, title | `# Chirality Root — Software Decomposition (SCA-004 CANDIDATE v1.3)` | `# Chirality Root — Software Decomposition (v1.3 — ACCEPTED CURRENT BASIS)` |
| WS-002 | same | line 6, `Revision` | `v1.3 (SCA-004 Gate-3 candidate — not approved or applied)` | `v1.3 — ACCEPTED CURRENT BASIS` |
| WS-003 | same | line 10, `Run` | Phase-0c candidate-run identity | Gate-5 authorization `TBD`, Git effect `TBD`, later-recorded-act convention, Phase-0d package run, and predecessor candidate run |
| WS-004 | same | line 11, `Amendment` | exact Gate-3 candidate; Gate-3/Gate-4 approvals pending; no live effect | revision 1.3 applied from R3-A-approved bytes plus append approval `TBD`; R3-B condition carried; Gate-5 authorization/Git effect `TBD` |
| WS-005 | same | lines 13–23, status blockquote | Gate-3 candidate not approved/applied; revision 1.2 remains live; later Gate-5 required | revision 1.3 accepted current basis; R3-A/R3-B approvals; Gate-5 authorization and Git effect `TBD`; later backfill; pointer treatment pending its own authority |
| WS-006 | same | line 285, Deliverables responsibility sentence | `seven SCA-004 candidate rows` | `seven applied SCA-004 rows` |
| WS-007 | same | line 419, `Revision / Date` cell | `v1.3 SCA-004 candidate / 2026-08-23` | `v1.3 applied revision 1.3 / 2026-08-23` |
| WS-008 | same | line 494, OI-011 row | two current-status references to SCA-004 candidate rows | two applied-revision references preserving the same responsibility assignment |
| WS-009 | same | line 579, DEC-025 row | Gate-3 candidate; R2-A drafting-only; no live authority before approvals/application | revision 1.3; R3-A/R3-B recorded; append approval, Gate-5 authorization, and Git effect `TBD` |
| WS-010 | same | lines 644–651, SCA-004 change-log entry | Gate-3 candidate; R2-A drafting only; approvals/application remain required | revision 1.3 applied; R3 approvals recorded; append/Gate-5/Git slots `TBD`; pointer authority pending |
| SL-001 | `chirality_root_scope_ledger_v1_0.csv` | row 84 (`SOW-083`), column `Notes` | `This candidate's bidirectional traceability registers are the artifact F4 is checked against.` | `Applied revision 1.3's bidirectional traceability registers are the artifact F4 is checked against.` |
| SL-002 | same | row 104 (`SOW-103`), column `Notes` | `Boundary item; the present run is the decomposition candidate and accepts nothing.` | `Boundary item; applied revision 1.3 does not itself materialize any folder or change the public-export boundary.` |
| TEL-001 | `chirality_root_coverage_telemetry_v1_0.md` | line 5, `Revision` | `v1.3 SCA-004 Gate-3 candidate` | `v1.3 — applied revision 1.3` |
| TEL-002 | same | lines 6–7, `Status` | candidate only; revision 1.2 live until approvals and Gate-5 | applied revision 1.3; R3-A/R3-B; Gate-5 authorization/Git effect `TBD`; later backfill; pointer authority pending |
| TEL-003 | same | line 20, base-telemetry `Revision` cell | `v1.3 (SCA-004 Gate-3 candidate)` | `v1.3 (applied revision 1.3)` |
| TEL-004 | same | line 126, reverse-trace status prose | `candidate scope ledger` | `applied scope ledger` |
| TEL-005 | same | lines 128–129, reverse-trace status prose | `candidate objective register`; `candidate PackageIDs` | `applied objective register`; `applied PackageIDs` |
| TEL-006 | same | line 162, OI-011 row | `seven SCA-004 candidate rows` | `seven applied SCA-004 rows` |

The exact, full before/after bytes—including the complete multi-line text for
WS-003 through WS-005, WS-008 through WS-010, and TEL-002—are the corresponding
zero-context hunks in `Gate_5_Application_Append.diff`. The applied side is
also materialized in `Gate_5_Applied_Candidate/`; no prose abbreviation in
this inventory replaces those exact bytes.

## Literal `candidate` occurrences classified as non-slots

The following CSV cells also contain the word `candidate`, but do not assert
the current package's candidate posture and therefore remain byte-identical:

- deliverable register rows 41, 49, and 52 (governed SHA-role and promotion-path definitions);
- objective register row 6 (OBJ-005 governed promotion statement);
- forward trace row 3 (historical D-GOV-25 `AcceptedCandidateSHA` evidence);
- scope ledger rows 23, 38, 55, 65, 72, 74, 96, and 97 (normative statements about candidate documents, packets, SHAs, or promotion).

Historical candidate-era prose in the working surface (D-GOV-25,
SCA-002/SCA-003 history, and generic promotion-path language) is likewise not
a current-status slot and is preserved. This exclusion is required to avoid
rewriting history or changing governed scope statements.

## Boundary

`Gate_5_Application_Append.diff` changes only the 18 slots above. It changes
no other byte semantically, and in particular changes no counts, identifiers,
row sets, mappings, package parents, scope/objective allocations, or traces.
