from Tkinter import *
from random import *
from calc import Calc
from infoWindow import Fail
from gridTransform import GridTransform

'''
@author: Daniel Xander
@author: John Truong
'''
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlot:
  """ The XYPlot Class is responsible for everything concerning the Canvas.It contains
  several drawing functions and scales the given data points onto the drawing layer.    """
  
  def __init__(self,_parent,_width,_height):
    ''' This Constructor sets default values for the main drawing Window'''  
    self.NegativValueBool = 0 #This 'Bool' decides which Grid-form is drawn
    self.ALLSETGO = 0         #This 'Bool'is needed because of resize problems during initialisation
    self.width=_width         #initial width of canvas
    self.height=_height       #initial height of canvas
    self.parent=_parent       #parent window of canvas
    self.bgcolor="white"
    self.fgcolor="black"
    self.canvas = Canvas(self.parent,width=self.width,height=self.height,bg=self.bgcolor)
    self.repaint(self.fgcolor)
    self.canvas.bind('<Configure>',self.resize)
    self.colorList = ['#0000FF','#FF0000','#00FF00', '#FFCC00',
                    '#FF66FF','#00FFFF'] #blue,red,green,yellow,pink,turky
    self.calc = Calc()                   #Calculating Object, used regression and maxima search
    self.gridtransform = GridTransform() #Object, used for scaling 
  
  def repaint(self,_color,maxima = None):
      '''The repaint method is called initionally and everytime something in the canvas is changed.
      It is splittet into two parts, one Drawing the main L Grid for just positive Values and one in
      cross Format for positiv and negativ Values.Every drawn Object is scaled with width and height
      of the canvas'''  
# -----------------------------------------------------------------
# ---------------------Setting Up L Grid
# -----------------------------------------------------------------      
      if self.NegativValueBool == 0:  
          #Drawing Backround of Plot-Canvas
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
         
          nextX = 0
          nextY = 0
          for i in range (0,7):
              #Drawing littlelines on X-Axis
              self.canvas.create_line((0.1)*self.width+nextX,0.9*self.height,(0.1)*self.width+nextX,0.91*self.height,width=2,fill=_color)
              #Drawing lightGrey BackroundGrid X-Direction
              self.canvas.create_line((0.1)*self.width+nextX,0.9*self.height,(0.1)*self.width+nextX,0.1*self.height,width=0.1,fill= 'LightGrey')
              #Drawing littlelines on Y-Axis
              self.canvas.create_line(0.1*self.width,0.9*self.height-nextY,(0.09)*self.width,0.9*self.height-nextY,width=2,fill=_color)
              #Drawing lightGrey BackroundGrid Y-Direction
              self.canvas.create_line(0.1*self.width,0.9*self.height-nextY,0.9*self.width,0.9*self.height-nextY,width=0.1,fill='LightGrey')
              nextX = nextX +(0.8*self.width)/6
              nextY = nextY +(0.8*self.height)/6
              
          #Drawing X-Axis and Y-Axis
          self.canvas.create_line(0.1*self.width,0.9*self.height,0.9*self.width,0.9*self.height,width=2,fill =_color)
          self.canvas.create_line(0.1*self.width,0.9*self.height,0.1*self.width,0.1*self.height,width=2,fill=_color)
# -----------------------------------------------------------------
# --------Calculating and writing of interval labels for L Grid
# -----------------------------------------------------------------              
          if maxima != None:
              next = 0
              x_float = 0
              for i in range(0,7):
              #Drawing value Labels on X-Axis    
                  if i<1:
                      #to prevent division by zero
                      x_float = 0
                  else:
                      #stepsize on x axis is maxima divided by 6
                      x_float = x_float + maxima[0]/6
                 
                  stringx_float = round(x_float,3) #important to use new float, to prevent rounding error  
                  x_str = str(stringx_float)
                 
                  if x_str != '0':
                      self.canvas.create_text(0.1 * self.width+next,0.92*self.height, text=x_str)
                  next = next +(0.8*self.width)/6
              
              countMaxima = 0
              for i in range (0,len(maxima)-1):
                  #look how many values must be drawn per step
                              if maxima[i]!= 0.0:
                                  countMaxima = countMaxima +1
                        
              newY  = 0        
              for countY in range (1,countMaxima):
              #Drawing value labels on Y-Axis, depending on Maximum of each y  
                  if countY < 5:
                      next = 0
                      y_float = 0
                      for i in range (0,7):
                          if i<1:
                              y_float = 0
                          else:
                              y_float = y_float + maxima[countY]/6#divide maxima by 6 to get step values
                          stringy_float = round (y_float,3)
                          y_str = str(stringy_float)
                          if stringy_float != 0.0:
                              self.canvas.create_text(0.05*self.width,(0.9+newY)*self.height-next,text = y_str)
                          next = next + (0.8*self.height)/6        
                      newY = newY+0.018   
                  else:
                      Fail('It is not possible to show more than 4 Y-value Labels\n on the Y-Axis due to readability.All are drawn, but only the first 4 value Labels \n are shown, if you want to compare more than 4 you have to split up the .csv file and\n  import again ')
                      break
                      
      else:
