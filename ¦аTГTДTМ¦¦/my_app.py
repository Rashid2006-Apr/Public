from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from instr import *
from second_win import *


class MainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.bnt_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_txt, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.bnt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
mw = MainWin()
app.exec_()
