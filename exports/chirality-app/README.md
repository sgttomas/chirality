# Chirality App Public Export

This export profile builds the public `chirality-app` repository from the
private canonical `chirality` tree.

The export is allowlist-based. Private projects, domains, migration records,
historical plans, source corpora, archives, dependency folders, build outputs,
local runtime state, and environment files are excluded.

Run from the private repo root:

```sh
python3 exports/chirality-app/export_public.py
```

To replace the local public repo after reviewing the staging report:

```sh
python3 exports/chirality-app/export_public.py --apply-target /Users/ryan/ai-env/projects/chirality-app
```
