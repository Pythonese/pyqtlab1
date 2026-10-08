import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class ExpressionCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вычисление выражения")
        self.setGeometry(100, 100, 400, 100)

        self.input_expr = QLineEdit()
        self.output_result = QLineEdit()
        self.output_result.setReadOnly(True)
        self.btn_calc = QPushButton("Вычислить")
        self.btn_calc.clicked.connect(self.calc_expr)

        layout = QHBoxLayout()
        layout.addWidget(self.input_expr)
        layout.addWidget(self.btn_calc)
        layout.addWidget(self.output_result)
        self.setLayout(layout)

    def calc_expr(self):
        try:
            result = eval(self.input_expr.text())
            self.output_result.setText(str(result))
        except Exception:
            QMessageBox.warning(self, "Ошибка", "Некорректное выражение")

app = QApplication(sys.argv)
window = ExpressionCalc()
window.show()
sys.exit(app.exec())
