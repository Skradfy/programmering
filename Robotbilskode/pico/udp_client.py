import serial
from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button_on = QtWidgets.QPushButton('On', self)
        self.button_on.clicked.connect(self.send_on)

        self.button_off = QtWidgets.QPushButton('Off', self)
        self.button_off.clicked.connect(self.send_off)

        self.button_ana = QtWidgets.QPushButton('Ana', self)
        self.button_ana.clicked.connect(self.send_ana)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button_on)
        layout.addWidget(self.button_off)
        layout.addWidget(self.button_ana)
        self.setLayout(layout)
        self.setWindowTitle('Pico Controller')

    def send_on(self):
        self.send_command('on')

    def send_off(self):
        self.send_command('off')

    def send_ana(self):
        self.send_command('ana')

    def send_command(self, command):
        ser.write(command.encode())

ser = serial.Serial('COM14', 9600)  # Replace 'COM14' with your HC-06 COM port

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
