from tools.palUtilities import VERSION
from PyQt5.QtGui import QIcon
from windows.mainWindow import MainWindow
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
import sys

# Creates a window with properties to close.
def startApp():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    win.setWindowIcon(QIcon('img/logo.png'))
    trayIcon = QSystemTrayIcon(QIcon("img/logo.png"), parent=app)
    trayIcon.setToolTip(f"TiltiPal {VERSION}")
    sys.exit(app.exec_())
    
# Starts the program.
startApp()