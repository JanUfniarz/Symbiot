from client_division.gpt.gpt_client import GPTClient
from tool_kits.tool_kit import ToolKit


# intended for the calibrator
class NordStarExtractor(ToolKit):
    def __init__(self, name_generator: GPTClient):
        super().__init__()
        self.name_generator = name_generator

    @ToolKit.tool_function(
        """
        This function manage the brief of conversation.
        When you are sure you asked all questions you need to, call this function.
        call it only if you are sure you have all data to start making project
        """,
        parameters=[dict(
            name="nord_star",
            type="string",
            description=
            """
            This is a summary of the dialogue. Convey here what exactly the user 
            wants to achieve with all the details, 
            so that based on this summary developers can start working on the project
            """)])
    def extract_nord_star(self, nord_star: str):
        name = self.name_generator.chat(nord_star)
        self.mediator("client").calibration_ended(nord_star, name)
