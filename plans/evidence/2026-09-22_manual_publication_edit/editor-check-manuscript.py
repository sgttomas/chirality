from pathlib import Path
from collections import Counter
import hashlib,json,re,sys
source=Path('/Users/ryan/Library/CloudStorage/ProtonDrive-Ryan.Tufts@protonmail.com-folder/GBT/Project_Management_for_Human_Agent_Teams_Consolidated_v3.md')
candidate=Path(sys.argv[1])
t= candidate.read_text()
s=source.read_text()
anchors=re.findall(r'<a id="([^"]+)"',t)
refs=re.findall(r'\]\(#([^)]+)\)',t)
body=t.split('# Selected References')[0]
cites=re.findall(r'\[([0-9][0-9,– -]*)\](?!\()',body)
nums=[]
for group in cites:
 for part in group.split(','):
  part=part.strip()
  if re.fullmatch(r'\d+',part): nums.append(int(part))
  elif re.fullmatch(r'\d+[–-]\d+',part):
   a,b=map(int,re.split('[–-]',part));nums.extend(range(a,b+1))
selected=[int(n) for n in re.findall(r'\*\*\[(\d+)\]\*\*',t.split('# Selected References')[-1])]
caption_labels=re.findall(r'^\*Figure ((?:[0-9]+|A)\.[0-9]+)\.',t,re.M)
figure_mentions=set(re.findall(r'\bFigure ((?:[0-9]+|A)\.[0-9]+)\b',t))
imgs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',t)
local_images=[{'reference':x,'exists':(candidate.parent/x).exists()} for x in imgs if not x.startswith(('http:','https:','data:'))]
strict_patterns={
'book_drafting_history':r'Edition [234]|for author review|offered for (?:his|her|author) review|supplied (?:v[1234]|manuscript|archive)|original manuscript|earlier edition|this edition|author[’\']s (?:directions|clarifications)|repository comparison|h_repository_application',
'operational_interfaces':r'Application note|Chirality application notes|LOOP_INIT|SOW_V1|MODE=|AllowedWriteTargets|PROFILE_PATH|TaskManagement|Task Management|ScopeOfWork\.md|_STATUS\.md|\.zip\b|D-GOV-\d+',
'editorial_markers':r'\[SMITH\]|TODO|TBD|FIXME|\[INSERT|\[PLACEHOLDER'
}
flags={k:[{'line':i,'text':line} for i,line in enumerate(t.splitlines(),1) if re.search(p,line,re.I if k=='book_drafting_history' else 0)] for k,p in strict_patterns.items()}

def prose(text,source_mode=False):
 out=[];para=[];fenced=False;skip=False
 def flush():
  if para:
   raw=' '.join(para)
   norm=re.sub(r'\s*\[\d[\d, –-]*\](?!\()','',raw)
   norm=re.sub(r'\s+',' ',norm).strip()
   out.append(norm);para.clear()
 for line in text.splitlines():
  if line.startswith('# '):
   flush()
   if source_mode:
    if re.match(r'# (Chirality application notes|Sources for Chapter|Appendix A)',line):skip=True
    elif re.match(r'# [1-7]\. |# Working vocabulary',line):skip=False
   else:
    if line=='# Selected References':skip=True
  if skip:continue
  if line.startswith('```'):
   flush();fenced=not fenced;continue
  if fenced:continue
  if not line.strip():flush();continue
  if re.match(r'^(#|<a |\||!\[|\*Figure |\*[^*]|[-+] |\d+\. )',line):flush();continue
  para.append(line)
 flush();return out
sp=prose(s,True);cp=prose(t)
cp_set=set(cp)
retained=[p for p in sp if p in cp_set]
table_blocks=[];table_block=[];in_fence=False;wide_specimens=[]
for line_number,line in enumerate(t.splitlines(),1):
 if line.startswith('```'):
  if table_block:table_blocks.append(table_block);table_block=[]
  in_fence=not in_fence;continue
 if in_fence:
  if len(line)>70:wide_specimens.append({'line':line_number,'columns':len(line)})
  continue
 if line.startswith('|'):table_block.append((line_number,line))
 elif table_block:table_blocks.append(table_block);table_block=[]
if table_block:table_blocks.append(table_block)
table_issues=[]
for table in table_blocks:
 columns=[len(re.findall(r'(?<!\\)\|',row))-1 for _,row in table]
 if len(set(columns))>1:table_issues.append({'start':table[0][0],'columns':columns})
local_file_links=[{'reference':link,'exists':(candidate.parent/link.split('#',1)[0]).exists()} for link in re.findall(r'\]\(([^)]+)\)',t) if not link.startswith(('#','http:','https:','data:','mailto:'))]
report={
'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'source_unchanged':hashlib.sha256(source.read_bytes()).hexdigest()=='c245f0ebdd0e88185a085c47c0bb697a5831a6fba94b3418e355a883b3398cf1',
'words':len(t.split()),'lines':len(t.splitlines()),'anchors':len(anchors),'duplicate_anchors':[a for a,n in Counter(anchors).items() if n>1],'missing_internal_targets':sorted(set(refs)-set(anchors)),'fences_even':sum(x.startswith('```') for x in t.splitlines())%2==0,
'citation_numbers_used':sorted(set(nums)),'selected_reference_numbers':selected,'unmapped_citations':sorted(set(nums)-set(selected)),'uncited_numbered_references':sorted(set(selected)-set(nums)),'figure_captions':caption_labels,'duplicate_caption_numbers':[a for a,n in Counter(caption_labels).items() if n>1],'missing_figure_captions':sorted(figure_mentions-set(caption_labels)),
'images':local_images,'local_file_links':local_file_links,'table_blocks':len(table_blocks),'table_column_issues':table_issues,'specimen_lines_over_70_columns':wide_specimens,'blank_lines_splitting_table_candidates':[t.count('\n',0,m.start())+1 for m in re.finditer(r'(?m)^\|.*\|\n[ \t]*\n\|',t)],'consecutive_duplicate_headings':re.findall(r'(?m)^(#{2,4} [^\n]+)\n\s*\n\1$',t),'review_flags':flags,
'prose_preservation':{'normalization':'Whitespace and chapter-local numeric citations removed for comparison; source application notes, source lists, and historical appendix excluded; this mechanical count is not a judgment of semantic preservation.','source_body_prose_paragraphs':len(sp),'unchanged_normalized_paragraphs':len(retained),'unchanged_fraction':round(len(retained)/len(sp),4),'source_body_words_in_unchanged_paragraphs':sum(len(p.split()) for p in retained),'source_body_prose_words':sum(len(p.split()) for p in sp)}
}
print(json.dumps(report,indent=2,ensure_ascii=False))
