"""I107 SB round 3: U3's reviewed delta table (delta_reviewed_u3.json) for I65's delta tool, from a dry run's inventory
(main ba500defa4, B1 + PR-N as merged -> U3's code commit 8a12de28db). Fingerprints are the tool's own, computed on this
candidate (no carried fingerprint, so RV124 C-N1 does not arise). An entry is written only for a hunk attributed to the
legacy pressure retirement by one of these checks (comments ignored throughout; tokens: identifiers, numbers,
punctuation, and each string literal as one token):
  T  test-only code: the deleted file historical_pressure_reference.rs, declared only as `#[cfg(test)] mod` at the base;
     or a removed `#[cfg(test)] if crate::historical_pressure_reference::active() { return/continue; }` statement (the
     named historical tests' bypass; compiled into the lib test binary only).
  R  a pure removal: no added code, and the removed code names an identifier the commit retired from that file (present
     in the file's code at the base, absent at the candidate), e.g. PressureThrustLoad, pressure_membrane, membrane_radius,
     or from the enclosing fn (present in the fn at the base, absent from the same-named fn at the candidate: a local or
     parameter such as `include_pressure_longitudinal`), or a local binding the fn lost (bound by `let` or as a parameter at
     the base, bound nowhere in the candidate's fn, any remaining spelling only a field access `.name`, e.g. `pressure`).
  A  removed call arguments `false, false` to append_{endpoint,station}_stress_results, whose two removed parameters are
     include_pressure and include_pressure_longitudinal (both false here, so the removed rows were never appended).
  S  a subtractive edit: the token diff only deletes, and every deleted run names a retired identifier, or is
     punctuation, or is a literal argument (`None`, `false`) of a call whose callee lost at least that many parameters,
     each named for pressure (e.g. `, &pressure_thrust_loads`, `+ if include_pressure_longitudinal {..}`, or the `None`
     formerly passed as recover_section_stress's `pressure`).
  H  H-1: the only replacement turns a run naming a retired identifier into the literal `0.0` (`axial + 0.0`).
  W  wording: only string literals differ, and each new literal's format placeholders are the old literal's
     (a text correction: no argument, call or control flow changes).
  F  an added refusal, each checked by name: [F1] the RETIRED_MODE/RETIRED_VERSION consts; [F2] the
     PRESSURE_MODEL_REAUTHOR_REQUIRED branch for exactly 1.0.0/legacy_pressure_v1; [F3] the legacy-primitive refusal
     widened from nonzero values (and a #[cfg(test)] bypass) to every value; [F4] G11's joint refusals, which only push
     blocking diagnostics and `continue`.
  Z  the expansion-joint pressure-thrust result count, now the constant 0.
  Q  a qualification-test hunk of the in-build profile re-pin: PINNED_RECORD and the challenge's W1/MAX phase bytes, each
     old value less exactly 800 (= 9 x 32 + 64 x 8), and the re-pin's doc comment.
The F checks run before S, H and W, so a refusal is never read as a subtractive edit.
Premise P0 for S, H and Z (behaviour): on every admitted model no primitive load has category or dimension "pressure"
(pressure_runtime.rs refuses one of any value without the exact contract, and EXACT_PRESSURE_REQUIRES_REGION with it;
validate_profile runs first on the one ordinary entry, and the source-receipt routes passed `&[]`). So, on every model
that reaches a solve, build_pressure_thrust_loads returned no load, pressure_for_pipe returned None, every removed
summand was +0.0 and every removed branch was not taken: the deleted terms were identities.
A hunk that fits none gets no entry, so the pass stops on it (5) or reads it (6).
Usage: python3 mk_delta_reviewed_u3.py <repo> <dry-run delta_inventory.json> <out json>"""
import collections, difflib, json, os, re, subprocess, sys
repo, inv_p, out_p = sys.argv[1:4]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*a, ok=False):
    r = subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env)
    if r.returncode and not ok: raise SystemExit(f"git {a}: {r.stderr}")
    return r.stdout if not r.returncode else None
