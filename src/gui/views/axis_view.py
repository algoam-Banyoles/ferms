"""Axis view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class AxisView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Axis view"))
        self.setLayout(layout)
