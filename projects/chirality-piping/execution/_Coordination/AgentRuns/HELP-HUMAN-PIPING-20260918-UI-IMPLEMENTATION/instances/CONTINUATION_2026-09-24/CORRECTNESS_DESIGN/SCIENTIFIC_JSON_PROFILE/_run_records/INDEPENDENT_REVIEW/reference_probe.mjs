// Independent Node/V8 reference observations; no product module or WASM import.
import assert from 'node:assert/strict';
import {writeFileSync,readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
const base=new URL('.',import.meta.url);
const py=JSON.parse(readFileSync(new URL('PYTHON_REFERENCE.json',base),'utf8'));
const bits=n=>{const b=Buffer.alloc(8);b.writeDoubleBE(n);return b.toString('hex')};
const value=h=>Buffer.from(h,'hex').readDoubleBE();
const hash=s=>createHash('sha256').update(s,'utf8').digest('hex');
const parsed=[];
for(const row of [...py.ordinary_tokens,...py.exact_midpoints]){
  const n=JSON.parse(row.token);
  if(row.outcome==='overflow') assert.equal(Number.isFinite(n),false);
  else assert.equal(bits(n),row.bits);
  parsed.push({token:row.token,bits:bits(n),stringify:JSON.stringify(n)});
}
// All 24 finite entries in RFC8785 AppendixB, algorithm references only.
const appendix=[
 ['0000000000000000','0'],['8000000000000000','0'],
 ['0000000000000001','5e-324'],['8000000000000001','-5e-324'],
 ['7fefffffffffffff','1.7976931348623157e+308'],['ffefffffffffffff','-1.7976931348623157e+308'],
 ['4340000000000000','9007199254740992'],['c340000000000000','-9007199254740992'],
 ['4430000000000000','295147905179352830000'],
 ['44b52d02c7e14af5','9.999999999999997e+22'],['44b52d02c7e14af6','1e+23'],['44b52d02c7e14af7','1.0000000000000001e+23'],
 ['444b1ae4d6e2ef4e','999999999999999700000'],['444b1ae4d6e2ef4f','999999999999999900000'],['444b1ae4d6e2ef50','1e+21'],
 ['3eb0c6f7a0b5ed8c','9.999999999999997e-7'],['3eb0c6f7a0b5ed8d','0.000001'],
 ['41b3de4355555553','333333333.3333332'],['41b3de4355555554','333333333.33333325'],
 ['41b3de4355555555','333333333.3333333'],['41b3de4355555556','333333333.3333334'],
 ['41b3de4355555557','333333333.33333343'],['becbf647612f3696','-0.0000033333333333333333'],
 ['43143ff3c1cb0959','1424953923781206.2']];
for(const [h,text] of appendix)assert.equal(JSON.stringify(value(h)),text);
assert.equal(JSON.stringify(JSON.parse('18446744073709551615')),'18446744073709552000');
assert.equal(JSON.stringify(JSON.parse('1e160')),'1e+160');
assert.equal(JSON.stringify(JSON.parse('1e20')),'100000000000000000000');
assert.equal(Number.isSafeInteger(-0),true);
assert.equal(Object.is(JSON.parse('-0'),-0),true);
assert.equal(JSON.stringify(-0),'0');
assert.equal(JSON.stringify(NaN),'null');
assert.equal(JSON.stringify(Infinity),'null');
assert.equal(JSON.stringify([,undefined]),'[null,null]');
assert.equal(JSON.stringify({x:undefined}),'{}');
assert.throws(()=>JSON.stringify(1n));
let getterCount=0;
JSON.stringify({get x(){getterCount++;return 1;}});
assert.equal(getterCount,1);
const rawA='{"x":9007199254740993}',rawB='{"x":9007199254740992}';
const semantic=JSON.stringify(JSON.parse(rawA));
assert.equal(semantic,JSON.stringify(JSON.parse(rawB)));
assert.notEqual(hash(rawA),hash(rawB));
const F=1e-306,A=596902.6041820607,pa=F/A,mpa=pa/1e6;
assert.equal(bits(pa),py.stress_units.pa_bits);assert.equal(bits(mpa),py.stress_units.mpa_bits);
const result={status:'PASS',node:process.version,v8:process.versions.v8,product_execution:false,
 scope:'Node built-in reference probes only; no Rust authority or WASM qualification',
 parsed,appendix_b_finite_vectors:appendix.length,
 js_hazards:{minus_zero_is_safe_integer:true,minus_zero_stringifies:'0',nonfinite_stringifies:'null',
 arrays_erase_undefined_and_holes:true,object_undefined_omitted:true,getter_invoked:true,bigint_throws:true},
 identity_collision:{raw_A:rawA,raw_B:rawB,raw_A_sha256:hash(rawA),raw_B_sha256:hash(rawB),
 same_semantic_text:semantic,same_semantic_sha256:hash(semantic)},
 stress_units:{pa_bits:bits(pa),mpa_bits:bits(mpa)},
 script_sha256:createHash('sha256').update(readFileSync(new URL(import.meta.url))).digest('hex')};
writeFileSync(new URL('NODE_REFERENCE.json',base),JSON.stringify(result,null,2)+'\n');
process.stdout.write(JSON.stringify({status:'PASS',parsed_tokens:parsed.length,appendix_b_finite_vectors:appendix.length,product_execution:false})+'\n');
