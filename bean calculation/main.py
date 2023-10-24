import numpy as np
from BendingMoment import BendingMoment
from Torque import Torque

if __name__ == '__main__':
    # define characteristic points
    x = np.array([0 , 90 , 180 , 270 , 360])
    MGy = np.array([0 , 0 ,  0 , 590 , 0])
    MSy = np.array([76.4 , 76.4 , 76.4 , 76.4, 0])
    # creating X to function
    new_x = np.linspace(x[0],x[len(x)-1],720) 

    # show plot Bendig Moment
    bending_moment = BendingMoment(x,MGy)
    bending_moment.draw_plot(new_x)

    # show plot Torque
    torque = Torque(x,MSy)
    torque.draw_plot(new_x)
    