from sqlalchemy.orm import Session
from Models.DB.Model_for_databases.circuit import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Contact, Contact_Model_without_Pydantic, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model
def Insert_All_Tour(engine,data1:list[Circuit_Model]) -> bool:
    with Session(engine) as session:
        try:
            session.add_all([Circuit(title=data.title,subtitle=data.subtitle,description=data.description,duration=data.duration,difficulty=data.difficulty,price=data.price,image=data.image) for data in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False

def Insert_All_Contact(engine,data1:list[Contact_Model_without_Pydantic])  -> bool :
    with Session(engine) as session:
        try:
            session.add_all([Contact(name=data.name,subject=data.subject,body=data.body,mail=data.mail,number=data.number,begining=data.begining,number_of_person=data.number_of_person,total_price=data.total_price,Completed=data.Completed) for data in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Itinerary(engine,data1:list[Itinerary_Model])  -> bool :
    with Session(engine) as session:
        try:
            session.add_all([Itinerary(place=data.place,order_id=data.order_id,circuit_id=data.circuit_id) for data  in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Adrenaline(engine,data1:list[Adrenaline_Model])  -> bool :
    with Session(engine) as session:
        try:
            session.add_all([Adrenaline(content=data.content,circuit_id=data.circuit_id) for data  in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Equipment(engine,data1:list[Equipement_Model])  -> bool :
    with Session(engine) as session:
        try:
            session.add_all([Equipement(equipement=data.equipement,circuit_id=data.circuit_id) for data in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False
def Insert_All_Included_In_Price(engine,data1:list[Included_task_in_Price_Model])  -> bool :
    with Session(engine) as session:
        try:
            session.add_all([Included_task_in_Price(content=data.content,circuit_id=data.circuit_id) for data in data1])
            session.commit()
            return True
        except Exception as Error:
            print(Error)
            return False

