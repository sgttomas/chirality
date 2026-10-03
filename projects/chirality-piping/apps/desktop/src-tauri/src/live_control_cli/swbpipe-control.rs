//! Development CLI: no desktop startup, engine access or Apply route.
#[path = "../live_control_wire.rs"]
#[allow(dead_code)]
mod wire;
use serde_json::{json, Value};
use std::io::{Read, Write};
use wire::WireError;

fn usage() -> Value {
    json!({"protocol_version":1,"usage":"swbpipe-control --attachment <descriptor-path> inspect|preview|submit|status",
        "stdin":"One params JSON object; one response JSON object on stdout.",
        "methods":wire::METHODS,"limits":{"frame_bytes_including_newline":wire::MAX_FRAME_BYTES,"descriptor_bytes":wire::MAX_DESCRIPTOR_BYTES,"native_in_flight":wire::MAX_IN_FLIGHT,"deadline_seconds":30},
        "boundaries":"Local attachment authorization only. Apply is available only in the app review UI. Controller recovery is session-only; uncertain submit retries must retain original workspace, preview and idempotency key."})
}

fn describe() -> Value {
    let mut value = usage();
    value["limits"] = json!({"frame_bytes_including_newline":wire::MAX_FRAME_BYTES,"descriptor_bytes":wire::MAX_DESCRIPTOR_BYTES,"native_in_flight":wire::MAX_IN_FLIGHT,"deadline_seconds":30,"max_node_ids":128,"max_changes":64,"max_previews":256,"max_idempotency_associations":1024,"preview_wall_clock_ttl":null});
    value["method_descriptions"] = json!([
        {"method":"inspect","description":"Discover the current workspace or inspect explicit nodes and mint a coherent basis; no mutation.","params":[{"scope":"workspace"},{"scope":"nodes","workspace":"opaque workspace","node_ids":["explicit node ID"]}],"result_shapes":[{"workspace":"opaque workspace","identity":"app/controller/workspace/project identity","readiness":"ready","selection":[{"object_type":"object type","ref":"ID"}],"supported":{"object_type":"Node","field_path":"position.x","operation_kind":"modify","change_kind":"set_field","dimension":"length","length_unit":"project source unit"},"limits":{"max_node_ids":128,"max_changes":64}},{"workspace":"opaque workspace","identity":"identity","basis":"opaque basis","basis_identity":"identity plus published model_revision and complete ModelHashEvidence","nodes":[{"id":"ID","label":"label","position":{"x":0,"y":0,"z":0}}],"length_unit":"project source unit"}]},
        {"method":"preview","description":"Validate one or up to 64 ordered Node position.x changes on frozen temporary state; no model/history mutation or acceptance.","params":{"workspace":"opaque workspace","basis":"opaque basis","changes":[{"target":{"object_type":"Node","ref":"explicit node ID"},"field_path":"position.x","before":"decimal string","after":"decimal string","unit":"inspected project source unit","dimension":"length"}]},"result_shape":{"workspace":"opaque workspace","preview_ref":"opaque preview or null when blocked","basis":"opaque basis","basis_identity":"identity plus published model_revision and complete ModelHashEvidence","validation":"passed or blocked","outcome":"complete existing validate-only OperationBatchOutcome, including diagnostics and ordered operation_outcomes"}},
        {"method":"submit","description":"Publish the passed frozen preview into the local review queue. Same key/preview joins or recovers the original ticket; never Applies.","params":{"workspace":"original workspace","preview_ref":"opaque passed preview","idempotency_key":"stable caller key"},"result_shape":{"workspace":"original workspace","ticket":"opaque ticket","state":"queued, committed, rejected, withdrawn, expired or outcome_unknown","reason":"stable reason or null","receipt":"complete observed receipt only when committed, otherwise null"}},
        {"method":"status","description":"Recover a ticket from this controller session, including an older workspace. Pending receipt hashing can return not_ready.","params":{"workspace":"original workspace","ticket":"opaque ticket"},"result_shape":{"workspace":"original workspace","ticket":"opaque ticket","state":"queued, committed, rejected, withdrawn, expired or outcome_unknown","reason":"stable reason or null","receipt":"complete observed receipt only when committed, otherwise null"}}
    ]);
    value["receipt_origin"] = json!("origin.request_id identifies the preview invocation that created the proposal, not a later submit/status/retry invocation.");
    value["capacity_policy"] = json!("The controller reuses one coherent current inspection basis, retiring it when revision/hash changes while frozen previews and ticket recovery remain independent. Preview and idempotency capacities refuse admission without evicting promised recovery records.");
    value
}

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    if args.len() == 1 && matches!(args[0].as_str(), "help" | "--help" | "-h" | "describe") {
        println!(
            "{}",
            if args[0] == "describe" {
                describe()
            } else {
                usage()
            }
        );
        return;
    }
    let mut app_id = None;
    let mut request_id = None;
    let response = execute(&args, &mut app_id, &mut request_id).unwrap_or_else(|error| {
        json!({
            "protocol_version":1,"app_instance_id":app_id,"request_id":request_id,"error":error
        })
    });
    let failed = response.get("error").is_some();
    // Error payloads originate from documented wire constructors or validated controller replies.
    println!("{response}");
    if failed {
        std::process::exit(1);
    }
}
fn execute(
    args: &[String],
    app_id: &mut Option<String>,
    request_id: &mut Option<String>,
) -> Result<Value, WireError> {
    if args.len() != 3 || args[0] != "--attachment" {
        return Err(WireError::new("invalid_request"));
    }
    if !wire::METHODS.contains(&args[2].as_str()) {
        return Err(WireError::new("unsupported_method"));
    }
    #[cfg(not(target_os = "macos"))]
    {
        let _ = (app_id, request_id);
        return Err(WireError::new("unsupported_host"));
    }
    #[cfg(target_os = "macos")]
    {
        use std::os::unix::net::UnixStream;
        use std::time::{Duration, Instant};
        let attachment = wire::private_fs::read_attachment(std::path::Path::new(&args[1]))?;
        *app_id = Some(attachment.app_instance_id.clone());
        let mut input = Vec::new();
        std::io::stdin()
            .take(wire::MAX_FRAME_BYTES as u64 + 1)
            .read_to_end(&mut input)
            .map_err(|_| WireError::new("invalid_request"))?;
        if input.len() > wire::MAX_FRAME_BYTES {
            return Err(WireError::new("frame_too_large"));
        }
        let params: Value =
            serde_json::from_slice(&input).map_err(|_| WireError::new("invalid_request"))?;
        if !params.is_object() {
            return Err(WireError::new("invalid_request"));
        }
        let id = wire::random_id("req-")?;
        *request_id = Some(id.clone());
        let request = wire::Request {
            protocol_version: 1,
            request_id: id.clone(),
            app_instance_id: attachment.app_instance_id.clone(),
            capability: attachment.capability,
            method: args[2].clone(),
            params,
        };
        let frame = wire::encode_frame(
            &serde_json::to_value(request).map_err(|_| WireError::new("internal_error"))?,
        )?;
        let mut stream = UnixStream::connect(&attachment.socket_path)
            .map_err(|_| WireError::new("controller_unavailable"))?;
        stream
            .set_read_timeout(Some(Duration::from_millis(100)))
            .map_err(|_| WireError::new("internal_error"))?;
        stream
            .set_write_timeout(Some(wire::REQUEST_DEADLINE))
            .map_err(|_| WireError::new("internal_error"))?;
        let deadline = Instant::now() + wire::REQUEST_DEADLINE;
        stream
            .write_all(&frame)
            .map_err(|_| WireError::new("outcome_unknown"))?;
        let bytes = wire::read_frame(&mut stream, deadline)
            .map_err(|_| WireError::new("outcome_unknown"))?;
        let response: Value =
            serde_json::from_slice(&bytes).map_err(|_| WireError::new("outcome_unknown"))?;
        validate_response(&response, &attachment.app_instance_id, &id)?;
        Ok(response)
    }
}
fn validate_response(response: &Value, app: &str, id: &str) -> Result<(), WireError> {
    let object = response
        .as_object()
        .ok_or_else(|| WireError::new("outcome_unknown"))?;
    let is_error = match (object.contains_key("result"), object.contains_key("error")) {
        (true, false) => false,
        (false, true) => true,
        _ => return Err(WireError::new("outcome_unknown")),
    };
    let payload_key = if is_error { "error" } else { "result" };
    let expected_keys = [
        "protocol_version",
        "app_instance_id",
        "request_id",
        payload_key,
    ];
    if object.len() != expected_keys.len()
        || expected_keys.iter().any(|key| !object.contains_key(*key))
        || object.get("protocol_version") != Some(&json!(1))
        || object.get("app_instance_id").and_then(Value::as_str) != Some(app)
    {
        return Err(WireError::new("outcome_unknown"));
    }
    // A missing key is never the explicit pre-correlation null allowed on errors.
    match object.get("request_id") {
        Some(Value::String(actual)) if actual == id => {}
        Some(Value::Null) if is_error => {}
        _ => return Err(WireError::new("outcome_unknown")),
    }
    let body = if is_error {
        json!({"error": object["error"]})
    } else {
        json!({"result": object["result"]})
    };
    wire::validate_reply(&body).map_err(|_| WireError::new("outcome_unknown"))
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn cli_rejects_wrong_correlation_and_extra_envelope_fields() {
        let good = json!({"protocol_version":1,"app_instance_id":"a","request_id":"r","result":{"workspace":"old"}});
        assert!(validate_response(&good, "a", "r").is_ok());
        assert!(validate_response(&good, "other", "r").is_err());
        assert!(validate_response(&good, "a", "other").is_err());
        let mut bad = good;
        bad["capability"] = json!("forged");
        assert!(validate_response(&bad, "a", "r").is_err());
    }
    #[test]
    fn cli_requires_exact_keys_and_explicit_typed_correlation() {
        let error = serde_json::to_value(WireError::new("capacity")).unwrap();
        let correlated_error =
            json!({"protocol_version":1,"app_instance_id":"a","request_id":"r","error":error});
        assert!(validate_response(&correlated_error, "a", "r").is_ok());
        let mut null_error = correlated_error.clone();
        null_error["request_id"] = Value::Null;
        assert!(validate_response(&null_error, "a", "r").is_ok());

        let missing_plus_unknown = json!({"protocol_version":1,"app_instance_id":"a","error":error,"unknown":"replacement"});
        let missing_with_both =
            json!({"protocol_version":1,"app_instance_id":"a","error":error,"result":null});
        let null_success =
            json!({"protocol_version":1,"app_instance_id":"a","request_id":null,"result":null});
        let both = json!({"protocol_version":1,"app_instance_id":"a","request_id":"r","result":null,"error":error});
        for invalid in [missing_plus_unknown, missing_with_both, null_success, both] {
            let rejection = validate_response(&invalid, "a", "r").unwrap_err();
            assert_eq!(rejection.code, "outcome_unknown");
            assert!(rejection
                .next_action
                .contains("original workspace, preview and idempotency key"));
        }
        for wrong_type in [json!(1), json!(true), json!([]), json!({})] {
            let mut invalid = correlated_error.clone();
            invalid["request_id"] = wrong_type;
            assert!(validate_response(&invalid, "a", "r").is_err());
        }
        let mut missing = correlated_error;
        missing.as_object_mut().unwrap().remove("request_id");
        assert!(validate_response(&missing, "a", "r").is_err());
    }
}
