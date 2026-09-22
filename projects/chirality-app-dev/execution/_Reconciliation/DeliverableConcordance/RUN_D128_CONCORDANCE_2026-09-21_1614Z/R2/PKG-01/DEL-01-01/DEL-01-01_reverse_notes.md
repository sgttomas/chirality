# DEL-01-01 — reverse-pass notes (pass 2)

Sealed ledger `DEL-01-01_claims.csv` SHA-256
`b839e48bf3593c52a06668f029223ed4166c354487ccc49b5e47782f3ea7cb4d` (unchanged).

## Responses

`DEL-01-01_reverse.csv` answers the 364 capability rows in eight files, concatenated in the order the
manager gave: BUILD 41, ELECTRON 35, HARNESS 60, ROUTES 44, RTCONTRACT 53, RTCORE 50, SETTINGS 42,
WORKSPACE 39. The manager's message said 365. The files hold 364 `CAP-` rows, and every per-file
validation passes on coverage.

| Response | Rows |
|---|---:|
| CLAIMED_BY | 0 |
| PARTIAL | 38 |
| NOT_MINE | 326 |

DEL-01-01 is a DOC_UPDATE governance deliverable. It restates invariants but owns no runtime
capability outright, so every overlap is PARTIAL. The PARTIAL rows cluster as follows:

- **Human gate and lifecycle** (CLM-004.1, CLM-004.5, CLM-009.9): ROUTES-031/032, WORKSPACE-020/022/025/026/032/034,
  SETTINGS-024/025, HARNESS-051.
- **Canonical audit store** (CLM-005): RTCORE-015, ELECTRON-003, HARNESS-037/038.
- **Runtime audit** (CLM-004.3): RTCORE-017.
- **Provider-shaped events, R4-Q5** (CLM-009.7): RTCORE-025/029, RTCONTRACT-022/024.
- **Reliance boundaries, R4-Q1** (CLM-004.4): HARNESS-027/044/045/047, RTCONTRACT-019/042, RTCORE-030/031.
- **Claude-as-current-path versus Codex-sole** (STATE-1): HARNESS-028/031/033, RTCONTRACT-045/053,
  RTCORE-004/048, BUILD-015.
- **Source warnings** (CLM-009.8): WORKSPACE-017.
- **Dependency non-satisfaction** (CLM-009.10): WORKSPACE-024.

## Errata (1 ClaimKey, 2 fields)

- **CLM-004.1 ImplementationEvidence and Notes.**
  - The sealed row tagged `workbench-surface.tsx` `REACH=LIVE` and said it was rendered through
    `tertiary-sidebar-tabs.tsx`. That is wrong. `WovenDialogueRoute` discards the legacy `LoopShell`
    prop (`woven-dialogue-route.tsx:18`, `void legacy`), so the Workbench and Pipeline transition
    forms are never mounted (CAP-WORKSPACE-034/032 RETIRED-UNMOUNTED).
  - Correct tag: `REACH=LEGACY_ONLY` (UNREACHED).
  - The served transition route still enforces actor `HUMAN` plus `approvalSha`, so the ALIGNED
    Disposition stands. No verdict field changes.

**Census, sealed vs errata-applied:** identical. ALIGNED 19, STALE_SPECIFICATION 13,
NOT_AUDITABLE 7, STALE_ASSESSMENT 4, AUTHORITY_CONFLICT 4, PARTIALLY_IMPLEMENTED 3 (50 rows; 14 SEE).

## Reach disagreements

- **`REACHABILITY.csv` versus symbol-level reach:**
  - `workbench-surface.tsx` and `pipeline-surface.tsx` are LIVE in the pack but unmounted at symbol
    level. This is the erratum above.
  - `lifecycle/transition.ts` is LIVE only through the served API routes; no live UI caller exists
    (CAP-SETTINGS-025, CAP-WORKSPACE-022). My ledger cites it as a LIVE route-side guarantee, which
    matches.
- **Redaction, CAP-HARNESS-027:** it is LIVE, but no key source is populated in the renderer. My
  CLM-004.4 cites `sanitize.ts` as LIVE for the redaction boundary. That tag is correct for the module,
  but the redaction evidence is thin. The Disposition (PARTIALLY_IMPLEMENTED) is unaffected, so I filed
  no erratum.
- **Session store, CAP-RTCORE-015:** the capability notes confirm that the touched lines of
  `session-store.ts` (6-8, 128-158) are outside the lines I relied on (1111-1127). PostReleaseBasis NO
  stands.

## Coverage gaps (no forward row; not errata)

- **No live UI path performs lifecycle transitions** (Workbench/Pipeline unmounted). Nothing in
  DEL-01-01 records that a human-gate transition can now be made only by editing the file or calling the
  route directly. This bears on K-GATE-1's "status transition API" enforcement surface. No indexed unit
  owns it; route it to the lifecycle or shell owner (PKG-02/PKG-05).
- The forward notes already name the App DIRECTIVE §8 daemon gap. The reverse pass found no capability
  that changes it.
