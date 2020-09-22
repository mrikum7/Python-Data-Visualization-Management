from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QPushButton

class Cricket(QMainWindow):
    def __init__(self):
        super().__init__()
        self.runup = 0
        self.wicket = 0
        self.run = QLabel(self)
        self.run.setText(f"{self.runup}-{self.wicket}")
        self.run.setGeometry(200, 0, 100, 100)
        self.run.show()

        self.one = QPushButton('1', self)
        self.one.setGeometry(0, 150, 100, 100)
        self.one.clicked.connect(self.func_one)
        self.one.show()

        self.two = QPushButton('2', self)
        self.two.setGeometry(100, 150, 100, 100)
        self.two.show()

        self.three = QPushButton('3', self)
        self.three.setGeometry(200, 150, 100, 100)
        self.three.show()

        self.four = QPushButton('4', self)
        self.four.setGeometry(300, 150, 100, 100)
        self.four.show()

        self.six = QPushButton('6', self)
        self.six.setGeometry(400, 150, 100, 100)
        self.six.show()

        ## Make a button for OUT and implement the logic behind it.

        self.show()
    
    def func_one(self):
        self.runup = self.runup + 1
        self.run.setText(f"{self.runup}-{self.wicket}")

app = QApplication(['Cricket'])

obj = Cricket()

app.exec_()

