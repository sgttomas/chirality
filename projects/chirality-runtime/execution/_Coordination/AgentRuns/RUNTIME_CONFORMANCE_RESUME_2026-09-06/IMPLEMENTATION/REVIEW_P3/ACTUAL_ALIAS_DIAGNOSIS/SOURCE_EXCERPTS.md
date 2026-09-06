# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/tools/handlers/apply_patch.rs
SHA256 78889d430bb1453aeb189bd050aef76f24cea2b974f4e8364c584f631320d61e

396:         // Verify the parsed patch against the selected environment filesystem.
397:         let Some(turn_environment) = resolve_tool_environment(
398:             &step_context.environments,
399:             selected_environment_id.as_deref(),
400:         )?
401:         else {
402:             return Err(FunctionCallError::RespondToModel(
403:                 "apply_patch is unavailable in this session".to_string(),
404:             ));
405:         };
406:         let fs = turn_environment.environment.get_filesystem();
407:         let sandbox = turn
408:             .file_system_sandbox_context(/*additional_permissions*/ None, turn_environment);
409:         match codex_apply_patch::verify_apply_patch_args_with_mode(
410:             args,
411:             turn_environment.cwd(),
412:             apply_patch_file_update_mode(&turn),
413:             fs.as_ref(),
414:             Some(&sandbox),
415:         )
416:         .await
417:         {
418:             codex_apply_patch::MaybeApplyPatchVerified::Body(changes) => {
419:                 let tool_ctx = ToolCtx {
420:                     session,
421:                     step_context: Arc::clone(&step_context),
422:                     call_id,
423:                     tool_name,
424:                 };
425:                 let content = execute_verified_patch(
426:                     changes,
427:                     turn_environment.cwd(),
428:                     turn_environment.clone(),
429:                     Some(&tracker),
430:                     tool_ctx,
431:                 )
432:                 .await?;
433:                 Ok(boxed_tool_output(ApplyPatchToolOutput::from_text(content)))
434:             }
435:             codex_apply_patch::MaybeApplyPatchVerified::CorrectnessError(parse_error) => {
436:                 Err(FunctionCallError::RespondToModel(format!(
437:                     "apply_patch verification failed: {parse_error}"

552: async fn execute_verified_patch(
553:     action: ApplyPatchAction,
554:     cwd: &PathUri,
555:     turn_environment: TurnEnvironment,
556:     tracker: Option<&SharedTurnDiffTracker>,
557:     tool_ctx: ToolCtx,
558: ) -> Result<String, FunctionCallError> {
559:     let (file_paths, effective_additional_permissions, file_system_sandbox_policy) =
560:         effective_patch_permissions(tool_ctx.session.as_ref(), &turn_environment, &action, cwd)
561:             .await
562:             .unwrap_or_else(|_| patch_permissions_without_path_matching(&action));
563:     let apply = apply_patch::prepare_apply_patch(
564:         tool_ctx.step_context.turn.as_ref(),
565:         turn_environment.permission_profile(),
566:         &file_system_sandbox_policy,
567:         action,
568:     )?;
569:     let changes = convert_apply_patch_to_protocol(&apply.action);
570:     let emitter = ToolEmitter::apply_patch_for_environment(
571:         changes.clone(),
572:         apply.auto_approved,
573:         turn_environment.selection.environment_id.clone(),
574:     );
575:     let event_ctx = ToolEventCtx::new(
576:         tool_ctx.session.as_ref(),
577:         tool_ctx.step_context.turn.as_ref(),
578:         &tool_ctx.call_id,
579:         tracker,
580:     );
581:     emitter.begin(event_ctx).await;
582:
583:     let request = ApplyPatchRequest {
584:         turn_environment,
585:         action: apply.action,
586:         file_paths,
587:         changes: Arc::new(changes),
588:         exec_approval_requirement: apply.exec_approval_requirement,
589:         additional_permissions: effective_additional_permissions.additional_permissions,
590:         permissions_preapproved: effective_additional_permissions.permissions_preapproved,
591:     };
592:     let mut orchestrator = ToolOrchestrator::new();
593:     let mut runtime = ApplyPatchRuntime::new();

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/safety.rs
SHA256 6341d13d6d1b70ee5617548785257f01bb23e0d8e2d92753e0914380c6043a2b

52:         || matches!(
53:             policy,
54:             AskForApproval::Granular(granular_config) if !granular_config.sandbox_approval
55:         );
56:
57:     // Even though the patch appears to be constrained to writable paths, it is
58:     // possible that paths in the patch are hard links to files outside the
59:     // writable roots, so we should still run `apply_patch` in a sandbox in that case.
60:     if is_write_patch_constrained_to_writable_paths(action, file_system_sandbox_policy, cwd) {
61:         if matches!(
62:             permission_profile,
63:             PermissionProfile::Disabled | PermissionProfile::External { .. }
64:         ) {
65:             // Disabled and External profiles intentionally do not apply an
66:             // outer Codex filesystem sandbox.
67:             SafetyCheck::AutoApprove
68:         } else {
69:             // Only auto‑approve when we can actually enforce a sandbox. Otherwise
70:             // fall back to asking the user because the patch may touch arbitrary
71:             // paths outside the project.
72:             match get_platform_sandbox(windows_sandbox_level != WindowsSandboxLevel::Disabled) {
73:                 Some(_) => SafetyCheck::AutoApprove,

123: fn is_write_patch_constrained_to_writable_paths(
124:     action: &ApplyPatchAction,
125:     file_system_sandbox_policy: &FileSystemSandboxPolicy,
126:     cwd: &PathUri,
127: ) -> bool {
128:     // A full-disk policy permits every patch target, so no per-path writable-root check can
129:     // further constrain the result.
130:     if file_system_sandbox_policy.has_full_disk_write_access() {
131:         return true;
132:     }
133:     // TODO(anp): Make filesystem sandbox policies operate on PathUri.
134:     let Ok(native_cwd) = cwd.to_abs_path() else {
135:         return false;
136:     };
137:     // Normalize a path by removing `.` and resolving `..` without touching the
138:     // filesystem (works even if the file does not exist).
139:     fn normalize(path: &Path) -> Option<PathBuf> {
140:         let mut out = PathBuf::new();
141:         for comp in path.components() {
142:             match comp {
143:                 Component::ParentDir => {
144:                     out.pop();
145:                 }
146:                 Component::CurDir => { /* skip */ }
147:                 other => out.push(other.as_os_str()),
148:             }
149:         }
150:         Some(out)
151:     }
152:
153:     // Determine whether `path` is inside **any** writable root. Both `path`
154:     // and roots are converted to absolute, normalized forms before the
155:     // prefix check.
156:     let is_path_writable = |path: &PathUri| {
157:         // TODO(anp): Make sandbox policy path checks accept PathUri without host projection.
158:         let Ok(path) = path.to_abs_path() else {
159:             return false;
160:         };
161:         let abs = path.into_path_buf();
162:         let abs = match normalize(&abs) {
163:             Some(v) => v,
164:             None => return false,
165:         };
166:
167:         file_system_sandbox_policy.can_write_path_with_cwd(&abs, &native_cwd)
168:     };
169:
170:     for (path, change) in action.changes() {

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/core/src/tools/runtimes/apply_patch.rs
SHA256 becc8bdafb970443afb5c2aaab74fa0df2cfdffdf257dcb5593c89a1119d6659

169:         attempt: &SandboxAttempt<'_>,
170:         _ctx: &ToolCtx,
171:     ) -> Result<ApplyPatchRuntimeOutput, ToolError> {
172:         let started_at = Instant::now();
173:         let fs = req.turn_environment.environment.get_filesystem();
174:         let sandbox = Self::file_system_sandbox_context_for_attempt(req, attempt);
175:         let mut stdout = Vec::new();
176:         let mut stderr = Vec::new();
177:         let result = codex_apply_patch::apply_patch_with_options(
178:             &req.action.patch,
179:             ApplyPatchOptions {
180:                 update_file_mode: req.action.update_file_mode(),
181:                 // Only reject links when an otherwise-required sandbox was bypassed.
182:                 // Executor-managed sandboxes can have SandboxType::None.
183:                 follow_symlinks: attempt.sandbox_requested
184:                     || !attempt.manager.should_sandbox(
185:                         attempt.permissions,
186:                         self.sandbox_preference(),
187:                         attempt.enforce_managed_network,
188:                     ),
189:             },
190:             &req.action.cwd,
191:             &mut stdout,
192:             &mut stderr,
193:             fs.as_ref(),
194:             sandbox.as_ref(),
195:         )
196:         .await;
197:         let stdout = String::from_utf8_lossy(&stdout).into_owned();
198:         let stderr = String::from_utf8_lossy(&stderr).into_owned();
199:         let failed = result.is_err();
200:         let exit_code = if failed { 1 } else { 0 };
201:         let delta = match result {
202:             Ok(delta) => delta,
203:             Err(failure) => failure.into_parts().1,
204:         };
205:         self.committed_delta.append(delta);
206:         let output = ExecToolCallOutput {
207:             exit_code,

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/apply-patch/src/lib.rs
SHA256 5e6f736f3a4b66c1d651baa9b85ce6e6921de170faf901e6c2f78ad9a383eaf9

691:                     };
692:                     modified.push(affected_path);
693:                 } else {
694:                     try_write!(
695:                         fs.write_file(
696:                             &path_uri,
697:                             new_contents.clone().into_bytes(),
698:                             WriteFileOptions { follow_symlinks },
699:                             sandbox,
700:                         )
701:                         .await
702:                         .with_context(|| format!(
703:                             "Failed to write file {}",
704:                             path_uri.inferred_native_path_string()
705:                         ))

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/exec-server/src/local_file_system.rs
SHA256 1c5d8bbf51529c0cc0f2c73f22b78189910ee7e31d42bbf4230861add1e688a0

84:     fn file_system_for<'a>(
85:         &'a self,
86:         sandbox: Option<&'a FileSystemSandboxContext>,
87:     ) -> io::Result<(
88:         &'a dyn ExecutorFileSystem,
89:         Option<&'a FileSystemSandboxContext>,
90:     )> {
91:         if sandbox.is_some_and(FileSystemSandboxContext::should_run_in_sandbox) {
92:             Ok((self.sandboxed()?, sandbox))
93:         } else {
94:             Ok((&self.unsandboxed, sandbox))
95:         }
96:     }

595:
596:     async fn write_file(
597:         &self,
598:         path: &PathUri,
599:         contents: Vec<u8>,
600:         options: WriteFileOptions,
601:         sandbox: Option<&FileSystemSandboxContext>,
602:     ) -> FileSystemResult<()> {
603:         reject_sandbox_context(sandbox)?;
604:         let path = path.to_abs_path()?;
605:         if options.follow_symlinks {
606:             tokio::fs::write(path.as_path(), contents).await
607:         } else {
608:             no_follow::write_file(path.as_path(), contents).await
609:         }
610:     }
611:

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/exec-server/src/sandboxed_file_system.rs
SHA256 0282cecf59842650b78a767d7156e5e112008ab1acbcaa5fc5ecc31654108e7a

99:
100:     async fn read_file(
101:         &self,
102:         path: &PathUri,
103:         options: ReadFileOptions,
104:         sandbox: Option<&FileSystemSandboxContext>,
105:     ) -> FileSystemResult<Vec<u8>> {
106:         let sandbox = require_platform_sandbox(sandbox)?;
107:         validate_native_path(path)?;
108:         let response = self
109:             .run_sandboxed(
110:                 sandbox,
111:                 FsHelperRequest::ReadFile(FsReadFileParams {
112:                     path: path.clone(),
113:                     follow_symlinks: (!options.follow_symlinks).then_some(false),
114:                     sandbox: None,
115:                 }),
116:             )
117:             .await?
118:             .expect_read_file()
119:             .map_err(map_sandbox_error)?;
120:         STANDARD.decode(response.data_base64).map_err(|err| {
121:             io::Error::new(
122:                 io::ErrorKind::InvalidData,
123:                 format!("fs/readFile returned invalid base64 dataBase64: {err}"),
124:             )
125:         })
126:     }
127:
128:     async fn write_file(
129:         &self,
130:         path: &PathUri,
131:         contents: Vec<u8>,
132:         options: WriteFileOptions,
133:         sandbox: Option<&FileSystemSandboxContext>,
134:     ) -> FileSystemResult<()> {
135:         let sandbox = require_platform_sandbox(sandbox)?;
136:         validate_native_path(path)?;
137:         self.run_sandboxed(
138:             sandbox,
139:             FsHelperRequest::WriteFile(FsWriteFileParams {
140:                 path: path.clone(),
141:                 data_base64: STANDARD.encode(contents),
142:                 follow_symlinks: (!options.follow_symlinks).then_some(false),
143:                 sandbox: None,
144:             }),
145:         )
146:         .await?
147:         .expect_write_file()
148:         .map_err(map_sandbox_error)?;
149:         Ok(())
150:     }
151:
152:     async fn create_directory(
153:         &self,
154:         path: &PathUri,
155:         options: CreateDirectoryOptions,
156:         sandbox: Option<&FileSystemSandboxContext>,
157:     ) -> FileSystemResult<()> {
158:         let sandbox = require_platform_sandbox(sandbox)?;
159:         validate_native_path(path)?;
160:         self.run_sandboxed(
161:             sandbox,
162:             FsHelperRequest::CreateDirectory(FsCreateDirectoryParams {
163:                 path: path.clone(),
164:                 recursive: Some(options.recursive),

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/exec-server/src/fs_sandbox.rs
SHA256 6bd757ade4b4df954c30478fdeecf4de955ee94bc959d88e0b546b8a28228b4e

75:     pub(crate) fn sandbox_command(
76:         &self,
77:         sandbox: &FileSystemSandboxContext,
78:     ) -> Result<SandboxExecRequest, JSONRPCErrorError> {
79:         let cwd = sandbox_cwd(sandbox)?;
80:         let native_workspace_roots = sandbox
81:             .workspace_roots
82:             .iter()
83:             .map(native_workspace_root)
84:             .collect::<Result<Vec<_>, _>>()?;
85:         let workspace_roots = native_workspace_roots.as_slice();
86:         let native_permissions: PermissionProfile =
87:             sandbox.permissions.clone().try_into().map_err(|err| {
88:                 invalid_request(format!("invalid sandbox permission path URI: {err}"))
89:             })?;
90:         let native_permissions =
91:             native_permissions.materialize_project_roots_with_workspace_roots(workspace_roots);
92:         let mut file_system_policy = native_permissions.file_system_sandbox_policy();
93:         let helper_read_roots = if sandbox.use_legacy_landlock {
94:             Vec::new()
95:         } else {
96:             helper_read_roots(&self.runtime_paths)
97:         };
98:         add_helper_runtime_permissions(
99:             &mut file_system_policy,
100:             &helper_read_roots,
101:             cwd.native.as_path(),
102:         );
103:         normalize_file_system_policy_root_aliases(&mut file_system_policy);
104:         let network_policy = NetworkSandboxPolicy::Restricted;
105:         let permission_profile = PermissionProfile::from_runtime_permissions_with_enforcement(
106:             native_permissions.enforcement(),
107:             &file_system_policy,
108:             network_policy,
109:         );
110:         self.sandbox_exec_request(&permission_profile, &cwd, workspace_roots, sandbox)
111:     }
112:

198: fn helper_read_roots(runtime_paths: &ExecServerRuntimePaths) -> Vec<AbsolutePathBuf> {
199:     let mut roots = vec![runtime_paths.codex_self_exe.clone()];
200:     if let Some(path) = &runtime_paths.codex_linux_sandbox_exe
201:         && !roots.contains(path)
202:     {
203:         roots.push(path.clone());
204:     }
205:     roots
206: }
207:
208: fn add_helper_runtime_permissions(
209:     file_system_policy: &mut FileSystemSandboxPolicy,
210:     helper_read_roots: &[AbsolutePathBuf],
211:     cwd: &std::path::Path,
212: ) {
213:     if !file_system_policy.has_full_disk_read_access() {
214:         let minimal_read_entry = FileSystemSandboxEntry::new(
215:             FileSystemPath::Special {
216:                 value: FileSystemSpecialPath::Minimal,
217:             },
218:             FileSystemAccessMode::Read,
219:         );
220:         if !file_system_policy.entries.contains(&minimal_read_entry) {
221:             file_system_policy.entries.push(minimal_read_entry);
222:         }
223:     }
224:
225:     for helper_read_root in helper_read_roots {
226:         if file_system_policy.can_read_path_with_cwd(helper_read_root.as_path(), cwd) {
227:             continue;
228:         }
229:
230:         file_system_policy.entries.push(FileSystemSandboxEntry::new(
231:             helper_read_root.clone().into(),
232:             FileSystemAccessMode::Read,
233:         ));
234:     }
235: }

422:     #[test]
423:     fn helper_permissions_enable_minimal_reads_for_restricted_profile() {
424:         let cwd = AbsolutePathBuf::from_absolute_path(std::env::temp_dir().as_path())
425:             .expect("absolute cwd");
426:         let mut policy = restricted_policy(Vec::new());
427:
428:         add_helper_runtime_permissions(&mut policy, /*helper_read_roots*/ &[], cwd.as_path());
429:
430:         assert!(policy.include_platform_defaults());
431:     }
432:
433:     #[test]
434:     fn helper_permissions_enable_minimal_reads_for_restricted_profile_with_writes() {
435:         let cwd = AbsolutePathBuf::from_absolute_path(std::env::temp_dir().as_path())
436:             .expect("absolute cwd");
437:         let mut policy = restricted_policy(vec![path_entry(
438:             cwd.join("writable"),
439:             FileSystemAccessMode::Write,
440:         )]);
441:
442:         add_helper_runtime_permissions(&mut policy, /*helper_read_roots*/ &[], cwd.as_path());
443:
444:         assert!(policy.include_platform_defaults());
445:     }

675:     #[test]
676:     fn helper_permissions_include_only_the_helper_executable() {
677:         let codex_self_exe = std::env::current_exe().expect("current exe");
678:         let runtime_paths =
679:             ExecServerRuntimePaths::new(codex_self_exe, /*codex_linux_sandbox_exe*/ None)
680:                 .expect("runtime paths");
681:         let cwd = AbsolutePathBuf::from_absolute_path(std::env::temp_dir().as_path())
682:             .expect("absolute cwd");
683:         let mut policy = restricted_policy(Vec::new());
684:         let parent = runtime_paths
685:             .codex_self_exe
686:             .parent()
687:             .expect("current exe parent");
688:         let sibling = parent.join("credentials.json");
689:
690:         add_helper_runtime_permissions(
691:             &mut policy,
692:             &helper_read_roots(&runtime_paths),
693:             cwd.as_path(),
694:         );
695:
696:         assert!(
697:             policy.can_read_path_with_cwd(runtime_paths.codex_self_exe.as_path(), cwd.as_path())
698:         );
699:         assert!(!policy.can_read_path_with_cwd(parent.as_path(), cwd.as_path()));
700:         assert!(!policy.can_read_path_with_cwd(sibling.as_path(), cwd.as_path()));
701:     }

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/protocol/src/permissions.rs
SHA256 45347859f8d0f3b1ecb0ce40271c6447893f42f2a805191a3ee5959d47a82065

845:     /// Returns true when platform-default readable roots should be included.
846:     pub fn include_platform_defaults(&self) -> bool {
847:         !self.has_full_disk_read_access()
848:             && matches!(self.kind, FileSystemSandboxKind::Restricted)
849:             && self.entries.iter().any(|entry| {
850:                 matches!(
851:                     &entry.path,
852:                     FileSystemPath::Special { value }
853:                         if matches!(value, FileSystemSpecialPath::Minimal)
854:                             && entry.access.can_read()
855:                 )
856:             })

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/sandboxing/src/seatbelt.rs
SHA256 fe56fa7fbf4000e7f181373b94fd492e9ca0058cd7b62a9b192c84ae3d3c31b3

894:     let network_policy =
895:         dynamic_network_policy_for_network(network_sandbox_policy, enforce_managed_network, &proxy);
896:
897:     let include_platform_defaults = file_system_sandbox_policy.include_platform_defaults();
898:     let deny_read_policy =
899:         build_seatbelt_unreadable_glob_policy(file_system_sandbox_policy, sandbox_policy_cwd);
900:     let mut policy_sections = vec![
901:         MACOS_SEATBELT_BASE_POLICY.to_string(),
902:         file_read_policy,
903:         file_write_policy,
904:         network_policy,
905:     ];
906:     if include_platform_defaults {
907:         policy_sections.push(MACOS_RESTRICTED_READ_ONLY_PLATFORM_DEFAULTS.to_string());
908:         if profile == MacosSeatbeltProfile::Process {
909:             policy_sections.push(MACOS_PROCESS_APPLICATIONS_READ_POLICY.to_string());
910:         }
911:     }
912:     policy_sections.push(deny_read_policy);

# /private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/sandboxing/src/restricted_read_only_platform_defaults.sbpl
SHA256 092b34f8104b3a73da42bbcb600ba83f03c6f3eee1c8b39c02bf0939d824db56

100: (allow file-read* (subpath "/etc"))
101: (allow file-read* (subpath "/private/etc"))
102:
103: (allow file-read* file-test-existence
104:   (literal "/System/Library/CoreServices")
105:   (literal "/System/Library/CoreServices/.SystemVersionPlatform.plist")
106:   (literal "/System/Library/CoreServices/SystemVersion.plist"))
107:
108: ; Some processes read /var metadata during startup.
109: (allow file-read-metadata (subpath "/var"))
110: (allow file-read-metadata (subpath "/private/var"))
111:
112: ; IOKit access for root domain services.

# Exact undeclared temp grants
/private/tmp/runtime-execution-20260906/supplier-candidate/source/codex/codex-rs/sandboxing/src/restricted_read_only_platform_defaults.sbpl
93: ; Scratch space so tools can create temp files.
94: (allow file-read* file-test-existence file-write* (subpath "/tmp"))
95: (allow file-read* file-write* (subpath "/private/tmp"))
96: (allow file-read* file-write* (subpath "/var/tmp"))
97: (allow file-read* file-write* (subpath "/private/var/tmp"))
