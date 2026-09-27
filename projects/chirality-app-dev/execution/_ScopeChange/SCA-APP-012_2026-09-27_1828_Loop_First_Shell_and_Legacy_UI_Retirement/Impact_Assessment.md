---
amendment_id: SCA-APP-012
doc_kind: scope_change.impact_assessment
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-27
status: awaiting_checkpoint_1_acceptance
basis_commit: 0adfbc7476df33521883ce1573781237cd24d384
workflow: scope-change (bundled)
---

# SCA-APP-012 — Checkpoint-group-1 Impact Assessment

> **Status: PROPOSED, awaiting the owner's checkpoint-group-1 act.** This
> package proposes a change and states its impact. It changes no
> decomposition, companion register, PRD, SPEC, PLAN, Scope of Work,
> `_CONTEXT.md`, `_STATUS.md`, dependency register, pointer or code. No
> decision snapshot, `DECISION.md`, `SCA-APP-012_GROUP-1_AUTHORIZED.md` or
> `_LATEST.md` change exists or is implied. Exact amendment text belongs to
> checkpoint group 2.

Abbreviations:
- **Row n** is row `ActionSeq = n` of `Intake_Actions.csv` in this snapshot.
- **Lnnn** is a line of the named file at the basis commit.
- **SOW** is the deliverable's `ScopeOfWork.md`.
- **D** is the App decomposition `Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
- **Baseline** is `Pre_Change_Coverage.json` in this snapshot.

---

## For the owner: checkpoint group 1

### What SCA-APP-012 does

It deletes the last dead UI of the old loop-first shell and settles the
residuals SCA-APP-011 left. Nothing the user can reach today is lost:

- **The loop-first shell has not rendered since 2026-09-09.** Commit
  `9b005c23a` ("Adopt conversational roles, skills, and workflows for
  Chirality v3") replaced the `?legacy=1` branch of `WovenDialogueRoute` with
  `void legacy`. Every route has rendered the dialogue shell since then. The
  shell modules are still imported, but only as a JSX element that is never
  rendered.
- **`DeliverablesProvider` has no reader.** It only repeats a
  `/api/project/deliverables` fetch whose result nothing uses.
- **`GET /api/working-root/scope` has no caller.** Its last client went with
  the Workbench form in SCA-APP-011. The scan library behind it stays.
- **No App-side scaffold entry is planned**, following your direction
  "Scaffolding through the agent is enough." Scaffolding stays with the agent
  and the Root `project-setup` workflow.

Topology is unchanged: 10 packages, 52 deliverables, 84 scope items and 10
objectives. No deliverable is added or retired, and no scope item or
objective loses its only carrier. No deliverable is `ISSUED`, so no reopening
is involved.

### What accepting group 1 authorizes

Accepting group 1 accepts the proposed change and its impact as the basis for
drafting group 2:

1. **BASE (Rows 1–13), owner-directed.**
   - Retire the loop-first compatibility UI: the shells, the role-directory
     panel, the discarded `legacy` prop and `?legacy=1` link, and
     `lib/portal/agent-matrix-{launch,cells}.ts`.
   - Retire `DeliverablesProvider` and `GET /api/working-root/scope`.
   - Record the separate owner decision that PRD KG-033, PRD §6.4, SPEC §17.9
     and D-APP-74 L107 require, in the PRD, SPEC, PLAN, decomposition,
     DEL-02-01, DEL-02-03, DEL-07-03 and DEL-08-02 texts.
2. **S (Rows 14–16), owner-directed.** Restate DEL-07-02, DEL-06-03 CLM-031,
   SPEC §14.2 and PRD goal 17 / §6.1: scaffolding is done by the agent through
   Root `project-setup`, and no App-side scaffold entry is planned. The
   wording holds whichever lands first, this amendment or the Runtime change
   that retires `ProjectScaffoldPort`.
3. **Your answers to choices R and P below**, and the defaults listed after
   them unless you say otherwise.
4. **Group 2 drafting.** I prepare the exact text, `Amendment_Actions.csv`,
   `Supersession_Delta.csv` and the propagation plan for checkpoint group 2.

**One point to acknowledge.** PRD §6.4 lists preconditions for retiring the
loop-first UI: parity, accessibility, migration, performance, runtime
regression, packaged Desktop proof, and your acceptance. The loop-first UI has
been unreachable since 2026-09-09, so deleting it removes no reachable
behavior. The packaged Desktop evidence for the dialogue shell is still open
under KG-033. Accepting group 1 accepts that the retirement does not wait for
that evidence. The evidence stays open under its current owners.

It does **not** authorize any file edit, code merge, dependency change,
lifecycle change or pointer move. The code removal waits for group 3, as in
SCA-APP-011.

### Choices

| # | Choice | Options | Recommendation |
|---|---|---|---|
| **R** | **DEL-02-03-REQ-009** ("Deliverable summary widgets shall support routing to PIPELINE `TASK*` with a deliverable preselected", SOW L143, verification L181) and **DEP-02-03-009** | **R-b (Rows 17–18):** retire REQ-009 as history, remove the routing wording that only it carried, and retire DEP-02-03-009 at dependency re-extraction. **R-a (Rows 19–22):** restate REQ-009 as task-scope preselection under the DEL-08-03 dispatch contract. DEL-08-03, SOW-007 and PRD §7.5 then name it as a declared consumer, and DEP-02-03-009 stays `ACTIVE`, restated. | **R-b.** No deliverable summary widget exists in the live shell (DEL-02-03 CLM-012). The dispatch contract has no product consumer. R-a would add a presentation obligation for a widget nobody has planned, and SOW-007, DEL-08-03 and PRD §7.5 each say that any such consumer needs its own amendment, so R-a must edit three more carriers. R-b leaves DEL-08-03's TASK-scope semantics (FR-012, SOW-007) intact and removes the DX-15 tension (§6). |
| **P** | **`/workbench` and `/pipeline` page routes** | **P-keep:** keep both URLs as unlisted URL-compatibility entries into the dialogue shell; only their `legacy` element is deleted. **P-r (Rows 23–29):** redirect both to `/`, keeping the query string. **P-d (Rows 23–29):** delete both (404). | **P-keep.** Both URLs are pinned by the Electron renderer-security probe (`electron/main.ts` L647), by the packaged security proof (`scripts/run-packaged-security-proof.mjs` L49) and by their contract pins. P-r and P-d need a new packaged renderer-security native witness (DEL-09-06). The URLs also select the `WORKBENCH`/`PIPELINE` session mode and draft keys in `chat-panel.tsx` (L194-208, L472-505), so P-r and P-d would strand existing drafts and auto-resume behind those URLs. P-d reverses D-APP-108 Q3 ("no 404"). P-keep changes no scope text beyond BASE (§7). |

Defaults, applied unless you say otherwise:

- **L-lib: delete both portal helpers** (`agent-matrix-launch.ts` and
  `agent-matrix-cells.ts`). Neither has a product importer. The
  unknown-query-parameter duty stays with DEL-08-02, to be verified against
  the live shell route.
- **S-tool: narrow SPEC §14.2 `mcp__chirality__scaffold` and PRD goal 17 /
  §6.1 to the read-only preview** (Row 16). FR-119, the §8.13 sequence, PLAN
  R2 and TYPES §8.4 stay unchanged.
- **E: no change** to CONTRACT or companion-register wording.

With the recommended answers, group 2 carries 18 register rows: 17 MODIFY
and 1 ADD (Rows 1–18).

### Suggested reply

A short answer is enough, for example:

> "Accept SCA-APP-012 group 1: R-b, P-keep, defaults."

I then record your words verbatim in the group-1 decision snapshot and
prepare group 2.

---

## 1. Impact verdict

SCA-APP-012 is a **scope-reducing amendment that preserves topology**. Under
the recommended selections:

- 0 ADD or REMOVE deliverables;
- 1 ADD Decision Log row (DEC-027);
- MODIFY on DEL-02-01, DEL-02-03 (twice: BASE and R-b), DEL-06-03, DEL-07-02,
  DEL-07-03 and DEL-08-02;
- MODIFY on the SOW-001 notes, the hard constraint, the §13 note, telemetry,
  the PRD, the SPEC and the PLAN;
- the DEP-02-03-009 settlement, carried out by dependency-extract.

No scope item goes OUT and no objective loses support. The main costs are:

- **Test re-homing in the code change.** The code change deletes or edits
  11 test files. One case in `pkg08-compatibility-boundaries.test.ts`
  (the matrix-helper round trip) is dropped, not ported. The unknown-parameter
  duty it seemed to cover was never verified against the live shell, and
  DEL-08-02 keeps that duty open (§3.3).
- **Compatibility clauses.** Eight PRD clauses, two SPEC §17.9 sentences,
  four PLAN passages and D-APP-74 keep "the loop-first UI", "the existing UI"
  or "current UI" until separate owner acceptance. This amendment is that
  acceptance and must say so (Rows 10, 12, 13).
- **Text alignment** across six Scopes of Work (seven under R-a, eight with
  P-x), and dependency re-extraction for DEL-02-03 and its neighbours (§10).

## 2. Evidence basis

| Evidence | SHA-256 / result |
|---|---|
| `Brief.md` (this snapshot) | `d540c607be74de674e629072cf6a7938d01bb7bb4677a31f3fad2159cd9b9b27` |
| `Intake_Actions.csv` (this snapshot) | `8c5a3e6d1f2a0d0d30434bceb998217bdec94e82c4ac411559079947ee7fdff2`; 29 rows, all `PROPOSED` |
| `Pre_Change_Coverage.json` (this snapshot) | `4504d70e2cb213b44651fb0c8a8f34c593f1a49088c4f01eec5b65fbe90018cb`; byte-identical across runs at `0adfbc747` and after the rebase onto `ec81ef2c7` |
| `Evidence/Group1/build_pre_change_baseline.py` | `e7abdab1612037e67551df3d810e892f4e6adca9fa214cbdb7d5b6fceb1dbe7b` |
| Reused audit `COV_SCA_APP_011_POST_ACCEPTANCE_2026-09-27_0500` | 122/122 recorded inputs byte-identical at this basis; `WARNINGS`, 0 blockers |
| Decomposition / companion register / `_LATEST.md` | `cf6e56eb…d2321876` / `918e475a…a942c` / `904c1bd6…c42c04e3` (full values in `Brief.md`) |
| Other inputs | as listed with full SHA-256 in `Brief.md` |

## 3. What is dead, and why

### 3.1 Reachability at the basis

Static relative-import graph over `frontend/src` (tests excluded) and
`frontend/electron`. The roots are every app `page.tsx`, `layout.tsx`,
`not-found.tsx` and `route.ts`, and every Electron module. There are 259
product modules, of which 211 are reachable (Baseline
`frontend_reachability`).

| Scenario | Modules that become unreachable | Product importers | Test importers |
|---|---|---|---|
| **S1** Drop the `legacy` elements (never rendered) | `components/shell/loop-shell.tsx` | `app/chat/page.tsx` | — |
| | `components/shell/portal-loop-shell.tsx` | `app/page.tsx` | — |
| | `components/shell/loop-tertiary-shell.tsx` | `app/workbench/workbench-client.tsx`, `app/pipeline/pipeline-client.tsx` | — |
| | `components/shell/sidebar-right-loop-layout.tsx` | the three shells | `components/workspace-sidebar.test.ts` |
| | `components/shell/tertiary-sidebar-tabs.tsx` | the three shells | — |
| | `components/portal/agent-matrix.tsx` | `tertiary-sidebar-tabs.tsx` | `components/agent-matrix-panel.test.ts` |
| **S2** Also drop `DeliverablesProvider` | `components/workspace/deliverables-provider.tsx` | `app/layout.tsx` | — |
| | `lib/workspace/task-scope.ts` (library kept; test-only afterwards, like the dispatch contract) | `deliverables-provider.tsx` | `lib/task-scope-selection.test.ts` |
| **S3** Also drop the two page directories (P-x only) | `app/{workbench,pipeline}/page.tsx` and their clients | — | `components/loop-tertiary-routes.test.ts` |
| Already unreachable at the basis, in scope | `lib/portal/agent-matrix-launch.ts`, `lib/portal/agent-matrix-cells.ts` | none | `lib/agent-matrix-launch.test.ts`, `lib/agent-matrix-cells.test.ts`, `lib/pkg08-compatibility-boundaries.test.ts` |

### 3.2 Other dead threads found

- **`?legacy=1` link.** `woven-dialogue-shell.tsx` L384-388 builds
  `legacyHref` and passes it on. `Navigator` discards it (`void legacyHref`,
  `navigator.tsx` L119), and `ShellFrame` never destructures it
  (`shell-frame.tsx` L56 declares it). The test "preserves the legacy
  compatibility link" (`woven-dialogue-shell.test.tsx` L433-440) passes only
  because it mocks `ShellFrame`, which is the same kind of mock-only contract
  as KG-033's `[data-legacy]` residual.
- **Symbol-level residue** once the shells go:
  - `buildPortalPersonaHref` and `buildDirectChatHref` in
    `lib/shell/loop-first.ts`; `CHAT_SECTION` stays, because `chat-panel.tsx`
    uses it;
  - the `PersonaPicker` `buildHref` prop;
  - the `WorkspaceSidebar` `portalTab`/`workbenchTab`/`pipelineTab` props and
    tab constants (`AppShell`, used by `not-found.tsx`, passes none);
  - the `ShellFrame` `legacyHref` prop.
- **Legacy-only CSS.** Eleven class tokens in `app/globals.css` have no other
  product user: `loop-chat-host`, `loop-grid`, `loop-grid--sidebar-collapsed`,
  `loop-main`, `loop-persona-bar`, `loop-sidebar`, `portal-launch-notice`,
  `portal-matrix`, `portal-matrix--sidebar`, `portal-matrix-header` and
  `portal-matrix-heading` (Baseline `legacy_css_tokens`). `shell-pane*` stays,
  because `AppShell` uses it.
- **Copy.** The metadata description in `app/layout.tsx` reads "PORTAL,
  PIPELINE, and WORKBENCH shell for local agent execution". An optional tidy
  in the code change.

### 3.3 Tests the code change must handle

| Test | Action |
|---|---|
| `components/agent-matrix-panel.test.ts`, `lib/agent-matrix-launch.test.ts`, `lib/agent-matrix-cells.test.ts` | Delete with their modules |
| `components/workspace-sidebar.test.ts` | Drop the `SidebarRightLoopLayout` and tertiary-tab cases; keep any `WorkspaceSidebar` case `AppShell` still needs |
| `components/woven-dialogue-route.test.tsx` | Drop the `legacy` prop cases; keep the surface cases |
| `components/loop-tertiary-routes.test.ts` | Under P-keep, retarget to a page-route test that `/workbench` and `/pipeline` open the dialogue shell. Under P-x, replace with a redirect or 404 test |
| `lib/pkg08-compatibility-boundaries.test.ts` | Keep the role-boundary case (on `CHIRALITY_ROLES`) and the dispatch case; drop the matrix-helper round trip. DEL-08-02, DEL-08-03 and DEL-08-05 keep naming this file |
| `lib/loop-first.test.ts` | Keep the `CHAT_SECTION` case; drop the removed-helper cases |
| `components/woven-dialogue-shell.test.tsx`, `woven-dialogue-navigator.test.tsx`, `historical-chat-reveal.test.tsx` | Drop the `legacyHref` prop and the "legacy compatibility link" case |

No test weakens a protected check. The dropped cases test helpers that no
product code reaches.

## 4. Impact by action

| Row(s) | Set | Entity | Affected sections / files | Owning workflows after acceptance |
|---|---|---|---|---|
| 1 | BASE | DEL-02-01 | SOW L57 (superseded SCA-APP-004 obligation 2), L108 (SCA-APP-010 obligation 5), verification hooks | project-setup INCREMENTAL (`scope-of-work` REVISE); dependency-extract |
| 2 | BASE | DEL-02-03 | SOW CLM-003 L54; REQ-010 source L144 | same |
| 3 | BASE | DEL-07-03 | SOW L185, L255, L403 | project-setup INCREMENTAL |
| 4 | BASE | DEL-08-02 | SOW L86-87 hooks, L165, L204, L260 | project-setup INCREMENTAL; dependency-extract |
| 5 | BASE | SOW-001 | D L176, L409 | audit-decomp |
| 6 | BASE | Hard constraint | D L102 | audit-decomp |
| 7, 8, 9 | BASE | §13 note, DEC-027, telemetry | D after L675; after L642 and L660; L500-501 | audit-decomp |
| 10 | BASE | PRD (loop-first) | `docs/PRD.md` L163, L329, L355, L383, L596, L1263, L1674, L1714 | audit-scope-closure |
| 11 | BASE | PRD (scope route) | L883 and the carve-outs L163, L329, L383, L1674 | audit-scope-closure |
| 12 | BASE | SPEC | `docs/SPEC.md` L1126 (§17.2), L1279 and L1284-1286 (§17.9) | audit-scope-closure |
| 13 | BASE | PLAN | `docs/PLAN.md` L37, L118-120, L394, L560; a new §13 entry | audit-scope-closure |
| 14 | S | DEL-07-02 | SOW L24, L25, L229 (L477 stays history) | project-setup INCREMENTAL |
| 15 | S | DEL-06-03 | SOW CLM-031 L364 | project-setup INCREMENTAL |
| 16 | S | SPEC §14.2, PRD | `docs/SPEC.md` L999; `docs/PRD.md` L155, L323 | audit-scope-closure |
| 17 | R-b | DEL-02-03 | SOW L81, L116, L143, L147, L181, L185, L216, L287, L297, L317, L350 | project-setup INCREMENTAL; dependency-extract |
| 18 | R-b | DEP-02-03-009 | DEL-02-03 `Dependencies.csv`, `_DEPENDENCIES.md` | dependency-extract; `analyze_dep_closure` |
| 19–22 | R-a | DEL-02-03, DEL-08-03, SOW-007, PRD §7.5, DEP-02-03-009 | SOW L143, L181, L216; DEL-08-03 SOW L65, D L375, `_CONTEXT.md` L33; D L182, L415; PRD L465 | project-setup INCREMENTAL; dependency-extract |
| 23–29 | P-x | DEL-02-01, DEL-08-02, DEL-02-02, SOW-001/005, PRD, SPEC/DIRECTIVE/TYPES, hard constraint | DEL-02-01 SOW L54, L108, L205, L212; DEL-08-02 SOW and DEP-08-02-013; DEL-02-02 SOW L112; D L102, L176, L180, L409, L413; PRD L329, L446, L465, L1263, L1674, L1714; SPEC L1272; DIRECTIVE L234; TYPES L142-143 | project-setup INCREMENTAL; dependency-extract; packaged renderer-security re-evidence (DEL-09-06) |

## 5. Coverage

| Entity | Current carriers | Effect | Only carrier lost? | OUT? |
|---|---|---|---|---|
| SOW-001 (dialogue-centred shell) | DEL-02-01 | Notes drop "the loop-first UI" as a compatibility surface (Row 5) | No | No |
| SOW-002 (per-chat folder) | DEL-07-01, DEL-02-03 | None | No | No |
| SOW-003 (file tree and scope scans) | DEL-02-03 | The scope scan stays: the scan library and `/api/project/deliverables` (deliverables and knowledge types) remain; only the uncalled `/api/working-root/scope` goes | No | No |
| SOW-005 (routing, aliases, legacy route/query compatibility) | DEL-02-01, DEL-08-02 | Unchanged under P-keep; route/query semantics stay with DEL-08-02 | No | No |
| SOW-007 (dispatch semantics) | DEL-08-03 | Unchanged under R-b; notes gain a declared consumer under R-a | No | No |
| SOW-024 / SOW-025 (scaffolding) | DEL-07-02 | Unchanged; the scaffold library and `scaffold_preview` stay | No | No |
| OBJ-001 | 9 active supporters | Unchanged | No | — |
| OBJ-006 | 10 active supporters | Unchanged | No | — |
| OBJ-007 | 8 active supporters | Unchanged | No | — |

**No scope item or objective loses its only deliverable, and none goes OUT,
under any option.** Requirements that lose their only home are retired as
history, not moved:

| Requirement | Treatment |
|---|---|
| DEL-02-01 SCA-APP-004 obligation 2 ("Keep the existing loop-first and matrix UI reachable until separately retired", L57) | Already superseded by SCA-APP-010; annotated `[RETIRED — SCA-APP-012]` |
| DEL-02-01 SCA-APP-010 obligation 5, the loop-first part (L108) | Restated; routes, queries and aliases stay |
| DEL-02-03-REQ-009 and CLM-015 (R4-P29 launcher) | R-b: retired as history. R-a: restated |
| PRD KG-033 remediation clause and the `[data-legacy]` residual | Closed by this amendment's owner decision and the legacy-prop removal |
| DEL-06-03 CLM-031 (write-capable scaffold on the later write surface) | Restated: no write-capable App scaffold tool is planned |
| DEL-07-02 follow-up (a later App-side entry, such as a composed `ProjectScaffoldPort`) | Restated: no App-side entry is planned |

## 6. Choice R — DEL-02-03-REQ-009 and DEP-02-03-009

**What exists at the basis.**
- REQ-009 (SOW L143) and its verification (L181) name PIPELINE `TASK*`
  preselection.
- The Pipeline form is retired (SCA-APP-011), and accepted E80 (CLM-029, L322)
  withdrew the old Pipeline routing examples.
- SCA-APP-011 did not amend REQ-009. Its post-acceptance dependency
  extraction kept DEP-02-03-009 `ACTIVE` with the tension written into its
  Notes (DX-15, `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.md` L75-90) and called it
  "a DEL-02-03 scope question for a later change".
- The scope-closure audits record it as observation `ASC-ISS-001`.
- There is no deliverable summary widget in the live shell (CLM-012 L191).
- `lib/pipeline/pipeline-dispatch-contract.ts` has no product importer.
  `task-scope.ts` loses its only one when `DeliverablesProvider` goes
  (§3.1 S2).

**R-b (recommended), Rows 17–18.**
- Retire REQ-009 and its verification row as `[RETIRED — SCA-APP-012]`
  history, and mark CLM-015 as history.
- Remove the routing wording that only REQ-009 carried: CLM-005 L81, CLM-008
  L116, REQ-013 L147/L185, CLM-025 L287, CLM-026 L297, CLM-028 L317 and the
  APP-R024 clause L350.
- DEP-02-03-009 is retired at dependency re-extraction (Status `RETIRED`,
  SatisfactionStatus `NOT_APPLICABLE`, prior values in Notes). Retiring an
  edge cannot create a cycle.
- DEL-08-03, SOW-007 and PRD §7.5 are unchanged. They already say any later
  consumer needs its own amendment.
- This supersedes the D-APP-56 R4-P29 ownership confirmation (CLM-015), which
  placed the portal deliverable-rows launcher inside REQ-009. That launcher
  no longer exists.

**R-a, Rows 19–22.**
- Restate REQ-009 as optional task-scope preselection: a deliverable row
  carries its stable key into a `TASK` dispatch intent under the DEL-08-03
  contract.
- The obligation stays unimplemented and still needs a widget.
- Because SOW-007 (D L182, L415), DEL-08-03 (SOW L65, D L375, `_CONTEXT.md`
  L33) and PRD §7.5 (L465) say no presentation consumer exists and any later
  one needs its own amendment, R-a becomes that amendment and edits all
  three.
- DEP-02-03-009 stays `ACTIVE`, restated.

**Task Management.** TM-APP-051 (APP-R024, `DEFERRED`) asks for the
scope-scan, summary, status and route consumers of DEL-02-03 to be mapped.
- Under R-b the route consumer is retired.
- The scope-scan consumer is `/api/project/deliverables`; the other route
  goes.
- Summary and status consumers stay unmapped.

The Task Management loop records that disposition after group 3. This
amendment does not write the register.

## 7. Choice P — `/workbench` and `/pipeline`

**What exists at the basis.**
- `app/workbench/` and `app/pipeline/` each hold a `page.tsx` and a client
  that renders `WovenDialogueRoute` with a `LoopTertiaryShell` `legacy`
  element, which is discarded.
- `chat-panel.tsx` `resolveMode` (L195-208) maps the paths to the
  `WORKBENCH`/`PIPELINE` session modes. These key chat drafts (L488), session
  reuse (L499) and session creation (L718).
- `WovenWorkspaceSurface` (`woven-workspace-state.ts` L43) persists
  `'workbench' | 'pipeline'`.
- The Electron renderer-security probe (`electron/main.ts` L647) and the
  packaged security proof (`scripts/run-packaged-security-proof.mjs` L49)
  enumerate all four routes. `contract-pins.manifest.ts` L260 and L384 pin
  both lists.
- The `/pipeline` dispatch query keys (`category`, `taskScopeMode`,
  `scopeKey`, `targetDeliverableKey`) have no live consumer. Only `agent` is
  read by the live shell.
- Route/query compatibility is keyed with DEL-08-02 through DEP-08-02-013 and
  DEL-02-01 REQ-002, REQ-009 and REQ-011.

| Effect | P-keep (recommended) | P-r redirect to `/` | P-d delete (404) |
|---|---|---|---|
| Code | Page clients render the shell without a `legacy` element | Two pages become redirects that keep the query string | Two page directories deleted |
| Existing bookmarks | Open the dialogue shell, as today | Open `/` | 404 (`not-found.tsx`) |
| `WORKBENCH`/`PIPELINE` drafts and session reuse | Unchanged | Not reached through these URLs (records kept) | Same as P-r |
| Electron probe, packaged proof, contract pins | Unchanged | Route lists and pins change; new packaged renderer-security native witness (DEL-09-06) | Same |
| D-APP-108 Q3 | Stands | Superseded | Superseded, and reversed ("no 404") |
| Scope rows | none beyond BASE | Rows 23–29 | Rows 23–29 |
| DEP-08-02-013 | Unchanged | Retired or restated at re-extraction | Same |

P-keep satisfies the direction to retire dead UI. The two page files stop
carrying dead code. What is left is a URL-compatibility behavior that is
live, tested and pinned.

## 8. Item S — no App-side scaffold entry

**Owner direction:** "Scaffolding through the agent is enough." The
coordinating session reports a separate Runtime change, under review and not
merged at this basis, that retires `ProjectScaffoldPort`,
`RuntimeService.scaffold`, `POST /v1/projects/{id}/scaffold`, the client
method and the scaffold types.

**App scope text that names a future App-side scaffold entry** (Baseline
`scope_text_hits`, tag `scaffold_entry`):

| Text | Line | Row | Treatment |
|---|---|---|---|
| DEL-07-02 SOW | L24 (the Runtime API is Runtime-owned; the Runtime loop decides) | 14 | Restated to the owner's decision; the retirement is the Runtime loop's change |
| DEL-07-02 SOW | L25 (follow-up: an App-side entry such as a Runtime application tool or a composed `ProjectScaffoldPort`, defaulting to `<project>/execution`) | 14 | Restated: no App-side entry is planned; the agent scaffolds through `project-setup` into `<project>/execution` |
| DEL-07-02 SOW | L229 (the live composition lacks its `ProjectScaffoldPort`) | 14 | Restated |
| DEL-07-02 SOW | L477 (APP-R058, closed) | — | History; unchanged |
| DEL-06-03 SOW | L364 (CLM-031: write-capable scaffold moves to the later write surface) | 15 | Restated: preview stays read-only; no write-capable App scaffold tool is planned |
| DEL-06-03 SOW | L378, L410 | — | Preview row and Pass-3 disposition; unchanged |
| SPEC §14.2 | L999 (`mcp__chirality__scaffold`, wrap scaffold service or preview, gated) | 16 | Narrowed to the read-only preview (default S-tool) |
| PRD §3.1 goal 17, §6.1 | L155, L323 (scaffold among the in-process tools) | 16 | Read as scaffold preview |
| PRD FR-119, §8.13 sequence, L1513; PLAN R2 L204; TYPES §8.4 L482 | — | — | NO_CHANGE: the retained SDK-path record, preview wording already, or tool-name vocabulary |
| DEL-06-04-REQ-010, PRD §7.3, PLAN §1 L45, DEL-03-03 | — | — | Already consistent (agent path; preview read-only) |
| `_ScopeChange/_LATEST.md` L37 ("the Runtime loop's decision on its scaffold API") | — | — | Pointer text; not edited here. At SCA-APP-012 group 3 the new pointer states that item's status as it is then |

**Merge order.** No App code imports the Runtime scaffold port or types at
the basis: SCA-APP-011 removed the App port member, and the Baseline
`frontend_references` shows `ProjectScaffoldPort` and
`ScaffoldExecutionRoot{Request,Response}` only under
`projects/chirality-runtime/packages`. Rows 14–16 say "no App-side entry is
planned" and name the Runtime API as Runtime-owned "whose retirement is the
Runtime loop's own change". That is true before and after the Runtime change
merges, so neither change depends on the other. If the Runtime change were
withdrawn, the rows would still be true; only the pointer's status line would
differ.

## 9. Findings

### 9.1 The listed items, each verified

| Item | Verified | Evidence at basis |
|---|---|---|
| Loop-first shell reachable only through the discarded `legacy` element | Yes | §3.1 S1: six modules. `woven-dialogue-route.tsx` does `void legacy` since `9b005c23a` (2026-09-09) |
| `lib/portal/agent-matrix-launch.ts` imported only by tests | Yes, and `agent-matrix-cells.ts` too | §3.1 |
| `DeliverablesProvider` has no consumer | Yes | No `useDeliverables` caller; mounted only in `layout.tsx` L104-108 |
| `/api/working-root/scope`: callers | None in App, Electron, scripts or Runtime; no test. Wraps `scanProjectScopes`, which also backs `scope_scan` (`read-tools.ts` L736-751, retained SDK path) | Baseline `frontend_references` |
| `/workbench`, `/pipeline` resolve; `chat-panel.tsx` maps both | Yes (L195-208) | §7 |
| DEL-02-03 REQ-009 still stated at L143 and L181 | Yes; also CLM-015 L216 | §6 |
| Route-preservation clauses: PRD §3.1 goal 25, §6.1, §6.4, §14 metric 20; PLAN §3; SPEC §17.9; D L102; D-APP-74 L97-99, L107 | Yes: PRD L163, L329, L383, L1674; PLAN L118-120; SPEC L1279, L1284-1286; D L102; D-APP-74 L97-99, L107 | Rows 6, 10–13 |

### 9.2 Conflicts found beyond the list

1. **Texts describe a live loop-first UI that has not rendered since
   2026-09-09.** These are PRD §6.3 (L355: "the live baseline"), PLAN §1 (L37:
   "Live loop-first PORTAL, matrix …"), SPEC §17.9 (L1284) and PLAN §13.2
   (L560). The "reversible compatibility selection" of PLAN §13.2 step 2 no
   longer exists. The retirement preconditions of PRD §6.4 were never recorded
   as met, and KG-033 still lists packaged Desktop evidence for the dialogue
   shell as open. Rows 10 and 13 correct the text; the acknowledgment in the
   owner section covers the rest.
2. **The `?legacy=1` link** (§3.2) is computed and discarded. Its only test
   passes through a mock.
3. **PRD FR-001 acceptance (L596) and PRD §12.1 (L1263)** keep "the loop-first
   UI" / "the existing UI" compatible "until separately retired". PLAN §6.5
   (L394) says the same. The coordinator's list did not name these. Rows 10
   and 13.
4. **DEL-02-03-REQ-010** cites PRD FR-010, which SCA-APP-011 retired
   (SOW L144). Its source reference is refreshed in Row 2.
5. **DEL-07-03** names `/api/working-root/scope` as a possible scanner-output
   consumer (L185, L255, L403). Row 3.
6. **DEP-02-03-004 and DEP-08-03-007** quote or label the scope route. Their
   locators and labels are refreshed at re-extraction. DEL-08-03
   `_DEPENDENCIES.md` L91 warns `SOURCE_ENDPOINT_LABEL_CONFLICT`
   (`/api/project/deliverables` against `/api/working-root/scope`); the
   warning resolves once the route is retired.
7. **TM-APP-051 (APP-R024)** covers the same consumers (§6).
8. **DEL-06-03 CLM-031** plans write-capable scaffold execution on a later
   surface. SPEC §14.2 and PRD goal 17 / §6.1 list a scaffold tool. Both
   conflict with direction 2. Rows 15–16.
9. **The page routes are probed and pinned** by the Electron and
   packaged-security code (§7).
10. **`task-scope.ts` becomes test-only** when `DeliverablesProvider` goes
    (§3.1 S2). This is consistent with DEL-08-03 ("No presentation consumer
    exists"). Recorded, not a change.

### 9.3 Observations, not proposed

The Baseline lists 51 other product modules without a product importer at
the basis. They fall into these groups:
- 42 retained SDK/Pi harness modules under `lib/harness/`, kept deliberately
  under D-GOV-43;
- consent test fixtures;
- the deliberately unmounted `work-projection.tsx`;
- `workflows-view.tsx` and `workflow-detail.tsx`, superseded in the Workflows
  tab by `method-library-view.tsx`;
- `lib/workspace/navigation-intent.ts` and `governed-workflow.ts`;
- the DEL-08-03 dispatch contract.

None is legacy loop-first UI and none is proposed here. The
`workflows-view.tsx` pair belongs to DEL-02-02 and may interest that
deliverable's owner.

## 10. Dependencies and the DAG

**D-GOV-49 currency.** The App has no accepted project DAG (no
`execution/_DAG/`). Closure at the basis is 54 nodes, 103 edges and 0 SCCs
(Baseline `tools.analyze_dep_closure`). There is no accepted DAG version to
mark stale.

| Row | Content | R-b / P-keep | R-a | P-x |
|---|---|---|---|---|
| DEP-02-03-009 (DEL-02-03 → DEL-08-03, INTERFACE, routing/preselection) | `ACTIVE`, DX-15 tension | **Retire** at re-extraction | Keep, restated | — |
| DEP-02-03-004 (DEL-02-03 → REF-003, workspace API contract) | `ACTIVE`; EvidenceQuote lists `/api/working-root/scope` | Refresh the quote | Same | Same |
| DEP-08-03-007 (DEL-08-03 → SPEC §17.2 "working-root scope API") | `ACTIVE` | Refresh the target label to `/api/project/deliverables` | Same | Same |
| DEP-08-02-013 (DEL-08-02 → DEL-08-03, row-level OPERATIVE → PIPELINE routing) | `ACTIVE` | Unchanged | Unchanged | Retire or restate |
| DEP-02-01-006, DEP-02-02-020 (legacy compatibility semantics owned by DEL-08-02) | `ACTIVE` | Unchanged | Unchanged | Refresh wording |

No row in any register names the loop-first shell modules,
`DeliverablesProvider` or `ProjectScaffoldPort` (Baseline `dependency_rows`).
Only edges are removed, and no new edge is proposed, so no cycle can form.
Every change is a dependency-extract rerun after acceptance, never a direct
write by this workflow.

## 11. Downstream consumers

| Consumer | Effect |
|---|---|
| App frontend | The code change after group 3 (§13) |
| MCP tools (`read-tools.ts`) | None: `scope_scan` and `scaffold_preview` call their libraries directly |
| Runtime (`projects/chirality-runtime`) | None from this amendment: no reference to `/api/working-root/scope`. Its own scaffold-API retirement is separate and pending (§8) |
| Electron and packaged security proof | None under P-keep; route lists, pins and native witness under P-x |
| Task Management | TM-APP-051 disposition note after group 3 (§6) |
| `exports/chirality-app` projection | Lists the deleted files; regenerated with the code change |
| Historical run records, secret-scan and review hash files, tranche manifests | Mention paths; historical, not rewritten |
| Piping, PEC, Root `tools/` | No reference found |

## 12. ISSUED deliverables

**None.** Across the App, 53 deliverables are `IN_PROGRESS` and 1 is `OPEN`
(retired DEL-09-07). There is no `ISSUED` and no `CHECKING` deliverable. All
affected deliverables are `IN_PROGRESS`, so no reopening is authorized or
needed. `ScopeChanging` is recorded on every row regardless.

## 13. The code change (after group 3; not in this package)

1. Delete the six S1 modules and the two `lib/portal` modules. Remove the
   `legacy` prop from `WovenDialogueRoute` and its four callers, and the
   `legacyHref` thread. Delete `deliverables-provider.tsx` and its layout
   mount, and `app/api/working-root/scope/route.ts`.
2. Remove the §3.2 symbol residue and the eleven CSS tokens. Keep
   persisted-state parsing tolerant of the `'workbench' | 'pipeline'` and
   sidebar tab values (SPEC §17.8).
3. Handle the tests as in §3.3.
4. Under P-keep, keep both page routes; they render the shell with no legacy
   element. Under P-x, apply the redirect or deletion and re-evidence the
   packaged renderer security (DEL-09-06).
5. Take the scope text from group 2, not from the code PR.
6. Update the tranche manifest, if the App loop records one for the code
   change, and regenerate the export projection.
7. Rerun on the actual candidate: typecheck, the full frontend tests, the
   build and premerge gates, and the registered checks. Product source also
   needs the fresh read-only `software-code-review`.

## 14. Package-role classification and derivative status

| Surface | Package role | Classification | Authority basis |
|---|---|---|---|
| Decomposition v3.2 | Working surface | DIRECT_EDIT at application | Group-2 exact text |
| `contract_invariant_coverage_register.csv` | Authoritative companion register | NO_CHANGE (default E) | No enforcement surface changes |
| `docs/PRD.md`, `docs/SPEC.md`, `docs/PLAN.md` | Authoritative carriers outside the decomposition | DIRECT_EDIT only if the group-2 write boundary names them | Contract `ALLOWED_PROPAGATION_WRITES` |
| `docs/DIRECTIVE.md`, `docs/TYPES.md` | Authoritative carriers | NO_CHANGE under P-keep; DIRECT_EDIT under P-x only if named | Same |
| Affected `ScopeOfWork.md` (DEL-02-01, 02-03, 06-03, 07-02, 07-03, 08-02; R-a adds 08-03; P-x adds 02-02) | Deliverable production contracts | Named in the group-2 boundary, or handed to `project-setup` INCREMENTAL (`scope-of-work` REVISE) | Contract non-ownership |
| DEL-08-03 `_CONTEXT.md` (R-a only) | Working surface | DIRECT_EDIT at application | Default write scope |
| Other `_CONTEXT.md` | Working surface | NO_CHANGE (no affected wording) | Baseline `scope_text_hits` |
| `_STATUS.md` | Working surface | NO_CHANGE (no REMOVE; no lifecycle change) | — |
| `Dependencies.csv` / `_DEPENDENCIES.md` | Deliverable dependency evidence | RECOMPUTE by dependency-extract | §10 |
| `_Coordination/_TaskManagement/REGISTER.csv` | Task Management record | Downstream: its loop records the TM-APP-051 disposition | §6 |
| `_ScopeChange/_LATEST.md` | Snapshot / handoff artifact | Unchanged until group 3 | Pointer posture `ACCEPTED_PREDECESSOR` (SCA-APP-011) |
| `_Evaluation/DecompCoverage`, `ScopeClosureAudit`, `DepClosure` snapshots | Derived publication artifacts | STALE_REBUILD_REQUIRED after application | audit-decomp, audit-scope-closure, `analyze_dep_closure` |
| `exports/chirality-app` | Derived publication artifact | Regenerated with the code change | Export tooling |

| Derivative package | Owner | Status after amendment | Required action |
|---|---|---|---|
| Deliverable Scopes of Work not written directly | `project-setup` INCREMENTAL (`scope-of-work` REVISE) | STALE_REBUILD_REQUIRED | REVISE after group 3 |
| Dependency registers of DEL-02-03, DEL-08-03 (and DEL-08-02, DEL-02-01 under P-x) | dependency-extract | STALE_REBUILD_REQUIRED | Re-extract; then `analyze_dep_closure` |
| Decomposition coverage audit | audit-decomp | STALE_REBUILD_REQUIRED | Post-change baseline at group 3 |
| Scope-closure audit | audit-scope-closure | STALE_REBUILD_REQUIRED | After incremental setup |
| Export projection | App export tooling | STALE_REBUILD_REQUIRED at the code change | Regenerate |

## 15. Orphan and structural risk

| Check | R-b + P-keep | R-a | P-x |
|---|---|---|---|
| IN scope items without a deliverable | 0 | 0 | 0 |
| Objectives without a deliverable | 0 | 0 | 0 |
| Packages without a deliverable | 0 | 0 | 0 |
| Dangling dependency references | DEP-02-03-009 retired; 2 label refreshes | 2 label refreshes; DEP-02-03-009 restated | DEP-08-02-013 retired or restated |
| Topology | 10 / 52 / 84 / 10 | same | same |
| Package-discipline rule | Kept | Kept | Kept |

## 16. Supersession bindings to prepare at group 2

| Rows | Superseded authority fact | Type |
|---|---|---|
| 1, 5, 10, 12 | D-APP-74 L97-99 ("… current UI remain compatibility surfaces until separately retired") and L107 ("Old-UI retirement requires separate owner acceptance after parity, accessibility, compatibility, and packaged Desktop evidence") for the loop-first UI | SUPERSESSION |
| 2, 6, 11, 12 | D-APP-74 L97-99 for `GET /api/working-root/scope` | SUPERSESSION |
| 14 | SCA-APP-011 accepted DEL-07-02 text (the Runtime loop decides on its scaffold API; follow-up App-side entry) | SUPERSESSION |
| 17 (R-b) | D-APP-56 R4-P29 ownership confirmation in DEL-02-03 CLM-015 | SUPERSESSION |
| 21 (R-a) | SCA-APP-010 Supersession_Map D-006 (Pipeline controls presentation retired; any re-hosting a separate amendment) | SUPPLEMENTARY_EXTENSION |
| 23–29 (P-x) | D-APP-108 Q3 (L48: reachable, unlisted, no 404) | SUPERSESSION |

The cumulative map is carried forward from SCA-APP-011 through
`accumulate_supersession_map.py` at group 3.

## 17. Active snapshot and handoff-state impact

- **Pointer posture for group 3: `ACCEPTED_PREDECESSOR`.** `_LATEST.md` names
  SCA-APP-011 (`OPEN_PENDING_DERIVATIVE_CLOSURE`) and stays unchanged until
  SCA-APP-012's group-3 acceptance. SCA-APP-011's open derivative items
  remain its own, apart from the Runtime scaffold-API item, which the new
  pointer reports as it then stands.
- **Decision snapshots.** Group-1 and group-2 decisions will be recorded under
  `_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-{1,2}_{date}/`, with
  `SCA-APP-012_GROUP-{1,2}_AUTHORIZED.md` pointers. None exists and none is
  created here.
- **Group 3.** No `ISSUED` deliverable is involved, so the group-3 decision
  folder is optional (SCA-APP-011 recorded one).

## 18. Estimate and schedule staleness

The App carries no `_Estimates` tool root (the structure audit reports it
missing, carried). No estimate or schedule artifact is affected.

## 19. Recommended downstream reruns (after group 3; none executed here)

1. `project-setup` in `INCREMENTAL` mode: `scope-of-work` REVISE for the
   modified deliverables not written directly.
2. `dependency-extract` for DEL-02-03 and DEL-08-03, plus DEL-02-01 and
   DEL-08-02 under P-x; then `analyze_dep_closure.py`.
3. `audit-decomp` (post-change baseline) and `audit-scope-closure`.
4. Task Management: TM-APP-051 disposition note.
5. The code change (§13), under the App loop and standing Git authority, once
   group 3 is accepted.

## 20. What checkpoint group 2 will contain

- `Amendment_Preview.md` with exact before/after text for every selected row.
- `Propagation_Plan.md` with the exact write boundary, including which Scopes
  of Work and which PRD, SPEC and PLAN passages this amendment writes directly.
- `Amendment_Actions.csv` limited to the selected sets, with `ScopeChanging`
  on every row.
- `Supersession_Delta.csv`.
- The validation plan.
