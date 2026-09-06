from pathlib import Path
import re,json,hashlib
root=Path(__file__).resolve().parents[7]
css=root/'projects/chirality-app-dev/frontend/src/app/globals.css'
text=css.read_text()
start=text.index('/* SCA-APP-010 Stone presentation.')
source=text[start:]
blocks={name:re.search(pattern,source).group(1) for name,pattern in {'light':r'\.woven-workspace \{([^}]+)\}','dark':r':root\[data-theme="dark"\] \.woven-workspace \{([^}]+)\}'}.items()}
def lum(h):
 c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 c=[x/12.92 if x<=0.04045 else ((x+0.055)/1.055)**2.4 for x in c]
 return sum(a*b for a,b in zip(c,[0.2126,0.7152,0.0722]))
rows=[]
for theme,block in blocks.items():
 tokens=dict(re.findall(r'(--[a-z-]+):\s*(#[0-9a-f]{6});',block))
 for fg,bg in [(x,y) for x in ['--ink','--ink-soft','--ink-faint','--brand-ink'] for y in ['--ground','--surface']]+[('--cta-ink','--cta')]:
  a,b=sorted([lum(tokens[fg]),lum(tokens[bg])]);ratio=(b+0.05)/(a+0.05)
  rows.append({'theme':theme,'foregroundToken':fg,'backgroundToken':bg,'foreground':tokens[fg],'background':tokens[bg],'ratio':round(ratio,4),'normalText4_5':ratio>=4.5})
out={'source':str(css.relative_to(root)),'sourceSha256':hashlib.sha256(css.read_bytes()).hexdigest(),'method':'sRGB relative luminance, (Lmax+0.05)/(Lmin+0.05)','claim':'Source-token text contrast calculation only; not a rendered opacity/compositing or whole-interface accessibility audit. Decorative rules and disabled controls excluded.','rows':rows,'allDeclaredTextPairsPass':all(x['normalText4_5'] for x in rows)}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'pairs':len(rows),'minimum':min(x['ratio'] for x in rows),'pass':out['allDeclaredTextPairsPass']}))
