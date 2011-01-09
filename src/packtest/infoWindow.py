from Tkinter import *

'''
@author: Daniel Xander
@author: John Truong
'''

class Fail:
    '''Opens an Window with an Error information telling the user how to solve an problem.'''
    def __init__(self,message):
        self.failWindow = Tk()
        err_message = Label(self.failWindow, text = message)
        err_button = Button (self.failWindow,text = "OK",command=self.failWindow.destroy)
        err_message.pack()
        err_button.pack()
        
class Help:
    '''Opens an instructional window telling the user how to operate the application'''
    def __init__(self):
        helpWindow = Tk()
        help_title = Label(helpWindow, text="Help", font=("Helvetica", 16))
        help_message = Label(helpWindow, text = 
                                   "--- IMPORTER ---"
                             + "\n 1.0 Via Menu (File-Import) you can import .csv file with a specific format into the application"
                             + "\n"
                             + "\n--- OPEN SQLITE FILE ---"
                             + "\n 2.0 Via Menu (File-open DB) a new Window will be open and than you can choose by double click the experiments," 
                             + "\n       that you like to see on plot or table."
                             + "\n 2.1 Only 6 experiments can shown on same time."
                             + "\n 2.2 Experiment name can be cut if it is too long. max length of name 30 (but the hole name is on the listBox)"
                             + "\n"
                             + "\n--- SHOW TABLE ---"
                             + "\n 3.0 Show value on table by clicking the checkBoxes"
                             + "\n 3.1 ListBox show the hole experiment name (you can move horizontal)"
                             + "\n 3.2 Table are among one another"
                             + "\n 3.3 More than one indicator in one collection of data value can not be shown on table. (only metaData)"
                             + "\n"
                             + "\n--- SHOW PLOT ---"
                             + "\n 4.0 Show value on plot by clicking the checkBoxes and the button function (like draw_line) "
                             + "\n 4.1 ColorList for the plot and checkBoxes blue,red,green,yellow,pink,turquoise"
                             + "\n 4.2 More than one indicator can be shown on plot for example by different blue"
                             + "\n 4.3 Maximal 6 experiments can be shown on same time"
                             + "\n 4.4 After selected button function (like draw_line) you can change checkBoxes and update by"
                             + "\n       Button Update"
                             + "\n"
                             + "\n--- CLEAR EXPERIMENT ---"
                             + "\n 5.0 You can only delete all experiments by button clean all"
                             + "\n"
                             + "\n--- EXIT ---"
                             + "\n 6.0 Exit application by Button Quit"
                             , justify="left")
        help_button = Button(helpWindow, text = "OK", command=helpWindow.destroy)
        help_title.pack()
        help_message.pack()
        help_button.pack()
        
        
class About:
    '''Shows an Window with information about the application and the developers'''
    def __init__(self):
        aboutWindow = Tk()
        title = Label(aboutWindow, text="Newton\n--------------", font=("Helvetica", 16))
        title.pack()
        version = Label(aboutWindow, text="Version 1.0", font=("Helvetica", 12))
        version.pack()
        about_message = Label(aboutWindow, text = "06. Jan 2011\n\n This application is written"
                               + "\n by Daniel Xander and John Truong"
                               + "\n in a FHNW Project in the 3. Semester" 
                               + "\n\n on Python Version 2.7.1 and Tk Version 8.5"
                               + "\n\n email: \n daniel.xander@students.fhnw.ch \n john.truong@students.fhwnw.ch")
        about_button = Button(aboutWindow, text = "OK",command=aboutWindow.destroy)
        about_message.pack()
        about_button.pack()