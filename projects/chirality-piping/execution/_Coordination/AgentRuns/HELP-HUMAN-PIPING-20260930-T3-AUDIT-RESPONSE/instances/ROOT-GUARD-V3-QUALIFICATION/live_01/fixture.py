import subprocess, sys, time
mode = sys.argv[1]
if mode == 'leaf':
    time.sleep(float(sys.argv[2]))
elif mode == 'one':
    subprocess.run([sys.executable, __file__, 'leaf', '0.02'], check=True)
elif mode == 'tail':
    # Parent returns first; supervisor must drain the inherited short-lived leaf.
    subprocess.Popen([sys.executable, __file__, 'leaf', '0.08'])
elif mode == 'pair':
    children = [subprocess.Popen([sys.executable, __file__, 'leaf', d])
                for d in ('0.02', '0.05')]
    for child in children:
        if child.wait() != 0:
            raise SystemExit('leaf failure')
else:
    raise SystemExit('unknown fixture mode')
