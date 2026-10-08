"""I100 B1 SC: PY's harness pins for 07n (I-PY's lane): edits tests/test_retained_precision_contract.py in place.
Usage: pin_py_07n.py <tests/test_retained_precision_contract.py>"""
import sys

p = sys.argv[1]
t = open(p).read()


def rep(a, b):
    global t
    assert t.count(a) == 1, a[:80]
    t = t.replace(a, b)


rep('''    assert result["classifications"] == fixture["expected_classifications"]
    # U7 (07i): 18 entries are eligible''', '''    # 07n (B1 SC): an admitted rewrite that changes the classes (a case no longer selected, a row added or removed)
    # states its own `expected_classifications`, which the three readers agree on; otherwise the base's.
    assert result["classifications"] == entry.get("expected_classifications", fixture["expected_classifications"])
    # U7 (07i): 18 entries are eligible''')
rep('''def test_snapshot_07_counts_and_entry_format():
    """Snapshot 07m: 07l plus''', '''def test_snapshot_07_counts_and_entry_format():
    """Snapshot 07n (B1 SC) appends to 07m only (`test_snapshot_07n_appends_only_and_states_every_read` pins its
    part); 07m's own slices below are unchanged. Snapshot 07m: 07l plus''')
rep('''    assert (len(c["cases"]), len(c["mutations"]), len(c["must_pass"])) == (17, 294, 28)
    assert set(c) == {"version", "provenance", "arithmetic", "cases", "mutations", "must_pass", "d37"}
    entries = c["mutations"] + c["must_pass"]''', '''    assert (len(c["cases"]), len(c["mutations"]), len(c["must_pass"])) == (26, 534, 78)
    assert set(c) == {"version", "provenance", "arithmetic", "cases", "mutations", "must_pass", "d37"}
    entries = c["mutations"][:294] + c["must_pass"][:28]''')
rep('''    assert all(set(e) <= {"id", "base", "edits", "invocation_edits", "after_rehash", "rehash", "expected", "expected_by_reader", "expected_eligibility"} for e in entries)
    assert all(("expected_eligibility" in e) == (e in c["must_pass"]) for e in entries)
    eligible = lambda items, key: sum(item[key]["numerical_eligible"] for item in items)
    assert (eligible(c["cases"], "expected"), eligible(c["must_pass"], "expected_eligibility")) == (15, 18)''', '''    assert all(set(e) <= {"id", "base", "edits", "invocation_edits", "after_rehash", "rehash", "expected", "expected_by_reader", "expected_eligibility"} for e in entries)
    assert all(("expected_eligibility" in e) == (e in c["must_pass"]) for e in entries)
    eligible = lambda items, key: sum(item[key]["numerical_eligible"] for item in items)
    assert (eligible(c["cases"][:17], "expected"), eligible(c["must_pass"][:28], "expected_eligibility")) == (15, 18)''')
rep('''    assert [e["id"] for e in c["must_pass"][24:]] == l0(["isolated_estimate_uncoupled"]) + l0(["isolated_translation_stop"])
    assert {e["base"] for e in c["mutations"][278:286] + c["must_pass"][24:]} == {f"u8_l0_isolated_node_{mode}" for mode in L0_PINS}''', '''    assert [e["id"] for e in c["must_pass"][24:28]] == l0(["isolated_estimate_uncoupled"]) + l0(["isolated_translation_stop"])
    assert {e["base"] for e in c["mutations"][278:286] + c["must_pass"][24:28]} == {f"u8_l0_isolated_node_{mode}" for mode in L0_PINS}''')
rep('''    assert [e["id"] for e in c["mutations"][286:]] == B6_07M_IDS
    assert {e["base"] for e in c["mutations"][286:]} == {O_BASE, P_BASE}''', '''    assert [e["id"] for e in c["mutations"][286:294]] == B6_07M_IDS
    assert {e["base"] for e in c["mutations"][286:294]} == {O_BASE, P_BASE}''')
rep('''    assert [e["id"] for e in c["must_pass"] if "not_required" in statuses(e)] == ["not_required_second_case_checks_passed"]''',
    '''    assert [e["id"] for e in c["must_pass"][:28] if "not_required" in statuses(e)] == ["not_required_second_case_checks_passed"]''')
rep('''    assert [f["id"] for f in c["cases"] if f["provenance"] != SYNTHETIC_PROVENANCE] == [f"u8_l0_isolated_node_{mode}" for mode in L0_PINS]''',
    '''    assert [f["id"] for f in c["cases"][:17] if f["provenance"] != SYNTHETIC_PROVENANCE] == [f"u8_l0_isolated_node_{mode}" for mode in L0_PINS]''')
open(p, "w").write(t)
print("patched")

