"""Add-on L slot rule: rebuild each expected postimage from the committed preimage
(git show <base>:<path>) by changing only the Current State line, the Last Updated
line and appending exactly one History line; compare byte-for-byte with the file.
Usage: check_addon_L_slots.py <base commit> <D>"""
import subprocess, sys, hashlib
base, D = sys.argv[1], sys.argv[2]
S = "projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/"
DELS = {"DEL-02-03_Receipts_ledger_parser_per_loop_grammars": "6f94c04f79b678082b0407f93ec9c898d988c2693c0d1e19791f5cff985cf06f",
        "DEL-02-08_Work_graph_parser": "4341d6b2e192b3ada04a5897de94245639980d0d2048b2b8cb3202771dfe04fe",
        "DEL-02-09_MEMORY_run_index_parser": "e67be5871d8cd0f2a02e96c76418d5e161be5d17c7e5e44c7577bf829e171056"}
HIST = (f"- {D} — State set to IN_PROGRESS (WORKING_ITEMS at actual D-PEC-106 X1 production start; semantic step "
        f"skipped under Root docs/SPEC.md §3.3; ruling, preflights and act evidence in execution/_Coordination/X1_FIXTURES_{D}/)")
bad = 0
for d, want_pre in DELS.items():
    p = S + d + "/_STATUS.md"
    pre = subprocess.run(["git", "show", f"{base}:{p}"], capture_output=True, check=True).stdout
    ok_pre = hashlib.sha256(pre).hexdigest() == want_pre
    lines = pre.decode("utf-8").split("\n")
    assert lines[-1] == ""
    n_state = sum(l == "**Current State:** INITIALIZED" for l in lines)
    out = ["**Current State:** IN_PROGRESS" if l == "**Current State:** INITIALIZED" else
           (f"**Last Updated:** {D}" if l.startswith("**Last Updated:** ") else l) for l in lines[:-1]]
    exp = ("\n".join(out + [HIST]) + "\n").encode("utf-8")
    act = open(p, "rb").read()
    ok = ok_pre and n_state == 1 and exp == act
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'} {d}: preimage {'as tabled' if ok_pre else 'DIFFERS'}; expected postimage {hashlib.sha256(exp).hexdigest()} actual {hashlib.sha256(act).hexdigest()}")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {3-bad}/3")
sys.exit(1 if bad else 0)
