import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setGeometry(100, 100, 300, 400)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setText("0")

        self.current = 0.0
        self.operator = None
        self.new_number = True

        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0, 1, 4)
        ]

        for btn in buttons:
            if len(btn) == 3:
                text, r, c = btn
                rowspan = 1
                colspan = 1
            else:
                text, r, c, rs, cs = btn
                rowspan = rs
                colspan = cs
            b = QPushButton(text)
            b.clicked.connect(self.on_button_click)
            grid.addWidget(b, r, c, rowspan, colspan)

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text.isdigit() or text == '.':
            if self.new_number:
                self.display.setText(text if text != '.' else '0.')
                self.new_number = False
            else:
                if text == '.' and '.' in self.display.text():
                    return
                self.display.setText(self.display.text() + text)
        elif text in '+-*/':
            self.compute()
            self.current = float(self.display.text())
            self.operator = text
            self.new_number = True
        elif text == '=':
            self.compute()
            self.operator = None
            self.new_number = True
        elif text == 'C':
            self.display.setText('0')
            self.current = 0.0
            self.operator = None
            self.new_number = True

    def compute(self):
        if self.operator is None:
            return
        try:
            right = float(self.display.text())
            if self.operator == '+':
                result = self.current + right
            elif self.operator == '-':
                result = self.current - right
            elif self.operator == '*':
                result = self.current * right
            elif self.operator == '/':
                if right == 0:
                    QMessageBox.critical(self, "Ошибка", "Деление на ноль!")
                    return
                result = self.current / right
            else:
                return
            self.display.setText(str(result))
        except Exception:
            QMessageBox.critical(self, "Ошибка", "Некорректный ввод")

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
