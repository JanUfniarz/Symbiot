from client_division.gpt.gpt_client import GPTClient
from tool_kits.tool_kit import ToolKit


class NordStarExtractor(ToolKit):

    EXTRACT_NORD_STAR_DESCRIPTION = """
    This function manage the brief of conversation.
    When you are sure you asked all questions you need to, call this function.
    call it only if you are sure you have all data to start making project
    """

    NORD_STAR_DESCRIPTION = """
    This is a summary of the dialogue. 
    Convey here what exactly the user wants to achieve with all the details, 
    so that based on this summary developers can start working on the project
    """

    NAME_GENERATOR_PROMPT = """
    You will be given description of requirements for a program or script.
    Your role is to generate name for this program
    """

    def __init__(self, builder):
        super().__init__()

        self.name_generator: GPTClient = builder.new("gpt", "one_value_generator") \
            .add_sys_prompt(self.NAME_GENERATOR_PROMPT).get()

    @ToolKit.tool_function(EXTRACT_NORD_STAR_DESCRIPTION,
                           parameters=[dict(
                               name="nord_star",
                               type="string",
                               description=NORD_STAR_DESCRIPTION)])
    def extract_nord_star(self, nord_star: str):
        self.mediator("client").calibration_ended(
            nord_star,
            self.name_generator.chat(nord_star))