# -----------------------------------------------------------------
# ---------------------Setting Up Cross Grid
# -----------------------------------------------------------------
          #Drawing Backround of Plot-Canvas
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
          self.canvas.create_text(0.48*self.width,0.53*self.height,text = '0')
          nextX = 0
          nextY = 0
          for i in range (0,14):
              #Drawing littlelines on X-Axis
              self.canvas.create_line((0.05)*self.width+nextX,0.5*self.height,(0.05)*self.width+nextX,0.51*self.height,width=2,fill=_color)
              #Drawing lightGrey BackroundGrid X-Direction
              self.canvas.create_line((0.05)*self.width+nextX,0.05*self.height,(0.05)*self.width+nextX,0.95*self.height,width=0.1,fill='LightGrey')
              #Drawing littlelines on Y-Axis
              self.canvas.create_line(0.5*self.width,0.95*self.height-nextY,0.49*self.width,0.95*self.height-nextY,width=2,fill=_color)
              #Drawing lightGrey BackroundGrid Y-Direction
              self.canvas.create_line(0.05*self.width,0.95*self.height-nextY,0.95*self.width,0.95*self.height-nextY,width=0.1,fill='LightGrey')
              nextX = nextX +(0.45*self.width)/6
              nextY = nextY +(0.45*self.height)/6
              
          #Drawing X-Axis and Y-Axis    
          self.canvas.create_line(0.05,0.5*self.height,self.width-0.05,0.5*self.height,fill=_color)
          self.canvas.create_line(0.5*self.width,0.05,0.5*self.width,self.height-0.05,fill=_color)   
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
                  
                  if countY < 5:
                      for i in range (0,7):
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
                      newY = newY + 0.018
                  else:
                       Fail('It is not possible to show more than 4 Y-value Labels\n on the Y-Axis due to readability.All are drawn, but only the first 4 value Labels \n are shown, if you want to compare more than 4 you have to split up the .csv file and\n  import again ')  
                       break    
                    
  def resize(self,event ):
    '''This Method is called by an event thrown by Mainwindow.It resizes the canvas.
    We had to post the scalefit behind the initialisatioprocess of XY-Plot by using ALLSETGO.
    If this isn't done the scale ends up in an endless Loop'''
    if self.ALLSETGO <=2:
        self.ALLSETGO += 1
    else:
        self.ALLSETGO = 2    
   
    if self.ALLSETGO >= 2:
        self.repaint(self.bgcolor)
        self.width=event.width 
        self.height=event.height
        self.canvas.configure(width=self.width,height=self.height)
        self.repaint(self.fgcolor)
  
  def clear (self):
      '''This method clears the canvas, it must be called on update, or when a new set is drawn so that
      the old drawings aren't interferring with the new.'''
      self.repaint(self.bgcolor)

  
