from infoWindow import Fail

'''
@author: Daniel Xander
'''
class Calc:
    ''' This Class has Functions calculating maxima and a linear Regression '''
    
    
    def linreg(self,X,Y,maxX,maxY):
        '''Linear Regression of several Data Points'''
        x_w = 0.0
        y_w = 0.0
        Sxx = 0.0
        Sxy = 0.0
        a = 0.0
        c = 0.0
        
        #getting mean Value of each Array
        for i in range (0, len (X)):
            x_w += X[i]
        for i in range (0, len(Y)):
            y_w += Y[i]
            
        x_w = x_w/len(X) 
        y_w = y_w/len(Y)
        
        #Skalarmultiplication
        for i in range (0, len(X)):
            Sxx += (X[i]-x_w)* (X[i]-x_w)
        for i in range (0, len(Y)):
            Sxy += (X[i]-x_w)*(Y[i]-y_w)
    
        Sxx = Sxx /(len(X))
        Sxy = Sxy /(len(Y))  
        a = Sxy/Sxx #gradient of function
        c = y_w - a* x_w #interception-point of function and Y-Axis
        xpart = 1
        x1 = 0
        y1 = c
        
        #dividining gradient until size 0.1 is reached by counter or denominator
        while i ==0:
            if a <= 0.1 or xpart<=0.1:
                i=1
            else:
                a = a / 2
                xpart = xpart / 2
                
        x2 = x1
        y2 = y1
       
        #adding gradient to startpoint until end of drawing Canvas is reached        
        while x2 <= maxX and y2 <= maxY:
            x2 = x2 + xpart
            y2 = y2 + a 
               
        return x1,y1,x2,y2
    
    
    
    def getMax(self,searchmax):
      '''Here maxima and minima of every x or y-Data set in every Experiment drawn is calculated and 
      stored in an array''' 
      #the following arrays are holding the maxima and minima of every value collumn of
      #an csv File.They are Limited to 15, so that our programm isnt able to draw more than 15 y-collumns
      #from the same file.Our group only works with a maximum of 3 y-collums.If you draw more than 4 y-collumns the
      #graph is not readable because the labels on y Axiy are interferring  
      maxList = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
      minList = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMax = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMin = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
      try:
          for element in searchmax:#hopping through every Experiment searching for maxima and minima
              valuesTrans = zip(*element)
              for i in range(0,len(valuesTrans)):
                  changeListMax[i]= max(valuesTrans[i]) 
                  changeListMin[i]= min(valuesTrans[i])
              for j in range(0,len(changeListMax)):
                  if changeListMax[j] > maxList[j]:
                      maxList[j] = changeListMax[j]
                  if changeListMin[j] < minList[j]:
                      minList[j] = changeListMin[j]
      except IndexError:
          Fail("Maximum of drawable y-datas per csv sheet is reached.\nPlease split your data into sheets with less than 15\n y-data rows and import them one after another")                       
            
      return maxList,minList    