t2 = open(p).read()
t2 += '''

# ---------------------------------------------------------------------------------------------
# Snapshot 07n (B1 SC, I100; R/BRIEFS/B1_SC.md; PLAN_v2 §2.5), appended to 07m: W-C2's two producer-solved
# bases, `d38_beside_selected`, the out-of-order-authored and SF-2 successors, and 290 entries. Every new
# entry states its bound expectation (per reader only in a declared class: Rust's own raw G7 code where
# Python and TS share one; B1_SC items 12-14), and its unbound and transport reads: `expected_unbound`
# (or, for a per-reader entry, `expected_unbound_by_reader`) and `expected_transport`, each "pass"
# (admitted, not eligible) or a gate and code. An admitted rewrite that changes the classes states its own
# `expected_classifications`. Detail texts are not pinned.
# ---------------------------------------------------------------------------------------------
N07_W_C2 = {"sparse_interactive": ("7922e3e5278d0d87dc5faf79dfbc1f2a384899e97df306cc742355cdacdb6269", "cccb9664e1c58f0582348df3348d8b6e0b0941bcb0294a5b351a4d092ed18886"),
            "dense_scrutiny": ("f2800bd4f2b4c90217918a6e1287f98305a1b6b07893295b5790f387c075d3a3", "612e23ca4b90604b3d2351fd7465d2e3cefb0f3fbb36bdea39efaa82a68bc07a")}
# PP `retained_facade_tests.rs` REVERSED_PINNED, CBA_PINNED and AA2_PINNED: (receipt sha256, successor bytes sha256).
N07_PP_PINNED = {
    "cause_milestone_reversed_sparse_interactive": ("b79f691a4a899e3ed4a7d13957f74d4c4ee7430ee3062396214261144cbabd82", "93aa043538bbc01e0a7bcef4e381f88468edfd6792769b7041d7f6483ad959b1"),
    "cause_milestone_reversed_dense_scrutiny": ("c6b03683c8a2591f4d59429407608a6aafd0abf25663c7d771de60f221135832", "b70edc6d002c92692f00a247702353f79e6410acf17eb385b3d2c2500ca76d8e"),
    "sf2_c_b_a_sparse_interactive": ("863d692fa90d450240cbfacec1628937b8ccc9af2396637d4f913cc0bc416e80", "ea9a484657ca3de9a831a737b6a682966cc4b1a8783114b26298f34571cc7ebb"),
    "sf2_c_b_a_dense_scrutiny": ("7aeecbac57426a2104c3b9f958862daf3e9b2c0f00582599c0210121681db6a1", "c719bd8d3281d3bd3c0a731e8ba5ede8901938d10634db8078c6f6fa96d0b6d8"),
    "sf2_a_a2_sparse_interactive": ("41f330856d4c6e94e2e1308fcd467818604c8f7e999ce499c8f3b49e26ef0d56", "529233eb989aca3553bdedfc9d1813ab3287675748ff076c27cb024c2b7fef63"),
    "sf2_a_a2_dense_scrutiny": ("30001ccf42ad12acd9dbb458392fee514946c1a52aa0d4e5f0b20bde5b09ea71", "f4075cdc80eff27099a28f787cec07080b745eca2d598eb3381a84ec03964176"),
}
N07_BASES = ["w_c2_sparse_interactive", "w_c2_dense_scrutiny", "d38_beside_selected"] + list(N07_PP_PINNED)
N07_KEYS = {"id", "base", "edits", "invocation_edits", "after_rehash", "rehash", "expected", "expected_by_reader", "expected_eligibility",
            "expected_classifications", "expected_unbound", "expected_unbound_by_reader", "expected_transport"}


def _n07_entries():
    c = corpus()
    return c["mutations"][294:] + c["must_pass"][28:]


def test_snapshot_07n_appends_only_and_states_every_read():
    c = corpus()
    assert [x["id"] for x in c["cases"][17:]] == N07_BASES
    assert (len(c["mutations"]) - 294, len(c["must_pass"]) - 28) == (240, 50)
    new = _n07_entries()
    assert all(set(e) <= N07_KEYS and e["rehash"] == "all" and "after_rehash" not in e for e in new)
    assert all(("expected_eligibility" in e) == (e in c["must_pass"]) and (e["expected"] == "pass") == (e in c["must_pass"]) for e in new)
    assert all("expected_transport" in e and ("expected_unbound" in e) != ("expected_unbound_by_reader" in e) for e in new)
    per = [e for e in new if "expected_by_reader" in e]
    assert len(per) == 45 and all("expected_unbound_by_reader" in e for e in per)
    # The declared class only: Python and TS share the expectation, Rust's raw code differs, all at G7, and the
    # unbound read is the same raw read per reader.
    assert all(e["expected_by_reader"]["python"] == e["expected_by_reader"]["typescript"] == e["expected"] != e["expected_by_reader"]["rust"]
               and e["expected"]["gate"] == e["expected_by_reader"]["rust"]["gate"] == "G7" and e["expected_unbound_by_reader"] == e["expected_by_reader"] for e in per)
    assert sum("expected_classifications" in e for e in c["must_pass"][28:]) == 16
    eligible = lambda items, key: sum(item[key]["numerical_eligible"] for item in items)
    assert (eligible(c["cases"], "expected"), eligible(c["must_pass"], "expected_eligibility")) == (19, 46)
    entries = c["mutations"] + c["must_pass"]
    assert len({e["id"] for e in entries}) == len(entries) == 612


def _n07_read(read, source):
    try:
        result = read(deepcopy(source))
    except rp.RetainedPrecisionError as error:
        return {"gate": error.gate, "code": error.code}
    assert not result["invocation_bound"] and not result["numerical_eligible"]
    return "pass"


@pytest.mark.parametrize("entry", corpus()["mutations"][294:] + corpus()["must_pass"][28:], ids=lambda x: x["id"])
def test_snapshot_07n_unbound_and_transport_reads(entry):
    """07n: each entry's unbound read (no invocation) and transport read, as the corpus states them for Python."""
    fixture = next(f for f in corpus()["cases"] if f["id"] == entry["base"])
    source, _ = apply_entry(fixture, entry)
    unbound = entry["expected_unbound"] if "expected_unbound" in entry else entry["expected_unbound_by_reader"]["python"]
    assert _n07_read(rp.validate_retained_precision, source) == unbound
    assert _n07_read(rp.validate_retained_precision_transport, source) == entry["expected_transport"]


def test_snapshot_07n_bases_are_the_pinned_successors_and_the_d38_derivation():
    """07n's producer-solved bases are D-U6-5 copies: W-C2's committed fixtures (I85, I3), and the successors PP's
    own tests pin (receipt and bytes sha256); `d38_beside_selected` is W-C2 sparse rewritten by DESIGN_v2 §2's
    derivation (the records script's steps), resealed. Each passes with its invocation as stated, and is never
    eligible without it."""
    import hashlib
    c = corpus()
    bases = {x["id"]: x for x in c["cases"][17:]}
    for mode, (file_sha, receipt_sha) in N07_W_C2.items():
        base = bases[f"w_c2_{mode}"]
        raw = (ROOT / base["provenance"]["fixture"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == base["provenance"]["fixture_sha256"] == file_sha
        doc = json.loads(raw)
        assert doc["id"] == base["id"] and all(json.dumps(base[k]) == json.dumps(doc[k]) for k in ("source", "invocation"))
        assert receipt_sha is None or base["source"]["retained_precision"]["receipt_sha256"] == receipt_sha
    for bid, (receipt_sha, bytes_sha) in N07_PP_PINNED.items():
        p = bases[bid]["provenance"]
        assert (bases[bid]["source"]["retained_precision"]["receipt_sha256"], p["receipt_sha256"], p["successor_bytes_sha256"]) == (receipt_sha, receipt_sha, bytes_sha)
        assert p["kind"] == "producer_solved" and p["solver_mode"] == bases[bid]["invocation"]["solver_mode"]
    w = bases["w_c2_sparse_interactive"]
    body = w["source"]["retained_precision"]["body"]
    stages = dict.fromkeys(rp.STAGE_ORDER, "not_entered")
    stages.update(preparation="completed", native="failed")
    after = body["cases"][0]["run"]["invocation_after"]
    a1 = B + ["product_attempts", 1]
    derivation = [
        _set(B + ["cases", 2, "run"], None),
        _set(B + ["cases", 2, "reason"], {"code": "source_unavailable", "phase": "preparation", "cause": {"kind": "prepared_product_failure", "product_attempt_ref": 1}}),
        _set(a1 + ["run_ref"], None), _set(a1 + ["proof"], None), _set(a1 + ["stages"], stages),
        _set(a1 + ["result"], {"kind": "unavailable", "error": {"kind": "capture", "cause": {"kind": "origin", "cause": {"kind": "capacity"}}}}),
        _set(B + ["builds"], [b for b in body["builds"] if b["origin"]["run"] != 1]),
        _set(B + ["calls", 0, "owner_refs"], [{"kind": "case", "index": 0}]), _set(B + ["calls", 0, "run_refs"], [0]),
        _set(B + ["calls", 0, "source_refs"], [0]), _set(B + ["calls", 0, "invocation_after"], after),
        _set(B + ["groups", 0, "source_refs"], [0]), _set(B + ["work", "charged"], after),
        _set(B + ["work", "execution_order"], [{"kind": "case", "index": 0}]),
    ]
    derived = apply_mutation(w["source"], {"edits": derivation, "rehash": "all"})
    assert json.dumps(derived, sort_keys=True) == json.dumps(bases["d38_beside_selected"]["source"], sort_keys=True)
    assert bases["d38_beside_selected"]["provenance"] == SYNTHETIC_PROVENANCE
    for base in bases.values():
        result = rp.validate_retained_precision(deepcopy(base["source"]), deepcopy(base["invocation"]))
        assert {k: result[k] for k in ("invocation_bound", "numerical_eligible", "standing")} == base["expected"], base["id"]
        assert result["classifications"] == base["expected_classifications"], base["id"]
        assert rp.validate_retained_precision(deepcopy(base["source"]))["numerical_eligible"] is False
'''
open(p, "w").write(t2)
print("appended")
