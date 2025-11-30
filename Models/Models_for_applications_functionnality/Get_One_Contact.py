from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.DB.Model_for_databases.circuit import Contact, Contact_Model, Contact_Model_without_Pydantic
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function

def Get_all_Contact(engine,id,callback):
    try:
        with Session(engine) as session:
            contact_list = select(Contact).where(Contact.id == id)
            wide_result = session.execute(contact_list).all()
            usable_value:list[Contact_Model_without_Pydantic] = []
            for element in wide_result:
                usable_value.append(Contact_Model_without_Pydantic(id=element["id"],name=element["name"],subject=element["subject"],body=element["body"],mail=element["mail"],number=element["number"],begining=element["begining"],number_of_person=element["number_of_person"],total_price=element["total_price"]))
            callback(Result_model_function(code=1,data=usable_value,error=""))
    except Exception as Error:
            callback(Result_model_function(code=0,data=[],error=Error))