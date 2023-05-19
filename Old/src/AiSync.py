from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService
from languages.asp.asp_mapper import ASPMapper
from languages.asp.asp_input_program import ASPInputProgram
from languages.asp.answer_sets import AnswerSets
from Cell import Cell
from CurrentPiece import CurrentPiece
from In import In
from Output import Output


class AiSync:

    file_name = "ai/tetris"
    executable_name = "executable/dlv-2.1.1-windows64.exe"

    def __init__(self):
        self.handler = DesktopHandler(DLV2DesktopService(AiSync.executable_name))
        ASPMapper.get_instance().register_class(Cell)
        ASPMapper.get_instance().register_class(CurrentPiece)
        ASPMapper.get_instance().register_class(In)
        ASPMapper.get_instance().register_class(Output)
        self.fixedProgram = ASPInputProgram()
        self.variableProgram = ASPInputProgram()
        self.fixedProgram.add_files_path(AiSync.file_name)
        self.handler.add_program(self.fixedProgram)
        self.handler.add_program(self.variableProgram)

    def changeVariableProgram(self,matrix,currentPiece):
            for i in range(20):
                    for j in range(10):
                          self.variableProgram.add_object_input(Cell(i,j,matrix[i][j]))
            c = CurrentPiece(currentPiece)
            self.variableProgram.add_object_input(c)

    def execute(self):
        answerSets=self.handler.start_sync()
        for answerSet in answerSets.get_optimal_answer_sets():
                for obj in answerSet.get_atoms():
                      if isinstance(obj,Output):
                            return obj
                      
    def clearVariableProgram(self):
          self.variableProgram.clear_all()