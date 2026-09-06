// Preparation only: start after a fresh accepted production build and exact source freeze.
// Fixture data replaces recorded-session list/agents only; root/file policy and IPC stay production.
const http=require('node:http');
const fs=require('node:fs');
const path=require('node:path');
const config=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const observations=[];
const fixtureSessions=[
 {sessionId:'reveal-native-alpha',projectRoot:config.rootA,persona:'WORKING_ITEMS',mode:'read-only',createdAt:'2026-09-06T12:00:00.000Z',updatedAt:'2026-09-06T12:00:00.000Z'},
 {sessionId:'reveal-native-beta',projectRoot:config.rootB,persona:'HELP_HUMAN',mode:'read-only',createdAt:'2026-09-05T12:00:00.000Z',updatedAt:'2026-09-05T12:00:00.000Z'},
 {sessionId:'reveal-native-missing',projectRoot:config.rootMissing,persona:'RESEARCH',mode:'read-only',createdAt:'2026-09-04T12:00:00.000Z',updatedAt:'2026-09-04T12:00:00.000Z'}
];
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');
 if(url.pathname==='/api/harness/session/list'||url.pathname==='/api/harness/agents'){
  observations.push({time:new Date().toISOString(),path:url.pathname,projectRoot:url.searchParams.get('projectRoot')});
  fs.writeFileSync(path.join(__dirname,'fixture-reads.json'),JSON.stringify(observations,null,2));
  res.writeHead(200,{'content-type':'application/json','cache-control':'no-store'});
  res.end(JSON.stringify(url.pathname.endsWith('/agents')?{agents:[{name:'WORKING_ITEMS',type:1,class:'PERSONA'},{name:'HELP_HUMAN',type:0,class:'PERSONA'}]}:{sessions:fixtureSessions}));return;
 }
 if(url.pathname.startsWith('/api/harness/')){res.writeHead(503,{'content-type':'application/json'});res.end(JSON.stringify({error:'Isolated native Reveal fixture: runtime actions unavailable.'}));return;}
 const upstream=http.request({hostname:'127.0.0.1',port:config.productionPort,path:req.url,method:req.method,headers:{...req.headers,host:`127.0.0.1:${config.productionPort}`}},r=>{res.writeHead(r.statusCode,r.headers);r.pipe(res)});
 upstream.on('error',()=>{res.writeHead(502);res.end('Owned production server unavailable.');});req.pipe(upstream);
});
server.listen(config.proxyPort,'127.0.0.1',()=>console.log(JSON.stringify({pid:process.pid,fixture:'synthetic native Reveal only',proxyPort:config.proxyPort,productionPort:config.productionPort})));
process.on('SIGTERM',()=>server.close(()=>process.exit(0)));
