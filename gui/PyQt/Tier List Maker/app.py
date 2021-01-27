import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QApplication, QScrollArea, QVBoxLayout
import json

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Tier List Maker'
        self.window_hw = [640, 480]
        self.init_ui()
        
        
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.window_hw[0], self.window_hw[1])
        self.init_list()
        self.show()
        
    def init_list(self):
        self.list_title = QLabel(self)
        self.list_title.setText('Tier List Name')
        
if __name__ == "__main__":
    main = QApplication(sys.argv)
    ex = App()
    sys.exit(main.exec_())