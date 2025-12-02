from sqlalchemy.orm import Session
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode
from Models.DB.pool_creation import Sqlite_Engine
from sqlalchemy import select

from Models.Models_for_applications_functionnality.transverse_models import Result_model_function_Sqlite
def Get_Database_Config() -> Result_model_function_Sqlite:
    engine = Sqlite_Engine()
    with Session(engine.engine) as session:
        query = select(User_of_Database_for_Sqlite)
        list_of_database_auth = [element.__dict__ for element in session.scalars(query)]
        if len(list_of_database_auth) > 0:
            return Result_model_function_Sqlite(code=1,error="",data=User_of_Database_for_Sqlite_Mode(id=list_of_database_auth[0]["id"],database_name=list_of_database_auth[0]["database_name"],database_password=list_of_database_auth[0]["database_password"],database_user=list_of_database_auth[0]["database_user"],database_port=list_of_database_auth[0]["database_port"],))
        else:
            return Result_model_function_Sqlite(code=0,error="Database Empty",data=[])