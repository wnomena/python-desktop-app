from sqlalchemy.orm import Session
from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode
from Models.DB.pool_creation import Sqlite_Engine
from sqlalchemy import select
def Get_Database_Config() -> list[User_of_Database_for_Sqlite_Mode]:
    engine = Sqlite_Engine()
    with Session(engine.engine) as session:
        query = select(User_of_Database_for_Sqlite)
        list_of_database_auth = [User_of_Database_for_Sqlite_Mode(id=element.id,database_hosting=element.database_hosting,database_name=element.database_name,database_password=element.database_password,database_user=element.database_user,database_port=element.database_port) for element in session.scalars(query)]
        if len(list_of_database_auth) > 0:
            return list_of_database_auth
        else:
            return []