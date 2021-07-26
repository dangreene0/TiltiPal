from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QSound

import sys


class MyWindow(QMainWindow):
    
    def __init__(self):
        # Initializeds stuff!
        self.thread={}
        super(MyWindow,self).__init__()
        self.initUI()

    def initUI(self):
        
        # Creates the window.
        self.setWindowTitle("Fart Prank 9000")
        
        # Creates a label.
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Let the stink commence!")
        self.label.setStyleSheet("border: 1px solid black; background: pink;") 
        self.label.setGeometry(65, 20, 170, 40)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # Creates a button.
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click to begin dookie.")
        self.b1.clicked.connect(self.begin_scan)
        self.b1.setGeometry(50, 70, 200, 40)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Test your fate.")
        self.b2.clicked.connect(self.pause_scan)
        self.b2.setGeometry(50, 110, 200, 40)
        self.b2.setDisabled(True)
        self.detectPort()
    
    def detectPort(self):

        ports = serial.tools.list_ports.comports()
        n = 0
        for port in ports:
           print(str(ports[n]))
           n += 1 
            
        if ports:
            print("Ports Found!")
            while "NOPORTFOUND" in arduino.port:
                time.sleep(3)
                portName()
                print(arduino.port)
                if arduino.port != "NOPORTFOUND":
                    arduino.open
                self.b1.setDisabled(True)
                print("No Arduino Found!")
                self.b1.setText("No Arduino Detected")
                self.b1.setText("No Arduino Detected")
                self.b1.setText("No Arduino Detected")
                
                # TODO Create refresh button
            else:
                self.b1.setDisabled(False)
                self.b1.setText("Click to begin dookie.")
                print("Arduino Detected")
        elif not ports:
            self.label = QtWidgets.QLabel(self)
            self.label.setText("--No ports found!--")
            self.label.setGeometry(65, 150, 170, 20)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setFixedSize(300, 170)

    def begin_scan(self):
        self.thread[1] = ThreadClass(parent=None,index=1)
        self.thread[1].start()
        self.b1.setText("There's no going back now!")
        self.b2.setText("Click to end dookie scan.")
        self.b1.setEnabled(False)
        self.b2.setEnabled(True)
        try: 
            self.thread[1].any_signal.connect(self.init_scan)
        except:
            self.label.setText("Failed to launch the stinker!")
        
    def pause_scan(self):
        self.b1.setText("Click to begin dookie.")
        self.b2.setText("Dookie Ceasefire...")
        if not arduino.is_open:
            arduino.open
        try:
            self.thread[1].stop()
        except:
            print("No fart not commenced.")
        self.b1.setDisabled(False)
        self.b2.setDisabled(True)
        
    def init_scan(self):
        arduino.open
        index = self.sender().index
        if index == 0:
            self.b1.setEnabled(True)
            self.b2.setEnabled(False)
            self.b1.setText("Click to begin dookie.")
            self.b2.setText("Test your fate.")
            self.label.setText("Failed to launch the stinker!")
        elif index == 1:
            QSound.play("fart.wav")
        
class ThreadClass(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(int)
    
    def __init__(self, parent=None,index=0):
        super(ThreadClass, self).__init__(parent)
        self.index=index
        self.is_running = True

    def portWatch(self):
        ports = serial.tools.list_ports.comports()
        n = 0
        for port in ports:
           print(str(ports[n]))
           n += 1 
        if "Arduino" not in ports:
            return False
        if "Arduino" in ports:
            return True

    def run(self):
        go = True
        if arduino.port == "NOPORTFOUND" or self.portWatch() == True:
            self.stop
        else:
            print('Starting thread...',self.index)     
            portName()
            serial.Serial().open
            print(arduino.is_open)
            while go:
                line = str(serial.Serial().readline())
                print(line[2:-5])
                    
                if "BEEP" in line:
                    self.any_signal.emit(self.index)
            else:  
                self.index = 0
                self.any_signal.emit(self.index)
                portName()
                print(arduino.port)
                if arduino.port == "NOPORTFOUND":
                    self.terminate()
                elif arduino.port != "NOPORTFOUND":
                    arduino.open
                print('Please check the port')
                

    def stop(self):
        portName()
        if not arduino.is_open:
            print("Arduino is closed!")
        else:
            print("Arduino is still open!")
        self.is_running = False
        print('Stopping thread...',self.index)
        self.terminate()

# Creates a window with properties to close.
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
# Starts the program.
window()