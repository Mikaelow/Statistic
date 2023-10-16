import random 
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = np.array(np.linspace(0,60,30))
y = np.array([random.randint(0,1000) for _ in range(30)])
plt.scatter(x,y,color='red',marker='o')
plt.legend('Standard')
y_f=interp1d(x,y,kind='cubic')
x = np.array(np.linspace(0,60,10000))
y= y_f(x)
plt.plot(x,y)
plt.legend('Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
