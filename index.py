from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
from circuit_ui import Ui_MainWindow as circuit
from home import Ui_MainWindow as home
app = QApplication([])

window = QWidget()
ui = home(window)
if __name__ == "__main__":
    window.show()
    app.exec()

