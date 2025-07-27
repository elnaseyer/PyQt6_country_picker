from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
import requests
from country_picker.async_api_fetcher import ApiLoaderThread
from country_picker.parsers import parse_country_data

class MainWindow(QMainWindow):
    """Main window for the Expert Country Picker application."""

    def __init__(self):
        super().__init__()
        self.fetch_data()
        self.setWindowTitle("Expert Country Picker")
        self.resize(300, 100)

        # Create empty dropdown and label
        self.combo = QComboBox()
        self.label = QLabel("Select a country")

        # Add to layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.combo.currentTextChanged.connect(self.on_country_selected)


    def fetch_data(self) -> None:
        """Fetch country data from the API and populate the QComboBox."""
        self.loader_thread = ApiLoaderThread()
        self.loader_thread.failed.connect(lambda error: print(error))
        self.loader_thread.finished.connect(self.on_countries_loaded)
        self.loader_thread.start()

    def on_countries_loaded(self, countries: list[str]) -> None:
        """Handle the loaded countries and populate the QComboBox."""
        self.combo.addItems(countries)

    def on_country_selected(self, country_name):
        """Handle the selection of a country from the QComboBox."""
        self.label.setText(f"You selected: {country_name}")    