from Tkinter import *

class testApp3:
  def __init__( self, master ):
    self.ma = master
    self.f = Frame( self.ma )
    self.f.pack(fill=BOTH, expand=YES)
    self.width=500
    self.height=500
    self.parent=self.f
    self.bgcolor="#EEEEEE"
    self.fgcolor="black"
    self.drawcolor="blue"
    self.cv = Canvas(self.f, width=self.width, height=self.height, bg=self.bgcolor)
    self.cv.pack(fill=BOTH, expand=YES)
    #fButtons = Frame(self.f, border=2)
    self.bQuit = Button(self.f, text="Quit",command=self.f.quit)
    self.bRectangle=Button(self.f, text="Draw Rectangle",command=self.drawRectangle)
    self.bPlotData=Button(self.f, text="Draw Data",command=self.plotSampleData)
    self.bQuit.pack(side="right", anchor=S, padx=4, pady=4)
    self.bRectangle.pack(side="right", anchor=S, padx=4, pady=4)
    self.bPlotData.pack(side="right", anchor=S, padx=4, pady=4)
    #fButtons.pack(fill="both",expand="YES")
    self.cv.bind('<Configure>', self.resize )

  def repaint(self,_color):
    self.cv.create_rectangle(0,0, self.width, self.height,fill=self.bgcolor)
    self.cv.create_line(0,self.height/2,self.width,self.height/2,width=2,fill=_color,dash=(4,4))
    self.cv.create_line(self.width/2,0,self.width/2,self.height,width=2,fill=_color,dash=(10,2,10,2))

  def resize(self,event ):
    self.repaint(self.bgcolor)
    self.width=event.width
    self.height=event.height
    #self.width=event.width-4
    #self.height=event.height-4
    #self.cv.configure(width=self.width,height=self.height-30)
    self.repaint(self.fgcolor)

  def drawRectangle(self):
    self.repaint(self.fgcolor)
    self.canvas.create_rectangle(self.width/2-self.width/10,self.height/2-self.height/10, self.width/2+self.width/10, self.height/2+self.height/10,fill=self.drawcolor)
    
  def plotSampleData(self):
    data=[]
    for i in range(0,self.width,self.width/50):
        data.append(i)
        data.append(self.height-(randint(0,self.height)))
    self.repaint(self.fgcolor)
    self.canvas.create_line(data,fill=self.drawcolor)

root = Tk()
app = testApp3(root)
root.mainloop()