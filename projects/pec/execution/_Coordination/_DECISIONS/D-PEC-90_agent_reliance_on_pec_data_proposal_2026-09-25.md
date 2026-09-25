# D-PEC-90 — Agents act on PEC data: operational reliance without authority

Status: **PROPOSAL / AWAITING_RULING**. Prepared by HELP_HUMAN (run `HELP-HUMAN-PEC-20260923-SCA005`, node H5) for the PEC loop, 2026-09-25 (session date). No earlier direction approves this file. It changes no PRD, instruction, decomposition, ScopeOfWork, product or lifecycle byte, and asks for no lifecycle change. HELP_HUMAN owns the `_REGISTER.md` row.

## Provenance

- **Owner direction (evidence, not a ruling).** The owner asked, 2026-09-25, how agents would use what is being built. HELP_HUMAN answered from PRD v2.2 §8 that agents do not call PEC directly and receive only labeled, non-authoritative data if a harness injects it. The owner replied, verbatim:

  > I think the agent should actually rely upon this data.  I think that's the value and that's why you're building it carefully and programatically.

  The run record node H5 routes this statement here. It is transcribed as evidence of product intent; it amends nothing by itself.
- **Basis read at `origin/main` `088fb7868d3246361e7209dd9276c6b0f8fc75d9`.**

  | Source | SHA-256 |
  |---|---|
  | `projects/pec/docs/PRD.md` (v2.2) | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
  | `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
  | Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
  | Root `docs/PRD_ROOT.md` | `b6fa4e3d5ec5c20a4aa1dbfdfd43bed5a13d8287bc78f4635e3d944fb6c11931` |
  | `_DECISIONS/D-PEC-67_od7_g3_boundary_dispositions.md` | `c04f8ddd90cfe4ca3ecdabad8f48b4820c9952c9c4515655dc8ed21304d9d9a8` |
  | SCA-005 `Impact_Assessment.md` (owner-accepted 2026-09-24) | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
  | DEL-04-01 `ScopeOfWork.md` | `6f4e8c66a5712ba73e5000f1eafbfd5dd821bb4c339a23d77aa46b5b558830ae` |
  | DEL-00-03 `artifacts/v2/SPEC.md` | `cc9f4754ac3d8ab0901fb6099d469c4e8e4557507dd50683ec9389977b0f1bae` |

## The question

PEC's reason to exist is that Step 0 — re-deriving the live work surface from prose — is the most expensive, most repeated computation in the system (PRD §2), and outcome 1 is that orientation becomes "a sub-second query with per-claim citations, not a session-length prose derivation" (§3). The accepted text then requires a consumer to verify PEC data against its cited source before relying on it. If an agent must re-read every cited source, the derivation it was spared comes back, and outcome 1 is not reached. The owner's direction resolves that tension in favour of reliance.

## Two senses of "rely"

This proposal separates two things the current text treats together.

1. **Operational reliance (proposed).** An agent, directly or through its harness, takes a PEC record-tier claim as true *as of the examined-through commit the response carries* and acts on it without re-reading the cited source: what to work on, what is blocked or stale, which gate preconditions hold, what changed since commit X, whose declared scope overlaps. A PEC claim is a deterministic derivation from files at a pinned commit, with its rule, sources and freshness stated (PEC-K-04, PEC-K-08). Relying on it is like relying on `git status`, not like relying on an agent's prose.
2. **Authority (unchanged).** Rulings, acceptance, lifecycle transitions, merges and citations in governed records rest on the file-native record (K-AUTH-1, `D-GOV-01`, Root PRD N-1). PEC may locate the file; the governed record cites the file. PEC-K-01 (deleting PEC blocks no governed act) and PEC-K-02 (PEC output is never citable as authority) stay as they are.

Reliance in sense 1 is bounded by what the response itself declares:

- **Pinned.** The claim holds as of its examined-through SHA. An agent that needs a later state re-queries or reads the file.
- **Coverage-honest.** Where a feed is unparsed, stale or out of coverage, the response says so (PEC-ORI-006), and the agent may not rely on silence.
- **Record tier only for correctness.** Presence-tier facts (sessions, heartbeats, declared scopes) support advisory collision avoidance at their stated heartbeat age; no correctness decision rests on them (PEC-K-05).
- **Fallback.** If PEC is absent, degraded, or fails its own checks, the agent falls back to the files (PEC-K-01 unchanged).

"Reliance" here is distinct from the reliance-hold control of `D-PEC-67` L-A1 (`ACTIVE_RELIANCE_HOLDS.csv`, `pec_reliance_hold.py`), which governs relying on specific requirement clauses for production. This proposal does not touch that control. Any later text should use "operational reliance on PEC data" to keep the two apart.

## What it raises for the product

Once agents act on PEC answers, correctness of those answers becomes load-bearing:

- **Parser correctness** — a wrong parse becomes a wrong action. PKG-02 parsers need the same exactness the content guard received in D-PEC-87/89.
- **Parity** — PEC-RCN-005 parity against the practitioner harness moves from a diagnostic to the condition for reliance at a release (P1 already gates on "parity-diff vs harness clean or explained", §12).
- **Coverage statements** — PEC-ORI-006 becomes a safety property, not a courtesy.
- **Reliance starts at a release, not now.** No PEC consumer surface exists yet (P1 has the store and guard only). Operational reliance would begin at the first release whose gates prove the conditions above.

## Text the change would touch (exact loci; no bytes changed here)

PEC-owned:

| Locus | Current text (abridged) | Needed change |
|---|---|---|
| PRD §6 PEC-K-03 (L177) | "labeled, non-authoritative orientation data … If it injects PEC data, verify-before-rely is an interface precondition" | Replace verify-before-rely with operational reliance within the declared pin, coverage and tier; keep "non-authoritative" in the authority sense; keep pull-oriented, consumer-owned use |
| PRD §8 Agents (L240–243) | "never call PEC directly by instruction … receive orientation as labeled, non-authoritative data only if … inject it" | Allow agents to act on PEC data received through an enabled consumer; decide separately whether agents may query directly (an access-class change, §16 item 6) |
| PRD §9 / §11 / §12 | no reliance requirement or gate | Add a requirement stating the reliance envelope, and a release gate that proves parity and coverage before reliance is advertised |
| `projects/pec/AGENTS.md` L39–42 (K-02 gloss) | "labeled non-authoritative data, verified against its cited source before reliance" | Align with the amended K-03 |
| DEL-04-01 `ScopeOfWork.md` CLM-016, AX-007 | quotes K-03 verify-before-rely | Re-quote after the PRD changes (already `STALE_REBUILD_REQUIRED` under SCA-005) |
| DEL-00-03 `artifacts/v2/SPEC.md` L46 | "an enabled consumer owns use and verify-before-rely" | Re-quote (already `STALE_REVIEW_REQUIRED` under SCA-005) |

Not PEC-owned (notices and separate acts):

- **Root `AGENTS.md` L54–55:** "Search results and derived graphs help locate evidence; reliance remains grounded in the source records and their authority." Arguably compatible — a pinned, cited, deterministic derivation is reliance grounded in source records — but that reading is Root's to confirm. A Root instruction change needs its own authorized scope. PEC sends a notice; Root decides.
- **Root PRD N-1 and `D-GOV-01`:** unaffected. They bar citing projections as authority, which sense 2 keeps.
- **App / runtime consumers:** PEC-K-03 is an exact row adopted under `D-PEC-67` K03-A in coordination with consumer loops. Amending it needs a notice to the App loop; each consumer decides its own adoption (PEC-K-03 and K-11 keep consumer-owned use).

## Relation to SCA-005

SCA-005 already carries a PRD successor candidate that modifies §8 (Harnesses row, INV-013) and PEC-ORI-001 (INV-014), and marks DEL-04-01 `STALE_REBUILD_REQUIRED` and DEL-00-03 SPEC `STALE_REVIEW_REQUIRED`. It does not touch PEC-K-03. Folding this change into checkpoint 2 would add a K-03 amendment and new §9/§12 rows to that candidate and make checkpoint 2 wait on App coordination; running it separately risks DEL-04-01 being rebuilt around the old wording.

## Options

- **R-A (recommended). Adopt the direction now; amend the text in a separate scope change after SCA-005 checkpoint 2.** The ruling records operational reliance (sense 1, bounded as above) as PEC product direction of record, keeps sense 2 unchanged, and authorizes HELP_HUMAN to (i) ask WORKING_ITEMS to carry a NOTE into the checkpoint-2 package so DEL-04-01 and the §8 refresh are not rebuilt around verify-before-rely, (ii) send non-binding notices to Root and the App loop, and (iii) prepare the exact PRD/AGENTS amendment as the next PEC scope change once SCA-005 checkpoint 2 is accepted.
- **R-B. Fold into SCA-005 checkpoint 2.** Same direction; the checkpoint-2 package adds the K-03, §8, §9 and §12 amendments to the PRD successor candidate and regenerates the affected impact rows. Faster to the text; widens checkpoint 2 and ties it to App coordination.
- **R-C. Reliance including authority.** PEC output citable in governed records. Not recommended: it requires amending `D-GOV-01` and Root PRD N-1 (Root governance acts) and gives up the kill test (PEC-K-01), which is what makes a PEC defect slow work down rather than corrupt the record.
- **Amend** (state the change) or **defer**.

## What a ruling on R-A grants and does not grant

Grants: the direction of record above; the NOTE request to the SCA-005 checkpoint-2 preparation; the two notices; preparation of the later amendment.

Does not grant: any PRD, `AGENTS.md`, ScopeOfWork, SPEC, product or lifecycle byte change; any access-class change; any consumer's adoption; any change to the `D-PEC-67` L-A1 reliance-hold control; any Root act. Each of those needs its own act.

## Rollback

Before publication: discard. After merge: a later owner ruling supersedes the direction; nothing downstream has been changed by this record.

## Questions only the owner can answer

1. R-A, R-B, R-C, amend or defer?
2. Should agents eventually query PEC directly (an access-class change), or only act on data an enabled harness passes them?
