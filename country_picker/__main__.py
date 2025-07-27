import argparse
import sys
from PyQt6.QtWidgets import QApplication
from country_picker.mainwindow import MainWindow

def main():
    parser = argparse.ArgumentParser(description="Run the Expert Country Picker application.")
    parser.add_argument(
        "--select",
        type=str,
        help="Pre-select country (e.g., --select 'Aruba').",
    )
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = MainWindow(preselect_country=args.select)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()