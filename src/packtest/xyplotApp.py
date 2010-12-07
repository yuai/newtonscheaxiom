from Tkinter import *
from xyplot import *
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class XYPlotApp:
   def __init__(self, parent=0):
       
      
      m1 = PanedWindow()
      m1.pack(fill=BOTH, expand=1)
      left = Label(m1, text="left pane")
      m1.add(left)
      
      m2 = PanedWindow(m1, orient=VERTICAL)
      m1.add(m2)
      top = Label(m2, text="top pane")
      m2.add(top)
      bottom = Label(m2, text="bottom pane")
      m2.add(bottom)
      
      scrollbar = Scrollbar(left)
      scrollbar.pack( side = RIGHT, fill=Y )

      mylist = Listbox(left, yscrollcommand = scrollbar.set )
      for line in range(100):
           mylist.insert(END, "This is line number " + str(line))

      mylist.pack( side = LEFT, fill = BOTH )
      scrollbar.config( command = mylist.yview )

      
      
      
      #Checkbox
      CheckVar1 = IntVar()
      CheckVar2 = IntVar()
      C1 = Checkbutton(left, text = "Plot", variable = CheckVar1,onvalue = 1, offvalue = 0, height=5,width = 10)
      C2 = Checkbutton(left, text = "Table", variable = CheckVar2,onvalue = 1, offvalue = 0, height=5,width = 10)
      C1.pack()
      C2.pack()
      
      # XYPlot
      self.mainWindow = Frame(parent)
      self.xyPlot=XYPlot(top,500,300)
      
      # Buttons
      fButtons = Frame(bottom, border=2, relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bRectangle=Button(fButtons, text="Draw Rectangle",command=self.xyPlot.drawRectangle)
      bPlotData=Button(fButtons, text="Draw Data",command=self.xyPlot.plotSampleData)
      bQuit.pack(side="right")
      bRectangle.pack(side="right")
      bPlotData.pack(side="right")
      fButtons.pack(fill="both",expand="1")
      
      self.mainWindow.pack(fill="both",expand="1")
      

def donothing():
  filewin = Toplevel(mainWindow)
  button = Button(filewin, text="Do nothing button")
  button.pack()



mainWindow=Tk()
mainWindow.minsize(500,350)

# Menu beginne
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

app=XYPlotApp(mainWindow)
mainWindow.mainloop()