# -----------------------------------------------------------------
# -----Different drawing Functions to Draw on Canvas
# -----------------------------------------------------------------   
                    
  def drawControl(self,drawList,metaList,button):
      '''This Method decides which drawing Function is called, and gives the drawing Function the color
      for every Experiment and an maxima array used to scale data points'''
      maxima,minima = self.calc.getMax(drawList)
      for i in range ( 0,len(maxima)):
          if abs(minima[i]) > maxima[i]:
              maxima [i] = abs(minima[i])
      absoluteMinimum = min(minima)
      
      #Here is decided which Grid is taken for the drawing by setting Negativ Value bool depending on absolute minimum of all minima
      if absoluteMinimum < 0:
          self.NegativValueBool = 1
      else:
          self.NegativValueBool = 0   
      
      #Looking if max and min are correct to avoid dividing through zero
      if max(maxima)==0 and min(minima)==0:
          self.NegativValueBool = 2  
          
              
      
      self.repaint(self.fgcolor,maxima)
      self.drawMeta(metaList)
      
      
      if self.NegativValueBool != 2:#If this is not true an error ocurred in getMax function.
     
      #different drawing Functions are called depending on which button is pushed    
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
  
  def drawMeta(self,metaList):
      '''The units the x and y Axis are drawn on canvas.X is set default on "t in Sekunden", whereas y is taken from the 
      metadatadictionary of an given Experiment'''       
      if self.NegativValueBool == 0:
          self.canvas.create_text(0.90*self.width, 0.95*self.height, text="t in Sekunden")
      else:
           self.canvas.create_text(0.93*self.width, 0.60*self.height, text="t in Sekunden")
              
      space = 0
      for i in range(0,len(metaList)):
          if metaList[i]['vn_unit'].find('|') != -1:#Look if there is more than one MetaUnit
              singledata =  metaList[i]['vn_unit'].split('|')
              down = 0
              for single in range (0,len(singledata)):#Draw Meta units with fading colors exactly like their values
                  self.canvas.create_text((0.08+space)*self.width, (0.02+down)*self.height, text=singledata[single],fill =  self.colorFade(self.colorList[i],single))
                  down = down + 0.018
          else:        
              self.canvas.create_text((0.08+space)*self.width, 0.02*self.height, text=metaList[i]['vn_unit'],fill = self.colorList[i])
          space = space+0.08
               
  def drawLine(self,valueList,maxima,color,smooth):
       '''This Method is drawing an Line in the given color through every point of the valueList.
       The Line is scaled by the maxima array and can change into three patterns for three different
       y-Axis.If smooth is set True it draws an spline approximation through the points.Some Points may
       not lie on this approximatet line.'''
       self.drawDots(valueList, maxima, color)#First Draw all Dots, so that you can see the original for reference
       vn = len(valueList[0])#
       LineArray = []
       i = 0
       pattern  = None # Is the pattern of the line if more than one y-List is in the 
       
       while i < vn-1:
         
         del LineArray[:]
         
         if 0 < i < 4:#Fading color of the first 3 Experiments
             newcolor = self.colorFade(color,i)
             if i == 1:
                 pattern = (1,2,3,4)
             elif i == 2:
                     pattern =(1,2) 
             else:
                 
                 pattern = None         
         else:
             
             newcolor = color
               
         for j in range(0,len(valueList)):
             x1 = valueList[j][0]
             y1 = valueList[j][i+1]
             maxX = maxima[0]
             maxY = maxima[i+1]
             if self.NegativValueBool == 0 :#If set to zero, method is drawing on L-Grid scale
                 LineArray.append(self.gridtransform.transAxisX(x1,y1,maxX,maxY,self.width))
                 LineArray.append(self.gridtransform.transAxisY(x1,y1,maxX,maxY,self.height))
             else: # Method is drawing on Cross-Grid scale     
                 LineArray.append(self.gridtransform.negTransAxisX(x1,y1,maxX,maxY,self.width))
                 LineArray.append(self.gridtransform.negTransAxisY(x1,y1,maxX,maxY,self.height))
               
         if smooth == 0:
             #Drawing direct Lines from point to point
             self.canvas.create_line(LineArray,smooth = "false",width=2,fill = newcolor,dash = pattern)
         else:
             #Drawing approximation using given points
             self.canvas.create_line(LineArray,smooth = "true",width=2,fill = newcolor,dash = pattern)
               
         i=i+1  
                         
  def drawDots(self,valueList,maxima,color):
      '''Draws a dot for every x,y Koordinate in the valueList.It uses the maxima Array to scale
      and the color, which it can fade  in case of more than one y-Axis.'''
      vn = len ( valueList[0])
      if len(valueList) < 40:
          ovalsize = 3
      else:
          ovalsize = 2    
      i = 0
     
      while i < vn-1:
          if 0 < i < 4:
              newcolor = self.colorFade(color,i)
          else:
              newcolor = color   
          for j in range (0,len(valueList)):
              x = valueList[j][0]
              y = valueList[j][i+1]
              maxX = maxima [0]
              maxY = maxima [i+1]
        
              if self.NegativValueBool == 0:#If 0,drawing on scale of L Grid   
                  self.canvas.create_oval(self.gridtransform.transAxisX(x,y,maxX,maxY,self.width)-ovalsize
                                          ,self.gridtransform.transAxisY(x,y,maxX,maxY,self.height)-ovalsize
                                          ,self.gridtransform.transAxisX(x,y,maxX,maxY,self.width)+ovalsize
                                          ,self.gridtransform.transAxisY(x,y,maxX,maxY,self.height)+ovalsize,fill = newcolor)
              else: #drawing on scale of Cross-Grid      
                  self.canvas.create_oval(self.gridtransform.negTransAxisX(x,y,maxX,maxY,self.width)-ovalsize
                                          ,self.gridtransform.negTransAxisY(x,y,maxX,maxY,self.height)-ovalsize
                                          ,self.gridtransform.negTransAxisX(x,y,maxX,maxY,self.width)+ovalsize
                                          ,self.gridtransform.negTransAxisY(x,y,maxX,maxY,self.height)+ovalsize,fill = newcolor)
          i = i+1
                         
  def drawRegLine(self,valueList,maxima,color):
       '''This method uses the Calc Class to draw a Linear Regression of the Data points 
       in the valueList.I also changes color and pattern for the first 3 Lines pro Experiment'''
       self.drawDots(valueList, maxima, color)
       regList = zip(*valueList)
       vn = len ( valueList[0])
       i = 0
       pattern = None
       
       while i < vn-1:
           if 0 < i < 4:
               newcolor = self.colorFade(color,i)
               if i == 1:
                   pattern = (1,2,3,4)
               elif i == 2:
                   pattern =(1,2) 
               else:
                   pattern = None 
           else:
               newcolor = color
               
           for j in range (0,len(valueList)):  
               #using calc.linreg to generate an regression
               x1,y1,x2,y2=self.calc.linreg(regList[0],regList[i+1],maxima[0],maxima[i+1])
                   
               maxX = maxima [0]
               maxY = maxima [i+1]
               if self.NegativValueBool == 0:
                   #drawing in L-Grid scale
                   x1 = self.gridtransform.transAxisX(x1, y1, maxX, maxY, self.width)
                   y1 = self.gridtransform.transAxisY(x1, y1, maxX, maxY, self.height)
                   x2 = self.gridtransform.transAxisX(x2, y2, maxX, maxY, self.width)
                   y2 = self.gridtransform.transAxisY(x2, y2, maxX, maxY, self.height)
               else:    
                   #drawing in Cross-Grid scale
                   x1 = self.gridtransform.negTransAxisX(x1, y1, maxX, maxY, self.width)
                   y1 = self.gridtransform.negTransAxisY(x1, y1, maxX, maxY, self.height)
                   x2 = self.gridtransform.negTransAxisX(x2, y2, maxX, maxY, self.width)
                   y2 = self.gridtransform.negTransAxisY(x2, y2, maxX, maxY, self.height)
                  
               self.canvas.create_line(x1,y1,x2,y2,width=1.5,fill = newcolor,dash = pattern)
           i = i+1    
      
# -----------------------------------------------------------------
# ------------Function to Fade color from bright to dark 
# -----------------------------------------------------------------          
  def colorFade(self,hexstring,fade):
      '''This Function converts the given hex-value into RGB, subtracts the maximum so that the color
      gets darker, than it reconverts into hex and returns the new color'''
      rgb = []
      hex = hexstring.strip('#')
      hexlen = len(hex)
      for i in range(0,hexlen,hexlen/3):
          str = hex[i]+hex[i+1]
          rgb.append(int(str,16))
      count = 0 
      index = rgb.index(max(rgb))   
      rgb[index]=rgb[index]-(60*fade)
      if rgb[index]<= 0:
          rgb[index]=0
      rgbtuple  = tuple(rgb)    
          
      
      return "#%02x%02x%02x"%rgbtuple