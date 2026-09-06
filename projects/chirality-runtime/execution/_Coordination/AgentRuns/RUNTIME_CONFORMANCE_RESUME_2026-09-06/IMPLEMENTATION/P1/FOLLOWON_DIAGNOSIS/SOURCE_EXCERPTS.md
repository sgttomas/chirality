
## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/features/src/lib.rs

869:         id: Feature::ShellSnapshot,
870:         key: "shell_snapshot",
871:         stage: Stage::Stable,
872:         default_enabled: true,
873:     },
874:     FeatureSpec {

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/session/session.rs

1147:                 shell::default_user_shell()
1148:             };
1149:             let shell_snapshot = if config.features.enabled(Feature::ShellSnapshot) {
1150:                 ShellSnapshot::new(
1151:                     config.codex_home.clone(),
1152:                     thread_id,
1153:                     session_telemetry.clone(),
1154:                     state_db_ctx.clone(),
1155:                 )
1156:             } else {
1157:                 ShellSnapshot::disabled()
1158:             };
1159:             let turn_environments = Arc::new(ThreadEnvironments::new(
1160:                 environment_manager,
1161:                 default_shell.clone(),
1162:                 session_configuration.inferred_environment_config(),
1163:                 shell_snapshot,
1164:                 inherited_environments.unwrap_or_default(),
1165:                 config.features.enabled(Feature::DeferredExecutor),
1166:             ));

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/environment_selection.rs

560:             }
561:         } else {
562:             Some(local_shell)
563:         };
564:         let task = shell_snapshot
565:             .build(Arc::clone(&environment), selection.cwd, shell.clone())
566:             .boxed()
567:             .shared();
568:         drop(tokio::spawn(
569:             task.clone().in_current_span().with_current_subscriber(),
570:         ));
571:         Ok(ResolvedEnvironment {
572:             environment,
573:             shell,
574:             shell_snapshot: task,
575:             installed_config,
576:         })

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/shell_snapshot.rs

