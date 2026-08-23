# R19 executor preconditions

- Checked: `2026-08-23`
- HEAD: `d6861ae8251e2a81078577d4496e949735ff199d`
- Branch: `codex/app-login-proof-r19-staging`
- Frontend tree: `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`
- `origin/main`: `8635e40995b05f494ae35c6083dabdd50068bb52` (newer; deliberately not synchronized)
- Tracked worktree diff: empty
- Index: empty
- Git operation heads: absent
- Only initial porcelain entry: the manager-created R19 run root
- Exact proof root, plist, and public destination: absent and non-symlinks
- Exact service check: exit `113`

Exact service output:

```text
Bad request.
Could not find service "com.chirality.ci.runatload.login.owner.macos26.r19.3951dfe9-ec03-421b-b376-fd5f0d96992b" in domain for user gui: 501
```

No default operator surface was queried.
