import sys
from PyQt5.QtWidgets import QListWidget, QMainWindow, QMessageBox, QApplication, QLabel, QLineEdit, QPushButton, QComboBox, QStyleOption
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from json import load, dump
from PyQt5 import Qt

characters_json_path = 'assets/characters.json'
perks_json_path = 'assets/perks.json'

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Character Creator'
        self.window_coordinates = [150, 200, 600, 500]
        self.x, self.y, self.w, self.h = 60, 20, 200, 23 
        self.bg_color = '#546A7B'
        self.highlight_color = '#E07415'
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.window_coordinates[2], self.window_coordinates[3])
        self.setStyleSheet('background-color: {}'.format(self.bg_color))
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.init_combobox()
        self.init_lineedit()
        self.init_labels()
        self.init_buttons()
        self.init_portrait()
        self.init_list()
        self.show()
    
    def init_portrait(self):
        self.portrait_label = QLabel(self)
        self.portrait_pix = QPixmap()
        self.portrait_label.setPixmap(self.portrait_pix)
        
        self.portrait_label.move(self.x * 6, self.y + (30 * 1))
        self.portrait_label.setFixedSize(self.w, 140)
        self.portrait_label.setStyleSheet('''
                                         border-style: solid; 
                                         border-width: 3px; 
                                         border-color: {};
                                         background-color: black
                                         '''.format(self.highlight_color))
    
    def init_combobox(self):
        self.sheets_combo = QComboBox(self)
        self.sheets_combo.move(self.x * 6, self.y + (30 * 0))
        self.sheets_combo.resize(self.w, self.h)

        self.sheets_combo.addItems(characters_list['Presets'])
        self.sheets_combo.addItems(characters_list['Player Made'])
    
    def init_list(self):
        self.perk_list = QListWidget(self)
        self.perk_list.move(self.x, self.y + (30 * 8) + 20)
        self.perk_list.resize(self.w, 140)
        self.perk_list.addItems(perks_selection)

        self.perk_desc = QLineEdit(self)
        self.perk_desc.move(self.x + 300, self.y + (30 * 8) + 20)
        self.perk_desc.resize(self.w, 140)
        self.perk_desc.setDisabled(True)
        self.perk_desc.setText('This is what is gonna appear')
        self.perk_desc.setStyleSheet('background-color: white')
    
    def init_lineedit(self):
        self.name_box = QLineEdit(self)
        self.name_box.move(self.x, self.y + (30 * 0))
        self.name_box.resize(self.w, self.h)
        self.name_box.setStyleSheet('background-color: {}'.format(self.highlight_color))
        
        self.title_box = QLineEdit(self)
        self.title_box.move(self.x, self.y + (30 * 1))
        self.title_box.resize(self.w, self.h)
        self.title_box.setStyleSheet('background-color: {}'.format(self.highlight_color))
        
        self.bio_box = QLineEdit(self)
        self.bio_box.move(self.x, self.y + (30 * 2))
        self.bio_box.resize(self.w, self.h + 20)
        self.bio_box.setStyleSheet('background-color: {}'.format(self.highlight_color))
        
    def init_labels(self):
        self.namelabel = QLabel('Name', parent=self)
        self.namelabel.move(self.x - 30, self.y + (30 * 0) - 10)
        self.namelabel.lower()
        
        self.titlelabel = QLabel('Title', parent=self)
        self.titlelabel.move(self.x - 30, self.y + (30 * 1) - 10)
        self.titlelabel.lower()
        
        self.biolabel = QLabel('Bio', parent=self)
        self.biolabel.move(self.x - 30, self.y + (30 * 2) - 10)
        self.biolabel.lower()
    
    def init_buttons(self):
        # docstring used as style sheet for all buttons
        btn_stylesheet = '''QPushButton
                            {{
                            background-color : {};
                            }}
                            QPushButton::pressed
                            {{
                            background-color : {};
                            color: {}
                            }}'''.format(self.bg_color, self.highlight_color, 'white')
        
        self.save_btn = QPushButton('Save', self)
        self.save_btn.move(self.x, self.y + (30 * 3) + 20)
        self.save_btn.resize(int(self.w/2), self.h)
        self.save_btn.setStyleSheet(btn_stylesheet)
        
        self.save_btn.clicked.connect(Entry.save_character)
        
        self.clear_btn = QPushButton('Clear', self)
        self.clear_btn.move(self.x + int(self.w/2), self.y + (30 * 3) + 20)
        self.clear_btn.resize(int(self.w/2), self.h)
        self.clear_btn.setStyleSheet(btn_stylesheet)
        
        self.clear_btn.clicked.connect(Entry.clear_character)
        
        self.load_btn = QPushButton('Load', self)
        self.load_btn.move(self.sheets_combo.x(), self.y + (30 * 6))
        self.load_btn.resize(int(self.w/2), self.h)
        self.load_btn.setStyleSheet(btn_stylesheet)
        
        self.load_btn.clicked.connect(Entry.load_character)
        
        self.del_btn = QPushButton('Delete', self)
        self.del_btn.move(self.sheets_combo.x() + self.load_btn.width(), self.y + (30 * 6))
        self.del_btn.resize(int(self.w/2), self.h)
        self.del_btn.setStyleSheet(btn_stylesheet)
        
        self.del_btn.clicked.connect(Entry.del_character)
        
