import pathlib,json,hashlib,sys
import subprocess
r=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
m=json.loads(pathlib.Path(__file__).with_name('TRANSFORMATION.json').read_text())
h=lambda b:hashlib.sha256(b).hexdigest()
s=(r/m['canonical_source']).read_bytes();assert h(s)==m['canonical_source_sha256']
f=s[m['source_byte_offset']:m['source_byte_offset']+m['fixture_byte_length']];assert h(f)==m['fixture_sha256']
n=json.dumps(f.decode(),ensure_ascii=True)[1:-1].encode();assert len(n)==m['encoded_length']
b=(r/m['target']).read_bytes();assert h(b)==m['postimage_sha256']
k=m['marker'].encode();i=m['capture_byte_offset'];assert b.count(k)==1 and b[i:i+len(k)]==k
original=b[:i]+n+b[i+len(k):];assert h(original)==m['preimage_sha256']
print(json.dumps({'reconstruction':'PASS','preimage_sha256':h(original),'postimage_sha256':h(b),'source_sha256':h(s),'original_persisted':False}))
