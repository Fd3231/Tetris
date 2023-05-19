from languages.predicate import Predicate
from languages.asp.symbolic_constant import SymbolicConstant

class Output(Predicate):
    predicate_name="output"

    def __init__(self,col=None,rotation=None):
        Predicate.__init__(self,[("col"),("rotation")])
        self.col = col
        self.rotation = rotation
        
    def get_col(self):
        return self.col
        
    def set_col(self,col):
        self.col = col

    def get_rotation(self):
        return self.rotation

    def set_rotation(self,rotation):
        self.rotation = rotation
        
    def __str__(self):
        return "output(" + str(self.col) + "," + str(self.rotation) +")"