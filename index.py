from PySide6.QtWidgets import QApplication, QMainWindow
from circuit_ui import Ui_MainWindow

app = QApplication([])

window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)


if __name__ == "__main__":
    window.show()
    app.exec()

