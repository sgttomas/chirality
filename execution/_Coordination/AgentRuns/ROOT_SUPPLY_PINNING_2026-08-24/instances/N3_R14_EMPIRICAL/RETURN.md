# Return — N3 R14-Amended Empirical Evidence

- **Status:** `PASS_WITH_ADMITTED_DENIED_EGRESS_AND_DOCUMENTED_GAPS`
- **Basis:** `5cb493a09bf336593d2ed7412cfdabdcbc4e09a1`
- **Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`
- **Exact app server:** SHA-256
  `b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2`;
  observed version `0.149.0`.
- **Ancillary executed:** `codex-code-mode-host` SHA-256
  `8f9f6969cd5e69540482d58791f72e4e9b9888e576ae3ad446c422a058b70128`,
  help inventory only. Frozen `rg` and `zsh` were not relevant and not run.
- **Containment:** every vendor invocation passed an executable/profile hash
  gate and explicit sandbox-denial preflight; no connection completed, no
  credential prompt/login/device flow occurred, no approval was granted, and
  no write escaped disposable state.
- **Admitted denied egress:** featured plugin cache at
  `https://chatgpt.com/backend-api/plugins/featured?platform=codex`, curated
  GitHub sync at `https://api.github.com/repos/openai/plugins`, and curated
  export fallback at
  `https://chatgpt.com/backend-api/plugins/export/curated`.
- **Plugin switch:** `features.plugins`; runtime default/current readback
  `true`, explicit readback `false`; false eliminated all observed plugin
  startup attempts. This is the whole-plugin feature, not a curated-only
  switch.
- **Config/precedence:** complete effective readback; unmanaged requirements
  `null`; untrusted project layer disabled; session flags override the user
  layer; `multi_agent_v2` exact-pin behavior established.
- **Feature inventory:** complete 118 entries across two pages with stage,
  current state, and default state.
- **Precise gaps:** generated JSON schema, generated TypeScript types, and the
  resulting exhaustive schema-derived method inventory are
  `UNAVAILABLE_UNDER_BOUNDS`; neither authorized package entrypoint exposes
  the documented wrapper commands.
- **Teardown:** disposable state, both current quarantines, all artifact bytes,
  and temporary static extracts deleted; exact absence verified.
- **N4 gate:** `RELEASED_WITH_DOCUMENTED_GAPS`; N4 must carry every denied
  destination, the `features.plugins` result, schema/type/method gaps, and the
  R13-B G5 signature finding without claiming G2 acceptance.

Key evidence identities are pinned by candidate
`03_EMPIRICAL_EVIDENCE/ARTIFACT_HASHES.csv` (SHA-256
`66453d9bfb62cb61edf10387ac11c76214209ab9d48e8907b0c39f49dd0a43a0`).
No G2 acceptance, pin amendment, implementation, cutover, release,
publication, or reliance claim is made.