inv = json.load(open(inv_p)); old, new = inv["old"], inv["new"]
TOK = re.compile(r'//[^\n]*|/\*.*?\*/|b?r(#*)"(?:.|\n)*?"\1|b?"(?:\\.|[^"\\])*"|\'(?:\\(?:x[0-9a-fA-F]{2}|u\{[0-9a-fA-F]+\}|.)|[^\\\'\n])\'(?![A-Za-z_])'
                 r"|[A-Za-z_][A-Za-z0-9_]*|\d[\d_]*(?:\.\d[\d_]*)?(?:[eE][+-]?\d+)?(?:_?[fiu]\d+)?|::|->|=>|&&|\|\||[=!<>]=|\.\.=?|\S", re.S)
def toks(lines):
    out = []
    for m in TOK.finditer("\n".join(lines)):
        t = m.group(0)
        if t.startswith("//") or t.startswith("/*"): continue
        out.append(t)
    return out
is_id = lambda t: re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", t) is not None
is_str = lambda t: t.startswith('"') or t.startswith('b"') or t.startswith("r") and '"' in t[:3] or t.startswith("br")
KW = {"if", "else", "let", "mut", "for", "in", "match", "return", "Some", "None", "true", "false", "ref", "move", "self", "Self", "pub", "fn", "use"}
code_lines = lambda ls: [l for l in ls if toks([l])]
_cache = {}
def hunks(rel):
    if rel in _cache: return _cache[rel]
    out, cur = {}, None
    for l in (git("diff", "-U0", old, new, "--", P + rel) or "").split("\n"):
        m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", l)
        if m:
            n, nc = int(m.group(3)), int(m.group(4) or 1)
            cur = out.setdefault(f"{n}-{n + nc - 1}" if nc else f"after {n}", ([], [], (int(m.group(1)), int(m.group(2) or 1)))); continue
        if cur is not None and l[:1] in "-+" and l[:1] and not l.startswith(("---", "+++")):
            (cur[0] if l[0] == "-" else cur[1]).append(l[1:])
    _cache[rel] = out; return out
_ids = {}
def file_ids(rev, rel):
    k = (rev, rel)
    if k not in _ids:
        t = git("show", f"{rev}:{P}{rel}", ok=True)
        _ids[k] = {x for x in toks(t.split("\n")) if is_id(x)} if t is not None else set()
    return _ids[k]
def retired(rel):
    """identifiers in the file's code at the base and not at the candidate (whole file, comments and strings excluded)"""
    return file_ids(old, rel) - file_ids(new, rel)
FN = re.compile(r"^\s*(pub(\([^)]*\))?\s+)?(const\s+)?(async\s+)?(unsafe\s+)?(extern\s+\"[^\"]*\"\s+)?fn\s+(\w+)")
def fn_spans(L):  # I65's delta-tool span rule (brace matching on code text)
    out = []
    cl_ = lambda l: re.sub(r"'(\\.|[^'\\])'", "''", re.sub(r'"(\\.|[^"\\])*"', '""', l)).split("//")[0]
    for i, l in enumerate(L):
        m = FN.match(l)
        if not m: continue
        depth, started, j = 0, False, i
        while j < len(L):
            c = cl_(L[j]); depth += c.count("{") - c.count("}")
            if "{" in c: started = True
            if started and depth <= 0: break
            if not started and c.rstrip().endswith(";"): break
            j += 1
        out.append((i + 1, j + 1, m.group(7)))
    return out
_fs = {}
def fn_text(rev, rel):
    k = (rev, rel)
    if k not in _fs:
        t = git("show", f"{rev}:{P}{rel}", ok=True); L = t.split("\n") if t is not None else []
        _fs[k] = (L, fn_spans(L))
    return _fs[k]
