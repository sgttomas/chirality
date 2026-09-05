#!/usr/bin/env python3
"""Restore original lock-pinned host packages without network or install scripts."""
import argparse, base64, hashlib, json, os, platform, shutil, tarfile
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);ap.add_argument('--target',required=True);ap.add_argument('--cache',required=True);ap.add_argument('--result',required=True);a=ap.parse_args()
source=Path(a.source);target=Path(a.target);cache_root=Path(a.cache);d=json.loads((source/'package-lock.json').read_text());host='darwin' if platform.system()=='Darwin' else platform.system().lower();arch={'aarch64':'arm64','x86_64':'x64'}.get(platform.machine(),platform.machine());result={'host':host,'arch':arch,'lock_sha256':hashlib.sha256((source/'package-lock.json').read_bytes()).hexdigest(),'packages':[],'links':[],'scripts_executed':False,'network_used':False}
modules=target/'node_modules'
if modules.exists():shutil.rmtree(modules)
modules.mkdir(parents=True)
for key,v in sorted(d['packages'].items()):
 if not key.startswith('node_modules/') or v.get('link'):continue
 if v.get('os') and host not in v['os']:continue
 if v.get('cpu') and arch not in v['cpu']:continue
 integrity=v.get('integrity');assert integrity,(key,'missing integrity')
 alg,b64=integrity.split(' ',1)[0].split('-',1);h=base64.b64decode(b64).hex();cache=cache_root/'_cacache/content-v2'/alg/h[:2]/h[2:4]/h[4:];assert hashlib.new(alg,cache.read_bytes()).hexdigest()==h,key
 dest=target/key;dest.mkdir(parents=True,exist_ok=True)
 with tarfile.open(cache,'r:gz') as t:
  members=[]
  for m in t.getmembers():
   m.name=m.name.split('/',1)[1] if '/' in m.name else ''
   if m.name:members.append(m)
  t.extractall(dest,members=members,filter='data')
 package=json.loads((dest/'package.json').read_text());assert package['version']==v['version'],(key,package['version'],v['version'])
 result['packages'].append({'path':key,'version':v['version'],'integrity':integrity,'package_json_sha256':hashlib.sha256((dest/'package.json').read_bytes()).hexdigest()})
for key,v in d['packages'].items():
 if not key.startswith('node_modules/') or not v.get('link'):continue
 dest=target/key;dest.parent.mkdir(parents=True,exist_ok=True);to=(target/v['resolved']).resolve();dest.symlink_to(to);result['links'].append({'path':key,'target':str(to)})
for item in result['packages']:
 dest=target/item['path'];package=json.loads((dest/'package.json').read_text());bins=package.get('bin',{})
 if isinstance(bins,str):bins={package['name'].split('/')[-1]:bins}
 module_root=dest.parent.parent if dest.parent.name.startswith('@') else dest.parent
 bindir=module_root/'.bin';bindir.mkdir(exist_ok=True)
 for name,path in bins.items():
  src=dest/path
  if not src.is_file():continue
  src.chmod(src.stat().st_mode|0o111);link=bindir/name
  if not link.exists() and not link.is_symlink():link.symlink_to(os.path.relpath(src,bindir))
Path(a.result).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'packages':len(result['packages']),'links':len(result['links']),'versions':'PASS','integrities':'PASS'}))
