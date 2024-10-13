from injector import inject

from symbiot_lib.objects.gpt_agent import GPTAgent
from symbiot_server.control.agent_builder import AgentBuilder
from symbiot_server.control.services.symbiot_service import SymbiotService


class AgentService(SymbiotService):
    division_name = "client"

    # noinspection PyTypeChecker
    @inject
    def __init__(self,
                 agent_builder: AgentBuilder):
        super().__init__()
        self._builder: AgentBuilder = agent_builder

    def new_agent(self, by: str, content) -> GPTAgent:
        match by:
            case "name": return self._builder.new("gpt", content).get()
