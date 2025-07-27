from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)
import requests
from country_picker.parsecountrydata import parse_country_data

URL = "https://www.apicountries.com/countries"

class MainWindow(QMainWindow):
    """Main window for the Expert Country Picker application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expert Country Picker")
        self.resize(300, 100)

        # Create empty dropdown and label
        self.combo = QComboBox()
        self.label = QLabel("")

        # Add to layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.fetch_data_and_fill_qcombobox()
        self.combo.currentTextChanged.connect(self.on_country_selected)

    def fetch_data_and_fill_qcombobox(self):
        """Fetch country data from the API and populate the QComboBox."""
        try:
            response = requests.get(URL)
            response.raise_for_status()
            self.combo.addItems(parse_country_data(response.json()))
        except Exception as e:
            self.label.setText(f"Failed to load countries: {e}")

    def on_country_selected(self, country_name):
        """Handle the selection of a country from the QComboBox."""
        self.label.setText(f"You selected: {country_name}")    