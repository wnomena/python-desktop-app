from functools import reduce
from types import SimpleNamespace
from sqlalchemy import select
from sqlalchemy.orm import Session
from concurrent.futures import ProcessPoolExecutor
from Models.DB.Model_for_databases.circuit import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Contact, Contact_Model_without_Pydantic, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model
from Models.DB.pool_creation import Mysql_Engine, Sqlite_Engine
from Models.Models_for_applications_functionnality.Get_all_circuits import Get_all_Circuit

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
            session.add(Circuit(title=data.title,subtitle=data.subtitle,description=data.description,duration=data.duration,difficulty=data.difficulty,price=data.price,image=data.price,image=data.image))
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False

def Insert_All_Contact(engine,data:Contact_Model_without_Pydantic)  -> bool :
    with Session(engine) as session:
        try:
            session.add(Contact(name=data.name,subject=data.subject,body=data.body,mail=data.mail,number=data.number,begining=data.begining,number_of_person=data.number_of_person,total_price=data.total_price))
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
        with ProcessPoolExecutor() as executor:
            pass
    def Circuit_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Tour(self._engine)
        for element in mysql_data:
            temp = Insert_All_Tour(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    def Contact_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Contact(self._engine)
        for element in mysql_data:
            temp = Insert_All_Contact(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    def Itinerary_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Itinerary(self._engine)
        for element in mysql_data:
            temp = Insert_All_Itinerary(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    def Equipement_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Equipment(self._engine)
        for element in mysql_data:
            temp = Insert_All_Equipment(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    def Adrenaline_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Adrenaline(self._engine)
        for element in mysql_data:
            temp = Insert_All_Adrenaline(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    def Include_In_Price_Migration(self):
        BoolList:list[bool] = None
        mysql_data = Get_All_Included_In_Price(self._engine)
        for element in mysql_data:
            temp = Insert_All_Included_In_Price(self.engine,element)
            BoolList.append(temp)
        return reduce(lambda x,y : x or y,BoolList)
    

class Get_Value(Sqlite_Engine):
    def __init__(self):
        super().__init__(self)
    def Get(self):
        if self.engine:
            return Get_all_Circuit(engine=self.engine)