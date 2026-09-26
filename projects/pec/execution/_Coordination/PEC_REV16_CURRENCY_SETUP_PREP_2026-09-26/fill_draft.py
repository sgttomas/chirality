#!/usr/bin/env python3
"""Render DRAFT_D-PEC-101_rev16_currency_setup_proposal.md from the .src.md and the k1/ and k4/ evidence.
Preparation aid only. Usage: python3 fill_draft.py (run from this folder)."""
import hashlib, re
from pathlib import Path
H = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256((H / p).read_bytes()).hexdigest()
src = (H / "DRAFT_D-PEC-101_rev16_currency_setup_proposal.src.md").read_text(encoding="utf-8")

def tsv_table(path, title):
    rows = [l.split("\t") for l in (H / path).read_text().splitlines() if "\t" in l]
    head, body = rows[0], rows[1:]
    out = [f"{title}", "", "| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(f"`{c}`" if re.fullmatch(r"[0-9a-f]{64}", c) else c for c in r) + " |" for r in body]
    return "\n".join(out)

census = (H / "k4/evidence/census.md").read_text(encoding="utf-8")
tbl = "\n".join(l for l in census.splitlines() if l.startswith("|"))
k4_census = f"""The K4 generator globs all 66 deliverable folders at run time. It requires, and stops if any fails, that:

- the 61 `_CONTEXT.md` whose provenance ends ``then by revision 1.5 (`current_basis`, SCA-005 successor).`` (CTX_STD) and the 2 whose `D-PEC-93` provenance reads ``SCA-005 successor; deliverable added by A-19). Fields templated`` (A-20 for DEL-02-09) (CTX_D93) are exactly the pinned 63;
- the three SCA-006 A2 mirrors (DEL-04-03, DEL-08-01, DEL-08-03), which already carry ``then by revision 1.6 (`current_basis`, SCA-006 successor).``, are byte-identical to their pinned hashes and are not written;
- the 66 `_REFERENCES.md` naming ``(revision 1.5, accepted `current_basis`; SCA-005 successor)`` and `` `docs/PRD.md` v2.3 `` are exactly the pinned 66;
- any other context or reference already names revision 1.6 (and PRD v2.4) — the tolerance that lets K4 run before or after K1, whose new folders are born at revision 1.6;
- each anchor occurs exactly once.

So the plan's 63 / 66 holds (unlike `D-PEC-95`'s 40 → 42).

The acts:

- **CTX_STD (61):** ``then by revision 1.5 (`current_basis`, SCA-005 successor).⏎`` → ``then by revision 1.5 (`current_basis`, SCA-005 successor),⏎then by revision 1.6 (`current_basis`, SCA-006 successor).⏎`` — the exact form the three A2 mirrors carry. After the act the 64 `D-PEC-62`-scaffolded contexts share one byte-identical provenance block (checked).
- **CTX_D93 (2):** ``SCA-005 successor; deliverable added by A-19). Fields templated⏎`` → ``SCA-005 successor; deliverable added by A-19),⏎then by revision 1.6 (`current_basis`, SCA-006 successor). Fields templated⏎`` (A-20 for DEL-02-09).
- **References (66):** ``(revision 1.5, accepted `current_basis`; SCA-005 successor)`` → ``(revision 1.6, accepted `current_basis`; SCA-006 successor)`` and `` `docs/PRD.md` v2.3 `` → `` `docs/PRD.md` v2.4 ``.
- **Add-on C (`--covers`, 2 of the 66):** DEL-04-03 ``covers SOW-006;SOW-007)`` → ``covers SOW-006;SOW-007;SOW-097)``; DEL-08-03 ``covers SOW-043)`` → ``covers SOW-043;SOW-098)``, each asserted equal to its `Deliverables.csv` cell.

No other byte changes; no `_SEMANTIC.md`, `_DEPENDENCIES.md`, `Dependencies.csv` or `_STATUS.md` is touched. Lifecycle census (from `_STATUS.md`, unchanged by K4):

{tbl}

The re-pin changes deliverable metadata, not the artifacts under `CHECKING` (DEL-00-01, DEL-00-03, DEL-08-02, DEL-10-01) or `IN_PROGRESS` (DEL-01-03, DEL-01-05), and changes no lifecycle state; the `D-PEC-95` and SCA-004 re-pins are the precedents."""

g4 = sha("k4/gen_d101_k4.py")
k4_gen = f"""**K4: `gen_d101_k4.py`, SHA-256 `{g4}`.** Stdlib-only Python, prepared with CPython 3.13.7 (TASK-authored, manager-rerun and rebuilt byte-identically from exports of `aca930622` and `dfb089b8a`). Copied byte for byte into the run root and run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/<run root>/gen_d101_k4.py --repo "$(git rev-parse --show-toplevel)" [--covers]
```

Add-on C adds `--covers`. Before any write it checks: all 136 pinned hashes (129 targets; `PRD.md`, `SOFTWARE_DECOMP.md`, `Deliverables.csv`, `ScopeLedger.csv` and the three A2 mirrors); pinned literal anchors showing PRD version 2.4 and revision 1.6 `current_basis`; the population rule above; each anchor exactly once; the rendered post-state (every context ends its provenance at revision 1.6; every reference names revision 1.6 and PRD v2.4 and neither 1.5 nor v2.3; one provenance block across the 64); and that the write set equals the 129 targets. It exits 1 with nothing written on any failure, and a second run exits 1. `--check-only` renders without writing. K4 is **slot-free**: no date appears in any postimage, so there is no `--act-date`, no local-date check and no slot rule; the verifier's reproduction is a byte comparison on a fresh export. `build_gen_d101_k4.py`, `gen_d101_k4.template.py` and `tables_k4.py` are preparation aids, not bound."""

k1_table = (H / "k1/evidence/grant_table.md").read_text(encoding="utf-8").rstrip()
k4_table = (H / "k4/evidence/grant_table.md").read_text(encoding="utf-8").rstrip()
k4_table = "\n".join(l for l in k4_table.splitlines() if l.startswith("|"))

def results(path):
    rows = [l.split("\t") for l in (H / path).read_text().splitlines() if l.strip()]
    return "\n".join(f"| `{r[0]}` | {r[1]} | {r[2] if len(r) > 2 else ''} |" for r in rows)

ev = ("K1 prototype suite (`k1/run_k1_prototypes.sh`, rerun with `PRECOMMIT` = current `origin/main` "
      "`dfb089b8abae48ee699117c5bc167301963b2ab5`; the first run at `aca930622` is kept in `k1/evidence_aca930622/`, "
      "with identical results and identical postimage hashes). Exit 1 is expected where the description says so; "
      "the strict validator exits 1 whenever warnings exist under `--strict`.\n\n"
      "| Step | Exit | Meaning |\n|---|---:|---|\n" + results("k1/evidence/RESULTS.tsv") +
      "\n\nK4 prototype suite (`k4/run_k4_prototypes.sh`, TASK-run at `aca930622`; K4's pinned files are byte-identical at `dfb089b8a`, and the manager's combined runs above exercise the same generator there):\n\n"
      "| Step | Exit | Meaning |\n|---|---:|---|\n" + results("k4/evidence/RESULTS.tsv"))

arts = []
for p in sorted(x for x in H.rglob("*") if x.is_file() and x.name not in ("SHA256SUMS",) and "evidence" not in x.parts
                and not x.name.startswith("DRAFT_") and x.suffix in (".py", ".sh", ".md")):
    rel = p.relative_to(H)
    arts.append(f"| `{rel}` | `{sha(rel)}` |")
art = "| Artifact | SHA-256 |\n|---|---|\n" + "\n".join(arts) + "\n\nEvidence files (`k1/evidence/`, `k1/evidence_aca930622/`, `k4/evidence/`, `evidence/`) are hashed in `SHA256SUMS`."

rep = {
    "{{K4_CENSUS}}": k4_census, "{{K4_TABLE}}": k4_table,
    "{{K4_AGG}}": tsv_table("k4/evidence/aggregates.txt", "K4 aggregates (bytewise-sorted `projects/pec/…` path order; SHA-256 over the concatenated bytes; path list = SHA-256 of the paths each followed by LF):"),
    "{{K1_TABLE}}": k1_table,
    "{{K1_AGG}}": tsv_table("k1/evidence/aggregates.txt", "K1 aggregates (same conventions):"),
    "{{K4_GEN}}": k4_gen, "{{K1_GEN_HASH}}": sha("k1/gen_d101_k1.py"),
    "{{EVIDENCE_TABLE}}": ev, "{{ARTIFACT_TABLE}}": art,
}
for k, v in rep.items():
    assert src.count(k) >= 1, k
    src = src.replace(k, v)
assert "{{" not in src
out = H / "DRAFT_D-PEC-101_rev16_currency_setup_proposal.md"
out.write_text(src, encoding="utf-8")
print(out.name, hashlib.sha256(out.read_bytes()).hexdigest())
