import sys
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                          QWidget, QVBoxLayout, QSpinBox, QLabel)
from PySide6.QtCore import Qt

class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
        

    def init_ui(self):
        # central window 설정
        self.setWindowTitle("QSpinBox HW.")
        self.setGeometry(100, 100, 300, 200)

        # central widget 생성
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Vertical Layout 생성
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QSpinBox 인스턴스 생성
        spinbox = QSpinBox()
        spinbox.setMinimum(0)
        spinbox.setMaximum(10)
        spinbox.setValue(5)
        spinbox.setSingleStep(1)

        # QSpinBox 인스턴스 의 value 변경 처리 slot 지정.
        spinbox.valueChanged.connect(self.on_value_changed)

        # layout manager에 QSpinBox 인스턴스 추가
        layout.addWidget(spinbox)

        # QSpinBox 인스턴스의 현재  value를 표시할 QLabel 인스턴스 생성.
        self.label = QLabel("Selected Value: 5")
        layout.addWidget(self.label)

    def on_value_changed(self, value):
        self.label.setText(f"Selected Value: {value}")
        
    def keyPressEvent(self, event):
        
        if event.key() == Qt.Key.Key_P:
            print("P key pressed!")
            self.change_value(2)
            
        elif event.key() == Qt.Key.Key_M:
            print("M key pressed!")
            self.change_value(-2)
        else:
            super().keyPressEvent(event)
    
    def change_value(self, step):
        new_value = max(0, min(10, self.spinbox.value() + step))
        self.spinbox.setValue(new_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MW()
    main_window.show()
    sys.exit(app.exec())