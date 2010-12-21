from Tkinter import *
from random import *
from calc import Calc
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlot:
    
  
  """ The XYPlot Class is responsible for everything concerning the Canvas.It contains
  several drawing functions and scales the given data points onto the drawing layer.    """
  
  def __init__(self,_parent,_width,_height):
    ''' This Constructor sets default values for the main drawing Window'''  
    self.NegativValueBool = 0
    self.width=_width
    self.height=_height
    self.parent=_parent
    self.bgcolor="white"
    self.fgcolor="black"
    self.drawcolor="blue"
    self.canvas = Canvas(self.parent,width=self.width,height=self.height,bg=self.bgcolor)
    self.repaint(self.fgcolor)
    self.canvas.bind('<Configure>',self.resize)
    self.colorList = ['RoyalBlue','DarkOliveGreen','IndianRed', 'brown',
                    'LightPink','PaleVioletRed','khaki']
  
  
    
  def repaint(self,_color,maxima = None):
      '''The repaint method is called initionally and everytime something in the canvas is changed.
      It is splittet into two parts, one Drawing the main L Grid for just positive Values and one in
      cross Format for positiv and negativ Values.'''  
      
# -----------------------------------------------------------------
# ---------------------Setting Up L Grid
# -----------------------------------------------------------------      
      if self.NegativValueBool == 0:  
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
          self.canvas.create_line(0.1*self.width,0.9*self.height,0.9*self.width,0.9*self.height,width=2,fill =_color)
          self.canvas.create_line(0.1*self.width,0.9 * self.height,0.1*self.width,0.1*self.height,width=2,fill=_color)
          self.canvas.create_line(0.9*self.width,0.9*self.height,0.9*self.width,0.91*self.height,width=2,fill=_color)
          next = 0
          for i in range (0,7):
              self.canvas.create_line((0.1)*self.width+next,0.9*self.height,(0.1)*self.width+next,0.91*self.height,width=2,fill=_color)
              self.canvas.create_line((0.1)*self.width+next,0.9*self.height,(0.1)*self.width+next,0.1*self.height,width=0.1,fill= 'LightGrey')
              next = next +(0.8*self.width)/6
          next = 0    
          for i in range (0,7):
              self.canvas.create_line(0.1*self.width,0.9*self.height-next,(0.09)*self.width,0.9*self.height-next,width=2,fill=_color)
              self.canvas.create_line(0.1*self.width,0.9*self.height-next,(0.9)*self.width,0.9*self.height-next,width=0.1,fill='LightGrey')
              next = next +(0.8*self.height)/6
# -----------------------------------------------------------------
# --------Calculating and writing of interval labels for L Grid
# -----------------------------------------------------------------              
          if maxima != None:
              next = 0
              x_float = 0
              for i in range(0,7):
              #Drawing text Labels on X-Axis    
                  if i<1:
                      x_float = 0
                  else:
                      x_float = x_float + maxima[0]/6
                  stringx_float = round(x_float,3)   
                  x_str = str(stringx_float)
                  if x_str != '0':
                      self.canvas.create_text(0.1 * self.width+next,0.92*self.height, text=x_str)
                  next = next +(0.8*self.width)/6
              
              countMaxima = 0
              for i in range (0,len(maxima)-1):
                              if maxima[i]!= 0.0:
                                  countMaxima = countMaxima +1
                        
              newY  = 0        
              for countY in range (1,countMaxima):
              #Drawing text labels on Y-Axis, depending on Maximum of each y     
                  next = 0
                  y_float = 0
                  for i in range (0,7):
                      if i<1:
                          y_float = 0
                      else:
                          y_float = y_float + maxima[countY]/6
                      stringy_float = round (y_float,3)
                      y_str = str(stringy_float)
                      if stringy_float != 0.0:
                          self.canvas.create_text(0.05*self.width,(0.9+newY)*self.height-next,text = y_str)
                      next = next + (0.8*self.height)/6        
                  newY = newY+0.015    
                      
                      
      else:
