from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit

app = QApplication(['First GUI'])

text = QTextEdit()

text.show()

app.exec_()