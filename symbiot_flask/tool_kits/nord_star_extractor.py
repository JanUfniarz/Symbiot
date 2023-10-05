from tool_kits.tool_kit import ToolKit


# TODO: move it to accurate directory
# intended for the calibrator
class NordStarExtractor(ToolKit):
    def __init__(self):
        super().__init__()

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
        self.mediator("client").calibration_ended(nord_star)
