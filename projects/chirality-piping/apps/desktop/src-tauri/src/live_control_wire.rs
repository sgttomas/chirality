//! Version-one carrier protocol. Domain parameters/results stay controller-owned.
use serde::{Deserialize, Serialize};
use serde_json::{json, Value};
use std::io::{self, Read};
use std::time::{Duration, Instant};

pub const PROTOCOL_VERSION: u32 = 1;
pub const MAX_FRAME_BYTES: usize = 1_048_576;
pub const MAX_DESCRIPTOR_BYTES: usize = 16_384;
pub const MAX_IN_FLIGHT: usize = 16;
pub const REQUEST_DEADLINE: Duration = Duration::from_secs(30);
pub const METHODS: [&str; 4] = ["inspect", "preview", "submit", "status"];

// Deliberately no Debug: descriptors and requests contain capabilities.
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Attachment {
    pub protocol_version: u32,
    pub app_instance_id: String,
    pub socket_path: String,
    pub capability: String,
}
#[derive(Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Request {
    pub protocol_version: u32,
    pub request_id: String,
    pub app_instance_id: String,
    pub capability: String,
    pub method: String,
    pub params: Value,
}
#[derive(Clone, Debug, Serialize, Deserialize, PartialEq)]
#[serde(deny_unknown_fields)]
pub struct WireError {
    pub code: String,
    pub message: String,
    pub retryable: bool,
    pub next_action: String,
}
impl WireError {
    pub fn new(code: &str) -> Self {
        let (message, retryable, next_action) = match code {
            "outcome_unknown" => ("The outcome could not be delivered.", true, "For submit, retry the original workspace, preview and idempotency key; otherwise reconcile by status or inspect."),
            "not_ready" | "controller_unavailable" => ("The live controller is not ready.", true, "Wait for the controller; recover submit with the original workspace, preview and idempotency key."),
            "capacity" | "busy" => ("The carrier has reached its admission limit.", true, "Wait and retry the original request; preserve the original workspace, preview and idempotency key."),
            "unauthorized" | "wrong_app" => ("The attachment does not authorize this app.", false, "Use the descriptor emitted by the intended running app and reconcile any earlier submit."),
            "unsupported_host" => ("Live control requires macOS.", false, "Use the development macOS host."),
            "unsupported_method" => ("This method is not available.", false, "Use inspect, preview, submit or status. Apply belongs to the local review UI."),
            "unsupported_protocol" => ("The protocol version is unsupported.", false, "Use a version-one CLI and attachment."),
            "frame_too_large" => ("The frame exceeds the carrier limit.", false, "Send one smaller JSON object within the documented frame limit."),
            "invalid_request" => ("The request or attachment is malformed or unsafe.", false, "Check the documented exact JSON shape and private attachment; reconcile any earlier submit."),
            _ => ("The carrier could not complete the request.", false, "Reconcile by status; for an uncertain submit retry only the original workspace, preview and idempotency key."),
        };
        Self {
            code: code.into(),
            message: message.into(),
            retryable,
            next_action: next_action.into(),
        }
    }
}
pub fn random_id(prefix: &str) -> Result<String, WireError> {
    let mut bytes = [0u8; 32];
    getrandom::fill(&mut bytes).map_err(|_| WireError::new("internal_error"))?;
    let hex: String = bytes.iter().map(|b| format!("{b:02x}")).collect();
    Ok(format!("{prefix}{hex}"))
}
pub fn failure(app: &str, request_id: Option<&str>, error: WireError) -> Value {
    json!({"protocol_version": PROTOCOL_VERSION, "request_id": request_id,
        "app_instance_id": app, "error": error})
}
pub fn envelope(app: &str, request_id: &str, response: Value) -> Value {
    let mut result = json!({"protocol_version": PROTOCOL_VERSION, "request_id": request_id,
        "app_instance_id": app});
    let obj = result.as_object_mut().expect("object");
    if let Some(value) = response.get("result") {
        obj.insert("result".into(), value.clone());
    } else if let Some(value) = response.get("error") {
        obj.insert("error".into(), value.clone());
    }
    result
}
pub fn validate_reply(value: &Value) -> Result<(), WireError> {
    let object = value
        .as_object()
        .ok_or_else(|| WireError::new("invalid_request"))?;
    if object.len() != 1 {
        return Err(WireError::new("invalid_request"));
    }
    if object.contains_key("result") {
        return Ok(());
    }
    if let Some(error) = object.get("error") {
        let parsed: WireError =
            serde_json::from_value(error.clone()).map_err(|_| WireError::new("invalid_request"))?;
        const CODES: &[&str] = &[
            "invalid_request",
            "unsupported_protocol",
            "unauthorized",
            "wrong_app",
            "unsupported_host",
            "unsupported_method",
            "unsupported_change",
            "frame_too_large",
            "capacity",
            "not_ready",
            "controller_unavailable",
            "busy",
            "stale_basis",
            "wrong_workspace",
            "unknown_preview",
            "unknown_ticket",
            "idempotency_conflict",
            "cancelled_before_publication",
            "expired",
            "outcome_unknown",
            "internal_error",
        ];
        if CODES.contains(&parsed.code.as_str()) {
            return Ok(());
        }
    }
    Err(WireError::new("invalid_request"))
}
pub fn encode_frame(value: &Value) -> Result<Vec<u8>, WireError> {
    let mut bytes = serde_json::to_vec(value).map_err(|_| WireError::new("internal_error"))?;
    if bytes.len() >= MAX_FRAME_BYTES {
        return Err(WireError::new("frame_too_large"));
    }
    bytes.push(b'\n');
    Ok(bytes)
}
/// Reads exactly one newline-terminated frame without unbounded allocation.
/// Socket callers additionally install a read timeout. Deadline covers slow trickles.
pub fn read_frame(reader: &mut impl Read, deadline: Instant) -> Result<Vec<u8>, WireError> {
    let mut bytes = Vec::new();
    let mut byte = [0u8; 1];
    loop {
        if Instant::now() >= deadline {
            return Err(WireError::new("outcome_unknown"));
        }
        match reader.read(&mut byte) {
            Ok(0) => return Err(WireError::new("invalid_request")),
            Ok(_) => {
                bytes.push(byte[0]);
                if bytes.len() > MAX_FRAME_BYTES {
                    return Err(WireError::new("frame_too_large"));
                }
                if byte[0] == b'\n' {
                    return Ok(bytes);
                }
                if bytes.len() == MAX_FRAME_BYTES {
                    return Err(WireError::new("frame_too_large"));
                }
            }
            Err(error) if error.kind() == io::ErrorKind::Interrupted => continue,
            Err(error)
                if matches!(
                    error.kind(),
                    io::ErrorKind::TimedOut | io::ErrorKind::WouldBlock
                ) =>
            {
                continue
            }
            Err(_) => return Err(WireError::new("invalid_request")),
        }
    }
}
pub fn validate_request(request: &Request, attachment: &Attachment) -> Result<(), WireError> {
    if request.protocol_version != PROTOCOL_VERSION {
        return Err(WireError::new("unsupported_protocol"));
    }
    if request.app_instance_id != attachment.app_instance_id {
        return Err(WireError::new("wrong_app"));
    }
    // Fixed-length random capability; compare every byte before returning.
    let a = request.capability.as_bytes();
    let b = attachment.capability.as_bytes();
    let mismatch = a.len() ^ b.len();
    let difference = a
        .iter()
        .zip(b.iter())
        .fold(0u8, |acc, (a, b)| acc | (a ^ b));
    if mismatch != 0 || difference != 0 {
        return Err(WireError::new("unauthorized"));
    }
    if request.request_id.is_empty() || !request.params.is_object() {
        return Err(WireError::new("invalid_request"));
    }
    if !METHODS.contains(&request.method.as_str()) {
        return Err(WireError::new("unsupported_method"));
    }
    Ok(())
}

