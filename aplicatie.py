# creaza un program de tip calculator, care sa retina retete de prajituri in format json,unde sa poti adauga retete noi, sa calculeze necesarul de materie prima si sa-mi rezulte un pdf ca si necesar.

from abc import ABC

class Retetar(ABC):
    def __init__(self)->None:
        self.retetar={}

    def adauga_reteta_noua(self,ingredient:str,cantitate:int):
        self.retetar[ingredient]=cantitate
        
        