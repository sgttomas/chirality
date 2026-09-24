//! Opt-in local carrier. The registered frontend alone owns domain state and Apply.
use crate::live_control_wire::{self as wire, Attachment, Request, WireError};
use serde::Serialize;
use serde_json::{json, Value};
use std::collections::HashMap;
use std::sync::{
    atomic::{AtomicBool, AtomicUsize, Ordering},
    mpsc, Arc, Mutex,
};
use tauri::{Emitter, Manager};

type Emit = Arc<dyn Fn(&str, Value) -> Result<(), WireError> + Send + Sync>;
#[derive(Clone)]
struct Registration {
    id: String,
    controller: String,
}
struct Pending {
    registration: Registration,
    request_id: String,
    sender: mpsc::Sender<Value>,
}
#[derive(Default)]
struct Registry {
    attachment: Option<Attachment>,
    registration: Option<Registration>,
    pending: HashMap<String, Pending>,
}
struct Inner {
    registry: Mutex<Registry>,
    emit: Mutex<Option<Emit>>,
    stopped: AtomicBool,
    connections: AtomicUsize,
    #[cfg(target_os = "macos")]
    owned: Mutex<Option<transport::OwnedPaths>>,
}
#[derive(Clone)]
pub struct LiveControl(Arc<Inner>);
impl Default for LiveControl {
    fn default() -> Self {
        Self(Arc::new(Inner {
            registry: Mutex::new(Registry::default()),
            emit: Mutex::new(None),
            stopped: AtomicBool::new(false),
            connections: AtomicUsize::new(0),
            #[cfg(target_os = "macos")]
            owned: Mutex::new(None),
        }))
    }
}
#[derive(Serialize)]
pub struct RegistrationResponse {
    enabled: bool,
    app_instance_id: Option<String>,
    registration_id: Option<String>,
    controller_session_id: String,
}
impl LiveControl {
    fn emit(&self, name: &str, value: Value) -> Result<(), WireError> {
        let emitter = self
            .0
            .emit
            .lock()
            .map_err(|_| WireError::new("internal_error"))?
            .clone();
        emitter.ok_or_else(|| WireError::new("controller_unavailable"))?(name, value)
    }
    fn cancel_event(&self, dispatch: &str, pending: &Pending, reason: &str) {
        let _ = self.emit("piping-live-control-cancel", json!({
            "registration_id":pending.registration.id, "controller_session_id":pending.registration.controller,
            "dispatch_id":dispatch, "request_id":pending.request_id, "reason":reason
        }));
    }
    fn register(&self, controller: String) -> Result<RegistrationResponse, WireError> {
        if controller.is_empty() || controller.len() > 512 {
            return Err(WireError::new("invalid_request"));
        }
        let mut registry = self
            .0
            .registry
            .lock()
            .map_err(|_| WireError::new("internal_error"))?;
        let Some(attachment) = registry.attachment.as_ref() else {
            return Ok(RegistrationResponse {
                enabled: false,
                app_instance_id: None,
                registration_id: None,
                controller_session_id: controller,
            });
        };
        if self.0.stopped.load(Ordering::Acquire) {
            return Err(WireError::new("controller_unavailable"));
        }
        let app_id = attachment.app_instance_id.clone();
        let registration = Registration {
            id: wire::random_id("reg-")?,
            controller: controller.clone(),
        };
        let old = std::mem::take(&mut registry.pending);
        registry.registration = Some(registration.clone());
        drop(registry);
        for (dispatch, pending) in old {
            self.cancel_event(&dispatch, &pending, "shutdown");
            let _ = pending
                .sender
                .send(json!({"error":WireError::new("outcome_unknown")}));
        }
        Ok(RegistrationResponse {
            enabled: true,
            app_instance_id: Some(app_id),
            registration_id: Some(registration.id),
            controller_session_id: controller,
        })
    }
    fn unregister(&self, registration_id: &str) -> Result<(), WireError> {
        let mut registry = self
            .0
            .registry
            .lock()
            .map_err(|_| WireError::new("internal_error"))?;
        if registry.registration.as_ref().map(|r| r.id.as_str()) != Some(registration_id) {
            return Err(WireError::new("controller_unavailable"));
        }
        registry.registration = None;
        let old = std::mem::take(&mut registry.pending);
        drop(registry);
        for (dispatch, pending) in old {
            self.cancel_event(&dispatch, &pending, "shutdown");
            let _ = pending
                .sender
                .send(json!({"error":WireError::new("outcome_unknown")}));
        }
        Ok(())
    }
    fn begin(&self, request: &Request) -> Result<(String, mpsc::Receiver<Value>), WireError> {
        let mut registry = self
            .0
            .registry
            .lock()
            .map_err(|_| WireError::new("internal_error"))?;
        let attachment = registry
            .attachment
            .as_ref()
            .ok_or_else(|| WireError::new("controller_unavailable"))?;
        wire::validate_request(request, attachment)?;
        if self.0.stopped.load(Ordering::Acquire) {
            return Err(WireError::new("controller_unavailable"));
        }
        let registration = registry
            .registration
            .clone()
            .ok_or_else(|| WireError::new("not_ready"))?;
        if registry.pending.len() >= wire::MAX_IN_FLIGHT {
            return Err(WireError::new("capacity"));
        }
        // Request IDs are correlation, not recovery authority. Concurrent reuse is rejected;
        // a later reuse still receives a newly minted dispatch ID.
        if registry
            .pending
            .values()
            .any(|p| p.request_id == request.request_id)
        {
            return Err(WireError::new("invalid_request"));
        }
        let dispatch = wire::random_id("dispatch-")?;
        let event = json!({"registration_id":registration.id, "controller_session_id":registration.controller,
            "dispatch_id":dispatch, "request_id":request.request_id, "app_instance_id":attachment.app_instance_id,
            "method":request.method, "params":request.params});
        let (sender, receiver) = mpsc::channel();
        registry.pending.insert(
            dispatch.clone(),
            Pending {
                registration,
                request_id: request.request_id.clone(),
                sender,
            },
        );
        drop(registry);
        if self.emit("piping-live-control-request", event).is_err() {
            self.cancel(&dispatch, "shutdown");
            return Err(WireError::new("outcome_unknown"));
        }
        Ok((dispatch, receiver))
    }
    fn reply(
        &self,
        registration_id: &str,
        dispatch_id: &str,
        response: Value,
    ) -> Result<(), WireError> {
        wire::validate_reply(&response)?;
        let mut registry = self
            .0
            .registry
            .lock()
            .map_err(|_| WireError::new("internal_error"))?;
        if registry.registration.as_ref().map(|r| r.id.as_str()) != Some(registration_id) {
            return Err(WireError::new("controller_unavailable"));
        }
        let pending = registry
            .pending
            .get(dispatch_id)
            .ok_or_else(|| WireError::new("invalid_request"))?;
        if pending.registration.id != registration_id {
            return Err(WireError::new("controller_unavailable"));
        }
        let app_id = &registry
            .attachment
            .as_ref()
            .ok_or_else(|| WireError::new("controller_unavailable"))?
            .app_instance_id;
        let response = if wire::encode_frame(&wire::envelope(
            app_id,
            &pending.request_id,
            response.clone(),
        ))
        .is_ok()
        {
            response
        } else {
            json!({"error":WireError::new("frame_too_large")})
        };
        let pending = registry
            .pending
            .remove(dispatch_id)
            .ok_or_else(|| WireError::new("invalid_request"))?;
        pending
            .sender
            .send(response)
            .map_err(|_| WireError::new("outcome_unknown"))
    }
    fn cancel(&self, dispatch_id: &str, reason: &str) {
        let pending = self
            .0
            .registry
            .lock()
            .ok()
            .and_then(|mut r| r.pending.remove(dispatch_id));
        if let Some(pending) = pending {
            self.cancel_event(dispatch_id, &pending, reason);
        }
    }
    pub fn shutdown(&self) {
        self.0.stopped.store(true, Ordering::Release);
        let pending = self
            .0
            .registry
            .lock()
            .ok()
            .map(|mut r| {
                r.registration = None;
                std::mem::take(&mut r.pending)
            })
            .unwrap_or_default();
        for (dispatch, pending) in pending {
            self.cancel_event(&dispatch, &pending, "shutdown");
            let _ = pending
                .sender
                .send(json!({"error":WireError::new("outcome_unknown")}));
        }
        #[cfg(target_os = "macos")]
        if let Ok(mut paths) = self.0.owned.lock() {
            if let Some(paths) = paths.take() {
                paths.cleanup();
            }
        }
    }
}

