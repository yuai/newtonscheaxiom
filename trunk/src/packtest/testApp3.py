from Tkinter import *

class testApp3:
  def __init__( self, master ):
    self.ma = master
    self.f = Frame( self.ma )
    self.f.pack(fill=BOTH, expand=YES)
    self.cv = Canvas(self.f, width=125, height=125, bg='red')
    self.cv.pack(fill=BOTH, expand=YES)
    self.b1 = Button( self.f, text='Hello', height=1, width=10,padx=0, pady=1,command = self.howbig )
    self.b1.pack(side=BOTTOM, anchor=S, padx=4, pady=4)
    self.cv.bind('<Configure>', self.resize )

  def howbig( self ):
    print self.cv['width'], self.cv['height']
    print self.cvw, self.cvh

  def resize( self, event ):
    print '(%d, %d)' % (event.width, event.height)
    self.cvw, self.cvh = event.width-4, event.height-4

root = Tk()
app = testApp3(root)
root.mainloop()