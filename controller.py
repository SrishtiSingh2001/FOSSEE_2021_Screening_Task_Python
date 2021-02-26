import sys
from PyQt5 import QtWidgets, QtGui
import view
from model import Model

class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = view.Window()


    def run(self):
        self._view.show()

        return self._app.exec_()


if __name__ == '__main__':
    c = Controller()
    sys.exit(c.run())
