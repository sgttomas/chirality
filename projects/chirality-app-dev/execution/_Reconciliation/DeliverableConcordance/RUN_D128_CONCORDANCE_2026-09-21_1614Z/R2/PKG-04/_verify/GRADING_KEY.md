# PKG-04 shared verifier grading key (R2)

One key for every PKG-04 verifier shard (R0 §3 caveat: shards graded the same fact differently).
The rulebook is `CONVENTIONS.md`; this key only fixes how shards grade it. It is a manager method
instrument, not a ruling.

## Verdicts

- `CONFIRMED`: the selected row's Disposition and the checked fields hold under the rulebook, and
  the cited evidence exists at the frozen basis (path and line resolve; ±3 lines drift tolerated
  when the content is the one described).
- `REFUTED`: the rulebook, applied to evidence at the frozen tree, clearly gives a different value.
  Give the correct value and the evidence. Say in `Field` which field; a Disposition refutation is
  `Field = Disposition` even if other fields are also wrong (list them in CorrectReading).
- `CONTESTED`: the rulebook admits both readings, or the evidence is genuinely ambiguous. Give both
  readings separated by ` || `. Do not use CONTESTED for a value you judge wrong.
- **Errata rows (class e):** grade the **ProposedValue**. CONFIRMED = the erratum is correct (the
  sealed value was wrong and the proposed value is right); REFUTED = the sealed value should stand
  or the proposed value is also wrong; `RowValue` = the SealedValue, `CorrectReading` = your value.
- **Reverse responses (class c):** grade whether the capability is owned (CLAIMED_BY) or partly
  covered (PARTIAL) by the named ClaimKey, per CONVENTIONS §5.1, and whether the capability row's
  own REACH/STATE tags hold at the frozen tree (flag in ConventionIssue if not).

## Fixed readings (apply identically)

1. **Reach (§2.3).** `REACHABILITY.csv` is module-level: a barrel re-export, or one symbol imported
   by live code, can mark a module LIVE while the cited symbol is reached only from tests or legacy
   code. Grade the tag at **symbol level** by following importers at the frozen tree. A wrong tag
   alone is a field-level refutation (`ImplementationEvidence`); it refutes the Disposition only if
   the corrected reach changes it under the §2.3 rule.
2. **Legacy versus live (§2.3).** A requirement stated as product behaviour ("the App/system shall…",
   user- or system-observable) is judged on the **live** path: PARTIALLY_IMPLEMENTED /
   IMPLEMENTED_DIFFERENTLY / DOCUMENTED_UNIMPLEMENTED as the live path covers it. A claim whose
   subject is the retained module itself ("SdkOptionsBuilder does X") may be judged at module level
   with its REACH tag. Where the SoW text supports both subjects, grade `CONTESTED`, not REFUTED.
3. **Authority (§1).** App `docs/PRD.md` and `docs/CONTRACT.md` (and SPEC where present) open with a
   GOVERNING "Current Codex-only MVP release basis" preamble saying Claude/Anthropic and Pi/oMLX
   text is compatibility history. Check App `docs/DIRECTIVE.md` §0 (authority order) yourself.
   `AUTHORITY_CONFLICT` is correct only when two GOVERNING texts conflict and §0 does not resolve
   it, or a ruling undercuts an unamended GOVERNING clause without naming it. If §0 resolves it, the
   row should cite both and take the resolved Disposition (often STALE_SPECIFICATION). Where the
   worker's reading of §0 is defensible either way, CONTESTED.
4. **MR-11** applies only when the ruling explicitly addresses the clause or deliverable.
5. **DirectionEvidence (§2.3).** `CTX:` for CONTEXT sources (RUN_BASIS §5), `GOV:` for a GOVERNING
   ruling that itself explains the divergence; `NOT_APPLICABLE` on ALIGNED/NOT_AUDITABLE. A
   `NONE_FOUND` is refuted if `_DECISIONS/_REGISTER.md` or a CONTEXT source records the direction.
   A GOVERNING source under `CTX:` (or vice versa) is a field refutation.
6. **CauseTag (§4)** precedence: mechanism first; PRE_V3_DRIFT for divergence already present before
   2026-08-22 unless a named v3 mechanism applies; UNRECORDED_JUDGMENT only with DirectionEvidence
   `NONE_FOUND`. Two defensible mechanisms → CONTESTED.
7. **AuthorityTier (§2.3):** highest source restated; NOT_APPLICABLE only for CONTEXT_CLAIM and for
   STATE_ASSERTION/REGISTER_DEFECT rows restating no normative source.
8. **PostReleaseBasis:** `YES` iff a relied-on line in a file on `TOUCHED_PATHS.csv` blames to one of
   the four commits (`git -C <FROZEN_TREE> blame -L`). Check any cited touched file.
9. **MechanicallyUnblocked (§2.5):** REMAINING_WORK rows only; gate on a retired premise → `NO` with
   `MOOT:<ruling>`; `NO` on every other row.
10. **AssessmentEvidence:** exactly one of OVERTAKEN / STILL CURRENT / NOT APPLICABLE; STALE_ASSESSMENT
    only where the overtaken conclusion is the operative defect.
11. **Register rows:** REFERENCES hash drift is one REGISTER row per deliverable cited with
    `HASH-RECOMPUTE@00115c719`; snapshot-true claims (MR-8 iv) are REGISTER rows.
12. **HumanDecisionNeeded:** rows turning on retained-harness status cite `R4-Q1`, Codex
    conformance `R4-Q2`, legacy `status_transition` actor `R4-Q3`; plain `R4` only for unframed
    questions.
