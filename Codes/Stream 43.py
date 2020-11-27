from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QFont

class Cricket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.font = QFont('Times', 20, QFont.Bold)
        self.runup = 0
        self.wicket = 0
        self.run = QLabel(self)
        self.run.setText(f"{self.runup}-{self.wicket}")
        self.run.setGeometry(200, 0, 100, 100)
        self.run.setFont(self.font)
        self.run.show()

        self.one = QPushButton('1', self)
        self.one.setGeometry(0, 150, 100, 100)
        self.one.clicked.connect(self.func_one)
        self.one.show()

        self.two = QPushButton('2', self)
        self.two.setGeometry(100, 150, 100, 100)
        self.two.clicked.connect(self.func_two)
        self.two.show()

        self.three = QPushButton('3', self)
        self.three.setGeometry(200, 150, 100, 100)
        self.three.clicked.connect(self.func_three)
        self.three.show()

        self.four = QPushButton('4', self)
        self.four.setGeometry(300, 150, 100, 100)
        self.four.clicked.connect(self.func_four)
        self.four.show()

        self.six = QPushButton('6', self)
        self.six.setGeometry(400, 150, 100, 100)
        self.six.clicked.connect(self.func_six)
        self.six.show()

        self.out = QPushButton('Out', self)
        self.out.setGeometry(500, 150, 100, 100)
        self.out.clicked.connect(self.func_out)
        self.out.show()

        ## Make a button for OUT and implement the logic behind it.

        self.show()
    
    def func_one(self):
        self.runup = self.runup + 1
        self.run.setText(f"{self.runup}-{self.wicket}")

    def func_two(self):
        self.runup = self.runup + 2
        self.run.setText(f"{self.runup}-{self.wicket}")
    
    def func_three(self):
        self.runup = self.runup + 3
        self.run.setText(f"{self.runup}-{self.wicket}")
    
    def func_four(self):
        self.runup = self.runup + 4
        self.run.setText(f"{self.runup}-{self.wicket}")

    def func_six(self):
        self.runup = self.runup + 6
        self.run.setText(f"{self.runup}-{self.wicket}")
    
    def func_out(self):
        if self.wicket < 9:
            self.wicket = self.wicket + 1
            self.run.setText(f"{self.runup}-{self.wicket}")
        else:
            self.run.setText(f"{self.runup}")

app = QApplication(['Cricket'])

obj = Cricket()

app.exec_()

