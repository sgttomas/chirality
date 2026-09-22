import sys, os
RUN=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RUN,'R3','_scripts'))
from r3lib import read_csv
def load(rel): return read_csv(os.path.join(RUN,rel))