fn main_window(window: &tauri::WebviewWindow) -> Result<(), WireError> {
    if window.label() != "main" {
        return Err(WireError::new("unauthorized"));
    }
    Ok(())
}
#[tauri::command]
pub fn live_control_register(
    window: tauri::WebviewWindow,
    state: tauri::State<'_, LiveControl>,
    controller_session_id: String,
) -> Result<RegistrationResponse, WireError> {
    main_window(&window)?;
    state.register(controller_session_id)
}
#[tauri::command]
pub fn live_control_reply(
    window: tauri::WebviewWindow,
    state: tauri::State<'_, LiveControl>,
    registration_id: String,
    dispatch_id: String,
    response: Value,
) -> Result<(), WireError> {
    main_window(&window)?;
    state.reply(&registration_id, &dispatch_id, response)
}
#[tauri::command]
pub fn live_control_unregister(
    window: tauri::WebviewWindow,
    state: tauri::State<'_, LiveControl>,
    registration_id: String,
) -> Result<(), WireError> {
    main_window(&window)?;
    state.unregister(&registration_id)
}
pub fn setup(app: &mut tauri::App) -> Result<(), Box<dyn std::error::Error>> {
    if let Err(error) = setup_enabled(app) {
        app.state::<LiveControl>().shutdown();
        // All setup errors below are fixed public diagnostics, never OS paths or secrets.
        eprintln!("Live control disabled: {error}. The desktop remains available.");
    }
    Ok(())
}
fn setup_enabled(app: &mut tauri::App) -> Result<(), Box<dyn std::error::Error>> {
    if std::env::var("SWBPIPE_LIVE_CONTROL").as_deref() != Ok("1") {
        return Ok(());
    }
    #[cfg(not(target_os = "macos"))]
    {
        return Err("unsupported_host: live control requires macOS".into());
    }
    #[cfg(target_os = "macos")]
    {
        // Validate generated configuration rather than accepting a caller label.
        if app.config().app.windows.len() != 1 || app.config().app.windows[0].label != "main" {
            return Err("live control requires the configured main webview".into());
        }
        let window = app
            .get_webview_window("main")
            .ok_or("live control main webview unavailable")?;
        let state = app.state::<LiveControl>().inner().clone();
        *state
            .0
            .emit
            .lock()
            .map_err(|_| "live control registry unavailable")? =
            Some(Arc::new(move |event, payload| {
                window
                    // Explicit target routing; supplier Any listeners are still eligible.
                    // Local-main ACL admission and registration/source guards remain required.
                    .emit_to(tauri::EventTarget::webview_window("main"), event, payload)
                    .map_err(|_| WireError::new("controller_unavailable"))
            }));
        transport::start(state).map_err(|_| "live control private endpoint unavailable")?;
        Ok(())
    }
}

