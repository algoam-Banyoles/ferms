"""Reports view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ReportsView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Reports view"))
        self.setLayout(layout)
