import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def r_squared(y, estimated):
  
    y, estimated = np.array(y), np.array(estimated)
    SEE = ((estimated - y)**2).sum()
    mMean = y.sum()/float(len(y))
    MV = ((mMean - y)**2).sum()
    return 1 - SEE/MV
