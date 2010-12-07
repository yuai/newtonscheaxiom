from Tkinter import *
from xyplot import *
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlotApp:
   def __init__(self, parent=0):
      self.mainWindow = Frame(parent)
      self.xyPlot=XYPlot(self.mainWindow,800,600)
      fButtons = Frame(self.mainWindow, border=2, relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bRectangle=Button(fButtons, text="Draw Rectangle",command=self.xyPlot.drawRectangle)
      bPlotData=Button(fButtons, text="Draw Data",command=self.xyPlot.plotSampleData)
      bQuit.pack(side="right")
      bRectangle.pack(side="right")
      bPlotData.pack(side="right")
      fButtons.pack(fill="both",expand="1")
      self.mainWindow.pack(fill="both",expand="1")
      
      menubar = Menu(mainWindow)
      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="Import", command=donothing)
      filemenu.add_separator()
      filemenu.add_command(label="Exit", command=mainWindow.quit)
      menubar.add_cascade(label="File", menu=filemenu)
      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Help Index", command=donothing)
      helpmenu.add_command(label="About...", command=donothing)
      menubar.add_cascade(label="Help", menu=helpmenu)
      mainWindow.config(menu=menubar)
      

def donothing():
  filewin = Toplevel(mainWindow)
  button = Button(filewin, text="Do nothing button")
  button.pack()

mainWindow=Tk()
app=XYPlotApp(mainWindow)
mainWindow.mainloop()