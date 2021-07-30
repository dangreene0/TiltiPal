from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtWidgets import QGridLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import pyqtSignal
import sys
import requests
import json
import time


class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None,index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
        self.is_running = True
        
    def run(self):
        duration = 1
        with open("data/history.json") as h:
            historyData = json.load(h)
            event = historyData["lastEvent"]
            while True:
                with open('data/data.json') as f:
                    time.sleep(duration)
                    data = json.load(f)
                    info = data[event]
                    for entry in info:
                        eventCode = entry["event-code"]
                        userCode = entry["user"]
                    print(eventCode,userCode)
                    urlGen = f"https://tiltify.com/api/v3/users/{userCode}/campaigns/{eventCode}"
                    response = requests.get(urlGen)
                    tiltifyData = json.loads(response.text)
                    total = tiltifyData["data"]["totalAmountRaised"]
                    print(total)

    def stop(self):
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()