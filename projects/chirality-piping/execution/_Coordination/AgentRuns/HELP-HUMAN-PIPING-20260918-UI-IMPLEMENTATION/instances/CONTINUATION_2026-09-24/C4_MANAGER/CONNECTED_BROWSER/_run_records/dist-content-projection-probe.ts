import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import * as THREE from "three";
import {buildModelIndex} from "./src/features/workspace/modelIndex";
import {pointPickPrimitives,authoredToLocal} from "./src/features/viewport/viewportSelection";
import {projectLabelAnchor,projectLabelPickTargets} from "./src/features/viewport/labelProjection";
import {placeMeasuredLabel,labelRectsOverlap} from "./src/features/viewport/labelPlacement";
const root=process.cwd(),records=process.argv[2],read=(p:string)=>JSON.parse(fs.readFileSync(p,"utf8")),sha=(p:string)=>crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
const modelPath=path.join(root,"projects/chirality-piping/fixtures/product_preview/invented_preview_model.json");const model=read(modelPath);const index=buildModelIndex(model,1,1);
const d=read(path.join(records,"dist-content-diagnostic-15-before-selected-pipe-keyboard-measurement.json"));const v=d.snapshot.viewport,c=v.camera,origin={x:c.localRenderOrigin[0],y:c.localRenderOrigin[1],z:c.localRenderOrigin[2]},width=v.canvas.cssWidth,height=v.canvas.cssHeight;
const camera=new THREE.PerspectiveCamera(c.fovDegrees,c.aspect,c.near,c.far);camera.position.fromArray(c.position).sub(new THREE.Vector3(...c.localRenderOrigin));camera.up.fromArray(c.up);camera.lookAt(new THREE.Vector3(...c.target).sub(new THREE.Vector3(...c.localRenderOrigin)));camera.updateMatrixWorld();
const primitives=pointPickPrimitives(index,model,origin);const exclusions=primitives.map(p=>({key:p.key,primitive:p,rects:projectLabelPickTargets({primitives:[p],camera,width,height,hiddenKeys:new Set(),actualOdRadiusByPipe:new Map()})}));
const key=JSON.stringify(["pipe","pipe:P-100"]),dom=d.labels.find((x:any)=>x.key===key),anchor=authoredToLocal(index.entities.get(key)!.anchor!,origin),projected=projectLabelAnchor(anchor,camera,width,height),label={...projected,width:dom.rect.width,height:dom.rect.height};
const directions=[[1,-1],[1,1],[-1,-1],[-1,1],[0,-1],[0,1],[1,0],[-1,0]],candidates=[];
for(const ring of [1,2,3]) for(const [dx,dy] of directions){const x=label.x+dx*(label.width/2+4+(ring-1)*(label.width+4)),y=label.y+dy*(label.height/2+4+(ring-1)*(label.height+4));const rect={left:x-label.width/2,right:x+label.width/2,top:y-label.height/2,bottom:y+label.height/2};candidates.push({ring,dx,dy,rect,blockedBy:exclusions.filter(e=>e.rects.some(r=>labelRectsOverlap(rect,r))).map(e=>e.key)});}
const sourcePaths=["modelIndex.ts"].map(()=>"projects/chirality-piping/apps/desktop/src/features/workspace/modelIndex.ts").concat(["viewportSelection.ts","labelProjection.ts","labelPlacement.ts","labelCollisionIndex.ts"].map(x=>"projects/chirality-piping/apps/desktop/src/features/viewport/"+x));
const result={kind:"offline reconstruction from exact observed camera/model/DOM dimensions; no browser or product mutation",sourceHashes:Object.fromEntries(sourcePaths.map(p=>[p,sha(path.join(root,p))])),modelHash:sha(modelPath),diagnosticHash:sha(path.join(records,"dist-content-diagnostic-15-before-selected-pipe-keyboard-measurement.json")),camera:c,width,height,label,dom,exclusions,candidates,all:placeMeasuredLabel(label,{width,height},[],exclusions.flatMap(e=>e.rects)),withoutOwn:placeMeasuredLabel(label,{width,height},[],exclusions.filter(e=>e.key!==key).flatMap(e=>e.rects)),byPrimitive:exclusions.map(e=>({key:e.key,result:placeMeasuredLabel(label,{width,height},[],e.rects)}))};
fs.writeFileSync(path.join(records,"dist-content-projection-probe-result.json"),JSON.stringify(result,null,2)+"\n");console.log(JSON.stringify({label,all:result.all,withoutOwn:result.withoutOwn,blockers:result.byPrimitive.filter(x=>!x.result.rect),candidateBlockers:candidates.map(x=>x.blockedBy)},null,2));
