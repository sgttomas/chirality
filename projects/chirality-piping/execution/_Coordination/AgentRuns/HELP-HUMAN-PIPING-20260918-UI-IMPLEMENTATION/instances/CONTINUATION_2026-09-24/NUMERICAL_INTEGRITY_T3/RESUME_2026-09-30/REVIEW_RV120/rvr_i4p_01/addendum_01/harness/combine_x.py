import json,sys
a=[]
for f in sys.argv[2:]: a+=json.load(open(f))
json.dump(a,open(sys.argv[1],'w'))
print(len(a))
