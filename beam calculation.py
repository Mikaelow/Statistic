import numpy as np

def lineal_conncection(x,y):
    i = 1
    while i < len(x):
        x1 = x[i-1]
        x2 = x[i]
        y1 = y[i-1]
        y2 = y[i]
        indicators(x1 , x2 , y1 , y2)
        i += 1

def indicators(x1 , x2 , y1 , y2):
    main_matrix = np.array([[x1,1],[x2,1]])
    a_matrix = np.array([[y1,1],[y2,1]])
    b_matrix = np.array([[x1,y1],[x2,y2]])
    main_indicator = np.linalg.det(main_matrix)
    a_indicator = np.linalg.det(a_matrix)
    b_indicator = np.linalg.det(b_matrix)
    coefficients_a_b(a_indicator,b_indicator,main_indicator)
    #print(f'a = {a_indicator:.2f}, b = {b_indicator:.2f}, main = {main_indicator:.2f}')


def coefficients_a_b(a_indicator,b_indicator,main_indicator):
    a = round(a_indicator/main_indicator,2)
    b = round(b_indicator/main_indicator,2)
    print(f'a = {a}, b = {b}')

if __name__ == '__main__':
    x = np.array([0.3 , 0.6 , 0.9 , 1.2 ])
    y = np.array([0,0,590,0])   
    lineal_conncection(x,y)