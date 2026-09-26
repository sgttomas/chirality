#!/usr/bin/env python3
"""Provisional D-PEC-101 part K4 exact generator: revision-1.6 re-pin of deliverable metadata.

Deterministic. Stdlib only. Slot-free: no date or other varying value appears
in any postimage, so there is no --act-date and no local-date check. Run from
any directory against a repository root whose bytes equal origin/main
aca930622ba167689881416044ba0feaee3ef003 for every path listed in PREIMAGES.
Every postimage is computed and every check passes before the first byte is
written; on any failure it exits 1, prints FAIL on stderr and writes nothing.
A second run exits 1 (the targets no longer match their pinned preimages).

Acts (anchor lines only; each anchor must occur exactly once in its file):
  * CTX_STD (61 _CONTEXT.md): the final provenance clause for revision 1.5
    gains a comma and a following revision-1.6 clause;
  * CTX_D93 (2 _CONTEXT.md, DEL-02-08 / DEL-02-09): the D-PEC-93 provenance
    line gains the revision-1.6 clause before "Fields templated";
  * references (66 _REFERENCES.md): the SOFTWARE_DECOMP.md bullet moves to
    revision 1.6 (SCA-006 successor) and the PRD bullet to v2.4;
  * add-on C (--covers): the ScopeLedger bullet of DEL-04-03 and DEL-08-03
    carries the revision-1.6 covers list, asserted equal to the
    Deliverables.csv CoversScopeItems cell. Same files, different postimages.

Fail-closed checks before any write:
  * every PREIMAGES path hashes to its pinned SHA-256 (129 targets and 7
    read-only basis files: PRD.md, SOFTWARE_DECOMP.md, Deliverables.csv,
    ScopeLedger.csv and the three SCA-006 A2-mirror _CONTEXT.md);
  * PRD.md names version 2.4 and SOFTWARE_DECOMP.md names revision 1.6 as
    current (pinned literal anchors, each exactly once);
  * population (globbed at run time): every deliverable _CONTEXT.md is a
    pinned target, a pinned A2 mirror, or already ends its provenance at
    revision 1.6 (SCA-006) without a pending revision-1.5 anchor; every
    _REFERENCES.md is a pinned target or already names revision 1.6 and PRD
    v2.4 without the revision-1.5 or PRD v2.3 bullet. The tolerance lets K4
    run before or after the separately rulable K1 part (new folders born at
    revision 1.6 / PRD v2.4);
  * every anchor occurs exactly once; all postimages rendered;
  * post-state (rendered): every context ends its provenance at revision 1.6
    (SCA-006); every reference names revision 1.6 and PRD v2.4 and neither
    revision 1.5 nor PRD v2.3; the 61 CTX_STD postimages and the 3 mirrors
    share one byte-identical provenance block;
  * the write set equals the grant (the 129 pinned targets, for either flag
    set).
The report also carries, report-only, whether each reference's covers list
equals its Deliverables.csv cell (a blank cell agrees with the D-PEC-95
add-on R "none — retired under SCA-005, formerly SOW-0NN" form).

Usage:
  python3 gen_d101_k4.py --repo <REPO_ROOT> [--covers] [--check-only]

stdout: a TSV report (only on success) with READ, CHECK, RENDER (check-only)
or WRITE rows: kind, subject, value 1, value 2.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

PEC = "projects/pec"
EX = f"{PEC}/execution"
PRD = f"{PEC}/docs/PRD.md"
DECOMP = f"{EX}/_Decomposition/SOFTWARE_DECOMP.md"
DELIVERABLES = f"{EX}/_Decomposition/Deliverables.csv"
LEDGER = f"{EX}/_Decomposition/ScopeLedger.csv"

# @@PINNED@@

# Basis currency anchors (each must occur exactly once).
PRD_VERSION_ANCHOR = "\n| **Version** | 2.4 |\n"
DECOMP_VERSION_ANCHORS = ['\nrevision: "1.6"\n', "\n| Revision | 1.6, 2026-09-26 (SCA-006) |\n"]

CTX_STD_OLD = "then by revision 1.5 (`current_basis`, SCA-005 successor).\n"
CTX_STD_NEW = ("then by revision 1.5 (`current_basis`, SCA-005 successor),\n"
               "then by revision 1.6 (`current_basis`, SCA-006 successor).\n")
CTX_D93_OLD = "SCA-005 successor; deliverable added by {A}). Fields templated\n"
CTX_D93_NEW = ("SCA-005 successor; deliverable added by {A}),\n"
               "then by revision 1.6 (`current_basis`, SCA-006 successor). Fields templated\n")
REF_PAIRS = [
    ("- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.5, accepted `current_basis`; SCA-005 successor)\n",
     "- `execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.6, accepted `current_basis`; SCA-006 successor)\n"),
    ("- `docs/PRD.md` v2.3 (accepted source corpus; see SourceRef column of the ledger)\n",
     "- `docs/PRD.md` v2.4 (accepted source corpus; see SourceRef column of the ledger)\n"),
]
COVERS_LINE = "- `execution/_Decomposition/ScopeLedger.csv` (SOW→PKG→DEL→OBJ ledger; covers {S})\n"
COVERS_RE = re.compile(r"^- `execution/_Decomposition/ScopeLedger\.csv` \(SOW→PKG→DEL→OBJ ledger; covers (.*)\)$",
                       re.M)
RETIRED_COVERS_RE = re.compile(r"none — retired under SCA-005, formerly SOW-\d{3}")
# Add-on C: revision 1.6 added SOW-097 to DEL-04-03 and SOW-098 to DEL-08-03.
COVERS_ADDON = {
    "DEL-04-03": ("SOW-006;SOW-007", "SOW-006;SOW-007;SOW-097", "SOW-097"),
    "DEL-08-03": ("SOW-043", "SOW-043;SOW-098", "SOW-098"),
}
# The final "revision X.Y (`current_basis`, SCA-NNN successor" clause of a provenance block.
REV_CLAUSE_RE = re.compile(r"revision (\d+\.\d+) \(`current_basis`,\s+(SCA-\d{3}) successor")


class Fail(Exception):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def replace_once(text: str, old: str, new: str, where: str) -> str:
    n = text.count(old)
    if n != 1:
        raise Fail(f"anchor count {n} != 1 in {where}: {old[:80]!r}")
    return text.replace(old, new)


def provenance(text: str, where: str) -> str:
    """The `## Provenance` block: from its heading to the next level-2 heading or EOF."""
    if text.count("\n## Provenance\n") != 1:
        raise Fail(f"{where}: `## Provenance` heading count != 1")
    block = "## Provenance\n" + text.split("\n## Provenance\n", 1)[1]
    nxt = block.find("\n## ", 1)
    return block if nxt < 0 else block[: nxt + 1]


def final_clause(text: str, where: str) -> tuple[str, str] | None:
    found = REV_CLAUSE_RE.findall(provenance(text, where))
    return found[-1] if found else None


def ctx_current(text: str, where: str) -> bool:
    return final_clause(text, where) == ("1.6", "SCA-006")


def ref_current(text: str) -> bool:
    return (REF_PAIRS[0][1] in text and REF_PAIRS[1][1] in text
            and REF_PAIRS[0][0] not in text and REF_PAIRS[1][0] not in text)


def del_id(rel: str) -> str:
    return Path(rel).parent.name.split("_")[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    ap.add_argument("--covers", action="store_true", help="add-on C (DEL-04-03 / DEL-08-03 covers lists)")
    ap.add_argument("--check-only", action="store_true", help="render and check; write nothing")
    a = ap.parse_args()
    repo = a.repo.resolve()
    report: list[tuple[str, str, str, str]] = []
    try:
        # 0. preimages (targets and basis)
        for rel, want in PREIMAGES.items():
            p = repo / rel
            if not p.is_file():
                raise Fail(f"pinned path missing: {rel}")
            got = sha(p.read_bytes())
            if got != want:
                raise Fail(f"preimage mismatch {rel}: {got} != {want}")
            report.append(("READ", rel, got, "basis" if rel in BASIS_PATHS else "target"))
        prd_text = (repo / PRD).read_text(encoding="utf-8")
        if prd_text.count(PRD_VERSION_ANCHOR) != 1:
            raise Fail("PRD.md does not name version 2.4 exactly once at the pinned anchor")
        decomp_text = (repo / DECOMP).read_text(encoding="utf-8")
        for anchor in DECOMP_VERSION_ANCHORS:
            if decomp_text.count(anchor) != 1:
                raise Fail(f"SOFTWARE_DECOMP.md anchor {anchor.strip()!r} count != 1")
        report.append(("CHECK", "basis_versions", "PRD 2.4", "SOFTWARE_DECOMP 1.6"))
        with open(repo / DELIVERABLES, newline="", encoding="utf-8") as f:
            dels = {r["DeliverableID"]: r for r in csv.DictReader(f)}

        # 1. population (globbed at run time; fail closed on anything unexpected)
        work = repo / EX
        all_ctx = sorted(str(p.relative_to(repo)) for p in work.glob("PKG-*/1_Working/DEL-*/_CONTEXT.md"))
        all_ref = sorted(str(p.relative_to(repo)) for p in work.glob("PKG-*/1_Working/DEL-*/_REFERENCES.md"))
        folders = sorted(str(p.relative_to(repo)) for p in work.glob("PKG-*/1_Working/DEL-*") if p.is_dir())
        ctext = {p: (repo / p).read_text(encoding="utf-8") for p in all_ctx}
        rtext = {p: (repo / p).read_text(encoding="utf-8") for p in all_ref}
        pinned_ctx = set(CTX_STD_PATHS) | set(CTX_D93_PATHS)
        extra_ctx, extra_ref = [], []
        for p in all_ctx:
            if p in pinned_ctx or p in MIRROR_PATHS:
                continue
            t = ctext[p]
            if not ctx_current(t, p) or CTX_STD_OLD in t or "SCA-005 successor; deliverable added by" in t:
                raise Fail(f"unpinned context is not already at revision 1.6: {p}")
            extra_ctx.append(p)
        for p in all_ref:
            if p in REF_PATHS:
                continue
            if not ref_current(rtext[p]):
                raise Fail(f"unpinned reference packet is not already at revision 1.6 / PRD v2.4: {p}")
            extra_ref.append(p)
        missing = sorted((pinned_ctx | set(MIRROR_PATHS) | set(REF_PATHS)) - set(all_ctx) - set(all_ref))
        if missing:
            raise Fail(f"pinned paths outside the globbed population: {missing[:3]}")
        report.append(("CHECK", "population_folders", str(len(folders)), f"{len(extra_ctx)} contexts / "
                       f"{len(extra_ref)} references already at 1.6 beyond the pins"))

        # 2. render
        writes: dict[str, bytes] = {}
        for p in CTX_STD_PATHS:
            writes[p] = replace_once(ctext[p], CTX_STD_OLD, CTX_STD_NEW, p).encode("utf-8")
        for p, anum in CTX_D93_PATHS.items():
            writes[p] = replace_once(ctext[p], CTX_D93_OLD.replace("{A}", anum),
                                     CTX_D93_NEW.replace("{A}", anum), p).encode("utf-8")
        for p in REF_PATHS:
            t = rtext[p]
            for old, new in REF_PAIRS:
                t = replace_once(t, old, new, p)
            d = del_id(p)
            if a.covers and d in COVERS_ADDON:
                old_s, new_s, sow = COVERS_ADDON[d]
                if dels[d]["CoversScopeItems"] != new_s:
                    raise Fail(f"{d}: Deliverables.csv CoversScopeItems {dels[d]['CoversScopeItems']!r} != {new_s!r}")
                t = replace_once(t, COVERS_LINE.replace("{S}", old_s), COVERS_LINE.replace("{S}", new_s), p)
                report.append(("CHECK", f"covers_addon {d}", new_s, "equals Deliverables.csv cell"))
            writes[p] = t.encode("utf-8")

        # 3. post-state checks on the rendered corpus
        post_c = {p: (writes[p].decode("utf-8") if p in writes else ctext[p]) for p in all_ctx}
        post_r = {p: (writes[p].decode("utf-8") if p in writes else rtext[p]) for p in all_ref}
        stale_c = [p for p in all_ctx if not ctx_current(post_c[p], p)]
        if stale_c:
            raise Fail(f"after rendering, contexts not ending at revision 1.6: {stale_c[:3]}")
        report.append(("CHECK", "contexts_final_clause_revision_1.6", str(len(all_ctx) - len(stale_c)),
                       str(len(all_ctx))))
        stale_r = [p for p in all_ref if not ref_current(post_r[p])]
        if stale_r:
            raise Fail(f"after rendering, references not at revision 1.6 / PRD v2.4: {stale_r[:3]}")
        report.append(("CHECK", "references_revision_1.6_prd_2.4", str(len(all_ref) - len(stale_r)),
                       str(len(all_ref))))
        blocks = {provenance(post_c[p], p) for p in list(CTX_STD_PATHS) + list(MIRROR_PATHS)}
        if len(blocks) != 1:
            raise Fail(f"{len(blocks)} distinct provenance blocks across the 61 re-pinned contexts and 3 mirrors")
        report.append(("CHECK", "provenance_block_identity", str(len(CTX_STD_PATHS) + len(MIRROR_PATHS)),
                       sha(next(iter(blocks)).encode("utf-8"))))
        # report-only: covers list versus register cell, every reference
        agree, disagree = 0, []
        for p in all_ref:
            m = COVERS_RE.findall(post_r[p])
            cell = dels.get(del_id(p), {}).get("CoversScopeItems")
            ok = len(m) == 1 and cell is not None and (
                m[0] == cell or (cell == "" and RETIRED_COVERS_RE.fullmatch(m[0]) is not None))
            if ok:
                agree += 1
            else:
                disagree.append(del_id(p))
        report.append(("CHECK", "covers_equal_register_report_only", f"{agree}/{len(all_ref)}",
                       ";".join(disagree) if disagree else "none differ"))

        # 4. grant
        expected = set(CTX_STD_PATHS) | set(CTX_D93_PATHS) | set(REF_PATHS)
        if set(writes) != expected or len(writes) != 129:
            raise Fail(f"write set differs from the grant: {sorted(set(writes) ^ expected)[:5]}")
        for rel in writes:
            if rel not in PREIMAGES or rel in BASIS_PATHS:
                raise Fail(f"write target without a pinned target preimage: {rel}")

        # 5. write (every postimage computed and checked above)
        agg_pre, agg_post = hashlib.sha256(), hashlib.sha256()
        order = sorted(writes, key=lambda r: r.encode("utf-8"))
        for rel in order:
            pre = (repo / rel).read_bytes()
            agg_pre.update(pre)
            agg_post.update(writes[rel])
            report.append(("RENDER" if a.check_only else "WRITE", rel, sha(pre), sha(writes[rel])))
        if not a.check_only:
            for rel in order:
                (repo / rel).write_bytes(writes[rel])
        tag = "A+C" if a.covers else "A"
        paths = "".join(r + "\n" for r in order).encode("utf-8")
        report.append(("CHECK", f"aggregate flags={tag} files={len(writes)}", agg_pre.hexdigest(),
                       agg_post.hexdigest()))
        report.append(("CHECK", f"pathlist flags={tag}", sha(paths), "newline-terminated, bytewise-sorted"))
    except Fail as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for row in report:
        print("\t".join(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
