// RV126: run the wasm32 norm over the triples file; write norm3,norm2 bits per triple.
import { readFileSync, writeFileSync } from "node:fs";
const [wasmPath, inPath, outPath] = process.argv.slice(2);
const { instance } = await WebAssembly.instantiate(readFileSync(wasmPath), {});
const { memory, buf, run } = instance.exports;
const input = readFileSync(inPath);
const n = input.length / 24;
const out = Buffer.alloc(16 * n);
const CH = 20000; // 20000*24 + 20000*16 = 800000 < 1 MiB
for (let s = 0; s < n; s += CH) {
  const m = Math.min(CH, n - s);
  const base = buf();
  new Uint8Array(memory.buffer, base, 24 * m).set(input.subarray(24 * s, 24 * (s + m)));
  run(m);
  out.set(new Uint8Array(memory.buffer, base + 24 * m, 16 * m), 16 * s);
}
writeFileSync(outPath, out);
console.log(`wasm32: ${n} triples`);
