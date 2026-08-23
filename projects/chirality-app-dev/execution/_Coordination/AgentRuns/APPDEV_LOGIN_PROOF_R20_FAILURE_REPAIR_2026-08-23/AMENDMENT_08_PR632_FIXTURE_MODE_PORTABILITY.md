# Amendment 08 — PR #632 fixture-mode portability repair

- Date: `2026-08-23`.
- Authority: exact owner direction in `CHAT_TRANSCRIPTION.md`.
- Basis: clean branch `codex/app-login-proof-r20-repair`, HEAD/origin branch `980f5951dbbfe88302514802384e4ffec33c38b9`, frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- Phase A is diagnosis-only: run the focused login-proof suite exactly once under `umask 0002`, freeze failure counts/message, and inspect test/product creation sites read-only. No frontend edit until diagnosis is accepted.
- Phase B may change only the focused test suite and, only if diagnosis proves product umask reliance, the minimum product directory-creation call needed to add explicit mode without weakening any guard. Explicit test fixture modes are `0o700` for directories and `0o600` for files.
- Phase C stops at fresh source review PASS and exact frontend candidate readiness for a CHANGE-owned source commit. No build is permitted before the exact source commit exists.
- Later phases are serialized on that commit: one supply verification, one offline pack, package/restaging evidence, prescribed full-suite runs, TM candidate, fresh review, governance gates, receipt, and CHANGE publication.
- Hard fences: no proof execution/claim, no guard weakening, no daemon/supply/procedure semantic change beyond authorized hardening and revision/package-identity restaging, no network/download, no rebase/force-push/merge, and no WORKING_ITEMS Git publication.
