# D-GOV-52 — Align two Root `AGENTS.md` passages with App v4 owner decisions

> **Status: CANDIDATE — NOT RULED.** This packet binds nothing (K-AUTH-1).
> It changes no instruction. `AGENTS.md` changes only through a later owner
> act and the application tranche that act authorizes. Writing, validating,
> committing or merging this packet is not approval.
>
> **Provisional ID:** D-GOV-52, the next free ID after D-GOV-51. Checked by
> `git grep "D-GOV-52"` on the working tree and on the local `origin/main`
> ref (`714199f7be`): no use. Reconcile to the actual next free ID at
> staging.
>
> **Basis:** working tree at `HEAD` `1c0cec9794c649fc3042a0e90807ff30fc9aed00`
> (branch `claude/app-v4-home-path-redaction`). Root `AGENTS.md` sha256
> `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd`
> (14200 bytes). It is identical at `HEAD` and the local `origin/main` ref
> (`git diff --stat origin/main -- AGENTS.md` is empty; the ref was not
> fetched).
>
> **Framed by:** a Type 2 TASK (node IC of run
> `APP-V4-DESIGN-PASS-4-20261003`, Claude Opus 5.5), dispatched by
> HELP_HUMAN. It does not delegate and wrote only this folder.
>
> **Record convention:** exact-prose candidate (D-GOV-23 pattern) with an
> inactive patch (D-GOV-43 pattern). Supersede, never edit: D-GOV-43 and its
> record are not changed. If the patch does not apply exactly at application,
> the wording comes back to the owner for approval again.

---

## 0. Purpose

Two passages of Root `AGENTS.md` no longer match decisions the owner made
for App v4:

- **(a)** "Instruction changes take effect at a verified idle boundary,
  preserving prior supplied content and conversation history." App v4
  DECISION-L L-2 fixes a conversation's role for its life. Edited guidance
  reaches new conversations only.
- **(b)** The App does not "veto the user's Codex configuration." The App v4
  design runs the App's own Codex with analytics off, as a session flag on
  the App's child process.

This packet proposes the smallest exact edits for both passages. It also
says whether (b) is a real conflict, names the loops to notify, lists the
checks, and lists what the owner approves.

## 1. Authority chain

| Source | What it supplies |
|---|---|
| Owner, 2026-10-03, verbatim: "1 yes, 2 no rewrite, 3 go, 4 A+C" (item 3 as put to the owner is quoted in the manifest); recorded in `projects/chirality-app-v4/execution/_Coordination/AgentRuns/APP-V4-DESIGN-PASS-4-20261003/OWNER_DECISIONS.md` (sha256 `0883eb7d8b88be7c1859661bcceab53947a35f49d7d93d39372cb2a01ef356f2`, untracked at the basis) | Direction to prepare this package. The owner applies it later in a separate act (effect 3) |
| Root `AGENTS.md` §Execution and governance | "Instruction changes require their own authorized scope and tranche manifest", and the rule to notify each affected project loop whose authority corpus or contract mirrors pin changed instructions |
| `docs/PRD_ROOT.md` O-10, D-11, D-12 | Root instruction changes are governance acts that need accountable human acceptance. A routed notice goes to each loop that pins or mirrors the changed surface. Root instruction changes use M2/G4 tranches |
| `tools/validation/validate_instruction_tranche_manifest.py` (G4) | Manifest schema and location (`docs/governance_harness/tranche_manifests/<TRANCHE_ID>.yaml`). Changed instruction-surface paths must be covered by an added manifest |
| `.agents/skills/chirality-change/SKILL.md` | PR closeout under the standing Git grant. The notice rule: the receiving loop decides whether to adopt |

## 2. Decision requested

The owner is asked to approve or reject the two exact edits in Annex A (E-1,
E-2), choose among the options in §3 and §4, and approve the notice routing
in §5. §7 lists every item. The application itself is a later owner act.

## 3. E-1 — passage (a), instruction changes

**Current** (`AGENTS.md` lines 204–206):

> Instruction changes take effect at a verified idle boundary, preserving
> prior supplied content and conversation history.

**Proposed (A1, recommended):**

> Instruction changes take effect at a verified idle boundary or, where the
> App fixes a conversation's role guidance for its life, in new conversations
> only, preserving prior supplied content and conversation history.

