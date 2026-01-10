from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QAbstractTableModel,Qt
from Controller.initiation_class import Initialization_instance
from Models.DB.Model_for_databases.circuit import Circuit_Model, User_of_Database_for_Sqlite_Mode
from Models.Models_for_applications_functionnality.Get_Database_User_from_Sqlite import Get_Database_Config
from Models.Models_for_applications_functionnality.transverse_models import Four_element_from_Circuit_Table
from configration import Ui_Madagascar_Tours as Configuration
from MainWindow import Ui_MainWindow
app = QApplication([])

# model of data for circuits tableview and contat's

class Circuits_TableView_Model(QAbstractTableModel):
    def __init__(self, data:list[Circuit_Model]):
        self.dynamic_data = [Four_element_from_Circuit_Table(id=element.id,title=element.title,price=element.price) for element in data]
        self.header = ["Id","Titre","Prix"]
    def data(self, index, /, role = ...):
        if index.isValid():
            return self.dynamic_data[index.row()][index.column()]
        else:
            return None
    def rowCount(self, /, parent = ...):
        return len(self.dynamic_data)
    def columnCount(self, /, parent = ...):
        return len(self.header)
    def headerData(self, section, orientation, /, role = ...):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.header[section]


class Diffrent_MainWindow(QMainWindow):
    data_used = Initialization_instance()
    COnfiguration_UI: Configuration = Configuration()
    Acceuil = Ui_MainWindow()

    def __init__(self,window:QMainWindow):
        self.window_instance = window
        if len(Get_Database_Config()):
            self.Acceuil.setupUi(self.window_instance)
        else:
            self.COnfiguration_UI.setupUi(self.window_instance)
            self.COnfiguration_UI.submit_and_close_btn.clicked.connect(self.configuration_submit)

    def configuration_submit(self):
        database_info = User_of_Database_for_Sqlite_Mode(database_hosting=self.COnfiguration_UI.hosting_database_input.text(),database_name=self.COnfiguration_UI.Nom_de_la_base_de_donnees_input.text(),database_password=self.COnfiguration_UI.password_input.text(),database_port=self.COnfiguration_UI.port_number_input.text(),database_user=self.COnfiguration_UI.nom_d_utilisateur_input.text(),id=None)
        Bool:bool = self.data_used.Set_Database_Information(database_info)
        if Bool:
            self.COnfiguration_UI
        

window = QMainWindow()
ui = Diffrent_MainWindow(window=window)
if __name__ == "__main__":
    window.show()
    app.exec()

