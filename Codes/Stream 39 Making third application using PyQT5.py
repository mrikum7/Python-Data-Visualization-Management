import sqlite3
from PyQt5.QtWidgets import QApplication, QTextEdit, QLabel, QPushButton, QWidget

app = QApplication(['Class Database'])

database = sqlite3.connect('Class_Data.db')
table_sql = '''create table if not exists Students(
               Sno Integer Primary Key,
               FirstName Varchar(50),
               LastName Varchar(50),
               Class Varchar(20)
);'''
database.execute(table_sql)

def InputData():
    first = first_text.toPlainText()
    last = last_text.toPlainText()
    CLASS = class_text.toPlainText()

    sql = f"insert into Students (FirstName, LastName, Class) values('{first}', '{last}', '{CLASS}');"
    database.execute(sql)
    database.commit()
    database.close()

win = QWidget()
win.show()

first_label = QLabel('First Name', win)
first_label.setGeometry(15, 0, 100, 50)
first_label.show()

first_text = QTextEdit(win)
first_text.setGeometry(0, 60, 100, 50)
first_text.show()

last_label = QLabel('Last Name', win)
last_label.setGeometry(150 + 15, 0, 100, 50)
last_label.show()

last_text = QTextEdit(win)
last_text.setGeometry(150, 60, 100, 50)
last_text.show()

class_label = QLabel('Class', win)
class_label.setGeometry(300 + 30, 0, 100, 50)
class_label.show()

class_text = QTextEdit(win)
class_text.setGeometry(300, 60, 100, 50)
class_text.show()

submit_button = QPushButton('Submit', win)
submit_button.setGeometry(150, 150, 100, 50)
submit_button.show()

submit_button.clicked.connect(InputData)

app.exec_()