import sys, os #시스템을 호출함

# import PySide6.QtCore
# from PySide6.QtWidgets import (QApplication, QWidget,QLabel)

PYSIDE = True  
try:
     import PySide6.QtCore
     from PySide6.QtCore import QSize  #pyside를 기반으로 돌아가는 가상환경
     from PySide6.QtWidgets import (QApplication, QWidget, 
                             QLabel, QPushButton)  
     from PySide6.QtGui import QFont,QIcon   
except: 
    PYSIDE = False

PYQT = True
try: 
    import PyQt6.QtCore  #pyqt를 기반으로 돌아가는 가상환경
    from PyQt6.QtWidgets import  (QApplication, QWidget, 
                             QLabel, QPushButton)
    from PyQt6.QtGui import QFont,QIcon
except:
    PYQT = False 
    
class MW(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Set up the appliation's GUI"""
        self.setFixedSize(250,250)
        self.setWindowTitle('QPushButton Example')
        self.setup_main_wnd()
        self.show()
        
    def setup_main_wnd(self):
        """Set up the Main Window"""
        
        self.hello_label = QLabel(self)
        self.hello_label.setText('Hello, World and Qt')
        self.hello_label.setFont(QFont('Arial',15))
        
        self.hello_label.move(10,20)
        
        path_py_file = os.path.realpath(__file__)
        path_py_file = os.path.dirname(path_py_file)
        img_fstr = os.path.join(path_py_file,'/visualstudio/world.jpg')

        it_button = QPushButton("icon and text button",self)
        it_button.setIcon(QIcon(img_fstr))
        it_button.clicked.connect(self.it_btn_clicked)
        it_button.resize(150,50)
        it_button.move(50,70)

        icon_button = QPushButton(self)
        icon_button.setIcon(QIcon(img_fstr))
        icon_button.clicked.connect(self.icon_btn_clicked)
        icon_button.setIconSize (QSize(120,30))
        icon_button.resize(150,50)
        icon_button.move(50,130)


        text_button = QPushButton("icon button",self)
        text_button.clicked.connect(self.text_btn_clicked) 
        text_button.resize(150,50)
        text_button.move(50,190)

    def it_btn_clicked(self):
        self.hello_label.setText("Icon and txt Button")

    def icon_btn_clicked(self):
        self.hello_label.setText("Icon Button")

    def text_btn_clicked(self):
        self.hello_label.setText("text Button")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())