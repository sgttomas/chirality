#!/usr/bin/env python3
"""Independent domain probes only; not a JSON canonicalizer or product test."""
import json, math, re, struct, sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

SAFE=2**53-1
NUMBER=re.compile(r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\Z')
INTEGER=re.compile(r'(?:0|-?[1-9][0-9]*)\Z')
def bits(v): return struct.pack('>d',v).hex()
def real(token):
    if not NUMBER.fullmatch(token): raise ValueError('syntax')
    exact=Decimal(token)
    if exact.is_zero() and exact.is_signed(): raise ValueError('negative_zero')
    value=float(token)
    if not math.isfinite(value): raise ValueError('overflow')
    if value==0 and exact!=0: raise ValueError('nonzero_underflow')
    return value

def count(token):
    if not INTEGER.fullmatch(token): raise ValueError('integer_token_required')
    n=int(token)
    if abs(n)>SAFE: raise ValueError('unsafe_exact_integer')
    return n

def rejection(fn,token,expected):
    try: fn(token)
    except ValueError as e:
        assert str(e)==expected,(token,str(e),expected)
        return str(e)
    raise AssertionError((token,'unexpected admission'))

rows=[]
for token in ['1e160','100000000000000000000','1e20','1.0e20','9007199254740991','9007199254740992','9007199254740993','9007199254740993.0','9.007199254740993e15','18446744073709551615','1','1.0','1e0','1.0000000000000000001','0.1','5e-324','1.7976931348623157e308','2.2250738585072014e-308']:
    value=real(token)
    try: exact_count={'status':'accept','value':count(token)}
    except ValueError as e: exact_count={'status':'reject','reason':str(e)}
    rows.append({'token':token,'real_bits':bits(value),'actual_binary64_hex':value.hex(),'real_integral_valued':value.is_integer(),'exact_integer':exact_count})
assert real('1e160').is_integer() and real('1e160')>SAFE and math.isfinite(real('1e160'))
assert len({bits(real(x)) for x in ['100000000000000000000','1e20','1.0e20']})==1
assert len({bits(real(x)) for x in ['9007199254740993','9007199254740993.0','9.007199254740993e15']})==1
assert real('9007199254740993')==9007199254740992
assert real('18446744073709551615')==18446744073709551616
assert count('9007199254740991')==SAFE
assert bits(real('5e-324'))=='0000000000000001'
assert bits(real('1.7976931348623157e308'))=='7fefffffffffffff'
assert Decimal.from_float(real('0.1'))!=Decimal('0.1')
assert len({bits(real(x)) for x in ['1','1.0','1e0','1.0000000000000000001']})==1
neg=[]
for token,reason in [('-0','negative_zero'),('-0.0','negative_zero'),('-0e3','negative_zero'),('1e-324','nonzero_underflow'),('-1e-324','nonzero_underflow'),('1e309','overflow'),('1.7976931348623159e308','overflow'),('NaN','syntax'),('Infinity','syntax')]:
    neg.append({'token':token,'reason':rejection(real,token,reason)})
for token in ['1.0','1e0','1.0000000000000000001']:
    assert rejection(count,token,'integer_token_required')
for token in ['9007199254740992','9007199254740993','18446744073709551615']:
    assert rejection(count,token,'unsafe_exact_integer')
mid='1.00000000000000011102230246251565404236316680908203125'
above='1.00000000000000011102230246251565404236316680908203126'
assert real(mid)==1.0 and real(above)==math.nextafter(1.0,math.inf)

def pairs(items):
    result={}
    for key,value in items:
        if key in result: raise ValueError('duplicate_decoded_key')
        result[key]=value
    return result
try: json.loads('{"a":1,"\\u0061":2}',object_pairs_hook=pairs)
except ValueError as e: assert str(e)=='duplicate_decoded_key'
else: raise AssertionError('duplicate accepted')
def valid_scalar(s):
    return all(not(0xd800<=ord(c)<=0xdfff or 0xfdd0<=ord(c)<=0xfdef or ord(c)&0xffff in (0xfffe,0xffff)) for c in s)
assert valid_scalar('\U0001f600') and not valid_scalar('\ud800') and not valid_scalar('\uffff')
keys=['\uff5a','\U0001f600']
assert sorted(keys,key=lambda s:s.encode('utf-16-be'))==['\U0001f600','\uff5a']
assert '\u00e9'!='e\u0301' and valid_scalar('\u00e9') and valid_scalar('e\u0301')
force,area=1e-306,596902.6041820607
exact_pa=Fraction.from_float(force)/Fraction.from_float(area)
pa=force/area;mpa=pa/1e6
pa_error=abs(Fraction.from_float(pa)-exact_pa)/abs(exact_pa)
mpa_reference=exact_pa/Fraction(1000000)
mpa_error=abs(Fraction.from_float(mpa)-mpa_reference)/abs(mpa_reference)
assert pa_error<Fraction(1,10**9) and mpa_error>Fraction(1,10**9)
with localcontext() as context:
    context.prec=80
    stress_probe={'force_bits':bits(force),'area_bits':bits(area),'pa':repr(pa),'pa_bits':bits(pa),'mpa':repr(mpa),'mpa_bits':bits(mpa),'pa_relative_error':str(Decimal(pa_error.numerator)/Decimal(pa_error.denominator)),'mpa_relative_error':str(Decimal(mpa_error.numerator)/Decimal(mpa_error.denominator)),'unchanged_relative_criterion':'1e-9','claim':'Independent represented-input arithmetic, not observed production execution'}
result={'status':'PASS','claim':'Independent binary64/domain examples only; canonical spellings and cross-language implementation parity are not executed here','python':sys.version,'real_admissions':rows,'real_rejections':neg,'midpoint':{'token':mid,'bits':bits(real(mid)),'above_token':above,'above_bits':bits(real(above))},'additional_checks':['exact count lexical/range rejection','0.1 not exact decimal','decoded duplicate key rejection','Unicode scalar/noncharacter controls','UTF16 supplementary key ordering','no Unicode normalization'],'stress_unit_precision':stress_probe,'signed_zero':{'positive_bits':bits(0.),'negative_bits':bits(-0.),'new_input_negative_zero':'rejected; old serializer is not exercised'}}
p=Path(__file__).parent/'_run_records/NUMERIC_PROBES.json';p.write_text(json.dumps(result,indent=2,ensure_ascii=True)+'\n')
print(json.dumps({'status':'PASS','real_admissions':len(rows),'real_rejections':len(neg),'output':str(p)}))
