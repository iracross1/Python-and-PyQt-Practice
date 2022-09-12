# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt."""

#provides the exit() function
import sys

#imports the required classes from PyQt6.QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

#creates a Python constant to hold a fixed window size in pixels for your calculator app.
WINDOW_SIZE = 235

#creates the PyCalcWindow class to provide the app’s GUI. Note that this class inherits from QMainWindow.
Class PyCalcWindow(QMainWindow):
    ""PyCalc's main window (GUI or view)."""

#defines the class initializer.
    def__init__(self):
#calls .__init__() on the super class for initialization purposes.
       super().__init__()
#sets the window’s title to "PyCalc"
       self.setWindowTitle("PyCalc")
#uses .setFixedSize() to give the window a fixed size
       self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
#create a QWidget object and set it as the window’s central widget.
       centralWidget = QWidget(self)
       self.setCentralWidget(centralWidget)

#defines your calculator’s main function
def main():
    """PyCalc's main function."""
    pycalcApp = QAppication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()
