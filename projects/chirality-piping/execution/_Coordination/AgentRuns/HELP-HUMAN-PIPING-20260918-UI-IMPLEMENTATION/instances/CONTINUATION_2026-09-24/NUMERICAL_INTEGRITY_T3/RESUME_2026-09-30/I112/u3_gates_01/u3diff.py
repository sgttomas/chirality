#!/usr/bin/env python3
"""I112 round 2 (U3 gates): classify one base/candidate output pair under the U3 brief's acceptance rule.

Classes (the brief, "Acceptance"):
  identical
  declared      only declared strings differ: the candidate, with each declared new string replaced by its old string, equals the
                base byte for byte. Declared pairs: T1, T3a, T3b, V1 and T2 of U3's CHANGE_RECORD §6 (the brief's T1, T2, T3, V1).
  declared_t2   T2 is present and the two digests that bind it (source_block_recovery.body.publication_sha256 and
                source_block_recovery.receipt_sha256) differ besides: (i) the candidate's own digests equal the product's
                recomputation from the candidate's content; (ii) the normalized candidate (declared strings replaced) with its two
                digests replaced by the product's recomputation from that normalized content equals the base byte for byte.
                The recomputation is the scratch helper i112_receipt_digests (PP source_receipt::hash's rule over the product's
                canonical_json crate).
  refusal       a designed refusal: the candidate is a refusal envelope (no results; status.mechanics MODEL_INCOMPLETE) whose
                blocking diagnostics include the documented code with the documented text, and the input carries the trigger:
                the legacy label (PRESSURE_MODEL_REAUTHOR_REQUIRED on pressure_contract), a legacy pressure primitive in a
                non-exact document named by the diagnostic's refs (case, load), or a joint refused by G11
                (JOINT_ELEMENT_STIFFNESS_INCOMPLETE, JOINT_ELEMENT_MAPPING_UNRESOLVED) named by its refs.
  OTHER         anything else (a stop). V2 and T4 are tracked but are not in the brief's list.
The removed-case class needs the input inventory and is decided by the caller.
"""
import json
import os
import re
import subprocess
import tempfile

DIGEST_BIN = 'WT/targets/i112-u3-digest/release/i112_receipt_digests'
PAIRS = [
    ('T1', 'pressure_thrust_treatment=arc_end_cap_tangent_pair_plus_consistent_radial_wall_load',
     'pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract'),
    ('T3a', 'pressure_thrust_generation=load_side_user_effective_area;pressure_thrust=',
     'pressure_thrust_generation=none_pressure_refused_outside_the_exact_straight_contract;user_pressure_thrust_reference='),
    ('T3b', '; pressure-thrust generation is load-side effective-area evidence and no compliance claim is made',
     '; no joint pressure thrust is generated and no compliance claim is made'),
    ('V1', 'expansion joint components require solver_consumption=mechanics_geometry_and_user_flexibility under DEC-045; pressure thrust remains load-side input evidence',
     'expansion joint components require solver_consumption=mechanics_geometry_and_user_flexibility under DEC-045; no joint pressure thrust is generated'),
    ('T2', 'Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open.',
     "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications."),
]
UNLISTED = [
    ('V2', 'expansion joint effective pressure area and movement limit must be finite positive user-entered values before load-side pressure-thrust evidence can be generated',
     'expansion joint effective pressure area and movement limit must be finite positive user-entered values; they are recorded as input evidence only, and no joint pressure thrust is generated'),
    ('T4', 'Nonzero pressure is refused on this route, and so is legacy imposed_displacement.',
     'Legacy pressure primitives are refused on this route, zero values included, and so is legacy imposed_displacement.'),
]
# the documented refusal texts (candidate PP/src/pressure_runtime.rs validate_profile; PP/src/preview_physics.rs
# refuse_unqualified_joint_elements)
REAUTHOR_PRIMITIVE = ('legacy pressure primitives are retired, zero values included; remove the primitive, or re-author the model to '
                      '2.0.0/exact_straight_pressure_v2 with explicit pressure_regions (an explicit [] for an unpressurized case) and E/nu materials')
REAUTHOR_LABEL = ('the 1.0.0/legacy_pressure_v1 pressure contract is retired; re-author the model to 2.0.0/exact_straight_pressure_v2 with '
                  'explicit pressure_regions (an explicit [] for an unpressurized case) and E/nu materials')
JOINT_STIFF = re.compile(r'expansion joint (\S+) declares mechanics_geometry_and_user_flexibility but has no user-entered (.+) stiffness, so its '
                         r'user-stiffness element cannot be assembled; the solve is refused rather than published without the joint \(G11\)$')
JOINT_MAP = re.compile(r'expansion joint (\S+) declares mechanics_geometry_and_user_flexibility but (.+), so its user-stiffness element cannot '
                       r'be assembled; the solve is refused rather than published without the joint \(G11\)$')
REFUSAL_CODES = ('PRESSURE_MODEL_REAUTHOR_REQUIRED', 'JOINT_ELEMENT_STIFFNESS_INCOMPLETE', 'JOINT_ELEMENT_MAPPING_UNRESOLVED')