The next sentence ("A full-history fork alone does not establish a different
role.") stays unchanged.

**Reason, with sources (paths under `projects/chirality-app-v4/execution/`):**

- DECISION-L L-2 (`_Coordination/AgentRuns/APP-V4-DESIGN-PASS-3-20261001/OWNER_DECISIONS.md`
  lines 141–178, sha256 `8a5d1114…20ac`): "a conversation's role is fixed
  for its life; a different role is a new conversation … Edited guidance
  applies to new conversations."
- R19-3 and R19-8 (same folder, `R19_RESOLUTIONS.md` lines 46–55 and
  113–118, sha256 `16930ecd…2a12c`). R19-3: K-9's "next idle point" becomes
  "new conversations". R19-8: at 0.158.0 a fork keeps the source's role.
- OBS-2 O-5 (`PKG-01_…/DEL-01-01_…/Design/OBS_2_0.158.0.md` §7, line 181,
  sha256 `61cc34ff…4ac0`): at Codex 0.158.0, `developerInstructions` on
  `thread/resume` "is accepted without error and silently ignored".
- OBS-3 W-6 (`…/Design/OBS_3_0.158.0.md` §8, line 191, sha256
  `554ac445…a843`): a fork "does not take new developer instructions".
- ROLE-v0.2 F-R9 (`PKG-02_…/DEL-02-04_…/Design/ROLE_SUPPLY.md` lines
  682–685) records this difference for an instruction-change notice.

**Why A1 keeps the idle-boundary clause rather than replacing it.** App v4
is a design-stage project: its design files are marked "DRAFT DEFINITION —
proposed, unsupplied, not implemented, not accepted". `projects/chirality-app-v4/README.md`
says "The published fallback remains v3.0.1 until its separate replacement
decision". Two other surfaces still describe the v3 App's idle-boundary
adoption:

- Root `docs/AGENT_WORKFLOW_RUNTIME.md`, lines 176–189: "confirmed idle
  unload followed by cold resume" at Codex 0.154.0.
- `projects/chirality-app-dev/AGENTS.md`, lines 97–98: "Edits apply at a
  confirmed safe boundary".

A1 stays true for both products and contradicts neither surface. The
idle-boundary sentence entered Root `AGENTS.md` in commit `95b3425195`,
together with the v3 product-guidance work.

**Alternative (A2, not recommended):**

> Edited role guidance reaches new conversations only, and a conversation's
> role is fixed for its life, preserving prior supplied content and
> conversation history.

A2 states App v4's rule for every App. It would contradict the published v3
App and the two surfaces above, unless the owner also directs that they be
aligned or that v3 be retired.

## 4. E-2 — passage (b), the user's Codex configuration

**Finding: a wording clarification, not a substantive conflict.** This is an
inference. It rests on the following reasoning, and the owner confirms or
rejects it in §7 item 2.

1. *What "veto" meant where it came from.* The D-GOV-43 proposal describes
   the retired v3 daemon as hosting a "configuration-vetoed Codex App
   Server" (`D-GOV-43.proposed.md` line 34). Ruling item 3 ends "There is no
   effective-configuration veto" (line 186). `IMPACT.md` family 2 names the
   retired mechanism: an "effective-configuration veto (`config/read` table
   checks)", whose purpose was to "Keep the agent inside a fixed, projected
   contract". The veto, then, was checking the user's effective configuration
   against a fixed table and enforcing it.
2. *What App v4 does* (paths under `PKG-01_…/1_Working/`):
   - It reads the person's `config.toml` through a link.
   - It writes that file only on the person's act (ACCESS-v0.2 I-2).
   - When Codex refuses a setting, the App shows the refusal and never
     "fixes" it (F-32).
   - Approval and sandbox reach Codex unchanged.
   - Plugins follow the person's own setting (L-3). The fallback
     `plugins = false` flag only repeats the person's own "off".
   - It never sends `features.*`, approval or sandbox keys (HOSTING-v0.9
     §8.2).

   The only value the App chooses itself that can differ from the person's
   is `analytics.enabled = false`. The App always passes it as a `-c`
   session flag to its own child (ACCESS-v0.2 §6 Q-1 step 3 and §9; K-12 per
   DECISION-K3 revised; HOSTING-v0.9 §4.2 step 3). Codex forms it into the
   `sessionFlags` layer (OBS-2 O-6 M2). The App records it in HOSTING's
   configuration identity. The network view shows it as `turned-off-by-app`
   (schema `access.network-observation`). It is never written to the
   person's file.
