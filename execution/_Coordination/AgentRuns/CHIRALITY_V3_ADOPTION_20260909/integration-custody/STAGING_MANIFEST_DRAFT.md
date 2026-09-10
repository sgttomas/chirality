# Chirality v3 staging manifest structure — draft

Status: **STRUCTURE ONLY — DO NOT STAGE**

This draft defines how the final exact staging manifest will be assembled after
the Runtime, App, and distribution terminal subjects are stable. It does not
select a commit, accept governed content, or authorize staging, commit, push,
merge, publication, package creation, supplier access, or native qualification.

## Source selection

The final source set is the path union below, with later exact subjects
overriding predecessor bytes for the same path:

1. Root `ROOT_SCOPE_FREEZE_V7.json` plus the reviewed
   `ROOT_SEMANTIC_SUCCESSOR_V1.json` overlay.
2. App authority corpus `CORPUS_V21_FREEZE_v2.md`: its five core postimages,
   52 bound deliverable `_REFERENCES.md` postimages, and the project instruction
   and coordination postimages named by the owning App packet.
3. The original reviewed App backend 37-file subject
   `runtime-context-review-v2/APP_SUBJECT.sha256`, plus the App shared-daemon
   integration-test postimage in the reviewed seven-path supplement, overlaid
   by the terminal App product freeze. Predecessor-only backend implementation
   files remain in the source union; later App subjects replace bytes only for
   paths they explicitly bind.
4. The original reviewed Runtime source freeze and seven-path supplement,
   overlaid by the terminal Runtime freeze that succeeds Runtime V3 after the
   historical native-plan read/export repair. Predecessor-only Runtime files
   remain included. The final manifest must bind Runtime and App-adapter
   overlaps exactly once while preserving both ownership references.
5. The terminal distribution/export subject produced after the final Root,
   Runtime, and App bytes settle.
6. The five Root-routed downstream coordination notices required by D-GOV-42.

No path enters the source set merely because it appears in `git status`.
Every staged source path must have one owning final subject and a current hash.
An overlap must have identical bytes and an explicit owner/consumer relation.

## Evidence selection

Select compact evidence needed to make the candidate reviewable and to bind
the effective source:

- governing adoption decision, tranche manifest, acceptance matrix, work graph,
  final manager handoffs, and integration custody manifest;
- each effective lane's terminal source subject, terminal independent review
  return, checks, and manifest;
- accepted probe source and compact probe logs needed for another reviewer to
  reproduce or evaluate a terminal finding;
- the App corpus V2 freeze and V2 independent review packet;
- Root semantic successor and Astra Section 2 terminal review packet;
- final Runtime Section 3 and App Section 4 Astra packets;
- final distribution/export subject and terminal integrity review;
- a compact record of tests, limitations, and the boundaries that remain
  unqualified.

Superseded subjects and failed predecessor reviews remain on disk and may be
staged only when the terminal evidence explicitly needs their append-only
lineage. Their earlier PASS or FAIL verdict never substitutes for the effective
subject.

## Preserved but excluded from documentary PR staging

The following are retained in the integration checkout but excluded unless a
terminal manifest demonstrates that a particular member is necessary:

- duplicate captured source trees under semantic or Astra review evidence;
- pytest temporary roots and copied repository fixtures, including
  `astra-second-pass/root/pytest-tmp-v1/`;
- interim validator source copies and superseded probe captures once terminal
  checks bind the accepted final probe source/results;
- transient package staging directories, dependency caches, build output,
  coverage output, logs, and browser automation scratch;
- superseded V1–Vn source freezes, validation summaries, and review packets not
  required by the terminal lineage;
- unrelated pnpm lock/workspace artifacts if they appear. Runtime's npm
  `package-lock.json` remains source because the effective Runtime subject owns
  it and the YAML dependency is required.

These exclusions reduce duplicate source and transient artifacts in the PR;
they do not delete or rewrite the preserved working-tree evidence.

## Final manifest fields

The final machine-readable manifest will record:

- base commit, branch, and effective subject hashes;
- every staged path, byte size, SHA-256, lane owner, artifact class, and source
  subject;
- overlap resolution and source-qualified ownership;
- preserved-but-excluded path prefixes and rationale;
- current test/review evidence and known qualification limits;
- zero unattributed source paths and zero stale effective-subject bindings;
- explicit statements that governed acceptance, merge, publishing, release,
  supplier, credential, package, and native qualification remain separate.

Final generation waits for the parent manager's final-freeze signal.
