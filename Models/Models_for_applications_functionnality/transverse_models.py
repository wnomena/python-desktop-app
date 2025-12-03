from Controller.returned_circuit_manager import Reterned_Circuit
from Models.Models_for_applications_functionnality.transverse_models import Result_model_function_Sqlite
class Result_model_function:
    def __init__(self,code:int,data:list[Reterned_Circuit],error:str):
        self.code = code
        self.data = data
        self.error = error

class Result_model_function_Sqlite:
    def __init__(self,code:int,data:list[Result_model_function_Sqlite],error:str):
        self.code = code
        self.data = data
        self.error = error

