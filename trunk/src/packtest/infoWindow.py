from Tkinter import *

class Fail:
    def __init__(self,message):
        self.failWindow = Tk()
        err_message = Label(self.failWindow, text = message)
        err_button = Button (self.failWindow,text = "OK",command=self.failWindow.destroy)
        err_message.pack()
        err_button.pack()
        
class Help:
    def __init__(self):
        helpWindow = Tk()
        title = Label(helpWindow, text="Help", font=("Helvetica", 16))
        help_message = Label(helpWindow, text = "1. Via Menu (File-Import) you can import .csv file with a specific format into the application"
                             + "2. Via Menu (File-open DB) a new Window will be open and than you can choose by double click the experiments, that you like to see on plot"
                             + "3. ")
        help_button = Button(helpWindow, text = "OK", command=helpWindow.destroy)
        help_message.pack()
        help_button.pack()
        
        
class About:
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