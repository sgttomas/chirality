# Runtime PRD: D-GOV-43 revision (2026-09-12)

This file carries the revision that would otherwise sit at the top of `docs/PRD.md`.

Root D-GOV-43 (ruled 2026-09-11) with its topology A2 supplement (recorded
2026-09-12) re-platforms the Runtime as an application-owned service hosting
stock Codex. Applied in this loop by the SCA-004 hold-closure packet in this directory under
ruling item 11's bounded coordinated authority. The statements of `docs/PRD.md` are read with this revision; `docs/PRD.md` itself is unchanged because the Root effective governance state of 2026-09-06 pins its bytes (ruling item 11: historical records are read with D-GOV-43, not rewritten).

- The seven-carrier partition is revised. DEL-02-07 (process supervisor and
  purpose-limited control), DEL-02-08 (exact supply and protocol pinning),
  DEL-02-09 (hosted account and consent boundary), DEL-02-10 (closed event
  schema and approval API v2), DEL-02-11 (worker retirement, restart and
  terminal reconciliation) and DEL-02-12 (conformance evidence and shared
  release fan-in) are RETIRED: families 1 and 2 of the purpose test retire,
  family 3's purpose is adapted into the App's effective Codex home. Their
  full IDs, executed records and history are preserved; nothing is re-created
  under another name. DEL-02-06 (stewardship and release assurance) is
  retained with its supplier snapshot, lease and version-mismatch refusal
  clauses revised; stewardship of the lockfile pin remains.
- Retained services: `RuntimeService`, the session store, the turn
  coordinator, `DelegatedRuntime`, `CodexSupervisor`, `CodexLogin`, the
  Unix-socket API with application-private client tokens, the client, the CLI
  and the PEC integration opportunity (compatibility unverified, not an MVP
  prerequisite).
- "Supervisor/daemon" ownership language reads as the application-owned
  Runtime service that the App starts, owns and stops; the App is the only
  production consumer. D-GOV-20 boundaries are read as amended by D-GOV-43;
  the residency boundary is retired; D-GOV-36's daemon custody exception is
  superseded on the App path by Codex's own account methods in the effective
  home.
- The nine `HELD_UNAVAILABLE` bindings in `HOLD_SUCCESSOR_MAP.csv` are closed
  by SCA-004; they are not re-seated or mapped onto the spike checks. Release
  readiness is established by ordinary checks (lockfile-pinned dependency,
  bundle signature and notarization, spike acceptance evidence, independent
  source review) and the three retained human decisions.
- The Gate3 payload hash index in `docs/PRD_AUTHORITY.md` remains the identity
  record of the accepted 2026-09-05 subject; the two loop-owned files amended by
  SCA-004 are re-hashed there once. README self-hash machinery is retired (item 11).
