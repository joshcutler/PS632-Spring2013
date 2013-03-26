# Tic-Tac-Toe Board for 2 human players

from Tkinter import *
import tkMessageBox

class MyWindow:
	def __init__(self, myParent):
		self.myContainer = Frame(myParent)
		self.myContainer.grid() 
		self.filled = [ [False]*3, [False]*3, [False]*3 ]
		self.currentPlayer = 1
		self.makeLayout()

	def makeLayout(self):
		self.label = Label(self.myContainer, text="Player 1's turn")
		self.label.grid(row=1, column=0, columnspan=3)

		self.buttons = {}
		for r in range(3):
			for c in range(3):
				buttonNum = r*10 + c 
				self.buttons[buttonNum] = Button(self.myContainer, text='', 
					width=1, height=1, command=lambda x=buttonNum: self.onClick(x) )
				self.buttons[buttonNum].grid(row=r+2, column=c)

	def onClick(self, x):
		r = x/10
		c = x % 10 
		print x, r, c, self.filled[r][c]
		if not self.filled[r][c]:
			if self.currentPlayer==1:
				self.buttons[x]["text"] = 'X'
				self.currentPlayer=2 
				self.label["text"] = "Player 2's turn"
			else: 
				self.buttons[x]["text"] = 'O'
				self.currentPlayer=1 
				self.label["text"] = "Player 1's turn"
			self.filled[r][c] = True 

	# TODO:
	# write checkWin() to see whether a player has won; if so alert them in a message & start new game
	# write allFilled() to see whethre the "cat" has won; alert & start new game

root = Tk()
root.geometry('300x200+150+40')
window = MyWindow(root)
root.title('Tic-Tac-Toe')
root.mainloop()