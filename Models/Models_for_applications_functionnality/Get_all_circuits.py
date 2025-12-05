
from types import SimpleNamespace
from sqlalchemy import select
from sqlalchemy.orm import Session

from Models.DB.Model_for_databases.circuit import  Circuit
from Models.Models_for_applications_functionnality.transverse_models import Four_element_from_Circuit_Table, Result_model_function, Result_model_function_for_table
def Get_all_Circuit_from_Sqlite(engine):
    with Session(engine) as session:
        try:
            data_joined = select(Circuit.id,Circuit.title,Circuit.subtitle,Circuit.price)
            data:list[Four_element_from_Circuit_Table] = [SimpleNamespace(**element.__dict__ ) for element in session.scalars(data_joined)]
            return Result_model_function_for_table(code=1,data=data,error="")
        except Exception as Error:
            return Result_model_function_for_table(code=0,data=[],error=Error) 