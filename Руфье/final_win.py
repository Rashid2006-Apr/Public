<<<<<<< HEAD
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
        
    def initUI(self):
        self.c_line = QVBoxLayout()
        self.index = QLabel(txt_index)
        self.workheart = QLabel(txt_workheart)
        self.c_line.addWidget(self.index, alignment=Qt.AlignCenter)
        self.c_line.addWidget(self.workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.c_line)
=======
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
>>>>>>> 77aa5063b4667b0516cee0302dd072e356430af8
