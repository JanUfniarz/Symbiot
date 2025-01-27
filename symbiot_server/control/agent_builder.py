import copy

from injector import inject

from symbiot_lib.objects.gpt_agent import GPTAgent
from symbiot_lib.objects.step_record import StepRecord
from symbiot_lib.tool_kits.nord_star_extractor import NordStarExtractor
from symbiot_lib.tool_kits.tool_kit import ToolKit
from symbiot_server.control.agent_factory import AgentFactory


def agent_required(method):
    def wrapper(self, *args, **kwargs):
        if not self._agent:
            raise Exception("No agent, "
                            "use new() or existing() first")
        return method(self, *args, **kwargs)

    return wrapper


class AgentBuilder:

    @inject
    def __init__(self, factory: AgentFactory):
        self._agent: GPTAgent | None = None
        self._factory: AgentFactory = factory

    def existing(self, agent: GPTAgent):
        self._agent = agent
        return self

    # noinspection PyTypeChecker
    def new(self, type_: str, template: str = None):
        if type_ == "gpt":
            if template:
                self._agent = self._factory.gpt(template)
                match template:

                    case "calibrator":
                        agent = copy.copy(self._agent)
                        extractor = NordStarExtractor(self)
                        self._agent = agent
                        self.add_access(extractor)

            else:
                self._agent = GPTAgent()
        return self

    @agent_required
    def get(self) -> GPTAgent:
        return self._agent

    @agent_required
    def add_step(self, step: StepRecord):
        messages = []
        for el in list(map(lambda entry: entry.split(
                "<@time>")[1],
                           step.body.split("<@entry>")[1:])):
            messages.append(dict(
                role="user",
                content=el.split("<@res>")[0]))
            messages.append(dict(
                role="assistant",
                content=el.split("<@res>")[1]))
        self._agent.messages += messages
        return self

    @agent_required
    def add_access(self, tool_kit: ToolKit):
        self._agent.functions = tool_kit.access
        self._agent.function_call = tool_kit.forced \
            if tool_kit.forced == "auto" \
            or tool_kit.forced == "none" \
            else {"name": tool_kit.forced}
        self._agent.tool_kit = tool_kit
        return self

    @agent_required
    def set_params(self, model: str = None,
                   temperature: float = None,
                   n: int = None,
                   max_tokens: int = None):
        if model is not None:
            self._agent.model = model
        if temperature:
            self._agent.temperature = temperature
        if n is not None:
            self._agent.n = n
        if max_tokens is not None:
            self._agent.max_tokens = max_tokens
        return self

    @agent_required
    def add_sys_prompt(self, prompt: str):
        self._agent.messages.append(dict(
            role="system",
            content=prompt))
        return self
