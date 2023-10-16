import random 
import matplotlib.pyplot as plt
x = list(range(1,60,2))
y=[random.randint(0,1000) for _ in range(30)]
plt.scatter(x,y,color='red',marker='o')
plt.title('Standard')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
