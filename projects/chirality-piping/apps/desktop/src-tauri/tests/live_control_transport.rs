#[path = "../src/live_control_wire.rs"]
#[allow(dead_code)]
mod wire;
use serde_json::{json, Value};

#[test]
fn canonical_manager_fixtures_use_exact_carrier_shapes() {
    let fixtures: Value =
        serde_json::from_str(include_str!("fixtures/live-control-wire-v1.json")).unwrap();
    assert_eq!(
        fixtures["wire_sha256"],
        "91f4910026bcceffc98c669a4d2487539ad63cc878822061e6cc1b40c98c40ce"
    );
    for case in fixtures["cases"].as_array().unwrap() {
        let request: wire::Request = serde_json::from_value(case["request"].clone()).unwrap();
        let response = &case["response"];
        assert_eq!(response["request_id"], request.request_id);
        let body = if let Some(v) = response.get("result") {
            json!({"result":v})
        } else {
            json!({"error":response["error"]})
        };
        wire::validate_reply(&body).unwrap();
        assert_eq!(
            wire::envelope(&request.app_instance_id, &request.request_id, body),
            *response
        );
        wire::encode_frame(response).unwrap();
    }
}
#[test]
fn unknown_request_fields_reject_and_apply_has_no_carrier_method() {
    let value = json!({"protocol_version":1,"request_id":"r","app_instance_id":"a","capability":"c","method":"inspect","params":{},"author":"forged"});
    assert!(serde_json::from_value::<wire::Request>(value).is_err());
    assert!(!wire::METHODS.contains(&"apply"));
}
#[cfg(target_os = "macos")]
mod macos {
    use super::*;
    use std::fs::{self, DirBuilder, OpenOptions};
    use std::os::unix::{
        fs::{symlink, DirBuilderExt, OpenOptionsExt, PermissionsExt},
        net::UnixListener,
    };
    use std::path::PathBuf;
    struct Fixture {
        dir: PathBuf,
        _listener: Option<UnixListener>,
    }
    impl Fixture {
        fn create() -> Self {
            let dir =
                PathBuf::from("/private/tmp").join(&wire::random_id("swb-test-").unwrap()[..28]);
            DirBuilder::new().mode(0o700).create(&dir).unwrap();
            let mut fixture = Self {
                dir: dir.clone(),
                _listener: None,
            };
            let socket = dir.join("s");
            let listener = UnixListener::bind(&socket).unwrap();
            fs::set_permissions(&socket, fs::Permissions::from_mode(0o600)).unwrap();
            let attachment = wire::Attachment {
                protocol_version: 1,
                app_instance_id: "fixture".into(),
                socket_path: socket.to_str().unwrap().into(),
                capability: "a".repeat(64),
            };
            let file = OpenOptions::new()
                .create_new(true)
                .write(true)
                .mode(0o600)
                .open(dir.join("attachment.json"))
                .unwrap();
            serde_json::to_writer(file, &attachment).unwrap();
            fixture._listener = Some(listener);
            fixture
        }
    }
    impl Drop for Fixture {
        fn drop(&mut self) {
            let _ = fs::remove_dir_all(&self.dir);
        }
    }
    #[test]
    fn attachment_refuses_symlink_public_permissions_and_non_socket() {
        let f = Fixture::create();
        let descriptor = f.dir.join("attachment.json");
        assert!(wire::private_fs::read_attachment(&descriptor).is_ok());
        let link = f.dir.join("link");
        symlink(&descriptor, &link).unwrap();
        assert!(wire::private_fs::read_attachment(&link).is_err());
        fs::set_permissions(&descriptor, fs::Permissions::from_mode(0o644)).unwrap();
        assert!(wire::private_fs::read_attachment(&descriptor).is_err());
        fs::set_permissions(&descriptor, fs::Permissions::from_mode(0o600)).unwrap();
        fs::set_permissions(&f.dir, fs::Permissions::from_mode(0o755)).unwrap();
        assert!(wire::private_fs::read_attachment(&descriptor).is_err());
        fs::set_permissions(&f.dir, fs::Permissions::from_mode(0o700)).unwrap();
        fs::remove_file(f.dir.join("s")).unwrap();
        fs::write(f.dir.join("s"), b"not socket").unwrap();
        assert!(wire::private_fs::read_attachment(&descriptor).is_err());
    }
    #[test]
    fn malformed_descriptor_never_echoes_content() {
        let f = Fixture::create();
        let descriptor = f.dir.join("attachment.json");
        fs::write(&descriptor, b"SECRET_MALFORMED").unwrap();
        let error = wire::private_fs::read_attachment(&descriptor)
            .err()
            .unwrap();
        assert!(!serde_json::to_string(&error)
            .unwrap()
            .contains("SECRET_MALFORMED"));
    }
}

#[test]
fn live_capability_is_local_main_listen_and_unlisten_only() {
    let capability: Value =
        serde_json::from_str(include_str!("../capabilities/live-control.json")).unwrap();
    assert_eq!(capability["local"], true);
    assert_eq!(capability["webviews"], json!(["main"]));
    assert_eq!(
        capability["permissions"],
        json!(["core:event:allow-listen", "core:event:allow-unlisten"])
    );
    // Omitting windows avoids granting all webviews embedded in a main window.
    assert!(capability.get("windows").is_none());
    assert!(capability.get("remote").is_none());
    let keys = capability.as_object().unwrap();
    assert_eq!(keys.len(), 5);
    assert!(keys.keys().all(|k| [
        "identifier",
        "description",
        "local",
        "webviews",
        "permissions"
    ]
    .contains(&k.as_str())));
}
