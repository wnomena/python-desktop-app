from types import SimpleNamespace
from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.DB.Model_for_databases.circuit import Contact, Contact_Model_without_Pydantic
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function, Result_model_function_for_Contact

def Get_all_Contact(engine) -> list[Contact_Model_without_Pydantic]:
    with Session(engine) as session:
        contact_list = select(Contact)
        return [Contact_Model_without_Pydantic(id=element.id,name=element.name,subject=element.subject,body=element.body,mail=element.mail,number=element.number,begining=element.begining,number_of_person=element.number_of_person,total_price=element.total_price,Completed=element.Completed) for element  in session.scalars(contact_list)]
            