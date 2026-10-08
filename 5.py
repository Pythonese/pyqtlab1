import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class RestaurantOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заказ в ресторане")
        self.setGeometry(100, 100, 500, 400)

        self.menu = {
            "Пицца": 350,
            "Паста": 280,
            "Салат": 200,
            "Суп": 180,
            "Стейк": 550,
        }

        self.order = {}

        self.checkboxes = {}
        self.spins = {}
        self.total_label = QLabel("Итого: 0 руб.")
        self.receipt = QPlainTextEdit()
        self.receipt.setReadOnly(True)

        main_layout = QVBoxLayout()

        group = QGroupBox("Меню")
        grid = QGridLayout()
        row = 0
        for dish, price in self.menu.items():
            chk = QCheckBox(f"{dish} ({price} руб.)")
            chk.stateChanged.connect(self.update_order)
            spin = QLineEdit("1")
            spin.setFixedWidth(40)
            spin.textChanged.connect(self.update_order)
            self.checkboxes[dish] = chk
            self.spins[dish] = spin
            grid.addWidget(chk, row, 0)
            grid.addWidget(QLabel("Кол-во:"), row, 1)
            grid.addWidget(spin, row, 2)
            row += 1
        group.setLayout(grid)
        main_layout.addWidget(group)

        main_layout.addWidget(self.total_label)
        main_layout.addWidget(QLabel("Чек:"))
        main_layout.addWidget(self.receipt)

        self.setLayout(main_layout)
        self.update_order()

    def update_order(self):
        total = 0
        receipt_lines = []
        for dish, chk in self.checkboxes.items():
            if chk.isChecked():
                try:
                    qty = int(self.spins[dish].text())
                    if qty < 1:
                        qty = 1
                        self.spins[dish].setText("1")
                except ValueError:
                    qty = 1
                    self.spins[dish].setText("1")
                price = self.menu[dish]
                cost = qty * price
                total += cost
                receipt_lines.append(f"{dish}: {qty} шт. = {cost} руб.")
            else:
                self.spins[dish].setText("1")

        self.total_label.setText(f"Итого: {total} руб.")
        self.receipt.setPlainText("\n".join(receipt_lines) if receipt_lines else "Корзина пуста")

app = QApplication(sys.argv)
window = RestaurantOrder()
window.show()
sys.exit(app.exec())
