# PKG-12 Initial Verifier Disposition

Status: `TERMINAL BLOCKED — EXCLUDED FROM ACCEPTED FAN-IN`

The sole initial `VERIFY-B1` stopped before semantic verification after its
path-discovery command emitted author-owned `AUTHOR-B1/CANDIDATE_MANIFEST.tsv`,
outside the original sealed independence read scope. The exact command and
incident are retained in `children/VERIFY-B1/INDEPENDENCE_INCIDENT.md`.

Parent validation confirms terminality and containment:

- `STATUS.json`: `6edf2dd9825ab87e950b631eedd01228b684a41cce4d8402df09b47f5bfa610e`
- `RETURN.md`: `18307f4cc62dc58cef818ced5afcb7332a41cbb94b6b6f6cc7496162aaa4cd85`
- self-excluding `MANIFEST.tsv` (10 valid entries):
  `1de677a9ce2b68523fc7c2c46084638da9a1c562a20fb96654eb3043b4f79ba7`
- candidate manifest remains 15/15 and matches frozen SHA-256
  `404a7031a720d2d05a46d8ddd1fc518294422c4693c7446729eafb5470cbe976`
- all 45/45 live bindings remain matched; live-project worktree and index
  diffs are empty; candidate and project writes are zero.

Amendment `amendments/WORKING-P3-PKG12/BRIEF_V2.md` authorizes exactly one
fresh replacement `VERIFY-B1-R1`. The initial verifier remains visible but is
not accepted evidence for the verifier gate.