3. *Why the wording still needs work.* A person may set analytics on in
   their own file. The App's Codex still runs with analytics off. A literal
   reading of "veto the user's Codex configuration" could cover that case.
   The App v4 design itself reads Root that broadly:
   - HOSTING-v0.9 §8.2: "the person's Codex configuration is not overridden
     (Root `AGENTS.md` …)".
   - ACCESS-v0.2 §9 and U-A9: "Whether the person may turn analytics back
     on for the App … (Root `AGENTS.md`: the App does not 'veto the user's
     Codex configuration')".
   - HELP_HUMAN's K-10 reservation in DECISION-K3.

   That reservation lapsed when K-10 was revised. The analytics flag remains.

So the analytics flag does not conflict with the meaning D-GOV-43 ruled. The
sentence's wording is ambiguous, though, and one sentence settles it. If the
owner reads "veto" broadly, the flag is a conflict. The fix would then be B2
below, or a change to K-12 for analytics in App v4.

**Current** (`AGENTS.md` lines 191–193, unchanged by the proposal):

> It does not filter Codex's notifications, leave a server request
> unanswered, veto the user's Codex configuration, pin approval or sandbox
> policy, or run a patched supplier.

**Proposed (B1, recommended): insert one sentence directly after it:**

> A setting the App passes only to Codex processes it owns, such as turning
> off Codex's analytics, is not a veto: it is shown and recorded, and the
> user's configuration file is unchanged.

**Option (B2):** B1 plus "; the user can reverse it in the App" before the
final period. B2 settles App v4's open item U-A9 ("Yes" proposed, owner of
the point: integrator, doctrine) at Root level. B1 leaves U-A9 to App v4.
B1 is recommended because it keeps Root minimal. The claim "not a veto" is
strongest if U-A9 resolves "Yes".

## 5. Affected surfaces, mirrors and loops

**How this was checked:**

- `git grep -l` for the current `AGENTS.md` sha256.
- Parsing `projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json`.
- Reading every `projects/*/chirality.project.json` and
  `frontend/scripts/prepare-packaged-instruction-root.mjs`.
- `git grep` for both passages' wording ("idle boundary", "safe boundary",
  "veto", "idle unload") across project `AGENTS.md`, `loop/`, `docs/` and
  App v4 Design files.

| Surface | Kind | Finding | Action |
|---|---|---|---|
| Any loop's authority corpus | Exact-hash pin | App v3 `AUTHORITY_CORPUS.json` `current_version` v25. Its `refs` list does not include `AGENTS.md`. No other loop has a corpus that contains it | None |
| `projects/*/chirality.project.json` | Manifest | `agentsOverlay` and `instructionRoot` only; no hashes | None |
| App packaged instruction root | Generated mirror | Bundles `projects/chirality-app-dev/instructions/AGENTS.md`, not Root `AGENTS.md` (`prepare-packaged-instruction-root.mjs` lines 11–12 and 264) | None |
| `exports/chirality-app/export-manifest.csv` line 23 | Root-owned derivative | Pins `AGENTS.md`, 14200 bytes, `c8ce87ef…` | Regenerate through `exports/chirality-app/export_public.py` in the application tranche, or record a deferral |
| Historical exact-hash pins | Run evidence | 758 files: App v4 241, Piping 430, PEC 81, App v3 5, export 1. They include run records, App v4 `_DAG/DAG-00N/Evidence/Tool_Run.json` `selected_context`, reviews and PEC proposals | Never rewritten. App v4's next DAG currency observation may report the changed Root input; App v4 decides |
| **App v4** (`projects/chirality-app-v4`) | Semantic mirror and originator | ROLE-v0.2 F-R9; R19-3; HOSTING-v0.9 §2 and §8.2; ACCESS-v0.2 §9 and U-A9; `conceptual/WORKING_RECORD.md` line 26 pin | **Notice.** Close or update F-R9 and the Root citations. U-A9 stays App v4's unless the owner chooses B2 |
| **App v3** (`projects/chirality-app-dev`) | Semantic mirror | Local `AGENTS.md` lines 97–98 ("Edits apply at a confirmed safe boundary") and `docs/harness/reliance_boundary_register.md` RB-SETTINGS ("without a Chirality veto"). Both stay consistent with A1 and B1 | **Notice**, informational. No adoption work under A1/B1. Under A2, App v3 would have to assess the conflict |
| **Runtime** (`projects/chirality-runtime`) | Implementer | Implements the v3 adoption mechanism described in Root `docs/AGENT_WORKFLOW_RUNTIME.md` lines 176–189. Its `AGENTS.md` and `docs/` carry neither passage | **Notice**, informational (precedent: `APP-PRODUCT-GUIDANCE-UPDATES-20260912` routed App and Runtime) |
| Piping, PEC | Instruction-root readers | No live pin and no copy of either passage. Their sessions read Root `AGENTS.md` live, and both passages concern the App only | None required (precedent: `ROOT-FOUR-GRAPH-ORIENTATION-20260919`, `none-required`) |
| Root `docs/AGENT_WORKFLOW_RUNTIME.md` lines 166–189 | Related Root surface | Describes the v3 App, consistent with A1 | Not changed here. It may need an App v4 counterpart when App v4 replaces v3 |

