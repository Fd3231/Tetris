from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from languages.asp.asp_mapper import ASPMapper
from languages.asp.asp_input_program import ASPInputProgram
from languages.asp.asp_filter_option import OptionDescriptor
from base.callback import Callback
from Cell import Cell
from CurrentPiece import CurrentPiece
from In import In
from Output import Output


class AiAsync():

    file_name = "ai/affidabile"
    executable_name = "executable/dlv-2.1.1-windows64.exe"
    #executable_name = "executable/dlv-2.1.1-linux-x86_64"

    def __init__(self):
        self.handler = DesktopHandler(DLV2DesktopService(AiAsync.executable_name))
        ASPMapper.get_instance().register_class(Cell)
        ASPMapper.get_instance().register_class(CurrentPiece)
        ASPMapper.get_instance().register_class(In)
        ASPMapper.get_instance().register_class(Output)
        self.fixedProgram = ASPInputProgram()
        self.variableProgram = ASPInputProgram()
        self.fixedProgram.add_files_path(AiAsync.file_name)
        self.handler.add_program(self.fixedProgram)
        self.handler.add_program(self.variableProgram)
        o = OptionDescriptor("--filter=output/2")
        self.handler.add_option(o)

    def changeVariableProgram(self,matrix,currentPiece):
            for i in range(20):
                    for j in range(10):
                          self.variableProgram.add_object_input(Cell(i,j,matrix[i][j]))
            c = CurrentPiece(currentPiece)
            self.variableProgram.add_object_input(c)

    def execute(self,mainBoard):
        c = MyCallback(mainBoard)
        return self.handler.start_async(c)
                      
    def clearVariableProgram(self):
          self.variableProgram.clear_all()
                
class MyCallback(Callback):
    def __init__(self,mainBoard):
        self.mainBoard = mainBoard
      
    def callback(self,answerSets):
        for answerSet in answerSets.get_optimal_answer_sets():
                for obj in answerSet.get_atoms():
                      if isinstance(obj,Output):
                            minCol = self.mainBoard.rotate(int(obj.get_rotation()))
                            if self.mainBoard.getCurrentPiece() == "o":
                                minCol = 4
                            col = int(obj.get_col())
                            n = col - minCol
                            if n>0:
                                self.mainBoard.move(True,False,n)
                            elif n<0:
                                self.mainBoard.move(False,True,abs(n))
                            self.mainBoard.drop()
