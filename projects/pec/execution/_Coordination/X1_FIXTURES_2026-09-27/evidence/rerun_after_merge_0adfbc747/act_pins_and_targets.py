"""After a merge of origin/main: every act pin (12) and every target (35) at HEAD, the three
add-on L postimages, write_status.sh, the hold register and script: as tabled. Read-only."""
import hashlib, importlib.util, sys
from pathlib import Path
rr = Path(sys.argv[1])
s = importlib.util.spec_from_file_location("a", rr / "apply_x1p.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
h = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
bad = 0
for rel, want in m.PINNED.items():
    ok = h(rel) == want; bad += not ok; print(("OK   " if ok else "FAIL ") + "pin " + rel)
for rel, (_, post) in m.TARGETS.items():
    ok = h(rel) == post; bad += not ok; print(("OK   " if ok else "FAIL ") + "target postimage " + rel)
S = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
extra = {S + "DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_STATUS.md": "84b238d263c6272f9e4845ad7c2804cf871bd417e40b161026e0fc91bf4c9b5e",
         S + "DEL-02-08_Work_graph_parser/_STATUS.md": "bfc995867fa2c87fb7c94acaf95c64fbc42aade174ac77c5c92ace14e3451ff6",
         S + "DEL-02-09_MEMORY_run_index_parser/_STATUS.md": "50bc10f4135b49e669921ee7d733b5e2bda0c4bcf541c7b2f8fb5ce8f034372a",
         "tools/scaffolding/write_status.sh": "0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3",
         "projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv": "f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc",
         "projects/pec/execution/_Scripts/pec_reliance_hold.py": "b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e"}
for rel, want in extra.items():
    ok = h(rel) == want; bad += not ok; print(("OK   " if ok else "FAIL ") + rel)
n = len(m.PINNED) + len(m.TARGETS) + len(extra)
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
