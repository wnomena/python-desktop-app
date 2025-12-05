from sqlalchemy.orm import Session
from sqlalchemy import select

from Controller.returned_circuit_manager import Reterned_Circuit
from Models.DB.Model_for_databases.circuit import Adrenaline, Adrenaline_Model, Circuit, Equipement, Equipement_Model, Included_task_in_Price, Included_task_in_Price_Model, Itinerary, Itinerary_Model
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function
def Get_One_Circuit_by_Id(engine,id) -> Result_model_function:
    with Session(engine) as session:
        try:
            data_joined = select(Circuit,Itinerary,Equipement,Included_task_in_Price,Adrenaline).outerjoin(Circuit.itinerary).outerjoin(Circuit.equipment_needed).outerjoin(Circuit.included_in_price).outerjoin(Circuit.adrenaline).where(Circuit.id == id)
            data = session.execute(data_joined).all()
            final_value_to_return:list[Reterned_Circuit] = []
            for a,b,c,d,e in data:
                ciruit =  a.__dict__
                itinarary = b.__dict__
                equipement = c.__dict__
                included = d.__dict__
                adrenaline = e.__dict__
                final_value_to_return.append(Reterned_Circuit(id=ciruit["id"],title=ciruit["title"],subtitle=ciruit["subtitle"],description=ciruit["description"],duration=ciruit["duration"],difficulty=ciruit["difficulty"],price=ciruit["price"],image=ciruit["image"],itinerary = [Itinerary_Model(id=itinarary["id"],place=itinarary["place"],order_id=itinarary["order_id"],circuit_id=itinarary["circuit_id"])],equipment = [Equipement_Model(id=equipement["id"],equipment=equipement["equipment"],circuit_id=equipement["circuit_id"])],include_in_price = [Included_task_in_Price_Model(id=included["id"],content=included["content"],circuit_id=included["circuit_id"])],adrenaline=[Adrenaline_Model(id=adrenaline["id"],content=adrenaline["content"],circuit_id=adrenaline["circuit_id"])]))
            return Result_model_function(code=1,data=final_value_to_return,error="")
        except Exception as Error:
            return Result_model_function(code=0,data=[],error=Error)