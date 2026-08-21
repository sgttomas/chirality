# Chirality App Public Export

This export profile builds the curated `chirality-app` desktop release
repository from the public canonical `chirality` source tree.

The projection is allowlist-based. Non-release projects, domain repositories,
migration records, historical plans, source corpora, archives, dependency
folders, build outputs, local runtime state, and environment files are excluded.

Private-project CI workflows are also excluded when their working directories
do not exist in the public tree. The public init prompt is generated as a
framework-only launcher rather than retaining private loop entrypoints.
Public governance decisions, their handoff, and `human_actors.md` remain in
scope because authority verification depends on them; private-project TRB
briefs and the practitioner-development backlog are explicitly excluded.

D-GOV-20 adds the generic `runtime/` workspace, bundled CLI, provider-neutral
contracts, and safe engine adapters to the public boundary. Export policy
continues to exclude credentials,
user-data and machine-registration state, logs, downloaded models, private PEC
or Piping adapters, and private project manifests/evidence.

`PUBLIC_README.md` is the authored landing page for the public repository.
The exporter deliberately maps it to root `README.md`; the canonical
repository's root README is not copied. Boundary validation fails if the
public README is missing its release/source-boundary markers or contains
source-repository framing that misstates the release projection.

Every entry in `ROOT_FILES`/`ROOT_DIRS` must exist at the repo root; the
exporter fails with an error listing any missing entries rather than silently
skipping them (owner ruling, 2026-07-01). When the tree is reorganized, update
the allowlist in `export_public.py` deliberately, then regenerate the tracked
`export-manifest.csv` and `export-report.md` by re-running the exporter.

Run from the Chirality source root:

```sh
python3 exports/chirality-app/export_public.py
```

To replace the local public repo after reviewing the staging report:

```sh
python3 exports/chirality-app/export_public.py --apply-target /Users/ryan/ai-env/projects/chirality-app
```
