import sys
from PyQt5 import Qtwidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# from django.test import TestCase

print(sys.argv)


def win():
    app = QApplication(sys.argv)
    won = QMainWindow()
    won.show()
    sys.exit(app.exec_())


win()


# Create your tests here.
