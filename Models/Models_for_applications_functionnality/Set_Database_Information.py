from sqlalchemy import Engine, insert
from PySide6.QtCore import Slot

from Models.DB.Model_for_databases.circuit import User_of_Database_for_Sqlite, User_of_Database_for_Sqlite_Mode

@Slot()
def Insert_Database_Information(engine:Engine,User_and_Database:User_of_Database_for_Sqlite):
    try:
        with engine.connect() as conn:
            conn.execute(insert(User_of_Database_for_Sqlite).values(User_and_Database))
            conn.commit()
            return True
    except Exception as err :
        return False