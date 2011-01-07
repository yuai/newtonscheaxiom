from Tkinter import *
from xyplot import XYPlot
from newtonImporter import NewtonImporter
from newtonAppFunction import NewtonAppFunction

'''
@author: Daniel Xander
@author: John Truong
'''    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class NewtonApp:
   ''' the class NewtonApp is the main class of the application.
       this class generate the GUI for the application.
   '''

   def __init__(self, parent=0,left=0):
      ''' constructor of the application '''
      
      self.mainWindow = Frame(main) # initial main Window
      
      self.xyPlot=XYPlot(main,800,600) # initial XYPlot default size for canvas
      
      self.var = IntVar() # variable for the radioButton (on or off)
      
      self.appFunction = NewtonAppFunction(left,self.xyPlot,self.var)
      
      self.appFunction.initListBox() # initial ScrollBar, ListBox
                                     # it is a function, because it has to add experiment
      
      self.initRadioButton() # initial button for canvas                               
      self.xyPlot.canvas.pack(fill="both", expand="1") # pack canvas after buttons for resize
      self.mainWindow.pack(fill="both",expand="1") # pack mainWindow
            
   def initMenu(self):
      ''' create Menu for the application '''
      menubar = Menu(mainWindow)
      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="Import", command=self.appFunction.importer)
      filemenu.add_command(label="open DB", command=self.appFunction.opendDB)
      filemenu.add_separator()
      filemenu.add_command(label="Exit", command=mainWindow.quit)
      menubar.add_cascade(label="File", menu=filemenu)
      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Help Index", command=self.appFunction.openHelp)
      helpmenu.add_command(label="About...", command=self.appFunction.openAbout)
      menubar.add_cascade(label="Help", menu=helpmenu)
      mainWindow.config(menu=menubar)  
         
   def initRadioButton(self):
      ''' initial RadioButton for Canvas '''
      
      fButtons = Frame(main, border="2", relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bQuit.pack(side="right")
      
      R1 = Radiobutton(fButtons, text="Draw dot", variable=self.var, value=1
                       ,command=self.appFunction.getDrawList,indicatoron =0)
      R1.pack(side="right")
      R2 = Radiobutton(fButtons, text="Draw line", variable=self.var, value=2
                       ,command=self.appFunction.getDrawList,indicatoron =0)
      R2.pack(side="right")
      R3 = Radiobutton(fButtons, text="Draw linear regression", variable=self.var, value=3
                       ,command=self.appFunction.getDrawList,indicatoron =0)
      R3.pack(side="right")
      R4 = Radiobutton(fButtons, text="Draw curve", variable=self.var, value=4
                       ,command=self.appFunction.getDrawList,indicatoron =0)
      R4.pack(side="right")
      fButtons.pack(fill="x",expand="0",side="bottom") 



mainWindow=Tk() # Initial Tkinter
mainWindow.minsize(800,600) # minsize for mainWindow for less problem with resize
# -----------------------------------------------------------------
#---------------------------- Label
# -----------------------------------------------------------------
left = Label(mainWindow,width="35") # Label for the experiments and table
left.pack(side="left",fill="y",expand="0")
main = Label(mainWindow) # main Label for the canvas and buttons
main.pack(side="right",fill="both",expand="1")
# -----------------------------------------------------------------
#---------------------------- Start Application
# -----------------------------------------------------------------
app=NewtonApp(main,left) # create a application
app.initMenu() # create menu for the application
mainloop()