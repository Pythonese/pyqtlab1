import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class WordThrower(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перекидыватель слов")
        self.setGeometry(100, 100, 400, 150)

        self.left_edit = QLineEdit()
        self.right_edit = QLineEdit()
        self.btn = QPushButton("→")
        self.btn.setFixedWidth(50)
        self.btn.clicked.connect(self.throw_word)

        self.direction = 1

        layout = QHBoxLayout()
        layout.addWidget(self.left_edit)
        layout.addWidget(self.btn)
        layout.addWidget(self.right_edit)
        self.setLayout(layout)

    def throw_word(self):
        left_text = self.left_edit.text()
        right_text = self.right_edit.text()
        self.right_edit.setText(left_text)
        self.left_edit.setText(right_text)
        if self.direction == 1:
            self.btn.setText("←")
            self.direction = -1
        else:
            self.btn.setText("→")
            self.direction = 1

app = QApplication(sys.argv)
window = WordThrower()
window.show()
sys.exit(app.exec())
