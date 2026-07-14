# Retained manifest-refresh attempt 2

- Stage: terminal manifest refresh after all member work passed.
- Result: failed closed; the command was interrupted after repeated command-resolution errors.
- Finding class: execution substrate / shell environment.
- Reason code: `ZSH_PATH_SPECIAL_PARAMETER_COLLISION`.
- Cause: a direct zsh loop used `path` as its iterator, which replaced zsh's command-search path.
- Remediation: regenerate and verify the manifest in Bash using a non-special iterator name.
- Candidate or project effect: none; only the self-excluding manifest was partially rewritten and is regenerated from durable bytes.
