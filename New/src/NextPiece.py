from languages.predicate import Predicate

class NextPiece(Predicate):
    predicate_name="nextpiece"

    def __init__(self,piece=None):
        Predicate.__init__(self,[("piece")])
        self.piece = piece
        
    def get_piece(self):
        return self.piece
        
    def set_piece(self, piece):
        self.piece = piece
        
    def __str__(self):
        return "nextpiece(" + self.piece + ")"