from PySide6.QtWidgets import QApplication, QMainWindow,QStackedWidget
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite_Mode
from Models.Models_for_applications_functionnality.Getter_and_Setter_for_Both_Database_Deffrent_database import Initialization_instance, Sqlite_Interaction
from Models.Models_for_applications_functionnality.Set_Database_Information import Insert_Database_Information
from configration import Ui_Madagascar_Tours
from login import Ui_Form
app = QApplication([])



class Diffrent_MainWindow(QMainWindow):
    Ui_Tours: Ui_Madagascar_Tours = Ui_Madagascar_Tours()
    
    def terminal_print(self,data):
        print(data)
    def __init__(self,window:QMainWindow):
        self.Ui_Tours.setupUi(window)
        self.Ui_Tours.submit_and_close_btn.clicked.connect(self.configuration_submit)
    def loadin_main_window(self,window:QMainWindow):
        pass
    def home_main_window(self,window:QMainWindow):
        pass

    def configuration_submit(self):
        sqlite_instance = Sqlite_Interaction()
        database_info = User_of_Database_for_Sqlite_Mode(database_hosting=self.Ui_Tours.hosting_database_input.text(),database_name=self.Ui_Tours.Nom_de_la_base_de_donnees_input.text(),database_password=self.Ui_Tours.password_input.text(),database_port=self.Ui_Tours.port_number_input.text(),database_user=self.Ui_Tours.nom_d_utilisateur_input.text(),id=None)
        Bool:bool = sqlite_instance.Set_Database_Information(database_info)
        print(Bool)
        if Bool:
            self.close()
        

window = QMainWindow()
ui = Diffrent_MainWindow(window=window)
if __name__ == "__main__":
    window.show()
    app.exec()

