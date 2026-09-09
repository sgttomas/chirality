---
name: chirality-change
description: Prepare, review, or close out Git changes in the Chirality repository using its branch, evidence, merge, authority-state, and downstream-notice conventions. Use only for Chirality project work, not general Git tasks or other repositories.
---

# Chirality Change

Apply these project conventions while using ordinary Git judgment and the authorization already present in the session:

- Treat `main` as Chirality's integration branch. Name task branches with the `codex/` prefix unless the user or an applicable owning-loop rule specifies otherwise.
- Preserve unrelated work. Retain exact evidence for the source, branch, commit, and completed check verdicts needed to review or close out the change.
- Use a separate worktree when the user requests isolation or when shared-monorepo risk makes isolation proportionate, such as overlapping writes to governance surfaces, risky refactors, or tool interference. Do not require a worktree for every change.
- Close project work through a human-gated pull request by default. An owner may direct merge execution under the applicable owning-loop rules; any stricter local merge discipline remains controlling until that loop adopts or acknowledges the shared policy. For merge-policy questions, consult [`docs/PRD_ROOT.md` §5.3.1](../../../docs/PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor).
- Keep governed acceptance, independent review, Git integration or publication, and product release as distinct states. A branch, commit, push, pull request, or merge does not itself accept governed truth or authorize release.
- When changed surfaces are pinned or mirrored by affected project loops, identify those loops and route a coordination notice describing the change and remaining adoption work. The receiving loop decides whether to adopt, amend, or decline it; the notice does not change downstream authority.

Do not invent approval-token syntax, add fresh approval gates, or infer authority beyond the user's request and the applicable owning-loop rules.
