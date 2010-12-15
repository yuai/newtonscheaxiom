from Tkinter import *
from random import *

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlot:
  """ init """
  def __init__(self,_parent,_width,_height):
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
    self.canvas.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
    self.canvas.create_line(0.1*self.width,0.9*self.height,0.9*self.width,0.9*self.height,width=2,fill =_color)
    self.canvas.create_line(0.1*self.width,0.9 * self.height,0.1*self.width,0.1*self.height,width=2,fill=_color)

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
          
      return x,y




  def transAxisX(self,x,y,maxX,maxY):
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
      maxima = self.getMax(drawList)
      print maxima
      colorList = ['RoyalBlue1','DarkOliveGreen1','khaki','IndianRed1', 'brown1',
                    'LightPink1','PaleVioletRed1']

      if button == 1 :
          i = 0
          for element in drawList:
              color = colorList[i]
              print color 
              self.drawDots(element,maxima,color)
              i = i+1
        
        
        
    
  def getMax(self,searchmax):
      maxList = [0.0,0.0,0.0,0.0,0.0,0.0]
      changeList = [0.0,0.0,0.0,0.0,0.0,0.0]
      for element in searchmax:
          valuesTrans = zip(*element)
          for i in range(0,len(valuesTrans)):
              changeList[i]= max(valuesTrans[i]) 
          for j in range(0,len(changeList)):
              if changeList[j] > maxList[j]:
                  maxList[j] = changeList[j]
            
      return maxList           
              
  def drawDots(self,valueList,maxima,color):
      print 'CAME TILL DRAWDOTS'
      vn = len ( valueList[0])
      i = 0
      while i < vn-1:
          for j in range (0,len(valueList)):
              x = valueList[j][0]
              y = valueList[j][i+1]
              maxX = maxima [0]
              maxY = maxima [1]
              self.canvas.create_oval(self.transAxisX(x,y,maxX,maxY)-3,self.transAxisY(x,y,maxX,maxY)-3,self.transAxisX(x,y,maxX,maxY)+3,self.transAxisY(x,y,maxX,maxY)+3,fill = color)
          i = i+1
      
      
      

