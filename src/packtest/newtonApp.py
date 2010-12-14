from Tkinter import *
from xyplot import *
from newtonImporter import NewtonImporter
from data_access import Experiment
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class NewtonApp:
    
   dbCount=0
   extable = []
   def __init__(self, parent=0):
      #---------------------------- XYPlot
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,400,250)
      #---------------------------- Scrollbar
      scrollbar = Scrollbar(left)
      scrollbar.pack( side="right", fill="y" )
      #---------------------------- ListBox
      myTablelist = Listbox(left, yscrollcommand = scrollbar.set,width = 30 )
      #for line in range(10):
      #     mylist.insert(END, "This is line number " + str(line))
      myTablelist.pack( side="bottom", fill="both", expand=1)
      scrollbar.config( command = myTablelist.yview )
      self.myTablelistbox = myTablelist
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
      myDBlist = Listbox(filewin, yscrollcommand = scrollbar.set, height=20,width=50, relief=SUNKEN )
      scrollbar.config( command = myDBlist.yview )
      count=0
      for x in NewtonApp.extable:
          #print NewtonApp.extable[count].load_metadata()
          exp_metadata = NewtonApp.extable[count].load_metadata()
          nr_series = exp_metadata['nr_series']
          actor_name = exp_metadata['actor_name']
          exp_name = exp_metadata['exp_name']
          
          myDBlist.insert(count, nr_series + ": " 
                        + actor_name + " " + exp_name)
          count=count+1
      myDBlist.pack( side="top", fill="both", expand=1)
      myDBlist.bind('<Double-Button-1>', self.showExp)
      self.myDBlistbox = myDBlist
      
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
       
       stringI = str(NewtonApp.dbCount)
       NewtonApp.extable.append(Experiment('C:/Users/John Truong/Desktop/db/test'+stringI+'.db',1))
       toplevel = Tk()
       toplevel.withdraw()
       filename = tkFileDialog.askopenfilename()
       test=NewtonImporter(filename,NewtonApp.extable[NewtonApp.dbCount])
       NewtonApp.dbCount=NewtonApp.dbCount+1
   
   def showExp(self,event):
       index = self.myDBlistbox.curselection()
       expName = self.myDBlistbox.get(index)
       var = StringVar()
       var.set(expName)
       CheckVar1 = IntVar()
       CheckVar2 = IntVar()
       C1 = Checkbutton(left, text = expName, variable = CheckVar1,command = self.showOnCanvas, anchor=NW)
       c2 = Checkbutton(left, text = "table", variable = CheckVar2,command = self.showTable, width = 30, anchor=NW)
       C1.pack(side="top")
       c2.pack(side="top")
       
   def showOnCanvas(self):
        print "showOnCanvas"

   def showTable(self):
        print "showTable"
        #result = NewtonApp.exp.load_values(1) #fragen
        print result
        for line in range(10):
           self.myTablelistbox.insert(END, "This is line number " + str(line))
        #count=0
        #for x in NewtonApp.extable:
        #    print NewtonApp.extable[count].load_metadata()
        #    exp_metadata = NewtonApp.extable[count].load_metadata()
        #    nr_series = exp_metadata['nr_series']
        #    actor_name = exp_metadata['actor_name']
        #    exp_name = exp_metadata['exp_name']
          
        #    mylist.insert(count)
        #    count=count+1
        #mylist.pack( side="top", fill="both", expand=1)
        #mylist.bind('<Double-Button-1>', self.showExp)
       
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