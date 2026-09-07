# Independent final review — self-current SCA-002 ledger repair

Verdict: **PASS_DECISION_READY_METADATA_REPAIR**.

The author-v6 candidate is complete, exact, mechanically applicable, self-current after application, and ready for the limited owner decision. Its identities are:

- author manifest: `author-v6-ledger-repair/MANIFEST.json`, SHA256 `f98e20e7db16bcabfeed39329b1c65241bebd4171a7be1f75f5dc1b300d19f59`
- one-file patch: `author-v6-ledger-repair/CANDIDATE.patch`, SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855`
- complete postimage: `author-v6-ledger-repair/POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`, SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`
- current canonical preimage: `projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv`, SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`

Every author manifest member and byte count verifies. The patch applies cleanly, passes strict whitespace validation, and has numstat 1/1. Canonical and postimage CSVs each contain one row and 14 fields. Only `DecisionRef` and `Notes` change; all other fields, including `CandidateState = GATE3_REVIEW_NOT_ACCEPTED`, remain byte-identical.

The correction is self-current. The first SCA-002 postapplication audit dated 2026-09-07 is described as a historical blocker on the then-current ledger metadata. The exact ledger state records resolution of that metadata inconsistency. The changed fields contain no repair-pending, Gate-5-blocked-pending-repair, or proposed/candidate self-label. A fresh independent audit rerun and separate Gate 5 owner acceptance remain future acts. The unchanged `PROPOSED-origin` SourceRef and CandidateState are explicitly historical strata and do not describe the current repair state.

The external owner evidence verifies exactly at the cited absolute aed8 paths: `DECISIONS.md` SHA256 `ff389e47a48386aeabe344496acf509386301aa0b72868a690ba5b4190bfe67c` and `MANIFEST_v2.json` SHA256 `f4fcbe92c15c3a9803f6835dfa1d9dc1563101ec3a6e7308b251b0570c314872`. It records `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` as owner-accepted contract basis. The candidate keeps that contract choice distinct from unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance, recovery/lifecycle, protected-fixture, hold, hosted-readiness, and release gates.

SCA-001 and SCA-002 states remain correctly separated, including completed SCA-001 Stages 1–2, pending SCA-001 publication/adoption, completed SCA-002 Gates 2–4 and canonical application, and pending future SCA-002 SOW propagation. The candidate conserves one SOW, seven carriers, four objectives, 66 requirements, nine holds plus R16-B, applicable full-wire/source gates, historical SOW basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1, project authorization, security/exclusion boundaries, and no activation or effect overclaim.

Exact limited approval wording: “Approve one exact Runtime ledger metadata application: apply `author-v6-ledger-repair/CANDIDATE.patch` SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855` to canonical ledger preimage SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`, producing postimage SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`; authorize the owning immutable repair snapshot and permitted `_ScopeChange/_LATEST.md` pointer update; then run a fresh independent `AUDIT_DECOMP`. This is not a repeat semantic or contract vote and grants no Git, publication, Root adoption, SOW, source, supplier, lifecycle, activation, hosted-readiness, protected-fixture, hold, or release authority. Gate 5 owner acceptance remains separate after a clean audit.”

This PASS is review evidence only and authorizes no application or later act. Role and nondelegation: independent ephemeral Agent 2 reviewer under Runtime SCOPE_CHANGE; instruction-asserted; no delegation performed.
