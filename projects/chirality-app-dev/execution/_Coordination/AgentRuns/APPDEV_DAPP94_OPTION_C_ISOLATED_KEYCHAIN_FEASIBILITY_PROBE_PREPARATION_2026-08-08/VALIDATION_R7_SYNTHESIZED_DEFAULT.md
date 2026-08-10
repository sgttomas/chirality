# R7 static validation

Status: `PASS_STATIC_PRE_FREEZE`

- intake `ff99492074fd0e7e7ca8005f1bceb57c8d1b11b2f2a8b9894d3b27df264bc27e`;
- driver `091b77160a127f371266fa08e440e9c39ec4be0123766da7f0284256cfff8edd`; `/bin/zsh -n` PASS;
- R7 root/returned absent; R5 root/returned present and untouched;
- keychain basename exactly `login.keychain-db`; zero `-s "$PROBE_KEYCHAIN"` bind writes;
- create/unlock then isolated default/search observations and exact one-element comparison;
- host/session hypothesis only; all R6 owner/backstop/probe/prompt/commit/cleanup/scope semantics preserved;
- no operational command executed.
