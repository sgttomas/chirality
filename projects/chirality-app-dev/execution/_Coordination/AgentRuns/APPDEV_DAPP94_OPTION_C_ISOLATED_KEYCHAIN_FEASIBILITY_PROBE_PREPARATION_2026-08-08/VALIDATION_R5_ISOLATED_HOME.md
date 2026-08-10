# D-APP-94 Option C R5 isolated-HOME static validation

Status: `PASS_STATIC_PRE_FREEZE`

- bounded R4 intake: 22 byte-identical raw objects, manifest SHA-256
  `962aa7135fcda412169e9477e5c57da517bd2dcf383084d2d7f24691646a5bf7`;
- predecessor disposition SHA-256:
  `2f4b3e4f666443c1e5f9c370279fc8e6ae2ba538476296ed611acfc8ea134d1e`;
- R5 driver SHA-256:
  `5f7cf2830679a0fb07ff26f6b7642d4d133347512af337cdcabffdc2b8a23d4a`;
- `/bin/zsh -n prepared/run-dapp94-option-c-probe-r5.zsh`: PASS;
- R5 root and `returned_r5/`: absent; retained R4 root/evidence and current
  `returned/`: present and untouched;
- isolated security operations: initial/bound default/search, create, unlock,
  bind, and delete each visibly use exact env-clean isolated HOME;
- plain owner-domain operations: raw pre/post observations plus mismatch-gated
  backstop only; rc error or cmp error records no proven drift and performs no
  owner write;
- failure/signal route: single owner guard, signals ignored before entry,
  MATCH performs no write, terminal error/backstop state blocks retry, all R5
  state retained;
- success cleanup: owner MATCH and backstop NOT_NEEDED, evidence copy/hash,
  state recheck, isolated-HOME delete only, isolated absence, R5-root removal;
- probe/material/scope boundaries remain bare Electron 43.2.0, public constant,
  public empty password mechanics, no GUI window/product/package/trace/network/
  credential/reliance/Git/Task-Management/foreign-loop authority.

No security/keychain command, Electron/process/runtime/GUI action, deletion,
move, overwrite, product/package/trace action, credential/network operation,
Git, Task Management, or other execution action occurred during preparation.
