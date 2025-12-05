from types import SimpleNamespace
from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.DB.Model_for_databases.circuit import Contact, Contact_Model_without_Pydantic
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function, Result_model_function_for_Contact

def Get_all_Contact(engine) -> Result_model_function_for_Contact:
    try:
        with Session(engine) as session:
            contact_list = select(Contact)
            usable_value:list[Contact_Model_without_Pydantic] = [SimpleNamespace(**element.__dict__) for element  in session.scalars(contact_list)]
            Result_model_function(code=1,data=usable_value,error="")
    except Exception as Error:
            Result_model_function(code=0,data=[],error=Error)