"""Projection view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ProjectionView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Projection view"))
        self.setLayout(layout)
