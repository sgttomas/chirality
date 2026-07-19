# Orchestration Plan — D-APP-65 Accepted-Recommendations Program

- **RunID:** `D-APP-65_ACCEPTED_RECOMMENDATIONS_2026-07-18`
- **Orchestrator:** HELP_HUMAN (Agent 0), Claude Fable 5, this session
- **Authority:** the owner (Ryan Tufts, K-AUTH-1) accepted, verbatim in chat on
  2026-07-18, the agent's presented recommendations for every parked
  owner-gated item ("I accept your recommendations.  Proceed accordingly."),
  ruled two scope points through in-chat structured questions (R4-P47 → all
  three fields; hardening packets → ruled in-session), and approved the
  execution plan. The acceptance and its accepted basis are bound verbatim
  with canonical hashes in the D-APP-65 packet. Agent selections inside the
  program are exercises under the D-APP-64 reasoned-selection overlay,
  attributed in run records.
- **Base:** branch `claude/dapp65-accepted-recommendations` off `origin/main`
  = `24dc7bfb291996936de7a8af04b9cb9e74c6485a`; Step-0 battery green at start
  (receipt validator VALID through Receipt-71; corpus no drift; self-check
  exit 0 at the pinned anchor INFO=15/NA=2/REVIEW=33/WARN=6).
- **Terminal act:** one PR; the owner's merge. No release, issuance,
  lifecycle advancement, or external effect. Fences F-APP-1..5 unchanged.

## Work graph (one atomic commit per tranche)

| Node | Tranche | Role | Work |
|---|---|---|---|
| N1 | T1 | governed-writes child (HELPS_HUMANS posture, sealed brief) | D-APP-65 packet + register row + kit writes (DEL-04-01 / DEL-00-02 / DEL-01-01 role fields; DEL-10-03 DEP-10-03-004 annotation) |
| N2 | T1 | fresh adversarial verifier (sealed refutation-only brief) | Enumeration-derived claims + whole-diff claim over the staged T1 tranche → `RETURN_T1_GOVERNED_DIFF_*.md` |
| N3 | T1 | Agent 0 | Commit 1 |
| N4 | T2 | code-test child (sealed brief) | DEL-04-05 four-class category assertions + kit updates + run record |
| N5 | T2 | fresh verifier | `RETURN_T2_GOVERNED_DIFF_*.md` → Commit 2 (Agent 0) |
| N6 | T3 | two parallel docs authors (sealed briefs) | DEL-01-01 seven governed artifacts (R004 resolved first); DEL-03-03 test index + SSE fixture README |
| N7 | T3 | fresh verifier | `RETURN_T3_GOVERNED_DIFF_*.md` → Commit 3 (Agent 0) |
| N8 | T4 | packet author child (sealed brief) | D-APP-66 (SHA revalidation) + D-APP-67 (redaction taxonomy) packets, register rows AWAITING_RULING |
| N9 | T4 | Agent 0 ↔ owner | Present options in chat; on ruling, transcribe verbatim + flip RULED; code child executes ruled option + tests |
| N10 | T4/T5 | fresh verifier; Agent 0 | `RETURN_T4_GOVERNED_DIFF_*.md` → Commits 4/5; receipts; closeout battery; PR |

## Safety

Children use bounded file tools within enumerated write scopes; Agent 0 runs
all deterministic gates and commits (serialized integration owner). Shared
reads allowed; sibling writes disjoint by tranche. A verifier BLOCK stops the
tranche: repair, preserve the failed return, re-verify. Nothing lands on
BLOCK. No lifecycle/state/`Checking Approval SHA` line changes anywhere in
the program except none (F-APP-4 untouched).
