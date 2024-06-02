import sys
from PySide6.QtWidgets import (QApplication, 
                                         QMainWindow, QLabel, QWidget)
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Event Handling Ex")
        label = QLabel(
            """<p>Press the <b>ESC</b> key
            to quit this program.</p>""")
        self.setCentralWidget(label)
        self.show()

    def keyPressEvent(self, event):
        """Reimplement the key press event to close the
        window."""
        if event.key() == Qt.Key.Key_A:
            print("A key pressed!")
            self.new_window = NewWindow()
            self.new_window.show()
            
        elif event.key() == Qt.Key.Key_Escape:
            print("esc key pressed!")
            self.close()
            
class NewWindow(MW):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")
        self.setGeometry(200, 200, 300, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MW()
    sys.exit(app.exec())