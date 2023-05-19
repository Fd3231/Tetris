from languages.predicate import Predicate
from languages.asp.symbolic_constant import SymbolicConstant

class In(Predicate):
    predicate_name="in"

    def __init__(self,row=None,col=None,piece=None,rotation=None):
        Predicate.__init__(self,[("row"),("col"),("piece"),("rotation")])
        self.row = row
        self.col = col
        self.piece = piece
        self.rotation = rotation

    def get_row(self):
        return self.row
        
    def get_col(self):
        return self.col
        
    def get_piece(self):
        return self.piece
        
    def set_row(self, row):
        self.row = row
        
    def set_col(self,col):
        self.col = col
        
    def set_piece(self,piece):
        self.piece = piece

    def get_rotation(self):
        return self.rotation

    def set_rotation(self,rotation):
        self.rotation = rotation
        
    def __str__(self):
        return "in(" + str(self.row) + "," + str(self.col) + "," + str(self.piece) + str(self.rotation) +")"