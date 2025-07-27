from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

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