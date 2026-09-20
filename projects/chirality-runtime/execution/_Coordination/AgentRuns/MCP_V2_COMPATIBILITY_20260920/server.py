import sys,json,datetime
from pathlib import Path
wire=Path(sys.argv[1])
V='2026-07-28'
P='io.modelcontextprotocol/'
def record(direction,frame):
 with wire.open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'direction':direction,'frame':frame})+'\n')
def send(frame):
 record('server-to-client',frame); print(json.dumps(frame,separators=(',',':')),flush=True)
def error(frame,code,message,data=None):
 result={'code':code,'message':message}
 if data is not None: result['data']=data
 send({'jsonrpc':'2.0','id':frame.get('id'),'error':result})
for line in sys.stdin:
 try: frame=json.loads(line)
 except Exception: continue
 record('client-to-server',frame)
 if 'id' not in frame: continue
 method=frame.get('method');params=frame.get('params') or {};meta=params.get('_meta') or {}
 if method=='initialize':
  error(frame,-32601,'This fixture accepts stateless MCP 2026-07-28 only; legacy initialize is unsupported.',{'supported':[V]});continue
 if P+'protocolVersion' not in meta or P+'clientCapabilities' not in meta:
  error(frame,-32602,'Missing required per-request MCP metadata.');continue
 if meta[P+'protocolVersion']!=V:
  error(frame,-32022,'Unsupported protocol version',{'supported':[V],'requested':meta[P+'protocolVersion']});continue
 if not isinstance(meta[P+'clientCapabilities'],dict):error(frame,-32602,'Invalid client capabilities');continue
 result={'resultType':'complete','_meta':{P+'serverInfo':{'name':'chirality-v2-compatibility-fixture','version':'0.0.0'}}}
 if method=='server/discover': result.update(supportedVersions=[V],capabilities={'tools':{}},instructions='Harmless isolated protocol fixture; no application data or side effects.')
 elif method=='tools/list':result['tools']=[{'name':'inspect_fixture','description':'Return the explicit invented workspace and basis references unchanged. No files or external state are read.','inputSchema':{'type':'object','properties':{'workspace':{'type':'string'},'basis':{'type':'string'}},'required':['workspace','basis'],'additionalProperties':False},'annotations':{'readOnlyHint':True,'destructiveHint':False,'idempotentHint':True,'openWorldHint':False}}]
 elif method=='tools/call':
  args=params.get('arguments')
  if params.get('name')!='inspect_fixture' or not isinstance(args,dict) or set(args)!= {'workspace','basis'} or not all(isinstance(v,str) for v in args.values()): error(frame,-32602,'Explicit workspace and basis are required');continue
  result.update(content=[{'type':'text','text':json.dumps(args,sort_keys=True)}],structuredContent=args,isError=False)
 else: error(frame,-32601,'Unknown method');continue
 send({'jsonrpc':'2.0','id':frame['id'],'result':result})