**Loops to notify:** App v4 (substantive), App v3 and Runtime
(informational). Annex B has the notice text.

## 6. Checks

Done at this basis:

- `git apply --check` of `AGENTS.proposed.patch` passed. Applied in a
  scratch copy, it yields `AGENTS.md` sha256
  `f96feb19d297c74e10048c506805b2fe3622c50cfefd6078f599724556113977`
  (14481 bytes). It adds no line longer than 80 columns: the 8 longer lines
  are pre-existing.
- `validate_manifest` (G4 function) on `ROOT-DGOV52-PROPOSAL-20261003.yaml`
  found no failures.
- At baseline, `validate_instruction_tranche_manifest.py` (CI mode),
  `validate_agent_instructions.py --json` and
  `validate_instruction_entrypoints.py .` pass.
- `validate_path_anchors.py .` already fails at baseline on one finding:
  `projects/chirality-app-v4/execution/_Coordination/_COORDINATION.md:18`,
  a home-directory path that this branch's redaction work addresses. The
  patch adds no path.
- `run_affected_tests.py --dry-run` for `AGENTS.md` plus this packet selects
  `practitioner_harness` and `validation`.

At application (owner-ruled):

1. Re-run `git apply --check` on the application basis. If `AGENTS.md`
   changed in the meantime, re-derive the patch. Any change of wording comes
   back to the owner.
2. Apply. Check `shasum -a 256 AGENTS.md`: it should equal the value above
   if the basis is unchanged. Check that `grep -c "in new conversations only"
   AGENTS.md` = 1 and `grep -c "is not a veto: it is" AGENTS.md` = 1.
3. Place the application manifest (Annex C) and the three notices. Run
   `python3 tools/validation/validate_instruction_tranche_manifest.py --base
   <base> --head HEAD --added-manifests-only` (G4) and CI mode.
4. `python3 tools/validation/validate_agent_instructions.py --json`,
   `python3 tools/validation/validate_instruction_entrypoints.py .` and
   `python3 tools/validation/validate_path_anchors.py .`.
5. `python3 tools/run_affected_tests.py --base <base>`.
6. Regenerate the export, or record the deferral in the manifest's
   `derivative_disposition`.
7. Independent review of the exact candidate revision and required CI, under
   the standing Git grant (`chirality-change`).

## 7. What the owner approves

1. **E-1:** A1 (recommended), A2, or no change.
2. **E-2:** that (b) is a wording clarification, not a conflict (§4); then
   B1 (recommended), B2 (also settles U-A9 "Yes"), or no change.
3. **Instrument:** a D-GOV-52 ruling record and register row (recommended,
   because E-2 restates the wording of D-GOV-43 item 3), or an ordinary M2
   tranche without a D-GOV record (precedent
   `ROOT-FOUR-GRAPH-ORIENTATION-20260919`).
4. **Notices:** App v4, App v3 and Runtime as in §5; none to Piping or PEC.
5. **Export:** regenerate in the application tranche, or defer.
6. **Application:** a later act that authorizes the application tranche
   (Annex C).

Not asked here: any App v4 design matter. U-A9 is asked only if B2 is
chosen.

## 8. Scope limits

This packet edits nothing outside this folder. It does not change:

- `AGENTS.md` or any other instruction;
- the D-GOV register or `_DECISIONS/`;
- App v4 design files;
- App v3 or Runtime instructions;
- `docs/AGENT_WORKFLOW_RUNTIME.md`;
- the export;
- any loop's basis.

Files in this folder:

- `PACKET.md`
- `AGENTS.proposed.patch`: the exact inactive delta, A1 + B1.
- `ROOT-DGOV52-PROPOSAL-20261003.yaml`: the proposal tranche manifest. Move
  it to `docs/governance_harness/tranche_manifests/` before committing; G4
  reads manifests only from there.

---

## Annex A — Exact text

### A.1 Passage (b): lines 191–198 after the edit (B1)

