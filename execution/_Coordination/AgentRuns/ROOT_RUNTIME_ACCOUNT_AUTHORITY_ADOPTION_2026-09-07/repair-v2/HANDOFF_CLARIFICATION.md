# Handoff clarification — review-v1 P1 repaired

Review v1 correctly found that the baseline fast path checked absence of the custody supplement but omitted the account-control supplement. The live helper now requires both exact supplement paths to be absent before returning `migration-baseline`. Its existing `safe_path` traversal and symlink checks are retained, while explicit path existence prevents file, directory or dangling-symlink forms from being treated as absence.

The policy and all Runtime evidence remain unchanged. Exact accepted current state still resolves three ordered adoptions as pending publication with no execution authority. Original author and review-v1 evidence are immutable; this directory and the root-level v2 freeze files are the append-only repair evidence. Fresh independent review remains required before publication.
