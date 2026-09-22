import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','..','_scripts'))
from r3lib import read_csv
def load():
    h,rows=read_csv(os.path.join(os.path.dirname(__file__),'..','SPOT_S2S3.csv'))
    if isinstance(rows[0],dict): return rows
    return [dict(zip(h,r)) for r in rows]
