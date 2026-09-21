# DOC-BUILDREL notes (EXT item 4, `docs/BUILD_AND_RELEASE.md`)

Audit question: does each section match what shipped at the frozen basis `00115c719`? Evidence was code and
packaging config under `projects/chirality-app-dev/frontend/**`, `R2/SURFACES/BUILD_*` and `ELECTRON_*`, the
gate transcripts, and, as evidence only, the two workflows and the `APP_V3_*` release AgentRuns records.

## 1. Census

- 48 rows over 15 indexed units (`#0`..`#14`). Coverage is complete.
- ClaimType: STATE_ASSERTION 27, REQUIREMENT 19, CONTEXT_CLAIM 2.
- Disposition: ALIGNED 32, STALE_SPECIFICATION 13, NOT_AUDITABLE 2, UNKNOWN 1.
- Confidence: HIGH 33, MEDIUM 14, LOW 1.
- HumanDecisionNeeded: NO 45, R4-Q1 3 (`#4.6`, `#4.7`, `#4.16`).
- **Split rate:** 4 of 15 units split (27%), giving 37 sub-rows.
  - `#4`: 14 table rows plus 2 prose rows (`.15`, `.16`).
  - `#7`: 5 table rows.
  - `#9` (§8.1): 6 numbered items plus the closing paragraph (`.7`).
  - `#10` (§8.2): 9 numbered items. The closing sentence is folded into `.9`.
- **SEE rows:** 0.
- **RELEASE_PROCESS_NOT_RUN rows:** `#4.7`, `#7.4`, `#9.3`, `#9.5`, `#11`, `#12`.

## 2. Least-confident rows

- **`#9.5` (LOW, UNKNOWN): packaged S-6/S-8.**
  - The source-run App passed S-1..S-8.
  - For the packaged App, `BUILD_EVIDENCE_20260912.md` says the agent did not run these checks, and
    `OWNER_TRIAL_NOTES.md` says the agent does not assert the owner's installation checks.
  - I found no record of these checks on the published v3.0.0.
  - Alternatives: `DOCUMENTED_UNIMPLEMENTED` if the owner confirms they were not run; `ALIGNED` if the owner ran
    them without a record.
- **`#9.3` (MEDIUM, ALIGNED): notarize.**
  - No notarization code exists. Notarization was done by hand for v3.0.0.
  - The package version at the basis is 3.0.1, and I found no 3.0.1 notarization record.
  - Alternative: `PARTIALLY_IMPLEMENTED`, if the step is read as covering the version at the basis rather than
    the published release.
- **`#10.6` (MEDIUM, STALE):** a static reading that `pack-electron.mjs` `REQUIRED_BUILD_INPUTS` fails without
  `instruction-root:prepare`. Nothing was executed.
- **`#4.6` (MEDIUM, STALE):** the "route-level" claim fails because the live turn route is backed by the Runtime
  daemon. Alternative: `ALIGNED` at module level, since the script runs its test (recorded as `ALSO_MODULE`).
- **`#5` (MEDIUM, ALIGNED):** I did not see the "Validation gate" field by name in the two build records I read.
  Alternative: `PARTIALLY_IMPLEMENTED`.

## 3. Register-defect summary

None. This is a governance support document, not a deliverable register, so there are no REGISTER rows.

## 4. Direction and cause

- **CauseTags:**
  - CODEX_SOLE_ENGINE 5: legacy Agent SDK and Pi commands and profile rows; the §10 open-decisions list.
  - A2_TOPOLOGY 3: the `desktop:pack` and `desktop:dist` chains and the §8.2 sequence, restructured by `f055fe9ed`
    and `39c0bb6ab`.
  - V3_RELEASE_SCOPE 3: the "future" framing and the v2.0.0 sentence, overtaken by the 2026-09-13 v3.0.0
    publication.
  - PRE_V3_DRIFT 2: the Node engine floor, raised 2026-07-23 in the D-APP-72 tranche, and the network-proof
    output location, moved 2026-08-01.
  - LIFECYCLE_GATE_PENDING 1: `#9.5`.
- **CAUSE2:** A2_TOPOLOGY (`#1`), CODEX_SOLE_ENGINE (`#4.13`, `#4.14`), V3_RELEASE_SCOPE (`#12`).
- **CONTEXT records used:**
  - `AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`: v3.0.0 notarized, stapled and published
    2026-09-13T05:08:54Z.
  - `BUILD_EVIDENCE_FINAL_UPDATES_20260913.md`
  - `APP_V3_CODEX_HOST_REPLATFORM_20260912/{PACKAGING_PROCEDURE,BUILD_EVIDENCE_20260912,RUN_LOG}.md`
  - `OWNER_TRIAL_NOTES.md`
- **GOVERNING:** D-GOV-43 (via App CONTRACT line 17 and D-APP-127), D-APP-72 (the ruling record names Node 22.19)
  and D-APP-127.
- **NONE_FOUND (`#6`):** I grepped `_DECISIONS/_REGISTER.md` for "network-policy" and "Evidence" and scanned the
  CONTEXT AgentRuns. Neither records the move of the network-proof output into the DEL-09-06 Evidence folder.
- **Manager summary: what ran and what did not.**
  - Ran at or before the basis: Developer ID signing, manual notarization and stapling, and GitHub publication of
    v3.0.0 with a `.sha256` asset.
  - Not evidenced as run:
    - packaged S-6/S-8;
    - a 3.0.1 notarization or publication;
    - the hosted release job, which `desktop-release-template.yml` hard-fails at its S0 block step;
    - attestation;
    - the packaged Agent SDK proof, which cannot pass on an A2 package.
- **Undocumented commands (IMPLEMENTED_UNDOCUMENTED, noted but given no row).** These shipped commands are absent
  from the §4 map:
  - `desktop:prepare`
  - `runtime:build`
  - `instruction-root:prepare`
  - `desktop:verify-dependencies`
  - `desktop:verify-codex-pin`
  - `electron:supply-chain`
  - `verify:version-identity`
  - `sbom:generate`
  - `notices:generate`
  - `proof:packaged-security`
  - `harness:validate:contract-deps`
  - `harness:validate:agentsdk-mcp-probe`
  - The split rule allows sub-rows only for table rows, so this is recorded here for the manager.

## 5. Method friction

- **Omissions have no row type.** The split rule has no row type for "section omits shipped behaviour". A
  `STATE-n` key is reserved for state assertions. Proposal: allow `DOC:<ID>#<n>.U` (undocumented) rows, or say
  that such findings go to notes only.
- **Section prose has no key.** Section prose outside a numbered list or table has no keyed home once the table
  is split. I used extra `.n` rows (`#4.15`, `#4.16`, `#9.7`) and said so in Notes.
- **"Did the process run" versus "is the text accurate".** For process sections these are different questions.
  The Disposition vocabulary has no process-not-run verdict, so I used UNKNOWN or ALIGNED plus the brief's
  `RELEASE_PROCESS_NOT_RUN:` token.

## 6. Effort

- About 25 files read in ranges:
  - the three docs;
  - `package.json`;
  - 8 scripts;
  - 4 electron files, by grep;
  - 2 workflows;
  - 7 AgentRuns records;
  - the register;
  - the D-APP-127 record;
  - the BUILD and ELECTRON capability files and notes.
- Git was used read-only, with `log -S` and `show` against the frozen tree.
- The context budget was comfortable.
