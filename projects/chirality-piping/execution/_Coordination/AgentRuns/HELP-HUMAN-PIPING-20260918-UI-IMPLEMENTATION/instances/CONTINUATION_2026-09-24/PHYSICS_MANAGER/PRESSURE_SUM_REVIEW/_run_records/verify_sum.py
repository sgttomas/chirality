from pathlib import Path
from fractions import Fraction
import hashlib,itertools,json,math,random,struct,subprocess,sys,time
root=Path.cwd(); r=Path(__file__).resolve().parent
source=root/'projects/chirality-piping/core/product_physics/src/pressure_sum.rs'
expected_hash='7231339e48cabe0f54122ac6253cb2ce936d025d1bb3a391e709030d8b617ef3'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected_hash
bits=lambda v:struct.unpack('>Q',struct.pack('>d',v))[0]
value=lambda b:struct.unpack('>d',struct.pack('>Q',b))[0]
cases=[]
def add(kind, operands):cases.append({'kind':kind,'operands':[f'{x:016x}' for x in operands]})
def floats(kind, operands):add(kind,[bits(x) for x in operands])
least=value(1); maximum=value(0x7fefffffffffffff); normal=value(1<<52)
for name,operands in [('empty',[]),('negative_zero',[-0.0]),('mixed_zero',[0.0,-0.0]),('cancel',[1.0,-1.0]),('max_cancel',[maximum,maximum,-maximum]),('min_subnormal_cancel',[maximum,-maximum,least]),('negative_min_subnormal_cancel',[-maximum,maximum,-least]),('normal_to_subnormal',[normal,-least]),('subnormal_to_normal',[value((1<<52)-1),least]),('overflow',[maximum,maximum]),('negative_overflow',[-maximum,-maximum]),('positive_inf',[math.inf]),('negative_inf',[-math.inf]),('nan',[math.nan])]:floats(name,operands)
for b in [0x7ff0000000000001,0xfff8000000000001]:add('nonfinite_payload',[b])
# Normal midpoint ties: even and odd retained significands, both signs, sticky bits.
for exponent in [-1021,-1000,-970,-100,-53,-1,0,1,52,100,500,970,1023]:
 base=math.ldexp(1.0,exponent);half=math.ldexp(1.0,exponent-53)
 for offset in [0,1,2,7]:
  x=value(bits(base)+offset)
  for sign in [1.0,-1.0]:
   for sticky in [0.0,least,-least]:floats('ties_and_sticky',[sign*x,sign*half,sign*sticky])
# Finite/infinite rounding threshold, including a sticky bit 2044 orders lower.
for sign in [1.,-1.]:
 for sticky in [0.,least,-least]:floats('overflow_threshold',[sign*maximum,sign*math.ldexp(1.0,970),sign*sticky])
# Sweep the normal exponent encoding and low-word offsets with cross-limb carry/borrow.
for exponent in range(1,2047):
 b=(exponent<<52)|((1<<52)-1)
 add('exponent_carry_borrow',[b,b,b|1<<63,1,1|1<<63])
# Physical signed coefficients near nu=.5 and nu=-1; the sum sees supplied rounded products.
for central in [bits(.5),bits(-1.),bits(0.)]:
 for delta in range(-8,9):
  b=central+delta
  if not 0<=b<(1<<64):continue
  nu=value(b)
  if not math.isfinite(nu):continue
  floats('source_coefficient',[1.,-2.*nu])
  floats('source_coefficient_signed',[-1.,2.*nu])
# Deterministic arbitrary finite bit patterns; cancellation may erase all high bits.
rng=random.Random(0x20260924)
for i in range(5000):
 operands=[]
 for _ in range(rng.randrange(1,40)):
  b=rng.getrandbits(64)
  if ((b>>52)&2047)==2047:b^=1<<52
  operands.append(b)
 if i%3==0:
  operands=operands+[b^(1<<63) for b in reversed(operands)]+[rng.randrange(1,1<<52)]
 add('random_finite_and_cancellation',operands)
# Permutations use an independently evaluated common exact sum; no order expectation from source.
for operand in [[bits(maximum),bits(-maximum),1,bits(1.),bits(-1.)], [bits(1.),bits(math.ldexp(1.,-53)),1,bits(-1.),bits(-math.ldexp(1.,-53))]]:
 for perm in itertools.permutations(operand):add('permutation',perm)
# Sustained carry propagation, large cancellation and nonzero exact remainder.
add('long_carry_cancel',[bits(maximum)]*10000+[bits(-maximum)]*10000+[1])
def oracle(case):
 xs=[value(int(b,16)) for b in case['operands']]
 if any(not math.isfinite(x) for x in xs):return 'ERR NonFinite'
 exact=sum((Fraction.from_float(x) for x in xs),Fraction(0))
 try: rounded=float(exact)
 except OverflowError:return 'ERR NonRepresentable'
 if not math.isfinite(rounded):return 'ERR NonRepresentable'
 # Exact zero is mathematical cancellation, intentionally canonical +0.
 return f'OK {bits(rounded):016x}'
start=time.time()
for c in cases:c['expected']=oracle(c)
(r/'oracle_cases.jsonl').write_text(''.join(json.dumps(c,separators=(',',':'))+'\n' for c in cases))
command=['rustc','--edition=2021',str(r/'sum_driver.rs'),'-o',str(r/'sum_driver')]
build=subprocess.run(command,text=True,capture_output=True);(r/'driver_build.log').write_text(build.stdout+build.stderr)
assert build.returncode==0,build.stderr
payload=''.join(' '.join(c['operands'])+'\n' for c in cases)
run=subprocess.run([str(r/'sum_driver')],input=payload,text=True,capture_output=True)
(r/'driver_output.log').write_text(run.stdout);(r/'driver_stderr.log').write_text(run.stderr)
assert run.returncode==0,run.stderr
observed=run.stdout.splitlines();assert len(observed)==len(cases)
failures=[{'index':i,'case':c,'observed':got} for i,(c,got) in enumerate(zip(cases,observed)) if c['expected']!=got]
counts={}
for c in cases:counts[c['kind']]=counts.get(c['kind'],0)+1
record={'source_sha256':expected_hash,'source_unchanged_after':hashlib.sha256(source.read_bytes()).hexdigest()==expected_hash,'oracle':'CPython fractions.Fraction exact sum of each finite input plus one CPython Fraction-to-binary64 rounding; compare all64 result bits. No product expected-value call.','seed':'0x20260924','cases':len(cases),'category_counts':counts,'failures':failures,'command':command,'build_exit':build.returncode,'run_exit':run.returncode,'python':sys.version,'rustc':subprocess.check_output(['rustc','--version','--verbose'],text=True),'elapsed_seconds':time.time()-start}
(r/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
(r/'sum_driver').unlink()
if failures:sys.exit(1)
