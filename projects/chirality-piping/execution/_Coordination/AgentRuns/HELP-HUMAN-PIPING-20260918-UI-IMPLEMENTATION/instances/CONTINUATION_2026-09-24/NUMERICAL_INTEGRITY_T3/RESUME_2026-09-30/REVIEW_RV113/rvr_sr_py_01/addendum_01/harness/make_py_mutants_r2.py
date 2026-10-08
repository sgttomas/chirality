"""RV113 (RV-R): a mutant schema for SR-PY repair 02 (2843a59a16), in the reviewer's own copy (WT/rv113/py2-mut).

Each mutant is an environment-guarded edit: `_mx("Pnn")` is true only when RV113_MUT == "Pnn"; with RV113_MUT unset the
copy behaves as the head (a control run checks it). Each anchor must match exactly once.
Usage: python make_py_mutants_r2.py <P root of the mutant copy> <manifest out>
"""
import json
import sys

root = sys.argv[1]
RP = f"{root}/core/analysis_runs/retained_precision.py"
GUARD = 'import os as _rv113_os\n\n\ndef _mx(i):\n    return _rv113_os.environ.get("RV113_MUT") == i\n\n'
text = open(RP).read()
M = []


def sub(old, new, mid, item, desc):
    global text
    assert text.count(old) == 1, (mid, text.count(old), old[:90])
    text = text.replace(old, new)
    M.append({"id": mid, "item": item, "description": desc})


def also(mid, item, desc):
    M.append({"id": mid, "item": item, "description": desc})


# ---------------------------------------------------------------- item 1: G3 and the ordinary basis at G5
sub('''            _need(s["index"]==si and s["owner"]["kind"]=="case" and ci is not None and 0<=ci<len(cases) and ids[ci]==s["owner"]["case_id"],gate,"COVERAGE_MISMATCH")''',
    '''            _need((_mx("P01") or s["index"]==si) and (_mx("P02") or s["owner"]["kind"]=="case") and ci is not None and (_mx("P03") or 0<=ci<len(cases)) and (_mx("P04") or ids[ci]==s["owner"]["case_id"]),gate,"COVERAGE_MISMATCH")''',
    "P01", "1 (f)", "G3: a source's index at its position dropped")
also("P02", "1 (f)", "G3: the source owner's kind dropped (I91's F-src-kind)")
also("P03", "1 (f)", "G3: the owner's case index range dropped (an IndexError then reaches the fallback)")
also("P04", "1 (f)", "G3: the owner's case id dropped")
sub('''            _need(mb["index"]==mi and len(set(mb["case_indices"]))==len(mb["case_indices"]) and all(x<len(cases) for x in mb["case_indices"]),gate,"COVERAGE_MISMATCH")''',
    '''            _need((_mx("P05") or mb["index"]==mi) and (_mx("P06") or len(set(mb["case_indices"]))==len(mb["case_indices"])) and (_mx("P07") or all(x<len(cases) for x in mb["case_indices"])),gate,"COVERAGE_MISMATCH")''',
    "P05", "1 (f)", "G3: a material basis's index dropped")
also("P06", "1 (f)", "G3: case_indices unique dropped")
also("P07", "1 (f)", "G3: case_indices in range dropped")
sub('''        fail(basis is not None and i in basis["case_indices"])''',
    '''        fail(_mx("P08") or basis is not None and (_mx("P09") or i in basis["case_indices"]))''',
    "P08", "1 G5", "G5 ordinary: the ordinary attempt's basis reference dropped")
also("P09", "1 G5", "G5 ordinary: the basis need only resolve")
# ---------------------------------------------------------------- item 2: G8 model scope
sub('''    need(model.get("schema_version") in ("0.1.0", "0.2.0", "0.3.0") and model.get("pressure_contract") is None and model.get("combinations", []) == [], "INVOCATION_MISMATCH")
    need(model.get("components", []) == [] and "reference_configurations" not in model, "INVOCATION_MISMATCH")''',
    '''    need(model.get("schema_version") in ("0.1.0", "0.2.0", "0.3.0") and ((not model.get("pressure_contract")) if _mx("P11") else model.get("pressure_contract") is None)
         and ((not model.get("combinations")) if _mx("P12") else (model.get("combinations", []) == [] or (_mx("P14") and model.get("combinations", 1) is None))), "INVOCATION_MISMATCH")
    need(((not model.get("components")) if _mx("P13") else (model.get("components", []) == [] or (_mx("P14") and model.get("components", 1) is None))) and (_mx("P10") or "reference_configurations" not in model), "INVOCATION_MISMATCH")''',
    "P10", "2 (g)", "G8: reference_configurations check dropped")
