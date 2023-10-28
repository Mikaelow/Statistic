import math
import numpy as np
class Diameter:
    def __init__(self, Mzr:np.array) -> None:
        self.Mzr = Mzr
    
    def calculate_diameter(self):
        d = ((32*self.Mzr)/(math.pi*78))**(1/3)
        return d*10