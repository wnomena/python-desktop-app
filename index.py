from PySide6.QtWidgets import QApplication, QMainWindow
from circuit_ui import Ui_MainWindow as circuit
from configuration import Ui_MainWindow as config

app = QApplication([])

window = QMainWindow()
ui = circuit()
ui.setupUi(window)


if __name__ == "__main__":

    window.show()
    app.exec()

