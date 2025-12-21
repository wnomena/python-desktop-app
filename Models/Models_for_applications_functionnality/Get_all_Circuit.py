from sqlalchemy.orm import Session
from sqlalchemy import select

from Controller.returned_circuit_manager import Reterned_Circuit
from Models.DB.Model_for_databases.circuit import Adrenaline, Adrenaline_Model, Circuit, Circuit_Model, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function
class Get_all_Model:
    def __init__(self,circuit:list[Circuit_Model] | None,itinerary:list[Itinerary_Model] | None,equipement:list[Equipement_Model] | None,Included:list[Included_task_in_Price_Model] | None,Adrenaline:list[Adrenaline_Model] | None):
        self.circuit = circuit
        self.itinerary = itinerary
        self.equipment = equipement
        self.included = Included
        self.adrenaline = Adrenaline
        
    def insert_circuit(self,circuit:Circuit_Model):
        for element in self.circuit:
            if element.id == circuit.id:
                return False
        self.circuit.append(circuit)
        return True
    
    def insert_itinerary(self,itinerary:Itinerary_Model):
        for element in self.itinerary:
            if element.id == itinerary.id:
                return False
        self.itinerary.append(itinerary)
        return True

    def insert_equipment(self,equipment:Equipement_Model):
        for element in self.equipment:
            if element.id == equipment.id:
                return False
        self.equipment.append(equipment)
        return True
    
    def insert_included(self,included:Included_task_in_Price_Model):
        for element in self.included:
            if element.id == included.id:
                return False
        self.included.append(included)
        return True
    
    def insert_adrenaline(self,adrenaline:Adrenaline_Model):
        for element in self.adrenaline:
            if element.id == adrenaline.id:
                return False
        self.adrenaline.append(adrenaline)
        return True
    
def Get_ALl_Circuit(engine) -> Get_all_Model:
    data_to_returned: Get_all_Model = None
    with Session(engine) as session:
        data_joined = select(Circuit,Itinerary,Equipement,Included_task_in_Price,Adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price).outerjoin(Circuit.adrenaline)
        data = session.execute(data_joined)
        for a,b,c,d,e in data:
            circuit_dict = a.__dict__
            data_to_returned.insert_circuit(Circuit_Model(id=circuit_dict["id"],title=circuit_dict["title"],subtitle=circuit_dict["subtitle"],description=circuit_dict["description"],duration=circuit_dict["duration"],difficulty=circuit_dict["difficulty"],price=circuit_dict["price"],image=circuit_dict["image"]))
            itinerary_dict = b.__dict__
            data_to_returned.insert_itinerary(Itinerary_Model(id=itinerary_dict["id"],place=itinerary_dict["place"],order_id=itinerary_dict["order_id"],circuit_id=itinerary_dict["circuit_id"]))
            equipment_dict = c.__dict__
            data_to_returned.insert_equipment(Equipement_Model(id=equipment_dict["id"],equipment=equipment_dict["equipment"],circuit_id=equipment_dict["circuit_id"]))
            Included = d.__dict__
            data_to_returned.insert_included(Included_task_in_Price_Model(id=Included["id"],content=Included["content"],circuit_id=Included["circuit_id"]))
            Adrenaline_dict = e.__dict__
            data_to_returned.insert_adrenaline(Adrenaline_Model(id=Adrenaline_dict["id"],content=Adrenaline_dict["content"],circuit_id=Adrenaline_dict["circuit_id"]))             
        print(data_to_returned)
        return data_to_returned