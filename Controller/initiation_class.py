from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from Controller.returned_circuit_manager import Group_element_to_simpllify_render, Reterned_Circuit
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode
from Models.DB.pool_creation import Sqlite_Engine
from Models.Models_for_applications_functionnality.Get_One_Circuit_With_Jointure import Get_One_Circuit_by_Id
from Models.Models_for_applications_functionnality.Get_All_Contact import Get_all_Contact
from Models.Models_for_applications_functionnality.Get_all_Circuit import Get_ALl_Circuit, Get_all_Model
from Models.Models_for_applications_functionnality.Getter_and_Setter_for_Both_Database_Deffrent_database import Insert_All_Contact, Insert_All_Equipment, Insert_All_Included_In_Price, Insert_All_Itinerary, Insert_All_Tour


class Initialization_instance(Sqlite_Engine):
    data_to_migrate:Get_all_Model = None
    _engine:Engine = None
    def __init__(self):
        super().__init__()
        self.Get_Database_Config()
        if self._engine:
            self.init_migration()


    def init_migration(self):
        with ThreadPoolExecutor(max_workers=4) as exc:
            self.data_to_migrate = Get_ALl_Circuit(self._engine)
            exc.submit(Insert_All_Tour,self.engine,self.data_to_migrate.circuit)
            exc.submit(Insert_All_Itinerary,self.engine,self.data_to_migrate.itinerary)
            exc.submit(Insert_All_Equipment,self.engine,self.data_to_migrate.equipment)
            exc.submit(Insert_All_Included_In_Price,self.engine,self.data_to_migrate.included)
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
                conn.add(User_of_Database_for_Sqlite(database_hosting=User_and_Database.database_hosting,database_name=User_and_Database.database_name,database_password=User_and_Database.database_password,database_port=User_and_Database.database_port,database_user=User_and_Database.database_user))
                conn.commit()
            self._engine = create_engine(f"mysql+pymysql://{User_and_Database.database_user}:{User_and_Database.database_password}@{User_and_Database.database_hosting}:3306/{User_and_Database.database_name}")    
            self.init_migration(self)
            return True
        except Exception as err :
            return False


    def Get_Database_Config(self):
        with Session(self.engine) as session:
            query = select(User_of_Database_for_Sqlite)
            try:
                list_of_database_auth = session.scalars(query).one()
                if list_of_database_auth:
                    self._engine = create_engine(f"mysql+pymysql://{list_of_database_auth.database_user}:{list_of_database_auth.database_password}@{list_of_database_auth.database_hosting}:3306/{list_of_database_auth.database_name}")
                    return True
                else:
                    self._engine = None
                    return False
            except Exception as p:
                print(p)
                self._engine = None
                return False