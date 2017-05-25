import pickle 
import os

staticfile = "/home/sora/proxyfilte.dat"

def load(sfile):
    with open(sfile, "rb") as f:
        res = pickle.load(f)
    return res

if not os.path.exists(staticfile):
    in_nouse = set()
    in_canuse = set()
    out_nouse = set()
    out_canuse = set()
    staticdict = dict()
else:
    staticdict = load(staticfile)
#    in_canuse, in_nouse, out_canuse, out_nouse = staticdict['in_canuse'], staticdict['in_nouse'], staticdict.get('out_canuse', set()), staticdict('out_nouse', set())
    out_canuse = staticdict('out_canuse', None)
