from Tkinter import *
import tkMessageBox

class MyWindow:
	def __init__(self, myParent):
		self.myContainer = Frame(myParent)
		self.myContainer.grid() 
		self.makeLayout()

	def makeLayout(self):
		self.label = Label(self.myContainer, text='This is a label')
		self.label.grid(row=1, column=1)

		self.listbox = Listbox(self.myContainer, font=('Helvetica', 12), fg='blue', height=3)
		self.listbox.grid(row=1, rowspan=2, column=2, columnspan=1, sticky=N)
		self.fillList()

		self.button = Button(self.myContainer, text='Show Message', width=12, height=1, 
			command=lambda: self.showMessage() )
		self.button.grid(row=2, column=1, sticky=W, padx=10, pady=10)

	def fillList(self):
		self.listbox.delete(0, END)
		for i in range(1, 4):
			text = "item %d" % i 
			self.listbox.insert(END, text)

	def showMessage(self):
		tkMessageBox.showinfo('Message', "Hello world!")

root = Tk()
root.geometry('300x200+150+40')
window = MyWindow(root)
root.title('Our Window')
root.mainloop()
