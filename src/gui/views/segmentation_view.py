"""Segmentation view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class SegmentationView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Segmentation view"))
        self.setLayout(layout)
