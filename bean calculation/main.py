import numpy as np
from LinealConnection import Linealc_Connection

if __name__ == '__main__':
    # define characteristic points
    x = np.array([0 , 90 , 180 , 270 , 360])
    MGy = np.array([0 , 0 ,  0 , 590 , 0])

    # creating X to function
    new_x = np.linspace(x[0],x[len(x)-1],720) 

    # show plot Bendig Moment
    bending_moment = Linealc_Connection(x,MGy)
    bending_moment.draw_plot(new_x)
    