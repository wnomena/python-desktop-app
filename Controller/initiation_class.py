from sqlalchemy.orm import Session


from Controller.returned_circuit_manager import Group_element_to_simpllify_render, Reterned_Circuit
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode
from Models.DB.pool_creation import Mysql_Engine, Sqlite_Engine
from Models.Models_for_applications_functionnality.Get_One_Circuit_With_Jointure import Get_One_Circuit_by_Id
from Models.Models_for_applications_functionnality.Get_All_Contact import Get_all_Contact
from Models.Models_for_applications_functionnality.Get_all_Circuit import Get_ALl_Circuit, Get_all_Model
from Models.Models_for_applications_functionnality.Getter_and_Setter_for_Both_Database_Deffrent_database import Insert_All_Contact, Insert_All_Equipment, Insert_All_Included_In_Price, Insert_All_Itinerary, Insert_All_Tour


class Initialization_instance(Mysql_Engine,Sqlite_Engine):
    data_to_migrate:Get_all_Model = None
    def __init__(self):
        #super().__init__(self)
        self.data_to_migrate = Get_ALl_Circuit(self._engine)
        Insert_All_Tour(self.engine,data=self.data_to_migrate.circuit)
        Insert_All_Itinerary(self.engine,self.engine,data=self.data_to_migrate.itinerary)
        Insert_All_Equipment(self.engine,self.data_to_migrate.equipment)
        Insert_All_Included_In_Price(self.engine,self.data_to_migrate.included)
        Insert_All_Contact(self.engine,Get_all_Contact(self._engine))
        

    def Get_One(self,id:int)  -> list[Reterned_Circuit]:
        list_of_circuit:list[Reterned_Circuit] = []
        data_brute_from_sqlite = Get_One_Circuit_by_Id(self.engine,id).data
        filter_method_to_avoid_repetition_from_jointure = Group_element_to_simpllify_render(data_brute_from_sqlite)
        for element in filter_method_to_avoid_repetition_from_jointure:
            list_of_circuit.append(element)
        return list_of_circuit
    
    def Set_Database_Information(self,User_and_Database:User_of_Database_for_Sqlite_Mode) -> bool:
        try:
            with Session(self.engine) as conn:
                print(User_and_Database.__dict__)
                conn.add(User_of_Database_for_Sqlite(database_hosting=User_and_Database.database_hosting,database_name=User_and_Database.database_name,database_password=User_and_Database.database_password,database_port=User_and_Database.database_port,database_user=User_and_Database.database_user))
                conn.commit()
                return True
        except Exception as err :
            print(err)
            return False
class Contact_Set_Interval(Mysql_Engine):
    def __init__(self):
        super().__init__()
    
    def Get_Contact(self):
        pass