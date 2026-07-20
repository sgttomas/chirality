# EVALUATION Protocol — D-APP-50 Five-Gate Completion

- **Run:** `APPDEV_LOOP_2026-07-20_DAPP50_HEADLESS_LIVE`
- **Node:** `V4-DAPP50-FIVE-GATE-COMPLETION`
- **Role:** fresh EVALUATION (Agent 1); no delegation
- **Frozen branch/HEAD:** `codex/app-dev-dapp50-headless-live-20260720` / `55a066fdff6877d8aa2a49ce08a545ac98872848`
- **Accepted subject basis:** four frozen W6 candidates accepted by W6R, plus the preserved V3 `BLOCK` evaluation package and terminals
- **Evaluation question:** does a fresh execution of exactly V3's five omitted commands close V3-F-001 while preserving the frozen subject and authority boundaries?
- **Criterion:** `ACCEPT` only if all five commands exit zero, the managed-premerge Section 8/9 counts are retained, the evaluator-owned server is stopped, and final frozen-state and write-containment checks pass
- **Toolbelt:** the five deterministic commands frozen in the V4 brief; no redundant gate, delegation, scoring, repair, cleanup, Git action, packaging, or release action
- **Write quarantine:** this exact five-file evaluation root and the V4 terminal instance

## Frozen entry state

Before the commands, V4 reproduced G2 HEAD, an empty index, the four W6
candidate hashes, one Receipt-85, absent `frontend/dist`, and no listener on
TCP port 3000. The tracked-diff fingerprint was
`317a9a6dff0e0a4e6620b93bb34f66ab49cabd591e46e53dd585b775d32e87a0`;
the pre-existing untracked-path fingerprint was
`77fd364434c753eb1a5fdaef2295090a37718de401ed48d9912373cb2c416da4`;
the cached-diff fingerprint was the empty SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Exact method

V4 ran exactly these five released validation commands, in order:

1. `npm run typecheck` from `projects/chirality-app-dev/frontend`;
2. `npm run build` from `projects/chirality-app-dev/frontend`;
3. `npm run harness:validate:premerge` from
   `projects/chirality-app-dev/frontend`, against a uniquely V4-owned
   `npm run dev:next` process, which V4 stopped immediately afterward;
4. `python3 -m pytest -q tools/validation` from the repository root;
5. `python3 -m pytest -q tools/practitioner_harness` from the repository root.

V4 did not rerun V3's focused/catalog/full-frontend/pull-contract/dependency/
receipt/corpus/self-check coverage. Those accepted V3 results are consumed as
preserved evidence. Ordinary ignored build and harness refreshes were allowed;
packaging was not run.

