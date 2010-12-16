from Tkinter import *
from xyplot import *
from newtonImporter import NewtonImporter
from data_access import Experiment
import os
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class NewtonApp:
   # -----------------------------------------------------------------
   # ---------------------------- variables of class NewtonApp
   # -----------------------------------------------------------------
   ''' Amount of Databases or experiments '''  
   dbCount=0
   ''' List for experiments '''
   extable = []
   ''' List for added experiments '''
   indexList = []
   ''' states of table of the check-buttons '''
   statesTable = []
   ''' states of plot of the check-buttons '''
   statesPlot = []
   ''' set tablecount. increment to show more tables in the list-box '''
   tablecount = 0
   ''' save the check button (for the plot) to change the color ''' 
   checkbuttonPlot = []
   
   def __init__(self, parent=0):
      ''' constructor '''
      file_count = len(os.listdir('C:/Users/db/'))
      for i in range(0,file_count):
          nr = str(i) # number (increment) for the database filename
          NewtonApp.extable.append(Experiment('C:/Users/db/test'+nr+'.db',1))
          NewtonApp.dbCount=NewtonApp.dbCount+1
      # -----------------------------------------------------------------   
      #---------------------------- XYPlot
      # -----------------------------------------------------------------
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,400,250)
      # -----------------------------------------------------------------
      #---------------------------- ScrollBar
      # -----------------------------------------------------------------
      scrollbar = Scrollbar(left)
      scrollbar.pack( side="right", fill="y")
      # -----------------------------------------------------------------
      #---------------------------- ListBox
      # -----------------------------------------------------------------
      myTablelist = Listbox(left, yscrollcommand = scrollbar.set, width=30)
      myTablelist.pack( side="bottom", fill="both", expand="1")
      scrollbar.config( command = myTablelist.yview )
      self.myTablelistbox = myTablelist
      
      fButton = Frame(left, border="2", relief="groove")
      bClean = Button(fButton, text="Clean all",command=self.mainWindow.quit)
      bClean.pack(side="left")
      fButton.pack(fill="x",expand="0",side="top")
      # -----------------------------------------------------------------
      # ---------------------------- Buttons for Canvas
      # -----------------------------------------------------------------
      fButtons = Frame(main, border="2", relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bQuit.pack(side="right")
      # -----------------------------------------------------------------
      #---------------------------- RadioButton
      # -----------------------------------------------------------------
      var = IntVar()
      R1 = Radiobutton(fButtons, text="Draw Rectangle", variable=var, value=1
                       ,command=self.xyPlot.drawRectangle,indicatoron =0)
      R1.pack(side="right")
      R2 = Radiobutton(fButtons, text="Draw Data", variable=var, value=2
                       ,command=self.xyPlot.plotSampleData,indicatoron =0)
      R2.pack(side="right")
      R3 = Radiobutton(fButtons, text="Draw Dot", variable=var, value=3
                       ,command=self.getDrawList,indicatoron =0)
      R3.pack(side="right")
      R4 = Radiobutton(fButtons, text="Draw Line", variable=var, value=4
                       ,command=self.xyPlot.plotSampleData,indicatoron =0)
      R4.pack(side="right")
      R5 = Radiobutton(fButtons, text="Approximate Line", variable=var, value=5
                       ,command=self.xyPlot.transAxis(5.0,5.0,10.0,10.0),indicatoron =0)
      R5.pack(side="right")
      fButtons.pack(fill="x",expand="0",side="bottom")
      # -----------------------------------------------------------------
      #---------------------------- Canvas
      # -----------------------------------------------------------------
      self.xyPlot.canvas.pack(fill="both", expand="1")
      self.mainWindow.pack(fill="both",expand="1")
      
   def opendDB(self):
      ''' open new window with the experiences from DB '''
      filewin = Toplevel(mainWindow)
      scrollbar = Scrollbar(filewin)
      scrollbar.pack( side="right", fill="y" )
      myDBlist = Listbox(filewin, yscrollcommand = scrollbar.set, height=20,width=50, relief="sunken" )
      scrollbar.config( command = myDBlist.yview )
      tempCount=0 # increment to load all metaData of the experiences
      for x in NewtonApp.extable:
          exp_metadata = NewtonApp.extable[tempCount].load_metadata()
          nr_series = exp_metadata['nr_series']
          actor_name = exp_metadata['actor_name']
          exp_name = exp_metadata['exp_name']
          myDBlist.insert(tempCount, nr_series + ": " 
                        + actor_name + " " + exp_name)
          tempCount=tempCount+1
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
       NewtonApp.extable.append(Experiment('C:/Users/db/test'+stringI+'.db',1))
       toplevel = Tk()
       toplevel.withdraw()
       filename = tkFileDialog.askopenfilename()
       test=NewtonImporter(filename,NewtonApp.extable[NewtonApp.dbCount])
       NewtonApp.dbCount=NewtonApp.dbCount+1
   
   def showExp(self,event):
       ''' show the specific added experience on the left side of the user interface '''
       index = self.myDBlistbox.curselection()
       i = int(index[0]) # convert tuple to integer
       NewtonApp.indexList.append(i) # add all added experience into indexList[]
       expName = self.myDBlistbox.get(index)
       # -----------------------------------------------------------------
       #---------------------------- CheckButton for experience
       # -----------------------------------------------------------------
       self.CheckVarPlot = IntVar()
       self.CheckVarTable = IntVar()
       c1 = Checkbutton(left, text="Plot["+expName+"]",variable=self.CheckVarPlot,anchor=NW,width=30)
       c2 = Checkbutton(left, text="Table["+expName+"]",variable=self.CheckVarTable
                        ,command=self.showTable,anchor=NW,width=30)
       NewtonApp.statesTable.append(self.CheckVarTable)
       NewtonApp.statesPlot.append(self.CheckVarPlot)
       NewtonApp.checkbuttonPlot.append(c1)
       c1.pack(side="top")
       c2.pack(side="top")

   def showTable(self): 
        ''' show values of the experience in the list-box '''
        self.myTablelistbox.delete(0, END) # delete list-box, list-box will be always generated completely
        valueList = []
        for pin in NewtonApp.indexList:
            values = NewtonApp.extable[pin].load_values(1)
            valueList.append(values)
        metaList = []
        for pin in NewtonApp.indexList:
            metas = NewtonApp.extable[pin].load_metadata()
            metaList.append(metas) 
        for tempI in range(0,len(valueList)):
            if NewtonApp.statesTable[tempI].get() == 1: # if argument is 0 do nothing
                # -----------------------------------------------------------------
                # -------------------------- Show Meta Data on List box
                # -----------------------------------------------------------------
                allmetaOfExp = metaList[tempI]
                allMetaString = str(allmetaOfExp['additional_info'])
                splitedString = allMetaString.split('|')            
                self.myTablelistbox.insert(NewtonApp.tablecount,"########################")
                self.myTablelistbox.insert(NewtonApp.tablecount+1,'Name: '+allmetaOfExp['exp_name'])
                tempTablecount=NewtonApp.tablecount+2 #tempTablecount for the meta data
                for temp in range(0,len(splitedString)) :
                    self.myTablelistbox.insert(tempTablecount, splitedString[temp])
                    tempTablecount=tempTablecount+1
                self.myTablelistbox.insert(tempTablecount+1,"-------------------------------")
                NewtonApp.tablecount = tempTablecount+2 # set the new tablecount plus the meta data
                # -----------------------------------------------------------------
                # -------------------------- Show Values on List box 
                # -----------------------------------------------------------------
                result = valueList[tempI]
                x,y = zip(*result)
                intC = 0 # increment to get the x and y
                for C in x:
                    NewtonApp.tablecount = NewtonApp.tablecount+1
                    xyString =  "x[%s] \t= %f \t y[%s] \t= %f" % (str(intC), x[intC], str(intC),y[intC]) 
                    self.myTablelistbox.insert(NewtonApp.tablecount, xyString )
                    intC = intC + 1
       
   def getDrawList(self):
       ''' get values from the experience '''
       valueList = []
       tempI=0 # variable increment go thought the check-buttons
       tempSel=0 # variable increment by selected check-buttons for the color
       colorList = ['RoyalBlue','DarkOliveGreen','IndianRed', 'brown',
                    'LightPink','PaleVioletRed','khaki']
       for x in NewtonApp.indexList:
           if NewtonApp.statesPlot[tempI].get() == 1:
               values = NewtonApp.extable[x].load_values(1)
               valueList.append(values)
               NewtonApp.checkbuttonPlot[tempI].config(selectcolor=colorList[tempSel])
               tempSel=tempSel+1
           if NewtonApp.statesPlot[tempI].get() == 0:
               NewtonApp.checkbuttonPlot[tempI].config(selectcolor="white")    
           tempI=tempI+1
       self.xyPlot.drawControl(valueList,1)

# -----------------------------------------------------------------  
#---------------------------- Initial Tkinter
# -----------------------------------------------------------------
mainWindow=Tk()
mainWindow.minsize(800,600)
# -----------------------------------------------------------------
#---------------------------- PanedWindow
# -----------------------------------------------------------------
m1 = PanedWindow(orient="vertical")
m1.pack(fill="both", expand="1")
m2 = PanedWindow(m1)
left = Label(m2)
m2.add(left)
main = Label(m2)
m2.add(main) 
m1.add(m2)
# -----------------------------------------------------------------
#---------------------------- Start Application
# -----------------------------------------------------------------
app=NewtonApp(main)
app.createMenu()
mainWindow.mainloop()