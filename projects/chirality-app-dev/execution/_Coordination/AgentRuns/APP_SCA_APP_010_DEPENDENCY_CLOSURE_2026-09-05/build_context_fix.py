#!/usr/bin/env python3
"""Deterministic context alignment for the thirteen SCA-APP-010 carriers under
D-APP-109 (node N8). Modes: --freeze (record pre-images), --apply (assert
pre-images, transform, write, record post-images), --check (post-image parity).

Writes only `_CONTEXT.md`, `_STATUS.md` (one history line), and `MEMORY.md`
(one line) per carrier, plus Evidence/context_fix/*.json in this run folder.
Fail-closed: every transformation is keyed on exactly-once text and every
introduced line is checked for trailing whitespace before any file is written.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_briefs as bb  # noqa: E402  (CARRIERS, row_fields, load_decomp, REPO, EXEC_REL)

RUN = bb.RUN
EVID = os.path.join(RUN, "Evidence", "context_fix")
DATE = "2026-09-05"
RULING = "D-APP-109"
PKG02_SA = ("DEL-02-01", "DEL-02-02", "DEL-02-04")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


def wrap(text: str) -> str:
    return textwrap.fill(text, width=80, break_long_words=False, break_on_hyphens=False)


def replace_once(text: str, old: str, new: str, where: str) -> str:
    n = text.count(old)
    if n != 1:
        fail(f"{where}: expected exactly one occurrence, found {n}: {old[:80]!r}")
    return text.replace(old, new, 1)


def carrier_dir(cid: str) -> str:
    return os.path.join(bb.REPO, bb.EXEC_REL, bb.CARRIERS[cid][0])


def targets(cid: str) -> list[str]:
    d = carrier_dir(cid)
    return [os.path.join(d, n) for n in ("_CONTEXT.md", "_STATUS.md", "MEMORY.md")]


# ------------------------------------------------------------- transactions
def tx_context(cid: str, text: str, row: dict) -> str:
    where = f"{cid}/_CONTEXT.md"
    line = bb.CARRIERS[cid][1]
    # Traceability rows
    m = re.search(r"^\| CoversScopeItems \| (.+?) \|$", text, re.M)
    if not m:
        fail(f"{where}: CoversScopeItems row missing")
    want = ", ".join(row["sow"])
    if m.group(1) != want:
        text = replace_once(text, m.group(0), f"| CoversScopeItems | {want} |", where)
    m = re.search(r"^\| SupportsObjectives \| (.+?) \|$", text, re.M)
    if not m:
        fail(f"{where}: SupportsObjectives row missing")
    want = ", ".join(row["obj"])
    if m.group(1) != want:
        text = replace_once(text, m.group(0), f"| SupportsObjectives | {want} |", where)
    # Anticipated Artifacts = the applied row's artifacts column
    sec = re.search(r"^## Anticipated Artifacts\n\n(.*?)(?=\n## )", text, re.M | re.S)
    if not sec:
        fail(f"{where}: Anticipated Artifacts section missing")
    body = wrap(row["artifacts"]) + "\n"
    text = text[: sec.start(1)] + body + text[sec.end(1):]
    # Source Authority (three PKG-02 carriers)
    if cid in PKG02_SA:
        sec = re.search(r"^## Source Authority\n\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
        if not sec:
            fail(f"{where}: Source Authority section missing")
        para = " ".join(sec.group(1).split())
        para = replace_once(
            para,
            "SCA-APP-004 and its owner-approved amendment prospectively control the current presentation target.",
            f"SCA-APP-010 (applied at Gate 5, 2026-09-04; D-APP-108) controls the current presentation target through the applied decomposition row L{line} and the SCA-APP-010 Gate-5 Current Contract section of `ScopeOfWork.md`; SCA-APP-004 and its owner-approved amendment remain dated history.",
            where,
        )
        if cid == "DEL-02-02":
            para = replace_once(
                para,
                "Work and Agents remain rebuildable, evidence-conditional projections; conversational prose and panel-local state must not be converted into project truth.",
                "The Who is working view, the Workflows view, and the proposal card present accepted state and never infer enforcement; conversational prose and panel-local state must not be converted into project truth.",
                where,
            )
        text = text[: sec.start(1)] + wrap(para) + "\n" + text[sec.end(1):]
    if cid == "DEL-08-03":
        text = replace_once(
            text,
            "## SCA-APP-004 Ownership Boundary\n",
            "## Ownership Boundary (SCA-APP-004 as amended by SCA-APP-010)\n",
            where,
        )
        text = replace_once(
            text,
            "- DEL-02-02 owns re-hosted Workbench/Pipeline, contextual Run, and\n  Coordination Panel presentation.\n",
            textwrap.fill(
                "- DEL-02-02 owns the right-panel Who is working view, Workflows view, and "
                "proposal card presentation (applied row L308); the contextual Pipeline "
                "presentation is retired from the active shell by SCA-APP-010 (DEC-025; "
                "code, routes, and tests retained), so DEL-08-03's dispatch semantics have "
                "no presentation consumer until a separate amendment re-hosts one.",
                width=80, subsequent_indent="  ", break_long_words=False, break_on_hyphens=False,
            ) + "\n",
            where,
        )
    return text


def history_line(cid: str, line: int) -> str:
    return (
        f"- {DATE} - {RULING} (owner direction 2026-09-05): dependency register re-extracted "
        f"against the applied decomposition row L{line} with the held edge proposals emitted as "
        "cycle-participating, non-gating rows (run "
        "`execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/`); "
        "`_CONTEXT.md` Traceability, Anticipated Artifacts, and Source Authority aligned to the "
        "applied row. No Remaining, lifecycle, Checking Approval SHA, product, or release change."
    )


def tx_status(cid: str, text: str) -> str:
    where = f"{cid}/_STATUS.md"
    if text.count("\n## History\n") != 1:
        fail(f"{where}: History section not exactly once")
    hl = history_line(cid, bb.CARRIERS[cid][1])
    hist = text.index("\n## History\n") + len("\n## History\n")
    tail = text[hist:]
    sec_end = re.search(r"\n## ", tail)
    section = tail[: sec_end.start()] if sec_end else tail
    dates = re.findall(r"^- (\d{4}-\d{2}-\d{2})", section, re.M)
    newest_first = len(dates) >= 2 and dates[0] > dates[-1]
    if newest_first:
        return text[:hist] + hl + "\n" + tail
    if sec_end:
        end = hist + sec_end.start()
        return text[:end].rstrip("\n") + "\n" + hl + "\n" + text[end:]
    return text.rstrip("\n") + "\n" + hl + "\n"


def tx_memory(cid: str, text: str) -> str:
    line = (
        f"- {DATE} - {RULING} dependency closure and context alignment: `Dependencies.csv` is "
        f"current with the applied row L{bb.CARRIERS[cid][1]}; rows noted `CYCLE_PARTICIPATING` are "
        "non-gating until their SCC is resolved by a recorded move, so read the seated items' "
        "`Depends` lines and gates, not those rows, for executable ordering; `_CONTEXT.md` "
        "traceability and artifacts equal the applied row; read `_STATUS.md` with this file "
        "before any write; nothing here is authority."
    )
    return text.rstrip("\n") + "\n" + line + "\n"


# ------------------------------------------------------------- modes
def read(p: str) -> bytes:
    with open(p, "rb") as f:
        return f.read()


def freeze() -> None:
    os.makedirs(EVID, exist_ok=True)
    pre = {os.path.relpath(p, bb.REPO): sha(read(p)) for cid in bb.CARRIERS for p in targets(cid)}
    with open(os.path.join(EVID, "pre_images.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(pre, f, indent=2)
        f.write("\n")
    print(f"froze {len(pre)} pre-images")


def apply() -> None:
    pre = json.load(open(os.path.join(EVID, "pre_images.json")))
    lines = bb.load_decomp()
    staged: dict[str, bytes] = {}
    for cid in bb.CARRIERS:
        row = bb.row_fields(lines, bb.CARRIERS[cid][1])
        assert row["id"] == cid
        for p in targets(cid):
            rel = os.path.relpath(p, bb.REPO)
            raw = read(p)
            if sha(raw) != pre[rel]:
                fail(f"pre-image mismatch: {rel}")
            text = raw.decode("utf-8")
            if p.endswith("_CONTEXT.md"):
                new = tx_context(cid, text, row)
            elif p.endswith("_STATUS.md"):
                new = tx_status(cid, text)
            else:
                new = tx_memory(cid, text)
            if new == text:
                continue
            before = set(text.split("\n"))
            for ln in new.split("\n"):
                if ln not in before and ln != ln.rstrip():
                    fail(f"{rel}: introduced trailing whitespace: {ln!r}")
            if "\r" in new or not new.endswith("\n"):
                fail(f"{rel}: line ending or final newline")
            staged[p] = new.encode("utf-8")
    post = {}
    for p, b in staged.items():
        with open(p, "wb") as f:
            f.write(b)
        post[os.path.relpath(p, bb.REPO)] = sha(b)
    with open(os.path.join(EVID, "post_images.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(post, f, indent=2)
        f.write("\n")
    print(f"applied {len(post)} files")


def check() -> None:
    post = json.load(open(os.path.join(EVID, "post_images.json")))
    bad = [rel for rel, h in post.items() if sha(read(os.path.join(bb.REPO, rel))) != h]
    if bad:
        fail(f"post-image mismatch: {bad}")
    print(f"verified {len(post)} post-images")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.freeze:
        freeze()
    if a.apply:
        apply()
    if a.check:
        check()
