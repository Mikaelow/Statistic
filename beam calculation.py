import numpy as np
import matplotlib.pyplot as plt

def loop_and_cheeck(a,b,x1,x2):
    new_x = np.linspace(x[0],x[len(x)-1],20)
    y_f = np.array([])
    for j in new_x:
            if x1<=j<=x2:
                new_y = np.round(a*j + b)
                y_f = np.append(y_f, new_y)
    return new_x, new_y


def lineal_conncection(x,y):
    i = 1
    while i < len(x):
        x1 = x[i-1] 
        x2 = x[i]
        y1 = y[i-1] 
        y2 = y[i]
        indicator = indicators(x1 , x2 , y1 , y2)
        a = indicator[0]
        b = indicator[1]
        loop_and_cheeck(a,b,x1,x2)
        i += 1

def indicators(x1 , x2 , y1 , y2):
    main_matrix = np.array([[x1,1],[x2,1]])
    a_matrix = np.array([[y1,1],[y2,1]])
    b_matrix = np.array([[x1,y1],[x2,y2]])
    main_indicator = np.linalg.det(main_matrix)
    a_indicator = np.linalg.det(a_matrix)
    b_indicator = np.linalg.det(b_matrix)
    return coefficients_a_b(a_indicator,b_indicator,main_indicator)

def coefficients_a_b(a_indicator,b_indicator,main_indicator):
    a = round(a_indicator/main_indicator,2)
    b = round(b_indicator/main_indicator,2)
    return a,b


if __name__ == '__main__':
    x = np.array([0.3 , 0.6 , 0.8])
    y = np.array([0   ,  10 , 50])   
    lineal_conncection(x,y)