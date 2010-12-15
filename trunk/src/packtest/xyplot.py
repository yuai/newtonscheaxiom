from Tkinter import *
from random import *

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlot:
    
  
  """ init """
  def __init__(self,_parent,_width,_height):
    self.NegativValueBool = 0
    self.width=_width
    self.height=_height
    self.parent=_parent
    self.bgcolor="#EEEEEE"
    self.fgcolor="black"
    self.drawcolor="blue"
    self.canvas = Canvas(self.parent,width=self.width,height=self.height,bg=self.bgcolor)
    self.repaint(self.fgcolor)
    self.canvas.bind('<Configure>',self.resize)
    
  def repaint(self,_color):
      if self.NegativValueBool == 0:  
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
          self.canvas.create_line(0.1*self.width,0.9*self.height,0.9*self.width,0.9*self.height,width=2,fill =_color)
          self.canvas.create_line(0.1*self.width,0.9 * self.height,0.1*self.width,0.1*self.height,width=2,fill=_color)
      else:
          self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
          self.canvas.create_line(0.05,0.5*self.height,self.width-0.05,0.5*self.height,fill=_color)
          self.canvas.create_line(0.5*self.width,0.05,0.5*self.width,self.height-0.05,fill=_color)
            

  def resize(self,event ):
    self.repaint(self.bgcolor)
    self.width=event.width-4
    self.height=event.height-4
    self.canvas.configure(width=self.width,height=self.height)
    self.repaint(self.fgcolor)

  def drawRectangle(self):
    self.repaint(self.fgcolor)
    self.canvas.create_rectangle(self.width/2-self.width/10,self.height/2-self.height/10, self.width/2+self.width/10, self.height/2+self.height/10,fill=self.drawcolor)
      
  def getExpData(self,event):
    self.repaint(self.fgcolor)
    
  def plotSampleData(self):
    data=[]
    for i in range(0,self.width,self.width/50):
  	  data.append(i)
  	  data.append(self.height-(randint(0,self.height)))
    self.repaint(self.fgcolor)
    self.canvas.create_line(data,fill=self.drawcolor)
    
  def drawSmooth(self):
      '''test for drawing splines trough points'''
      self.canvas.create_line(0,0,20,80,100,60,smooth = 'true')
      
 
  def transAxis(self,x,y,maxX,maxY):
      ''' Is OLD GET IT OUT'''
      if x == 0.0 and y == 0.0:
          x = 0.1 * self.width
          y = 0.9 * self.height
      elif x == 0.0 and y <> 0.0:
         x =  x = 0.1 * self.width
         y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
      elif x <> 0.0 and y == 0.0:
         x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
         y = 0.9 * self.height
      elif x<>0.0 and y <> 0.0:        
          x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
          y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
          
      return x,y
  
  def clear (self):
      self.repaint(self.bgcolor)
  
  
  def negTransAxisX(self,x,y,maxX,maxY):
      if x == 0.0 and y == 0.0:
          x = 0.5 *self.width
          y = 0.5 *self.height
      elif x == 0.0 and y <> 0.0:
          x = 0.5*self.width
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
      elif x <> 0.0 and y ==0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)
          y = 0.5 * self.height    
      elif x <> 0.0 and y <> 0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
           
      return x
  
  
  def negTransAxisY(self,x,y,maxX,maxY):
      if x == 0.0 and y == 0.0:
          x = 0.5 *self.width
          y = 0.5 *self.height
      elif x == 0.0 and y <> 0.0:
          x = 0.5*self.width
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
      elif x <> 0.0 and y ==0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)
          y = 0.5 * self.height    
      elif x <> 0.0 and y <> 0.0:
          x = 0.5 * self.width + (0.45*self.width)/(maxX/x)
          y = 0.5 * self.height - (0.45*self.height/(maxY/y))
           
      return y
              
          
      

  def transAxisX(self,x,y,maxX,maxY):
      ''' Transforms x,y Values into scale of Canvas'''
      if x == 0.0 and y == 0.0:
          x = 0.1 * self.width
          y = 0.9 * self.height
      elif x == 0.0 and y <> 0.0:
         x = 0.1 * self.width
         y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
      elif x <> 0.0 and y == 0.0:
         x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
         y = 0.9 * self.height
      elif x<>0.0 and y <> 0.0:        
          x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
          y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
          
      return x
  
  
  def transAxisY(self,x,y,maxX,maxY):
      ''' Transforms x,y Values into scale of Canvas'''
      if x == 0.0 and y == 0.0:
          x = 0.1 * self.width
          y = 0.9 * self.height
      elif x == 0.0 and y <> 0.0:
         x =  x = 0.1 * self.width
         y = 0.9 * self.height - (0.8*self.height)/(maxY/y)
      elif x <> 0.0 and y == 0.0:
         x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
         y = 0.9 * self.height
      elif x<>0.0 and y <> 0.0:        
          x = 0.1 * self.width + (0.8*self.width)/(maxX/x)
          y = 0.9 * self.height - (0.8*self.height)/(maxY/y)   
      return y
  
  
          
          
  def drawControl(self,drawList,button):
      maxima,minima = self.getMax(drawList)
      for i in range ( 0,len(maxima)):
          if abs(minima[i]) > maxima[i]:
              maxima [i] = abs(minima[i])
      absoluteMinimum = min(minima)
      if absoluteMinimum < 0:
          self.NegativValueBool = 1
      self.repaint(self.fgcolor)
      print maxima
      colorList = ['RoyalBlue','DarkOliveGreen','IndianRed', 'brown',
                    'LightPink','PaleVioletRed','khaki']

      if button == 1 :
          i = 0
          for element in drawList:
              color = colorList[i]
              print color 
              self.drawDots(element,maxima,color)
              i = i+1
        
        
        
    
  def getMax(self,searchmax):
      maxList = [0.0,0.0,0.0,0.0,0.0,0.0]
      minList = [0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMax = [0.0,0.0,0.0,0.0,0.0,0.0]
      changeListMin = [0.0,0.0,0.0,0.0,0.0,0.0]
      for element in searchmax:
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
              
  def drawDots(self,valueList,maxima,color):

      vn = len ( valueList[0])
      i = 0
      if self.NegativValueBool == 0:
          while i < vn-1:
              colortop = str(i+1)
              for j in range (0,len(valueList)):
                  x = valueList[j][0]
                  y = valueList[j][i+1]
                  maxX = maxima [0]
                  maxY = maxima [1]
                  self.canvas.create_oval(self.transAxisX(x,y,maxX,maxY)-3,self.transAxisY(x,y,maxX,maxY)-3,self.transAxisX(x,y,maxX,maxY)+3,self.transAxisY(x,y,maxX,maxY)+3,fill = color+colortop)
              i = i+1
      else:
          while i < vn-1:
              colortop = str(i+1)
              for j in range (0,len(valueList)):
                  x = valueList[j][0]
                  y = valueList[j][i+1]
                  maxX = maxima [0]
                  maxY = maxima [1]
                  self.canvas.create_oval(self.negTransAxisX(x,y,maxX,maxY)-3,self.negTransAxisY(x,y,maxX,maxY)-3,self.negTransAxisX(x,y,maxX,maxY)+3,self.negTransAxisY(x,y,maxX,maxY)+3,fill = color+colortop)
              i = i+1
      
      

