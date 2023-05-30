#from lib.embasp.languages.predicate import Predicate
from languages.predicate import Predicate

class Cell(Predicate):
    predicate_name="cell"

    def __init__(self,row=None,col=None,value=None):
        Predicate.__init__(self,[("row"),("col"),("value")])
        self.row = row
        self.col = col
        self.value = value

    def get_row(self):
        return self.row
        
    def get_col(self):
        return self.col
        
    def get_value(self):
        return self.value
        
    def set_row(self, row):
        self.row = row
        
    def set_col(self,col):
        self.col = col
        
    def set_value(self,value):
        self.value = value
        
    def __str__(self):
        return "cell(" + str(self.row) + "," + str(self.col) + "," + str(self.value) + ")"