import hashlib, re, sys, pathlib
# Independent re-derivation of REGISTERED_PROFILES[0].reviewed_inputs from the archive's files.
root = pathlib.Path(sys.argv[1]) / "projects/chirality-piping/core/product_physics"
bi = (root / "src/build_identity.rs").read_text()
m = re.search(r"REVIEWED_INPUTS: \[&str; (\d+)\] = \[(.*?)\];", bi, re.S)
n = int(m.group(1)); paths = re.findall(r'^\s*"([^"]+)",', m.group(2), re.M)
assert len(paths) == n, (n, len(paths))
enc = "v1" + "".join(";%s=%s" % (p, hashlib.sha256((root / p).read_bytes()).hexdigest()) for p in paths)
rm = (root / "src/retained_memory.rs").read_text()
pins = re.findall(r'reviewed_inputs: "([^"]+)"', rm)
print("REVIEWED_INPUTS", n, "paths", len(paths), "registered entries", len(pins))
print("re-derived == pinned:", enc == pins[0])
br = (root / "build.rs").read_text()
print("build.rs array:", re.findall(r"digests: \[Option<\[u8; 32\]>; (\d+)\]", br))
print("encode array:", re.findall(r"encode_reviewed_inputs\(digests: &\[Option<\[u8; 32\]>; (\d+)\]\)", bi))
for p in paths: print(" ", hashlib.sha256((root / p).read_bytes()).hexdigest()[:16], p)
