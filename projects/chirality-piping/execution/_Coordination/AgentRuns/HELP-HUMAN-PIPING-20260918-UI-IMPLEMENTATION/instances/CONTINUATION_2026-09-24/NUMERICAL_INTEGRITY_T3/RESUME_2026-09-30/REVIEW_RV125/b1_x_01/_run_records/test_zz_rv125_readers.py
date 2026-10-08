"""RV125 (RV-X of PR-B1; disposable archive copy only, never committed): the Python reader on the
successors and invocations RV125's Rust harness wrote (W-C2 and W-C2 permuted c, a, b; both modes),
bound, unbound and transport. Writes one JSON line per check to RV125_PY_OUT."""
import json
import os

import pytest

from core.analysis_runs import retained_precision as rp

PREFIX = os.environ.get("RV125_OUT", "")
OUT = os.environ.get("RV125_PY_OUT", "")


def show(call):
    try:
        r = call()
        return {"ok": True, "bound": r.get("invocation_bound"), "eligible": r.get("numerical_eligible"), "standing": r.get("standing"),
                "classes": len(r.get("classifications", []))}
    except Exception as error:  # noqa: BLE001 - recorded, then asserted
        return {"ok": False, "type": type(error).__name__, "gate": getattr(error, "gate", None), "code": getattr(error, "code", None), "message": str(error)[:300]}


@pytest.mark.parametrize("label", ["w_c2", "w_c2_cab"])
@pytest.mark.parametrize("mode", ["sparse_interactive", "dense_scrutiny"])
def test_rv125_py_reader(label, mode):
    source = json.load(open(f"{PREFIX}.{label}_{mode}.source.json"))
    invocation = json.load(open(f"{PREFIX}.{label}_{mode}.invocation.json"))
    row = {"label": label, "mode": mode,
           "py_bound": show(lambda: rp.validate_retained_precision(source, invocation)),
           "py_unbound": show(lambda: rp.validate_retained_precision(source)),
           "py_transport": show(lambda: rp.validate_retained_precision_transport(source))}
    with open(OUT, "a") as handle:
        handle.write(json.dumps(row) + "\n")
    assert row["py_bound"]["ok"], row
