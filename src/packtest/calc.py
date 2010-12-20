'''
Created on 07.12.2010

@author: Xandman
'''
class Calc:
    ''' This Class Calculates different approximation Models of numeric data'''
    
    
    def linreg(self,X,Y,maxX,maxY):
        '''Linear Regression of several Data Points'''
        x_w = 0.0
        y_w = 0.0
        Sxx = 0.0
        Sxy = 0.0
        a = 0.0
        c = 0.0
     
        for i in range (0, len (X)):
            x_w += X[i]
        for i in range (0, len(Y)):
            y_w += Y[i]
            
        x_w = x_w/len(X) 
        y_w = y_w/len(Y)
        
        for i in range (0, len(X)):
            Sxx += (X[i]-x_w)* (X[i]-x_w)
        for i in range (0, len(Y)):
            Sxy += (X[i]-x_w)*(Y[i]-y_w)
    
        Sxx = Sxx /(len(X))
        Sxy = Sxy /(len(Y))  
        a = Sxy/Sxx
        c = y_w - a* x_w
        xpart = 1
        x1 = 0
        y1 = c
        
        
        while i ==0:
            if a <= 0.1 or xpart<=0.1:
                i=1
            else:
                a = a / 2
                xpart = xpart / 2
                
        x2 = x1
        y2 = y1
                
        while x2 <= maxX and y2 <= maxY:
            x2 = x2 + xpart
            y2 = y2 + a 
               
        return x1,y1,x2,y2