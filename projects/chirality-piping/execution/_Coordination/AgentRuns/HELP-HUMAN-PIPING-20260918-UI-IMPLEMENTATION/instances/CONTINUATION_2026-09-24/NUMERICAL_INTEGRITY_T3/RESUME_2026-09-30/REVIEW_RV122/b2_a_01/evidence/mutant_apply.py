import sys, pathlib, importlib.util
spec = importlib.util.spec_from_file_location("d", sys.argv[1]); d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
pristine, target, mid = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
text = pristine.read_text()
if mid == "LIST":
    for m in d.M: print(m[0])
    sys.exit(0)
for (i, check, old, new) in d.M:
    if i == mid:
        n = text.count(old)
        if n != 1: raise SystemExit(f"{i}: old occurs {n} times")
        target.write_text(text.replace(old, new)); print(f"{i}\t{check}"); break
else:
    raise SystemExit("unknown " + mid)
