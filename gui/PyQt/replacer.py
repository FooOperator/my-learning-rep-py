import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon

class App(QMainWindow):
    message = 'Hey nerds!'
    
    def __init__(self):
        super().__init__()
        self.title = 'String Replacer'
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        self.label = QLabel('<h1>{}</h1>'.format(self.message), self)
        self.label.move(20, 0)
        self.label.resize(300, 40)
        self.label.setStyleSheet('background-color: black; color: white')
        
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 50)
        self.textbox.resize(280, 40)
        
        # Create a button in the window
        self.button = QPushButton('Replace', self)
        self.button.move(20, 100)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    def on_click(self):
        self.message = self.textbox.text()
        self.label.setText(f'<h1>{self.message}</h1>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())