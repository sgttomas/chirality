import { writeFile, mkdir, rm } from "node:fs/promises";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import assert from "node:assert/strict";
const { computeRuntimeArtifactDigest, createControlledArtifactGenerationForTests } = await import(pathToFileURL(resolve("packages/core/dist/runtime-conformance.js")).href);
const fixture = resolve(import.meta.dirname, "generation-fixture");
await mkdir(fixture, {recursive:true});
try {
 const modulePath=resolve(fixture,"module.mjs");
 await writeFile(modulePath,'export const generation = "A";\n');
 const lockPath=resolve(fixture,"lock.json"); await writeFile(lockPath,"{}\n");
 const generation=createControlledArtifactGenerationForTests(async()=>({sourceFiles:[modulePath],packageFiles:[lockPath]}));
 await generation.createVerifier().verify();
 const loadedA=await import(pathToFileURL(modulePath).href);
 const digestA=await computeRuntimeArtifactDigest([modulePath]);
 await writeFile(modulePath,'export const generation = "B";\n');
 const digestB=await computeRuntimeArtifactDigest([modulePath]);
 const stillLoaded=await import(pathToFileURL(modulePath).href);
 assert.notEqual(digestA,digestB);
 await assert.rejects(generation.createVerifier().verify());
 await writeFile(modulePath,'export const generation = "A";\n');
 await assert.rejects(generation.createVerifier().verify());
 assert.equal(loadedA.generation,"A"); assert.equal(stillLoaded.generation,"A");
 console.log(JSON.stringify({diskDigestChanged:true,cachedGeneration:stillLoaded.generation,changedGenerationDenied:true,restoredGenerationStillDenied:true,limitation:"Cache/digest reproduction only; no production admission or owner acceptance is performed"},null,2));
} finally {await rm(fixture,{recursive:true,force:true});}
