from PySide6.QtWidgets import QApplication, QMainWindow,QStackedWidget
from Models.Models_for_applications_functionnality.Getter_and_Setter_for_Both_Database_Deffrent_database import Initialization_instance
from circuit_ui import Ui_MainWindow as circuit
from login import Ui_Form
app = QApplication([])

class MainWindow(QMainWindow):
    stack = QStackedWidget()
    def __init__(self,window:QMainWindow):
        self.window:QMainWindow = window
        self.window.resize(594, 250)
        self.window.setStyleSheet(u"background-color: rgb(154, 153, 150);")
        self.widget = Ui_Form(self.window)
        self.window.setWindowTitle("Madagascar-tours")
        self.window.setCentralWidget(self.widget)

window = QMainWindow()
ui = MainWindow(window)
if __name__ == "__main__":
    window.show()
    app.exec()

