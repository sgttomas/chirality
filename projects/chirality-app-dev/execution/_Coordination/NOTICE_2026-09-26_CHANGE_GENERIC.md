# Generic change workflow

Owner-authorized Root tranche `ROOT-CHANGE-GENERIC-20260926` narrows the bundled `change` workflow into a repository-agnostic Git method. The App bundles this workflow for all users and excludes the project-scoped `chirality-change` skill, so App users in other repositories no longer receive `sgttomas/chirality` rules.

The workflow now:
- inspects state and ownership, isolates the change proportionately (shared checkout for disjoint scopes; branch or worktree lanes when asked or warranted, with overlap warnings), runs the repository's registered checks, reviews the diff, and produces the State Report and optional `{EXECUTION_ROOT}/_Change/` session log;
- grants no Git authority: without authorization the user or the repository's instructions actually give, it does not push, open or update a pull request, or merge, and states that assumption;
- names how repository conventions (a project `AGENTS.md`, a project-scoped change skill, contributor documentation, required CI) specialize its defaults without weakening its invariants;
- drops the `codex/` branch-prefix default (no prefix by default) and uses the repository's default branch as integration branch;
- renames the concurrency class `SHARED_MONOREPO` to `SHARED_CHECKOUT`.

The Chirality-specific rules it carried (standing Git grant and its merge conditions, `codex/` prefix, no-fast-forward PR integration, high-risk overlap paths, grant limits and destructive-action exclusions) now live in `.agents/skills/chirality-change/SKILL.md`, which this loop's instructions already name for Git closeout. The standing grant itself is unchanged.

Historical run records are not rewritten. This loop decides its own adoption; this source tranche grants no release.