# -----------------------------------------------------------------
# ---------------------Setting Up Cross Grid
# -----------------------------------------------------------------
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
          self.canvas.create_line(0.05,0.5*self.height,self.width-0.05,0.5*self.height,fill=_color)
          self.canvas.create_line(0.5*self.width,0.05,0.5*self.width,self.height-0.05,fill=_color)
          self.canvas.create_text(0.48*self.width,0.53*self.height,text = '0')
          next = 0
          for i in range (0,14):
              self.canvas.create_line((0.05)*self.width+next,0.5*self.height,(0.05)*self.width+next,0.51*self.height,width=2,fill=_color)
              self.canvas.create_line((0.05)*self.width+next,0.05*self.height,(0.05)*self.width+next,0.95*self.height,width=0.1,fill='LightGrey')
              next = next +(0.45*self.width)/6
          next = 0    
          for i in range (0,14):
              self.canvas.create_line(0.5*self.width,0.95*self.height-next,0.49*self.width,0.95*self.height-next,width=2,fill=_color)
              self.canvas.create_line(0.05*self.width,0.95*self.height-next,0.95*self.width,0.95*self.height-next,width=0.1,fill='LightGrey')
              next = next +(0.45*self.height)/6
# -----------------------------------------------------------------
# -----Calculating and writing of interval labels for Cross Grid
# -----------------------------------------------------------------
        
          if maxima != None:
              next = 0
              x_float = 0
              negx_float = 0
              for i in range(0,7):
              #Drawing text Labels on X-Axis    
                  if i==0:
                      negx_float = -maxima[0]
                      
                  else:
                      negx_float =negx_float + (maxima[0]/6)
                      x_float = x_float + (maxima[0]/6)        
                  stringnegx_float = round(negx_float,3)
                  stringx_float = round(x_float,3)    
                  negx_str = str(stringnegx_float)
                  x_str = str(stringx_float)
                  if stringnegx_float != 0.0:
                      self.canvas.create_text(0.05 * self.width+next,0.53*self.height, text=negx_str)
                  if stringx_float != 0.0:
                      self.canvas.create_text(0.5 * self.width+next,0.53*self.height, text=x_str)
                  next = next +(0.45*self.width)/6
              
              countMaxima = 0
              for i in range (0,len(maxima)-1):
                              if maxima[i]!= 0.0:
                                  countMaxima = countMaxima +1
                                  
              newY = 0
              for countY in range (1,countMaxima):
              #Drawing text labels on Y-Axis, depending on Maximum of each y    
                  next = 0
                  y_float = 0
                  negy_float = 0
                  for i in range (0,14):
                      if i<1:
                          negy_float = -maxima[countY]
                      else:
                          negy_float = negy_float + (maxima[countY]/6)
                          y_float = y_float + maxima[countY]/6
                          
                      stringnegy_float = round(negy_float,3)
                      stringy_float = round(y_float,3)    
                      negy_str = str(stringnegy_float)
                      y_str = str(stringy_float)
                      if stringnegy_float != 0.0:
                          self.canvas.create_text(0.45*self.width,(0.95+newY)*self.height-next,text = negy_str)
                      if stringy_float != 0.0:    
                          self.canvas.create_text(0.45*self.width,(0.5+newY)*self.height-next,text = y_str)
                      
                      next = next + (0.45*self.height)/6
                  newY = newY + 0.015    
                      
                              
              
        
            

  def resize(self,event ):
    '''resizes canvas if user changes size of Application'''  
    self.repaint(self.bgcolor)
    self.width=event.width-4 # This is just tested on Windows 7, have to look if it works on Mac OS 
    self.height=event.height-4
    self.canvas.configure(width=self.width,height=self.height)
    self.repaint(self.fgcolor)
      
  def getExpData(self,event):
    self.repaint(self.fgcolor)
  
  def clear (self):
      '''This method clears the canvas, it must be called on update, or when a new set is drawn so that
      the old drawings aren't interferring with the new.'''
      self.repaint(self.bgcolor)
  
# -----------------------------------------------------------------
# --------------Several Transformation Functions 
# -----------------------------------------------------------------  
  
  def negTransAxisX(self,x,y,maxX,maxY):
      ''' returns an Transformed x value for the Crossgrid'''
      if x == 0.0 and y == 0.0:
          x = 0.5 *self.width
      elif x == 0.0 and y <> 0.0:
          x = 0.5*self.width
      elif x <> 0.0 and y ==0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)   
      elif x <> 0.0 and y <> 0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)
           
      return x
  
  
  def negTransAxisY(self,x,y,maxX,maxY):
      ''' returns an Transformed y value for the Crossgrid'''
      if x == 0.0 and y == 0.0:
          y = 0.5 *self.height
      elif x == 0.0 and y <> 0.0:
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
      elif x <> 0.0 and y ==0.0:
          y = 0.5 * self.height    
      elif x <> 0.0 and y <> 0.0:
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
           
      return y
              
          
      

  def transAxisX(self,x,y,maxX,maxY):
      ''' returns an Transformed x value for the L Grid'''
      if x == 0.0 and y == 0.0:
          x = 0.1 * self.width
      elif x == 0.0 and y <> 0.0:
         x = 0.1 * self.width
      elif x <> 0.0 and y == 0.0:
         x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
      elif x<>0.0 and y <> 0.0:        
          x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
          
      return x
  
  
  def transAxisY(self,x,y,maxX,maxY):
      ''' returns an Transformed y value for the L Grid'''
      if x == 0.0 and y == 0.0:
          y = 0.9 * self.height
      elif x == 0.0 and y <> 0.0:
         y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
      elif x <> 0.0 and y == 0.0:
         y = 0.9 * self.height
      elif x<>0.0 and y <> 0.0:        
          y = 0.9 * self.height - (0.8*self.height)/(maxY/y)   
      
      return y
  