class Entry:
    def clear_character(self):
        # clears textboxes
        ex.name_box.setText('')
        ex.title_box.setText('')
        ex.bio_box.setText('')
        print('cleared')

    def save_character(self):
        # compiles input text into a json
        name = ex.name_box.text()
        title = ex.title_box.text()
        bio = ex.bio_box.text()
        portrait = None
       
        with open(characters_json_path, 'w') as target:
            try:
                new_char = {'{}'.format(name): {'Name': name, 'Title': title, 'Bio': bio, 'Portrait': portrait}}
                characters_list['Player Made'].update(new_char)
                dump(characters_list, target, indent=4, separators=(', ', ': '))
                print('saved')
            except:
                print('not saved')

    def load_character(self):
        # searches temp list for combobox selected option
        try:
            if ex.sheets_combo.currentText() in characters_list['Presets']:
                ex.name_box.setText(characters_list['Presets'][ex.sheets_combo.currentText()]['Name'])
                ex.title_box.setText(characters_list['Presets'][ex.sheets_combo.currentText()]['Title'])
                ex.bio_box.setText(characters_list['Presets'][ex.sheets_combo.currentText()]['Bio'])
                ex.portrait_pix.load(characters_list['Presets'][ex.sheets_combo.currentText()]['Portrait'])
                ex.portrait_label.setPixmap(ex.portrait_pix)
            else:
                ex.name_box.setText(characters_list['Player Made'][ex.sheets_combo.currentText()]['Name'])
                ex.title_box.setText(characters_list['Player Made'][ex.sheets_combo.currentText()]['Title'])
                ex.bio_box.setText(characters_list['Player Made'][ex.sheets_combo.currentText()]['Bio'])
                if characters_list['Player Made'][ex.sheets_combo.currentText()]['Portrait'] == None:
                    print('No portrait associated with entry')
                else:
                    ex.portrait_pix.load(characters_list['Player Made'][ex.sheets_combo.currentText()]['Portrait'])
                    ex.portrait_label.setPixmap(ex.portrait_pix)
            print('loaded')
        except:
            print('not loaded')
    
    def del_character(self):
        # deletes from temp list
        try:
            if ex.sheets_combo.currentText() in characters_list['Player Made']:
                del characters_list['Player Made'][ex.sheets_combo.currentText()]
                with open(characters_json_path, 'w') as target:
                    dump(characters_list, target, indent=4, separators=(', ', ': '))
                    print('deleted')
            else:
                ex.msg.setWindowTitle("Warning")
                ex.msg.setText("You can\'t delete presets!")
                ex.msg.setStandardButtons(QMessageBox.Ok)
                ex.msg.exec_()
                print('can\'t delete presets!')
        except:
            print('not deleted')
            
if __name__ == "__main__":
    with open(characters_json_path) as target:
        characters_list = load(target)
    with open(perks_json_path) as target:
        perks_selection = load(target)
    crud = QApplication(sys.argv)
    ex = App()
    sys.exit(crud.exec_())