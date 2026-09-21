"""Shared helpers for the EXT manager scripts (R2 scope extension)."""
import csv, glob, hashlib, io, os

HERE = os.path.dirname(os.path.abspath(__file__))
EXT = os.path.dirname(HERE)
R2 = os.path.dirname(EXT)
RUN = os.path.dirname(R2)

# ledger stem -> (item, folder relative to EXT)
LEDGERS = [
    ("DEC", "3", "DEC"),
    ("DOC-BUILDREL", "4", "DOC_REL"),
    ("DOC-RQGATES", "4", "DOC_REL"),
    ("DOC-RQRUN", "4", "DOC_REL"),
    ("DOC-VALSTRAT", "4", "DOC_VAL"),
    ("DOC-RELIANCE", "4", "DOC_VAL"),
    ("SOW", "5", "SOW"),
    ("DOC-PRODAGENTS", "6", "DOC_DEV"),
    ("DOC-ADDING_A_TOOL", "7", "DOC_DEV_R1"),  # rerun of record (DOC_DEV attempt superseded)
    ("DOC-README", "7", "DOC_DEV"),
    ("DOC-RUNTIME_ENGINE_CONTRACT", "7", "DOC_DEV"),
    ("DOC-TOOL_CATALOG", "7", "DOC_DEV"),
    ("DOC-TRACEABILITY", "7", "DOC_DEV"),
]


def ledger_path(stem, folder, kind="claims"):
    return os.path.join(EXT, folder, f"{stem}_{kind}.csv")


def read_rows(path):
    """CSV records (quoted newlines safe) without the #END record."""
    with open(path, encoding="utf-8", newline="") as fh:
        recs = list(csv.reader(fh))
    if recs and recs[-1] and recs[-1][0].strip() == "#END" and len(recs[-1]) == 1:
        recs = recs[:-1]
    hdr, data = recs[0], recs[1:]
    return hdr, [dict(zip(hdr, r)) for r in data if r]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def h(s):
    return hashlib.sha256(s.encode()).hexdigest()


def rel(path):
    return os.path.relpath(path, RUN)

# verifier lines graded against a superseded attempt: (shard, ledger)
SUPERSEDED = {("DOC67", "DOC-ADDING_A_TOOL")}
