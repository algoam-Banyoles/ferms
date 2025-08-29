"""Treatments view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class TreatmentsView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Treatments view"))
        self.setLayout(layout)
