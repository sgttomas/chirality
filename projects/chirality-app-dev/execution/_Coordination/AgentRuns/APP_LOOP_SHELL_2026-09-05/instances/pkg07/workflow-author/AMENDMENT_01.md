# Brief amendment 01 — native instruction-root binding

The dispatched TASK reads its instruction package at REPO_ROOT, resolved by git rev-parse --show-toplevel. For this native descendant execution set CHIRALITY_INSTRUCTION_ROOT to that resolved repository root for TASK instruction hydration. This is the manager-declared instruction root, not a product environment configuration change. No write fence, objective, check, or authority expansion. This explicit runtime binding supplements LAUNCH_BRIEF.md and resolves the missing shell variable; all instruction files remain read-only.
