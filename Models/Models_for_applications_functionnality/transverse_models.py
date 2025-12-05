from Controller.returned_circuit_manager import Reterned_Circuit
class Result_model_function:
    def __init__(self,code:int,data:list[Reterned_Circuit],error:str):
        self.code = code
        self.data = data
        self.error = error

class Four_element_from_Circuit_Table:
    def __init__(self,id:int,title:str,subtitle:str,price:int):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.price = price
class Result_model_function_for_table:
    def __init__(self,code:int,data:list[Four_element_from_Circuit_Table],error:str):
        self.code = code
        self.data = data
        self.error = error