65:
66:     pub(crate) fn disabled() -> Self {
67:         Self { config: None }
68:     }
69:
70:     pub(crate) async fn build(
71:         self,
72:         environment: Arc<Environment>,
73:         cwd: PathUri,
74:         shell: Option<Shell>,
75:     ) -> Option<Arc<ShellSnapshotFile>> {
76:         let config = self.config.as_ref()?;
77:         if environment.is_remote() {
78:             return None;
79:         }
80:
81:         let shell = shell?;
82:         // TODO(anp): Migrate shell snapshot creation to accept PathUri and defer native
83:         // conversion to the spawned shell process.
84:         let cwd = cwd.to_abs_path().ok()?;
85:         Self::build_for_cwd(Arc::clone(config), cwd, shell).await
86:     }
201: async fn write_shell_snapshot(
202:     shell_type: ShellType,
203:     output_path: &AbsolutePathBuf,
204:     cwd: &AbsolutePathBuf,
205: ) -> Result<()> {
206:     if shell_type == ShellType::PowerShell || shell_type == ShellType::Cmd {
207:         bail!("Shell snapshot not supported yet for {shell_type:?}");
208:     }
209:     let shell =
210:         get_shell(shell_type).with_context(|| format!("No available shell for {shell_type:?}"))?;
211:
212:     let raw_snapshot = capture_snapshot(&shell, cwd).await?;
213:     let snapshot = strip_snapshot_preamble(&raw_snapshot)?;
214:
215:     if let Some(parent) = output_path.parent() {
216:         let parent_display = parent.display();
217:         fs::create_dir_all(&parent)
218:             .await
219:             .with_context(|| format!("Failed to create snapshot parent {parent_display}"))?;
220:     }
221:
222:     let snapshot_path = output_path.display();
223:     fs::write(output_path, snapshot)
224:         .await
225:         .with_context(|| format!("Failed to write snapshot to {snapshot_path}"))?;
226:
227:     Ok(())
228: }
229:
230: async fn capture_snapshot(shell: &Shell, cwd: &AbsolutePathBuf) -> Result<String> {
231:     let shell_type = shell.shell_type;
232:     let script = snapshot_script(shell_type)
233:         .ok_or_else(|| anyhow!("Shell snapshotting is not yet supported for {shell_type:?}"))?;
234:     run_shell_script(shell, &script, cwd).await
235: }
236:
237: fn strip_snapshot_preamble(snapshot: &str) -> Result<String> {
238:     let marker = "# Snapshot file";
239:     let Some(start) = snapshot.find(marker) else {
240:         bail!("Snapshot output missing marker {marker}");
241:     };
242:
243:     Ok(snapshot[start..].to_string())
244: }
245:
246: async fn validate_snapshot(
247:     shell: &Shell,
248:     snapshot_path: &AbsolutePathBuf,
249:     cwd: &AbsolutePathBuf,
250: ) -> Result<()> {
251:     let snapshot_path_display = snapshot_path.display();
252:     let script = format!("set -e; . \"{snapshot_path_display}\"");
253:     run_script_with_timeout(
254:         shell,
255:         &script,
256:         SNAPSHOT_TIMEOUT,
257:         /*use_login_shell*/ false,
258:         cwd,
259:     )
260:     .await
261:     .map(|_| ())
262: }
263:
264: async fn run_shell_script(shell: &Shell, script: &str, cwd: &AbsolutePathBuf) -> Result<String> {
265:     run_script_with_timeout(
266:         shell,
267:         script,
268:         SNAPSHOT_TIMEOUT,
269:         /*use_login_shell*/ true,
270:         cwd,
271:     )
272:     .await
273: }
274:
275: async fn run_script_with_timeout(
276:     shell: &Shell,
277:     script: &str,
278:     snapshot_timeout: Duration,
279:     use_login_shell: bool,
280:     cwd: &AbsolutePathBuf,
281: ) -> Result<String> {
282:     let args = shell.derive_exec_args(script, use_login_shell);
283:     let shell_name = shell.name();
284:
285:     // Handler is kept as guard to control the drop. The `mut` pattern is required because .args()
286:     // returns a ref of handler.
287:     let mut handler = Command::new(&args[0]);
288:     codex_protocol::shell_environment::scrub_non_inheritable_env_vars(handler.as_std_mut());
289:     handler.args(&args[1..]);
290:     handler.stdin(Stdio::null());
291:     handler.current_dir(cwd);
292:     #[cfg(unix)]
293:     unsafe {
294:         handler.pre_exec(|| {
295:             codex_utils_pty::process_group::detach_from_tty()?;
296:             Ok(())
297:         });
298:     }
299:     handler.kill_on_drop(true);
300:     let output = timeout(snapshot_timeout, handler.output())
301:         .await
302:         .map_err(|_| anyhow!("Snapshot command timed out for {shell_name}"))?
303:         .with_context(|| format!("Failed to execute {shell_name}"))?;
304:
305:     if !output.status.success() {
306:         let status = output.status;
307:         let stderr = String::from_utf8_lossy(&output.stderr);
308:         bail!("Snapshot command exited with status {status}: {stderr}");
309:     }
310:
311:     Ok(String::from_utf8_lossy(&output.stdout).into_owned())
312: }
313:
314: /// Removes shell snapshots that either lack a matching session rollout file or
315: /// whose rollouts have not been updated within the retention window.

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/shell.rs

