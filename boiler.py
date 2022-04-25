import sys,random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
from farsiDictionary import farsimap

from module_flashcards_ import UiModuleFlashcards
clicks=-1
clicks=0
I=0
J=0
shuffled_dictionary={}
fm_keys=list(farsimap.keys())
random.shuffle(fm_keys)
total_length=[]
cum_len=[]
for i in fm_keys:
    total_length.append(len(list(farsimap[i].keys())))
    if len(cum_len) > 0:
        cum_len.append(total_length[-1]+cum_len[-1])
    else:
        cum_len.append(total_length[-1])

for i in fm_keys:
    fm_keys_keys=list(farsimap[i].keys())
    random.shuffle(fm_keys_keys)
    shuffled_dictionary[i]={}
    for j in fm_keys_keys:
        shuffled_dictionary[i][j]=farsimap[i][j]

#print(shuffled_dictionary)

class ModuleFlashcardsWindow(QWidget):
    global farsimap, clicks, shuffled_dictionary, total_length, cum_len, fm_keys, I, J
    
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
        global farsimap, clicks, shuffled_dictionary, total_length, cum_len, fm_keys, I, J
        clicks+=1
        if clicks > cum_len[I]:
            I+=1
            J=0
        
        new_word_list=list(shuffled_dictionary[fm_keys[I]].keys())
        print(new_word_list)
        self.ui.label.setText(fm_keys[I])
        self.ui.label_2.setText(farsimap[fm_keys[I]][new_word_list[J]])
        self.ui.label_3.setText(new_word_list[J])
        J+=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleFlashcardsWindow = ModuleFlashcardsWindow()
    ModuleFlashcardsWindow.show()
    sys.exit(app.exec_())

        
#        self.ui.pushButton.clicked.connect(self.clicked)

'''

'''