#[cfg(target_os = "macos")]
mod transport {
    use super::*;
    use std::fs::{self, DirBuilder, OpenOptions};
    use std::io::{Read, Write};
    use std::os::unix::{
        fs::{DirBuilderExt, MetadataExt, OpenOptionsExt, PermissionsExt},
        net::{UnixListener, UnixStream},
    };
    use std::path::{Path, PathBuf};
    use std::time::{Duration, Instant};
    struct Identity {
        dev: u64,
        ino: u64,
    }
    impl Identity {
        fn at(path: &Path) -> std::io::Result<Self> {
            let m = fs::symlink_metadata(path)?;
            Ok(Self {
                dev: m.dev(),
                ino: m.ino(),
            })
        }
        fn matches(&self, path: &Path) -> bool {
            Self::at(path)
                .map(|m| m.dev == self.dev && m.ino == self.ino)
                .unwrap_or(false)
        }
    }
    pub(super) struct OwnedPaths {
        directory: PathBuf,
        directory_id: Identity,
        files: Vec<(PathBuf, Identity)>,
    }
    impl OwnedPaths {
        pub(super) fn cleanup(self) {
            if !self.directory_id.matches(&self.directory) {
                return;
            }
            for (path, identity) in self.files {
                if identity.matches(&path) {
                    let _ = fs::remove_file(path);
                }
            }
            let _ = fs::remove_dir(self.directory);
        }
    }
    pub(super) fn start(state: LiveControl) -> Result<(), WireError> {
        // /private/tmp is canonical on macOS; a random exclusive child avoids long sun_path values.
        let directory =
            PathBuf::from("/private/tmp").join(wire::random_id("swbp-")?[..25].to_owned());
        DirBuilder::new()
            .mode(0o700)
            .create(&directory)
            .map_err(|_| WireError::new("internal_error"))?;
        let mut owned = OwnedPaths {
            directory_id: Identity::at(&directory).map_err(|_| WireError::new("internal_error"))?,
            directory: directory.clone(),
            files: vec![],
        };
        let created = (|| {
            wire::private_fs::private_dir(&directory)?;
            let socket = directory.join("control.sock");
            let listener =
                UnixListener::bind(&socket).map_err(|_| WireError::new("internal_error"))?;
            owned.files.push((
                socket.clone(),
                Identity::at(&socket).map_err(|_| WireError::new("internal_error"))?,
            ));
            fs::set_permissions(&socket, fs::Permissions::from_mode(0o600))
                .map_err(|_| WireError::new("internal_error"))?;
            listener
                .set_nonblocking(true)
                .map_err(|_| WireError::new("internal_error"))?;
            let attachment = Attachment {
                protocol_version: wire::PROTOCOL_VERSION,
                app_instance_id: wire::random_id("app-")?,
                socket_path: socket.to_string_lossy().into_owned(),
                capability: wire::random_id("")?,
            };
            let descriptor = directory.join("attachment.json");
            let mut file = OpenOptions::new()
                .write(true)
                .create_new(true)
                .mode(0o600)
                .open(&descriptor)
                .map_err(|_| WireError::new("internal_error"))?;
            owned.files.push((
                descriptor.clone(),
                Identity::at(&descriptor).map_err(|_| WireError::new("internal_error"))?,
            ));
            serde_json::to_writer(&mut file, &attachment)
                .map_err(|_| WireError::new("internal_error"))?;
            file.sync_all()
                .map_err(|_| WireError::new("internal_error"))?;
            state
                .0
                .registry
                .lock()
                .map_err(|_| WireError::new("internal_error"))?
                .attachment = Some(attachment);
            Ok((listener, descriptor))
        })();
        let (listener, descriptor) = match created {
            Ok(v) => v,
            Err(e) => {
                owned.cleanup();
                return Err(e);
            }
        };
        *state
            .0
            .owned
            .lock()
            .map_err(|_| WireError::new("internal_error"))? = Some(owned);
        let listener_state = state.clone();
        let spawned = std::thread::Builder::new()
            .name("piping-live-listener".into())
            .spawn(move || {
                let state = listener_state;
                while !state.0.stopped.load(Ordering::Acquire) {
                    match listener.accept() {
                        Ok((mut stream, _)) => {
                            if state
                                .0
                                .connections
                                .fetch_update(Ordering::AcqRel, Ordering::Acquire, |n| {
                                    (n < wire::MAX_IN_FLIGHT).then_some(n + 1)
                                })
                                .is_err()
                            {
                                let app = app_id(&state);
                                let _ = stream.set_write_timeout(Some(Duration::from_millis(100)));
                                send(
                                    &mut stream,
                                    &wire::failure(&app, None, WireError::new("capacity")),
                                );
                                continue;
                            }
                            let child = state.clone();
                            if std::thread::Builder::new()
                                .name("piping-live-request".into())
                                .spawn(move || {
                                    struct Permit(LiveControl);
                                    impl Drop for Permit {
                                        fn drop(&mut self) {
                                            self.0 .0.connections.fetch_sub(1, Ordering::AcqRel);
                                        }
                                    }
                                    let _permit = Permit(child.clone());
                                    serve(child, stream);
                                })
                                .is_err()
                            {
                                state.0.connections.fetch_sub(1, Ordering::AcqRel);
                            }
                        }
                        Err(e) if e.kind() == std::io::ErrorKind::WouldBlock => {
                            std::thread::sleep(Duration::from_millis(20))
                        }
                        Err(_) => {
                            state.shutdown();
                            break;
                        }
                    }
                }
            });
        if spawned.is_err() {
            state.shutdown();
            return Err(WireError::new("internal_error"));
        }
        // Only path, never descriptor content or capability.
        eprintln!("{}", descriptor.display());
        Ok(())
    }
    fn app_id(state: &LiveControl) -> String {
        state
            .0
            .registry
            .lock()
            .ok()
            .and_then(|r| r.attachment.as_ref().map(|a| a.app_instance_id.clone()))
            .unwrap_or_default()
    }
    fn send(stream: &mut UnixStream, response: &Value) {
        let encoded = wire::encode_frame(response).or_else(|_| {
            wire::encode_frame(&wire::failure(
                response["app_instance_id"].as_str().unwrap_or(""),
                None,
                WireError::new("frame_too_large"),
            ))
        });
        if let Ok(bytes) = encoded {
            let _ = stream.write_all(&bytes);
        }
    }
    fn serve(state: LiveControl, mut stream: UnixStream) {
        let deadline = Instant::now() + wire::REQUEST_DEADLINE;
        let _ = stream.set_read_timeout(Some(Duration::from_millis(20)));
        let _ = stream.set_write_timeout(Some(Duration::from_secs(1)));
        let app = app_id(&state);
        let bytes = match wire::read_frame(&mut stream, deadline) {
            Ok(bytes) => bytes,
            Err(error) => {
                send(&mut stream, &wire::failure(&app, None, error));
                return;
            }
        };
        let request: Request = match serde_json::from_slice(&bytes) {
            Ok(request) => request,
            Err(_) => {
                send(
                    &mut stream,
                    &wire::failure(&app, None, WireError::new("invalid_request")),
                );
                return;
            }
        };
        if Instant::now() >= deadline {
            send(
                &mut stream,
                &wire::failure(
                    &app,
                    Some(&request.request_id),
                    WireError::new("outcome_unknown"),
                ),
            );
            return;
        }
        let (dispatch, receiver) = match state.begin(&request) {
            Ok(v) => v,
            Err(error) => {
                send(
                    &mut stream,
                    &wire::failure(&app, Some(&request.request_id), error),
                );
                return;
            }
        };
        loop {
            match receiver.try_recv() {
                Ok(response) => {
                    send(
                        &mut stream,
                        &wire::envelope(&app, &request.request_id, response),
                    );
                    return;
                }
                Err(mpsc::TryRecvError::Disconnected) => {
                    send(
                        &mut stream,
                        &wire::failure(
                            &app,
                            Some(&request.request_id),
                            WireError::new("outcome_unknown"),
                        ),
                    );
                    return;
                }
                Err(mpsc::TryRecvError::Empty) => {}
            }
            if Instant::now() >= deadline {
                state.cancel(&dispatch, "timeout");
                send(
                    &mut stream,
                    &wire::failure(
                        &app,
                        Some(&request.request_id),
                        WireError::new("outcome_unknown"),
                    ),
                );
                return;
            }
            // Reading after the single request detects disconnect without retaining an
            // unbounded reader thread. Any second frame is invalid on this connection.
            let mut byte = [0u8; 1];
            match stream.read(&mut byte) {
                Ok(0) => {
                    state.cancel(&dispatch, "disconnect");
                    return;
                }
                Ok(_) => {
                    state.cancel(&dispatch, "disconnect");
                    send(
                        &mut stream,
                        &wire::failure(
                            &app,
                            Some(&request.request_id),
                            WireError::new("invalid_request"),
                        ),
                    );
                    return;
                }
                Err(e)
                    if matches!(
                        e.kind(),
                        std::io::ErrorKind::WouldBlock
                            | std::io::ErrorKind::TimedOut
                            | std::io::ErrorKind::Interrupted
                    ) => {}
                Err(_) => {
                    state.cancel(&dispatch, "disconnect");
                    return;
                }
            }
        }
    }
    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn socket_carrier_routes_historical_result_and_redacts_capability() {
            let state = LiveControl::default();
            state.0.registry.lock().unwrap().attachment = Some(Attachment {
                protocol_version: 1,
                app_instance_id: "a".into(),
                socket_path: "unused".into(),
                capability: "secret".into(),
            });
            let (events, requests) = mpsc::channel();
            *state.0.emit.lock().unwrap() = Some(Arc::new(move |name, value| {
                events.send((name.to_owned(), value)).unwrap();
                Ok(())
            }));
            let registration = state
                .register("controller".into())
                .unwrap()
                .registration_id
                .unwrap();
            let (mut client, server) = UnixStream::pair().unwrap();
            client
                .set_read_timeout(Some(Duration::from_secs(2)))
                .unwrap();
            let worker = state.clone();
            let task = std::thread::spawn(move || serve(worker, server));
            let request = json!({"protocol_version":1,"request_id":"r","app_instance_id":"a","capability":"secret","method":"status","params":{"workspace":"old","ticket":"t"}});
            client
                .write_all(&wire::encode_frame(&request).unwrap())
                .unwrap();
            let (name, event) = requests.recv_timeout(Duration::from_secs(2)).unwrap();
            assert_eq!(name, "piping-live-control-request");
            assert!(event.get("capability").is_none());
            state
                .reply(
                    &registration,
                    event["dispatch_id"].as_str().unwrap(),
                    json!({"result":{"workspace":"old","state":"committed"}}),
                )
                .unwrap();
            let bytes =
                wire::read_frame(&mut client, Instant::now() + Duration::from_secs(2)).unwrap();
            let response: Value = serde_json::from_slice(&bytes).unwrap();
            assert_eq!(response["request_id"], "r");
            assert_eq!(response["app_instance_id"], "a");
            assert_eq!(response["result"]["workspace"], "old");
            assert!(!String::from_utf8(bytes).unwrap().contains("secret"));
            task.join().unwrap();
        }
        #[test]
        fn disconnect_cancels_original_dispatch_without_claiming_absence() {
            let state = LiveControl::default();
            state.0.registry.lock().unwrap().attachment = Some(Attachment {
                protocol_version: 1,
                app_instance_id: "a".into(),
                socket_path: "unused".into(),
                capability: "secret".into(),
            });
            let (events, requests) = mpsc::channel();
            *state.0.emit.lock().unwrap() = Some(Arc::new(move |name, value| {
                events.send((name.to_owned(), value)).unwrap();
                Ok(())
            }));
            let registration = state
                .register("controller".into())
                .unwrap()
                .registration_id
                .unwrap();
            let (mut client, server) = UnixStream::pair().unwrap();
            let worker = state.clone();
            let task = std::thread::spawn(move || serve(worker, server));
            client.write_all(&wire::encode_frame(&json!({"protocol_version":1,"request_id":"r","app_instance_id":"a","capability":"secret","method":"submit","params":{}})).unwrap()).unwrap();
            let (_, dispatch) = requests.recv_timeout(Duration::from_secs(2)).unwrap();
            drop(client);
            let (name, cancel) = requests.recv_timeout(Duration::from_secs(2)).unwrap();
            assert_eq!(name, "piping-live-control-cancel");
            assert_eq!(cancel["reason"], "disconnect");
            assert_eq!(cancel["dispatch_id"], dispatch["dispatch_id"]);
            assert_eq!(cancel["registration_id"], registration);
            task.join().unwrap();
            assert!(state.0.registry.lock().unwrap().pending.is_empty());
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    fn fixture() -> (LiveControl, Arc<Mutex<Vec<(String, Value)>>>) {
        let state = LiveControl::default();
        state.0.registry.lock().unwrap().attachment = Some(Attachment {
            protocol_version: 1,
            app_instance_id: "fixture-app".into(),
            socket_path: "unused".into(),
            capability: "synthetic-fixture-capability".into(),
        });
        let events = Arc::new(Mutex::new(vec![]));
        let captured = events.clone();
        *state.0.emit.lock().unwrap() = Some(Arc::new(move |name, value| {
            captured.lock().unwrap().push((name.into(), value));
            Ok(())
        }));
        (state, events)
    }
    fn request(id: &str) -> Request {
        Request {
            protocol_version: 1,
            request_id: id.into(),
            app_instance_id: "fixture-app".into(),
            capability: "synthetic-fixture-capability".into(),
            method: "status".into(),
            params: json!({"workspace":"old","ticket":"ticket"}),
        }
    }
    #[test]
    fn registration_replacement_and_correlation_are_not_caller_controlled() {
        let (state, events) = fixture();
        assert_eq!(state.begin(&request("r")).err().unwrap().code, "not_ready");
        let first = state
            .register("controller-a".into())
            .unwrap()
            .registration_id
            .unwrap();
        let (dispatch, receiver) = state.begin(&request("r")).unwrap();
        assert!(state.begin(&request("r")).is_err());
        let second = state
            .register("controller-b".into())
            .unwrap()
            .registration_id
            .unwrap();
        assert_eq!(receiver.recv().unwrap()["error"]["code"], "outcome_unknown");
        assert!(state.unregister(&first).is_err());
        assert!(state
            .reply(&first, &dispatch, json!({"result":{}}))
            .is_err());
        let (next, receiver) = state.begin(&request("r")).unwrap();
        assert_ne!(dispatch, next);
        state
            .reply(
                &second,
                &next,
                json!({"result":{"workspace":"old","state":"committed"}}),
            )
            .unwrap();
        assert_eq!(receiver.recv().unwrap()["result"]["workspace"], "old");
        assert!(state.reply(&second, &next, json!({"result":{}})).is_err());
        let events = events.lock().unwrap();
        assert!(events.iter().all(|(_, v)| v.get("capability").is_none()));
        assert_eq!(
            events
                .iter()
                .find(|(n, _)| n == "piping-live-control-cancel")
                .unwrap()
                .1["registration_id"],
            first
        );
    }
    #[test]
    fn admission_and_cancel_preserve_successor() {
        let (state, events) = fixture();
        state.register("c".into()).unwrap();
        let mut dispatches = vec![];
        for n in 0..wire::MAX_IN_FLIGHT {
            dispatches.push(state.begin(&request(&n.to_string())).unwrap());
        }
        assert_eq!(
            state.begin(&request("overflow")).err().unwrap().code,
            "capacity"
        );
        state.cancel(&dispatches[0].0, "timeout");
        state.begin(&request("after-cancel")).unwrap();
        assert_eq!(
            events
                .lock()
                .unwrap()
                .iter()
                .filter(|(n, _)| n == "piping-live-control-cancel")
                .count(),
            1
        );
        state.shutdown();
        assert!(state.begin(&request("after-shutdown")).is_err());
    }
    #[test]
    fn disabled_is_inert() {
        let state = LiveControl::default();
        let reply = state.register("c".into()).unwrap();
        assert!(!reply.enabled);
        assert!(reply.app_instance_id.is_none());
        assert!(reply.registration_id.is_none());
    }
    #[test]
    fn authentication_and_method_errors_never_dispatch() {
        let (state, events) = fixture();
        state.register("c".into()).unwrap();
        let mut r = request("r");
        r.capability = "bad".into();
        assert_eq!(state.begin(&r).err().unwrap().code, "unauthorized");
        r = request("r");
        r.app_instance_id = "other".into();
        assert_eq!(state.begin(&r).err().unwrap().code, "wrong_app");
        r = request("r");
        r.method = "apply".into();
        assert_eq!(state.begin(&r).err().unwrap().code, "unsupported_method");
        assert!(events.lock().unwrap().is_empty());
    }
}
