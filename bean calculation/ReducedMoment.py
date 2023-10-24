import numpy as np
import math 
class ReducedMoment:
    # T torque
    # BM Bending Moment
    def __init__(self, t:np.array, bm:np.array):
        self.t = t
        self.bm = bm

    def calculate_reduce_moment(self) -> np.array:
        i = 0
        rm = np.array([])
        while i < len(self.t):
            x = self.bm[i] 
            y = self.t[i]
            y_f = math.sqrt(math.pow(x, 2) + 0.75 * math.pow(y, 2))
            rm = np.append(rm, y_f)
            i += 1 
        return rm
