#!/usr/bin/env python3
"""Reviewer-owned probes; no product, author-probe or canonicalizer import."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,math,re,struct,sys

OUT=Path(__file__).parent
SAFE=2**53-1
def bits(v): return struct.pack('>d',v).hex()
def rational(v): return F(*v.as_integer_ratio())
def exact_decimal(q):
    """Exact decimal for a dyadic rational, without Decimal rounding."""
    sign='-' if q<0 else ''
    q=abs(q); k=q.denominator.bit_length()-1
    assert q.denominator==2**k
    digits=str(q.numerator*5**k)
    if not k:return sign+digits
    digits=digits.rjust(k+1,'0')
    return sign+digits[:-k]+'.'+digits[-k:]
def nearest_check(token):
    exact=F(Decimal(token)); actual=float(token)
    if not math.isfinite(actual):return {'token':token,'outcome':'overflow'}
    distance=abs(rational(actual)-exact)
    for adjacent in [math.nextafter(actual,-math.inf),math.nextafter(actual,math.inf)]:
        if math.isfinite(adjacent):
            other=abs(rational(adjacent)-exact)
            assert distance<=other,(token,actual,adjacent)
            if distance==other:
                assert int(bits(actual),16)%2==0,(token,'wrong tie parity')
    return {'token':token,'bits':bits(actual),'python_repr':repr(actual),
            'exact_nonzero':exact!=0,'rounded_zero':actual==0}

tokens=['1e160','100000000000000000000','1e20','1.0e20',
        '9007199254740991','9007199254740992','9007199254740993',
        '9007199254740995','9007199254740993.0','9.007199254740993e15',
        '18446744073709551615','295147905179352825856',
        '1','1.0','1e0','1.0000000000000000001','0.1',
        '5e-324','-5e-324','1e-324','-1e-324',
        '2.2250738585072014e-308','1.7976931348623157e308','1e309']
rows=[nearest_check(t) for t in tokens]
assert float('1e160').is_integer() and math.isfinite(float('1e160'))
assert float('9007199254740993')==2**53
assert float('9007199254740995')==2**53+4
assert float('18446744073709551615')==2**64
assert bits(float('5e-324'))=='0000000000000001'

# Exact ties at 1 and zero, plus values on either side. This checks conversion,
# not the accuracy or resource range of a solver using the admitted value.
special=[]
for q,expected in [
    (F(1)+F(1,2**53),'3ff0000000000000'),
    (F(1)+F(1,2**53)+F(1,2**110),'3ff0000000000001'),
    (F(1,2**1075),'0000000000000000'),
    (F(1,2**1075)+F(1,2**1200),'0000000000000001'),
    (F(1,2**1075)-F(1,2**1200),'0000000000000000')]:
    token=exact_decimal(q); row=nearest_check(token)
    assert row['bits']==expected
    special.append(row)
overflow_boundary=2**1024-2**970
assert math.isinf(float(str(overflow_boundary)))
assert bits(float(str(overflow_boundary-1)))=='7fefffffffffffff'

# Strict count admission must precede ordinary parsing.
grammar=re.compile(r'(?:0|-?[1-9][0-9]*)\Z')
def safe_integer_token(t):return bool(grammar.fullmatch(t)) and abs(int(t))<=SAFE
count_cases={t:safe_integer_token(t) for t in ['0','-0','1','1.0','1e0',
    '1.0000000000000000001',str(SAFE),str(SAFE+1),str(-SAFE),str(-SAFE-1)]}
assert count_cases=={'0':True,'-0':False,'1':True,'1.0':False,'1e0':False,
    '1.0000000000000000001':False,str(SAFE):True,str(SAFE+1):False,
    str(-SAFE):True,str(-SAFE-1):False}
def nonnegative_count(t):return safe_integer_token(t) and int(t)>=0
assert not nonnegative_count('-1') and nonnegative_count('0')
assert isinstance(True,int) and type(True) is not int
assert json.loads('1.0000000000000000001')==1
assert type(json.loads('-0')) is int and json.loads('-0')==0
assert bits(json.loads('-0.0'))=='8000000000000000'
assert json.loads('9007199254740993')==9007199254740993

# Duplicate rejection happens after decoded names, before map overwrite.
def pairs(xs):
    d={}
    for k,v in xs:
        if k in d:raise ValueError('duplicate')
        d[k]=v
    return d
for doc in ['{"a":1,"\\u0061":2}','{"n":{"a":1,"\\u0061":2}}']:
    try:json.loads(doc,object_pairs_hook=pairs)
    except ValueError as e:assert str(e)=='duplicate'
    else:raise AssertionError('duplicate accepted')
assert json.loads('"\\ud83d\\ude00"')=='\U0001f600'
def scalar(s):
    return all(not(0xd800<=ord(c)<=0xdfff or 0xfdd0<=ord(c)<=0xfdef
                   or ord(c)&0xffff in [0xfffe,0xffff]) for c in s)
for cp in [0xd800,0xdfff,0xfdd0,0xfdef,0xfffe,0xffff,0x1fffe,0x10ffff]:
    assert not scalar(chr(cp))
assert scalar('\U0001f600') and scalar('\u00e9') and scalar('e\u0301')
assert sorted(['\uff5a','\U0001f600'],key=lambda s:s.encode('utf-16-be'))==['\U0001f600','\uff5a']

# Exact represented-input arithmetic for stress units; no product area formula.
force,area=1e-306,596902.6041820607
q=rational(force)/rational(area)
pa=force/area;mpa=pa/1_000_000
pa_error=abs(rational(pa)/q-1)
mpa_error=abs(rational(mpa)*1_000_000/q-1)
assert pa_error<F(1,10**9)<mpa_error
with localcontext() as context:
    context.prec=80
    dec=lambda f:str(Decimal(f.numerator)/Decimal(f.denominator))
    stress={'force_bits':bits(force),'area_bits':bits(area),'pa_bits':bits(pa),
            'mpa_bits':bits(mpa),'pa_repr':repr(pa),'mpa_repr':repr(mpa),
            'pa_relative_error':dec(pa_error),'mpa_relative_error':dec(mpa_error),
            'criterion':'1e-9','pa_exact_ratio':str(q)}

result={'status':'PASS','python':sys.version,'scope':'independent host/reference probes only',
        'product_execution':False,'ordinary_tokens':rows,'exact_midpoints':special,
        'overflow_midpoint_rejected_by_finite_policy':True,'exact_integer_cases':count_cases,
        'nonnegative_count_bound_controls':'PASS',
        'python_host_notes':['int retains unsafe integer text','bool subclasses int',
            'integer -0 spelling erases before typed admission','fractional token rounds to1'],
        'unicode_and_duplicate_controls':'PASS','stress_units':stress,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(OUT/'PYTHON_REFERENCE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','ordinary_tokens':len(rows),'midpoint_cases':len(special),'product_execution':False}))
