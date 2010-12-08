'''
Created on 07.12.2010

@author: Xandman
'''
class Calc:
    ''' This Class Calculates different approximation Models of numeric data'''
    
    
    def linreg(self,X,Y):
        '''Linear Regression of several Data Points'''
        x_w = 0.0
        y_w = 0.0
        Sxx = 0.0
        Sxy = 0.0
        a = 0.0
        c = 0.0
     
        for i in range (0, len (x)):
            x_w += x[i]
        for i in range (0, len(y)):
            y_w += y[i]
            
        x_w = x_w/len(x) 
        y_w = y_w/len(y)
        
        for i in range (0, len(x)):
            Sxx += (x[i]-x_w)* (x[i]-x_w)
        for i in range (0, len(y)):
            Sxy += (x[i]-x_w)*(y[i]-y_w)
    
        Sxx = Sxx /(len(x))
        Sxy = Sxy /(len(y))   
        a = Sxy/Sxx
        c = y_w - a* x_w
     
        print " y = %f * x + 0" %a
        
        
    
    
        

#x = [168,170,161,168,162,172,164,167,170,158]
#y = [39,39,38,38,37,41,38,38,40,37]
x= [0,0.2,0.4,0.6,0.8]
y= [0,1.7,2.57,3.17,3.67]
go = Calc ()
go.linreg(x,y)