# DEL-01-02 Precheck

- Sequence: `1/3`
- Started: `2026-07-14T03:38:26Z`
- Accepted checkout: `main@ef461cfdb3a4b135dc670b04f646eca3eac47712`
- Frozen row: exact `DEL-01-02` row in parent `FROZEN_INPUTS.tsv`; all nine source/control hashes matched.
- Accepted decomposition: `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713`
- Scope/objective binding: `SOW-003,SOW-028`; `OBJ-002`.
- Lifecycle/format: `_STATUS.md` says `IN_PROGRESS`; exactly four legacy production documents were present; live `ScopeOfWork.md` was absent.
- Dependencies: `Dependencies.csv` contained 13 data rows, all `ACTIVE`; the frozen register and summary hashes matched.
- Authority: path-scoped batch variance is `{REPO_ROOT}/execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01/HUMAN_DIRECTION.md`; normative format/tool authority is `D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176` under `AMENDMENT-001.md`.
- Brief re-read: the frozen row and child brief were re-read at the start. The tool-source contract was re-read after the first failed-before-output invocation, and `AMENDMENT-001.md` was read before retry.

Result: `PASS` after the recorded authority-token amendment and one failed-before-output retry.
