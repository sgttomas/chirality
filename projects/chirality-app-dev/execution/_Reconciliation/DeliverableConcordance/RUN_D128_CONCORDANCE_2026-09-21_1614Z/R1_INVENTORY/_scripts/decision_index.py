#!/usr/bin/env python3
"""DECISION_INDEX.csv from the frozen App decision register table rows (`| D-... |`).

Cells split on `|` (register rows have exactly six cells). State = leading upper-case
word(s) of the state cell, `/`-joined words kept (e.g. RULED, AWAITING_RULING, NOT_PREPARED); StateCellVerbatimShort =
first 160 chars of the state cell; PacketPath / RulingPath = backticked tokens containing `/` or
ending `.md` in the packet / ruling cells (`;`-joined; empty when the cell names no path);
EffectFlag = PENDING_EFFECT if state or ruling cell matches /pending|HELD|held|remain|not applied|awaiting/i,
else NONE; DeliverablesNamed / PackagesNamed = sorted unique DEL-xx-yy / PKG-xx tokens anywhere in the row.
"""
import argparse, os, re
import r1_common as C

EFFECT = re.compile(r"pending|held|remain|not applied|awaiting", re.I)


def paths(cell):
    toks = [t for t in re.findall(r"`([^`]+)`", cell) if "/" in t or t.endswith(".md")]
    return ";".join(toks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen-root", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    reg = os.path.join(a.frozen_root, C.APP_REL, "execution/_Coordination/_DECISIONS/_REGISTER.md")
    rows = []
    for line in C.read_text(reg).split("\n"):
        if not re.match(r"^\|\s*D-", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            raise SystemExit(f"unexpected cell count {len(cells)}: {line[:80]}")
        did, _dec, _blocks, state, packet, ruling = cells
        m = re.match(r"[A-Z][A-Z_]+(?:\s*/\s*[A-Z][A-Z_]+\b)*", state)
        rows.append([
            did, m.group(0) if m else "", state[:160], paths(packet), paths(ruling),
            "PENDING_EFFECT" if EFFECT.search(state) or EFFECT.search(ruling) else "NONE",
            ";".join(sorted(set(re.findall(r"\bDEL-\d{2}-\d{2}\b", line)))),
            ";".join(sorted(set(re.findall(r"\bPKG-\d{2}\b", line)))),
        ])

    def key(r):
        m = re.match(r"([A-Z-]+?)-?(\d+)(.*)", r[0])
        return (m.group(1), int(m.group(2)), m.group(3)) if m else (r[0], 0, "")
    rows.sort(key=key)
    C.write_csv(a.out, ["DecisionID", "State", "StateCellVerbatimShort", "PacketPath", "RulingPath",
                        "EffectFlag", "DeliverablesNamed", "PackagesNamed"], rows)
    print(len(rows), "decisions;", sum(1 for r in rows if r[5] == "PENDING_EFFECT"), "PENDING_EFFECT")


if __name__ == "__main__":
    main()
