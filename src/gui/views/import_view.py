"""Import view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class ImportView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Import view"))
        self.setLayout(layout)
