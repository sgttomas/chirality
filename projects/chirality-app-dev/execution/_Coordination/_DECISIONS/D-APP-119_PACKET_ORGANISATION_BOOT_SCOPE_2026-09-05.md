# D-APP-119 — organisation-layer common boot scope

Status: PROPOSAL — AWAITING_RULING
Owner: Ryan Tufts
Prepared: 2026-09-05 by WORKING_ITEMS pkg07 for HELP_HUMAN

## Decision requested

Choose whether to authorize the exact App boot caller addition and explicit local pin configuration below for DEL-07-01-V3-01, or defer implementation. The pending asynchronous question presented by HELP_HUMAN has no response at preparation; it is a pending question, not owner direction or a ruling.

## Accepted scope and observed limitation

DEL-07-01 live Remaining requires organisation-layer protection and SHA-256-per-asset pin verification at boot (SOW-084; controlling ScopeOfWork SCA-APP-010 section, decomposition at dbd812a52d5ed0cb3ed173f3aaaa68703a914291). Existing item loci name App harness instruction-root/path-policy helpers, fixtures/tests, and electron/daemon-instruction-root.ts if daemon-boundary enforcement is needed. They do not name electron/main.ts.

Read-only execution trace: initializeDaemon in main.ts calls the named resolver only for packaged boot. Development boot sets CHIRALITY_INSTRUCTION_ROOT directly. Both paths then start the runtime. Verification confined to the allowed resolver misses development boot; ordinary App readability helpers do not prove this live common boot path. Accepted return is not waived. Selection/preflight succeeded but implementation is held at this scope fork.

## Frozen reviewable candidate

Run-relative base: execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg07/boundary-proposal/.

- MAIN_BOOT_SEAM_CANDIDATE.diff SHA-256 `691c8bf1ba623207e4d9aab554a49bd58bb20c58704903f396a69e4bc71ee814`.
- PROPOSAL.md SHA-256 `40faeb6ad49f5277f3cdddf63917acc6ea0e77bff8dd663cb88dff1e9a055daa`.
- SOURCE_IDENTITIES.sha256 binds the original main.ts; PATCH_CHECK.json records git apply --check exit0. Candidate files are proposals, not adopted requirements.

Exact additional product write locus: `frontend/electron/main.ts`, solely the attached import of assertDaemonOrganisationLayerReady and awaited call after both instruction-root-resolution branches and before startRuntimeHost. No Root-owned path is added. Implementation of that export remains in already-listed `frontend/electron/daemon-instruction-root.ts`; verifier and path-policy integration remain within the accepted App harness helper/test loci. No other main.ts behavior may change under this decision.

## Options

### A — Approve exact App seam and local pin configuration

Authorize the exact additional main.ts seam plus the following explicit implementation configuration within the existing DEL-07-01 App helper/boot scope:

- CHIRALITY_ORGANISATION_ROOT is an absolute local directory; CHIRALITY_ORGANISATION_PINS_SHA256 is the expected 64-lowercase-hex SHA256 of manifest bytes. Both absent keeps existing bundled-only behavior. Partial, empty, malformed or relative configuration fails closed.
- Fixed `<organisationRoot>/organisation-pins.json`: exact schema `chirality-organisation-pins/v1`, with `assets` a nonempty sorted unique list of objects containing only relative POSIX `path` and lowercase-hex `sha256`. Manifest identity is checked against explicitly configured expected digest; manifest does not authenticate itself.
- Verify all inventoried regular assets and reject unlisted assets, malformed/extra fields, duplicates, traversal, absolute paths, symlinks, special/missing/unreadable files or digest mismatch. Manifest itself is excluded from asset inventory. Canonical organisation root is separate in both directions from working root and bundled base. No verifier writes or automatic repinning.
- No-config check returns without new project-registration requirement. Configured boot resolves the registered working root and verifies separation/pins before runtime starts. Unavailable registration or integrity failure propagates outside fallback catch, never silently selecting bundled fallback. App readability/path-policy integration proves its own working-root, write and proposal-path denials with fixtures.

Recommendation: A for this narrow caller gap, provided the owner intends the specified local configuration carrier. It enables a testable App boot return without implying Root-wide coverage.

### B — Defer

Keep the accepted item and its full return unchanged. No organisation implementation is dispatched. Retain the concrete candidate and live blocker; revisit scope/configuration later. Independent B workflow-contract implementation is unaffected.

## Tests and evidence

Fixtures: absent/partial/malformed configuration; manifest and asset digest changes; full inventory, traversal/symlink and special-file rejection; canonical root overlap; both-layer App write/root/proposal-path denials; packaged and development boot verification before runtime invocation; configured failure cannot fall back. Pin bytes and source identities, canonical outputs, command/environment/version/exit records and recomputable manifests required. Packaging checks remain DEL-08-01, composition remains DEL-04-04.

Fresh read-only TASK software-code-review over100percent frozen diff must PASS with actionable findings repaired/re-reviewed. Run actual registered frontend tests/typecheck/build/premerge and harness gates; A1 re-stage consequence applies. Missing runtime-binding disposition follows current AGENTS; no test/release PASS is inferred here. Parent freezes exact author/test loci and preserves existing policy invariants before dispatch.

## Explicit boundaries

No Root runtime schema/tool/CLI-wide organisation enforcement is authorized or claimed. Root ProjectRegistry currently returns only workingRoot/instructionRoot; a Root-wide protection claim requires a separately owned integration decision. No packaging/composition completion, provider/network expansion, release/distribution, lifecycle/Checking Approval SHA change, authority-truth mutation, or waived acceptance criterion follows from A. This packet grants no implementation by its existence.

## On-ruling mechanism

The owner must rule A or B through the existing governed decision path. Record actual owner words/evidence separately; never turn the unanswered async question into a ruling. Parent updates the register only after an actual act. LOOP_INIT Step1 requires the owner act observable on origin/main after fetch before implementation reliance; in-session approval alone is not presumed sufficient for a new scope gate. After observable A: recheck pinned patch/current source, APP-HOLD and exact scope; parent freezes amended implementation brief, dispatches bounded author and fresh review, verifies actual gates and deliverable state. Drift or additional loci return to owner/parent rather than silently widening A. After B: preserve held item and candidate without author dispatch.

Attribution: OpenAI GPT-6 per runtime context, exact serving ID unavailable; WORKING_ITEMS pkg07 instruction-asserted native role. Derivative proposal cites live accepted scope and frozen candidate; no ruling, acceptance, pointer movement or implementation act.
