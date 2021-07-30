from windows.totalWindow import totalWindow
from tools.palUtilities import VERSION, readHistory
from tools.errorDefs import NoCampaignError, NoPreviousFileError
from windows.fileFetchWindow import fromFileWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QLabel, QPushButton, QDesktopWidget
import json
import os


class MainWindow(QMainWindow):
    # TODO seperate fucntions into utilities
    def __init__(self):
        # Initializeds stuff!
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        
        # Creates the window.
        self.setWindowTitle(f"TiltiPal {VERSION}")
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.setFixedSize(400, 290)
        #centers application
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        # Border image
        self.l1 = QLabel(self)
        borderImg = QtGui.QPixmap('img/title.png').scaled(400,110)
        self.l1.setPixmap(borderImg)
        self.l1.setGeometry(0,0,borderImg.width(),borderImg.height())
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        
        # Change Campaign Button
        self.b1 = QPushButton(self)
        self.b1.setText("Change Campaign")
        self.b1.clicked.connect(self.chooseFromFilesWindow)
        self.b1.setGeometry(10,105, 150, 50)
        # TODO fix geometry on these

        # Label for campaign history
        self.l2 = QLabel(self)
        self.l2.setGeometry(160,110 ,220,40)
        self.l2.setStyleSheet("border: 1px solid black; background: lightgrey; border-radius: 5px;")
        self.l2.setWordWrap(True)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleCheckFile()

        # button to change save file
        self.b2 = QPushButton(self)
        self.b2.setText("Change Save File")
        self.b2.clicked.connect(self.openFileNameDialog)
        self.b2.setGeometry(10,165, 150, 50)
        # TODO fix geometry on these

        # Label for current data file
        self.l3 = QLabel(self)
        self.l3.setGeometry(160,170 ,220,40)
        # TODO turn this into a function!!!
        with open("data/history.json") as f:
            data = json.load(f)
            filePath = data["previousFile"]
            fileName = os.path.basename(filePath)
            self.l3.setText(fileName)
        self.l3.setStyleSheet("border: 1px solid black; background: lightgrey; border-radius: 5px;")
        self.l3.setWordWrap(True)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)

        # start live feed Button
        self.b3 = QPushButton(self)
        self.b3.setText("Start Live Count")
        self.b3.clicked.connect(self.totalFeedWindow) 
        self.b3.setGeometry(110,225, 150, 50)
        # TODO fix geometry on these

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JSON Files (*.json)")
        if filePath:
            self.writeSelectedSaveFile(filePath)
            fileName = os.path.basename(filePath)
            self.l3.setText(fileName)
            self.chooseFromFilesWindow()

    # updates the save data file with the selection
    def writeSelectedSaveFile(self,fileName):
        with open("data/history.json") as f:
            data = json.load(f)
            data["previousFile"] = fileName

        with open('data/history.json', 'w') as f:
            json.dump(data, f, indent=2)
                
    def doubleCheckFile(self):
        try:
            previous, event = readHistory()
            if event:
                self.l2.setText(event)
        except json.decoder.JSONDecodeError:
            self.l2.setText("No Data Available/Empty File")
        except FileNotFoundError:
            self.l2.setText("Missing File")
        except NoCampaignError:
            self.l2.setText("No Previous Campaign")
        except NoPreviousFileError:
            self.l2.setText("No Campaign Data Available")
            
    def chooseFromFilesWindow(self):                                             # <===
        self.win = fromFileWindow()
        self.win.show()
        self.setDisabled(True)
        self.win.window_closed.connect(self.campaignSelectClose)

    def campaignSelectClose(self):
        self.setEnabled(True)
        self.doubleCheckFile()


    def totalFeedWindow(self):                                             # <===
        self.win = totalWindow()
        self.win.show()
        self.setDisabled(True)
        self.win.window_closed.connect(self.totalFeedClose)

    def totalFeedClose(self):
        self.setEnabled(True)
        self.doubleCheckFile()