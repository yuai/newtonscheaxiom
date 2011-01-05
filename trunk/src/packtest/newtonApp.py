from Tkinter import *
from expList import ExpList
from xyplot import XYPlot
from newtonImporter import NewtonImporter
from data_access import Experiment
from infoWindow import Fail
from infoWindow import About
from infoWindow import Help
import os # to get number of available experiments respectively databases
import tkFileDialog # to get the selected filename on local disk space 

'''
@author: Daniel Xander
@author: John Truong
'''    
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
      self.checkbuttonPlot = [] # save check button to change the color
      self.checkbuttonTable = [] # save checkbuttonTable to destroy it
      self.mainPath = 'db/' #All SqliLite Files are stored here
      self.namePath = 'db/test'#SQL data path with data name
      self.MAX_SHOWN_EXP = 6 # max experiment on the same time
      self.MAX_LEN_EXPNAME = 30 
      # max length for the overview of the selected experiment on the left side
      # (e.g. that_is_a_long_experimentname --> that_is_a_long_experimentnam...
      # not apply for the listBox
      
      file_count = len(os.listdir(self.mainPath))
      for i in range(0,file_count-1): # -1 nur fuer testzwecken
          nr = str(i) # number (increment) for the database filename
          self.explist.addExp(Experiment(self.namePath+nr+'.db',1))
      # -----------------------------------------------------------------   
      #---------------------------- XYPlot
      # -----------------------------------------------------------------
      self.mainWindow = Frame(main)
      self.xyPlot=XYPlot(main,800,600) # default size for canvas
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
      self.var = IntVar() # variable for the radioButton
      R1 = Radiobutton(fButtons, text="Draw dot", variable=self.var, value=1
                       ,command=self.getDrawList,indicatoron =0)
      R1.pack(side="right")
      R2 = Radiobutton(fButtons, text="Draw line", variable=self.var, value=2
                       ,command=self.getDrawList,indicatoron =0)
      R2.pack(side="right")
      R3 = Radiobutton(fButtons, text="Draw linear regression", variable=self.var, value=3
                       ,command=self.getDrawList,indicatoron =0)
      R3.pack(side="right")
      R4 = Radiobutton(fButtons, text="Draw curve", variable=self.var, value=4
                       ,command=self.getDrawList,indicatoron =0)
      R4.pack(side="right")
      fButtons.pack(fill="x",expand="0",side="bottom")
      # -----------------------------------------------------------------
      #---------------------------- Canvas
      # -----------------------------------------------------------------
      self.xyPlot.canvas.pack(fill="both", expand="1") # pack canvas after buttons for resize
      self.mainWindow.pack(fill="both",expand="1")
      
   def opendDB(self):
      ''' open new window with the experiments from DB in a ListBox'''
      filewin = Toplevel(mainWindow) # create a new Window
      scrollbar = Scrollbar(filewin) 
      scrollbar.pack( side="right", fill="y" )
      self.myDBlist = Listbox(filewin, yscrollcommand = scrollbar.set
                         , height=20,width=100, relief="sunken" ) # to use information on the listbox outside of this method
      scrollbar.config( command = self.myDBlist.yview )
      if self.explist.dbCount == 0 :
          msg = Message(filewin, text="No file in DB", width=100)
          msg.pack(side="top")
      
      for i in range(0,self.explist.dbCount): # get all meta information from all DB
          exp_metadata = self.explist.getMetaData(i)
          nr_series = exp_metadata['nr_series']
          exp_data = exp_metadata['date']
          actor_name = exp_metadata['actor_name']
          exp_name = exp_metadata['exp_name']
          exp_addinfo = exp_metadata['additional_info']
          self.myDBlist.insert(i, nr_series + ": " + exp_name + " |   " 
                        + actor_name + " |  " + exp_data + ", " + exp_addinfo)
      self.myDBlist.pack( side="top", fill="both", expand=1)
      self.myDBlist.bind('<Double-Button-1>', self.showExp) # event by double click on experiment
      
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
      helpmenu.add_command(label="Help Index", command=self.openHelp)
      helpmenu.add_command(label="About...", command=self.openAbout)
      menubar.add_cascade(label="Help", menu=helpmenu)
      mainWindow.config(menu=menubar)   
      
   def importer(self):
       ''' open new Window to select a .csv file to import into to the DB '''
       toplevel = Tk()
       toplevel.withdraw()
       filename = tkFileDialog.askopenfilename()
       filename = str(filename) # convert to string
       # problem with import .py file csv.Error do not resolve it. so we have to do like this
       if filename[len(filename)-3:len(filename)] == "csv":
           exp = NewtonImporter(filename,self.namePath,self.explist.dbCount)
           if exp.getExperiment()!= None:
               self.explist.addExp(exp.getExperiment())
       else:
           Fail( "You are trying to open an file which is  not \n compatible with this Programm.\n This Programm can only read Data in the .csv file Format")
       
   def sendDbCount(self):
       return self.explist.dbCount    
              
   def showExp(self,event):
       ''' show the specific added experiment on the left side of the user interface '''
       if (len(self.checkbuttonPlot)+1>self.MAX_SHOWN_EXP): # only
           Fail( "You are trying to show more than "+str(self.MAX_SHOWN_EXP)+" experiments which is  not \n compatible with this Programm.")
       else :
           index = self.myDBlist.curselection()
           i = int(index[0]) # convert tuple to integer
           self.explist.addIndexList(i)
           expNameActor = self.myDBlist.get(index) # expNameActor with experiment name and actor name
           expNameActorList = expNameActor.split('|') # split experiment name with actor name
           expName = expNameActorList[0] # show only experiment name
           # -----------------------------------------------------------------
           #---------------------------- CheckButton for experiment
           # -----------------------------------------------------------------
           CheckVarPlot = IntVar()
           CheckVarTable = IntVar()
           self.statesTable.append(CheckVarTable) # add to a list to know which is selected for show table
           self.statesPlot.append(CheckVarPlot) # add to a list to know which is selected for show on plot
           if (len(expName)>self.MAX_LEN_EXPNAME): # if experiment name is too long
               cutexpName = expName[0:self.MAX_LEN_EXPNAME] +"..." # cut experiment name
               expName = cutexpName
           c1 = Checkbutton(left, text="Plot["+expName+"]",variable=CheckVarPlot, anchor=NW, width="35")
           c2 = Checkbutton(left, text="Table["+expName+"]",variable=CheckVarTable
                                ,command=self.showTable,anchor=NW,width="35")
           self.checkbuttonPlot.append(c1) # add to a list to destroy by button "clean all" and to change color by selecting
           self.checkbuttonTable.append(c2) # add to a list to destroy by button "clean all"
           c1.pack(side="bottom")
           c2.pack(side="bottom")          
            
   def cleanAllExp(self):
       ''' clean all experiments on the application '''
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
       ''' update Plot after changing on checkBoxes '''
       self.getDrawList()
               
   def showTable(self): 
        ''' show values of the experiment in the list-box '''
        self.myTablelistbox.delete(0, END) # delete list-box, list-box will be always generated completely
        valueList = self.explist.getValueList()
        metaList = self.explist.getMetaList()
        for tempI in range(0,len(valueList)):
            if self.statesTable[tempI].get() == 1: # if argument is 0 do nothing
                # -----------------------------------------------------------------
                # -------------------------- Show Meta Data on List box
                # -----------------------------------------------------------------
                allmetaOfExp = metaList[tempI] # all meta data
                allMetaString = str(allmetaOfExp['additional_info']) # additional info like "Masse, Winkel"
                splitedString = allMetaString.split('|') 
                self.myTablelistbox.insert(NewtonApp.tablecount,"########################") # after this are meta data
                self.myTablelistbox.insert(NewtonApp.tablecount+1,'ID: '+allmetaOfExp['nr_series'])
                self.myTablelistbox.insert(NewtonApp.tablecount+2,'ExpName: '+allmetaOfExp['exp_name'])
                self.myTablelistbox.insert(NewtonApp.tablecount+3,'Actor: '+allmetaOfExp['actor_name'])
                self.myTablelistbox.insert(NewtonApp.tablecount+4,'Date: '+allmetaOfExp['date'])
                tempTablecount=NewtonApp.tablecount+5 #tempTablecount for the meta data
                for temp in range(0,len(splitedString)) : # add additional info
                    self.myTablelistbox.insert(tempTablecount, splitedString[temp])
                    tempTablecount=tempTablecount+1
                self.myTablelistbox.insert(tempTablecount+1,"-------------------------------") # end of meta data
                NewtonApp.tablecount = tempTablecount+2 # set the new tablecount plus the meta data
                # -----------------------------------------------------------------
                # -------------------------- Show Values on List box 
                # -----------------------------------------------------------------
                result = valueList[tempI]
                try:
                    x,y = zip(*result)
                    intC = 0 # increment to get the x and y
                    for C in x: # print all value respectively points of experiment
                        NewtonApp.tablecount = NewtonApp.tablecount+1
                        xyString =  "x[%s] \t= %f \t y[%s] \t= %f" % (str(intC), x[intC], str(intC),y[intC]) 
                        self.myTablelistbox.insert(NewtonApp.tablecount, xyString )
                        intC = intC + 1
                except ValueError:
                    Fail("Sorry, Table only can show one Y-Axis\n If you want to see all you have to split your csv File into \n one for every Y-Set")        
                   
   def getDrawList(self):
       ''' get values from the experiment '''
       valueList = []
       metaList = []
       tempI=0 # variable increment go thought the check-buttons
       tempSel=0 # variable increment by selected check-buttons for the color
       colorList = self.xyPlot.colorList
       for index in self.explist.indexList:
           if self.statesPlot[tempI].get() == 1: # selected checkBox for plot
               values = self.explist.getValues(index)
               metadata = self.explist.getMetaData(index)
               metaList.append(metadata)
               valueList.append(values)
               self.checkbuttonPlot[tempI].config(selectcolor=colorList[tempSel]) # change color
               tempSel=tempSel+1
           if self.statesPlot[tempI].get() == 0: # not selected checkBox for plot
               self.checkbuttonPlot[tempI].config(selectcolor="white") # default color is white of a checkBox
           tempI=tempI+1
       self.xyPlot.drawControl(valueList,metaList,self.var.get())  
       
   def initListBox(self):
       ''' initial the ListBox on the left side (for the table and experiments) '''
       scrollbar = Scrollbar(left)
       scrollbar.pack( side="right", fill="y")
       # -----------------------------------------------------------------
       #---------------------------- ListBox
       # -----------------------------------------------------------------
       myTablelist = Listbox(left, yscrollcommand = scrollbar.set, width="35")
       myTablelist.xview() # for long name
       myTablelist.pack( side="bottom", fill="both", expand="1")
       scrollbar.config( command = myTablelist.yview )
       self.myTablelistbox = myTablelist
       fButton = Frame(left, border="2", relief="groove")
       # clean all experiments
       bClean = Button(fButton, text="Clean all",command=self.cleanAllExp)
       bClean.pack(side="left")
       # update the changes for the plot
       bUpdate = Button(fButton, text="Update",command=self.updatePlot)
       bUpdate.pack(side="left")
       fButton.pack(fill="x",expand="0",side="bottom")
       
   def openAbout(self):
       ''' open new window for about information '''
       About()
       
   def openHelp(self):
       ''' open new window for help information '''
       Help()
# -----------------------------------------------------------------  
#---------------------------- Initial Tkinter
# -----------------------------------------------------------------
mainWindow=Tk()
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
app.createMenu() # create menu for the application
mainloop()