19:
20:     /// Takes a string of shell and returns the full list of command args to
21:     /// use with `exec()` to run the shell command.
22:     pub fn derive_exec_args(&self, command: &str, use_login_shell: bool) -> Vec<String> {
23:         match self.shell_type {
24:             ShellType::Zsh | ShellType::Bash | ShellType::Sh => {
25:                 let arg = if use_login_shell { "-lc" } else { "-c" };
26:                 vec![
27:                     self.shell_path.to_string_lossy().to_string(),
28:                     arg.to_string(),
29:                     command.to_string(),
30:                 ]
31:             }
32:             ShellType::PowerShell => {

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/tools/handlers/unified_exec.rs

97: pub(crate) fn get_command(
98:     args: &ExecCommandArgs,
99:     session_shell: Arc<Shell>,
100:     shell_mode: &UnifiedExecShellMode,
101:     allow_login_shell: bool,
102: ) -> Result<ResolvedCommand, String> {
103:     let use_login_shell = match args.login {
104:         Some(true) if !allow_login_shell => {
105:             return Err(
106:                 "login shell is disabled by config; omit `login` or set it to false.".to_string(),
107:             );
108:         }
109:         Some(use_login_shell) => use_login_shell,
110:         None => allow_login_shell,
111:     };
112:
113:     match shell_mode {
114:         UnifiedExecShellMode::Direct => {
115:             let model_shell = args
116:                 .shell
117:                 .as_ref()
118:                 .map(|shell_str| get_shell_by_model_provided_path(&PathBuf::from(shell_str)));
119:             let shell = model_shell.as_ref().unwrap_or(session_shell.as_ref());
120:             Ok(ResolvedCommand {
121:                 command: shell.derive_exec_args(&args.cmd, use_login_shell),
122:                 shell_type: shell.shell_type,
123:             })
124:         }
125:         UnifiedExecShellMode::ZshFork(zsh_fork_config) => {

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/tools/runtimes/mod.rs

234: pub(crate) fn maybe_wrap_shell_lc_with_snapshot(
235:     command: &[String],
236:     session_shell: &Shell,
237:     shell_snapshot: Option<&AbsolutePathBuf>,
238:     explicit_env_overrides: &HashMap<String, String>,
239:     env: &HashMap<String, String>,
240:     runtime_path_prepends: &RuntimePathPrepends,
241: ) -> Vec<String> {
242:     if cfg!(windows) {
243:         return command.to_vec();
244:     }
245:
246:     let Some(snapshot) = shell_snapshot else {
247:         return command.to_vec();
248:     };
249:
250:     if !snapshot.exists() {
251:         return command.to_vec();
252:     }
253:
254:     if command.len() < 3 {
255:         return command.to_vec();
256:     }
257:
258:     let flag = command[1].as_str();
259:     if flag != "-lc" {
260:         return command.to_vec();
261:     }
262:
263:     let snapshot_path = snapshot.to_string_lossy();

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/tools/runtimes/unified_exec.rs

477:             &command,
478:             &req.cwd,
479:             &env,
480:             managed_network_context,
481:             additional_permissions,
482:         )
483:         .map_err(|error| match error {
484:             ToolError::Rejected(_) => {
485:                 ToolError::Rejected("missing command line for PTY".to_string())
486:             }
487:             error @ ToolError::Codex(_) => error,
488:         })?;
489:         let options = unified_exec_options(attempt.network_denial_cancellation_token.clone());
490:         let process = self
491:             .manager
492:             .open_session_with_exec_env(
493:                 req.process_id,
494:                 command,
495:                 options,
496:                 attempt,
497:                 managed_network,
498:                 network_proxy_launch,
499:                 /*environment_id*/ Some(&req.turn_environment.selection.environment_id),
500:                 req.exec_server_env_config.clone(),
501:                 windows_sandbox_proxy_settings_mode,
502:                 req.tty,
503:                 Box::new(NoopSpawnLifecycle),
504:                 req.turn_environment.environment.as_ref(),
505:             )
506:             .await?;
507:         Ok(UnifiedExecAttempt {
508:             process,
509:             metrics_sidecar,

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/shell-command/src/shell_detect.rs

60:
61: #[cfg(unix)]
62: fn get_user_shell_path() -> Option<PathBuf> {
63:     let uid = unsafe { libc::getuid() };
64:     use std::ffi::CStr;
65:     use std::mem::MaybeUninit;
66:     use std::ptr;
67:
68:     let mut passwd = MaybeUninit::<libc::passwd>::uninit();
69:
70:     // We cannot use getpwuid here: it returns pointers into libc-managed
71:     // storage, which is not safe to read concurrently on all targets (the musl
72:     // static build used by the CLI can segfault when parallel callers race on
73:     // that buffer). getpwuid_r keeps the passwd data in caller-owned memory.
74:     let suggested_buffer_len = unsafe { libc::sysconf(libc::_SC_GETPW_R_SIZE_MAX) };
75:     let buffer_len = usize::try_from(suggested_buffer_len)
76:         .ok()
77:         .filter(|len| *len > 0)
78:         .unwrap_or(1024);
79:     let mut buffer = vec![0; buffer_len];
80:
81:     loop {
82:         let mut result = ptr::null_mut();
83:         let status = unsafe {
84:             libc::getpwuid_r(
85:                 uid,
86:                 passwd.as_mut_ptr(),
87:                 buffer.as_mut_ptr().cast(),
88:                 buffer.len(),
89:                 &mut result,
90:             )
91:         };
92:
93:         if status == 0 {
94:             if result.is_null() {
95:                 return None;
96:             }
97:
98:             let passwd = unsafe { passwd.assume_init_ref() };
99:             if passwd.pw_shell.is_null() {
100:                 return None;
101:             }
102:
103:             let shell_path = unsafe { CStr::from_ptr(passwd.pw_shell) }
104:                 .to_string_lossy()
105:                 .into_owned();
106:             return Some(PathBuf::from(shell_path));
107:         }
108:
109:         if status != libc::ERANGE {
110:             return None;
111:         }
266: pub fn default_user_shell() -> DetectedShell {
267:     default_user_shell_from_path(get_user_shell_path())
268: }
269:
270: pub fn default_user_shell_from_path(user_shell_path: Option<PathBuf>) -> DetectedShell {
271:     if cfg!(windows) {
272:         get_shell(ShellType::PowerShell).unwrap_or_else(ultimate_fallback_shell)
273:     } else {
274:         let user_default_shell = user_shell_path
275:             .and_then(|shell| detect_shell_type(&shell))
276:             .and_then(get_shell);
277:
278:         let shell_with_fallback = if cfg!(target_os = "macos") {
279:             user_default_shell
280:                 .or_else(|| get_shell(ShellType::Zsh))
281:                 .or_else(|| get_shell(ShellType::Bash))
282:         } else {
283:             user_default_shell
284:                 .or_else(|| get_shell(ShellType::Bash))
285:                 .or_else(|| get_shell(ShellType::Zsh))
286:         };
287:
288:         shell_with_fallback.unwrap_or_else(ultimate_fallback_shell)

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/protocol/src/shell_environment.rs

14: pub const NON_INHERITABLE_ENV_VARS: &[&str] = &[
15:     CODEX_EXEC_SERVER_NOISE_AUTH_TOKEN_ENV_VAR,
16:     "NODE_REPL_AUTH_TOKEN",
17:     OPENAI_FEDERATION_RULE_ID_ENV_VAR,
18:     OPENAI_IDENTITY_TOKEN_FILE_ENV_VAR,
19:     OPENAI_WORKLOAD_IDENTITY_CONTEXT_ENV_VAR,
20: ];
21:
22: pub fn is_non_inheritable_env_var(name: &str) -> bool {
23:     NON_INHERITABLE_ENV_VARS
24:         .iter()
25:         .any(|restricted| restricted.eq_ignore_ascii_case(name))
26: }
27:
28: /// Configures a child command to omit non-inheritable variables from the
29: /// process environment and explicit command overrides.
30: ///
31: /// This prevents accidental propagation of Codex launch context; it is not a
32: /// filesystem security boundary for the referenced identity-token file.
33: pub fn scrub_non_inheritable_env_vars(command: &mut std::process::Command) {
34:     let configured_names = command
35:         .get_envs()
36:         .map(|(name, _)| name.to_os_string())
37:         .collect::<Vec<_>>();
38:
39:     for name in NON_INHERITABLE_ENV_VARS {
40:         command.env_remove(name);

## /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/config.schema.json

5648:         "send_async_message": {
5649:           "type": "boolean"
5650:         },
5651:         "shell_snapshot": {
5652:           "type": "boolean"
5653:         },
5654:         "shell_tool": {
5655:           "type": "boolean"
