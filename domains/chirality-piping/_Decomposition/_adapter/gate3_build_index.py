#!/usr/bin/env python3
"""Build the dense retrieval index with length-sorted batching (3.6x faster).

Wraps tools/retrieval/build_source_index.py WITHOUT modifying it: monkeypatches
its module-global `encode_texts` with a length-sorted variant, then calls the
tool's own main() so all BM25 / SQLite catalog / meta.json logic runs unchanged.

Why: fastembed pads every batch to its longest member. With the piping corpus
(21,912 short LEDGER_ATOM chunks interleaved with long SECTION_NODE /
MARKDOWN_SECTION chunks, p95 ~2k-5k chars), almost every unsorted batch contains
a long chunk, so the short atoms are all computed at the 512-token cap. Sorting
texts by length before batching makes batches length-homogeneous: short batches
run fast, only genuinely-long batches pay the long cost. Measured on this
machine (M3, 16GB): unsorted 2.6/s (~4h) vs sorted 9.6/s (~63 min), 3.6x.

The embeddings are IDENTICAL to the unsorted build — each vector is scattered
back to its original chunk position, so embeddings.npy[i] still corresponds to
chunk i in chunk_id order (the order build_source_index.main writes into
index_rows). CoreML/GPU was benchmarked and gives no speedup (bge-base ops fall
back to CPU under onnxruntime's CoreML EP); the win is batching, not the device.

Usage:  python3 _adapter/gate3_build_index.py <SNAPSHOT_DIR> [--batch N]
Run with cwd = MONOREPO_ROOT.
"""
from __future__ import annotations
import sys
from pathlib import Path

MONO = Path.cwd()
sys.path.insert(0, str(MONO / "tools/retrieval"))
import build_source_index as B  # noqa: E402
import numpy as np  # noqa: E402


def encode_texts_sorted(texts, model_name, dim, batch):
    from fastembed import TextEmbedding
    model = TextEmbedding(model_name=model_name)
    order = sorted(range(len(texts)), key=lambda i: len(texts[i]))
    embs = np.empty((len(texts), dim), dtype=np.float32)
    written = 0
    for pos, vec in zip(order, model.embed([texts[i] for i in order], batch_size=batch)):
        v = np.asarray(vec, dtype=np.float32)
        if v.shape[0] != dim:
            raise RuntimeError(f"unexpected dim {v.shape[0]} (expected {dim})")
        embs[pos] = v
        written += 1
        if written % 2000 == 0:
            print(f"      {written:,}/{len(texts):,}", flush=True)
    if written != len(texts):
        raise RuntimeError(f"embedded {written} != {len(texts)}")
    return embs


def main():
    snap = sys.argv[1]
    batch = "128"
    for a in sys.argv[2:]:
        if a.startswith("--batch"):
            batch = a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]
    B.encode_texts = encode_texts_sorted  # monkeypatch (tool file untouched)
    sys.argv = ["build_source_index.py", "--snapshot", snap, "--force", "--batch", batch]
    return B.main()


if __name__ == "__main__":
    raise SystemExit(main())
