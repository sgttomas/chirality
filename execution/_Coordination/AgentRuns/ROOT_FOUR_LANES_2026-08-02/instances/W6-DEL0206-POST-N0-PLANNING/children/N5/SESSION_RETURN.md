# W6 manager capture — N5 read-only adversarial return

- Runtime child: `/root/w1_del0206/n5_w6`
- Runtime parent: `/root/w1_del0206`
- Launch brief SHA-256: `ba94ee032bcdaacecc38e3f257a5e10f93dfb8551f4f792da0986758ad71f669`
- Governing brief SHA-256: `632d2cbefac9003f36d9d722374b22fdeca5d0da45e637acf7335c8a7d872121`
- Verdict: `RETURN`
- Coverage: `18/18` declared inputs read fully and hash-verified; N4 outputs `7/7` reviewed.
- Writes/repair: none.

## Finding ledger

| ID | Severity | Finding | Evidence | Affected outputs | Required disposition |
|---|---|---|---|---|---|
| `N5-F01` | `BLOCKING_FOR_ADOPTION` | The degraded-mode delta neither supplies the complete ten-condition degraded-mode candidate required by the accepted Scope of Work nor binds itself as a delta to the accepted base candidate's exact bytes. Preservation of the accepted degraded-mode floor is therefore unproven. | `ScopeOfWork.md` AC-003 and its Evidence Matrices section require ten independent rows with boundary, behavior, recovery, class/open item, retry, redaction/evidence, and verification fields. `DEGRADED_MODE_DELTA_CANDIDATE.md` has no one-to-one matrix. Accepted base candidate SHA-256 `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917` appears nowhere in N4 output. | Primary: `integration/DEGRADED_MODE_DELTA_CANDIDATE.md`; consequential: `integration/N4_SELF_CHECK.md` and `integration/N4_RETURN.md`. | Return N4. Produce a complete ten-condition candidate or an exact base-hash-bound delta proving one-to-one preservation of all ten rows, including unresolved class, retry, redaction/evidence, and verification fields. N5 performs no repair. |

Other adversarial checks passed: REC-001..018; D1-D9; TBD/OD6 001..016; all accepted N1-N3 findings; P0-P9; eight terminal classes; client/PEC boundaries; and absence of false execution, adoption, implementation, lifecycle, release, closure, or reliance claims.

Tool/effect statement: non-shell Node reads, hashes, JSON parsing, and in-memory comparisons only. No write, repair, shell, network, executable check, runtime execution, delegation, Git, dispatch, adoption, lifecycle, release, reliance, or foreign-loop effect.
