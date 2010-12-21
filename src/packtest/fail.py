from Tkinter import *

class Fail:
    def __init__(self,message):
        self.failWindow = Tk()
        err_message = Label(self.failWindow, text = message)
        err_button = Button (self.failWindow,text = "OK",command=self.failWindow.destroy)
        err_message.pack()
        err_button.pack()
        
    

        