"""Prognosis view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PrognosisView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Prognosis view"))
        self.setLayout(layout)
