# Chirality

Chirality is a filesystem-native agent operating system for governed
professional knowledge work. AI agents act on real work under explicit scope,
evidence, write-boundary, snapshot, and human-gate rules, so that machine
output is never confused with professional authority.

> If the filesystem is the database, architecture is a state-and-authority
> specification, not a service mesh.

Authoritative project state is file-based: packages, deliverables,
dependency registers, review records, snapshots, and decisions are plain
git-tracked files readable by humans, agents, and deterministic tools. If a
decision is not in a versioned file, it does not exist for purposes of
reliance. Agents propose, deterministic tools compute, humans rule. No agent
may certify, approve, sign, seal, or issue professional work product.

This repository is the private canonical source tree, upstream of the public
`chirality-app` export.

## Orientation

1. `AGENTS.md` — runtime doctrine and live agent index
2. `docs/DIRECTIVE.md` — founding constraints and design philosophy
3. `docs/SPEC.md` — physical structures and file formats
4. `docs/TYPES.md` — vocabulary, identifiers, lifecycle and epistemic types
5. `docs/CONTRACT.md` — binding K-* invariants
6. `docs/PLAN.md` — governed roadmap
7. `skills/README.md` — skill registry
8. `tools/REGISTRY.md` — deterministic tool registry

Explanatory background (not required reading for agents) lives in
`docs/thesis/`.

## Layout

| Path | Role |
| --- | --- |
| `AGENTS.md`, `agents/` | Runtime doctrine and agent instruction contracts |
| `skills/` | Method packs loaded by `TASK` |
| `tools/` | Deterministic helpers, validators, and the curated registry |
| `docs/` | Governance, specifications, standards, roadmap, and thesis |
| `init/` | Bootstrap and next-session notes |
| `runtime/` | Shared agent-runtime substrate (daemon, clients, contracts) |
| `exports/` | Public export profiles, manifests, and reports (private) |
| `projects/` | Private project workspaces |
| `domains/` | Private domain packs and local corpora |
| `plans/` | Non-governing planning material |

`projects/`, `domains/`, `plans/`, and `exports/` are not part of the public
export. The export profile in `exports/chirality-app/` is the boundary
contract; do not infer public package contents from the root listing.

## Validation and Export

```sh
python3 tools/validation/validate_skill_metadata.py skills
python3 tools/validation/discover_test_surfaces.py . --text
python3 exports/chirality-app/export_public.py
```

Run skill metadata validation after skill changes, test discovery when test
surfaces change, and the export tool after changing any public-exported
surface.

## License

MIT License. See `LICENSE.md`.

Copyright (c) 2026 Ryan Tufts