also("P11", "2 (g)", "G8: pressure_contract back to the falsiness test")
also("P12", "2 (g)", "G8: combinations back to `not model.get(...)`")
also("P13", "2 (g)", "G8: components back to `not model.get(...)`")
also("P14", "2 (g)", "G8: combinations and components may be null")
# ---------------------------------------------------------------- item 3: C2's cause table
sub('''        if cause is not None and cause.get("kind") != "prepared_product_failure":''',
    '''        if not _mx("P15") and cause is not None and (_mx("P34") or cause.get("kind") != "prepared_product_failure"):''',
    "P15", "3 C2", "the whole C2 table dropped")
sub('''                fail(phase == "preparation" and code == "source_unavailable" and run is None
                     and c.get("source_decline") is not None and _same(c["source_decline"]["error"], cause["error"]))''',
    '''                fail((_mx("P16") or phase == "preparation") and (_mx("P17") or code == "source_unavailable") and (_mx("P18") or run is None)
                     and c.get("source_decline") is not None and (_mx("P19") or _same(c["source_decline"]["error"], cause["error"])))''',
    "P16", "3 C2", "source_error: phase dropped")
also("P17", "3 C2", "source_error: code dropped")
also("P18", "3 C2", "source_error: no Run dropped")
also("P19", "3 C2", "source_error: the decline's error equality dropped")
sub('''                fail(phase == "receipt" and code in RECEIPT_FAILURE_CODES)''',
    '''                fail((_mx("P20") or phase == "receipt") and (_mx("P21") or code in (RECEIPT_FAILURE_CODES[:2] if _mx("P22") else RECEIPT_FAILURE_CODES)))''',
    "P20", "3 C2", "receipt_failure: phase dropped")
also("P21", "3 C2", "receipt_failure: code set dropped")
also("P22", "3 C2", "receipt_failure: invocation_not_representable removed from the set")
sub('''                fail(phase == "facade" and code == "facade_certificate" and run is not None and run["kernel_terminal"]["kind"] == "selected"
                     and _same(cause["owner_ref"], {"kind": "case", "index": i}))''',
    '''                fail((_mx("P23") or phase == "facade") and (_mx("P24") or code == "facade_certificate") and (_mx("P25") or run is not None and run["kernel_terminal"]["kind"] == "selected")
                     and (_mx("P26") or _same(cause["owner_ref"], {"kind": "case", "index": i})))''',
    "P23", "3 C2", "facade_failure: phase dropped")
also("P24", "3 C2", "facade_failure: code dropped")
also("P25", "3 C2", "facade_failure: selected Run dropped")
also("P26", "3 C2", "facade_failure: owner_ref dropped")
sub('''                fail(phase in ("routing", "preparation") and run is None and code == PRECONDITION_CODES.get(cause["precondition"]))''',
    '''                fail((_mx("P27") or phase in ("routing", "preparation")) and (_mx("P28") or run is None) and (code in set(PRECONDITION_CODES.values()) if _mx("P29") else code == PRECONDITION_CODES.get(cause["precondition"])))''',
    "P27", "3 C2", "unavailable_precondition: phase dropped")
also("P28", "3 C2", "unavailable_precondition: no Run dropped")
also("P29", "3 C2", "unavailable_precondition: keying replaced by the set of four codes")
sub('''                fail(phase == "kernel" and run is not None and code == "kernel_" + run["kernel_terminal"]["kind"]
                     and _same(cause, run["kernel_terminal"]["reason"]))''',
    '''                fail((_mx("P30") or phase == "kernel") and (_mx("P31") or run is not None) and (_mx("P32") or code == "kernel_" + run["kernel_terminal"]["kind"])
                     and (_mx("P33") or _same(cause, run["kernel_terminal"]["reason"])))''',
    "P30", "3 C2", "kernel: phase dropped")
also("P31", "3 C2", "kernel: a Run present dropped")
also("P32", "3 C2", "kernel: code dropped")
also("P33", "3 C2", "kernel: cause equal to the terminal's reason dropped")
also("P34", "3 C2", "the table also applied to prepared_product_failure causes")
# ---------------------------------------------------------------- item 4: the transport header's gate
sub('''        error=RetainedPrecisionError("G7" if code in ("SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID","SOURCE_PREVIEW_PHYSICS_INVALID") else "G2",code);error.detail=text''',
    '''        error=RetainedPrecisionError("G7" if _mx("P35") or (not _mx("P36") and code in ("SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID","SOURCE_PREVIEW_PHYSICS_INVALID")) else "G2",code);error.detail=text''',
    "P35", "4 header", "every transport base failure at G7 (the old label)")
also("P36", "4 header", "every transport base failure at G2 (the metadata check's too)")

lines = text.split("\n")
k = next(i for i, l in enumerate(lines) if (l.startswith("import ") or l.startswith("from ")) and "__future__" not in l)
lines.insert(k, GUARD.rstrip("\n") + "\n")
open(RP, "w").write("\n".join(lines))
json.dump(M, open(sys.argv[2], "w"), indent=1)
print(len(M), "mutants")
