
"""
from lib.embasp.platforms.desktop.desktop_handler import DesktopHandler
from lib.embasp.specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from lib.embasp.languages.asp.asp_mapper import ASPMapper
from lib.embasp.languages.asp.asp_input_program import ASPInputProgram
from lib.embasp.languages.asp.asp_filter_option import OptionDescriptor
from lib.embasp.base.callback import Callback
"""
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
from NextPiece import NextPiece
import platform


class AiHandler():

    file_name1 = "ai/tetris2.asp"
    file_name2 = "ai/tetris1.asp"
    to_execute = file_name1
    mappings = "ai/mappings.asp"
    if platform.system() == "Darwin":
        executable_name = "executable/dlv-2.1.1-macos"
    if platform.system() == "Windows":
        executable_name = "executable/dlv-2.1.1-windows64.exe"
    #executable_name = "executable/dlv-2.1.1-linux-x86_64"

    def __init__(self):
        self.handler = DesktopHandler(DLV2DesktopService(AiHandler.executable_name))
        ASPMapper.get_instance().register_class(Cell)
        ASPMapper.get_instance().register_class(CurrentPiece)
        ASPMapper.get_instance().register_class(In)
        ASPMapper.get_instance().register_class(Output)
        ASPMapper.get_instance().register_class(NextPiece)
        self.fixedProgram = ASPInputProgram()
        self.variableProgram = ASPInputProgram()
        self.handler.add_program(self.fixedProgram)
        self.handler.add_program(self.variableProgram)
        self.fixedProgram.add_files_path(AiHandler.mappings)
        o = OptionDescriptor("--filter=output/2")
        self.handler.add_option(o)

    def changeVariableProgram(self,matrix,currentPiece,nextPiece):
        for i in range(20):
            for j in range(10):
                self.variableProgram.add_object_input(Cell(i,j,matrix[i][j]))
        c = CurrentPiece(currentPiece)
        if nextPiece != None:
            AiHandler.to_execute = AiHandler.file_name1
            n = NextPiece(nextPiece)
            self.variableProgram.add_object_input(n)
        else:
            AiHandler.to_execute = AiHandler.file_name2
        self.variableProgram.add_files_path(AiHandler.to_execute)
        self.variableProgram.add_object_input(c)


    def execute(self,mainBoard):
        c = MyCallback(mainBoard)
        return self.handler.start_async(c)
                      
    def clearVariableProgram(self):
        self.variableProgram.clear_all()
                
class MyCallback(Callback):
    def __init__(self,mainBoard):
        self.mainBoard = mainBoard
        self.piece = mainBoard.getCurrentPiece()
      
    def callback(self,answerSets):
        for answerSet in answerSets.get_optimal_answer_sets():
            for obj in answerSet.get_atoms():
                if isinstance(obj,Output) and self.mainBoard.getCurrentPiece()==self.piece:
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
                        
