import numpy as np
from BendingMoment import BendingMoment
from Torque import Torque
from ReducedMoment import ReducedMoment
from Diameter import Diameter
import matplotlib.pyplot as plt

if __name__ == '__main__':
        # define characteristic points
    x = np.array([0 , 90 , 180 , 270 , 360])
    MGy = np.array([0 , 0 ,  0 , 590 , 0])
    MSy = np.array([76.4 , 76.4 , 76.4 , 76.4, 0])

        # creating X to function
    new_x = np.linspace(x[0],x[len(x)-1],720) 

        #  Bendig Moment
    bending_moment = BendingMoment(x,MGy)
    bending_f = bending_moment.bending_moment_function(new_x)

        #  Torque
    torque = Torque(x,MSy)
    torque_f = torque.torque_moment_function(new_x)

        # Reduced Moment
    reduced_moment = ReducedMoment(torque_f , bending_f)
    reduced_f = reduced_moment.calculate_reduce_moment()

        # Diameter
    diameter = Diameter(reduced_f)
    diameter_f1 = diameter.calculate_diameter()
    #diameter_f2 = [-_ for _ in diameter_f1]

        #Draw plots
    plt.subplot(4,1,1)
    plt.plot(new_x, bending_f, color = 'red')
    plt.title('Bendig Moment')
    plt.subplot(4,1,2)
    plt.plot(new_x, torque_f)
    plt.title('Torque')
    plt.subplot(4,1,3)
    plt.plot(new_x, reduced_f, color = 'purple')
    plt.title('Reduced Moment')
    plt.subplot(4,1,4)
    plt.plot(new_x, diameter_f1, color = 'green')
    #plt.plot(new_x, diameter_f2, color = 'green')
    plt.title('Diameter')
    plt.show()

    