#[cfg(target_os = "macos")]
pub mod private_fs {
    use super::*;
    use std::fs::{self, File, OpenOptions};
    use std::os::unix::fs::{FileTypeExt, MetadataExt, OpenOptionsExt};
    use std::path::{Component, Path};
    unsafe extern "C" {
        fn getuid() -> u32;
    }
    pub fn uid() -> u32 {
        unsafe { getuid() }
    }
    pub fn no_symlinks(path: &Path) -> Result<(), WireError> {
        if !path.is_absolute() {
            return Err(WireError::new("invalid_request"));
        }
        let mut current = std::path::PathBuf::new();
        for part in path.components() {
            match part {
                Component::RootDir | Component::Normal(_) => current.push(part.as_os_str()),
                _ => return Err(WireError::new("invalid_request")),
            }
            if fs::symlink_metadata(&current)
                .map_err(|_| WireError::new("invalid_request"))?
                .file_type()
                .is_symlink()
            {
                return Err(WireError::new("invalid_request"));
            }
        }
        Ok(())
    }
    pub fn private_dir(path: &Path) -> Result<(), WireError> {
        no_symlinks(path)?;
        let m = fs::symlink_metadata(path).map_err(|_| WireError::new("invalid_request"))?;
        if !m.is_dir() || m.uid() != uid() || m.mode() & 0o777 != 0o700 {
            return Err(WireError::new("invalid_request"));
        }
        Ok(())
    }
    pub fn read_attachment(path: &Path) -> Result<Attachment, WireError> {
        no_symlinks(path)?;
        let parent = path
            .parent()
            .ok_or_else(|| WireError::new("invalid_request"))?;
        private_dir(parent)?;
        // O_NOFOLLOW on macOS closes the final-component check/open race.
        let mut file: File = OpenOptions::new()
            .read(true)
            .custom_flags(0x100)
            .open(path)
            .map_err(|_| WireError::new("invalid_request"))?;
        let m = file
            .metadata()
            .map_err(|_| WireError::new("invalid_request"))?;
        if !m.is_file()
            || m.uid() != uid()
            || m.mode() & 0o777 != 0o600
            || m.nlink() != 1
            || m.len() > MAX_DESCRIPTOR_BYTES as u64
        {
            return Err(WireError::new("invalid_request"));
        }
        let mut bytes = Vec::new();
        file.by_ref()
            .take(MAX_DESCRIPTOR_BYTES as u64 + 1)
            .read_to_end(&mut bytes)
            .map_err(|_| WireError::new("invalid_request"))?;
        if bytes.len() > MAX_DESCRIPTOR_BYTES {
            return Err(WireError::new("invalid_request"));
        }
        let attachment: Attachment =
            serde_json::from_slice(&bytes).map_err(|_| WireError::new("invalid_request"))?;
        if attachment.protocol_version != PROTOCOL_VERSION {
            return Err(WireError::new("unsupported_protocol"));
        }
        if attachment.app_instance_id.is_empty()
            || attachment.capability.len() != 64
            || !attachment.capability.bytes().all(|b| b.is_ascii_hexdigit())
        {
            return Err(WireError::new("invalid_request"));
        }
        let socket = Path::new(&attachment.socket_path);
        if socket.parent() != Some(parent) {
            return Err(WireError::new("invalid_request"));
        }
        no_symlinks(socket)?;
        let sm = fs::symlink_metadata(socket).map_err(|_| WireError::new("invalid_request"))?;
        if !sm.file_type().is_socket() || sm.uid() != uid() || sm.mode() & 0o777 != 0o600 {
            return Err(WireError::new("invalid_request"));
        }
        Ok(attachment)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn frame_boundary_and_unterminated_are_explicit() {
        let mut valid = vec![b' '; MAX_FRAME_BYTES - 1];
        valid.push(b'\n');
        assert_eq!(
            read_frame(&mut valid.as_slice(), Instant::now() + REQUEST_DEADLINE)
                .unwrap()
                .len(),
            MAX_FRAME_BYTES
        );
        assert_eq!(
            read_frame(
                &mut vec![b' '; MAX_FRAME_BYTES].as_slice(),
                Instant::now() + REQUEST_DEADLINE
            )
            .unwrap_err()
            .code,
            "frame_too_large"
        );
        assert_eq!(
            read_frame(&mut b"{}".as_slice(), Instant::now() + REQUEST_DEADLINE)
                .unwrap_err()
                .code,
            "invalid_request"
        );
    }
    #[test]
    fn reply_cannot_replace_correlation_or_mix_result_and_error() {
        assert!(validate_reply(&json!({"result":null})).is_ok());
        assert!(validate_reply(&json!({"result":{},"request_id":"fake"})).is_err());
        assert!(validate_reply(&json!({"result":{},"error":WireError::new("busy")})).is_err());
        assert_eq!(
            envelope("native", "real", json!({"result":{"workspace":"old"}}))["result"]
                ["workspace"],
            "old"
        );
    }
}
