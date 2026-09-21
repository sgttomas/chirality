# V-DEC verifier notes (shard DEC, ledger DEC)

CSV: `V-DEC.csv`, SHA-256 `019f7f4467f9f1b34bc2d07c482dcb779a1ae1c8ef0ec814b14647e6b577ca8f`
(16 verdict lines for 15 selected items, then `#END`).

## (i) Counts

Items checked: 15 (class a 6, class b 5, class c 4). No class e items.

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (self-flag / LOW) | 6 | 3 (D-APP-92, D-APP-94, REGISTER-5) | 0 | 3 (D-APP-96, D-APP-112.2, D-APP-125.1) |
| b (non-ALIGNED sample) | 5 | 5 | 0 | 0 |
| c (ALIGNED sample) | 4 | 4 | 0 | 0 |
| **Total** | 15 | 12 | 0 | 3 |

By Field (verdict lines): Disposition CONTESTED 3 (D-APP-96, D-APP-112.2, D-APP-125.1);
DirectionEvidence CONTESTED 1 (D-APP-112.2). REFUTED 0 on any field, so no verdict-field
refutations and nothing for CORRECTIONS.csv from this shard.

## (ii) Patterns

1. **Supersession by records outside the RUN_BASIS §5 GOVERNING list.** D-APP-112.2 treats an
   owner direction held only in an AgentRuns `OWNER_DIRECTION.md` file (no register row) as
   `GOV:` and as the basis for ACCEPTED_DIVERGENCE. D-APP-96 cites D-APP-108, a seating ruling
   that never mentions the ruled presentation. Both are plausible, but the grading key requires a
   GOVERNING ruling that permits the difference. Both were already self-flagged by the worker.
2. **Corpus-only rulings later overtaken by product change (D-APP-96).** Where a ruling's stated
   effect is purely a corpus act ("no product bytes change") and the product later moves, ALIGNED
   (the effect landed) and ACCEPTED_DIVERGENCE both have support. The rulebook does not say
   whether item 3 judges the stated act or the ruled end state. Proposal: state that item 3 judges
   the stated effect and routes later product drift to the owning package ledger.
3. **Root/Runtime-owned effects (D-APP-125.1).** Contract finalization assigned to the Runtime
   and Root owners cannot be shown absent from App surfaces alone. Following the manager's
   direction, this is CONTESTED (DOCUMENTED_UNIMPLEMENTED || UNKNOWN). By contrast, D-APP-120 B1
   Root routing *is* evidenced App-side (`APP_SHELL_CONVERGENCE_2026-09-06/iteration-03/ROUTING_EVIDENCE.md:7`),
   although the worker's Notes called it out of bounds. The disposition still holds.

Minor slips (ConventionIssue only): D-APP-104 and D-APP-107 Notes cite `execution/_Scripts/app_hold.py`
without the `projects/chirality-app-dev/` prefix. D-APP-92 cites the first D-APP-92 handoff instead of
the latest (`HANDOFF_STATE_R11.md`), which supports the same reading. The flag handling on D-APP-104
and D-APP-107 (flags inaccurate, routed to REGISTER-1) is correct. All cited register line numbers
(107–152) and status/code line anchors checked resolve at the frozen basis. REACH tags match
`REACHABILITY.csv` (all LIVE). PostReleaseBasis NO holds for every item: only `runtime-daemon.ts` is on
TOUCHED_PATHS, and its ranges end at line 686, before the cited line 1338.

## (iii) Effort

About 35 files or line ranges were read: the register, 10 ruling records, 6 `_STATUS.md` files,
LOOP_INIT and its archive, 5 AgentRuns handoffs and directions, 4 code files, and the evidence
pack CSVs. Git use was `log -S` (All sessions label), `show --stat` on 06068dfb8, e079cbc39 and
03e61f38f, and `log -1` on 774d9aabf, 5bd5a63ef and be243fdf6, all against the frozen tree.
The context budget was comfortable.
