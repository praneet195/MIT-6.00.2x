import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools
def find_combination(choices, total):
    powerset = []
    for i in itertools.product([1,0], repeat = len(choices)):
        powerset.append(np.array(i))
    filseq= []
    filsel= []
    for j in powerset:
        if sum(j*choices) == total:
            filseq.append(j)
        elif sum(j*choices) < total:
            filsel.append(j)
    if len(filseq) > 0:
        minx = min(enumerate(filseq), key=lambda x:sum(x[1]))[1]
        return minx
    else:
        minx = max(enumerate(filsel), key = lambda x:sum(x[1]))[1]
        return minx
        
