import subprocess,json
inner=['/usr/bin/sandbox-exec','-p','(version 1)(allow default)(deny network*)','/usr/bin/true']
policies={
'network':'(deny network*)',
'writes':'(deny file-write*)',
'securityd':'(deny mach-lookup (global-name "com.apple.securityd"))',
'reads':'(deny file-read-data (require-not (require-any (literal "/") (subpath "/System") (subpath "/usr") (subpath "/bin") (subpath "/sbin"))))',
'reads_etc':'(deny file-read-data (require-not (require-any (literal "/") (subpath "/System") (subpath "/usr") (subpath "/bin") (subpath "/sbin") (subpath "/private/etc"))))',
}
for label,rule in policies.items():
 r=subprocess.run(['/usr/bin/sandbox-exec','-p','(version 1)(allow default)'+rule]+inner,capture_output=True,text=True,cwd='/')
 print(json.dumps({'profile':label,'exit':r.returncode,'stderr':r.stderr}))
for label,rule in policies.items():
 profile='(version 1)(allow default)'+rule
 r=subprocess.run(['/usr/bin/sandbox-exec','-p',profile,'/usr/bin/sandbox-exec','-p',profile,'/usr/bin/true'],capture_output=True,text=True,cwd='/')
 print(json.dumps({'profile':label+'_identical_nested','exit':r.returncode,'stderr':r.stderr}))
