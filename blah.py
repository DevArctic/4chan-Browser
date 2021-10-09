import requests
from PyQt5.QtWidgets import *

URL = "https://a.4cdn.org/boards.json"
r = requests.get(url=URL)
boardData = r.json()

app= QApplication([])

class Window(QWidget):

	def resizeEvent(self, e):
		positionBoardButtons()

window = Window()

numBoards = len(boardData["boards"])
bsizew = 100
bsizeh = 50
boardButtons = []

def createBoardButtons():
	for x in range(numBoards):
		boardButtons.append(QPushButton(boardData["boards"][x]["board"]))
	for each in boardButtons:
		each.resize(bsizew,bsizeh)
		each.setParent(window)

def positionBoardButtons():
	wWidth = window.frameGeometry().width()
	print (wWidth)
	col = wWidth // bsizew
	paddingTotal = wWidth % bsizew
	paddingLeft = paddingTotal // 2
	paddingTop = 25
	if (numBoards % col == 0):
		rows = numBoards // col
	else:
		rows = (numBoards // col) + 1
	posList = []
	for y in range(rows):
		for x in range(col):
			posList.append((((bsizew * x) + paddingLeft),((bsizeh * y) + paddingTop)))
	for x in range(numBoards):
		boardButtons[x].move(posList[x][0],posList[x][1])



createBoardButtons()
positionBoardButtons()

window.show()
app.exec()
