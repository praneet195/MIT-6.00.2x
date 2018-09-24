import numpy as np

def generate_models(x, y, degs):
  
    return [np.polyfit(x, y, z) for z in degs]
