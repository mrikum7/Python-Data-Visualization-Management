from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
import numpy as np
import pyqtgraph as pg

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.t = np.linspace(0, 2 * np.pi, 1000)
        self.num = 0.01
        self.graph = pg.PlotWidget(self, background = 'k')
        self.grid = QGridLayout()
        self.timer = QTimer()
        self.grid.addWidget(self.graph, 0, 0, 1, 1)
        self.setLayout(self.grid)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000/60)
        self.graph.show()
        self.graph.plotItem.setLabel('left', 'Sine')
        self.setGeometry(0, 0, 500, 200)
        self.show()


    def update(self):
        self.graph.plotItem.clear()
        self.pen = pg.mkPen('y', width = 3)
        data = np.sin(self.t + self.num)
        self.graph.plotItem.plot(self.t, data, pen = self.pen)
        self.num = self.num + 0.01
        
        

app = QApplication(['Auto Update'])

win = Window()

app.exec_()