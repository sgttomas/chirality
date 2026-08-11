#!/usr/bin/python3
from pathlib import Path
import sys

root = Path(sys.argv[1])
files = sorted(p for p in root.rglob("*") if p.is_file())
sentinels = sum(1 for p in files if "<<UNFILLED:" in p.read_text(encoding="utf-8"))
total = sum(p.stat().st_size for p in files)
print(f"file_count={len(files)} byte_total={total} filled={len(files)-sentinels} remaining={sentinels} native_context_telemetry=unavailable")
