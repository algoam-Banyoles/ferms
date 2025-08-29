"""Budget view placeholder."""

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class BudgetView(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Budget view"))
        self.setLayout(layout)
