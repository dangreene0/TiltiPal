from PyQt5.QtWidgets import QComboBox, QMainWindow, QDesktopWidget
from PyQt5.QtCore import pyqtSignal
import json


class fromFileWindow(QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Please choose a campaign")
        self.setFixedSize(280, 40)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        # TODO move this json reading function to it's own file
    
        self.combo = QComboBox(self)
        self.combo.setGeometry(0,0,280,40)
        with open("data/history.json") as f:
            data = json.load(f)
            file = data["previousFile"]
        with open(file) as f:
            data = json.load(f)
            campaignList = []
            
            for campaign in data:
                campaignList.append(campaign)
                self.combo.addItem(campaign)

    # updates the history file with the selection
    def writeSelectedEvent(self):
        with open("data/history.json") as f:
            data = json.load(f)
            newEvent = self.combo.currentText()
            data["lastEvent"] = newEvent

        with open('data/history.json', 'w') as f:
            json.dump(data, f, indent=2)

    def closeEvent(self, event):
        self.writeSelectedEvent()
        self.window_closed.emit()
        event.accept()