# VERIFY-B1 Attempts

One terminal verifier invocation completed all five members. There were zero member failures, retries, candidate repairs, semantic repairs, or evidence normalization repairs. The inherited verifier harness was bound before invocation to trim comma-separated reference tokens and to use a visible verifier-only mutation in the negative probe; these are established template bindings, not runtime failures or candidate changes.

After all substantive terminal files were written, the verifier session ended
with a transient model-capacity error before invoking its already-written
deterministic `build_manifest.py`. The parent manager retained the error,
verified the completed terminal state, invoked that verifier-owned builder
without changing any substantive evidence, and independently reproduced every
resulting row, byte count, and SHA-256 binding. No member work was rerun and no
candidate or project byte changed.
