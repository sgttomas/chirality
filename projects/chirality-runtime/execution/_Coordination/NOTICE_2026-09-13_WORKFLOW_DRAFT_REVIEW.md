# Workflow draft review

Owner-directed Day 1 maintenance adds a reviewable draft before registering a new workflow. The core `workflows/create-workflow/WORKFLOW.md` and App default `instructions/AGENTS.md` now direct new packages into `.chirality/workflow-drafts/<name>/`. The App shows instructions and included resources, prepares feedback in chat, and registers only the reviewed bytes through an explicit user action. Existing registered names are preserved, and changed drafts require renewed review.

Runtime canonical parsing is reused; `.chirality/workflows` remains the execution library. No role, permission, supplier or account boundary changes. Existing accepted packages and historical instruction snapshots remain untouched. Future packaging consumes the revised shared workflow and App default; user-edited copies remain under their existing preservation policy. This source tranche grants no release.
