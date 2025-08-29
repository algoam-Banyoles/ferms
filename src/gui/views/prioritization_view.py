"""Prioritization view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PrioritizationView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Prioritization view"))
        self.setLayout(layout)
