from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from instr import *
from final_win import *

class TestWin(QWidget):

    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.txt_name = QLabel(txt_name)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.btn_test1 = QPushButton(txt_starttest1)
        self.btn_test2 = QPushButton(txt_starttest2)
        self.btn_test3 = QPushButton(txt_starttest3)
        self.btn_sendresults = QPushButton(txt_sendresults)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_hintage = QLineEdit(txt_hintage)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.timer = QLabel(txt_timer)
       
        self.txt_age = QLabel(txt_age)
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hintname, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hintage, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.txt_hinttest3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.btn_sendresults, alignment=Qt.AlignCenter)
        
        self.r_line.addWidget(self.timer, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()          

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_sendresults.clicked.connect(self.next_click)


    




