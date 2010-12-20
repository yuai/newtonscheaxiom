from Tkinter import *
from expList import ExpList
from xyplot import XYPlot
from newtonImporter import NewtonImporter
from data_access import Experiment
import os
import tkFileDialog
import csv
    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class NewtonApp:
   # -----------------------------------------------------------------
   # ---------------------------- variables of class NewtonApp
   # -----------------------------------------------------------------
   ''' set tablecount. increment to show more tables in the list-box '''
   tablecount = 0
   
   def __init__(self, parent=0,left=0):
      ''' constructor '''
      
      self.explist = ExpList()
      self.statesPlot = [] # states of plot of the check-buttons
      self.statesTable = [] # states of table of the check buttons
      self.checkbuttonPlot = [] # save check button (for the plot) to change the color
      self.checkbuttonTable = [] # save checkbuttonTable to destroy it
      
      file_count = len(os.listdir('C:/Users/db/'))
      for i in range(0,file_count):
          nr = str(i) # number (increment) for the database filename
          self.explist.addExp(Experiment('C:/Users/db/test'+nr+'.db',1))
      # -----------------------------------------------------------------   
      #---------------------------- XYPlot
      # -----------------------------------------------------------------
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,400,250)
      # -----------------------------------------------------------------
      #---------------------------- ScrollBar, ListBox
      # -----------------------------------------------------------------
      self.initListBox()
      # -----------------------------------------------------------------
      # ---------------------------- Buttons for Canvas
      # -----------------------------------------------------------------
      fButtons = Frame(main, border="2", relief="groove")
      bQuit = Button(fButtons, text="Quit",command=self.mainWindow.quit)
      bQuit.pack(side="right")
      # -----------------------------------------------------------------
      #---------------------------- RadioButton
      # -----------------------------------------------------------------
      self.var = IntVar()
      R1 = Radiobutton(fButtons, text="Draw Dot", variable=self.var, value=1
                       ,command=self.getDrawList,indicatoron =0)
      R1.pack(side="right")
      R2 = Radiobutton(fButtons, text="Draw Line", variable=self.var, value=2
                       ,command=self.getDrawList,indicatoron =0)
      R2.pack(side="right")
      R3 = Radiobutton(fButtons, text="Approximate Line", variable=self.var, value=3
                       ,command=self.getDrawList,indicatoron =0)
      R3.pack(side="right")
      R4 = Radiobutton(fButtons, text="Draw Spline", variable=self.var, value=4
                       ,command=self.getDrawList,indicatoron =0)
      R4.pack(side="right")
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
      for x in range(0,self.explist.dbCount):
          exp_metadata = self.explist.getMetaData(tempCount)
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
       stringI = str(self.explist.dbCount)
       self.explist.addExp(Experiment('C:/Users/db/test'+stringI+'.db',1))
       toplevel = Tk()
       toplevel.withdraw()
       filename = tkFileDialog.askopenfilename()
       NewtonImporter(filename,self.explist.getExp(self.explist.dbCount-1))
       
       
   def showExp(self,event):
       ''' show the specific added experience on the left side of the user interface '''
       index = self.myDBlistbox.curselection()
       i = int(index[0]) # convert tuple to integer
       self.explist.addIndexList(i)
       expName = self.myDBlistbox.get(index)
       # -----------------------------------------------------------------
       #---------------------------- CheckButton for experience
       # -----------------------------------------------------------------
       CheckVarPlot = IntVar()
       CheckVarTable = IntVar()
       c1 = Checkbutton(left, text="Plot["+expName+"]",variable=CheckVarPlot, anchor=NW, width="35")
       c2 = Checkbutton(left, text="Table["+expName+"]",variable=CheckVarTable
                        ,command=self.showTable,anchor=NW,width="35")
       self.statesTable.append(CheckVarTable)
       self.statesPlot.append(CheckVarPlot)
       self.checkbuttonPlot.append(c1)
       self.checkbuttonTable.append(c2)
       c1.pack(side="top")
       c2.pack(side="top")
   
   def cleanAllExp(self):
       self.var.set(0) # reset radio button
       self.statesTable = []
       self.statesPlot = []
       NewtonApp.tablecount = 0
       self.myTablelistbox.delete(0, END)
       for i in range(0, len(self.checkbuttonPlot)):
           self.checkbuttonPlot[i].destroy()
       for i in range(0, len(self.checkbuttonTable)):
           self.checkbuttonTable[i].destroy()
           
       self.checkbuttonPlot = []
       self.checkbuttonTable = []
       self.explist.resetIndexList()
   
   def updatePlot(self):
       self.getDrawList()
               
   def showTable(self): 
        ''' show values of the experience in the list-box '''
        self.myTablelistbox.delete(0, END) # delete list-box, list-box will be always generated completely
        valueList = self.explist.getValueList()
        metaList = self.explist.getMetaList() 
        for tempI in range(0,len(valueList)):
            if self.statesTable[tempI].get() == 1: # if argument is 0 do nothing
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
       metaList = []
       tempI=0 # variable increment go thought the check-buttons
       tempSel=0 # variable increment by selected check-buttons for the color
       colorList = ['RoyalBlue','DarkOliveGreen','IndianRed', 'brown',
                    'LightPink','PaleVioletRed','khaki']
       for index in self.explist.indexList:
           if self.statesPlot[tempI].get() == 1:
               values = self.explist.getValues(index)
               metadata = self.explist.getMetaData(index)
               metaList.append(metadata)
               valueList.append(values)
               self.checkbuttonPlot[tempI].config(selectcolor=colorList[tempSel])
               tempSel=tempSel+1
           if self.statesPlot[tempI].get() == 0:
               self.checkbuttonPlot[tempI].config(selectcolor="white")    
           tempI=tempI+1
       self.xyPlot.drawControl(valueList,metaList,self.var.get())  
       
   def initListBox(self):
       scrollbar = Scrollbar(left)
       scrollbar.pack( side="right", fill="y")
       # -----------------------------------------------------------------
       #---------------------------- ListBox
       # -----------------------------------------------------------------
       myTablelist = Listbox(left, yscrollcommand = scrollbar.set, width="35")
       myTablelist.pack( side="bottom", fill="both", expand="1")
       scrollbar.config( command = myTablelist.yview )
       self.myTablelistbox = myTablelist
       fButton = Frame(left, border="2", relief="groove")
       bClean = Button(fButton, text="Clean all",command=self.cleanAllExp)
       bClean.pack(side="left")
       bUpdate = Button(fButton, text="Update",command=self.updatePlot)
       bUpdate.pack(side="left")
       fButton.pack(fill="x",expand="0",side="top")

# -----------------------------------------------------------------  
#---------------------------- Initial Tkinter
# -----------------------------------------------------------------
mainWindow=Tk()
mainWindow.minsize(800,600)
# -----------------------------------------------------------------
#---------------------------- Label
# -----------------------------------------------------------------
left = Label(mainWindow,width="35")
left.pack(side="left",fill="y",expand="0")
main = Label(mainWindow)
main.pack(side="right",fill="both",expand="1")
# -----------------------------------------------------------------
#---------------------------- Start Application
# -----------------------------------------------------------------
app=NewtonApp(main,left)
app.createMenu()
mainloop()