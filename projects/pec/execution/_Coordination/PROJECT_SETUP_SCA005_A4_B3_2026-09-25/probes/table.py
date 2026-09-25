import sys, re
lines = open(sys.argv[1], encoding='utf-8').read().splitlines()
start = [i for i, l in enumerate(lines) if l.startswith('| Deliverable, file | Act |')][0]
W = 'projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/'
for l in lines[start + 2:]:
    if not l.startswith('|'):
        break
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    name, act, pre, post = c
    if '(folder)' in name:
        continue
    m = re.match(r'(DEL-02-0[89]) `(.+?)`', name)
    if m:
        d = {'DEL-02-08': 'DEL-02-08_Work_graph_parser', 'DEL-02-09': 'DEL-02-09_MEMORY_run_index_parser'}[m.group(1)]
        path = W + d + '/' + m.group(2)
    else:
        path = 'projects/pec/execution/' + re.match(r'`(.+?)`', name).group(1)
    print(path, act, pre.strip('`'), post.strip('`'), sep='\t')