def digests_of(text, workdir):
    with tempfile.NamedTemporaryFile('w', suffix='.json', dir=workdir, delete=False) as fh:
        fh.write(text)
        p = fh.name
    try:
        r = json.loads(subprocess.run([DIGEST_BIN, p], capture_output=True, text=True, check=True).stdout.splitlines()[0])
    finally:
        os.unlink(p)
    if 'error' in r:
        raise ValueError(r['error'])
    return r['publication_sha256'], r['receipt_sha256']


def normalize(text):
    used = {}
    for tag, old, new in PAIRS:
        n = text.count(new)
        if n:
            text = text.replace(new, old)
            used[tag] = n
    return text, used


def unlisted_present(base, cand):
    return [tag for tag, old, new in UNLISTED if new in cand and old in base]


def _primitive(model, case_id, load_id):
    for c in model.get('load_cases', []):
        if c.get('id') == case_id:
            for l in c.get('primitive_loads', []):
                if l.get('id') == load_id:
                    return l
    return None


def refusal_check(cand_doc, model):
    """[(code, refs, trigger)] for every documented refusal diagnostic, or None when the candidate is no refusal envelope or a
    refusal diagnostic is not documented or not triggered by the input."""
    if not isinstance(cand_doc, dict) or cand_doc.get('results') or (cand_doc.get('status') or {}).get('mechanics') != 'MODEL_INCOMPLETE':
        return None
    found = []
    for d in cand_doc.get('diagnostics', []):
        if d.get('code') not in REFUSAL_CODES or d.get('severity') != 'blocking':
            continue
        refs, msg = d.get('affected_refs') or [], d.get('message', '')
        if model is None:
            return None
        exact = (model.get('pressure_contract') or {}).get('version') == '2.0.0'
        if d['code'] == 'PRESSURE_MODEL_REAUTHOR_REQUIRED':
            if refs == ['pressure_contract']:
                pc = model.get('pressure_contract') or {}
                ok = msg == REAUTHOR_LABEL and pc.get('version') == '1.0.0' and pc.get('mode') == 'legacy_pressure_v1'
                trig = 'legacy label 1.0.0/legacy_pressure_v1'
            elif len(refs) == 2:
                load = _primitive(model, refs[0], refs[1])
                ok = (msg == REAUTHOR_PRIMITIVE and not exact and load is not None
                      and (load.get('category') == 'pressure' or load.get('dimension') == 'pressure'))
                trig = 'legacy pressure primitive %s in %s (value %s)' % (refs[1], refs[0], (load or {}).get('value'))
            else:
                ok = False
        else:
            m = (JOINT_STIFF if d['code'] == 'JOINT_ELEMENT_STIFFNESS_INCOMPLETE' else JOINT_MAP).match(msg)
            comp = next((c for c in model.get('components', []) if c.get('id') == (m.group(1) if m else None)), None)
            ok = bool(m) and comp is not None and refs and refs[0] == comp['id']
            trig = 'joint %s: %s' % (m.group(1) if m else '?', m.group(2) if m else '?')
        if not ok:
            return None
        found.append((d['code'], refs, trig))
    return found or None


def classify(base_text, cand_text, model=None, workdir='.'):
    if base_text == cand_text:
        return 'identical', {}
    norm, used = normalize(cand_text)
    info = {'declared': used}
    unl = unlisted_present(base_text, cand_text)
    if unl:
        info['unlisted_text_changes'] = unl
    if norm == base_text and used and not unl:
        return 'declared', info
    if 'T2' in used and not unl:
        try:
            cand_doc = json.loads(cand_text)
            sbr = cand_doc.get('source_block_recovery') or {}
            cp, cr = sbr['body']['publication_sha256'], sbr['receipt_sha256']
            rp, rr = digests_of(cand_text, workdir)
            np_, nr = digests_of(norm, workdir)
            info.update(cand_digests=[cp, cr], rule_on_cand=[rp, rr], rule_on_normalized=[np_, nr])
            if (cp, cr) == (rp, rr) and norm.count(cp) == 1 and norm.count(cr) == 1:
                patched = norm.replace(cp, np_, 1).replace(cr, nr, 1)
                if patched == base_text:
                    return 'declared_t2', info
            info['why'] = 'T2 digest check failed'
        except Exception as e:  # noqa: BLE001
            info['why'] = 'T2 digest check error: %s' % e
        return 'OTHER', info
    try:
        cand_doc = json.loads(cand_text)
    except Exception:
        cand_doc = None
    ref = refusal_check(cand_doc, model) if cand_doc is not None else None
    if ref:
        info['refusal'] = ref
        try:
            base_doc = json.loads(base_text)
            info['base_status'] = (base_doc.get('status') or {}).get('mechanics')
            info['base_results'] = len(base_doc.get('results') or [])
            info['base_blocking_codes'] = sorted({d['code'] for d in base_doc.get('diagnostics', []) if d.get('severity') == 'blocking'})
        except Exception:
            info['base_status'] = 'not JSON: ' + base_text[:80]
        return 'refusal', info
    info['why'] = 'not identical, not declared text, not a documented refusal'
    return 'OTHER', info
