"""Main application window."""

from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QTabWidget

from .views import (
    axis_view,
    budget_view,
    import_view,
    indices_view,
    prioritization_view,
    prognosis_view,
    projection_view,
    reports_view,
    segmentation_view,
    treatments_view,
)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Pavement Planner")
        tabs = QTabWidget()
        tabs.addTab(import_view.ImportView(), "Import")
        tabs.addTab(axis_view.AxisView(), "Eix")
        tabs.addTab(projection_view.ProjectionView(), "Projecció")
        tabs.addTab(indices_view.IndicesView(), "Índexs")
        tabs.addTab(segmentation_view.SegmentationView(), "Segmentació")
        tabs.addTab(treatments_view.TreatmentsView(), "Tractaments")
        tabs.addTab(prioritization_view.PrioritizationView(), "Priorització")
        tabs.addTab(budget_view.BudgetView(), "Pressupost")
        tabs.addTab(prognosis_view.PrognosisView(), "Prognosi")
        tabs.addTab(reports_view.ReportsView(), "Informes")
        self.setCentralWidget(tabs)
