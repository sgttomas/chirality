import { readFileSync, writeFileSync, readdirSync, mkdirSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { resolve, dirname } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createHash } from "node:crypto";
import { isDeepStrictEqual } from "node:util";
const repo=execFileSync("git",["rev-parse","--show-toplevel"],{encoding:"utf8"}).trim();
const raw=dirname(fileURLToPath(import.meta.url)), prior=resolve(raw,"optional-wall-probe"), out=resolve(raw,"FINAL_CHECKS_R3/optional-wall-replay");
mkdirSync(out,{recursive:true});
const assets=resolve(repo,"projects/chirality-piping/apps/desktop/public/wasm-engine");
const engine=await import(pathToFileURL(resolve(assets,"open_pipe_stress_operation_applier.js")).href);
engine.initSync({module:readFileSync(resolve(assets,"open_pipe_stress_operation_applier_bg.wasm"))});
const names=readdirSync(prior).filter(x=>/^(bound|unbound)-.*\.json$/.test(x)).sort();
if(names.length!==10)throw new Error("Expected exact ten preserved inputs");
const results=[];
for(const name of names){
 const originalBytes=readFileSync(resolve(prior,name)),old=JSON.parse(originalBytes),{model,intent,shouldApply}=old;
 const validation=JSON.parse(engine.validate_operation_json(JSON.stringify(model),JSON.stringify(intent),"null"));
 const applied=JSON.parse(engine.apply_operation_json(JSON.stringify(model),JSON.stringify(intent),"null"));
 const expected=structuredClone(model); expected.pipe_segments[0].section.mill_tolerance=JSON.parse(intent.change.after);
 const okay=Boolean(applied.applied_model)===shouldApply && validation.applied_model===null && validation.input_model_unchanged===true && applied.input_model_unchanged===true && (shouldApply?isDeepStrictEqual(applied.applied_model,expected):applied.diff_preview.length===0&&validation.diff_preview.length===0);
 const result={name,prior_input_file_sha256:createHash("sha256").update(originalBytes).digest("hex"),model,intent,shouldApply,validation,applied,okay};
 writeFileSync(resolve(out,name),JSON.stringify(result,null,2)+"\n"); results.push({name,shouldApply,actualApplied:Boolean(applied.applied_model),codes:applied.diagnostics.map(x=>x.code),okay});
}
writeFileSync(resolve(out,"summary.json"),JSON.stringify(results,null,2)+"\n");
writeFileSync(resolve(out,"identity.json"),JSON.stringify({repo,node:process.version,assets:readdirSync(assets).map(name=>({name,sha256:createHash("sha256").update(readFileSync(resolve(assets,name))).digest("hex")}))},null,2)+"\n");
console.log(JSON.stringify(results,null,2));process.exitCode=results.every(x=>x.okay)?0:1;
