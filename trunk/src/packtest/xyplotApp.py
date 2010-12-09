from Tkinter import *
from xyplot import *
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlotApp:
   def __init__(self, parent=0):
      #Checkbox
      CheckVar1 = IntVar()
      CheckVar2 = IntVar()
      C1 = Checkbutton(left, text = "Plot", variable = CheckVar1,onvalue = 1, offvalue = 0, height=1,width = 25)
      C2 = Checkbutton(left, text = "Table", variable = CheckVar2,onvalue = 1, offvalue = 0, height=1,width = 25)
      C1.pack(side="top")
      C2.pack(side="top")
      C1 = Checkbutton(left, text = "Plot", variable = CheckVar1,onvalue = 1, offvalue = 0, height=1,width = 25)
      C2 = Checkbutton(left, text = "Table", variable = CheckVar2,onvalue = 1, offvalue = 0, height=1,width = 25)
      C1.pack(side="top")
      C2.pack(side="top")
       
       
      scrollbar = Scrollbar(left)
      scrollbar.pack( side=RIGHT, fill=Y )

      mylist = Listbox(left, yscrollcommand = scrollbar.set )
      for line in range(100):
           mylist.insert(END, "This is line number " + str(line))

      mylist.pack( side=TOP, fill=BOTH, expand=1)
      scrollbar.config( command = mylist.yview )
      
      # XYPlot
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,400,250)
      
      # Buttons
      fButtons = Frame(main, border=2, relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bRectangle=Button(fButtons, text="Draw Rectangle",command=self.xyPlot.drawRectangle)
      bPlotData=Button(fButtons, text="Draw Data",command=self.xyPlot.plotSampleData)
      bPlotDot=Button(fButtons, text="Draw Dot",command=self.xyPlot.plotSampleData)
      bPlotLine=Button(fButtons, text="Draw Line",command=self.xyPlot.plotSampleData)
      bApproximateLine=Button(fButtons, text="Approximate Line",command=self.xyPlot.transAxis(5.0,5.0,10.0,10.0))
      bPlotDifferent=Button(fButtons, text="Different",command=self.xyPlot.drawSmooth)
      bPlotInterate=Button(fButtons, text="Draw Interate",command=self.xyPlot.plotSampleData)
      bQuit.pack(side="right")
      bRectangle.pack(side="right")
      bPlotData.pack(side="right")
      bPlotDot.pack(side="right")
      bPlotLine.pack(side="right")
      bApproximateLine.pack(side="right")
      bPlotDifferent.pack(side="right")
      bPlotInterate.pack(side="right")
      fButtons.pack(fill=X,expand="0",side="bottom")
      
      
      self.xyPlot.canvas.pack(fill="both", expand="1")
      
      self.mainWindow.pack(fill="both",expand="1")
      

def donothing():
  filewin = Toplevel(mainWindow)
  button = Button(filewin, text="Do nothing button")
  button.pack()
  
def importer():
  import os
  from Tkinter import Tk
  import tkFileDialog

  toplevel = Tk()
  toplevel.withdraw()

  filename = tkFileDialog.askopenfilename()

  if os.path.isfile(filename):
    for line in open(filename,'r'):
        print line,
  else: print 'No file chosen'
  raw_input('Ready, push Enter')




mainWindow=Tk()
mainWindow.minsize(800,600)

# PanedWindow
m1 = PanedWindow(orient=VERTICAL)
m1.pack(fill=BOTH, expand=1)
#top = Label(m1)
#m1.add(top)
m2 = PanedWindow(m1)
left = Label(m2)
m2.add(left)
main = Label(m2)
m2.add(main) 
m1.add(m2)


# Menu
menubar = Menu(mainWindow)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Import", command=importer)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=mainWindow.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)
mainWindow.config(menu=menubar)

app=XYPlotApp(main)
mainWindow.mainloop()