def fn_retired(rel, nl, minus_n):
    """identifiers in the fn enclosing the hunk at the base and absent from the same-named fn enclosing it at the candidate"""
    OL, OS = fn_text(old, rel); NL, NS = fn_text(new, rel)
    o0, oc = minus_n
    enc_o = [(a, b, n) for a, b, n in OS if oc and a <= o0 <= b]
    if not enc_o: return set(), None
    a, b, name = min(enc_o, key=lambda x: x[1] - x[0])
    n0 = int(nl.split()[-1]) if nl.startswith("after") else int(nl.split("-")[0])
    enc_n = [(c, d, n) for c, d, n in NS if n == name and c <= max(n0, 1) + (0 if not nl.startswith("after") else 1) and d >= n0]
    if not enc_n: return set(), name
    c, d, _ = min(enc_n, key=lambda x: x[1] - x[0])
    ids = lambda L: {x for x in toks(L) if is_id(x)}
    ot, nt = toks(OL[a - 1:b]), toks(NL[c - 1:d])
    def bound(T):
        out = set()
        for i, t in enumerate(T):
            if t == "let":
                j = i + 1 + (T[i + 1] == "mut")
                if j < len(T) and is_id(T[j]): out.add(T[j])
            if is_id(t) and i + 1 < len(T) and T[i + 1] == ":" and i > 0 and T[i - 1] in ("(", ","): out.add(t)
        return out
    lost_bind = {x for x in bound(ot) - bound(nt) if all(nt[i - 1] == "." for i, t in enumerate(nt) if t == x and i > 0)}
    return (ids(OL[a - 1:b]) - ids(NL[c - 1:d])) | lost_bind, name
def params(rev, rels, fn):
    for rel in rels:
        t = git("show", f"{rev}:{P}{rel}", ok=True)
        m = re.search(r"\bfn " + re.escape(fn) + r"\s*(?:<[^>]*>)?\(", t or "")
        if not m: continue
        i, d = m.end(), 1
        while d and i < len(t):
            d += {"(": 1, ")": -1}.get(t[i], 0); i += 1
        sig, out, depth, cur = t[m.end():i - 1], [], 0, ""
        for ch in sig:
            depth += {"<": 1, ">": -1, "(": 1, ")": -1, "[": 1, "]": -1}.get(ch, 0)
            if ch == "," and depth == 0: out.append(cur); cur = ""
            else: cur += ch
        out.append(cur)
        return [x.split(":")[0].strip().replace("mut ", "") for x in out if ":" in x]
    return None
def removed_params(rel, fn):
    rels = [rel, "core/product_physics/src/lib.rs", "core/loads/stress_recovery/src/lib.rs"]
    o, n = params(old, rels, fn), params(new, rels, fn)
    return [x for x in o if x not in n] if o is not None and n is not None else None
def callee_before(T, i):
    d = 0
    for j in range(i - 1, -1, -1):
        if T[j] == ")": d += 1
        elif T[j] == "(":
            if d == 0: return T[j - 1] if j and is_id(T[j - 1]) else None
            d -= 1
    return None
CFG_STMT = re.compile(r"# \[ cfg \( test \) \] if crate :: historical_pressure_reference :: active \( \) \{ (return|continue) ; \}")
def placeholders(s):
    return collections.Counter(re.findall(r"\{[^{}]*\}", s.replace("{{", "").replace("}}", "")))
