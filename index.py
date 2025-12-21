from PySide6.QtWidgets import QApplication, QMainWindow
from Controller.initiation_class import Initialization_instance
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite_Mode
from configration import Ui_Madagascar_Tours as Configuration
from Tours import Ui_Madagascar_Tours as Home
from login import Ui_Form
app = QApplication([])



class Diffrent_MainWindow(QMainWindow):
    data_used = Initialization_instance()
    COnfiguration_UI: Configuration = Configuration()
    Tours_Manager_UI:Home = Home()

    def __init__(self,window:QMainWindow):
        self.window_instance = window
        self.COnfiguration_UI.setupUi(self.window_instance)
        #self.COnfiguration_UI.submit_and_close_btn.clicked.connect(self.configuration_submit)

    def configuration_submit(self):
        database_info = User_of_Database_for_Sqlite_Mode(database_hosting=self.COnfiguration_UI.hosting_database_input.text(),database_name=self.COnfiguration_UI.Nom_de_la_base_de_donnees_input.text(),database_password=self.COnfiguration_UI.password_input.text(),database_port=self.COnfiguration_UI.port_number_input.text(),database_user=self.COnfiguration_UI.nom_d_utilisateur_input.text(),id=None)
        Bool:bool = self.data_used.Set_Database_Information(database_info)
        print(Bool)
        

window = QMainWindow()
ui = Diffrent_MainWindow(window=window)
if __name__ == "__main__":
    window.show()
    app.exec()

