from pathlib import Path
import datetime, hashlib, json, os, subprocess, tempfile, time
root = Path("/private/tmp/piping-live-control-20260924")
r = root / "projects/chirality-piping"
base = r / "apps/desktop/src-tauri"
out = r / "execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/LIVE_MANAGER/INTEGRATION/NATIVE/SELF_TEST"
binary = base / "target/debug/bundle/macos/SWBPIPE.app/Contents/MacOS/openpipestress-desktop"
expected = "b5cf18a7aab4975c3c95a717bf5ebc3de5e62730b7dd81d5f799e7de6183d9ef"
sha = lambda data: hashlib.sha256(data).hexdigest()
assert sha(binary.read_bytes()) == expected
parent = Path(tempfile.mkdtemp(prefix="packaged-self-test-", dir=base / "target"))
os.chmod(parent, 0o700)
sentinel = parent / "sibling-sentinel.txt"
sentinel.write_bytes(b"Preserve this unrelated sibling of the wrapper-owned smoke directory.\n")
sentinel_hash = sha(sentinel.read_bytes())
def snapshot():
    entries = []
    for p in sorted(parent.rglob("*")):
        try:
            stat = p.lstat()
            entries.append({"path": str(p), "relative": str(p.relative_to(parent)), "kind": "directory" if p.is_dir() else "file", "size": stat.st_size})
        except FileNotFoundError:
            pass
    return entries
before = snapshot()
env = os.environ.copy()
env.pop("SWBPIPE_LIVE_CONTROL", None)
env["TMPDIR"] = str(parent) + "/"
argv = [str(binary), "--self-test-saved-edited-load"]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
observations = []
timed_out = False
with (out / "stdout.raw").open("wb") as stdout, (out / "stderr.raw").open("wb") as stderr:
    process = subprocess.Popen(argv, cwd=root, env=env, stdout=stdout, stderr=stderr)
    (out / "RUN_STARTED.json").write_text(json.dumps({"pid": process.pid, "argv": argv, "cwd": str(root), "start_utc": started, "binary_sha256": expected, "TMPDIR": str(parent), "SWBPIPE_LIVE_CONTROL_present": False, "HOME_overridden": False, "parent_mode": oct(parent.stat().st_mode & 0o777), "before": before}, indent=2))
    deadline = time.monotonic() + 60
    previous = None
    while process.poll() is None:
        current = snapshot()
        if current != previous:
            observations.append({"time_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "entries": current})
            previous = current
        if time.monotonic() >= deadline:
            timed_out = True
            process.kill()
            break
        time.sleep(0.001)
    exit_code = process.wait()
after = snapshot()
observed_smoke = sorted({entry["path"] for observation in observations for entry in observation["entries"] if entry["kind"] == "directory" and Path(entry["path"]).name.startswith("openpipestress-packaged-edited-load-smoke-")})
stdout = (out / "stdout.raw").read_bytes()
stderr = (out / "stderr.raw").read_bytes()
try:
    result = json.loads(stdout)
except (ValueError, UnicodeDecodeError):
    result = None
record = {"pid": process.pid, "argv": argv, "cwd": str(root), "start_utc": started, "end_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "exit_code": exit_code, "timed_out": timed_out, "binary_pre_sha256": expected, "binary_post_sha256": sha(binary.read_bytes()), "TMPDIR": str(parent), "SWBPIPE_LIVE_CONTROL_present": False, "HOME_overridden": False, "parent_mode": oct(parent.stat().st_mode & 0o777), "before": before, "during": observations, "after": after, "observed_wrapper_directories": observed_smoke, "observed_wrapper_paths_removed": {p: not Path(p).exists() for p in observed_smoke}, "wrapper_name_matches_child_pid": all(("smoke-" + str(process.pid) + "-") in p for p in observed_smoke), "sentinel_unchanged": sentinel.exists() and sha(sentinel.read_bytes()) == sentinel_hash, "sentinel_sha256": sentinel_hash, "stdout_sha256": sha(stdout), "stdout_bytes": len(stdout), "stderr_sha256": sha(stderr), "stderr_bytes": len(stderr), "result": result, "manual_temp_cleanup": False, "process_complete": True}
(out / "RUN_RESULT.json").write_text(json.dumps(record, indent=2))
print(json.dumps({"pid": process.pid, "exit_code": exit_code, "status": result.get("status") if isinstance(result, dict) else None, "observed_wrapper_directories": observed_smoke, "wrapper_paths_removed": record["observed_wrapper_paths_removed"], "sentinel_unchanged": record["sentinel_unchanged"], "stderr_bytes": len(stderr), "private_parent_retained": str(parent)}, indent=2))
if exit_code != 0 or timed_out or not isinstance(result, dict) or result.get("status") != "PASS":
    raise SystemExit(1)
assert record["binary_post_sha256"] == expected
assert record["sentinel_unchanged"]
