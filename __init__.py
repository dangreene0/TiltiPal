from windows.mainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

# Creates a window with properties to close.
def startApp():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
# Starts the program.
startApp()