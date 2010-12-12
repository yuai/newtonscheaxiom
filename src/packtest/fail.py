from Tkinter import *

class Fail:
    def _init_(self,message):
        failWindow = Tk()
        err_message = Label(failWindow, text = message)
        err_button = Button (failWindow,text = "OK",command=self.failWindow.quit)

        