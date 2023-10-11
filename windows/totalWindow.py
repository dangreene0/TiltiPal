from tools.worker import ThreadClass
from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox, QMainWindow, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import pyqtSignal


class totalWindow(QMainWindow):
    window_closed = pyqtSignal()
    def __init__(self):
        self.thread={}
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.thread[1] = ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.setWindowTitle("Current Total")
        self.setFixedSize(300,220)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.l4 = QLabel(self)
        self.l4.setGeometry(35,40 ,220,40)
        self.l4.setStyleSheet("border: 1px solid black; background: lightgrey; border-radius: 5px;")
        self.l4.setWordWrap(True)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.thread[1].message_sent[str].connect(self.updateLabel4)
      
        self.b4 = QPushButton(self)
        self.b4.setText("Stop Feed")
        self.b4.clicked.connect(self.stopFeed)
        self.b4.setGeometry(70,130, 150, 50)

    def updateLabel4(self, text):
        self.l4.setText(text)

    def stopFeed(self):
        self.thread[1].stop()
        self.close()

    def closeEvent(self, event):
        self.window_closed.emit()
        self.stopFeed()
        event.accept()