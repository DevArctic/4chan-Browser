import requests
from PyQt5.QtWidgets import *

URL = "https://a.4cdn.org/boards.json"
r = requests.get(url=URL)
boardData = r.json()

app= QApplication([])

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
numBoards = len(boardData["boards"])

class BoardWindow(QWidget):

	def setButtons(self, buttons):
		self.buttons = buttons

	def resizeEvent(self, e):
		positionBoardButtons(self.buttons, self)

def buttonClick(stuff):
	print (stuff.text())	

def startBoardWindow():

	window = BoardWindow()
	boardStringList = []
	for x in range(numBoards):
		boardStringList.append(boardData["boards"][x]["board"])
	window.setButtons(createBoardButtons(boardStringList, window))
	positionBoardButtons(window.buttons, window)
	return window

def createBoardButtons(boardStringList, window):
	boardButtons = []
	for each in boardStringList:
		boardButtons.append(QPushButton(each))
	for each in boardButtons:
		each.resize(BUTTON_WIDTH,BUTTON_HEIGHT)
		each.setParent(window)
		each.clicked.connect(lambda state, each=each: buttonClick(each))
	return boardButtons

def positionBoardButtons(buttons, window):
	wWidth = window.frameGeometry().width()
	print (wWidth)
	col = wWidth // BUTTON_WIDTH
	paddingTotal = wWidth % BUTTON_WIDTH
	paddingLeft = paddingTotal // 2
	paddingTop = 25
	if (numBoards % col == 0):
		rows = numBoards // col
	else:
		rows = (numBoards // col) + 1
	posList = []
	for y in range(rows):
		for x in range(col):
			posList.append((((BUTTON_WIDTH * x) + paddingLeft),((BUTTON_HEIGHT * y) + paddingTop)))
	for x in range(numBoards):
		buttons[x].move(posList[x][0],posList[x][1])


window = startBoardWindow()
window.show()

app.exec()
