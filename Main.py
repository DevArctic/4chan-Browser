import requests
from PyQt5.QtWidgets import *

class WindowManager():
	def __init__(self):
		self.currentWindow = []
		self.previousWindow = []

	

class BoardsWindow(QWidget):

	def start(self):
		r = requests.get(url="https://a.4cdn.org/boards.json")
		self.data = r.json()
		self.boardStringList = []
		self.BUTTONH = 50
		self.BUTTONW = 100
		self.boardNum = len(self.data["boards"])
		for x in range(self.boardNum):
			self.boardStringList.append(self.data["boards"][x]["board"])
		self.createButtons()
		self.positionButtons()

	def positionButtons(self):
		tWidth = self.frameGeometry().width()
		col = tWidth // self.BUTTONW
		paddingTotal = tWidth % self.BUTTONW
		paddingLeft = paddingTotal // 2
		paddingTop = 25
		if (self.boardNum % col == 0):
			rows = self.boardNum // col
		else:
			rows = (self.boardNum // col) + 1
		posList = []
		for y in range(rows):
			for x in range(col):
				posList.append((((self.BUTTONW * x) + paddingLeft),((self.BUTTONH * y) + paddingTop)))
		for x in range(self.boardNum):
			self.buttons[x].move(posList[x][0],posList[x][1])


	def createButtons(self):
		self.buttons = []
		for each in self.boardStringList:
			self.buttons.append(QPushButton(each))
		for each in self.buttons:
			each.resize(self.BUTTONW,self.BUTTONH)
			each.setParent(self)
			each.clicked.connect(lambda state, each=each: self.buttonClick(each))

	def resizeEvent(self, e):
		self.positionButtons()		

	def buttonClick(self, buttonClicked):
		print (buttonClicked.text())

app = QApplication([])
window = BoardsWindow()
window.start()
window.show()
app.exec()