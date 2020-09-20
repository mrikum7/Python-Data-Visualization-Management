from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class Window(QWidget):
    def __init__(self, name):
        self.name = name
        super().__init__()
        self.setWindowTitle(self.name)
        self.button = QPushButton('Button', self)
        self.button.show()
        self.show()


app = QApplication([])

win = Window('First Window')

app.exec_()

