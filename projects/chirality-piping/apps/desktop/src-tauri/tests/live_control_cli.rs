#![cfg(feature = "live-control-cli")]
use serde_json::Value;
use std::process::Command;
#[test]
fn help_and_describe_are_offline_json_and_apply_is_rejected() {
    for command in ["help", "describe"] {
        let output = Command::new(env!("CARGO_BIN_EXE_swbpipe-control"))
            .arg(command)
            .output()
            .unwrap();
        assert!(output.status.success());
        assert!(output.stderr.is_empty());
        let value: Value = serde_json::from_slice(&output.stdout).unwrap();
        assert_eq!(value["protocol_version"], 1);
        if command == "describe" {
            assert_eq!(value["method_descriptions"].as_array().unwrap().len(), 4);
            assert_eq!(value["limits"]["max_idempotency_associations"], 1024);
            assert_eq!(value["limits"]["max_changes"], 64);
        }
        assert!(value["methods"]
            .as_array()
            .unwrap()
            .iter()
            .all(|m| m != "apply"));
    }
    let output = Command::new(env!("CARGO_BIN_EXE_swbpipe-control"))
        .args(["--attachment", "/nonexistent", "apply"])
        .output()
        .unwrap();
    assert!(!output.status.success());
    assert!(output.stderr.is_empty());
    let value: Value = serde_json::from_slice(&output.stdout).unwrap();
    assert_eq!(value["error"]["code"], "unsupported_method");
}
#[test]
fn malformed_invocation_is_one_structured_error() {
    let output = Command::new(env!("CARGO_BIN_EXE_swbpipe-control"))
        .arg("SECRET_ARG")
        .output()
        .unwrap();
    assert!(!output.status.success());
    assert!(output.stderr.is_empty());
    let text = String::from_utf8(output.stdout).unwrap();
    assert_eq!(text.lines().count(), 1);
    assert!(!text.contains("SECRET_ARG"));
    let value: Value = serde_json::from_str(&text).unwrap();
    assert_eq!(value["error"]["code"], "invalid_request");
}

#[cfg(target_os = "macos")]
mod macos {
    use super::*;
    use std::fs::{self, DirBuilder, OpenOptions};
    use std::io::{BufRead, BufReader, Write};
    use std::os::unix::{
        fs::{DirBuilderExt, OpenOptionsExt, PermissionsExt},
        net::UnixListener,
    };
    use std::process::{Child, Output, Stdio};
    use std::time::{Duration, Instant};