# -----------------------------------------------------------------
# -----Different drawing Functions to Draw on Canvas
# -----------------------------------------------------------------   
          
          
  def drawControl(self,drawList,metaList,button):
      '''This Method decides which drawing Function is called, and gives the drawing Function the color
      for every Experiment and an maxima array used to scale data points'''
      maxima,minima = self.getMax(drawList)
      for i in range ( 0,len(maxima)):
          if abs(minima[i]) > maxima[i]:
              maxima [i] = abs(minima[i])
      absoluteMinimum = min(minima)
      #Here is decided which Grid is taken for the drawing by setting Negativ Value bool depending on absolute minimum of all minimum
      if absoluteMinimum < 0:
          self.NegativValueBool = 1
      else:
          self.NegativValueBool = 0   
      
      self.repaint(self.fgcolor,maxima)
      self.drawMeta(metaList)
      #different drawing Functions are called dependig on which button is pushed
      if button == 1 :
          i = 0
          for element in drawList:
              color = self.colorList[i]
              self.drawDots(element,maxima,color)
              i = i+1
      elif button == 2 :
           i = 0
           for element in drawList:
              color = self.colorList[i]
              self.drawLine(element,maxima,color,0)
              i = i+1
      elif button == 3 :
           i = 0
           for element in drawList:
              color = self.colorList[i]
              self.drawRegLine(element,maxima,color)
              i = i+1
      elif button == 4:
           i = 0
           for element in drawList:
              color = self.colorList[i]
              self.drawLine(element,maxima,color,1)
              i = i+1   
                  
        
        
        
    
  def getMax(self,searchmax):
      '''Here maxima and minima of every x or y-Data set in every Experiment drawn is calculatet and 
      stored in an array''' 
      maxList = [0.0,0.0,0.0,0.0,0.0,0.0]
      minList = [0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMax = [0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMin = [0.0,0.0,0.0,0.0,0.0,0.0]
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
            
      return maxList,minList
  
  def drawMeta(self,metaList):
      '''The units the x and y Axis are drawn on canvas.X is set default on "t in Sekunden", whereas y is taken from the 
      metadatadictionary of an given Experiment'''       
      if self.NegativValueBool == 0:
          self.canvas.create_text(0.90*self.width, 0.95*self.height, text="t in Sekunden")
          space = 0
          for i in range(0,len(metaList)):
              self.canvas.create_text((0.08+space)*self.width, 0.05*self.height, text=metaList[i]['vn_unit']+' ; ',fill = self.colorList[i])
              space = space+0.08
              
      else:
          self.canvas.create_text(0.93*self.width, 0.60*self.height, text="t in Sekunden")
          space = 0
          for i in range(0,len(metaList)):
              self.canvas.create_text((0.46-space)*self.width, 0.02*self.height, text=metaList[i]['vn_unit']+' ; ',fill = self.colorList[i])
              space = space+0.08
          


  def drawLine(self,valueList,maxima,color,smooth):
       self.drawDots(valueList, maxima, color)
       vn = len(valueList[0])
       LineArray = []
       i = 0
       if self.NegativValueBool == 0 :
           while i < vn-1:
               del LineArray[:]
               if i < 4:
                   colortop = str(i+1)
               else:
                   colortop = '1'
               
               for j in range(0,len(valueList)):
                   print valueList[j][i+1] 
                   x1 = valueList[j][0]
                   y1 = valueList[j][i+1]
                   maxX = maxima[0]
                   maxY = maxima[i+1]
                   LineArray.append(self.transAxisX(x1,y1,maxX,maxY))
                   LineArray.append(self.transAxisY(x1,y1,maxX,maxY))
               
               if smooth == 0:
                   self.canvas.create_line(LineArray,smooth = "false",fill = color+colortop)
               else:
                   self.canvas.create_line(LineArray,smooth = "true",fill = color+colortop)
               i=i+1  
       else:
           while i < vn-1:
              del LineArray[:]
              if i < 4:
                  colortop = str(i+1)
              else:
                  colortop = '1' 
              for j in range (0,len(valueList)-1):
                  x1 = valueList[j][0]
                  y1 = valueList[j][i+1]
                  x2 = valueList[j+1][0]
                  y2 = valueList[j+1][i+1]
                  maxX = maxima [0]
                  maxY = maxima [i+1]
                  LineArray.append(self.negTransAxisX(x1,y1,maxX,maxY))
                  LineArray.append(self.negTransAxisY(x1,y1,maxX,maxY))
                  LineArray.append(self.negTransAxisX(x2,y2,maxX,maxY))
                  LineArray.append(self.negTransAxisY(x2,y2,maxX,maxY))
                  
              if smooth == 0:
                  self.canvas.create_line(LineArray,smooth = 'false',fill = color+colortop)
              else:
                  self.canvas.create_line(LineArray,smooth = 'true',fill = color+colortop)
                  
              i = i+1
  
      
      
               
              
  def drawDots(self,valueList,maxima,color):
      
      vn = len ( valueList[0])
      i = 0
      if self.NegativValueBool == 0:
          while i < vn-1:
              if i < 4:
                  colortop = str(i+1)
              else:
                  colortop = '1'    
              for j in range (0,len(valueList)):
                  x = valueList[j][0]
                  y = valueList[j][i+1]
                  maxX = maxima [0]
                  maxY = maxima [i+1]
                  self.canvas.create_oval(self.transAxisX(x,y,maxX,maxY)-3,self.transAxisY(x,y,maxX,maxY)-3,self.transAxisX(x,y,maxX,maxY)+3,self.transAxisY(x,y,maxX,maxY)+3,fill = color+colortop)
              i = i+1
      else:
          while i < vn-1:
              colortop = str(i+1)
              if i < 4:
                  colortop = str(i+1)
              else:
                  colortop = '1' 
              for j in range (0,len(valueList)):
                  x = valueList[j][0]
                  y = valueList[j][i+1]
                  maxX = maxima [0]
                  maxY = maxima [i+1]
                  self.canvas.create_oval(self.negTransAxisX(x,y,maxX,maxY)-3,self.negTransAxisY(x,y,maxX,maxY)-3,self.negTransAxisX(x,y,maxX,maxY)+3,self.negTransAxisY(x,y,maxX,maxY)+3,fill = color+colortop)
              i = i+1
              
              
              
              
              
  def drawRegLine(self,valueList,maxima,color):
       self.drawDots(valueList, maxima, color)
       regList = zip(*valueList)
       calc = Calc()
       vn = len ( valueList[0])
       i = 0
       if self.NegativValueBool == 0:
           if i < 4:
                  colortop = str(i+1)
           else:
               colortop = '1'
           for j in range (0,len(valueList)): 
               x1,y1,x2,y2=calc.linreg(regList[0],regList[i+1],maxima[0],maxima[i+1])
               maxX = maxima [0]
               maxY = maxima [i+1]
               x1 = self.transAxisX(x1, y1, maxX, maxY)
               y1 = self.transAxisY(x1, y1, maxX, maxY)
               x2 = self.transAxisX(x2, y2, maxX, maxY)
               y2 = self.transAxisY(x2, y2, maxX, maxY)
               
               self.canvas.create_line(x1,y1,x2,y2,width=1.5,fill = color+colortop)
               
       else:
            if i < 4:
                  colortop = str(i+1)
            else:
                  colortop = '1' 
                  
            for j in range (0,len(valueList)): 
               x1,y1,x2,y2=calc.linreg(regList[0],regList[i+1],maxima[0],maxima[i+1])
               maxX = maxima [0]
               maxY = maxima [i+1]
               x1 = self.negTransAxisX(x1, y1, maxX, maxY)
               y1 = self.negTransAxisY(x1, y1, maxX, maxY)
               x2 = self.negTransAxisX(x2, y2, maxX, maxY)
               y2 = self.negTransAxisY(x2, y2, maxX, maxY)
               
               self.canvas.create_line(x1,y1,x2,y2,width=1.5,fill = color+colortop)
                  
                   
               
           
           
       
      
      
      

