from Tkinter import *
from xyplot import *
from newtonImporter import NewtonImporter
from data_access import Experiment
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class NewtonApp:
    
   dbCount=1
   def __init__(self, parent=0):
      #------------------------------ Checkbox
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
      #---------------------------- XYPlot
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,400,250)
      #---------------------------- Scrollbar
      scrollbar = Scrollbar(left)
      scrollbar.pack( side="right", fill="y" )
      #---------------------------- ListBox
      mylist = Listbox(left, yscrollcommand = scrollbar.set )
      for line in range(100):
           mylist.insert(END, "This is line number " + str(line))
      mylist.pack( side="top", fill="both", expand=1)
      scrollbar.config( command = mylist.yview )
      #---------------------------- Buttons
      fButtons = Frame(main, border=2, relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bQuit.pack(side="right")
      #---------------------------- Radiobutton
      var = IntVar()
      R1 = Radiobutton(fButtons, text="Draw Rectangle", variable=var, value=1
                       ,command=self.xyPlot.drawRectangle,indicatoron =0)
      R1.pack(side="right")
      R2 = Radiobutton(fButtons, text="Draw Data", variable=var, value=2
                       ,command=self.xyPlot.plotSampleData,indicatoron =0)
      R2.pack(side="right")
      R3 = Radiobutton(fButtons, text="Draw Dot", variable=var, value=3
                       ,command=self.xyPlot.plotSampleData,indicatoron =0)
      R3.pack(side="right")
      R4 = Radiobutton(fButtons, text="Draw Line", variable=var, value=4
                       ,command=self.xyPlot.plotSampleData,indicatoron =0)
      R4.pack(side="right")
      R5 = Radiobutton(fButtons, text="Approximate Line", variable=var, value=5
                       ,command=self.xyPlot.transAxis(5.0,5.0,10.0,10.0),indicatoron =0)
      R5.pack(side="right")
      fButtons.pack(fill=X,expand="0",side="bottom")
      #---------------------------- Canvas
      self.xyPlot.canvas.pack(fill="both", expand="1")
      self.mainWindow.pack(fill="both",expand="1")
      
   def opendDB(self):
      ''' open new window with the experiences from DB '''
      filewin = Toplevel(mainWindow)
      scrollbar = Scrollbar(filewin)
      scrollbar.pack( side="right", fill="y" )
      mylist = Listbox(filewin, yscrollcommand = scrollbar.set, height=20 )
      exp_metadata = self.e.load_metadata()
      test1 = self.e.load_values(1)
      test2 = self.e.load_values(2)
      print test1
      print test2
        
      nr_series = exp_metadata['nr_series']
      actor_name = exp_metadata['actor_name']
      exp_name = exp_metadata['exp_name']
      
      for line in range(100):
          mylist.insert(END, nr_series + ": " 
                        + actor_name + " " + exp_name)   
      mylist.pack( side="top", fill="both", expand=1)
      scrollbar.config( command = mylist.yview )
      mylist.bind('<Double-Button-1>', self.xyPlot.test)
   
   def createMenu(self):
      ''' create Menu for the application '''
      menubar = Menu(mainWindow)
      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="Import", command=self.importer)
      filemenu.add_command(label="open DB", command=self.opendDB)
      filemenu.add_separator()
      filemenu.add_command(label="Exit", command=mainWindow.quit)
      menubar.add_cascade(label="File", menu=filemenu)
      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Help Index")
      helpmenu.add_command(label="About...")
      menubar.add_cascade(label="Help", menu=helpmenu)
      mainWindow.config(menu=menubar)   
      
   def importer(self):
       ''' open new Window to select a .csv file to import into to the DB '''
       import os
       from Tkinter import Tk
       import tkFileDialog
       
       self.extable = []
       stringI = str(NewtonApp.dbCount)
       self.extable.append(Experiment('C:/Users/John Truong/Desktop/db/test'+stringI+'.db',1))
       NewtonApp.dbCount=NewtonApp.dbCount+1 
       toplevel = Tk()
       toplevel.withdraw()
       filename = tkFileDialog.askopenfilename()
       test=NewtonImporter(filename,self.extable[0])
       print self.extable[0].load_metadata()

#---------------------------- Initial Tkinter
mainWindow=Tk()
mainWindow.minsize(800,600)
#---------------------------- PanedWindow
m1 = PanedWindow(orient=VERTICAL)
m1.pack(fill="both", expand=1)
m2 = PanedWindow(m1)
left = Label(m2)
m2.add(left)
main = Label(m2)
m2.add(main) 
m1.add(m2)
#---------------------------- Start Application
app=NewtonApp(main)
app.createMenu()
mainWindow.mainloop()