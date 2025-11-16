from Models.DB.Model_for_databases.circuit import *
from sqlalchemy.orm import joinedload



class CircuitController:
    def __init__(self,db):
        self.db = db

    def create_circuit(self,data):
        circuit = Circuit(**data)
        self.db.add(circuit)
        self.db.commit()

    def get_all_circuits(self):
        return (self.db.query(Circuit)
            .options(
            joinedload(Circuit.itinerary),
            joinedload(Circuit.equipment),
            joinedload(Circuit.include_in_price),
            joinedload(Circuit.contact)
        ).all())

    def get_circuit_byid(self,circuit_id):

        return (
            self.db.query(Circuit)
            .options(
                joinedload(Circuit.itinerary),
                joinedload(Circuit.equipment),
                joinedload(Circuit.include_in_price),
                joinedload(Circuit.contact)
            )
            .filter(Circuit.id == circuit_id)
            .first()
        )


class ItineraryController:
    def __init__(self,db):
        self.db = db

    def create_itinerary(self,data):
        itinerary = Itinerary(**data)
        self.db.add(itinerary)
        self.db.commit()

    def get_all_itinerary(self):
        return self.db.query(Itinerary).all()

    def get_itinerary_byid(self,itinerary_id):
        return (
            self.db.query(Itinerary).filter(Itinerary.id == itinerary_id)
        )


class EquipmentController:
    def __init__(self,db):
        self.db = db

    def create_equipment(self,data):
        equipements = Equipement(**data)
        self.db.add(equipements)
        self.db.commit()

    def get_all_equipments(self):
        return self.db.query(Equipement).all()

    def get_equipment_byid(self,equipment_id):
        return (
            self.db.query(Equipement).filter(Equipement.id == equipment_id)
        )

class IncludeInPriceController:
    def __init__(self,db):
        self.db = db

    def create_include_in_price(self,data):
        include_in_price = Included_task_in_Price(**data)
        self.db.add(include_in_price)
        self.db.commit()

    def get_all_include_in_price(self):
        return self.db.query(Included_task_in_Price).all()

    def get_include_in_price_byid(self,include_in_price_id):
        return (
            self.db.query(Included_task_in_Price).filter(Included_task_in_Price.id == include_in_price_id)
        )