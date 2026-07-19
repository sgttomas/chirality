# PKG-06 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (Instance G4)

- **Window:** `c313325b7` (R6 basis) → `ff2f68c82` (HEAD). Agent claims only; no verdict here is an owner act.

## Counts

| Metric | Value |
|---|---:|
| Prior claim rows (frozen manifest) | 131 |
| In-scope selected | 131 (100%) |
| Confirmed (ScopedDisposition == PriorDisposition) | 118 |
| Re-dispositioned (disposition deltas) | 13 |
| New rows minted (`DEL-XX-YY-SCOPED-Snn`) | 11 |
| HumanDecisionNeeded = YES | 7 |

Deltas (all STALE/mismatch → ALIGNED on verified repair or ruling):
DEL-06-01 ACC-001 (SOW CLM-029 records REF-006 MATCH), REGISTER-1 (UPD-127
call-path resolution); DEL-06-02 ACC-001 (stale wording retired), UNMAPPED-1
(R4-P27 domain-roster ownership reconciliation now in the SOW), REGISTER-2
(contest ruled Reading B by D-APP-56 P18 → not a defect); DEL-06-03
ACC-06-03-001, REGISTER-1 (dated correction block); DEL-06-05 REQ-009,
REQ-016, ACC-001 (stale TBD/HASH_MISMATCH wording retired in the SOW),
REGISTER-1 (Notes cell repaired); DEL-06-06 REQ-014 (warning retired),
UNMAPPED-1 (hook.progress adopted by R4-P04 and now test-covered).

## Selection reasoning

Rule (a) captured every prior row: the window deleted all four kit documents
for every PKG-06 deliverable and replaced each with a consolidated
`ScopeOfWork.md` under the owner-ratified D-GOV-15/D-GOV-16 standard
(migration commits 2026-07-13). In addition, the PKG-06 implementation
surfaces changed materially in the window (rule (a)/(b)):
`permission-overlay.ts` (policy v4→v7, new coordination class),
`tool-path-policy.ts` (managed child read/write scopes; symlink rejection
extended to reads), `tool-shell-policy.ts` (v2 managed-child Bash gate),
`sdk-options-builder.ts` (scope threading), `tool-descriptor.ts` /
`tool-names.ts` / `tool-catalog` (registry v10→v13, MCP server 1.0.0→2.0.0,
four coordination tools), `mcp/read-tools.ts` (coordination tool wiring),
plus additive test growth. Every change was inspected via window diff; all
are additive/strengthening — no prior PKG-06 behavioral claim is falsified.

## Key window facts

1. **D-GOV-16 SOW consolidation** — same structural event as PKG-05; all
   prior ledger kit-file anchors are dead (rows `DEL-06-0X-SCOPED-S01`).
2. **Managed multi-agent orchestration control plane** (commits
   `62e563e47`/`c9734a6ee`/`ee35409f5`, owner-merged): new `coordination`
   permission class with workspaceWrite-only hard deny; four registered
   `mcp__chirality__` coordination tools (delegate_agent,
   report_coordination_notice, send_agent_update, ack_agent_update);
   managed-child path/Bash scope enforcement bound to declared
   context/write targets. Consistent with AGENTS.md managed-delegation
   doctrine, but no PKG-06 kit requirement or numbered D-APP decision maps
   the surface to an owning deliverable → five S02 rows
   (IMPLEMENTED_UNDOCUMENTED, HDN=YES).
3. **Stale-wording cleanup was uneven across the migrated SOWs**: DEL-06-02,
   DEL-06-03, DEL-06-05, DEL-06-06 came out clean (prior STALE_SPECIFICATION
   rows RESOLVED); DEL-06-04 still carries present-tense
   HASH_MISMATCH/warning-qualified assertions (SOW lines 255/313-314/333/349
   + REQ-016 wording) → PERSISTING; DEL-06-06 REQ-015 path-TBD placeholders
   persist; DEL-06-01/06-05 test-path TBDs persist as non-gating notes.
4. **Baseline check** confirmed persisting wording existed at `c313325b7`
   (never repaired at R5), so PERSISTING rather than migration regression.

## Human decisions (7)

1. DEL-06-01 UNMAPPED-1 — subagent permission-class ownership (standing).
2. DEL-06-01-SCOPED-S02 — coordination permission-class ownership/adoption.
3. DEL-06-02-SCOPED-S02 — coordination MCP tool surface (registry v13 rows,
   catalog, server 2.0.0) ownership/adoption.
4. DEL-06-03-SCOPED-S02 — coordination-tool co-location on the read MCP
   surface; keep the read-slice exclusion wording truthful.
5. DEL-06-04-SCOPED-S02 — managed-child path-scope enforcement ownership.
6. DEL-06-05 UNMAPPED-1 — ratify or record the 120000/600000 ms Bash timeout
   numerics (standing).
7. DEL-06-05-SCOPED-S02 — managed-child Bash gate ownership.

Recommend the five coordination-surface items (2-5, 7) be consolidated into
ONE ownership packet, mirroring the W6/PKG-10 precedent.

## Ambiguities

- Whether the new coordination surface is "ruled" for ACCEPTED_DIVERGENCE
  coding: it is owner-merged and doctrine-backed (AGENTS.md), but no numbered
  D-APP decision names it in PKG-06 scope, so I coded
  IMPLEMENTED_UNDOCUMENTED with HDN=YES rather than guessing an authority.
- DEL-06-02 REGISTER-2: the prior row's own decision rule said Reading B ⇒
  NOT_A_DEFECT; the vocabulary has no such token, so I coded ALIGNED with the
  D-APP-56 P18 ruling cited.

## Not examined (stands on R3/R6)

- Unchanged register files (Dependencies.csv/_DEPENDENCIES.md for most
  deliverables) were checked only for the specific prior defect text.
- No re-derivation of out-of-package rows; no whole-corpus rework.
- No test execution and no fresh full-suite gate transcript exists in the
  window; behavioral confirmations are window-diff plus code inspection
  (`RUN-INSPECTION@ff2f68c82`) over surfaces byte-identical or
  additively-changed relative to the W1-gated state.

## Method deviations (disclosed)

- Same as PKG-05 notes: the harness exposes no Grep/Glob tool, and the kit
  files were deleted/renamed in-window, so strictly read-only Bash
  (`ls`, `grep`, `git log/diff/show`, `sed -n`, `head`) was used as the
  Grep/Glob substitute. Writes were confined exactly to the four PKG_LEDGERS
  targets; no network, no delegation, no test execution.
