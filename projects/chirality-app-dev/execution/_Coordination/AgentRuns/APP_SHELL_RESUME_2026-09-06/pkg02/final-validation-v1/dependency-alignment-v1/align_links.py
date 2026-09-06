import pathlib,json,hashlib,subprocess,os,stat,datetime
r=pathlib.Path.cwd();run=r/'projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06';o=run/'pkg02/final-validation-v1/dependency-alignment-v1';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=json.loads((run/'DEPENDENCY_ALIGNMENT_MANIFEST_v1.json').read_text());f=r/'projects/chirality-app-dev/frontend';pkg=json.loads((f/'package.json').read_text());lock=json.loads((f/'package-lock.json').read_text());
for x in m['inputs']:assert sha(r/x['path'])==x['sha256']
paths=subprocess.check_output(['git','ls-files','-z','--','projects/chirality-app-dev/frontend','projects/chirality-runtime'],text=True).split('\0');tracked={x:sha(r/x) for x in paths if x and (r/x).is_file()};(o/'TRACKED_PREIMAGE.json').write_text(json.dumps(tracked,indent=2)+'\n');before=[]
for x in m['links']:
 p=r/x['symlink_path'];s=p.lstat();assert stat.S_ISLNK(s.st_mode);assert s.st_ino==x['observed_inode'] and s.st_dev==x['observed_device'];assert os.readlink(p)==x['old_target_exact'];assert not p.parent.is_symlink() and not p.parent.parent.is_symlink();assert pkg['dependencies'][x['package']]==x['declared_file_dependency'];assert lock['packages']['node_modules/'+x['package']]==x['lock_record'];assert (p.parent/x['suggested_relative_link_target']).resolve()==(r/x['new_target_repository_relative']).resolve()
 for t in x['current_declared_type_files']:assert sha(r/t['path'])==t['sha256']
 old=pathlib.Path(x['old_target_exact']).stat();before.append({'path':x['symlink_path'],'readlink':os.readlink(p),'inode':s.st_ino,'external_target_inode':old.st_ino,'external_target_mtime_ns':old.st_mtime_ns})
(o/'LINK_PREIMAGE.json').write_text(json.dumps(before,indent=2)+'\n')
for x in m['links']:
 p=r/x['symlink_path'];assert p.is_symlink() and os.readlink(p)==x['old_target_exact'];p.unlink();p.symlink_to(x['suggested_relative_link_target'])
after=[]
for x,b in zip(m['links'],before):
 p=r/x['symlink_path'];assert p.resolve()==(r/x['new_target_repository_relative']).resolve();old=pathlib.Path(x['old_target_exact']).stat();assert old.st_ino==b['external_target_inode'] and old.st_mtime_ns==b['external_target_mtime_ns'];after.append({'path':x['symlink_path'],'readlink':os.readlink(p),'realpath':str(p.resolve()),'external_target_directory_unchanged':True})
changes=[x for x,h in tracked.items() if sha(r/x)!=h];assert not changes
result={'status':'SEVEN_IGNORED_LINKS_ALIGNED','executor':'/root/resume_pkg02','timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_sha256':sha(run/'DEPENDENCY_ALIGNMENT_MANIFEST_v1.json'),'amendment_v7_sha256':sha(run/'instances/resume_pkg02/AMENDMENT_v7.md'),'tracked_files_preserved':len(tracked),'tracked_changes':changes,'links':after,'source_config_changes':[],'npm_ci':'NOT_RUN','external_writes':'NONE; only unlink/symlink on seven App-local link inodes'};(o/'ALIGNMENT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
