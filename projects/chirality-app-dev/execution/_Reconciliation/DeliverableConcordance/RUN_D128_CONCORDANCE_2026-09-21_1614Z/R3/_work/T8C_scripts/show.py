"""Show source text for a ClaimKey from the frozen tree. Usage: show.py KEY [nlines]"""
import csv,sys,os,glob
RUN=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
F=os.environ['FROZEN']
key=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 25
base=key.split('#')[0]; local=key.split('#')[1] if '#' in key else ''
unit=local.split('.')[0]
if key.startswith('DEL-'):
    for r in csv.DictReader(open(os.path.join(RUN,'R1_INVENTORY','CLAIM_INDEX.csv'))):
        if r['ClaimKey']==f'{base}#{unit}':
            d=glob.glob(f"{F}/projects/chirality-app-dev/execution/PKG-*/1_Working/{base}_*")[0]
            p=os.path.join(d,r['SourceFile']); L=int(r['SourceLine'])
            print('##',r['SourceFile'],L,r['Section'],'|',r['Label'],'| sub:',r['SubItems'])
            lines=open(p).read().split('\n')
            for i in range(L-1,min(len(lines),L-1+n)): print(i+1, lines[i][:400])
            break
    else: print('no index row', key)
else:
    for r in csv.DictReader(open(os.path.join(RUN,'R1_INVENTORY','EXTENSION_INDEX.csv'))):
        if r['UnitKey']==key.split('.')[0] or r['UnitKey']==key:
            p=os.path.join(F,r['SourcePath']); L=int(r['SourceLine'])
            print('##',r['SourcePath'],L,'|',r['Label'][:200])
            lines=open(p).read().split('\n')
            for i in range(L-1,min(len(lines),L-1+n)): print(i+1, lines[i][:400])
            break
    else: print('no ext index row', key)
