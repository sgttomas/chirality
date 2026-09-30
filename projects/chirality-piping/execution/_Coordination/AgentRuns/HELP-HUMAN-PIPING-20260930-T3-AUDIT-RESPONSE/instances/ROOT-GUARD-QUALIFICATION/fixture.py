import os, signal, subprocess, sys, time
mode = sys.argv[1]
if mode == 'leaf':
    time.sleep(30)
elif mode == 'ignore-leaf':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    print('IGNORE-READY', os.getpid(), flush=True)
    time.sleep(30)
elif mode == 'escape-leaf':
    os.setsid()
    print('ESCAPE-READY', os.getpid(), flush=True)
    time.sleep(6)
elif mode in ('sleepers', 'ignore', 'escape'):
    leaf = {'sleepers': 'leaf', 'ignore': 'ignore-leaf', 'escape': 'escape-leaf'}[mode]
    p = subprocess.Popen([sys.executable, __file__, leaf])
    print('PARENT-READY', os.getpid(), 'CHILD', p.pid, flush=True)
    time.sleep(30)
elif mode in ('alloc16', 'cap64'):
    n = (16 if mode == 'alloc16' else 64) * 1024 * 1024
    blob = bytearray(n)
    for index in range(0, n, 4096):
        blob[index] = 1
    print('ALLOCATED', n, os.getpid(), flush=True)
    time.sleep(3 if mode == 'alloc16' else 30)
elif mode == 'clean':
    print('CLEAN-READY', os.getpid(), flush=True)
    time.sleep(3)
else:
    raise SystemExit('unknown fixture')
