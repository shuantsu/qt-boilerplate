# ======================
# QT
# ======================
import qdarkstyle
from PyQt5 import QtWidgets, QtCore 



# ======================
# modules
# ======================
from gui import Ui_Form
import sys



# ======================
# main script
# ======================
class MyWindow(QtWidgets.QWidget):
 
    def __init__(self):
     
        super(MyWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #self.showMaximized()


# ======================
# run
# ======================
app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
sys.exit(app.exec())