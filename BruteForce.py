import numpy as np
from itertools import combinations
import copy as cp
import ObjectiveResult as result
    
def BruteForce(x,y,n,k):
    best = float('inf')
    denak = [i for i in range(len(y))]
    combs= combinations(denak,k)
    exc = np.zeros((n,k))
    print(exc)
    p = []
    return BruteForceWorker(denak,y,n,k,exc,0,best,x)


def BruteForceWorker(nexc,y,n,k,exc,i,best,bestx):
    print(exc)
    if(i == len(exc)):
        return exc
    else:
        combs = combinations(nexc,k)
        moment = cp.deepcopy(nexc)
        for comb in combs:
            nexc = kendu(moment, comb)
            exc[i] = list(comb)
            x = BruteForceWorker(nexc,y,n,k,exc,i+1,best,bestx)
            e = result.result(x,y)
            if(best > e):
                best = e
                bestx = cp.deepcopy(x)
        return bestx

def kendu(a,b):
    s = []
    for elem in a:
        if(not elem in b):
            s.append(elem)
    return s
            
    
