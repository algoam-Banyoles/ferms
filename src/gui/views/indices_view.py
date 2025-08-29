"""Indices view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class IndicesView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Indices view"))
        self.setLayout(layout)
