from concurrent.futures import ProcessPoolExecutor
from Models.DB.pool_creation import Mysql_Engine, Sqlite_Engine
from Models.Models_for_applications_functionnality.Get_all_circuits import Get_all_Circuit

def Get_All_Tour(engine):
    
    pass
def Get_All_Contact(engine):
    pass
def Get_All_Itinerary(engine):
    pass
def Get_All_Adrenaline(engine):
    pass
def Get_All_Equipment(engine):
    pass
def Get_All_Included_In_Price(engine):
    pass

def Insert_All_Tour(engine):
    pass
def Insert_All_Contact(engine):
    pass
def Insert_All_Itinerary(engine):
    pass
def Insert_All_Adrenaline(engine):
    pass
def Insert_All_Equipment(engine):
    pass
def Insert_All_Included_In_Price(engine):
    pass


class Initialization_instance(Mysql_Engine,Sqlite_Engine):
    def __init__(self):
        super().__init__(self)
        with ProcessPoolExecutor() as executor:
            pass


class Get_Value(Sqlite_Engine):
    def __init__(self):
        super().__init__(self)
    def Get(self):
        if self.engine:
            return Get_all_Circuit(engine=self.engine)