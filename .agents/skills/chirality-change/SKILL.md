---
name: chirality-change
description: Prepare, review, or close out Git changes in the Chirality repository using its branch, evidence, merge, authority-state, and downstream-notice conventions. Use only for Chirality project work, not general Git tasks or other repositories.
---

# Chirality Change

Apply these project conventions while using ordinary Git judgment and the authorization already present in the session:

- Treat `main` as Chirality's integration branch. Name task branches with the `codex/` prefix unless the user or an applicable owning-loop rule specifies otherwise.
- Preserve unrelated work and accepted historical evidence. For ordinary changes, use the Git diff/commit and one concise review or PR record identifying the checked revision, results, and remaining limits. Create additional snapshots or receipts only when an applicable instrument or a concrete recovery need requires them; do not duplicate Git history in chains of source copies, hash manifests, and closeout reports.
- Use a separate worktree when the user requests isolation or when shared-monorepo risk makes isolation proportionate, such as overlapping writes to governance surfaces, risky refactors, or tool interference. Do not require a worktree for every change.
- Close project work through a human-gated pull request by default. An owner may direct merge execution under the applicable owning-loop rules; any stricter local merge discipline remains controlling until that loop adopts or acknowledges the shared policy. For merge-policy questions, consult [`docs/PRD_ROOT.md` §5.3.1](../../../docs/PRD_ROOT.md#531-merge-gate-policy--the-d-8-successor).
- Keep governed acceptance, independent review, Git integration or publication, and product release as distinct states. A branch, commit, push, pull request, or merge does not itself accept governed truth or authorize release.
- When changed surfaces are pinned or mirrored by affected project loops, identify those loops and route a coordination notice describing the change and remaining adoption work. The receiving loop decides whether to adopt, amend, or decline it; the notice does not change downstream authority.

For implementation and closeout in this monorepo:

- Separate maintained source and test fixtures from run evidence. Permanent tests and public packaging should not depend on a dated agent-run directory. Keep useful regression cases in the maintained test suite; preserve one-time migration evidence as history rather than requiring the migration to be re-proved forever.
- Keep working summaries revisable until a real review or acceptance boundary. Format authored documents and generate derived files before binding their bytes for review. Preserve raw tool output verbatim when needed; do not make it an editable, style-normalized source artifact. A later correction needs evidence for the affected change, not another full copy of the previous packet.
- Judge a check by the failure it prevents. Keep behavioral, permission, containment, compatibility, and reproducibility checks. Remove obsolete migration assertions, incidental wording/order assertions, and duplicate evidence checks when they protect no current requirement. When a governing instrument requires such a check, propose the corresponding amendment rather than silently bypassing it or adding another workaround.
- For changes crossing App, Runtime, or provider adapters, validate the actual connecting path early. Separate component passes do not establish integration. Check the deliverable from committed or explicitly selected files, including its maintained fixtures and resources; untracked local evidence must not supply a hidden dependency.
- Match preflight to the actual candidate and affected CI entrypoints. Scope candidate checks to files being submitted, and run required range checks against the complete PR diff. If a repair changes a protected CI or instruction path, update the candidate's tranche declaration before rerunning. Re-run affected checks after repairs; repeat broader suites only when the change or an unresolved concern warrants it.

Do not invent approval-token syntax, add fresh approval gates, or infer authority beyond the user's request and the applicable owning-loop rules.
