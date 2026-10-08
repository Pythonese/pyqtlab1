import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class MorseCode(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Азбука Морзе")
        self.setGeometry(100, 100, 500, 300)

        self.entry = QLineEdit()
        self.entry.setReadOnly(True)

        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..'
        }

        grid = QGridLayout()
        row, col = 0, 0
        for letter in sorted(self.morse_dict.keys()):
            btn = QPushButton(letter)
            btn.clicked.connect(self.add_morse)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 5:
                col = 0
                row += 1

        layout = QVBoxLayout()
        layout.addWidget(self.entry)
        layout.addLayout(grid)
        self.setLayout(layout)

    def add_morse(self):
        sender = self.sender()
        letter = sender.text()
        if letter in self.morse_dict:
            self.entry.setText(self.entry.text() + self.morse_dict[letter] + " ")

app = QApplication(sys.argv)
window = MorseCode()
window.show()
sys.exit(app.exec())
