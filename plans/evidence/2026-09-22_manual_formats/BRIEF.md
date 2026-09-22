# Management manual v2 formats and guide styling

Date: 2026-09-22. Primary: HELP_HUMAN `/root`. Git integration owner:
WORKING_ITEMS `/root/closeout_manager`. Basis:
`e74feb34b7ca99ebeb903ffb52f7fdd2b3efd169` (freshly fetched `origin/main`).
Branch: `codex/management-manual-v2-formats-20260922`.

## Owner direction and interpretation

Ryan Tufts, active chat on 2026-09-22, verbatim as supplied by the primary:

> Make new DOCX and PDF formats of the management manual v2, using the same style as previous. Make the HTML to resemble it (matching exactly is not necessary).

The primary stated the interpretation to the user: create DOCX/PDF editions
from the revised management-manual Markdown using the supplied v1 styling,
and restyle the existing agent-guide HTML to resemble that style. Preserve
all Markdown publication content and all v1 originals. This continuation
does not reopen the completed editorial review, amend live instructions,
adopt a workflow, change project state, or establish governed acceptance.

## Write boundary and ownership

Authorized output scope:

- `docs/alignment-manual/Project_Management_for_Human_Agent_Teams_Consolidated_v2.docx`
  and the matching `.pdf`.
- Supporting renderer code needed for those formats under
  `docs/alignment-manual/`.
- `docs/alignment-manual/render_manual.py` and generated
  `CHIRALITY_AGENT_USER_MANUAL_v1.html` for presentation changes only.
- `docs/alignment-manual/README.md` for format links and accurate maintenance
  instructions; `requirements.txt` only if a genuine dependency change is
  needed.
- This run-evidence directory and
  `docs/governance_harness/tranche_manifests/ROOT-MANUAL-FORMATS-20260922.yaml`.

The Markdown manuscripts and agent-guide content are frozen inputs. Earlier
reading/review evidence remains immutable. Temporary QA products belong
outside the submission or in an ignored location. No root README change,
project-file change, new publication prose, live pointer update, or instruction
amendment is included in this scope. G4 still applies to the protected
`docs/**` paths; its manifest records scope and grants no authority.

The closeout manager fetched origin, verified a clean index/worktree, and
created this branch from current main in the existing isolated worktree
before authoring began. The root was notified that the branch was ready.
Native agents share broad host filesystem/network permissions; assignments
and role boundaries are instruction-based, not per-agent mechanical fences.
The closeout manager performs no staging, commit or push until the root
signals content and visual readiness. Standing owner Git authorization then
permits ordinary PR closeout with actual-candidate review and required CI.

## Verification and return

Record source/style identities and reproducible generation commands. Verify
the original and Markdown hashes, output completeness, real figures and links,
HTML/source parity, deterministic or explained rendering behavior, and
independent review of the final artifacts and renderer changes. Use the
bundled LibreOffice/Poppler document path for full visual DOCX/PDF QA.
The earlier browser file-URL security restriction remains; no alternate
browser route is authorized. Report actual visual coverage and any limit
without treating structural checks as visual proof.

Run affected repository checks and complete-range G4/conflict checks before
PR closeout. Verify required CI and source HEAD before merge. Automatically
selected non-required product coverage is additional evidence, not a new
merge gate for this documentation slice; investigate any material failure.
Preserve the independent review, check results, source revision and merge in
ordinary PR/Git history. Return artifact paths, PR/merge identity, validation
results and remaining limits to the root.
