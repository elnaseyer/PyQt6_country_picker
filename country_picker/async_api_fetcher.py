import requests
from PyQt6.QtCore import QThread, pyqtSignal
from .parsers import parse_country_data
from .constants import URL

class ApiLoaderThread(QThread):
    """
    Thread to fetch country data from an API and emit a sorted list of country names.
    """
    finished = pyqtSignal(list)
    failed = pyqtSignal(str)

    def run(self):
        try:
            response = requests.get(URL, timeout=10)
            response.raise_for_status()
            countries = parse_country_data(response.json())
            self.finished.emit(countries)
        except Exception as e:
            self.failed.emit(f"Failed to load countries: {e}")
