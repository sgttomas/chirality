#!/usr/bin/env python3
"""Checkpoint-0 record arithmetic only. No solver, runner or audit imports.

The evaluated formula is an explicitly incomplete normalized schedule candidate,
not the final admission estimate. See FORMULA.md. Frozen input validation occurs
before parsing. The output identifies this script by content hash and separates
its uncommitted origin from the product/input Git basis (AUD-REV-N1).
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
BASIS = '3bddc2b05f6106e969c7cf43373b230845c7cc66'
P = Path('projects/chirality-piping')
H = P/'core/solver/performance_harness'
T3 = P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/NUMERICAL_INTEGRITY_T3'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def lines(path):
    return [json.loads(s) for s in (ROOT/path).read_text().splitlines() if s.strip()]

def grow(n, size):
    """Historical/liballoc assumption, NOT measured on this host."""
    if not n:
        return 0
    minimum = 8 if size == 1 else (4 if size <= 1024 else 1)
    return max(minimum, 1 << (n-1).bit_length())*size

def normalized(c, fixed=None):
    """Live-phase normalization. It intentionally retains unresolved old terms.

    Includes Uc overlap, shift lifetimes, A2 block/report storage, formation
    scratch and a conservative tracker-table normalization. Not a heap proof.
    """
    f, n, m, q, z, sky = [c['w1_'+k] for k in ['free_dofs','dofs','members','rows','pattern_entries','profile_entries']]
    b, bodies, r = [c['w1_'+k] for k in ['blocks','bodies','constraints']]
    fixed = c['estimate_w1_fixed_bytes'] if fixed is None else fixed
    kept, phases, detail = fixed, {}, {}
    phases['group_legacy_unclosed'] = kept + 78*m*32
    # ABI assumptions only. Wide Option uses the historical bool niche;
    # BoundRefusal/Option bound=16, ShiftResult <=5*w+24,
    # BlockCertificate <=11*w+64. Each must receive a pinned-layout witness.
    decide = 4608*4304 + 15*q*40
    for p, limbs, resid in [(128,4,4),(256,4,8),(512,8,16),(1024,16,16)]:
        w, wr = 8*limbs+16, 8*resid+16
        shared = c[f'estimate_w1_shared_{p}']
        pivot = 768*4304 + 5*f*40
        build = 0 if p == 1024 else m*(164*wr+16)
        # Factor work and condition solves are not present in old shared_build.
        # The result counts the full shared payload at each partial build.
        build = max(build + z, f*w, 5*f*w + 8*f + 24*b)
        phases[f'shared_{p}'] = kept + shared + build + pivot
        kept += shared
        state = c[f'estimate_w1_state_{p}']
        solve = c[f'estimate_w1_solve_{p}'] + 14*f*40
        phases[f'solve_{p}'] = kept + state + solve
        kept += state
        if p == 128:
            continue
        ww = 80 if p == 256 else 144
        # Old VerifyShared formula overcounted Option by 8 but omitted refusal.
        verify = c[f'estimate_w1_verify_{p}'] + b*8
        bounded = m*(5*w+8)
        vbuild_parts = {
            'bounded_assembly': 144*m*w,
            'wide_formation': 0 if p == 1024 else m*(164*ww+16),
            'uc_nl_overlap': 4*f*w + 4*f + 2*b*w,
        }
        vbuild = bounded + 16*b + max(vbuild_parts.values())
        phases[f'verify_build_{p}'] = kept + verify + vbuild
        kept += verify
        live = 3*n*w + 8*f*w + (q+6*m)*w + 50*n + r*(ww+w)
        # Caller-owned data, refusal slots and growing start vector.
        pre = b + 16*b + grow(b,w+16)
        profile = sky*w + 36*f
        shifted = sky*w + 32*f + f*w + b
        # Results, current, sigma, in_flight and per-block refused.
        schedule = b*(5*w+32) + b*(w+16) + b*w + grow(b,8) + 16*b
        shift_steps = {
            'shift_factor_work': f*w,
            'shift_nl_at_bt_ct': 3*f*w,
            'shift_collect_next': f*w + b*w + grow(b,w+16),
        }
        shift = pre + profile + shifted + schedule + max(shift_steps.values())
        formation_scratch = (18*m+n)*w
        block_report = b*(19*w+64) + bodies*(13*w+16)
        after_extra = pre + b*(5*w+32) + block_report
        pass_parts = {
            'formation_recovery_envelope': live + 3*q*w + formation_scratch,
            'shift': live + 3*q*w + shift,
            'after_shift': live + 5*q*w + after_extra,
        }
        report = 5*q*w + 2*f*w + block_report
        phases[f'pass_{p}'] = kept + max(pass_parts.values())
        phases[f'decide_{p}'] = kept + report + decide
        detail[str(p)] = dict(wide_bytes=w, verify_payload=verify,
            verify_build_components=vbuild_parts, verify_build=vbuild,
            shift_components=shift_steps, pass_components=pass_parts,
            pass_bytes=max(pass_parts.values()), report_bytes=report,
            shift_only_known_delta=2*f*w-8*(3*q+f),
            uc_nl_overlap_bytes=4*f*w,
            legacy_pass_bytes=c[f'estimate_w1_pass_{p}'])
    max_at = max(phases, key=phases.get)
    return dict(fixed_bytes=fixed,max_bytes=phases[max_at],max_phase=max_at,
                phases=phases,detail=detail,
                unresolved=['construction/capacity/fixed binary terms',
                            'decision map/sort/capacity and finish payload closure',
                            'pinned ABI/liballoc witnesses', 'final A1 impact'])

def policy(run, estimate, previous):
    """The recorded W1 branch, with refusal branches retained for candidates."""
    assert run['mode'] == 'w1a'
    if estimate > run['heap_cap_bytes']//2:
        return {'decision':'deferred','reason':"deferred:the binary's backstop would refuse "
                '(estimate %d B > half the heap cap %d B)' % (estimate,run['heap_cap_bytes']//2)}
    if run['members'] > 100:
        pred = run['model'].replace('-n%05d-' % run['members'], '-n%05d-' % (run['members']//10))
        assert any(x['model']==pred and x['mode']=='w1a' and x.get('classification') not in (None,'not_run') for x in previous)
    usable=[x for x in previous if x['family']==run['family'] and x['mode']=='w1a'
            and (100 if run['members']>=1000 else 0)<=x['members']<run['members'] and x.get('classification')=='ok']
    rss_ratios=[]; fp_ratios=[]; rf_ratios=[]
    for rec in usable:
        fp=rec['rss']['time_peak_footprint_bytes']; rss=rec['peak_rss_bytes']; heap=rec['repeats_heap_peak_move'] or 0
        rss_ratios.append(max(max(0,rss-run['baseline_rss_bytes']),heap)/rec['estimate_adm_bytes'])
        fp_ratios.append(max(max(0,fp-run['baseline_footprint_bytes']),heap)/rec['estimate_adm_bytes'])
        rf_ratios.append(rss/fp)
    rho=max(fp_ratios) if fp_ratios else 2.0
    rho_rss=max(rss_ratios) if rss_ratios else 2.0
    rf=max(rf_ratios) if rf_ratios else 1.45
    half=run['rss_cap_bytes']//2
    out=dict(decision=None,reason=None,estimate_adm_bytes=estimate,rho=rho,rho_rss=rho_rss,
             half_cap_bytes=half,footprint_estimate_bytes=None,rss_to_footprint=rf,
             projected_rss_bytes=None,projected_rss_limit_bytes=int(.8*run['rss_cap_bytes']))
    if estimate*rho>half:
        out.update(decision='deferred',reason='deferred:estimate_fails_admission (%d B x rho %.3f > C/2)' % (estimate,rho));return out
    footprint=int(estimate*rho); projected=int(footprint*rf)
    out.update(footprint_estimate_bytes=footprint,projected_rss_bytes=projected)
    if projected>out['projected_rss_limit_bytes']:
        out.update(decision='deferred',reason='deferred:projected_rss_exceeds_0.8C (%d B x %.3f = %d B > %d B)' % (footprint,rf,projected,out['projected_rss_limit_bytes']));return out
    out.update(decision='admitted',reason='estimate %d B x rho %.3f <= C/2; projected RSS %d B <= 0.8C' % (estimate,rho,projected))
    return out

def validate_inputs(pins):
    assert pins['git_basis']==BASIS
    for entry in pins['inputs']:
        path=entry['path']; raw=(ROOT/path).read_bytes()
        assert digest(raw)==entry['sha256'], 'working input drift: '+path
        if entry.get('at_product_basis'):
            frozen=subprocess.check_output(['git','show',BASIS+':'+path])
            assert raw==frozen, 'Git input drift: '+path

def main():
    pins=json.loads((HERE/'INPUTS.json').read_text())
    validate_inputs(pins)
    hc={r['model']:r for r in lines(H/'observations/k6b/counts.jsonl')}
    estimates={mid:normalized(c) for mid,c in hc.items()}
    admissions=[]
    heap_checks=[]
    for name in ['VK','KF3']:
        base=T3/'IMPLEMENTATION'/name/'_run_records/b'
        vc={r['model']:r for r in lines(base/('setup/counts.jsonl' if name=='VK' else 'counts.json'))}
        oldprev=[];newprev=[]
        for rec in lines(base/'runs/records.jsonl'):
            mid=rec['model']; c=hc[mid]; v=vc[mid]
            for k in ['free_dofs','rows','profile_entries','pattern_entries']:
                assert c['w1_'+k]==v[k], (mid,k)
            old=policy(rec,v['estimate_max_bytes'],oldprev)
            assert old==rec['admission'], 'historical policy mismatch '+rec['run_id']
            new_estimate=normalized(c,v['estimate_fixed_bytes'])['max_bytes']
            new=policy(rec,new_estimate,newprev)
            admissions.append(dict(slice=name,run_id=rec['run_id'],all_original_fields_match=True,
                original=old,provisional=new,decision_changed=old['decision']!=new['decision'],
                changed_fields=[k for k in set(old)|set(new) if old.get(k)!=new.get(k)]))
            oldprev.append(rec);newprev.append(dict(rec,estimate_adm_bytes=new_estimate))
            for metric in ['repeats_heap_peak','repeats_heap_peak_move']:
                peak=rec.get(metric)
                if peak is not None:
                    heap_checks.append(dict(slice=name,model=mid,metric=metric,recorded=peak,
                        estimate=new_estimate,margin=new_estimate-peak,binary='vk_scale'))
    packet=json.loads((ROOT/H/'observations/k6b/k6b_packet.json').read_text())
    # Discover summary records structurally without importing a maintained runner.
    def visit(x):
        if isinstance(x,dict):
            if x.get('mode')=='w1a' and x.get('model') in hc and 'repeats_heap_peak' in x:
                yield x
            for v in x.values():yield from visit(v)
        elif isinstance(x,list):
            for v in x:yield from visit(v)
    seen=set()
    for rec in visit(packet):
        identity=(rec.get('run_id'),rec['model'],rec.get('repeats_heap_peak'))
        if identity in seen:continue
        seen.add(identity)
        for metric in ['repeats_heap_peak','repeats_heap_peak_move']:
            peak=rec.get(metric)
            if peak is not None:
                estimate=estimates[rec['model']]['max_bytes']
                heap_checks.append(dict(slice='K6B-packet',model=rec['model'],run_id=rec.get('run_id'),
                    metric=metric,recorded=peak,estimate=estimate,margin=estimate-peak,binary='k6_observe'))
    assert len(admissions)==36
    result=dict(status='PROVISIONAL_INCOMPLETE_CANDIDATE_NOT_ADMISSION_AUTHORITY',
        product_input_basis=BASIS,actual_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        script=dict(path=str(Path(__file__).relative_to(ROOT)),sha256=digest(Path(__file__).read_bytes()),
                    revision='uncommitted I21-K6C working-tree record; content-hash identified'),
        inputs_manifest_sha256=digest((HERE/'INPUTS.json').read_bytes()),
        model_count=len(hc),estimates=estimates,admissions=admissions,
        decision_changes=sum(r['decision_changed'] for r in admissions),heap_checks=heap_checks,
        k6b_w1_summary_records=len(seen),negative_heap_margins=[r for r in heap_checks if r['margin']<0],
        limits=['Final-formula replay is outstanding, including A1 and every unresolved allocation term.',
                'Historical measurements and approvals are inputs, not M3 admission or fresh observations.',
                'No imports, compiler invocation, solver, installation, signal, guard or model execution.'])
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':main()
