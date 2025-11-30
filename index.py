from PySide6.QtWidgets import QApplication, QMainWindow
from circuit_ui import Ui_MainWindow

app = QApplication([])

window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
app.exec()