need = inv["unreviewed"] + inv["unreviewed_qualification_tests"]
entries, refused = [], []
for r in need:
    rel, nl, cls = r["file"], r["new_lines"], r["class"]
    minus, plus, ostart = hunks(rel).get(nl, ([], [], (0, 0)))
    mt, pt = toks(minus), toks(plus)
    FRET, enc_fn = fn_retired(rel, nl, ostart) if rel.endswith(".rs") else (set(), None)
    RET = (retired(rel) | FRET) - KW   # keywords and literals are never "retired"
    ret_named = sorted({t for t in mt if is_id(t) and t in RET}, key=lambda t: (not re.search(r"(?i)pressure|thrust|membrane|hoop|internal_area", t), t))
    kind = why = None; extra = {}
    base = os.path.basename(rel)
    if rel.endswith("/historical_pressure_reference.rs") and not pt:
        decl = git("show", f"{old}:{P}core/product_physics/src/lib.rs").split("\n")
        at = [i for i, l in enumerate(decl) if re.fullmatch(r"\s*mod historical_pressure_reference;\s*", l)]
        if at and all(decl[i - 1].strip() == "#[cfg(test)]" for i in at) and git("show", f"{new}:{P}{rel}", ok=True) is None:
            kind, why = "T", (f"the deleted file (its {len(minus)} lines): declared only as `#[cfg(test)] mod historical_pressure_reference;` "
                              f"(base lib.rs:{at[0]}-{at[0] + 1}); compiled into the lib test binary only. It held the named historical tests' "
                              "scope that suspended the legacy-pressure and joint refusals")
    elif cls == "qualification-test":
        nums = lambda ls: [int(x.replace("_", "")) for l in ls for x in re.findall(r"\b\d{1,3}(?:_\d{3}){2,}\b", l)]
        mo, po = nums(minus), nums(plus)
        if mo and len(mo) == len(po) and all(a - b == 800 for a, b in zip(mo, po)):
            kind, why = "Q", (f"the in-build profile re-pin: {len(mo)} pinned phase values, each the old less exactly 800 B "
                              "(9 x 32 B for StressRecoveryResult, 64 x 8 B for DerivedSection; RV127 ADDENDUM_01 checked the atoms); "
                              "no binding, form or phase changes")
        elif not mt and not minus and all(l.strip().startswith("///") for l in plus):
            kind, why = "Q", "the re-pin's doc comment (no code)"
    elif not pt and mt and CFG_STMT.fullmatch(" ".join(mt)):
        kind, why = "T", ("a removed #[cfg(test)] statement: the named historical tests' bypass of this refusal "
                          "(crate::historical_pressure_reference::active(), whose module is deleted); normal builds never compiled it")
    elif not pt and mt:
        if ret_named:
            kind, why = "R", f"a removal on the retired pressure path; it names {len(ret_named)} identifier(s) the commit retired from {base}"
        elif [t for t in mt if t not in ","] == ["false", "false"]:
            t = git("show", f"{new}:{P}{rel}").split("\n"); a = int(nl.split()[-1])
            call = next((re.search(r"(append_(endpoint|station)_stress_results)\(", t[i]).group(1) for i in range(a - 1, max(a - 8, 0), -1)
                         if re.search(r"append_(endpoint|station)_stress_results\(", t[i])), None)
            o = git("show", f"{old}:{P}core/product_physics/src/lib.rs"); n_ = git("show", f"{new}:{P}core/product_physics/src/lib.rs")
            sig = lambda s, f: re.search(r"fn " + f + r"\((.*?)\)\s*\{", s, re.S).group(1) if f else ""
            if call:
                po_, pn_ = sig(o, call), sig(n_, call)
                gone = [p.split(":")[0].strip() for p in po_.split(",") if p.strip() and p.strip() not in [q.strip() for q in pn_.split(",")]]
                if gone == ["include_pressure", "include_pressure_longitudinal"]:
                    kind, why = "A", (f"the two `false` arguments of {call}'s removed parameters {gone}; with both false the "
                                      "removed pressure rows were never appended from this call")
    elif mt or pt:
        txt_m, txt_p = " ".join(mt), " ".join(pt)
        # the refusals are checked first (F), so a refusal is never read as a subtractive edit
        if True:
            if base == "pressure_runtime.rs" and not mt and re.fullmatch(r'const RETIRED_MODE : & str = "legacy_pressure_v1" ; const RETIRED_VERSION : & str = "1.0.0" ;', txt_p):
                kind, why = "F", "[F1] the retired contract's mode and version as consts, used only to refuse it by name ([F2])"
            elif base == "pressure_runtime.rs" and '"PRESSURE_MODEL_REAUTHOR_REQUIRED"' in pt and "legacy_pressure_v1" in txt_m:
                ok = ("declared == ( Some ( RETIRED_VERSION ) , Some ( RETIRED_MODE ) )" in txt_p and '"blocking"' not in txt_p
                      and "} else if declared != ( Some ( EXACT_VERSION ) , Some ( EXACT_MODE ) ) {" in txt_p)
                if ok:
                    kind, why = "F", ("[F2] the retired 1.0.0/legacy_pressure_v1 contract, formerly accepted, is refused by name "
                                      "(PRESSURE_MODEL_REAUTHOR_REQUIRED, blocking through problem()); every other contract keeps the old "
                                      "PRESSURE_CONTRACT_UNSUPPORTED branch, now `declared != exact`")
            elif base == "pressure_runtime.rs" and "historical_pressure_reference" in txt_m and "!= 0.0" in txt_m and txt_p == 'if load . category == "pressure" || load . dimension == "pressure" {':
                kind, why = "F", ("[F3] the legacy-primitive refusal widened: formerly a pressure-category or pressure-dimension primitive "
                                  "with a nonzero value (and not inside the #[cfg(test)] historical scope); now every such primitive, zero "
                                  "values included. It refuses a superset, and establishes premise P0")
            elif base == "preview_physics.rs" and not mt and "JOINT_ELEMENT_STIFFNESS_INCOMPLETE" in txt_p and "JOINT_ELEMENT_MAPPING_UNRESOLVED" in txt_p:
                pushes = txt_p.count("diagnostics . push ( diag (")
                mut_other = re.findall(r"\b(\w+)\s*(?:\.\s*(?:push|insert|extend|retain|clear)\s*\(|\+=|=(?![=>]))", txt_p)
                lets = set(re.findall(r"let (?:mut )?(\w+)", txt_p))
                writes = [w for w in mut_other if w not in lets and w not in ("diagnostics", "let") and w not in KW]
                extra["writes_outside_locals"] = writes
                if pushes == 2 and txt_p.count('"blocking"') == 2 and txt_p.count("continue ;") == 2 and not writes:
                    kind, why = "F", ("[F4] G11 (I111; extended by ROOT): a user-flexibility expansion joint missing any of its four user "
                                      "stiffness values, or whose pipe or node does not resolve, is refused (blocking) rather than silently "
                                      "skipped by the element builder. The code only reads the model, builds local values and pushes "
                                      "two blocking diagnostics, then `continue`s; its loops and allocations are this pass's item 4")
            elif txt_p == "let component_pressure_thrust_load_count = 0 ;" and "append_expansion_joint_pressure_thrust_results" in txt_m:
                kind, why = "Z", ("the count of expansion-joint pressure-thrust results, formerly the number of joints whose exact net thrust "
                                  "was nonzero (a zero net was skipped). Under premise P0 there is no thrust load, so it was 0 on every "
                                  "admitted model; the published summary count is the same constant")
        if not kind:
            sm = difflib.SequenceMatcher(None, mt, pt, autojunk=False); ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
            def okrun_at(i1, i2):
                run = mt[i1:i2]
                if any(is_id(t) and t in RET for t in run): return True
                if any(is_str(t) for t in run) or not all(not is_id(t) or t in KW for t in run): return False
                lits = [t for t in run if t in ("None", "false", "true")]
                if not lits: return all(not is_id(t) or t in ("if", "else") for t in run)
                callee = callee_before(mt, i1); rp = removed_params(rel, callee) if callee else None
                if rp and len(rp) >= len(lits) and all("pressure" in x for x in rp):
                    extra.setdefault("literal_arguments_of_removed_parameters", []).append({"callee": callee, "removed_parameters": rp, "arguments": lits})
                    return True
                return False
            if ops and all(o[0] == "delete" for o in ops) and all(okrun_at(o[1], o[2]) for o in ops):
                kind, why = "S", "a subtractive edit: only tokens of the retired pressure path are deleted (premise P0: each deleted term was an identity)"
                extra["deleted_tokens"] = [" ".join(mt[o[1]:o[2]]) for o in ops]
            elif (ops and all(o[0] in ("delete", "replace") for o in ops) and sum(o[0] == "replace" for o in ops) == 1
                  and all(okrun_at(o[1], o[2]) for o in ops)
                  and all(pt[o[3]:o[4]] == ["0.0"] for o in ops if o[0] == "replace")):
                kind, why = "H", ("H-1: the retired pressure summand becomes the literal `0.0`; premise P0: the summand was +0.0 on every admitted "
                                  "model, so the arithmetic and the published sign of a zero are unchanged")
                extra["replaced_tokens"] = [" ".join(mt[o[1]:o[2]]) + "  ->  " + " ".join(pt[o[3]:o[4]]) for o in ops]
            elif ops and all(o[0] == "replace" and o[2] - o[1] == o[4] - o[3] for o in ops) and all(
                    is_str(mt[i]) and is_str(pt[j]) for o in ops for i, j in zip(range(o[1], o[2]), range(o[3], o[4]))):
                pairs = [(mt[i], pt[j]) for o in ops for i, j in zip(range(o[1], o[2]), range(o[3], o[4]))]
                if all(placeholders(b) == placeholders(a) for a, b in pairs):
                    kind, why = "W", "wording only: string literals changed, their format placeholders unchanged; no argument, call or control flow changes"
                    extra["literals"] = [{"old": a[:400], "new": b[:400]} for a, b in pairs]
    if not kind:
        refused.append({"file": rel, "new_lines": nl, "class": cls, "fingerprint": r["fingerprint"], "removed": [l.strip() for l in code_lines(minus)][:4],
                        "added": [l.strip() for l in code_lines(plus)][:4]}); continue
    e = {"fingerprint": r["fingerprint"], "file": rel, "at_final_basis": f"{base}:{nl}", "class": cls, "attribution": kind,
         "removed": [l.strip()[:200] for l in code_lines(minus)][:6], "added": [l.strip()[:200] for l in code_lines(plus)][:6],
         "removed_lines": len(minus), "added_lines": len(plus), "evidence": why,
         "reviewed_by": ("attributed by I107 (SB, Pass B round 3) to U3, the legacy pressure retirement (PR #1168; R/I110/pressure_retire_01..06, "
                         "R/REVIEW_RV127/u3_stage1_01); read hunk by hunk; for RV124's confirmation")}
    if ret_named: e["retired_identifiers_named"] = ret_named[:12]
    if enc_fn: e["enclosing_fn_at_base"] = enc_fn
    e.update(extra); entries.append(e)
by = collections.Counter(e["attribution"] for e in entries)
json.dump({"about": "U3 Pass B (I107): entries for the hunks of main ba500defa4 (B1 + PR-N as merged) -> 8a12de28db (U3's code) that need one, "
                    "keyed by the delta tool's fingerprint, each attributed by mk_delta_reviewed_u3.py's checks (its docstring states them and "
                    "premise P0).",
           "dry_run_inventory": {"old": old, "new": new, "needing_entries": len(need)}, "by_kind": dict(sorted(by.items())),
           "entries": entries, "refused": refused}, open(out_p, "w"), indent=1)
print(json.dumps({"needing": len(need), "entries": len(entries), "refused": len(refused), "by_kind": dict(sorted(by.items()))}))
for x in refused: print("REFUSED", json.dumps(x)[:400])
sys.exit(1 if refused else 0)
