# V-DEL-01-01 — verifier shard notes (DEL-01-01)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT, LOW/self-flag) | 5 | 5 | 0 | 0 |
| a30 (sampled non-ALIGNED) | 8 | 7 | 0 | 1 |
| b (sampled ALIGNED) | 6 | 6 | 0 | 0 |
| c (reverse PARTIAL) | 8 | 8 | 0 | 0 |
| e (errata, CLM-004.1 ImplementationEvidence and Notes) | 2 | 2 | 0 | 0 |
| **Total** | **29** | **28** | **0** | **1** |

Verdict-field refutations: 0. CONTESTED on a verdict field: 1 (CLM-021.6 Disposition).

## (ii) Patterns

- **Authority routing (grading key 4) holds on all four AUTHORITY_CONFLICT rows.** CLM-009.7,
  CLM-021.5, CLM-023 and STATE-1 do not treat the CONTRACT/PRD Codex-only preambles as overriding
  App DIRECTIVE. They route by §1 bullet 3. D-GOV-43 preserves "the Codex sole-engine rule"
  (D-GOV-43.proposed.md:26-27, 303) and prescribes faithful transport (item 2). Its surface list
  names only Root DIRECTIVE §5/§7 (:348), and IMPACT.md's App row lists PRD/SPEC/CONTRACT/PLAN/TYPES
  but not App DIRECTIVE. No App register row names App DIRECTIVE §2.8 or §2.10. So a ruling undercuts
  an unamended higher clause without naming it. MR-11 does not apply, and the §0 order is displaced
  by that ruling.
  - R4-Q5 fits the event-shape rows (K-ENGINE-4 and DIRECTIVE §2.10 versus amended K-EVENT-1/6).
  - R4-Q1 is correctly added by subject-test rule 3: the only code that meets the SoW reading
    (`sdk-message-mapper.ts`, `chirality-hooks.ts` and the others) is LEGACY_ONLY.
  - STATE-1's extra plain `R4` covers App DIRECTIVE §2.8 (Claude default) versus K-ENGINE-3. No named
    question frames that exactly, and R4-Q1 is also cited, so I accepted it. A stricter reading could
    fold it into R4-Q1.
  - CLM-004.4 (PARTIALLY_IMPLEMENTED, R4-Q1) is partly met by LIVE code. I accepted R4-Q1 because the
    containment, hooks and settings parts are met only by LEGACY_ONLY modules, and R4-Q1 names
    K-PATH/K-HOOK.
- **Reference-integrity rows follow the §2.6 tie-break consistently.**
  - STALE_SPECIFICATION with `SEE:REGISTER-1` on text that restates the MATCH as current: CLM-003,
    CLM-017, CLM-022.
  - ALIGNED on CLM-015, whose text is tied to the snapshot ("the current D-APP-38 corpus snapshot
    records REF-006 MATCH"). This is literally true: AUTHORITY_CORPUS.json has current_version v23,
    which records 8649ccba.
  - The one open item is CLM-021.6 (Principle 6, SEE CLM-009.8). It is STALE_ASSESSMENT on an
    overtaken Checklist C-08 PASS. The operative defect is arguably the deliverable text that smooths
    over drift, which argues for PARTIALLY_IMPLEMENTED or STALE_SPECIFICATION, so I graded it
    CONTESTED. The same question applies to CLM-009.8, which is outside this shard.
- **The erratum is sound.** `WovenDialogueRoute` discards its `legacy` prop
  (woven-dialogue-route.tsx:18), so `workbench-surface.tsx` is never mounted. Its REACHABILITY tag,
  LIVE via app/chat/page.tsx, is a module-level false positive (grading key 3). The served transition
  route (route.ts:52-66 → transition.ts:88-117, 170-176) still enforces HUMAN plus approvalSha, so
  ALIGNED stands.
  - status-parser is genuinely executed: app/layout.tsx → DeliverablesProvider →
    /api/project/deliverables. That supports CLM-004.5, CLM-009.4 and CLM-021.2.
- **Minor anchor observation, not refuted.** STATE-1 cites app-owned-composition.ts:169
  (`new SessionStore`) as evidence that "the live engine is Codex only". The Codex host and supervisor
  are at :161-165 and :171, within the 1–6-line drift allowance of grading key 1. Lines 170-171 blame
  to da95ec194 (TOUCHED_PATHS), so if the relied-on line were :171, PostReleaseBasis would be YES. As
  cited (:169, blame 95364569a), NO is correct.
- Every line anchor checked resolved at the frozen tree: delegated-engine-adapter :86-91 and
  :257-282; session-store :654, :955-975 and :1111-1127; runtime-service-host :75; transition.ts;
  status-parser :212; _REFERENCES.md :12-13; _CONTEXT.md :48; _STATUS.md :3 and :17. Every cited
  test-case name was found once in its file.

## (iii) Effort

About 30 files or ranges read: the rulebook, RUN_BASIS, the unit ledger and reverse files, four
capability files, App DIRECTIVE and CONTRACT, the D-GOV-43 proposal and IMPACT, the SoW, context
files, and eight code files. There were three read-only git calls (log and blame -L). The context
budget was not tight. No run-folder file other than my two outputs was written.
