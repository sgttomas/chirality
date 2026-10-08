"""RV113 (RV-R): a mutant schema for SR-TS repair 01 (6fa6a64658), in the reviewer's own copy (WT/rv113/ts1-mut).

Each mutant is a source edit of TS guarded by `mx('<id>')`, true only when the environment's RV113_MUT equals the id;
with RV113_MUT unset the copy behaves as the head (a control run checks it). Each anchor must match exactly once.
Usage: python make_ts_mutants_r1.py <retainedPrecision.ts> <manifest out>
"""
import json
import sys

path, manifest_out = sys.argv[1], sys.argv[2]
ts = open(path).read()
manifest = []


def sub(old, new, mid, item, desc):
    global ts
    assert ts.count(old) == 1, (mid, ts.count(old), old[:90])
    ts = ts.replace(old, new)
    manifest.append({"id": mid, "item": item, "description": desc})


def also(mid, item, desc):
    manifest.append({"id": mid, "item": item, "description": desc})


anchor = "const MAX_BITS = 0x7fefffffffffffffn;\n"
assert ts.count(anchor) == 1
ts = ts.replace(anchor, anchor + "const mx = (id: string): boolean => (globalThis as any).process?.env?.RV113_MUT === id;\n")

# ---------------------------------------------------------------- (g) at G8 INVOCATION
sub("""  const absentOrEmpty = (key: string) => !Object.hasOwn(model, key) || (Array.isArray(model[key]) && model[key].length === 0);
  fail(!Object.hasOwn(model, 'reference_configurations') && model.pressure_contract == null && absentOrEmpty('combinations') && absentOrEmpty('components'), 'INVOCATION_MISMATCH');""",
    """  const absentOrEmpty = (key: string) => (mx('U03') && key === 'combinations') || (mx('U04') && key === 'components') ? !model[key]?.length
    : !Object.hasOwn(model, key) || (mx('U05') && model[key] === null) || (Array.isArray(model[key]) && model[key].length === 0);
  fail((mx('U01') || !Object.hasOwn(model, 'reference_configurations')) && (mx('U02') ? !model.pressure_contract : model.pressure_contract == null) && absentOrEmpty('combinations') && absentOrEmpty('components'), 'INVOCATION_MISMATCH');""",
    "U01", "(g)", "reference_configurations check dropped")
also("U02", "(g)", "pressure_contract back to the falsiness test (false, 0 and '' admitted)")
also("U03", "(g)", "combinations back to the old `!combinations?.length`")
also("U04", "(g)", "components back to the old `!components?.length`")
also("U05", "(g)", "combinations and components may be null")
sub("""  if (invocation) fail(same(ids, invocation.request?.model?.load_cases?.map((c: Obj) => c.id)));""",
    """  if (invocation) fail(same(ids, invocation.request?.model?.load_cases?.map((c: Obj) => c.id)) && (!mx('U06') || !(invocation.request?.model?.combinations?.length)));""",
    "U06", "conjunct", "TS's G3 combinations conjunct restored")
# ---------------------------------------------------------------- C2 precondition keying
sub("""      else if (cause.kind === 'unavailable_precondition') fail(['routing', 'preparation'].includes(c.reason.phase) && !c.run && Object.hasOwn(PRECONDITION_CODES, cause.precondition) && c.reason.code === PRECONDITION_CODES[cause.precondition]);""",
    """      else if (cause.kind === 'unavailable_precondition') fail((mx('U09') || ['routing', 'preparation'].includes(c.reason.phase)) && (mx('U10') || !c.run) && (mx('U07')
        ? ['source_unavailable', 'resource_admission_not_available', 'upstream_no_wrap_not_established', 'caller_not_qualified'].includes(c.reason.code)
        : Object.hasOwn(PRECONDITION_CODES, cause.precondition) && c.reason.code === (mx('U08') && cause.precondition === 'source_family' ? 'caller_not_qualified' : PRECONDITION_CODES[cause.precondition])));""",
    "U07", "C2", "precondition keying replaced by the old set of four codes")
also("U08", "C2", "source_family keyed to caller_not_qualified")
also("U09", "C2", "precondition phase dropped")
also("U10", "C2", "precondition no-Run dropped")
# ---------------------------------------------------------------- transport header at G2 (Rust's order and code)
sub("""    const base = projection(s), headerRefusal = headerCode(base, 'rust'); if (headerRefusal !== null) throw new RetainedPrecisionError(gate, headerRefusal);""",
    """    const base = projection(s), headerRefusal = mx('U11') ? null : headerCode(base, mx('U12') ? 'python' : 'rust'); if (headerRefusal !== null) throw new RetainedPrecisionError(mx('U13') ? 'G7' : gate, headerRefusal);""",
    "U11", "header", "transport header check dropped")
also("U12", "header", "transport header in Python's order (carrier branch, evidence before recovery)")
also("U13", "header", "transport header refusal reported at G7")
sub("""  const first = order === 'rust' ? recovery ?? evidence : evidence ?? recovery;""",
    """  const first = order === 'rust' && !mx('U14') ? recovery ?? evidence : evidence ?? recovery;""",
    "U14", "header", "Rust order: contract_evidence before source_block_recovery")
sub("""  if (order === 'python' && Object.hasOwn(p, 'carrier_evidence')) return 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED';""",
    """  if ((order === 'python' || mx('U15')) && Object.hasOwn(p, 'carrier_evidence')) return 'SOURCE_PRODUCER_CONTRACT_UNSUPPORTED';""",
    "U15", "header", "Rust order: the carrier_evidence branch kept")
sub("""    || !f.limitations.every(text)) return 'SOURCE_FORMULATION_BASIS_UNSUPPORTED';
  return null;""",
    """    || !f.limitations.every(text)) return mx('U16') && order === 'rust' ? null : 'SOURCE_FORMULATION_BASIS_UNSUPPORTED';
  return null;""",
    "U16", "header", "Rust order: the formulation-basis branch dropped")
open(path, "w").write(ts)
json.dump(manifest, open(manifest_out, "w"), indent=1)
print(len(manifest), "mutants")
