from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameIput=Entry(self)
		self.nameIput.pack()
		self.alertButton=Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	
	def hello(self):
		name=self.nameIput.get() or 'World'
		messagebox.showinfo('Message','Hello, %s'%name)
app=Application()
app.master.title('Hello World')
app.mainloop()