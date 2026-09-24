from pathlib import Path
import hashlib, json
r = Path("projects/chirality-piping")
base = r / "apps/desktop/src-tauri"
source = base / "capabilities/live-control.json"
expected = json.loads(source.read_text())
assert set(expected) == {"identifier", "description", "local", "webviews", "permissions"}
assert expected["local"] is True and expected["webviews"] == ["main"]
assert expected["permissions"] == ["core:event:allow-listen", "core:event:allow-unlisten"]
paths = [base / "gen/schemas/capabilities.json", *sorted((base / "target/debug/build").glob("openpipestress-desktop-*/out/capabilities.json"))]
assert len(paths) >= 3
artifacts = {}
for path in paths:
    value = json.loads(path.read_text())
    assert set(value) == {"live-control"}, str(path)
    assert value["live-control"] == expected, str(path)
    artifacts[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
manifest_path = base / "gen/schemas/acl-manifests.json"
manifest = json.loads(manifest_path.read_text())["core:event"]
resolved = {}
for permission, command in [("allow-listen", "listen"), ("allow-unlisten", "unlisten")]:
    definition = manifest["permissions"][permission]
    assert definition["commands"] == {"allow": [command], "deny": []}
    resolved["core:event:" + permission] = definition
for path in [source, manifest_path, base / "gen/schemas/desktop-schema.json", base / "src/live_control.rs", r / "apps/desktop/src/services/liveControlBridge.ts"]:
    artifacts[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
native = (base / "src/live_control.rs").read_text()
frontend = (r / "apps/desktop/src/services/liveControlBridge.ts").read_text()
assert '.emit_to(tauri::EventTarget::webview_window("main"), event, payload)' in native
assert frontend.count('target: { kind: "WebviewWindow", label: "main" }') == 2
print(json.dumps({"result": "PASS", "generated_capability": expected, "resolved_permissions": resolved, "artifact_sha256": artifacts, "sender_receiver_target": "WebviewWindow/main on both native events and frontend listeners", "limits": "Build-time/source admission and routing evidence only. Tauri Any listeners may also receive targeted events. No actual runtime handshake or non-main denial was exercised."}, indent=2))
