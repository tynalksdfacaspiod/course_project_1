from PySide6.QtWidgets import QApplication

from windows.main_window import MainWindow

app = QApplication([])

window = MainWindow()
window.resize(400, 800)
window.show()

app.exec()