```text
stream. It does not filter Codex's notifications, leave a server request
unanswered, veto the user's Codex configuration, pin approval or sandbox
policy, or run a patched supplier. A setting the App passes only to Codex
processes it owns, such as turning off Codex's analytics, is not a veto: it is
shown and recorded, and the user's configuration file is unchanged. Approval
and sandbox policy are the user's choice per project and per turn; changing
them grants nothing beyond what the host enforces. Local models are Codex
model providers, not a second engine.
```

### A.2 Passage (a): lines 207–211 after the edit (A1)

```text
product guidance and their intended full role. Instruction changes take effect
at a verified idle boundary or, where the App fixes a conversation's role
guidance for its life, in new conversations only, preserving prior supplied
content and conversation history. A full-history fork alone does not establish
a different role.
```

The authoritative delta is `AGENTS.proposed.patch`. Only line wrapping
changes outside the two inserted phrases.

## Annex B — Notice text (for the application tranche)

Path: `projects/<loop>/execution/_Coordination/NOTICE_<date>_ROOT_D-GOV-52_AGENTS_MD_APP_V4_ALIGNMENT.md`
for `chirality-app-v4`, `chirality-app-dev` and `chirality-runtime`.

```markdown
# Notice — Root AGENTS.md: instruction-change timing and App-process settings (D-GOV-52)

Root `AGENTS.md` changed at <commit> (sha256 <new>; was c8ce87ef…1dffd), under
<ruling or manifest>. Two passages:

1. "Instruction changes take effect at a verified idle boundary or, where the
   App fixes a conversation's role guidance for its life, in new
   conversations only, …"
2. Added after "does not … veto the user's Codex configuration …": "A setting
   the App passes only to Codex processes it owns, such as turning off
   Codex's analytics, is not a veto: it is shown and recorded, and the user's
   configuration file is unchanged."

This notice is coordination, not authority. Your loop decides whether to
adopt, amend or decline.
<App v4 only:> ROLE-v0.2 F-R9 and the Root citations in HOSTING-v0.9 §2/§8.2
and ACCESS-v0.2 §9/U-A9 may be updated; U-A9 remains yours <unless B2>.
<App v3, Runtime:> Both edits are consistent with the v3 idle-boundary path
and RB-SETTINGS; no adoption work is expected.
```

## Annex C — Application tranche manifest (draft; complete at application)

```yaml
schema: instruction-tranche-manifest/v1
tranche_id: ROOT-DGOV52-APPLICATION-<YYYYMMDD>
title: Apply D-GOV-52 - Root AGENTS.md instruction-change timing and App-process settings
date: <YYYY-MM-DD>
basis: <application basis sha>
instruction_surface_paths:
  - AGENTS.md
  - docs/governance_harness/_DECISIONS/D-GOV-52_agents_md_app_v4_alignment.md   # if item 3 = D-GOV record
  - docs/governance_harness/_DECISIONS/_REGISTER.md                              # if item 3 = D-GOV record
  - docs/governance_harness/tranche_manifests/ROOT-DGOV52-APPLICATION-<YYYYMMDD>.yaml
  - projects/chirality-app-v4/execution/_Coordination/NOTICE_<date>_ROOT_D-GOV-52_AGENTS_MD_APP_V4_ALIGNMENT.md
  - projects/chirality-app-dev/execution/_Coordination/NOTICE_<date>_ROOT_D-GOV-52_AGENTS_MD_APP_V4_ALIGNMENT.md
  - projects/chirality-runtime/execution/_Coordination/NOTICE_<date>_ROOT_D-GOV-52_AGENTS_MD_APP_V4_ALIGNMENT.md
m2_gate:
  authorization: <owner's ruling, verbatim, with its custody>
  authorized_by: Ryan Tufts
  authorization_date: <YYYY-MM-DD>
  integration_owner: <the single serialized integration owner>
  merge_gate: owner-authorized-pr
  self_merge: true
m6_notice:
  disposition: routed
  routed_to: [<the three notice paths above>]
  rationale: >-
    App v4 originated both differences and mirrors the Root text in its
    design files; App v3 and Runtime implement or mirror the passages.
    Piping and PEC hold no pin or copy of either passage.
scope_limits:
  - the two AGENTS.md passages of Annex A only
  - no App v4, App v3 or Runtime instruction or design change
derivative_paths:
  - exports/chirality-app/export-manifest.csv
  - exports/chirality-app/export-report.md
  - exports/chirality-app/staging/
derivative_disposition:
  status: <regenerated | deferred>
  rationale: <...>
```
