# Fresh Re-review — N1 D-GOV-35 Packet, Cycle 2

Verdict: `FAIL — ONE ACTIONABLE FINDING`

Review basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`

Subject: repaired N1 proposal packet plus N1 `RETURN.md` and `STATUS.json`

This is fresh read-only review evidence. It is not owner acceptance, adoption
of D-GOV-35, or authority to apply the proposed instruction delta.

## Finding

### 1. MEDIUM — The downstream pin/mirror inventory still omits the tracked Chirality App public-export derivative

The repaired App/Piping inventory correctly adds every exact-hash surface
under `projects/chirality-app-dev/` and `projects/chirality-piping/` identified
by the prior review. A repository-wide exact search, however, finds one further
Chirality App downstream pin that `IMPACT.md` does not classify:

- `exports/chirality-app/export-manifest.csv` records `AGENTS.md`, size
  `17355`, at SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`.
- `exports/chirality-app/export-report.md` identifies the projection as the
  `chirality-app` release projection and records one top-level `AGENTS.md`.
- `exports/chirality-app/README.md` states that this profile builds the curated
  `chirality-app` desktop release repository and that its tracked manifest and
  report are regenerated through `export_public.py`.
- Root `execution/_Coordination/HANDOFF_STATE.md` expressly classifies the
  public export under `exports/chirality-app/` as a stale derivative deferred
  to the next export release. It is therefore neither an immutable historical
  evidence file nor an App-loop authority surface; it is a Root-owned tracked
  downstream projection that must be regenerated or explicitly deferred when
  an authorized application changes live `AGENTS.md`.

Although this surface is outside `projects/chirality-app-dev/`, it is a
SHA-pinned Chirality App projection of the exact file proposed for amendment.
The owner required the downstream pinned/mirrored inventory, and the packet's
closure language presently omits this known derivative and its follow-on.

Bounded repair: add the exact public-export manifest path to `IMPACT.md`,
classify it as a Root-owned mutable/stale derivative rather than App authority
or immutable evidence, name `exports/chirality-app/export_public.py` as its
governing regeneration profile, and require the later authorized application
handoff to regenerate it through its owning workflow or record explicit
deferral. Do not regenerate or edit the export in N1. Recompute packet and
return hashes and submit the repaired packet to another fresh review.

## Prior findings disposition

1. **Zero-context/default-apply conflict: CLOSED under amendment N1 version
   2.** The literal default `git apply --check` passes. The four hunks use only
   in-section adjacent anchors, do not claim conventional `-U0`, and reduce the
   delta to 23 additions and 5 deletions. Removing an additional anchor from
   the final hunk makes default Git reject the patch, confirming the recorded
   compatibility boundary.
2. **Downstream inventory: PARTIALLY CLOSED.** Every previously named omitted
   App/Piping project path is now exact and correctly calibrated, including
   the login-proof evidence and both historical process-input maps. The public
   export finding above remains.
3. **Code-behavior calibration: CLOSED.** Both the proposal and `IMPACT.md`
   now state only that lines 205–213 deny untyped/generalist delegation
   requests reaching the existing governance gate. They leave native-class
   integration to App WP-06 and preserve the path, line range, exact hash, and
   no-Root-code-write boundary.

## Mechanical and semantic checks that passed

- `HEAD` is the accepted basis
  `6b0c5219b6a2653e2fc491b1d998abcf78fcf776`, and it resolves as a commit.
- Live `AGENTS.md` is unchanged at SHA-256
  `268becd0bac9da8421b30089e4e4167a5e5f79bf3892d0f72ad41a63180a3aeb`;
  `git diff -- AGENTS.md` is empty.
- Literal `git apply --check` passes; `git apply --numstat` reports `23`
  additions and `5` deletions.
- `validate_agent_instructions.py` passes: 34 files, 0 errors, 0 warnings.
- `validate_instruction_entrypoints.py` passes.
- Global `validate_candidate_whitespace.py --base-ref origin/main` passes,
  including the formerly blocking N2 EOF condition.
- Packet exact hashes reproduce:
  - `D-GOV-35.proposed.md`:
    `924c1b098f1510bca9189e1ac06e4c2fd8e9d358a9fc3c4e42fdd04a53b69c88`;
  - `AGENTS.proposed.patch`:
    `4455adda4199be5493e1f8d2171ebb4641f40666c35cf09e90adc935ff6355ee`;
  - `IMPACT.md`:
    `7d1afa8b4c0e8b57a925b98e8d226fce38f11987cffa82d70feee5ce1940aa4f`;
  - exact `README.md`:
    `0723e118931e45937380f34cba2d80c7326096128257f0c6fcb41d1cca9ed544`;
  - normalized README self-hash:
    `a6234e8eccb2184287b1bd602ff5bd3e2c5d0b0f3d0a6fd80bbe91626bab2d5c`.
- The G0 A3 owner quotation matches after Markdown line-wrap whitespace
  normalization.
- The cited App code hash reproduces as
  `2b2d750be8fb3974593599631f64f920bc3b3fd4512640545bf1a22e61ec215c`.
- The proposal still contains every required substantive ruling clause:
  second executable class; sole Chirality-managed path preservation; untyped
  primary entry; no automatic native-descendant Agent 2 classification;
  Codex Agent 0/1/2 role-entry parity; exact labels; calibrated K-SUBAGENT
  claim; TM-ROOT-126 concordance; required App authority/SOW/code surfaces;
  owner-ruling gate; and hold/non-effect boundaries.
- N1 content remains confined to the declared proposal folder, with only its
  declared N1 control-plane return/status records outside that folder. No live
  instruction, standard, App/Piping subject, lifecycle, pointer, hold, pin,
  implementation, release, publication, or merge surface was changed by N1.

N1 remains `PROPOSED — AWAITING OWNER RULING`. The packet is not ready for
HELP_HUMAN fan-in until the bounded inventory repair and a fresh independent
review pass.
