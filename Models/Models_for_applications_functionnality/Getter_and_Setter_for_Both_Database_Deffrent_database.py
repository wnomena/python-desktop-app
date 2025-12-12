from functools import reduce
from types import SimpleNamespace
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from concurrent.futures import ProcessPoolExecutor
from Controller.returned_circuit_manager import Group_element_to_simpllify_render, Reterned_Circuit
from Models.DB.Model_for_databases.circuit import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Contact, Contact_Model_without_Pydantic, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model, User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode
from Models.DB.pool_creation import Mysql_Engine, Sqlite_Engine
from Models.Models_for_applications_functionnality.Get_All_Contact import Get_all_Contact
from Models.Models_for_applications_functionnality.Get_One_Circuit_With_Jointure import Get_One_Circuit_by_Id
from Models.Models_for_applications_functionnality.Get_all_Circuit import Get_ALl_Circuit, Get_all_Model
from Models.Models_for_applications_functionnality.transverse_models import Four_element_from_Circuit_Table, Result_model_function

def Get_All_Tour(engine) -> list[Circuit_Model]:
    with Session(engine) as session:
        data_joined = select(Circuit)
        data:list[Circuit_Model] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data
def Get_All_Contact(engine) -> list[Contact_Model_without_Pydantic]:
    with Session(engine) as session:
        data_joined = select(Contact)
        data:list[Contact_Model_without_Pydantic] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data
def Get_All_Itinerary(engine) -> list[Itinerary_Model]:
    with Session(engine) as session:
        data_joined = select(Itinerary)
        data:list[Itinerary_Model] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data
def Get_All_Adrenaline(engine) -> list[Adrenaline_Model]:
    with Session(engine) as session:
        data_joined = select(Adrenaline)
        data:list[Adrenaline_Model] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data
def Get_All_Equipment(engine) -> list[Equipement_Model]:
    with Session(engine) as session:
        data_joined = select(Equipement)
        data:list[Equipement_Model] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data
def Get_All_Included_In_Price(engine) -> list[Included_task_in_Price_Model]:
    with Session(engine) as session:
        data_joined = select(Included_task_in_Price)
        data:list[Included_task_in_Price_Model] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
        return data

def Insert_All_Tour(engine,data:Circuit_Model) -> bool:
    with Session(engine) as session:
        try:
            session.add(Circuit(title=data.title,subtitle=data.subtitle,description=data.description,duration=data.duration,difficulty=data.difficulty,price=data.price,image=data.image))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False

def Insert_All_Contact(engine,data:Contact_Model_without_Pydantic)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Contact(name=data.name,subject=data.subject,body=data.body,mail=data.mail,number=data.number,begining=data.begining,number_of_person=data.number_of_person,total_price=data.total_price,Completed=data.Completed))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Itinerary(engine,data:Itinerary_Model)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Itinerary(place=data.place,order_id=data.order_id,circuit_id=data.circuit_id))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Adrenaline(engine,data:Adrenaline_Model)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Adrenaline(content=data.content,circuit_id=data.circuit_id))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Equipment(engine,data:Equipement_Model)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Equipement(equipement=data.equipement,circuit_id=data.circuit_id))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Included_In_Price(engine,data:Included_task_in_Price_Model)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Included_task_in_Price(content=data.content,circuit_id=data.circuit_id))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False


class Initialization_instance(Mysql_Engine,Sqlite_Engine):
    def __init__(self):
        super().__init__(self)
        data_to_migrate:Get_all_Model = Get_ALl_Circuit(self._engine)


    def Get_One(self,id:int)  -> list[Reterned_Circuit]:
        list_of_circuit:list[Reterned_Circuit] = []
        data_brute_from_sqlite = Get_One_Circuit_by_Id(self.engine,id).data
        filter_method_to_avoid_repetition_from_jointure = Group_element_to_simpllify_render(data_brute_from_sqlite)
        for element in filter_method_to_avoid_repetition_from_jointure:
            list_of_circuit.append(element)
        return list_of_circuit
    
    def Get_Contacts_from_Sqlite(self) -> Contact_Model_without_Pydantic :
        with Session(self.engine) as session:
            contact_list = select(Contact)
            usable_value:list[Contact_Model_without_Pydantic] = [SimpleNamespace(**element.__dict__) for element  in session.scalars(contact_list)]
            return usable_value

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
        return Get_All_Contact(self._engine)