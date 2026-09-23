#!/usr/bin/env python3
"""Focused, read-only artifact checks; write a single result alongside this script."""
from pathlib import Path
import hashlib, importlib.util, json, re
from html.parser import HTMLParser
from urllib.parse import unquote,urlsplit
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[3]
DOCS=ROOT/'docs/alignment-manual'
SOURCE=DOCS/'CHIRALITY_AGENT_USER_MANUAL_v3.md'
HTML=SOURCE.with_suffix('.html')
BASIS='b3e2ce4ec74e01d6f393fc0bc069699bb079df91'
DATE='2026-09-22'
md=MarkdownIt('commonmark',{'html':True}).enable(['table','strikethrough'])
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('manual_renderer',DOCS/'render_manual.py')
renderer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
class Audit(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True); self.events=[]; self.links=[]; self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and 'href' in a:self.links.append(a['href'])
  if tag=='div':return
  if tag in ('h1','h2','h3','h4','h5','h6'):a.pop('id',None)
  self.events.append(('open',tag,sorted(a.items())))
 def handle_endtag(self,tag):
  if tag!='div':self.events.append(('close',tag))
 def handle_data(self,data):
  text=' '.join(data.split())
  if text:self.events.append(('text',text))
source_text=SOURCE.read_text()
html_text=HTML.read_text()
body=html_text.split('<!-- BEGIN MARKDOWN CONTENT -->',1)[1].split('<!-- END MARKDOWN CONTENT -->',1)[0]
a,b=Audit(),Audit()
a.feed(md.render(source_text));b.feed(body)
parity=a.events==b.events
assert parity,'Markdown/HTML article content or links differ'
full=Audit();full.feed(html_text)
assert len(full.ids)==len(set(full.ids)),'duplicate rendered IDs'
cache={HTML:set(full.ids)}
def ids_for(p):
 if p in cache:return cache[p]
 raw=p.read_text()
 if p.suffix=='.html':
  parser=Audit();parser.feed(raw);ids=set(parser.ids)
 elif p.suffix=='.md':
  tokens=md.parse(raw);parser=Audit();parser.feed(md.render(raw));ids=set(parser.ids);counts={}
  for i,t in enumerate(tokens):
   if t.type=='heading_open':
    label=renderer.plain_text(md.renderer.renderInline(tokens[i+1].children or [],md.options,{}))
    slug=renderer.slugify(label)
    # Current links target explicit IDs or unique headings; repeated-heading IDs retained.
    n=counts.get(slug,0);counts[slug]=n+1
    ids.add(slug if n==0 else f'{slug}-{n}')
 else: ids=set()
 cache[p]=ids;return ids
broken=[]; local=set(); fragments=set(); external=set()
for href in full.links:
 u=urlsplit(href)
 if u.scheme or u.netloc:external.add(href);continue
 path=(HTML.parent/unquote(u.path)).resolve() if u.path else HTML
 local.add((str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),u.fragment))
 if not path.exists():broken.append({'href':href,'reason':'missing target'});continue
 if u.fragment:
  fragments.add(href)
  if unquote(u.fragment) not in ids_for(path):broken.append({'href':href,'reason':'missing fragment'})
assert not broken,broken
rendered1,summary1=renderer.render(SOURCE,HTML,DATE,BASIS)
rendered2,summary2=renderer.render(SOURCE,HTML,DATE,BASIS)
assert rendered1==rendered2==html_text,'non-deterministic or stale HTML'
assert sha(SOURCE) in html_text and BASIS in html_text,'missing source fingerprint'
assert 'Project_Management_for_Human_Agent_Teams_Consolidated_v5.md' not in source_text
assert 'Project_Management_for_Human_Agent_Teams_Consolidated_v7.md' in source_text
manifest=json.loads((Path(__file__).parent/'guide-sources.json').read_text())
assert manifest['inherited_v2_source_comparison']['all_changes_in_reviewed_amendment']
for s in manifest['inherited_v2_source_comparison']['sources']:
 assert sha(ROOT/s['path'])==s['current_sha256'],f"inherited source drift: {s['path']}"
for s in manifest['sources']:
 assert sha(ROOT/s['path'])==s['sha256'],f"source drift: {s['path']}"
result={'date':DATE,'basis_revision':BASIS,'result':'PASS','source':str(SOURCE.relative_to(ROOT)),'source_sha256':sha(SOURCE),'html':str(HTML.relative_to(ROOT)),'html_sha256':sha(HTML),'checks':{'source_html_article_parity':{'result':'PASS','canonical_events':len(a.events),'method':'Independent markdown-it rendering compared with HTML article tags, text and attributes; only generated heading IDs and table wrapper divs omitted.'},'local_links_and_fragments':{'result':'PASS','unique_local_targets_with_fragments':len(local),'fragment_links':len(fragments),'external_links_not_fetched':len(external),'broken':broken},'unique_rendered_ids':{'result':'PASS','count':len(full.ids)},'deterministic_render':{'result':'PASS','method':'Two maintained-renderer outputs equal each other and saved candidate bytes; explicit source/output/date/revision.'},'fingerprint':{'result':'PASS','source_sha256_present':True,'basis_revision_present':True},'v2_operating_sources':{'result':'PASS','unchanged_sources':manifest['inherited_v2_source_comparison']['unchanged_count'],'changed_sources_reexamined':manifest['inherited_v2_source_comparison']['changed_count']},'captured_source_hashes':{'result':'PASS','sources':len(manifest['sources'])}},'render_summary':summary1,'limits':['No new visual browser QA; prior local-HTML policy denial respected with no workaround.','No network link fetches, broad repository tests or product tests.','No execution or adoption inferred from illustrative examples.']}
(Path(__file__).parent/'guide-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'result':result['result'],'source_sha256':result['source_sha256'],'html_sha256':result['html_sha256'],'checks':{k:v['result'] for k,v in result['checks'].items()}},indent=2))
