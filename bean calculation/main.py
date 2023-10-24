import numpy as np
import matplotlib.pyplot as plt
from LinealConnection import Linealc_Connection

if __name__ == '__main__':
    x = np.array([0 , 90 , 180 , 270 , 360])
    MGy = np.array([0 , 0 ,  0 , 590 , 0])
    new_x = np.linspace(x[0],x[len(x)-1],720) 
    lineal_conncection = Linealc_Connection(x,MGy)
    y_f_line = lineal_conncection.conncection(new_x)
    plt.plot(new_x , y_f_line , color = 'blue')
    plt.scatter(x , MGy , color='red' , marker = 'o')
    plt.show()
    