import numpy as np
import matplotlib.pyplot as plt

class Torque:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def torque_moment_function(self, new_x):    
        y_f = np.array([])
        i = 1
        while i < len(self.x):
            x1 = self.x[i-1]
            x2 = self.x[i]
            y1 = self.y[i-1]
            y2 = self.y[i]
            for j in new_x:
                if  x1 <= j <= x2:
                    y_f = np.append(y_f,y2)
                else: 
                    pass
            i += 1
        return y_f
