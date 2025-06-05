import os
from PySide6.QtWidgets import QApplication

from frontend.windows.main_window import MainWindow
from backend.other.file import cleanup



if __name__ == "__main__":
    app = QApplication([])
    app.aboutToQuit.connect(cleanup)

    window = MainWindow()
    window.resize(400,800)
    window.show()

    cleanup()

    app.exec()
