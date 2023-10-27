import numpy as np

class BendingMoment:
    def __init__(self,x:np.array , y:np.array):
        self.x = x
        self.y = y
        
    def loop_and_cheeck(self,a,b,x1,x2,j):
        if x1<=j<=x2:
            new_y = a*j + b
            return new_y
        else:
            pass

    def bending_moment_function(self, new_x) -> np.array:
        i = 1
        y_f = np.array([])
        while i < len(self.x):
            x1 = self.x[i-1] 
            x2 = self.x[i]
            y1 = self.y[i-1] 
            y2 = self.y[i]
            indicator = self.indicators(x1 , x2 , y1 , y2)
            a = indicator[0]
            b = indicator[1]
            for j in new_x:
                new_y = self.loop_and_cheeck(a,b,x1,x2,j)
                y_f = np.append(y_f, new_y)
            i += 1
        y_f = y_f[y_f != None]
        return y_f
        
    def indicators(self, x1 , x2 , y1 , y2):
        main_matrix = np.array([[x1,1],[x2,1]])
        a_matrix = np.array([[y1,1],[y2,1]])
        b_matrix = np.array([[x1,y1],[x2,y2]])
        main_indicator = np.linalg.det(main_matrix)
        a_indicator = np.linalg.det(a_matrix)
        b_indicator = np.linalg.det(b_matrix)
        return self.coefficients_a_b(a_indicator,b_indicator,main_indicator)

    def coefficients_a_b(self, a_indicator,b_indicator,main_indicator):
        a = round(a_indicator/main_indicator,2)
        b = round(b_indicator/main_indicator,2)
        return a,b

    
    
#plt.scatter(x , MGy , color='red' , marker = 'o') #MG points