    struct OwnedDirectory(std::path::PathBuf);
    impl Drop for OwnedDirectory {
        fn drop(&mut self) {
            let _ = fs::remove_dir_all(&self.0);
        }
    }
    struct OwnedChild(Option<Child>);
    impl OwnedChild {
        fn child(&mut self) -> &mut Child {
            self.0.as_mut().expect("owned child")
        }
        fn output_after_exit(&mut self) -> Output {
            self.0
                .take()
                .expect("owned child")
                .wait_with_output()
                .expect("collect exited CLI")
        }
        fn finish(&mut self, timeout: Duration) -> Output {
            let deadline = Instant::now() + timeout;
            loop {
                if self.child().try_wait().expect("poll CLI").is_some() {
                    return self.output_after_exit();
                }
                if Instant::now() >= deadline {
                    let _ = self.child().kill();
                    let output = self.output_after_exit();
                    panic!(
                        "CLI failed to exit before deadline: {}",
                        diagnostics(&output)
                    );
                }
                std::thread::sleep(Duration::from_millis(10));
            }
        }
    }
    impl Drop for OwnedChild {
        fn drop(&mut self) {
            if let Some(mut child) = self.0.take() {
                let _ = child.kill();
                let _ = child.wait();
            }
        }
    }
    fn diagnostics(output: &Output) -> String {
        let stderr = String::from_utf8_lossy(&output.stderr).replace(&"a".repeat(64), "[redacted]");
        let code = serde_json::from_slice::<Value>(&output.stdout)
            .ok()
            .and_then(|v| v["error"]["code"].as_str().map(str::to_owned))
            .unwrap_or_else(|| "no structured error code".into())
            .replace(&"a".repeat(64), "[redacted]");
        format!(
            "status={}, error_code={}, stderr={}",
            output.status, code, stderr
        )
    }
    fn accept_bounded(
        listener: &UnixListener,
        child: &mut OwnedChild,
    ) -> std::os::unix::net::UnixStream {
        listener
            .set_nonblocking(true)
            .expect("nonblocking fixture listener");
        let deadline = Instant::now() + Duration::from_secs(5);
        loop {
            match listener.accept() {
                Ok((stream, _)) => return stream,
                Err(error) if error.kind() == std::io::ErrorKind::WouldBlock => {}
                Err(error) => panic!("fixture accept failed: {error}"),
            }
            if child
                .child()
                .try_wait()
                .expect("poll connecting CLI")
                .is_some()
            {
                let output = child.output_after_exit();
                panic!(
                    "CLI exited before connecting; verify descriptor/CLI error: {}",
                    diagnostics(&output)
                );
            }
            if Instant::now() >= deadline {
                let _ = child.child().kill();
                let output = child.output_after_exit();
                panic!(
                    "CLI did not connect before deadline: {}",
                    diagnostics(&output)
                );
            }
            std::thread::sleep(Duration::from_millis(10));
        }
    }
    #[test]
    fn real_cli_preserves_correlation_historical_status_and_nonzero_errors() {
        for is_error in [false, true] {
            let suffix = std::time::SystemTime::now()
                .duration_since(std::time::UNIX_EPOCH)
                .unwrap()
                .as_nanos();
            let dir = std::path::PathBuf::from(format!(
                "/private/tmp/swbc-{}-{suffix}",
                std::process::id()
            ));
            DirBuilder::new().mode(0o700).create(&dir).unwrap();
            let _directory = OwnedDirectory(dir.clone());
            let socket = dir.join("s");
            let listener = UnixListener::bind(&socket).unwrap();
            fs::set_permissions(&socket, fs::Permissions::from_mode(0o600)).unwrap();
            let descriptor = dir.join("attachment.json");
            let attachment = serde_json::json!({"protocol_version":1,"app_instance_id":"fixture-app","socket_path":socket,"capability":"a".repeat(64)});
            serde_json::to_writer(
                OpenOptions::new()
                    .create_new(true)
                    .write(true)
                    .mode(0o600)
                    .open(&descriptor)
                    .unwrap(),
                &attachment,
            )
            .unwrap();
            let child = Command::new(env!("CARGO_BIN_EXE_swbpipe-control"))
                .args(["--attachment", descriptor.to_str().unwrap(), "status"])
                .stdin(Stdio::piped())
                .stdout(Stdio::piped())
                .stderr(Stdio::piped())
                .spawn()
                .unwrap();
            let mut child = OwnedChild(Some(child));
            child
                .child()
                .stdin
                .take()
                .unwrap()
                .write_all(br#"{"workspace":"old","ticket":"t"}"#)
                .unwrap();
            let mut stream = accept_bounded(&listener, &mut child);
            stream
                .set_write_timeout(Some(Duration::from_secs(2)))
                .unwrap();
            stream
                .set_read_timeout(Some(std::time::Duration::from_secs(2)))
                .unwrap();
            let mut line = String::new();
            BufReader::new(stream.try_clone().unwrap())
                .read_line(&mut line)
                .unwrap();
            let request: Value = serde_json::from_str(&line).unwrap();
            assert_eq!(request["params"]["workspace"], "old");
            assert!(
                request["capability"] == "a".repeat(64),
                "CLI attachment authorization mismatch"
            );
            let mut response = serde_json::json!({"protocol_version":1,"app_instance_id":"fixture-app","request_id":request["request_id"]});
            if is_error {
                response["error"] = serde_json::json!({"code":"outcome_unknown","message":"Synthetic uncertainty.","retryable":true,"next_action":"Retry the original workspace, preview and idempotency key."});
            } else {
                response["result"] = serde_json::json!({"workspace":"old","ticket":"t","state":"committed","reason":null,"receipt":{"synthetic":true}});
            }
            writeln!(stream, "{response}").unwrap();
            let output = child.finish(Duration::from_secs(5));
            assert_eq!(output.status.success(), !is_error);
            assert!(output.stderr.is_empty());
            let text = String::from_utf8(output.stdout).unwrap();
            assert!(!text.contains(&"a".repeat(64)));
            assert_eq!(text.lines().count(), 1);
            assert_eq!(serde_json::from_str::<Value>(&text).unwrap(), response);
            drop(listener);
            drop(stream);
        }
    }
}
