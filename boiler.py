import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget


from module_flashcards import UiModuleFlashcards

class ModuleFlashcardsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings','app8')
        print(self.settings.fileName())
        self.ModuleFlashcardsWindow = QMainWindow()
        self.ui = UiModuleFlashcards()
        self.ui.setupUi(self.ModuleFlashcardsWindow)
        # EVENTS
        self.ui.pushButton.clicked.connect(self.clicked)
    
    def show(self):
        self.ModuleFlashcardsWindow.show()
   
    def clicked(self):
        self.ui.label.setText('Button clicked')
        self.ui.label_2.setText('Button clicked')
        self.ui.label_3.setText('Button clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleFlashcardsWindow = ModuleFlashcardsWindow()
    ModuleFlashcardsWindow.show()
    sys.exit(app.exec_())

        
#        self.ui.pushButton.clicked.connect(self.clicked)

