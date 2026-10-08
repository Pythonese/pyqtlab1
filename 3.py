import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QPlainTextEdit, QMessageBox, QGroupBox)
from PyQt6.QtCore import Qt

class HideWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пряталки")
        self.setGeometry(100, 100, 400, 200)

        self.widgets = []
        self.checkboxes = []

        for i in range(3):
            lbl = QLabel(f"Виджет {i+1}")
            lbl.setStyleSheet("border: 1px solid black; padding: 10px;")
            chk = QCheckBox(f"Показать {i+1}")
            chk.setChecked(True)
            chk.stateChanged.connect(self.toggle_visibility)
            self.widgets.append(lbl)
            self.checkboxes.append(chk)

        layout = QVBoxLayout()
        for w, chk in zip(self.widgets, self.checkboxes):
            h = QHBoxLayout()
            h.addWidget(chk)
            h.addWidget(w)
            layout.addLayout(h)
        self.setLayout(layout)

    def toggle_visibility(self, state):
        sender = self.sender()
        for i, chk in enumerate(self.checkboxes):
            if chk is sender:
                self.widgets[i].setVisible(chk.isChecked())

app = QApplication(sys.argv)
window = HideWidgets()
window.show()
sys.exit(app.exec())
